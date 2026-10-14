# -*- coding: utf-8 -*-
"""§3 el foso · §4 la competencia · §5 el mercado"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, cm
from reportlab.platypus import PageBreak

def s3_foso():
    o = flag_titulo("3 · El foso: por qué el cliente no se va",
                    "No es la liquidez, ni la marca, ni la costumbre. Es que la posición abierta no se puede mudar de casa")
    o += [p("«Foso» (<i>moat</i>, en la jerga de Warren Buffett) es la ventaja que impide que un competidor te "
        "quite el negocio aunque tenga más dinero y mejor tecnología. Casi todo lo que se llama foso no lo es. "
        "Aquí sí lo hay, y conviene entender el mecanismo exacto, porque de él depende todo lo demás.")]
    o += [p("<b>El mecanismo, en una frase:</b> un futuro de CME no es un contrato con otra persona — es un "
        "contrato <i>con CME</i>. Y no existe ninguna vía por la que ese contrato se convierta en un contrato con "
        "otra cámara. No es que sea caro cambiarse: es que <b>no hay puerta</b>.")]
    o += [p("<b>Qué le pasa de verdad a un fondo que quiere mudarse.</b> Supongamos que gestiona 5.000 millones y "
        "quiere llevarse sus futuros sobre bonos del Tesoro a un rival más barato. Tiene que:")]
    o += [tabla([
        ["PASO", "QUÉ CUESTA"],
        ["1 · Cerrar su posición en CME", "Cruzar el diferencial de compraventa y pagar comisión"],
        ["2 · Abrirla de nuevo en el rival",
         "Diferencial más ancho y libro menos profundo, porque hay menos gente al otro lado"],
        ["3 · Aguantar el hueco entre ambas",
         "Durante unos minutos u horas está sin cobertura, expuesto al mercado"],
        ["<b>4 · Y aquí está el golpe</b>",
         "<b>Al sacar los bonos, el RESTO de su cartera en CME —índices, divisas, energía— pierde las "
         "compensaciones que tenía contra ellos. La garantía que CME le exige por lo que NO se ha movido SUBE.</b>"]],
        [4.6*cm, 12.0*cm], font_sz=8.8)]
    o += [callout("EN ROMÁN PALADINO",
        "El coste de irse de CME <b>no es proporcional a lo que te llevas: es superproporcional, porque castiga lo "
        "que dejas.</b> Es como una tarifa plana de móvil familiar: si una sola línea se va a otra compañía, no "
        "sólo paga más ella — suben todas las demás. Multiplícalo por miles de millones y por cada uno de los "
        "grandes fondos del mundo, y tienes el foso.")]
    o += [p("<b>Cuánto vale ese servicio, en dinero.</b> CME entrega a sus miembros más de <b>95.000 millones de "
        "dólares diarios</b> de ahorro en garantías. Sobre los 158.110 millones que custodia, eso significa que "
        "<b>el neteo que regala equivale al 60% del colateral que cobra</b>. A un coste de financiación de entre el "
        "0,5% y el 4% anual, ese ahorro vale a sus clientes entre 475 y 3.800 millones al año — frente a los 5.281 "
        "millones que CME les cobra en comisiones. Los clientes pagan el peaje porque el peaje les devuelve casi lo "
        "que cuesta.")]
    o += [p("<b>Los dos ataques que el foso ya sobrevivió — y cómo murieron.</b>")]
    o += [callout("CASO HISTÓRICO",
        "<b>Eurex US (2003-2008) pidió ENTRAR en el pool.</b> La mayor bolsa de derivados de Europa desembarcó en "
        "Chicago con tarifas subvencionadas, dispuesta a perder dinero años. Su plan era compensar en The Clearing "
        "Corporation, la cámara histórica del CBOT, para que sus contratos se pudieran netear contra los del CBOT. "
        "<b>CBOT respondió mudando su compensación entera a CME semanas antes de que Eurex abriera</b>, dejando la "
        "cámara vieja vacía. Eurex demandó por competencia desleal y perdió, catorce años después.<br/><br/>"
        "<b>ELX Futures (2009-2016) pidió PORTABILIDAD.</b> La respaldaban doce de los mayores bancos del mundo — "
        "es decir, los propios clientes de CME coaligados contra su proveedor. Su jugada fue legal: pidió al "
        "regulador una regla que permitiera cerrar en CME y abrir en ELX de forma casada. <b>El regulador dictaminó "
        "en 2010 que esa operación era legal, pero que ninguna bolsa estaba OBLIGADA a aceptarla.</b> CME se negó, "
        "y la regla fue papel mojado. Última operación de ELX: junio de 2016.")]
    o += [p("Y hay un detalle que remata el caso: <b>CME mantiene con la bolsa de Singapur un acuerdo que permite "
        "exactamente lo que le negó a ELX</b> —abrir una posición en una bolsa y cerrarla en la otra— vigente hasta "
        "abril de 2027. La portabilidad es técnicamente trivial. Existe donde a CME le conviene que exista.")]
    o += [p("<b>Ahora, la medición honesta del foso.</b> Esto es lo mejor de esta tesis, y no lo da CME: lo da "
        "quien está intentando cruzarlo. FMX, la plataforma de BGC respaldada por diez bancos, compite contra CME "
        "en dos mercados vecinos a la vez:")]
    o += [chart("charts/07_foso.png")]
    o += [p("En el <b>contado</b> del Tesoro —donde cada operación se liquida en dos días y nada queda «abierto»— "
        "FMX tiene el 42% del mercado y sigue ganando cuota. En los <b>futuros</b> del Tesoro —donde la posición se "
        "queda abierta meses y no se puede mudar— tiene el 0,37%. <b>Misma empresa, misma tecnología, mismos "
        "clientes, mismo año.</b> La única diferencia entre 42% y 0,37% es la existencia del foso.")]
    o += [p("<b>Y ahora la parte incómoda: dónde el foso NO protege.</b> Tres fugas documentadas.")]
    o += [tabla([
        ["LA FUGA", "LA EVIDENCIA"],
        ["<b>No defiende el precio</b>",
         "El foso garantiza que el cliente no se va. No garantiza que pague más. <b>El beneficio de explotación por "
         "contrato fue de 0,6148 US$ en 2009 y de 0,5990 en 2025</b>: plano en dólares corrientes, un 35% menos en "
         "términos reales."],
        ["<b>No defiende el flanco</b>",
         "Cboe se llevó la demanda de exposición al S&amp;P 500 hacia las <i>opciones</i>, pasando del 58% al 74% "
         "de cuota <b>sin tocar un solo contrato del interés abierto de CME</b>. Ganó un producto distinto sobre el "
         "mismo subyacente. El foso aguantó la plaza y la guerra se mudó de barrio."],
        ["<b>No defiende del proveedor</b>",
         "CME paga a S&amp;P Dow Jones Indices por licenciar el índice S&amp;P 500. Ese peaje pasó de 84,9 M US$ en "
         "2011 (2,6% de los ingresos) a <b>371,0 M en 2025 (5,7%)</b>. Crece al 11,1% anual mientras el negocio "
         "crece al 5,0%. En el 2T-2026 subió un 13,4% con los ingresos planos."]],
        [4.0*cm, 12.6*cm], font_sz=8.8)]
    o += [callout("PAUSA REFLEXIVA",
        "Un foso que protege la <b>cantidad</b> pero no el <b>precio</b> produce un negocio que crece en unidades y "
        "se estanca en euros. ¿Recuerdas algún otro caso así? Los periódicos tenían un foso local absoluto y "
        "perdieron el precio de la publicidad. Costco tiene un foso de escala y <i>sí</i> sube su cuota de socio "
        "con la inflación. La pregunta que decide el múltiplo que merece CME no es «¿tiene foso?» — lo tiene — "
        "sino <b>«¿su foso incluye el derecho a subir la tarifa?»</b>. En dieciséis años, la respuesta ha sido no.")]
    return o + [PageBreak()]

def s4_competencia():
    o = flag_titulo("4 · El campo de batalla",
                    "En el segundo trimestre de 2026, CME fue el único de siete operadores comparables cuyo beneficio de explotación cayó")
    o += [p("Esto no es una opinión sobre el sector: sale de las siete cuentas de resultados presentadas ante los "
        "reguladores el mismo trimestre.")]
    o += [tabla([
        ["EMPRESA", "INGRESOS 2T-26", "VARIACIÓN", "BENEFICIO DE EXPLOTACIÓN", "VARIACIÓN"],
        ["<b>CME Group</b>", "<b>1.706,2 M US$</b>", "<b>+0,8%</b>", "<b>1.107,1 M US$</b>",
         "<font color='#C60C2A'><b>−2,0%</b></font>"],
        ["Cboe", "731,6 M US$ (neto)", "+24,6%", "476,0 M US$", "<font color='#6C7E48'><b>+40,4%</b></font>"],
        ["Nasdaq", "2.532 M US$ (bruto)", "+20,5%", "712 M US$", "<font color='#6C7E48'>+25,4%</font>"],
        ["Deutsche Börse", "—", "—", "EBIT", "<font color='#6C7E48'>+11%</font>"],
        ["HKEX", "—", "—", "EBITDA", "<font color='#6C7E48'>+20%</font>"],
        ["LSEG", "—", "—", "EBITDA ajustado (semestre)", "<font color='#6C7E48'>+13,7%</font>"],
        ["ICE", "3.611 M US$ (bruto)", "+10,7%", "1.391 M US$", "<font color='#6C7E48'>+7,2%</font>"]],
        [3.1*cm, 3.5*cm, 2.2*cm, 5.0*cm, 2.8*cm], font_sz=8.4)]
    o += [p("<b>El dato más incómodo del trimestre no es que CME cayera. Es quién la alcanzó.</b>")]
    o += [chart("charts/06_margen.png")]
    o += [p("En 2022, el margen de explotación de Cboe era del 28,1% y el de CME del 60,1%: <b>32 puntos de "
        "diferencia</b>. En el segundo trimestre de 2026, Cboe marcó 65,1% y CME 64,9%. La superioridad "
        "estructural de márgenes que justificaba pagar una prima por CME <b>ha dejado de existir en cuatro años</b>.")]
    o += [p("<i>Un matiz que juega a favor de CME y hay que decirlo:</i> el margen de Cboe se mide sobre ingresos "
        "netos de costes que simplemente pasan de largo. Cboe mueve 1.442,8 millones brutos para quedarse 731,6. "
        "CME se queda prácticamente todo lo que factura. <b>Cboe es más eficiente sobre lo que retiene, no sobre lo "
        "que toca.</b>")]
    o += [p("<b>El frente que decide la próxima década: el inversor particular.</b> Cboe llevó su cuota en "
        "derivados ligados al S&amp;P 500 del 58% al 74% en cinco años. En las opciones que vencen el mismo día "
        "—el producto de moda entre particulares— tiene el <b>77%</b> del mercado frente a menos del 8% de CME. Y "
        "en junio de 2026 se derogó la regla que limitaba a los pequeños inversores a operar sólo unas veces por "
        "semana, lo que disparó su cuota minorista al 57%.")]
    o += [p("Mientras tanto, la dirección de CME reconoció en su conferencia de julio que <b>el 94% de su volumen "
        "sigue siendo institucional</b>. Los E-nano del 24 de agosto son la respuesta directa — y llegan a una "
        "fiesta que empezó sin ellos.")]
    o += [callout("DATO CURIOSO",
        "La amenaza mejor cuantificada del trimestre no es una bolsa: es un bróker de móvil. <b>Robinhood facturó "
        "156 millones de dólares en contratos de evento en el 2T-2026, frente a 10 millones un año antes.</b> Eso "
        "equivale al <b>11,5% de todas las comisiones de compensación de CME</b>, construido desde cero en cuatro "
        "trimestres por una empresa que no es una bolsa de derivados. Y CME, en lugar de listar el producto, "
        "<b>demandó a su propio regulador el 18 de junio de 2026</b> para impedir que otros lo listen.")]
    o += [p("<b>Y un frente donde CME es el retador, no el incumbente:</b> en energía, ICE facturó 518 millones "
        "contra 187 de CME —2,8 veces más— y con una tarifa por contrato de 1,90 dólares frente a 1,13. La "
        "narrativa de «CME es el monopolio» sólo es cierta en su patio: en el patio de al lado, es el pequeño.")]
    return o + [PageBreak()]

def s5_mercado():
    o = flag_titulo("5 · El mercado y sus límites",
                    "Ninguna capa está cerca de agotarse. Y CME no controla el acelerador de ninguna de las grandes")
    o += [p("El «mercado direccionable» (TAM, por sus siglas en inglés: todo el dinero que en teoría podrías llegar "
        "a facturar) de CME es enorme y está poco penetrado. Ése es el argumento alcista, y es real. Pero hay que "
        "desarmar primero un dato que engaña a casi todo el mundo.")]
    o += [callout("LA TRAMPA",
        "En 2025 el volumen mundial de derivados <b>cayó un 42,2%</b>, y la cuota de CME saltó del 3,2% al 5,9% "
        "sin que CME hiciera absolutamente nada. ¿Qué pasó? <b>India.</b> Sólo seis contratos de opciones de las "
        "bolsas indias sumaron 40.300 millones de contratos en nueve meses —el 47% del volumen mundial— con "
        "micro-lotes cuyo tamaño es una fracción de un contrato americano. <b>El contrato indio se opera y muere "
        "el mismo día; el americano se queda abierto en el libro.</b> Cualquier «cuota mundial» que incluya India "
        "sin ajustar es ruido. Los denominadores honestos: 28,8% de Norteamérica, 16,2% del mundo sin Asia.")]
    o += [p("<b>Las capas del mercado, con su penetración real:</b>")]
    o += [tabla([
        ["CAPA", "TAMAÑO DEL MERCADO", "PENETRACIÓN DE CME", "LECTURA"],
        ["Tipos de interés", "31,46 billones US$ de deuda del Tesoro viva",
         "≈9% en futuros del Tesoro", "Poco penetrada, pero la puerta vecina está cerrada: LCH compensa el 98% de los swaps en dólares"],
        ["Índices bursátiles", "Institucional y particular", "94% institucional",
         "<font color='#C60C2A'><b>El frente caliente. Cboe domina al particular</b></font>"],
        ["Datos de mercado", "49.200 M US$ de gasto mundial", "<b>1,6%</b>, creciendo al 20%",
         "<font color='#6C7E48'><b>La mejor capa: triplica el ritmo de su industria</b></font>"],
        ["Internacional", "—", "31-33% del volumen, +32%",
         "<font color='#6C7E48'>La pista más limpia: no exige trocear nada</font>"],
        ["Compensación del Tesoro", "Mandato regulatorio desde el 31-dic-2026", "Aprobada, <b>volumen cero</b>",
         "El rival (FICC) ya compensa el 58% del volumen obligado"],
        ["Divisas", "9,6 billones US$ al día", "1-2%, <b>y decreciendo</b>", "La capa más débil"],
        ["Criptomonedas", "12,7 billones US$ trimestrales en perpetuos", "5-8%",
         "<font color='#C60C2A'>CME renuncia por decisión propia al producto que crece</font>"],
        ["Contratos de evento", "Robinhood: 156 M US$/trimestre", "Irrelevante",
         "<font color='#C60C2A'>Robinhood factura seis veces el techo de esa línea en CME</font>"]],
        [2.9*cm, 4.0*cm, 3.3*cm, 6.4*cm], font_sz=7.9)]
    o += [p("<b>Ahora, el hallazgo que corrige el análisis anterior de este archivo — y corrige a favor de CME.</b>")]
    o += [p("La sospecha era que trocear los contratos en trozos cada vez más pequeños fuera <b>canibalismo</b>: "
        "vender lo mismo en diez pedazos, cobrar diez veces menos por pedazo, y acabar ingresando igual pero "
        "pareciendo que creces. Suena razonable. <b>Y es falso, y se puede demostrar con aritmética.</b>")]
    o += [callout("EN ROMÁN PALADINO",
        "Piensa en un jamón. Si vendes el jamón entero a 300 euros y luego lo vendes en 10 lonchas, <b>la pregunta "
        "no es cuánto cobras por loncha: es cuánto cobras por el jamón completo.</b> Si las diez lonchas suman 300, "
        "es lo mismo. Si suman 500, has descubierto que la gente paga más por comodidad.<br/><br/>"
        "Los datos dicen que CME está en el segundo caso. Con los micro-contratos ya en el <b>54%</b> del volumen "
        "de índices, si cada micro costase la décima parte del grande, la tarifa media habría caído a 0,53 dólares. "
        "<b>El dato observado es 0,605.</b> Es decir: un micro cuesta entre el 40% y el 60% de un contrato "
        "grande siendo la décima parte de tamaño. <b>Por unidad de riesgo transferido, CME cobra unas cinco veces "
        "más.</b> Trocear le sale rentable.")]
    o += [p("<b>El contrapeso, que impide celebrarlo del todo.</b> En los nueve primeros meses de 2025, contando "
        "cada micro como una décima parte, la exposición real al S&amp;P 500 negociada en CME <b>cayó un 3,0%</b> "
        "mientras el recuento de contratos subía un 7,8%. Y la propia nota de prensa de los E-nano lo admite: los "
        "particulares están <i>«priced out»</i>, expulsados por precio, porque el índice ha subido demasiado.")]
    o += [p("Conclusión honesta: <b>trocear no capta mercado nuevo. Defiende el mercado que ya tenía frente a la "
        "subida del índice.</b> Es poder de precio real, pero es un poder de precio <i>defensivo</i>.")]
    o += [p("<b>Y qué limita el crecimiento, en una frase.</b> No es el dinero: CME invierte el 1,28% de sus ventas "
        "en mantenimiento. No es el talento. <b>Es el interés abierto</b> —el total de contratos vivos en el "
        "libro—, que depende de tres cosas: cuánta deuda del Tesoro hay que cubrir, cuánto valen los índices, y "
        "cuánta incertidumbre hay en el mundo. <b>CME no controla ninguna de las tres.</b>")]
    o += [p("La prueba está en su propio año: del primer al segundo trimestre de 2026, el volumen diario cayó un "
        "21% —de 36,2 a 29,8 millones de contratos— <b>sin que la empresa hiciera nada distinto</b>. Cuando el "
        "trimestre lo decide la volatilidad y no la empresa, la empresa no es el motor: es el peaje de la carretera "
        "por la que pasa el motor.")]
    return o + [PageBreak()]
