# -*- coding: utf-8 -*-
"""CONTENIDO · NIVEL 2 · EL NEGOCIO — Ultra Tesis DECK (25-ago-2026).

Expone: parte_2(), seccion_2(), seccion_3(), seccion_4(), seccion_5().
Cada función devuelve una LISTA de flowables de ReportLab.

  §2 · Qué compras cuando compras Deckers — dos marcas, ninguna fábrica
  §3 · Los tres márgenes, sobre una zapatilla de 150 dólares
  §4 · El mapa del dinero — marca, canal, geografía; unidades contra precio
  §5 · Por qué rinde el 101% sobre el capital

Reglas propias de este nivel:
  · Tono de profesor. Segunda persona cuando enseña.
  · Ni un múltiplo, ni una tasa de descuento, ni un precio objetivo. Eso es el nivel 4.
  · Todo término técnico se define en el sitio donde aparece por primera vez.
  · Toda cifra procede de DATOS.md. Cero cifras de otra fuente.
"""
import motor_qg as M
from reportlab.platypus import Spacer, PageBreak, KeepTogether
from reportlab.lib.units import cm


# ═══════════════════════════════════════════════════════════════════════
#  PORTADILLA DE PARTE
# ═══════════════════════════════════════════════════════════════════════
def parte_2():
    out = []
    out += M.portadilla(
        "2", "El negocio",
        "Qué es Deckers, explicado sin un solo múltiplo — aquí se aprende el "
        "vocabulario que la valoración dará por sabido")

    out.append(M.p(
        "El nivel anterior dio la respuesta sin el razonamiento. Éste no contiene ni un precio "
        "objetivo ni una sola de las cuentas que deciden el veredicto. Contiene lo que hace falta "
        "antes: <b>qué es exactamente esta empresa, de dónde sale cada dólar que entra y qué queda "
        "de él.</b> Aquí se aprenden cuatro palabras —margen bruto, margen operativo, capital "
        "invertido y ROIC— que el nivel 4 usará como si las supieras de siempre. Si abandonas al "
        "acabar este bloque te llevas algo completo: sabrás describir el negocio de Deckers mejor "
        "que la mayoría de quien lo comenta.", "cuerpo"))

    out.append(M.respiro(0.2))
    out.append(M.tabla([
        ["Sección", "La pregunta que contesta", "Palabra nueva"],
        ["<b>§2</b> · Qué compras",
         "Si no tiene fábricas, ¿qué es exactamente lo que se compra?",
         "permiso para cobrar caro"],
        ["<b>§3</b> · Los tres márgenes",
         "De 150 dólares que paga un cliente, ¿cuántos se queda la empresa, y en qué escalón se "
         "pierde el resto?",
         "margen bruto, operativo y neto"],
        ["<b>§4</b> · El mapa del dinero",
         "¿Qué parte del crecimiento fue vender más pares, y qué parte cobrarlos más caros?",
         "precio contra unidades"],
        ["<b>§5</b> · El 101%",
         "¿Cuánto dinero hay que dejar metido dentro para que esto funcione, y cuánto devuelve al "
         "año?",
         "capital invertido, NOPAT, ROIC"],
    ], col_w=[3.6 * cm, 8.8 * cm, 4.6 * cm], font_sz=8.4))

    out.append(M.respiro(0.25))
    out.append(M.p(
        "Una promesa de lectura: en las páginas que siguen no aparece la palabra «barata» ni la "
        "palabra «cara». Calidad y precio son dos preguntas distintas, y mezclarlas es la forma más "
        "común de equivocarse. Aquí sólo se contesta la primera.", "nota"))

    out.append(PageBreak())
    return out


