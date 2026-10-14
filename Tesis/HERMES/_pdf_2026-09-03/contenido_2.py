# -*- coding: utf-8 -*-
"""El moat · Los seis guardianes (knock-outs) · El motor de crecimiento"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, S, C, cm
from reportlab.platypus import Spacer, PageBreak


def s4_moat():
    o = flag_titulo("§3 · El moat", "Las cuatro capas del foso, y el único asedio real que sobrevivió")
    o += [p("Un foso defensivo de verdad no es una sola trinchera: es una fortaleza medieval bien "
            "construida, con anillos concéntricos, de modo que un atacante que supere el primero se "
            "encuentra con el segundo, y luego el tercero, y agotado, con el cuarto. Hermès tiene cuatro "
            "anillos, y se refuerzan entre sí.")]
    o += [p("El primero es el <b>poder de fijar precio</b>: subidas de entre 6% y 9% anuales en los "
            "bolsos icónicos, sostenidas durante una década sin que el volumen vendido se resienta — "
            "algo que casi ningún fabricante de bienes de consumo en el mundo puede decir de sí mismo "
            "sin exagerar. El segundo es la <b>escasez deliberada</b>: cada artesano produce en torno a "
            "15 unidades al mes por línea, muy por debajo de la demanda dispuesta a pagar, con listas de "
            "espera de meses o años — no un cuello de botella accidental de una fábrica que no da "
            "abasto, sino una decisión estratégica declarada, el equivalente corporativo de la poda del "
            "viticultor. El tercer anillo es la <b>integración vertical completa</b>: curtiembres "
            "propias, manufactura enteramente francesa, distribución enteramente propia, sin un solo "
            "mayorista entre el taller y el mostrador. El cuarto es la <b>barrera del saber-hacer</b>: "
            "formar a un artesano capaz de coser un Birkin toma años de práctica supervisada, y nadie "
            "—ni casas rivales con presupuestos comparables— ha logrado replicar ese modelo a escala "
            "industrial en casi dos siglos.")]
    o += [Spacer(1, 4), chart("charts/g6_moat.png", 16.4), Spacer(1, 8)]
    o += [callout("CASO HISTÓRICO",
        "Una fortaleza sólo demuestra su solidez cuando alguien la ataca de verdad, y Hermès ya vivió "
        "ese asedio. <b>Entre 2010 y 2014, LVMH</b> —el mayor conglomerado de lujo del mundo— acumuló "
        "silenciosamente el 23% del capital de Hermès a través de instrumentos financieros derivados "
        "(contratos cuyo valor depende del precio de la acción, sin necesidad de comprarla directamente) "
        "que, bajo la legislación francesa de la época, no obligaban a divulgar la posición hasta cruzar "
        "cierto umbral. Fue, en efecto, un asedio nocturno: para cuando la familia notó el tamaño del "
        "ejército a sus puertas, ya estaba dentro de las murallas. La respuesta fue tan rápida como el "
        "ataque había sido sigiloso: más de cincuenta herederos dispersos por generaciones consolidaron, "
        "en semanas, un holding —H51 SAS— con una cláusula que bloqueó el 50,2% del capital fuera del "
        "alcance de cualquier comprador externo. LVMH se retiró en diciembre de 2014, distribuyó su "
        "participación entre sus propios accionistas y se comprometió a no volver a comprar acciones de "
        "Hermès durante cinco años. <b>Ese compromiso expiró en diciembre de 2019</b> — llevan ya siete "
        "años sin esa restricción, un dato que el juicio adversarial de este documento no deja pasar "
        "por alto (§9).")]
    o += [p("Hay una prueba clásica para saber si el ahorro de escala de una empresa dominante beneficia "
            "al cliente, a la propia empresa, o se lo queda un competidor más agresivo. En Hermès, el "
            "ahorro no llega al cliente en ningún año: el precio sube siempre. Llega, en parte, a la "
            "propia empresa —el margen operativo se mantuvo estable entre 39% y 42% durante cinco años, "
            "mientras las ventas se multiplicaban por 1,8—, y en parte financia la expansión de "
            "capacidad: las inversiones de capital (<i>capex</i>) de crecimiento pasaron de 4,5% de las "
            "ventas en 2022 a 7,3% en 2025. Ningún competidor se queda con ese margen: en 2025, mientras "
            "LVMH reportaba ingresos −4,6% y Kering −14,6%, Hermès crecía +9% a tipo de cambio "
            "constante — la única de las tres grandes casas que, ese año, creció ingresos y sostuvo "
            "margen a la vez.")]
    o += [Spacer(1, 4), chart("charts/g2_metiers.png", 16.4), Spacer(1, 8)]
    o += [p("El comportamiento durante el peor trimestre del sector en una generación —el confinamiento "
            "de 2020— confirma el patrón fuera de una crisis financiera y dentro de una crisis operativa "
            "real. Mientras Ralph Lauren recortaba su capex un 60,1% y Kering un 17,7% —con sus dos "
            "primeros ejecutivos renunciando a su retribución variable—, Hermès <b>aumentó</b> su "
            "plantilla un 7,7%, sin ayudas públicas, sostuvo su inversión, y aprovechó el momento para "
            "integrar a J3L, un proveedor histórico de cuero. Comprar al proveedor en el trimestre más "
            "duro del sector no es un gesto defensivo: es ampliar capacidad cuando todos los demás la "
            "reducen. La plantilla de producción —un dato físico, no contable, y por eso más difícil de "
            "maquillar— creció de 9.469 a 12.055 personas entre 2022 y 2025, un 27%, justo cuando el "
            "relato de “la escasez que se agota” predeciría lo contrario.")]
    o += [PageBreak()]
    return o


# ═══════════════════════════════════════════════════════════════════════════
def s5_guardianes():
    o = flag_titulo("§4 · Los seis guardianes", "Los knock-outs del método, y por qué ninguno se activa")
    o += [p("Antes de preguntarse si un negocio es bueno, el método exige preguntarle si tiene algo "
            "estructuralmente roto que descalifique cualquier análisis posterior — seis guardianes en la "
            "puerta, cada uno con autoridad de veto absoluto, indiferentes a lo bonito que sea el resto "
            "de la historia. O el guardián dispara con evidencia dura de un documento con fecha y "
            "página, o no dispara: no existe un término medio de “cuarentena”.")]
    o += [tabla([
        ["EL GUARDIÁN VIGILA", "VEREDICTO EN HERMÈS"],
        ["Estructuras societarias opacas de acceso indirecto",
         "SCA (<i>société en commandite par actions</i>, una forma jurídica francesa que separa la "
         "gestión —familiar— de los accionistas que cotizan) en Euronext Paris, llanamente. No dispara."],
        ["Que la compensación en acciones devore el flujo de caja",
         "132 M€ (2025) sobre un flujo de caja libre ajustado de 3.880 M€ — 3,4%. No dispara."],
        ["Que el retorno sobre el capital no supere su coste de forma sostenida",
         "Entre 42% y 60% en los 7 ejercicios auditados 2019-2025 (mínimo 42,3%, en 2020) frente a un "
         "coste de capital de mercado de ~8,9% (§9). No sólo no dispara: el margen es abismal."],
        ["Reexpresiones contables de ingresos que delaten maquillaje",
         "Sin evidencia de ninguna en los informes anuales revisados 2020-2025. No dispara."],
        ["Dependencia peligrosa de un solo cliente o regulador",
         "Ingresos repartidos entre 6 oficios y 6 regiones geográficas, sin concentración de riesgo. "
         "No dispara."],
        ["Deuda que pueda estallar",
         "Deuda financiera bruta de 34 M€ (0,02% del capital empleado) frente a una caja neta de "
         "12.239 M€. No dispara."],
        ], [6.2*cm, 9.4*cm], font_sz=8.4)]
    o += [p("Los seis guardianes examinan la puerta y la dejan pasar sin condiciones.")]
    o += [PageBreak()]
    return o


# ═══════════════════════════════════════════════════════════════════════════
def s6_motor():
    o = flag_titulo("§5 · El motor de crecimiento",
                    "Reinversión, retorno, y la tensión entre lo que el negocio PUEDE dar y lo que hay que exigirle")
    o += [p("Todo negocio crece por la misma ecuación simple: cuánto de sus ganancias reinvierte, "
            "multiplicado por cuánto rinde cada euro reinvertido — a ese segundo factor, cuando se mide "
            "sobre el capital nuevo destinado a crecer, se le llama ROIIC (retorno sobre el capital "
            "incremental invertido). Hermès reinvierte relativamente poco de sus ventas —entre 13,0% y "
            "13,5%, según el ejercicio—, muy por debajo del 25% que definiría a un “compounder” "
            "que se traga toda su propia caja para crecer: no es ese tipo de negocio. Sobre su beneficio "
            "operativo neto de impuestos, la reinversión sube a cerca del 47%, y el ROIIC —descontado el "
            "efecto, indemostrable con documentos, de que los márgenes simplemente sigan expandiéndose— "
            "se mueve entre 23,4% y 30,2% según la ventana temporal elegida. Multiplicando reinversión "
            "por retorno se obtiene el crecimiento “mecánico” que la aritmética permite: entre "
            "11,4% y 16,1% anual — un rango amplio que se disputa más abajo.")]
    o += [callout("LA METÁFORA",
        "Un corredor de fondo puede, en su mejor día, con viento a favor y las piernas frescas, correr "
        "un maratón a un ritmo espectacular. Eso es lo que la aritmética de Hermès permite en su mejor "
        "combinación de supuestos: el 16,1%. Pero exigirle a ese mismo atleta que sostenga ese ritmo, "
        "carrera tras carrera, durante diez años seguidos, es una pregunta completamente distinta. "
        "<b>Lo que un atleta puede correr una vez y lo que se le puede exigir sostener una década no "
        "son el mismo número</b> — y confundirlos es el error más común al proyectar crecimiento.")]
    o += [p("Por eso este documento declara, de forma explícita y discrecional —un juicio del analista, "
            "no un hecho verificado—, una “g defendible” bastante más modesta: entre 6,0% y "
            "9,0% anual, una banda que se amplió tras el ataque adversarial (antes era 6,0%-7,5%). "
            "¿Qué limita ese ritmo sostenible? La capacidad física de manufactura artesanal, que no se "
            "improvisa. El calendario de nuevos talleres de marroquinería ya está comprometido y es "
            "público hasta 2030 —Loupes en 2026, Charleville-Mézières en 2027, Colombelles en 2028, Les "
            "Andelys en 2030—, a un ritmo de aproximadamente un taller nuevo por año sobre una base de 24 "
            "o 25 existentes (cada uno con ~300 puestos nuevos, sobre una plantilla de producción de "
            "12.055 personas), lo que añade entre 4% y 5% de capacidad anual en marroquinería, el oficio "
            "que representa el 44% de los ingresos del grupo. Y la expansión ya no se limita a la "
            "marroquinería: Hermès también está desarrollando el centro de Couzeix (vajilla, 2027), "
            "ampliando su manufactura relojera de Le Noirmont en Suiza (2028), y levantando una nueva "
            "Manufacture de Métaux para piezas metálicas — el techo físico de crecimiento del grupo es, "
            "hoy, algo más amplio que “solo marroquinería”.")]
    o += [callout("PAUSA REFLEXIVA",
        "Hermès acumula 12.900 millones de euros de caja neta a 30 de junio de 2026 (comunicado H1 2026, "
        "restated) — que ha seguido <b>creciendo</b> pese al ritmo de inversión más alto de su historia. "
        "Si la capacidad de los talleres fuera de verdad el único techo duro que limita el crecimiento, "
        "una dirección con retornos de 52% a 60% sobre el capital debería estar desplegando esa caja con "
        "más urgencia todavía. Esa caja ociosa es evidencia real —no especulación— de que la escasez "
        "podría ser, al menos en parte, una elección de marca reversible, y no un límite físico "
        "irreversible. Por eso la banda se amplió hacia arriba en vez de sostener un punto medio "
        "falsamente preciso: la honestidad exige reconocer la incertidumbre, no disfrazarla de "
        "precisión.")]
    o += [p("La valoración de este documento (§9) traduce esta banda en tres escenarios explícitos, "
            "año a año, anclados además en la propia guía de inversión de Hermès para 2026 — no en un "
            "solo número medio, sino en una senda completa que se puede comprobar trimestre a trimestre.")]
    o += [PageBreak()]
    return o
