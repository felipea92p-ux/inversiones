# -*- coding: utf-8 -*-
"""Seccion 2 (el negocio) y Seccion 3 (los doce trimestres)."""
import motor_qg as M
from reportlab.platypus import Spacer, PageBreak, KeepTogether
from reportlab.lib.units import cm

CW = 17.0  # ancho util en cm


def seccion_2():
    out = M.flag_titulo("2 &middot; El negocio: de donde sale cada dolar",
                        "Cuatro motores de ingresos, y una tabla que decide la tesis: quien manda hoy, "
                        "el precio o las unidades")
    out.append(M.p(
        "<b>2.1 &middot; Lo que Intuit es, en una frase que sirva dentro de dos anos.</b> "
        "Intuit es el sistema de registro contable y fiscal de la pequena empresa y del declarante "
        "estadounidense, monetizado por suscripcion y, cada vez mas, por precio sobre una base "
        "instalada que no puede irse sin coste. No es una empresa de software de productividad ni una "
        "fintech: es un <b>peaje sobre obligaciones legales recurrentes</b> &mdash;pagar impuestos, "
        "pagar nominas, cobrar a clientes, llevar libros&mdash; con la propiedad rara de que el cliente "
        "no puede dejar de hacer esas cosas y de que cambiar de proveedor significa mover el historial "
        "contable de su empresa entera.", "cuerpo"))

    out.append(M.p("<b>2.2 &middot; Los cuatro motores de ingresos.</b> [HECHO, 10-K FY2025, "
                   "acc. 0000896878-25-000035] FY2025 cerro con 18.831 millones de dolares de "
                   "ingresos:", "cuerpo"))
    filas = [
        ["Bloque", "Ingresos\nFY2025", "% del\ntotal", "Crecim.\nFY2025", "Que es realmente"],
        ["GBS &mdash; Global Business Solutions", "11.077", "58,8%", "+16%",
         "QuickBooks, Mailchimp, nomina, pagos, credito"],
        ["&nbsp;&nbsp;&middot; Ecosistema online", "8.302", "44,1%", "+20,5%",
         "El motor. QBO Accounting + Online Services"],
        ["&nbsp;&nbsp;&middot; Ecosistema desktop", "2.775", "14,7%", "+5,1%",
         "Base cerrada a clientes nuevos. Puro precio"],
        ["Consumer &mdash; TurboTax", "4.870", "25,9%", "+10%",
         "Temporada fiscal. 100% de EE.UU. y Canada"],
        ["Credit Karma", "2.263", "12,0%", "+32%", "Intermediacion de credito de terceros"],
        ["ProTax", "621", "3,3%", "+4%", "Software para preparadores profesionales"],
    ]
    out.append(M.tabla(filas, [4.7 * cm, 2.1 * cm, 1.7 * cm, 1.9 * cm, 6.6 * cm]))
    out.append(Spacer(1, 6))
    out.append(M.p(
        "El dato de rentabilidad que hay que retener, porque sostiene todo lo demas: el margen "
        "operativo del segmento GBS es del <b>76,9%</b>, el de ProTax del <b>85,8%</b> y el de Credit "
        "Karma del <b>36,9%</b> &mdash;las dos ultimas cifras dejaron de publicarse el 1-ago-2025 con "
        "la fusion de segmentos; ver §3.3. Un negocio con margenes de segmento de tres cuartas partes "
        "no es un negocio normal: es un peaje.", "cuerpo"))

    out.append(M.chart("charts/c1_motores_ingresos.png"))
    out.append(Spacer(1, 4))

    out.append(M.p(
        "<b>2.3 &middot; La descomposicion que decide la tesis: precio contra unidades, motor por "
        "motor.</b> Esta es la tabla mas importante del documento. Esta construida con el orden de "
        "palabras que la propia Intuit usa en sus filings, no con interpretacion: en un 10-Q, el motor "
        "que la empresa nombra primero es el motor principal, y ese orden se cambio deliberadamente "
        "en febrero de 2025.", "cuerpo"))

    filas2 = [
        ["Motor", "Peso", "Quien manda", "Evidencia literal"],
        ["QuickBooks Online Accounting", "~30% de GBS", "PRECIO, desde Q2 FY2025",
         '"driven by higher effective prices, customer growth, and mix-shift" &mdash; nueve '
         "comunicados consecutivos. Antes de feb-2025, la misma frase empezaba por "
         '"customer growth"'],
        ["Online Services &middot; Pagos", "grande", "UNIDADES (el unico bloque grande)",
         "Volumen de pagos online +29% / +29% / +30% en los tres trimestres de FY2026 "
         "(+18% ex-Bill Pay)"],
        ["Online Services &middot; Nomina", "medio", "MEZCLA primero",
         "9M FY2026 +204 M, con la mezcla nombrada antes que el volumen"],
        ["Online Services &middot; QuickBooks Capital", "pequeno, creciendo rapido",
         "NINGUNO &mdash; es una cartera de prestamos",
         "+144 M en 9M FY2026; originaciones 4.930 M contra 2.873 M (+72%); saldo vivo "
         "687 M (FY2023) &rarr; 1.662 M (Q3 FY2026)"],
        ["Ecosistema Desktop", "14,7% del total", "PRECIO PURO, al 100%",
         '"due to higher effective prices" &mdash; y nada mas en la frase. Base cerrada a '
         "clientes nuevos, creciendo +5,1% en FY2025 y +6-10% en FY2026"],
        ["TurboTax (nucleo)", "25,9% del total", "PRECIO, con unidades NEGATIVAS 3 anos seguidos",
         "Unidades totales EE.UU. 40,5M &rarr; 39,9 (&minus;1%) &rarr; 39,2 (&minus;2%) &rarr; "
         "guiado &asymp;&minus;2%. ARPR/ARPU +10% &rarr; +13% &rarr; +11%"],
        ["TurboTax Live", "53% de TurboTax en FY2026", "UNIDADES, CEDIENDO PRECIO",
         "FY2026: ingresos +36%, clientes +38% &rarr; ARPU implicito &minus;1,4%"],
        ["Credit Karma", "12% del total", "EXOGENO &mdash; ciclo de credito de terceros",
         "FY2025 +32%; FY2026 ~+19%"],
        ["Mailchimp", "~1.300 M", "PRECIO sobre una base que no crece",
         "~+1,6%. Las cuatro veces que Intuit describe su motor, el precio va primero"],
    ]
    out.append(M.tabla(filas2, [3.5 * cm, 2.9 * cm, 3.8 * cm, 6.8 * cm], font_sz=7.7))
    out.append(Spacer(1, 6))
    out.append(M.p(
        "Leida la tabla entera de una vez sale el retrato del negocio: de los cuatro bloques grandes, "
        "<b>tres estan monetizando por precio</b> (QBO Accounting, Desktop, TurboTax) y el cuarto "
        "(Credit Karma) no depende de Intuit sino del ciclo de credito. Los dos unicos sitios donde las "
        "unidades siguen siendo el motor declarado son <b>pagos</b> &mdash;que es volumen "
        "transaccional, no clientes nuevos&mdash; y <b>TurboTax Live</b>, que crece por unidades "
        "bajando el precio.", "cuerpo"))

    out.append(M.callout("LECCIÓN TRANSFERIBLE",
        "La frase que resume el hallazgo aritmetico mas importante del expediente, y que ninguna mesa "
        "habia nombrado: <b>por primera vez, el motor nuevo de Intuit crece por unidades y pierde "
        "precio, mientras el nucleo crece por precio y pierde unidades. Las dos mitades del negocio "
        "han intercambiado sus motores.</b> [INFERENCIA aritmetica sobre dos HECHOS del 8-K del "
        "20-may-2026] Eso encaja exactamente con la doctrina declarada de "
        '"we are going to have a model where we are very competitive on price", y significa que la '
        "palanca de precio que sostiene la valoracion ya no esta donde el relato dice que esta."))

    out.append(M.p(
        "<b>2.4 &middot; Y el ajuste que desinfla el poder de precio, porque hay que decirlo.</b> "
        "Los +144 M de QuickBooks Capital en 9M FY2026 caen enteros dentro del ARPC y aportan cero "
        "clientes. Depurando solo esa linea, el ecosistema online crece <b>17,9%</b> en vez de 20,2%: "
        "2,4 puntos del ARPC no son un precio, son una cartera de credito con su propio coste de "
        "capital y su propia perdida esperada, alojada en la linea de inversion del estado de flujos y "
        "por tanto fuera del FCF publicado. Si las originaciones del ano superan ~6.500 M (contra "
        "3.992 M en FY2025), QuickBooks Capital deja de ser un accesorio y hay que valorarlo aparte.",
        "cuerpo"))
    out.append(PageBreak())
    return out