# ═══════════════════════════════════════════════════════════════════════
#  §2 · QUÉ COMPRAS CUANDO COMPRAS DECKERS
# ═══════════════════════════════════════════════════════════════════════
def seccion_2():
    out = M.flag_titulo(
        "§2 · Qué compras cuando compras Deckers",
        "Dos marcas, ninguna fábrica — y la única pregunta que gobierna el documento entero")

    out.append(M.p(
        "<b>Cuando compras una acción de Deckers no compras una fábrica. No compras ni una.</b> "
        "Compras dos marcas y la red que las pone delante del cliente. Conviene decirlo así de "
        "crudo en el primer párrafo, porque todo lo demás —el margen del 57,7%, los 1.602,6 "
        "millones de caja, el retorno del 101% sobre el capital— es consecuencia de que esos dos "
        "nombres puedan seguir cobrando caro.", "cuerpo"))

    out.append(M.p(
        "Físicamente: Deckers diseña un modelo, lo encarga a fábricas independientes del sudeste "
        "asiático, paga el producto terminado y lo vende de dos maneras —a tiendas ajenas que lo "
        "revenden, y directamente al consumidor en sus 203 tiendas propias y en su web—. Entre el "
        "zapato y el cliente hay una marca. Entre Deckers y el zapato no hay ninguna máquina que "
        "sea suya. <i>[HECHO — 10-K FY2026: 203 tiendas al 31-mar-2026, 49 en Estados Unidos.]</i>",
        "cuerpo"))

    out.append(M.tabla([
        ["Marca", "Qué vende, en una línea", "FY2026", "Peso", "Var. i.a."],
        ["<b>UGG</b>",
         "Bota de piel de oveja, de 1978. La compra quien ya la conoce y la sustituye cuando se "
         "gasta.",
         "<b>2.738,8</b>", "<b>50,0%</b>", "+8,2%"],
        ["<b>HOKA</b>",
         "Zapatilla de correr de suela gruesa. La compra el corredor que busca amortiguación y "
         "repite modelo.",
         "<b>2.587,3</b>", "<b>47,3%</b>", "+15,9%"],
        ["Otras",
         "Teva y el resto. Deckers vendió Sanuk en agosto de 2024, liquidó Koolaburra y retiró AHNU "
         "en menos de tres ejercicios.",
         "146,2", "2,7%", "<b>&minus;33,9%</b>"],
    ], col_w=[1.9 * cm, 8.3 * cm, 2.4 * cm, 1.9 * cm, 2.4 * cm], font_sz=8.2))
    out.append(M.p(
        "<i>[HECHO — 10-K FY2026 (acc. 0001628280-26-037664) y 8-K del 21-may-2026. Millones de "
        "dólares; los pesos son cálculo propio sobre 5.472,3 M de ingresos.]</i>", "nota"))

    out.append(M.p(
        "Mira la tercera fila antes que las dos primeras. Deckers ha salido de tres marcas en tres "
        "años: no es un conglomerado de calzado que reparte apuestas, es una empresa que probó a "
        "serlo, no le salió y se replegó sobre lo que funciona. <b>El 97,3% de los ingresos son dos "
        "nombres</b>, y uno de los dos vende una bota de piel de oveja que cualquier fábrica del "
        "mundo sabe hacer y que se copia constantemente.", "cuerpo"))

    # ── LAS DOS CARAS DEL MISMO HECHO ───────────────────────────────────
    out.append(M.p("No tener fábricas: la cara buena y la cara mala", "h2"))

    out.append(M.p(
        "La buena es enorme: <b>crecer no exige enterrar dinero.</b> Si vendieras coches, un 10% "
        "más de coches significaría ampliar una planta, con cientos de millones hundidos en "
        "hormigón dos años antes de cobrar el primer euro. Deckers, para vender un 10% más de "
        "zapatos, firma más pedidos. El recibo está en el último ejercicio: los ingresos subieron "
        "486,7 M, de 4.985,6 a 5.472,3, y para conseguirlo gastó <b>84,6 M en instalaciones</b> y "
        "<b>redujo</b> inventario, de 495,2 a 487,0. Vendió más con menos producto parado en el "
        "almacén; un fabricante de verdad no puede hacer eso ningún año. <i>[HECHO — 10-K "
        "FY2026.]</i>", "cuerpo"))

    out.append(M.p("La cara mala: la barrera industrial no existe", "h3"))

    out.append(M.p(
        "La mala hay que decirla con la misma fuerza: <b>si tú no necesitas fábrica, tu competidor "
        "tampoco.</b> La barrera de entrada industrial —la que protege a una acería o a una red "
        "eléctrica— aquí no existe. Las mismas fábricas de Vietnam y de Indonesia producen para "
        "cualquiera que llegue con un diseño y una orden de compra, y no hay patente que lo impida: "
        "las espumas y las placas se rodean en dos o tres años, y una bota de piel de oveja no "
        "tiene ni eso. Lo único que separa a Deckers de un recién llegado con el mismo proveedor es "
        "que el cliente pague más por el mismo objeto porque lleva un nombre estampado. A eso lo "
        "llamaré, en todo el documento, <b>el permiso para cobrar caro</b>: no es una metáfora, es "
        "literalmente lo que se compra, y es revocable sin previo aviso.", "cuerpo"))

    # ── LA CADENA DE SUMINISTRO ─────────────────────────────────────────
    out.append(M.p("Dónde se fabrica de verdad, y el punto único de fallo", "h2"))

    out.append(M.p(
        "Dos frases del mismo documento oficial apuntan en direcciones opuestas, y las dos son "
        "ciertas. La tranquilizadora: <i>«During the year ended March 31, 2026, production of our "
        "finished goods was predominantly from Vietnam and Indonesia, while less than 5% was from "
        "China or any other individual country.»</i> Dos ejercicios antes, el 10-K de FY2024 aún "
        "decía <i>«most of our products are manufactured in China and Vietnam»</i>. La empresa se "
        "movió, y deprisa. <i>[HECHO — citas literales.]</i>", "cuerpo"))

    out.append(M.p(
        "La otra está en el apartado de riesgos y desmonta la lectura cómoda de la primera: "
        "<i>«Sheepskin is in high demand and sourced primarily from Australia and processed largely "
        "by two tanneries in China capable of meeting our quality, volume, and animal welfare "
        "standards. This geographic and supplier concentration exposes us to supply disruption "
        "risk.»</i> <i>[HECHO — cita literal, 10-K FY2026, Item 1A.]</i>", "cuerpo"))

    out.append(M.p("Por qué la primera frase engaña si se lee sola", "h3"))

    out.append(M.p(
        "Léelas juntas y verás por qué la primera engaña si se lee sola. <b>El «menos del 5%» mide "
        "producto terminado, no insumo.</b> Aguas arriba, la piel de oveja australiana de UGG pasa "
        "por <b>dos curtidurías, las dos en China</b>: dos plantas para la materia prima de la "
        "marca que aporta el 50,0% de las ventas, con el propio filing admitiendo que si dejan de "
        "operar puede no haber sustituto aceptable. Cualquier titular que diga «Deckers ya salió de "
        "China» es falso: salió con el zapato, no con la piel.", "cuerpo"))

    out.append(M.callout("CASO HISTÓRICO",
        "<b>Qué ocurre cuando una marca pierde el permiso para cobrar caro.</b> Under Armour pasó "
        "de disputarle a Nike el escaparate del deportista a ser un nombre que el consumidor "
        "esperaba encontrar rebajado. No perdió una fábrica, ni una patente, ni un cliente "
        "institucional: perdió la disposición del comprador a pagar el precio de etiqueta, con el "
        "producto idéntico la semana antes y la semana después. Cuando ese permiso se retira, el "
        "descuento es la única herramienta que queda, y descontar acelera lo que se pretendía "
        "frenar. <b>Deckers ya lo vivió en casa:</b> compró Sanuk, la deterioró contablemente por "
        "118,0 M en FY2017 y acabó vendiéndola en agosto de 2024. Una marca de calzado no muere de "
        "una crisis financiera; muere de una temporada en la que deja de justificar su precio."))

    out.append(M.p(
        "Ya tienes el planteamiento: un negocio ligero, sin deuda financiera, con dos marcas que "
        "hoy cobran caro, sin barrera industrial que lo proteja y con un cuello de botella físico "
        "declarado por escrito sobre la mitad de sus ventas. <b>Todos los riesgos de esta tesis son "
        "variantes de una sola pregunta, y es la que gobierna el documento entero:</b>", "cuerpo"))

    out.append(KeepTogether([
        M.p('<font size="16" color="#C60C2A"><b>¿Cuántos años dura el permiso?</b></font>', "h2"),
        M.p(
            "No se contesta con una fórmula, y quien diga que tiene una está vendiendo algo. Se "
            "contesta acumulando indicios: qué margen defiende cada marca (§3 y §7), quién compra de "
            "verdad y quién sólo coloca producto (§4 y §8) y qué mecanismo sostiene el precio pleno "
            "(§10).", "nota"),
    ]))

    out.append(PageBreak())
    return out


