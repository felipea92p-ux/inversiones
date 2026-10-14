# -*- coding: utf-8 -*-
"""Portada · Resumen · §1 el negocio · §2 la historia"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, kpi_panel, S, C, cm
from reportlab.platypus import Spacer, PageBreak, NextPageTemplate, Paragraph, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER

def portada():
    t_emp = ParagraphStyle("te", fontName="Serif-B", fontSize=40, leading=44, textColor=C["tinta"])
    t_tag = ParagraphStyle("tg", fontName="Serif-I", fontSize=13.5, leading=19, textColor=C["gris"])
    t_sec = ParagraphStyle("ts", fontName="Sans-B", fontSize=9, leading=12, textColor=C["rojo"])
    return [
        Spacer(1, 7.0*cm),
        Paragraph("BOLSAS Y MERCADOS · INFRAESTRUCTURA FINANCIERA · ESTADOS UNIDOS", t_sec),
        Spacer(1, 10),
        Paragraph("CME Group", t_emp),
        Spacer(1, 6),
        Paragraph("El peaje que no puede subir su tarifa", t_tag),
        Spacer(1, 4),
        Paragraph("Un negocio extraordinario, un precio exacto y una pregunta que no es la que "
                  "parece: no <i>cuánto vale</i>, sino <i>cuánto riesgo corres tú</i> al tenerlo.", t_tag),
        Spacer(1, 1.7*cm),
        kpi_panel([("64,9%", "MARGEN DE EXPLOTACIÓN", "de cada 100 dólares que factura,<br/>casi 65 le sobran"),
                   ("1,28%", "LO QUE REINVIERTE", "capex sobre ventas: no necesita<br/>capital para funcionar"),
                   ("−2,9%", "MARGEN DE SEGURIDAD", "el precio de hoy está por encima<br/>de lo que vale para tu cartera")]),
        Spacer(1, 1.1*cm),
        tabla([["FECHA", "PRECIO (dato vivo)", "VEREDICTO", "HORIZONTE"],
               ["22 de agosto de 2026", "275,03 US$", "NO COMPRAR TODAVÍA", "10 años o más"]],
              [4.15*cm]*4, font_sz=9),
        Spacer(1, 0.5*cm),
        M.p("<font size=8.4 color='#666054'><i>Documento de trabajo personal. Elaborado con 24 agentes de "
            "investigación sobre fuente primaria: 5,81 millones de tokens, 1.385 consultas a registros de la SEC, "
            "la CFTC, el Tesoro de EE.UU. y los tribunales federales. No es asesoramiento de inversión.</i></font>"),
        NextPageTemplate("Normal"), PageBreak()]

def resumen():
    o = flag_titulo("El resumen en treinta segundos", "Si sólo lees una página, que sea ésta")
    o += [p("<b>CME Group es la mayor bolsa de derivados del mundo, y es un negocio extraordinario.</b> "
        "De cada 100 dólares que ingresa, casi 65 le sobran después de pagarlo todo. Necesita tan poco dinero "
        "para funcionar que gasta en mantenimiento menos de lo que sus equipos se deprecian. Y tiene un foso "
        "competitivo real: dos rivales con dinero ilimitado lo atacaron de frente, en 2004 y en 2009, y los dos "
        "murieron en el intento.")]
    o += [p("<b>Y aun así, la respuesta es no comprar hoy.</b> No porque el negocio esté roto — está impecable — "
        "sino por tres cosas que este documento demuestra con datos, no con opiniones.")]
    o += [p("<b>Primero: no crece por sí mismo.</b> El crecimiento de CME viene de que se negocian más contratos, "
        "y eso depende de la volatilidad del mundo, del tamaño de la deuda estadounidense y del nivel de los tipos "
        "de interés. Ninguna de las tres cosas la controla CME. Su propio dinero reinvertido explica <b>cero</b> "
        "del crecimiento. Y desde 2007 el beneficio por acción creció tres puntos anuales menos que el beneficio "
        "total, porque emitió acciones nuevas para pagar sus compras.")]
    o += [p("<b>Segundo: no es indestructible.</b> El 52,6% de su foso vive en las opciones, y ahí un rival —Cboe— "
        "pasó del 58% al 74% de cuota en cinco años y le igualó el margen en cuatro. El foso de CME defiende bien "
        "la plaza que le atacan de frente, y no defiende nada del flanco.")]
    o += [p("<b>Tercero, y es lo que decide: el precio ya está bien puesto.</b> Cuatro métodos de valoración "
        "independientes —flujos descontados, múltiplos de beneficio, valor de empresa y rentabilidad total— "
        "convergen entre 259 y 276 dólares. El precio de hoy es 275,03. No está cara ni barata: está en su sitio.")]
    o += [callout("EN ROMÁN PALADINO",
        "«Margen de seguridad» es la diferencia entre lo que algo vale y lo que cuesta. Si vale 100 y cuesta 70, "
        "tienes un 30% de margen: puedes equivocarte bastante y aún así no perder dinero. <b>En CME ese margen "
        "hoy es de aproximadamente −3%.</b> No hay colchón. Y sin colchón, cualquier error de análisis lo paga "
        "entero tu bolsillo.")]
    o += [p("<b>Lo que sí ha cambiado, y mucho, es el precio al que sí.</b> Los dos análisis anteriores de este "
        "archivo pedían un descuento del 40%, lo que ponía la entrada en 165-185 dólares — un nivel que CME no "
        "ha visto desde 2017. Con el criterio revisado el 21 de agosto de 2026, la zona de compra sube a "
        "<b>235 dólares para un primer tramo y 200 para una posición completa</b>. Y eso tiene una consecuencia "
        "incómoda: <b>el 29 de junio de 2026 CME cotizó a 218,31 dólares</b>. Estuvo comprable durante seis "
        "sesiones y nadie miró.")]
    o += [hr(), p("<b>Las tres cifras que hay que retener:</b>")]
    o += [tabla([
        ["LA CIFRA", "QUÉ SIGNIFICA"],
        ["<b>42% frente a 0,37%</b>",
         "La misma empresa rival (FMX), con la misma tecnología y los mismos diez bancos detrás, compite contra CME "
         "en dos mercados vecinos. Donde CME tiene foso saca un 0,37%. Donde no lo tiene, un 42%. "
         "<b>Ésa es la anchura exacta del foso, y la mide el atacante, no CME.</b>"],
        ["<b>0,6148 → 0,5990 dólares</b>",
         "Lo que CME gana de beneficio por cada contrato que pasa por su casa: en 2009 y en 2025. Plano en dólares "
         "corrientes, es decir <b>un 35% menos en poder adquisitivo real</b>. Un peaje que no puede subir su tarifa "
         "en dieciséis años no merece el múltiplo de un peaje que sí puede."],
        ["<b>4,06% frente a 4,74%</b>",
         "Lo que rinde CME sobre su beneficio normalizado, frente a lo que paga el bono del Tesoro de EE.UU. a diez "
         "años. <b>El accionista cobra 68 puntos básicos MENOS que quien no corre ningún riesgo.</b> Todo lo que "
         "gane por encima tiene que venir del crecimiento futuro."]],
        [3.9*cm, 12.7*cm], font_sz=8.8)]
    o += [callout("PAUSA REFLEXIVA",
        "Antes de seguir, una pregunta honesta: si te dijeran que existe un negocio con un 65% de margen, sin "
        "necesidad de invertir, con un monopolio de hecho probado en tribunales y dos siglos de historia... "
        "¿a qué precio sería <b>mala</b> idea comprarlo? Esa pregunta —y no «¿es buena la empresa?»— es la que "
        "decide este documento. La calidad del negocio y el acierto de la inversión son dos cosas distintas, y "
        "confundirlas es la forma más cara de perder dinero con empresas excelentes.")]
    return o + [PageBreak()]

def s1_negocio():
    o = flag_titulo("1 · Qué hace CME, explicado desde cero",
                    "El negocio entero cabe en una frase: cobra un peaje diminuto cada vez que alguien traslada un riesgo")
    o += [p("Imagina un agricultor de Illinois en marzo. Va a cosechar maíz en septiembre y no sabe a qué precio "
        "podrá venderlo. Puede que suba y gane una fortuna, o puede que baje y arruine el año. Al otro lado del "
        "país, una fábrica de cereales para el desayuno tiene el problema exacto opuesto: necesita maíz en "
        "septiembre y le aterra que el precio suba.")]
    o += [p("Los dos quieren lo mismo: <b>certidumbre</b>. Así que firman un acuerdo hoy para intercambiar maíz "
        "en septiembre a un precio fijado ahora. Eso es un <b>futuro</b> (un contrato que obliga a comprar o vender "
        "algo en una fecha futura a un precio acordado hoy). El agricultor duerme tranquilo, la fábrica también, "
        "y ninguno de los dos depende ya de la suerte.")]
    o += [p("Falta un problema, y es <i>el</i> problema: <b>¿y si en septiembre uno de los dos no cumple?</b> Si el "
        "maíz se ha desplomado, la fábrica tiene un incentivo enorme para desaparecer. Si se ha disparado, lo tiene "
        "el agricultor. Un contrato entre dos desconocidos que se firma hoy y se cumple dentro de seis meses vale "
        "exactamente lo que valga la honradez del que peor lo esté pasando.")]
    o += [p("<b>Ahí es donde entra CME, y ése es todo el negocio.</b> CME se coloca en medio de los dos y se "
        "convierte en la contraparte de ambos: le compra al agricultor y le vende a la fábrica. Ninguno de los dos "
        "tiene que confiar en el otro — sólo en CME. A cambio, les cobra a cada uno unos céntimos.")]
    o += [callout("LA METÁFORA",
        "CME no es un mercado: es <b>la cámara de compensación</b> (la institución que se interpone entre comprador "
        "y vendedor y garantiza a ambos). Funciona como la sala de fianzas de un tribunal. Las dos partes depositan "
        "dinero antes de empezar; la casa lo custodia; y si alguien incumple, la casa paga y persigue al moroso. "
        "El servicio no es juntar a las partes — eso lo hace cualquiera. <b>El servicio es que nadie tenga que "
        "fiarse de nadie.</b>")]
    o += [p("<b>Cómo cobra, exactamente.</b> La unidad de cobro se llama <i>round turn</i> («vuelta completa»): un "
        "contrato abierto y luego cerrado. Un billete de ida y vuelta. CME no cobra por el tamaño de lo que "
        "aseguras, ni por cuánto tiempo lo tienes, ni una cuota de socio: <b>cobra por pieza</b>. Y ese detalle, "
        "que parece técnico, es la mitad de esta tesis.")]
    o += [chart("charts/01_peaje.png")]
    o += [p("Fíjate en la asimetría del gráfico: su producto más voluminoso —los futuros sobre tipos de interés, "
        "14,5 millones de contratos diarios— es también el más barato, a 48 céntimos. Y por un contrato agrícola, "
        "del que apenas mueve 2 millones, cobra 1,43 dólares: <b>casi tres veces más</b>. La razón es simple: en "
        "tipos compite contra bancos gigantes que negocian sus tarifas; en maíz y ganado no compite con nadie.")]
    o += [p("<b>Las otras dos patas del negocio.</b> Además de las comisiones (el 79% de lo que ingresa), CME "
        "tiene dos fuentes más:")]
    o += [tabla([
        ["PATA", "QUÉ ES", "2T-2026", "CRECE"],
        ["<b>Datos de mercado</b>",
         "Vender los precios que se forman en su propia casa. Es el subproducto perfecto: el dato ya existe, "
         "producirlo cuesta cero, y quien opera necesita verlo. <b>Es la única línea con poder de subir precios.</b>",
         "238,1 M US$", "<font color='#6C7E48'><b>+20,2%</b></font>"],
        ["<b>El «flotante»</b>",
         "CME custodia el dinero que las dos partes depositan como garantía. Lo invierte, devuelve casi todo el "
         "interés a sus miembros, y <b>se queda un diferencial</b>. No es un negocio: es un peaje sobre el dinero "
         "ajeno mientras está aparcado.",
         "123,1 M US$", "depende<br/>de los tipos"],
        ["<b>Comisiones</b>", "El peaje por contrato descrito arriba.", "1.352,5 M US$",
         "<font color='#C60C2A'><b>−2,6%</b></font>"]],
        [3.1*cm, 8.2*cm, 2.6*cm, 2.7*cm], font_sz=8.6)]
    o += [callout("DATO CURIOSO",
        "CME custodia <b>158.110,7 millones de dólares</b> de garantías de sus clientes. Su empresa entera vale en "
        "bolsa 98.894 millones. <b>Es decir: guarda en depósito 1,6 veces lo que vale ella misma</b>, y 138.500 "
        "millones de eso están literalmente en una cuenta en el Banco de la Reserva Federal de Chicago — un "
        "privilegio que sólo tienen las infraestructuras declaradas «sistémicamente importantes» por el Estado. "
        "Además hay otros 195.681 millones en garantías que ni siquiera aparecen en el balance porque no son dinero, "
        "sino bonos depositados.")]
    o += [p("<b>Y todo esto lo hacen 3.875 personas.</b> Eso son 1,68 millones de dólares de ingresos por empleado. "
        "Para hacerse una idea: un banco comercial típico anda por 300.000. Es la señal más limpia de que aquí no "
        "se vende trabajo, se cobra un derecho de paso.")]
    o += [p("<b>Dos advertencias que hay que tener presentes toda la lectura.</b> La primera: CME declara ante la "
        "SEC <b>un solo segmento operativo</b>, lo que significa que no publica cuánto gana con cada línea de "
        "producto. Todo desglose de rentabilidad por línea de este documento es una inferencia aritmética, no un "
        "dato de la empresa. La segunda: hay dos concentraciones declaradas en el propio informe anual — "
        "<b>una sola firma canaliza el 12% de las comisiones</b> y <b>dos revendedores el 30% de los ingresos de "
        "datos</b>.")]
    return o + [PageBreak()]

def s2_historia():
    o = flag_titulo("2 · Cómo se construyó el foso",
                    "CME no inventó su ventaja competitiva: la compró, y el recibo sigue en el balance")
    o += [p("En 1848, un grupo de comerciantes de grano de Chicago fundó el Chicago Board of Trade. En 1898, otro "
        "grupo hizo lo propio con la mantequilla y los huevos; ese segundo se convertiría en el Chicago Mercantile "
        "Exchange. Durante un siglo, los dos cobraron por <b>ejecutar</b> operaciones, no por garantizarlas.")]
    o += [p("El giro llega en 1971. Leo Melamed, entonces presidente del Merc, quiere lanzar futuros sobre divisas "
        "—algo que nadie había hecho— y necesita respetabilidad intelectual. Le encarga un ensayo justificativo a "
        "Milton Friedman, que aún no había ganado el Nobel. <b>Friedman cobró 7.500 dólares.</b> Los futuros sobre "
        "divisas se listaron el 16 de mayo de 1972, y detrás llegaron el eurodólar (1981) y el S&amp;P 500 (1982), "
        "que hoy siguen siendo el corazón del negocio.")]
    o += [callout("DATO CURIOSO",
        "Aquellos 7.500 dólares de 1971 son, ajustados por inflación, unos 58.000 de hoy. Compraron el argumento "
        "académico que legitimó una industria que en 2025 movió <b>119.000 millones de contratos</b> en todo el "
        "mundo. Probablemente la consultoría con mejor retorno de la historia financiera.")]
    o += [p("<b>El gen que explica el presente aparece en 1997</b>, con el E-mini S&amp;P 500: el mismo contrato de "
        "siempre, pero de una quinta parte del tamaño. La idea era ensanchar la base de clientes partiendo el "
        "producto en trozos más pequeños. Funcionó tan bien que se ha repetido cuatro veces más: los Micro E-mini "
        "en 2019, el oro de una onza en 2024, y los <b>E-nano lanzados el 24 de agosto de 2026, que son una "
        "centésima parte del E-mini original</b>. La sección 6 explica por qué eso es a la vez la mejor y la peor "
        "noticia de esta tesis.")]
    o += [p("<b>Y luego vino la fase de compra, que es la que explica el balance de hoy.</b> Entre 2007 y 2018, CME "
        "se comió a sus competidores:")]
    o += [tabla([
        ["AÑO", "COMPRA", "QUÉ APORTÓ"],
        ["2007", "Chicago Board of Trade", "Los futuros sobre bonos del Tesoro de EE.UU. — hoy su mayor franquicia"],
        ["2008", "NYMEX y COMEX", "Petróleo, gas natural, oro y cobre"],
        ["2012", "Kansas City Board of Trade", "Trigo duro de invierno"],
        ["2018", "NEX Group", "BrokerTec (contado de bonos del Tesoro) y EBS (divisas)"]],
        [1.6*cm, 5.0*cm, 10.0*cm], font_sz=8.8)]
    o += [p("Coste conjunto: <b>26.218 millones de dólares</b>. Y aquí está la parte que casi nadie mira. Cuando "
        "una empresa compra otra por encima del valor de sus bienes físicos, la diferencia se apunta en el balance "
        "como <b>fondo de comercio</b> (el valor de lo intangible: la marca, los clientes, la posición) e "
        "<b>intangibles</b>. En CME eso suma:")]
    o += [tabla([
        ["PARTIDA DEL BALANCE", "IMPORTE", "QUÉ ES"],
        ["Fondo de comercio", "10.505,8 M US$", "Lo pagado de más por CBOT, NYMEX, KCBT y NEX"],
        ["Intangibles de vida definida", "2.494,6 M US$", "Relaciones con clientes, que se van amortizando"],
        ["<b>Autorizaciones de producto</b>", "<b>17.175,3 M US$</b>",
         "<b>El permiso de la CFTC para listar cada contrato. Nunca se amortiza.</b>"]],
        [5.2*cm, 3.2*cm, 8.2*cm], font_sz=8.8)]
    o += [p("Esa tercera línea merece detenerse. <b>Son 17.175 millones de dólares — el 55,9% de todos los activos "
        "de larga duración de la empresa y el 59,8% de su patrimonio neto — y su justificación contable cabe en "
        "once palabras</b> que figuran en una nota al pie del informe anual: <i>«Product authorizations from the "
        "CFTC have no term limits»</i> (las autorizaciones de producto de la CFTC no tienen límite temporal).")]
    o += [callout("LA TRAMPA",
        "<b>El activo más grande del balance de CME es un permiso administrativo.</b> Vale mucho mientras ese "
        "permiso sea escaso. El 29 de mayo de 2026, el regulador estadounidense abrió una vía nueva para que otros "
        "listen contratos que antes sólo tenían las bolsas establecidas. No es una expropiación ni nada parecido — "
        "pero es exactamente el tipo de cambio que un balance no recoge hasta que es tarde. La sección 9 lo trata "
        "como un riesgo con <b>fecha concreta</b>: el 16 de noviembre de 2026.")]
    o += [p("<b>El resultado de todas esas compras es el foso.</b> Al meter tipos de interés, energía, metales, "
        "divisas e índices bursátiles dentro de <i>una sola</i> cámara, CME puede hacer algo que ningún rival "
        "puede: <b>compensar los riesgos de un cliente entre sí</b>. Si alguien apuesta a que suben los tipos y a "
        "la vez a que baja el petróleo, esas dos posiciones se contrarrestan en parte, y CME le pide menos dinero "
        "en garantía. El ahorro que entrega por ese concepto supera los <b>95.000 millones de dólares diarios</b>.")]
    o += [p("Nadie puede replicar esa cartera porque las piezas ya no existen sueltas: CME se las comió todas. "
        "<b>El foso de CME es, literalmente, un acta notarial de 2007-2008 con un sello del regulador encima.</b>")]
    return o + [PageBreak()]
