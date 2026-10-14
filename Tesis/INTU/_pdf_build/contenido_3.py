# -*- coding: utf-8 -*-
"""Seccion 4 (el moat) y Seccion 5 (la valoracion)."""
import motor_qg as M
from reportlab.platypus import Spacer, PageBreak
from reportlab.lib.units import cm


def seccion_4():
    out = M.flag_titulo("4 &middot; El mecanismo del moat",
                        "Tres mecanismos apilados, con vidas distintas — y las dos amenazas tratadas "
                        "con rigor, no con titulares")

    out.append(M.p("<b>4.1 &middot; Por que mecanismo concreto gana dinero.</b> No es “la marca” "
                   "ni “los datos” ni “la IA”. Son tres mecanismos apilados, y "
                   "conviene medirlos por separado porque tienen vidas distintas:", "cuerpo"))

    out.append(M.p(
        "<b>(1) El coste de cambio contable, el unico verificado con numero.</b> [HECHO, 10-K FY2025 "
        "y 8-K del 20-may-2026] El Desktop Ecosystem es una base cerrada a clientes nuevos &mdash;"
        "nadie puede comprar el producto&mdash; y aun asi crecio +5,1% en FY2025 y +6-10% en FY2026, "
        "exclusivamente por subida de precio, con la frase del filing sin mas motor que ese. Esa es la "
        "prueba mas limpia de coste de cambio que un negocio puede aportar: una cohorte cerrada, "
        "envejeciendo, que absorbe subidas de precio anuales sin fugarse. Un cliente de QuickBooks "
        "tiene dentro su plan de cuentas, su historico, su conciliacion bancaria, su nomina y a menudo "
        "a su contable externo; migrar es un proyecto, no una decision.", "cuerpo"))
    out.append(M.p(
        "<b>(2) El peaje sobre una obligacion legal recurrente.</b> El cliente no compra Intuit porque "
        "quiera: compra porque tiene que declarar y tiene que pagar nominas. La demanda no es "
        "discrecional ni ciclica en el sentido economico normal. Eso es lo que produce margenes de "
        "segmento del 76,9%.", "cuerpo"))
    out.append(M.p(
        "<b>(3) El canal del contable, que casi nadie mide.</b> El ecosistema de contables externos "
        "(ProTax, QuickBooks Online Accountant) hace que quien decide la herramienta muchas veces no "
        "sea quien la paga. Es distribucion con incentivo alineado, y es la razon por la que ProTax "
        "opera al 85,8% de margen sobre 621 M.", "cuerpo"))

    out.append(M.callout("LECCIÓN TRANSFERIBLE",
        "Contra-prueba que viene de fuera y que hay que dar entera: <b>Xero esta subiendo su ARPU un "
        "+23%, mas que Intuit.</b> La subida de precio de doble digito es una propiedad de la "
        "categoria, no un sintoma de la debilidad de Intuit. Es la mejor evidencia del moat "
        "precisamente porque no la produce Intuit."))

    out.append(M.p("<b>4.2 &middot; Cuantos anos puede sostenerlo.</b> Respuesta, dada como "
                   "INFERENCIA fechada y no como HECHO: <b>entre diez y quince anos en QuickBooks, y "
                   "entre cinco y ocho en TurboTax.</b>", "cuerpo"))
    out.append(M.p(
        "<b>QuickBooks (10-15 anos):</b> el coste de cambio no se erosiona con el tiempo, se acumula "
        "&mdash;cada ano de historial contable dentro de la plataforma sube el coste de salir. La "
        "amenaza no es que alguien haga mejor software; es que la contabilidad de la pequena empresa "
        "deje de ser un producto que se compra y pase a ser una funcion que el banco o el sistema de "
        "pagos regala. Eso no esta ocurriendo (Wave lleva una decada siendo gratis y factura ~123 M "
        "contra los 11.077 M de GBS).", "cuerpo"))
    out.append(M.p(
        "<b>TurboTax (5-8 anos):</b> aqui si hay un reloj, y no es el que todo el mundo mira. El 10-K "
        "FY2025 declara por escrito que los usuarios gratuitos son la cantera de los de pago "
        '&mdash;"customers who use our free consumer tax products and whose tax scenarios evolve in '
        'subsequent years to require paid services"&mdash; y esa cantera paso de 13 M (FY2022) a '
        "11 M, a &gt;10 M, a 8 M, a ~7 M guiado en FY2026: &minus;46% en cuatro anos.", "cuerpo"))

    out.append(M.callout("PAUSA REFLEXIVA",
        "El argumento correcto contra TurboTax no es “pierde cuota”: es que <b>esta cobrando "
        "hoy el inventario de manana</b>, con una firma temporal de tres a cinco anos, invisible en "
        "cualquier trimestre. Es el unico riesgo del expediente que puede convertir esto en otra cosa, "
        "y es el unico que la valoracion no puede descontar porque no tiene serie.<br/><br/>"
        "El contra-argumento honesto, que le da la vuelta: Credit Karma tiene ~140 M de miembros, los "
        "declarantes originados desde Credit Karma crecen +54% y su ARPU es un 30% superior en "
        "usuarios de ambos productos. Puede que Intuit haya cambiado la cantera de sitio en vez de "
        "vaciarla. Eso es genuinamente NO DECIDIBLE hoy y es la unica pregunta que importa en el "
        "Investor Day del 17-sep."))

    out.append(M.p("<b>4.3 &middot; La amenaza de la IA, tratada con rigor y no con titulares.</b> "
                   "Hay que separar dos cosas que la conversacion publica mezcla.", "cuerpo"))
    out.append(M.p(
        "<b>(a) La IA como sustituto del producto.</b> El argumento es: un modelo de lenguaje puede "
        "llevar tu contabilidad y hacer tu declaracion, luego el software desaparece. Lo que la "
        "evidencia primaria dice hoy [HECHO, Q&amp;A de los tres trimestres de FY2026]: Goodarzi "
        'sobre OpenAI, "there is no revenue share... the economics that we enjoy today when directly '
        'working with customers, we will enjoy tomorrow"; y sobre los modelos de terceros, "the data '
        'does not leave our four walls... we only experience the economics in the relationship and we '
        'do not share in the economics". Aujla nombro el foso cuatro veces seguidas: datos '
        "propietarios, ser el nucleo del flujo de fondos, e inteligencia humana como diferenciador.",
        "cuerpo"))
    out.append(M.callout("CASO HISTÓRICO",
        "El dato que mas pesa contra la amenaza no es una declaracion, es una admision en contra: "
        "cuando Goodarzi explico por que perdieron el segmento DIY de menos de 50.000 USD de renta, "
        'dijo <i>"none of this has anything to do with AI. This is all about being price-right"</i>, '
        'y anadio que esos clientes <i>"are actually willing to have experiences that are far worse '
        'for them as long as the price is right"</i>. <b>La empresa perdio cuota por precio, no por '
        "producto.</b> Un mercado donde el cliente marginal acepta una experiencia peor a cambio de "
        "precio cero es un mercado donde una IA superior no es la variable decisiva."))
    out.append(M.p(
        "<b>(b) La IA como palanca de coste y de precio dentro del producto.</b> Aqui si hay evidencia "
        "y es material: 3 M de clientes usando agentes con &gt;85% de recurrencia, el agente contable "
        "ahorrando 12-14 horas al mes, y la aritmetica explicita de Aujla &mdash; “people in "
        "North America value their time around $75 an hour. So that is $900-plus of value we are "
        "delivering. We can take a cut of that”. Y el modelo de consumo anunciado para agosto de "
        "2026. Pero tres nombres de marca en cinco trimestres &mdash;“Intuit Assist” &rarr; "
        "“Intuit Intelligence” &rarr; “AI agents” / “system of "
        "intelligence”&mdash; y ninguno con metrica de ingresos asociada en ningun trimestre.",
        "cuerpo"))
    out.append(M.p(
        "<b>Lectura, marcada como tal:</b> la IA es hoy, para Intuit, una historia de coste (ya "
        "cobrada: 17% de plantilla) y una promesa de precio (aun no medible). No es una amenaza "
        "existencial demostrada, y quien la use como tal esta usando un titular. El riesgo real no es "
        "que la IA mate a QuickBooks; es que comprima el precio del trabajo humano dentro de TurboTax "
        "Live &mdash;y eso ya esta ocurriendo, medido: ARPU de TT Live &minus;1,4% en FY2026 con "
        "clientes +38%.", "cuerpo"))

    out.append(M.p("<b>4.4 &middot; Direct File, con rigor: la amenaza es real y esta muerta hoy.</b> "
                   "[HECHO, 10-Q de Intuit] Direct File esta SUSPENDIDO, y lo declara el propio filing "
                   "de la empresa. Ese es el estado a dia de hoy y no admite matiz.", "cuerpo"))
    out.append(M.callout("LECCIÓN TRANSFERIBLE",
        'El dato que retira el marco bajista de la casa, y hay que retirarlo: <i>"pierde cuota en un '
        'mercado que crece"</i> es cierto <b>y esta mal interpretado</b>. La categoria DIY del IRS '
        "crecio +1,7% en la temporada 2026 (e-file autopreparado 64.601 &rarr; 65.730 miles, corte del "
        "8-may) mientras el total de declaraciones caia &minus;0,6%. Pero la cuota se cede en el suelo "
        "del mercado, contra el precio CERO, donde nunca hubo moat, y el CEO admitio la derrota con "
        "esas palabras. La prueba esta en el unico rival de pago a escala: <b>H&amp;R Block perdio "
        "&minus;3,8% de volumen DIY de pago con una subida de precio de solo +4,2%, mientras TurboTax "
        "hacia +2% de unidades de pago con +11% de ARPU.</b> Nadie de pago esta ganando lo que "
        "TurboTax cede."))
    out.append(M.p(
        "Lo que si queda vivo de Direct File como riesgo: es un riesgo politico, binario y no "
        "descontable, con una probabilidad que depende de una administracion y no de una empresa. La "
        "forma correcta de tratarlo en este marco no es meterlo en la senda de crecimiento &mdash;eso "
        "seria falsa precision&mdash; sino nombrarlo como riesgo de cola y limitarlo por tamano de "
        "posicion. Con la posicion al 6,03% del NAV y un tope de ruina del 15%, esta limitado.",
        "cuerpo"))
    out.append(PageBreak())
    return out