# ═══════════════════════════════════════════════════════════════════════
#  §3 · LOS TRES MÁRGENES, SOBRE UNA ZAPATILLA DE 150 DÓLARES
# ═══════════════════════════════════════════════════════════════════════
def seccion_3():
    out = M.flag_titulo(
        "§3 · Los tres márgenes, sobre una zapatilla de 150 dólares",
        "Bruto, operativo y neto — tres preguntas distintas que casi todo el mundo confunde en una")

    out.append(M.p(
        "<b>De cada 150 dólares que un cliente le paga a Deckers, a Deckers le quedan 28,07.</b> "
        "Lo que importa es dónde se van los otros 121,93, porque cada escalón perdido contesta una "
        "pregunta distinta. Un margen no es contabilidad: es un termómetro, y hay tres midiendo "
        "cosas que no tienen nada que ver entre sí. <i>[HECHO: los tres márgenes, del 10-K FY2026. "
        "INFERENCIA: su aplicación a un par ilustrativo de 150 dólares.]</i>", "cuerpo"))

    out.append(M.figura(
        "charts/c02_zapatilla_margenes.png", w_cm=16.6,
        pie="Cada barra roja es dinero que sale y no vuelve: la primera —63,45— es lo que costó "
            "fabricar y traer el zapato; la segunda —51,93—, toda la estructura que hace que "
            "alguien lo quiera y lo encuentre."))

    # ── EL PRIMERO ──────────────────────────────────────────────────────
    out.append(M.p("Primer escalón · El margen bruto, o el detector de mentiras", "h2"))

    out.append(M.p(
        "<b>Margen bruto</b> es lo que queda del precio de venta tras descontar lo que costó el "
        "producto: fábrica, materiales, transporte, arancel. En Deckers, <b>57,7%</b>: de cada 150 "
        "dólares, 63,45 son el zapato y 86,55 son el nombre.", "cuerpo"))

    out.append(M.p(
        "Detente aquí, porque de los tres es el único que no se puede fingir. Los otros dos se "
        "mejoran recortando: despides gente, cierras tiendas, bajas publicidad, y suben un par de "
        "años. El bruto no, porque tiene sólo dos palancas y las dos son externas: <b>o el cliente "
        "acepta pagar más, o al proveedor le cuesta menos producir.</b> Nada más. Por eso es el "
        "detector de mentiras de una marca de consumo. Y el historial de Deckers es notable: del "
        "51,0% de FY2022 al 57,7% de FY2026, casi siete puntos en cuatro ejercicios en un sector "
        "donde lo normal es perderlos. Eso no se consigue recortando, sino vendiendo a precio "
        "pleno, decisión que hay que volver a tomar cada trimestre.", "cuerpo"))

    # ── EL SEGUNDO ──────────────────────────────────────────────────────
    out.append(M.p("Segundo escalón · El margen operativo, o cuánto cuesta la máquina", "h2"))

    out.append(M.p(
        "De los 86,55 que quedaban se van 51,93 en gastos de estructura —en la jerga contable, "
        "<b>SG&amp;A</b>: publicidad, patrocinios, sueldos, el alquiler de las 203 tiendas, la "
        "logística, los sistemas—. El resultado, <b>34,62 dólares por par</b>, es el <b>beneficio "
        "operativo</b> —o EBIT, por sus siglas inglesas—, y sobre el precio de venta es el "
        "<b>margen operativo: 23,08%</b>. Si el bruto mide poder de precio, éste mide eficiencia: "
        "cuánto cuesta mantener en pie la máquina que convierte producto en deseo.", "cuerpo"))

    out.append(M.p(
        "Y es donde vive el problema de esta empresa. El dato, sin interpretar: en FY2026 el margen "
        "bruto bajó 20 puntos básicos —de 57,9% a 57,7%— y el operativo bajó 57 —de 23,65% a "
        "23,08%—. El zapato aguantó su precio; la estructura creció más deprisa que las ventas. "
        "<i>Un punto básico es una centésima de punto porcentual.</i>", "cuerpo"))

    # ── EL TERCERO ──────────────────────────────────────────────────────
    out.append(M.p("Tercer escalón · El margen neto, o lo que de verdad queda", "h2"))

    out.append(M.p(
        "Del beneficio operativo salen los impuestos y entran los ingresos financieros de la caja. "
        "Neto de todo: <b>28,07 dólares del par de 150</b>, un <b>margen neto del 18,7%</b>. Es el "
        "número que la prensa llama «beneficio» y el menos informativo de los tres, porque mezcla "
        "el negocio con dos cosas que no lo son: la fiscalidad y el rendimiento del dinero parado.",
        "cuerpo"))

    out.append(M.callout("LECCIÓN TRANSFERIBLE",
        "Vale para cualquier negocio de marca que analices. <b>El margen bruto sólo puede subir por "
        "dos vías: que el cliente acepte pagar más, o que a ti te cueste menos producir.</b> No hay "
        "una tercera. De ahí la regla práctica: tres años seguidos de margen bruto cayendo en una "
        "marca de consumo no son un problema de costes ni un ciclo de materias primas; son <b>una "
        "marca que perdió el derecho a cobrar caro</b> y lo tapa con descuento. La cuenta de "
        "resultados tarda dos o tres ejercicios en admitirlo; el margen bruto lo dice el primero."))

    # ── LA GUÍA ─────────────────────────────────────────────────────────
    out.append(M.p("Y lo que la propia empresa dice que va a pasar", "h2"))

    out.append(M.p(
        "No es una previsión mía: es la guía que la dirección publicó el 21 de mayo de 2026 y subió "
        "el 23 de julio. Baja los tres escalones a la vez.", "cuerpo"))

    out.append(M.tabla([
        ["Escalón", "FY2026 realizado", "Guía FY2027", "Diferencia"],
        ["<b>Margen bruto</b>", "57,7%", "«algo mejor que 56,5%»", "<b>&minus;120 pb</b>"],
        ["<b>Margen operativo</b>", "23,08%", "«algo mejor que 21,5%»", "<b>&minus;155 pb</b>"],
        ["Beneficio neto", "1.024,1 M",
         "978-988 M implícitos en un BPA de 7,35-7,50", "<b>&minus;4%</b>"],
        ["Ingresos", "5.472,3 M", "5.860-5.910 M", "+7,1% a +8,0%"],
    ], col_w=[3.9 * cm, 3.5 * cm, 6.4 * cm, 2.9 * cm], font_sz=8.2))
    out.append(M.p(
        "<i>[HECHO — guía del 21-may-2026, subida el 23-jul-2026. INFERENCIA — el neto implícito "
        "sale del punto medio del BPA guiado, 7,425, por unos 133 millones de acciones. «pb» = "
        "puntos básicos.]</i>", "nota"))

    out.append(M.p(
        "Es la primera tensión real del documento. <b>Las ventas suben entre un 7% y un 8% y el "
        "beneficio neto baja un 4%:</b> la empresa espera vender más y ganar menos. El beneficio "
        "por acción sube igualmente —de 7,02 a 7,35-7,50— pero no porque el negocio gane más, sino "
        "porque habrá un 9% menos de acciones entre las que repartirlo.", "cuerpo"))

    out.append(PageBreak())
    return out