def seccion_3():
    out = M.flag_titulo("3 &middot; La trayectoria de doce trimestres",
                        "Es el corazon del documento y lo que no caduca manana")

    out.append(M.p("<b>3.1 &middot; Promesas contra entregas &mdash; los marcos de largo plazo.</b>",
                   "cuerpo"))
    filas = [
        ["#", "Promesa", "Cifra", "Que paso", "Veredicto"],
        ["L1", "GBS/SBSEG 15-20%/ano. Reiterada ago-23, ago-24, ago-25", "15-20%",
         "FY23 +24% &middot; FY24 +19% &middot; FY25 +16% &middot; FY26 ~+16%",
         "CUMPLIDA &mdash; deslizandose al borde bajo, monotonamente: 24&rarr;19&rarr;16&rarr;16"],
        ["L2", "ARPC de pago online 10-20%. Nunca tocada en 4 anos", "10-20%",
         "FY24 +11% &middot; FY25 +14%", "CUMPLIDA y acelerando"],
        ["L3", "Clientes de pago online 10-20% (Aujla, 22-feb-2024)", "10-20%",
         "Recortada a 5-10% seis meses despues. FY24 +6% &middot; FY25 +5%",
         "RECORTADA A LA MITAD y entregada en el SUELO EXACTO de la banda nueva"],
        ["L4", "Consumer Group 8-12% (reiterada 23-may-2024)", "8-12%",
         'Recortada a 6-10% 90 dias despues, "in this interim period". FY24 +7% (habria FALLADO la '
         "banda vieja) &middot; FY25 +10%",
         'CUMPLIDA SOLO BAJO LA BANDA REBAJADA. El "interim period" lleva 2 anos sin fecha de salida'],
        ["L5", "Credit Karma 20-25%/ano (reiterada 24-ago-2023)", "20-25%",
         "Recortada a 10-15% el 22-ago-2024. Despues: FY25 +32%, FY26 ~+19%",
         "RECORTADA justo antes de dos anos excelentes. La ironia cuenta a favor de la empresa"],
        ["L6", "TurboTax Live 15-20%", "15-20%",
         "FY23 +17% &middot; FY24 +17% &middot; FY25 +47% &middot; FY26 +36%",
         "CUMPLIDA Y BATIDA POR MUCHO"],
        ["L7", 'TT Live sera "the majority of Consumer Group revenue" (Aujla, 22-ago-2024)', "&gt;50%",
         "FY24 ~30% &rarr; FY25 41% &rarr; FY26: 53% de TurboTax", "CUMPLIDA en dos anos"],
        ["L8", '"annual EPS growth of at least mid-teens over the coming years" (Aujla, 20-may-2026)',
         "&ge;15%", "Nueva, sin fecha de vencimiento", "ABIERTA &mdash; su defecto es no tener plazo"],
        ["L9", 'GBS de ~10.000 M "a mucho mas" en 3-5 anos (Goodarzi, ago-24)', "&mdash;",
         "GBS FY2026 &asymp; 12.850 M", "ABIERTA, en camino"],
        ["L10", "La reestructuracion de 2024 (223 M, 8% de plantilla) rendiria en "
         '"dos, tres anos o mas"', "FY26-27",
         "La ventana ES AHORA. Y en may-2026 hicieron otra el doble de grande (17% de plantilla)",
         "VENCE MANANA. Que haya hecho falta una segunda reestructuracion el doble de grande dentro "
         "de la ventana de rendimiento de la primera es, por si solo, la respuesta"],
    ]
    out.append(M.tabla(filas, [1.05 * cm, 5.1 * cm, 1.45 * cm, 4.95 * cm, 4.45 * cm], font_sz=7.5))
    out.append(PageBreak())

    out.append(M.p("<b>3.2 &middot; Promesas contra entregas &mdash; las guias anuales.</b>", "cuerpo"))
    filas2 = [
        ["Ejercicio", "Guiado (fecha)", "Entregado", "Veredicto"],
        ["FY2024 ingresos", "15.890-16.105 M (+11-12%), 24-ago-23", "16.285 M (+13,3%)", "BATIDA"],
        ["FY2025 ingresos", "18.160-18.347 M (+12-13%), 22-ago-24", "18.831 M (+16,1%)",
         "BATIDA POR MUCHO"],
        ["FY2025 op. GAAP", "4.649-4.724 M (+28-30%)", "4.923 M (+35,6%)", "BATIDA"],
        ["FY2025 Online Ecosystem", "~+20%", "+20,5% (8.302 M)", "CLAVADA"],
        ["FY2026 ingresos", "20.997-21.186 M (+12-13%), 21-ago-25", "subido a 21.341-21.374 M "
         "el 20-may-26", "EN CAMINO DE BATIRSE"],
        ["FY2026 op. GAAP", "5.782-5.859 M (+17-19%), 21-ago-25", "REBAJADO a 5.705-5.725 M "
         "el 20-may-26", "INCUMPLIDA CONTRA SU PROPIA GUIA INICIAL. La UNICA linea rebajada en "
         "cuatro anos"],
        ["FY2026 Credit Karma &middot; GBS", "+10-13% &middot; +14-15%", "subidos a ~+19% &middot; "
         "~+16%", "BATIDAS"],
    ]
    out.append(M.tabla(filas2, [3.6 * cm, 5.0 * cm, 5.0 * cm, 3.4 * cm], font_sz=7.8))
    out.append(Spacer(1, 8))

    out.append(M.p("La aritmetica del punto que mas pesa, y su contrapeso entero:", "cuerpo"))
    filas3 = [
        ["", "Ingresos", "Op. GAAP", "Margen GAAP", "Reestruct.", "Margen ex-cargo"],
        ["FY2024 real", "16.285", "3.630", "22,29%", "223", "23,66%"],
        ["FY2025 real", "18.831", "4.923", "26,14%", "15", "26,22%"],
        ["FY2026 guiado ago-25", "20.997", "5.782", "27,54%", "0 previsto", "27,54%"],
        ["FY2026 guiado may-26", "21.341", "5.705", "26,73%", "300 (de 300-340)", "28,14%"],
    ]
    out.append(M.tabla(filas3, [3.6 * cm, 2.3 * cm, 2.3 * cm, 2.7 * cm, 3.0 * cm, 3.1 * cm],
                       font_sz=7.9))
    out.append(Spacer(1, 6))

    out.append(M.callout("PAUSA REFLEXIVA",
        "<b>La acusacion:</b> la promesa de margen de FY2026 cayo 81 puntos basicos entre agosto y "
        "mayo, en el mismo ano en que la empresa despidio al 17% de su plantilla y subio el precio en "
        "toda la linea. Y la guia solo incorpora 300 M de un cargo declarado de 300-340: hasta 40 M "
        "estan fuera del numero.<br/><br/>"
        "<b>La defensa, que es real y se da entera:</b> la guia no se rebajo, se subio. La revision "
        "ex-cargo es 6.005-6.025 M contra 5.782-5.859 M iniciales = +166 a +223 M (+2,8% a +3,9%), en "
        "el mismo movimiento que subio la de ingresos. Y <i>us-gaap:RestructuringCharges</i> en el "
        "XBRL de EDGAR para el periodo 2025-08-01 &rarr; 2026-04-30 es CERO: los tres trimestres "
        "publicados de FY2026 no llevan cargo alguno, y los 9M reales dan margen operativo GAAP de "
        "31,64% contra 30,56% (+108 pb interanual). La senda limpia es 23,66% &rarr; 26,22% &rarr; "
        "28,14%.<br/><br/>"
        "<b>Resolucion:</b> el angel gana el hecho contable y lo gana limpiamente. Pero la pregunta "
        "correcta no es si el margen se expande &mdash;se expande&mdash; sino de donde sale. Y ahi el "
        "dato que decide es el del segmento: el margen interanual de GBS paso de +4/+5 pp (FY2023-24) "
        "a +1/+2 pp (FY2025) a &minus;0,7 / &minus;0,9 / &minus;0,1 pp en los tres trimestres de "
        "FY2026. <b>El margen consolidado sube mientras el margen del segmento &mdash;el mas cercano "
        "al motor de unidades&mdash; se va a cero.</b> Eso es apalancamiento de la capa corporativa y "
        "de 3.100 personas menos, no apalancamiento operativo sobre unidades que crecen."))

    out.append(M.chart("charts/c3_margen_segmento.png"))
    out.append(PageBreak())

    out.append(M.p("<b>3.3 &middot; La cronologia de las metricas retiradas.</b> Regla que se impone "
                   "antes de escribir esto: una metrica solo cuenta como retirada sospechosa si "
                   "(a) desaparecio y (b) el periodo inmediatamente anterior era malo. Si desaparecio "
                   "plana o mejorando, la acusacion se cae y se dice.", "cuerpo"))
    out.append(M.p("<b>Las que SI forman patron:</b>", "h3"))
    filas4 = [
        ["Metrica", "Ultima\naparicion", "Que hacia justo antes", "Lectura"],
        ["Coeficientes de sensibilidad de Consumer (1 pt declaraciones IRS &asymp; 1 pt ingresos; "
         "1 pt cuota DIY &asymp; 2,5 pts)", "Q3 FY2023", "Era la regla que permitia a un tercero "
         "auditar la aritmetica de Intuit",
         "LA RETIRADA MAS GRAVE. No es una metrica: es la clave de conversion"],
        ["Total de declaraciones al IRS y crecimiento de la categoria DIY", "Q3 FY2023",
         "Ambas cayendo", "Hoy queda la cuota sin el tamano de la tarta &mdash; y hoy juega a favor: "
         "la categoria DIY crecio +1,7% y no lo publican"],
        ['El marco de "los cuatro motores del negocio consumer"', "Q3 FY2023",
         "Dos de los cuatro empeorando", "Hoy quedan piezas sueltas, no el marco"],
        ['Fila "Canada TurboTax Units"', "Q4 FY2023 (3,7 M, +5%)", "Era la UNICA fila que crecia",
         "Patron invertido y aun asi relevante: se retiro la fila buena"],
        ["Resultado operativo de Credit Karma (36,9%) y ProTax (85,8%)", "10-K FY2025",
         "Credit Karma acelerando (+32%)", "Patron de RESOLUCION, no de resultado. La unica unidad "
         "cuyo fondo de comercio podia deteriorarse dejo de ser auditable el mismo ano"],
        ['Seccion "Long-Term Growth Expectations" (bandas de clientes y ARPC)', "Q4 FY2025",
         "Clientes entregando +5%, el suelo exacto de su banda",
         "AUN NO ES UNA RETIRADA. Sale manana o no sale &mdash; y si no sale, ese es el titular"],
    ]
    out.append(M.tabla(filas4, [5.0 * cm, 2.4 * cm, 4.6 * cm, 5.0 * cm], font_sz=7.4))
    out.append(Spacer(1, 8))

    out.append(M.p("<b>Las que NO forman patron &mdash; la correccion mas importante de este "
                   "documento:</b>", "h3"))
    filas5 = [
        ["Acusacion de la casa", "Veredicto", "Prueba"],
        ['"Dejaron de publicar la comparacion de unidades federales; es el patron central de '
         'ocultacion" &mdash; premisa del pre-compromiso del 22-ago', "FALSA. Nunca desaparecio",
         "Compromiso de calendario anual, frase identica salvo el ano, cumplido 2 de 2. Ningun "
         'analista la pidio jamas: "federal" aparece cero veces en los tres Q&amp;A de FY2026'],
        ['"Ocultan el crecimiento de clientes ex-precio" &mdash; defecto declarado en gates.md',
         "FALSA, y es la correccion mas valiosa aqui",
         'Intuit publica cada agosto "US QBO customers excluding self-employed": FY2024 +11%, '
         "FY2025 +8%. Existe, es primaria, y sale manana"],
        ['"Clientes de pago online y ARPC solo salen en el 10-K (~3-sep)"', "FALSA",
         'Ambas estan en el guion propio del Q4 FY2025 y del Q4 FY2024. El gate de gates.md se '
         "resuelve MANANA, no el 3-sep"],
        ['"Mailchimp desaparecio de la lista de motores porque iba mal"', "CIERTA pero trivial",
         "Iba mal, si &mdash; pero Intuit publica su lastre voluntariamente cada trimestre en forma "
         "de la cuna ex-Mailchimp"],
        ['"combined platform revenue es un agregado nuevo para tapar"', "FALSA",
         "Existe desde el Q4 FY2022, solo se publica en Q4, y se publica cuando sube "
         "(FY2025 +19% a 14,9 B)"],
    ]
    out.append(M.tabla(filas5, [5.4 * cm, 3.0 * cm, 8.6 * cm], font_sz=7.5))
    out.append(Spacer(1, 8))

    out.append(M.p("<b>Los dos cambios de definicion silenciosos &mdash; esto si es serio:</b>",
                   "h3"))
    filas6 = [
        ["Cambio", "Antes", "Despues", "Por que importa"],
        ["ARPR &rarr; ARPU", 'FY2023-25: "average revenue per return"',
         'FY2026 Q3: "average revenue per user"',
         "Cambia el denominador sin nota de conciliacion. El +11% de FY2026 y el +13% de FY2025 no "
         "son la misma serie"],
        ['Cuota "total IRS returns" &rarr; "e-files"', "FY2025 Q3", "FY2026 Q3",
         "Cambiaron al denominador que crece (+1,1%) el ano en que el otro cae (&minus;0,6%). "
         'Goodarzi lo explico en el Q&amp;A: "e-files will be up 1%, but... e-file does not include the '
         'manual of filings". Sabian que divergian'],
    ]
    out.append(M.tabla(filas6, [3.0 * cm, 3.6 * cm, 3.6 * cm, 6.8 * cm], font_sz=7.6))
    out.append(PageBreak())

    out.append(M.p("<b>3.4 &middot; Los cinco puntos de inflexion.</b>", "cuerpo"))
    hitos = [
        ("23-may-2023 &mdash; el negocio fiscal se rompe y se presenta como una subida de guia.",
         "Consumer recortado de 9-10% a 5-6% (200 M), categoria DIY admitida a la baja, cuota "
         '&minus;80 pb. Y el titular del 8-K es "Raises Total Company Full Year Guidance", porque '
         "SBSEG subio. Es la ultima llamada de Clatterbuck y siete de los diez analistas abren con "
         "felicitaciones personales. La ruptura del negocio fiscal ocurre y queda tapada por la "
         "mecanica de Relaciones con Inversores y por una despedida. En la misma temporada se "
         "retiran las cuatro metricas de auditoria de Consumer y jamas vuelven."),
        ("24-ago-2023 &mdash; el acta de nacimiento de la doctrina.",
         'Goodarzi, sobre Consumer: "You\'re going to see more come from ARPC than volume. ... '
         'It\'s just our view looking at the next 10 years. By the way, this is not a one-year '
         'answer." Y en la MISMA llamada, sobre small business, lo contrario: "we want to drive the '
         'majority of our growth from a volume and mix and the lesser part from price". Lo que en '
         "FY2023 estaba acotado a TurboTax es exactamente lo que hoy describe tambien a GBS. Es la "
         "promesa mas honesta que hizo Intuit en cuatro anos y nadie la trato como lo que era."),
        ("22-ago-2024 &mdash; el dia bisagra. Una sola llamada, cinco cosas.",
         "(1) Clientes de pago online 10-20% &rarr; 5-10%. (2) Credit Karma 20-25% &rarr; 10-15%. "
         "(3) Consumer 8-12% &rarr; 6-10%. (4) ARPC y GBS intactos. (5) El segmento se renombra de "
         '"Small Business and Self-Employed" a "Global Business Solutions" &mdash; la palabra que '
         "nombraba al colectivo que caia &minus;14% desaparecio del nombre&mdash; junto con 223 M de "
         "reestructuracion y el 8% de la plantilla. Lexico de mid-market: de 9 a 32 menciones en un "
         "trimestre. <b>Barrido de las 282 lineas del Q&amp;A: ningun analista pregunto por el "
         "recorte a la mitad de la banda de clientes. Cero preguntas.</b> La palanca que hoy decide "
         "el gate de Felipe se rebajo a la mitad en directo y no genero una sola pregunta. Es el "
         "silencio mas grande del expediente."),
        ("31-oct-2024 / 25-feb-2025 &mdash; el mecanismo cruza y la empresa lo escribe.",
         "QuickBooks Online Accounting (donde Intuit nombra el precio) supera a Online Services "
         "(donde nombra clientes y volumen) y no se ha vuelto a invertir en once trimestres. Y el "
         "comunicado del Q2 FY2025 invierte el orden de sus propios motores y pone el precio "
         "primero &mdash; y no vuelve atras en nueve comunicados. Entre esas dos fechas Intuit deja "
         "de ser un negocio de unidades y pasa a ser un negocio de precio, en su propia redaccion."),
        ("20-may-2026 &mdash; la admision.",
         '"I am constructively dissatisfied... We lost on price". 17% de la plantilla (~3.100 '
         "personas, cierre de Reno y Woodland Hills). Guia de ingresos subida y guia de resultado "
         "operativo GAAP bajada. Mailchimp pasa a ordeno. Margen de segmento de GBS &minus;0,1 pp. "
         'Y el operador impone por primera vez "Please limit yourself to 1 question": 7 analistas '
         "frente a los 15 del Q1. El trimestre con el recorte del 17% y el fallo fiscal es el unico "
         "con limite explicito de preguntas y el de menos participantes."),
    ]
    for tit, cuerpo in hitos:
        out.append(M.p(f"&#9654; <b>{tit}</b> {cuerpo}", "cuerpo"))

    out.append(M.p(
        "<b>Y la inflexion de MEDICION, 1-ago-2025.</b> Cuatro segmentos &rarr; dos. Desaparecen del "
        "filing el resultado operativo de Credit Karma y de ProTax. La resolucion del filing bajo, no "
        "subio. Y el 10-Q del Q3 FY2026 ya presenta el fondo de comercio en dos cubos (GBS 9.822 "
        "&middot; Consumer 4.160) en lugar de cuatro: <b>Credit Karma dejo de ser testeable por "
        "separado el 20-may-2026</b> [HECHO, Nota 5 del 10-Q].", "cuerpo"))
    out.append(PageBreak())

    out.append(M.p("<b>3.5 &middot; Mailchimp: el gemelo caido interno, y el caso de control de toda "
                   "la tesis.</b>", "cuerpo"))
    filas7 = [
        ["Promesa", "Fecha", "Que paso"],
        ['"we expect that the growth in Mailchimp to accelerate in the coming quarters"',
         "29-nov-2022", "INCUMPLIDA"],
        ["Reaceleracion via integracion + mid-market + internacional &mdash; tres llamadas "
         "seguidas, cero cifras, cero fechas", "may-23, ago-23, ago-24", "INCUMPLIDA x3"],
        ['"We expect Mailchimp to exit fiscal 2026 growing double digits"', "con fecha",
         'INCUMPLIDA con fecha. Movida el 26-feb-2026 a "some time beyond fiscal 2026"'],
        ['"we are rightsizing our investment in Mailchimp" + "think about a desktop business"',
         "20-may-2026", "Convertido en activo de ordeno. Aujla admitio que el flujo de caja "
         '"will generate more value for Intuit than a third party is likely to pay for that asset" '
         "&mdash; se sondeo la venta y el precio no compenso"],
    ]
    out.append(M.tabla(filas7, [6.0 * cm, 3.2 * cm, 7.8 * cm], font_sz=7.8))
    out.append(Spacer(1, 8))
    out.append(M.p(
        "12.000 millones pagados en nov-2021 &mdash;5.700 M en efectivo y 10,1 M de acciones de "
        "Intuit valoradas al cierre del 29-oct-2021 de 625,99 USD, un 72% por encima del precio de "
        "hoy&mdash; por un activo que hoy factura ~1.300 M creciendo ~1,6% y que resta tres puntos al "
        "crecimiento del ecosistema online.", "cuerpo"))
    out.append(M.callout("CASO HISTÓRICO",
        "<b>Por que es el caso de control y no una anecdota:</b> prueba que el moat de Intuit no es "
        '"la plataforma", no son "los 100 millones de clientes" y no es transferible por adquisicion. '
        "Intuit compro un negocio de marketing por correo electronico, le enchufo su distribucion, su "
        "capital y su equipo directivo durante cuatro anos y medio, y el negocio no se movio. Lo que "
        "funciona en QuickBooks y en TurboTax no es exportable. Eso acota el moat a donde de verdad "
        "vive: el registro contable y la obligacion fiscal."))
    out.append(PageBreak())
    return out