def seccion_5():
    out = M.flag_titulo("5 &middot; La valoracion",
                        "El motor produce un rango de 171 a 533 dolares; la disputa no es aritmetica, "
                        "son tres insumos")

    out.append(M.p("<b>5.1 &middot; El motor, declarado antes de los numeros.</b>", "cuerpo"))
    filas = [
        ["Parametro", "Valor"],
        ["Tasa", "r = Y10 + 5,00 pp, piso 8,50%. Y10 = 4,69% (H.15) &rarr; r = 9,69%. Sin beta, sin "
         "prima de pais, identica para toda empresa"],
        ["Motor", "DCF convencional a 10 anos sobre owner earnings, senda de crecimiento declarada y "
         "decreciente linealmente de g&#8320; (ano 1) a g&#8734; (ano 10), terminal por Gordon a "
         "g&#8734;, descuento a r"],
        ["Puente", "EV &minus; deuda neta 1.327 M (5.973 &minus; 2.884 &minus; 1.668 &minus; 94) "
         "&divide; 273,537 M acciones (dei:EntityCommonStockSharesOutstanding, 14-may-2026)"],
        ["Prueba de coherencia", "Comprar a valor justo (MoS = 0) debe devolver TIR = r al centimo. "
         "<b>La pasa: MoS 0 &rarr; TIR 9,690%</b>"],
        ["Prueba de replicacion", "El motor reproduce la matriz del diablo celda a celda (base 3.982, "
         "g&#8734; 3,58%: el publica 269-345 para g&#8320; 6&rarr;12%; se obtiene 268-344) y las "
         "salidas del angel dentro del 1% (496/441/383/307 contra 492/442/379/303). Lo que se discute "
         "no es aritmetica: son tres insumos"],
    ]
    out.append(M.tabla(filas, [3.2 * cm, 13.8 * cm], font_sz=8.2))
    out.append(Spacer(1, 8))

    out.append(M.p("<b>5.2 &middot; Los tres insumos en disputa, resueltos.</b>", "cuerpo"))
    out.append(M.p("<b>(A) La base de owner earnings.</b> El metodo manda: FCF menos SBC medida como "
                   "dilucion neta real (nunca la media ponderada diluida) mas los impuestos de "
                   "net-share settlement de financiacion. FY2025: FCF = 6.207 &minus; 84 = 6.123 M. "
                   "Acciones emitidas bajo planes de empleado netas de retenidas: 3.180 mil. Impuestos "
                   "de retencion en vesting (financiacion): 982 M. A precio de hoy (364,53): "
                   "1.159 + 982 = 2.141 M de coste real de retribucion &rarr; <b>OE = 3.982 M</b>. El "
                   "angel llega, por otro camino, a ~2.080 M cargando el gasto contable completo. Las "
                   "dos camaras convergen en ~2,1 B: ese punto esta cerrado.", "cuerpo"))
    out.append(M.p(
        "Lo que sigue abierto es el ano base. Angel: FY2026E = 5.100 M. Diablo: FY2025 = 3.982 M. La "
        "normalizacion de FY2026 &mdash;quitando el vuelco de impuestos diferidos que el diablo "
        "demostro y que el angel concede&mdash; da ~4.250 M. <b>D3, juicio puro. GANA EL DIABLO. Base "
        "central = 3.982 M.</b> El eje se recorre entero (3.982 / 4.250 / 5.100) porque la base de "
        "owner earnings no esta acotada por ninguna regla.", "cuerpo"))
    out.append(M.callout("PAUSA REFLEXIVA",
        "Un candado que el diablo aporta y que se adopta entero: el flujo de operaciones de 9M FY2026 "
        "sube +1.681 M, de los cuales <b>1.428 M (85%) es el vuelco de la linea de impuestos "
        "diferidos</b> (+1.150 este ano contra &minus;278 el anterior). <b>Prohibido usar el FCF "
        "publicado de FY2026 como base del DCF.</b> Quien lo haga estara capitalizando un desfase "
        "fiscal a perpetuidad."))

    out.append(M.p("<b>(B) g&#8734; &mdash; la correccion del 23-ago, que es lo nuevo.</b> "
                   "g&#8734; = min{4,30% ; ROIIC &times; tasa de reinversion sostenible}, con el ROIIC "
                   "medido en ventana de 4 anos sobre capital invertido total con el fondo de comercio "
                   "dentro, sin apelacion. Ventana mandada (FY2021&rarr;FY2025): diablo 17,01% "
                   "(capital operativo), angel 16,08% (capital total). Los dos por encima de r = "
                   "9,69%. Tasa de reinversion: 103% en esa misma ventana (contiene Mailchimp) contra "
                   "21,7% organica reciente &rarr; 16,63% (capada a 4,30%) contra 3,58%. "
                   "<b>D3, juicio puro. GANA EL DIABLO: g&#8734; = 3,58%.</b> Una reinversion del 103% "
                   "sostenida a perpetuidad es aritmeticamente imposible, y la que la sostuvo fue M&amp;A "
                   "que rinde el 48% de su coste de capital. Se publica igualmente el 4,30% como techo "
                   "del eje.", "cuerpo"))
    out.append(M.p(
        "La guarda NO se activa: C-4 fija la ventana en 4 anos sobre el ultimo ejercicio cerrado, sin "
        "excepcion, y en ella el capital invertido crece 11.308-11.959 M. El ROIIC es medible. El tope "
        "antiguo (g&#8320; &le; g&#8734; + 2 pp) no se hereda. <b>Sin la correccion, g&#8734; = 2,34%</b> "
        "(inflacion implicita: Y10 4,69% &minus; TIPS 10a 2,35%). <b>Con g&#8734; = 0, el techo "
        "terminal cae a 10,32&times;.</b>", "cuerpo"))

    out.append(M.p("<b>(C) g&#8320;.</b> Capada por el minimo de {reinversion &times; ROIC, CAGR "
                   "ingresos 3a, CAGR ingresos 5a, CAGR NOPAT 3a} = min{~17,9% ; 13,95% ; 19,65% ; "
                   "23,53%} = <b>13,95%</b>. Con la ventana organica reciente de 3 anos el termino cae "
                   "a 3,95% y pasaria a ser el minimo vinculante: es un factor de 3,5&times; y es la "
                   "mayor palanca de toda la valoracion. Se resuelve por consistencia de ventana, se "
                   "declara como decision de metodo (no de hecho), y se publica la columna del 3,95% "
                   "en la matriz ampliada. <b>g&#8320; central = 9,00%</b>, declarado como juicio: "
                   "FY2026 imprimira ~+14% de ingresos y ~+16% de operativo; la guia FY2027 recalculada "
                   "a mano dara ~+10,5-11,5%; la cantera gratuita cae &minus;46% en cuatro anos; y la "
                   "senda decrece hasta 3,58%, lo que da un CAGR de owner earnings a diez anos de "
                   "~6,2% contra una empresa que promete EPS &ge;15%.", "cuerpo"))
    out.append(PageBreak())

    out.append(M.p("<b>5.3 &middot; Los numeros.</b>", "cuerpo"))
    out.append(M.p("Matriz 3&times;3 obligatoria &mdash; CON la correccion del 23-ago "
                   "(g&#8734; = 3,58%):", "h3"))
    filas2 = [
        ["Base OE &darr; / g&#8320; &rarr;", "5,58% (tope antiguo)", "9,00% (central)",
         "13,95% (tope min-de-4)"],
        ["3.982 M (FY2025, diablo)", "263 $ &middot; term 57,1% &middot; TIR 8,03%",
         "304 $ &middot; term 58,3% &middot; TIR 8,71%", "372 $ &middot; term 59,8% &middot; "
         "TIR 9,81%"],
        ["4.250 M (FY2026E normalizado)", "281 $ &middot; TIR 8,33%", "325 $ &middot; TIR 9,05%",
         "398 $ &middot; TIR 10,21%"],
        ["5.100 M (angel)", "339 $ &middot; TIR 9,27%", "391 $ &middot; TIR 10,11%",
         "478 $ &middot; TIR 11,46%"],
    ]
    out.append(M.tabla(filas2, [4.4 * cm, 4.2 * cm, 4.2 * cm, 4.2 * cm], font_sz=7.9))
    out.append(M.p("<i>Ratio maximo/minimo = 1,816 &rarr; DECIDIBLE (umbral: &gt;2,0 &rarr; NO "
                   "DECIDIBLE).</i>", "nota"))

    out.append(M.p("La misma matriz &mdash; SIN la correccion (g&#8734; = 2,34%, Enmienda 29 pura):",
                   "h3"))
    filas3 = [
        ["Base OE &darr; / g&#8320; &rarr;", "5,58%", "9,00%", "13,95%"],
        ["3.982 M", "227 $ &middot; TIR 6,98%", "261 $ &middot; term 52,4% &middot; TIR 7,69%",
         "319 $ &middot; TIR 8,83%"],
        ["4.250 M", "242 $", "279 $", "340 $"],
        ["5.100 M", "292 $", "335 $", "409 $"],
    ]
    out.append(M.tabla(filas3, [4.4 * cm, 4.2 * cm, 4.2 * cm, 4.2 * cm], font_sz=7.9))
    out.append(M.p("<i>Ratio maximo/minimo = 1,807 &rarr; DECIDIBLE.</i>", "nota"))
    out.append(Spacer(1, 8))

    out.append(M.p("Las dos salidas obligatorias adicionales:", "h3"))
    filas4 = [
        ["Lectura", "Central (OE 3.982, g&#8320; 9%)", "Peso del terminal", "TIR a 10 anos"],
        ["g&#8734; = 4,30% (techo de la correccion)", "338 $", "62,0%", "9,31%"],
        ["g&#8734; = 0 y techo 10,32&times; (exigencia del diablo)", "209 $", "43,1%", "5,78%"],
    ]
    out.append(M.tabla(filas4, [7.0 * cm, 4.0 * cm, 3.3 * cm, 2.7 * cm], font_sz=8.0))
    out.append(M.p(
        "<b>Peso del terminal: 43,1% a 63,5% en todas las lecturas. Nunca supera el 75%</b>, luego el "
        "veredicto con g&#8734; = 0 no es obligatorio por esa via. Se publica porque el diablo lo "
        "exige por otra via (la ventana desfavorable del ROIIC) y porque es el suelo del caso. "
        "<b>Extremos absolutos de la matriz ampliada: minimo 171 $ (OE 3.982 &middot; g&#8320; 3,95% "
        "&middot; g&#8734; 0). Maximo 533 $ (OE 5.100 &middot; g&#8320; 13,95% &middot; g&#8734; "
        "4,30%). Ratio 3,12</b> &mdash; por eso la matriz obligatoria es la 3&times;3 y no el barrido "
        "libre.", "cuerpo"))

    out.append(M.chart("charts/c4_banda_valoracion.png"))
    out.append(PageBreak())
    out.append(M.chart("charts/c5_matriz_sensibilidad.png"))
    out.append(Spacer(1, 8))

    out.append(M.callout("LECCIÓN TRANSFERIBLE",
        "<b>El numero que resuelve el cargo decisivo del diablo.</b> La celda mas dura de toda la "
        "matriz &mdash;OE 3.982, g&#8320; 3,95% (la lectura organica pura), g&#8734; = 0, techo "
        "10,32&times;&mdash; vale <b>170,84 $ y devuelve una TIR a diez anos de 4,690%</b>. El Tesoro "
        "a diez anos esta al 4,69%. Es decir: en el peor escenario que este metodo admite, comprar "
        "Intuit a 364,53 empata con el efectivo. No pierde contra el. Y en el escenario central con "
        "la correccion, la TIR es 8,71%: 402 puntos basicos por encima.<br/><br/>"
        "El diablo afirma lo contrario &mdash;“el activo rinde 3,05-3,94% contra un Tesoro al "
        "4,69%”&mdash; usando el rendimiento estatico de owner earnings sobre EV (que es 3,94% "
        "con su propia base, y se confirma) frente a una TIR a diez anos. Son unidades distintas. El "
        "rendimiento estatico supone crecimiento cero y ningun reinvertimiento, un escenario mas duro "
        "incluso que la celda de g&#8734; = 0. <b>Es el mismo error de unidades del que el acusa "
        "&mdash;con razon&mdash; a la tesis de cosecha cuando compara una serie de clientes contra una "
        "serie de ingresos.</b>"))

    out.append(M.p("<b>5.4 &middot; El contexto que ninguna de las dos camaras vio, y que reencuadra "
                   "todo.</b> [HECHO, barras de precio de IBKR, contrato 270662, extraidas el "
                   "24-ago-2026]", "cuerpo"))
    filas5 = [
        ["", "Precio", "EV", "EV / OE (3.982)", "OE / EV"],
        ["Maximo de cierre 52s &mdash; 22-sep-2025", "702,09", "193.375", "48,6&times;", "2,06%"],
        ["Minimo de cierre 12m &mdash; sem. 22-jun-2026", "255,07", "71.098", "17,9&times;", "5,60%"],
        ["Coste medio de la posicion de Felipe", "262,23", "73.057", "18,3&times;", "5,45%"],
        ["Cierre 21-ago-2026 (encargo)", "364,53", "101.039", "25,4&times;", "3,94%"],
        ["Ultimo precio, 24-ago (barra parcial)", "369,49", "102.396", "25,7&times;", "3,89%"],
    ]
    out.append(M.tabla(filas5, [6.4 * cm, 2.6 * cm, 2.6 * cm, 2.9 * cm, 2.5 * cm], font_sz=8.0))
    out.append(Spacer(1, 6))
    out.append(M.chart("charts/c2_precio_multiplo.png"))
    out.append(Spacer(1, 6))
    out.append(M.p(
        "<b>Tres consecuencias, y son grandes:</b> (1) El mercado ya hizo la rebaja. Intuit cayo "
        "&minus;63,7% de cierre a cierre en nueve meses y ha rebotado +43% en ocho semanas. Las dos "
        "camaras escribieron sus cargos tratando 364,53 como un dato estable. No lo es. (2) El trigger "
        "permanente de drawdown esta ENCENDIDO y gates.md no lo registraba: desde el maximo de cierre "
        "de 52 semanas (702,09) hasta 364,53 hay &minus;48,1%, casi el doble del umbral del 25%. "
        "(3) Discrepancia de precio declarada: el encargo fija el cierre del 21-ago en 364,53; la "
        "barra diaria de IBKR da 367,00 para esa sesion. Diferencia 0,68%. Se usa 364,53 en toda la "
        "aritmetica por mandato del encargo. Ninguna conclusion de este documento cambia de signo con "
        "2,47 USD.", "cuerpo"))
    out.append(PageBreak())

    out.append(M.p("<b>5.5 &middot; El candado de recompra, entero y en contra.</b> [HECHO, estado de "
                   "patrimonio del 10-K FY2025 y del 10-Q Q3 FY2026]", "cuerpo"))
    filas6 = [
        ["Ejercicio", "Recompradas", "Importe", "Precio medio"],
        ["FY2023", "4.700 mil", "1.967 M", "418,51 $"],
        ["FY2024", "3.427 mil", "1.978 M", "577,06 $"],
        ["FY2025", "4.319 mil", "2.793 M", "646,68 $"],
        ["Q3 FY2026", "3.749 mil", "1.561 M", "416,38 $"],
    ]
    out.append(M.tabla(filas6, [4.0 * cm, 4.0 * cm, 4.0 * cm, 4.0 * cm], font_sz=8.4))
    out.append(Spacer(1, 6))
    out.append(M.p(
        "Total FY2023-FY2025: 6.738 M por 12.446 mil acciones, media 541,38 $. Y el contador neto solo "
        "bajo de 281.932 a 279.129 mil: <b>2.403 USD de caja por cada accion neta retirada</b>, contra "
        "un precio de mercado de 364,53.", "cuerpo"))
    out.append(M.callout("PAUSA REFLEXIVA",
        "<b>Cuantificacion del dano:</b> comprando 6.738 M a 541,38 medios contra un valor central de "
        "304, se destruyo 6.738 &times; (1 &minus; 304/541,38) = <b>~2.955 M, equivalente a 10,80 USD "
        "por accion</b>. Es dinero ya gastado y no se descuenta otra vez del valor de hoy, porque ya "
        "esta dentro del balance y del contador de acciones. <b>Regla hacia delante:</b> mientras el "
        "precio supere P_justo, cada dolar de recompra destruye (1 &minus; V/P) de si mismo. A 364,53 "
        "contra 304, eso son 16,6 centimos por dolar. La recompra del Q3 FY2026 se ejecuto a 416,38, "
        "un 37% por encima del valor central: el candado ya esta mordiendo hoy.<br/><br/>"
        "<b>El contrapeso del angel, tambien cierto:</b> con la metrica que el propio metodo ordena, "
        "el contador paso de 280.292 (ago-2024) a 273.537 (14-may-2026): &minus;2,41% en 21 meses. "
        "<b>La dilucion neta real es NEGATIVA.</b> Ambas cosas son verdad a la vez: la dilucion esta "
        "resuelta y el precio pagado por resolverla fue malo."))

    out.append(M.p("<b>5.6 &middot; Y el hecho de balance que hay que mirar sin parpadear.</b> "
                   "[HECHO, balance del 10-K FY2025] Patrimonio 19.710 &minus; fondo de comercio "
                   "13.980 &minus; intangibles adquiridos netos 5.302 = <b>428 M de patrimonio "
                   "tangible. 1,56 USD por accion. El 2,2% del patrimonio declarado.</b> Fondo de "
                   "comercio por segmento a 31-jul-2025: GBS 9.825 &middot; Consumer 51 &middot; "
                   "Credit Karma 4.007 &middot; ProTax 97. Y desde el 20-may-2026, en dos cubos: "
                   "GBS 9.822 &middot; Consumer 4.160.", "cuerpo"))
    out.append(M.p(
        "Lo que esto significa y lo que no. No significa que Intuit sea fragil: un negocio con "
        "margenes de segmento del 76,9% y capex del 0,66% de los ingresos no necesita patrimonio "
        "tangible. <b>Significa que el ROIC contable del 18-20% descansa sobre un denominador que "
        "contiene 13.980 M de fondo de comercio nunca deteriorado</b>, y que un deterioro de 5.000 M "
        "subiria el ROIC contable en el acto. La ausencia de cargo no es prueba de salud del activo: "
        "es prueba de que la prueba de deterioro se hace sobre una unidad que contiene QuickBooks. El "
        "diablo tiene toda la razon en esto y se adopta.", "cuerpo"))
    out.append(PageBreak())
    return out