# ═══════════════════════════════════════════════════════════════════════
#  §4 · EL MAPA DEL DINERO
# ═══════════════════════════════════════════════════════════════════════
def seccion_4():
    out = M.flag_titulo(
        "§4 · El mapa del dinero",
        "Los mismos 5.472,3 millones, contados por marca, por canal y por geografía — "
        "y la descomposición que decide cualquier tesis de marca")

    out.append(M.p(
        "Deckers ingresó <b>5.472,3 millones de dólares</b> en el ejercicio cerrado el 31 de marzo "
        "de 2026, un 9,8% más. El resto de la sección son tres maneras de partir esa cifra, y no es "
        "contabilidad: <b>cada corte contesta una pregunta distinta, y en dos de los tres hay un "
        "trozo parado.</b> <i>[HECHO — 10-K FY2026 y 8-K del 21-may-2026.]</i>", "cuerpo"))

    out.append(M.figura(
        "charts/c01_mapa_dinero.png", w_cm=16.6,
        pie="Las tres barras suman lo mismo. Lo que hay que buscar en un mapa así no es lo que "
            "crece, sino lo que no se mueve."))

    # ── EL CANAL ────────────────────────────────────────────────────────
    out.append(M.p("Qué es el canal, y por qué la venta directa deja más", "h2"))

    out.append(M.p(
        "El segundo corte es el que menos gente entiende y el que más dice. <b>Mayorista</b> es "
        "vender a otro que revende: una cadena de deportes, un especialista de running. Deckers le "
        "factura una fracción del precio de etiqueta y el minorista se queda el resto por ponerlo "
        "en su escaparate y financiar el inventario: Deckers cobra menos por par, pero de golpe y "
        "sin alquiler ni dependientes. Son 3.208,1 M, un +12,3%.", "cuerpo"))

    out.append(M.p(
        "<b>Venta directa al consumidor</b> —en la jerga, DTC— es vender en tienda propia o en la "
        "web: 2.264,2 M, un +6,3%. Aquí Deckers cobra el precio de etiqueta entero y se queda "
        "también el margen del minorista. Por eso <b>la venta directa deja más margen</b>: no "
        "porque el zapato sea distinto, sino porque hay un intermediario menos repartiendo. A "
        "cambio asume alquiler, nómina, inventario parado y el coste de traer al cliente.",
        "cuerpo"))

    out.append(M.p("La diferencia que no es contable: comprar no es consumir", "h3"))

    out.append(M.p(
        "Hay una segunda diferencia, menos contable y más importante: <b>el mayorista mide lo que "
        "las tiendas compran; la venta directa mide lo que los consumidores compran.</b> No son lo "
        "mismo y pueden separarse muchos trimestres antes de que se note. Guarda el matiz con su "
        "cifra: el comparable de la venta directa —sólo tiendas y web con más de un año de vida— "
        "creció un <b>+4,6%</b> frente al +12,3% del mayorista. Es la sección §8 entera.", "cuerpo"))

    # ── PRECIO CONTRA UNIDADES ──────────────────────────────────────────
    out.append(M.p("La descomposición que decide cualquier tesis de marca", "h2"))

    out.append(M.p(
        "Cuando los ingresos de una marca suben un 9,8%, esa cifra sola no significa nada: puede "
        "haberse conseguido de dos maneras opuestas —<b>vendiendo más pares, o cobrando más caro "
        "cada par</b>— y las dos envejecen de forma completamente distinta.", "cuerpo"))

    out.append(M.p(
        '<font size="13" color="#C60C2A"><b>unidades +6,2% &nbsp; más &nbsp; precio y mezcla '
        '+3,4 puntos &nbsp; = &nbsp; ingresos +9,8%</b></font>', "h2"))
    out.append(M.p(
        "Deckers vendió 78.700 miles de pares y artículos frente a 74.100 el año anterior. Como los "
        "ingresos crecieron más que las unidades, la diferencia la aportaron el precio y la mezcla "
        "—vender proporcionalmente más de lo caro—. A divisa constante el crecimiento fue del "
        "+9,0%. <i>[HECHO en unidades e ingresos; INFERENCIA en el reparto, que no se publica "
        "desagregado.]</i>", "nota"))

    out.append(M.p(
        "Dos tercios de volumen y un tercio de precio es un reparto sano: Deckers sube precios "
        "<b>sin destruir la unidad</b>. Ésa es la firma de una marca con el permiso vigente.",
        "cuerpo"))

    out.append(M.p("Invierte el problema: el mismo +9,8%, tres empresas distintas", "h3"))

    out.append(M.p(
        "Ahora invierte el problema. Mismo +9,8%, otro reparto: unidades <b>planas</b> y precio "
        "+9,8%. Línea de ingresos idéntica, negocio distinto —una marca que ya no capta clientes "
        "nuevos y exprime a los que tiene—; parece sana dos años y se rompe al tercero, porque el "
        "precio tiene techo y el volumen no. El reparto contrario, unidades +9,8% y precio plano, "
        "es una marca creciendo a base de regalar margen. <b>La misma cifra describe tres empresas "
        "distintas según cómo se reparta, y sólo una de las tres es comprable.</b> Por eso lo que "
        "hay que vigilar no es el 3,4% de precio: es si el 6,2% de unidades sobrevive al año que "
        "viene.", "cuerpo"))

    # ── LOS DOS PARADOS ─────────────────────────────────────────────────
    out.append(M.p("Y los dos trozos que no se mueven", "h2"))

    out.append(M.p(
        "Vuelve al mapa. El primero es pequeño y ya estaba descontado: las otras marcas caen un "
        "33,9%, hasta 146,2 M, por haber vendido Sanuk y liquidado Koolaburra, y pesan un 2,7%. "
        "<b>El segundo no es pequeño en absoluto:</b> Estados Unidos —el 58,3% de las ventas, "
        "3.191,5 M de 5.472,3 M— creció un +0,2%. Todo el crecimiento del ejercicio vino de fuera: "
        "internacional +26,8%.", "cuerpo"))

    out.append(M.dato_grande(
        "+0,2%",
        "CRECIMIENTO EN ESTADOS UNIDOS, FY2026",
        "Exactamente +0,151%. Es el mercado donde las dos marcas están más maduras y mejor "
        "conocidas, y pesa el 58,3% de las ventas. [HECHO — 10-K FY2026.]"))

    out.append(M.callout("PAUSA REFLEXIVA",
        "Si vives donde HOKA y UGG están por todas partes, tu impresión de esta empresa la está "
        "formando <b>el mercado que lleva un año sin crecer</b>: lo que ves en la calle procede "
        "íntegramente del 58,3% parado, y el +26,8% ocurre en países que no pisas. Sesgo de "
        "disponibilidad en estado puro. <b>La pregunta útil no es «se ven muchas HOKA», sino «¿por "
        "qué el mercado que mejor las conoce dejó de comprar más?».</b> Puede ser un mercado maduro "
        "que se sostiene, o saturación; no se contesta mirando por la ventana."))

    out.append(PageBreak())
    return out


# ═══════════════════════════════════════════════════════════════════════
#  §5 · POR QUÉ RINDE EL 101% SOBRE EL CAPITAL
# ═══════════════════════════════════════════════════════════════════════
def seccion_5():
    out = M.flag_titulo(
        "§5 · Por qué rinde el 101% sobre el capital",
        "Qué es el capital invertido, qué es el ROIC, y por qué un número de tres cifras obliga a "
        "enseñar cómo se calculó")

    out.append(M.p(
        "<b>Deckers gana en un año, después de impuestos, algo más de lo que tiene invertido en el "
        "negocio entero:</b> 975,1 millones de beneficio contra 965,6 millones de capital empleado. "
        "Un retorno del <b>101,0%</b>. Es el hallazgo de calidad de este expediente y conviene "
        "decirlo antes de explicarlo, porque cuando lo expliques con calma seguirá pareciendo "
        "increíble.", "cuerpo"))

    out.append(M.p(
        "Un número así no se puede soltar sin enseñar cómo se ha calculado: los retornos de tres "
        "cifras casi siempre son un error de convención, y la única defensa es declarar la fórmula "
        "entera antes de presumir del resultado.", "cuerpo"))

    # ── CAPITAL INVERTIDO ───────────────────────────────────────────────
    out.append(M.p("Primero: qué es el capital invertido", "h2"))

    out.append(M.p(
        "Imagina que montas tú mismo una tienda de zapatos. Antes de vender un par tienes que dejar "
        "dinero metido en cosas: el género de las estanterías, la reforma del local, la fianza. Y "
        "ese dinero no vuelve mientras la tienda siga abierta; si lo sacas, la tienda cierra. A ese "
        "dinero atrapado —el que hay que dejar dentro para que el negocio funcione— se le llama "
        "<b>capital invertido</b>.", "cuerpo"))

    out.append(M.p(
        "No es todo el dinero que has puesto, y ahí están los dos ajustes que lo cambian todo. "
        "Primero: <b>la caja sobrante no cuenta.</b> Los 1.907,2 millones que Deckers tenía en el "
        "banco al cierre del ejercicio no hacen funcionar el negocio; meterlos en el denominador "
        "sería castigar a la empresa por ser prudente. Segundo: <b>lo que te financian tus "
        "proveedores tampoco cuenta.</b> Si te sirven el género a noventa días, lo estás vendiendo "
        "con dinero de ellos.", "cuerpo"))

    out.append(M.caja_formula(
        "LA CONVENCIÓN COMPLETA · CAPITAL INVERTIDO",
        "(activo corriente &minus; caja) &minus; (pasivo corriente &minus; arrendamiento corriente) "
        "+ instalaciones netas + fondo de comercio + intangibles + activos por derecho de uso",
        "Los dos primeros paréntesis son el fondo de maniobra: lo atrapado en inventario y en lo "
        "que te deben, menos lo que te financian. Después se suma lo físico —tiendas, almacenes, "
        "sistemas—, lo que se pagó en su día por marcas compradas y el valor capitalizado de los "
        "locales alquilados, que son tienda igual aunque el contrato diga alquiler. Es la "
        "convención del método, idéntica para todas las empresas: cambiarla por empresa es la forma "
        "más fácil de hacer trampa."))

    # ── NOPAT Y ROIC ────────────────────────────────────────────────────
    out.append(KeepTogether([
        M.p("Segundo: qué es el NOPAT, y qué es el ROIC", "h2"),
        M.p(
            "El numerador tiene que ser coherente con ese denominador. <b>NOPAT</b> —siglas inglesas de "
            "«beneficio operativo después de impuestos»— es el EBIT de §3 menos los impuestos que le "
            "corresponden. Se usa el operativo y no el neto por una razón concreta: el neto incluye los "
            "intereses que cobra la caja, y la caja se acaba de excluir del denominador; meterla arriba "
            "y sacarla abajo infla el resultado gratis. Y el <b>ROIC</b> —retorno sobre el capital "
            "invertido— es la división de uno por otro: <b>975,1 entre 965,6 igual a 101,0%</b>. Por "
            "cada 100 dólares atrapados dentro del negocio, éste devuelve 101 limpios al año.",
            "cuerpo"),
    ]))

    out.append(M.figura(
        "charts/c03_roic_capital.png", w_cm=16.6,
        pie="Las dos barras son el numerador y el denominador de la misma división. Desde FY2025 la "
            "azul supera a la gris: eso es exactamente lo que significa un ROIC por encima del "
            "100%."))

    out.append(M.tabla([
        ["Ejercicio", "NOPAT", "Capital invertido", "<b>ROIC</b>", "Margen operativo"],
        ["FY2022", "452,0", "915,2", "49,4%", "17,93%"],
        ["FY2023", "506,5", "1.046,6", "48,4%", "18,00%"],
        ["FY2024", "719,6", "885,1", "<b>81,3%</b>", "21,63%"],
        ["FY2025", "916,2", "888,2", "<b>103,2%</b>", "23,65%"],
        ["<b>FY2026</b>", "<b>975,1</b>", "<b>965,6</b>", "<b>101,0%</b>", "<b>23,08%</b>"],
    ], col_w=[2.9 * cm, 3.2 * cm, 4.3 * cm, 3.1 * cm, 3.5 * cm], font_sz=8.4))
    out.append(M.p(
        "<i>[HECHO en los estados financieros de los 10-K FY2022 a FY2026; INFERENCIA en la "
        "convención de capital invertido y en el cálculo del NOPAT, que son propios y quedan "
        "declarados arriba. Millones de dólares.]</i>", "nota"))

    # ── LAS DOS ADVERTENCIAS ────────────────────────────────────────────
    out.append(M.p("Dos advertencias honestas, porque un número así invita a creérselo", "h2"))

    out.append(M.p(
        "<b>Primera: el salto de FY2024 no fue una mejora operativa.</b> El ROIC pasó del 48,4% al "
        "81,3% en un ejercicio y la tentación es leerlo como un salto de calidad. Mira la columna "
        "del medio: el capital invertido <b>bajó</b>, de 1.046,6 a 885,1. Fue un vaciado de "
        "inventario —el fondo de maniobra cayó de 481,9 a 275,0 millones y el inventario de 532,9 a "
        "474,3, con las ventas subiendo de 3.627,3 a 4.287,8—. Parte del ROIC de hoy no es que el "
        "numerador se disparara: es que el denominador se encogió, y un cociente que mejora por "
        "abajo no es repetible. <i>[HECHO en el balance; INFERENCIA en la atribución.]</i>",
        "cuerpo"))

    out.append(M.p("La segunda advertencia: el capital ha dejado de ser la restricción", "h3"))

    out.append(M.p(
        "<b>Segunda, y es la que de verdad importa: un ROIC del 101% significa que el capital ha "
        "dejado de ser la restricción de este negocio.</b> Si cada 100 dólares metidos dentro "
        "devuelven 101 al año, cualquier proyecto se financia solo antes de acabar el ejercicio; y "
        "Deckers cerró con 1.907,2 millones parados en el banco —1.602,6 al 30 de junio, tras las "
        "recompras— y sin un dólar de deuda financiera. <b>Deckers no puede crecer más rápido "
        "metiendo más dinero: sólo puede crecer si más gente quiere sus zapatos.</b> Eso tiene dos "
        "caras: ninguna cantidad de capital permite a un competidor comprar su sitio, pero tampoco "
        "permite a Deckers defenderlo. Todo depende del permiso de §2, y el permiso no se compra.",
        "cuerpo"))

    out.append(M.callout("LECCIÓN TRANSFERIBLE",
        "<b>Un ROIC sin convención declarada no es un dato: es una opinión con decimales.</b> El "
        "mismo negocio y las mismas cuentas dan un 56,5% en un agregador y un 101,0% con la "
        "convención de arriba, según qué metas en el denominador. Ninguna de las dos es mentira y "
        "ninguna es comparable con la otra. De ahí la regla práctica: cuando leas un ROIC, <b>lo "
        "primero que hay que buscar no es el número, es la fórmula</b>; si no está, el número no "
        "vale nada. Y cuando la convención cambia de una empresa a otra dentro del mismo documento, "
        "ya no estás leyendo un análisis: estás leyendo un argumento."))

    out.append(M.p(
        "Eso obliga a una corrección. El estudio sectorial que originó esta pregunta atribuye a "
        "Deckers un ROIC del <b>56,5%</b> y lo etiqueta como «cifra oficial reportada del 10-K "
        "FY2026». <b>Deckers no reporta ROIC</b>, ni ninguna empresa lo hace: no es una magnitud "
        "contable y siempre la calcula quien la publica. Con la convención declarada arriba sale "
        "<b>101,0%</b>. La corrección va a favor de Deckers, y la doy con la misma naturalidad con "
        "la que daré las que van en contra. <i>[HECHO — el 10-K FY2026 no contiene la palabra "
        "ROIC.]</i>", "cuerpo"))

    # ── EL ANUNCIO ──────────────────────────────────────────────────────
    out.append(M.p("Un aviso para el nivel 4, que aquí sólo se anuncia", "h2"))

    out.append(M.p(
        "Queda una consecuencia de este 101% que hay que registrar ahora aunque se resuelva en §14. "
        "Hay una regla —del método propio de este marco— que dice que una empresa crece a la "
        "velocidad a la que reinvierte multiplicada por lo que rinde esa reinversión: si vuelves a "
        "meter la mitad de lo que ganas y cada euro rinde un 20%, creces un 10%. El problema "
        "aparece al aplicarla aquí. Entre FY2022 y FY2026 el NOPAT de Deckers subió <b>523,1 "
        "millones</b> mientras el capital invertido subía <b>50,4</b>: sobre el beneficio acumulado "
        "de esos cuatro ejercicios, la <b>tasa de reinversión fue del 1,62%</b>. <i>[INFERENCIA — "
        "cálculo propio.]</i>", "cuerpo"))

    out.append(M.p("Qué pasa al aplicarla aquí", "h3"))

    out.append(M.p(
        "Aplícala y verás el problema: reinvertir un 1,62% entrega un crecimiento del <b>1,63%</b> "
        "anual, para una empresa cuyas ventas acaban de crecer un 9,8% y a la que su propia "
        "dirección guía al +7-8% durante cuatro años. <b>La regla no mide el crecimiento de "
        "Deckers: mide que Deckers no necesita capital para crecer.</b> Es la señal de calidad "
        "convertida en castigo por un automatismo. Que un negocio excelente haga saltar tu propia "
        "maquinaria no es una anécdota técnica: es la clase de cosa que decide veredictos, y se "
        "litiga en §14.", "cuerpo"))

    out.append(M.p(
        "Con esto termina el nivel 2: sabes qué vende Deckers y a quién, sabes leer sus tres "
        "márgenes, sabes de dónde sale cada dólar y cuánto capital hace falta para producirlo. Es "
        "todo el vocabulario que el resto del documento da por sabido. Lo que viene ahora es la "
        "película.", "cuerpo"))

    out.append(PageBreak())
    return out
