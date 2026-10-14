# -*- coding: utf-8 -*-
"""Gestión y la grieta en la armadura · Lo que el mercado ya sabe · El pre-mortem"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, S, C, cm
from reportlab.platypus import Spacer, PageBreak


def s7_gestion():
    o = flag_titulo("§6 · Gestión y la grieta en la armadura",
                    "Axel Dumas, el pacto H51, y un heredero que nunca lo firmó")
    o += [p("Axel Dumas, de la sexta generación familiar, dirige Hermès como consejero delegado desde "
            "2014 —justo el año en que se resolvió el asedio de LVMH—, sucediendo al primer ejecutivo no "
            "familiar en la historia de la casa. Su compensación variable está indexada al crecimiento "
            "de la utilidad neta, no al precio de la acción en el corto plazo: un incentivo que empuja a "
            "pensar en décadas, no en trimestres — exactamente el horizonte que un negocio de escasez "
            "artesanal necesita de su capitán.")]
    o += [callout("LA METÁFORA",
        "Toda armadura, por buena que sea, tiene una junta donde las placas se encuentran, y ahí es "
        "donde hay que mirar con más cuidado. La alianza familiar que blindó a Hermès del asedio de "
        "2010-2014 —el pacto H51— no es perpetua: <b>vence en 2031</b> y necesita la unanimidad de más "
        "de cincuenta herederos para renovarse. Funciona como un tratado de defensa mutua con fecha de "
        "caducidad escrita en el propio tratado, y toda alianza así lleva dentro la misma pregunta: qué "
        "pasa si, cuando llega el vencimiento, no todos los firmantes originales quieren renovar.")]
    o += [p("Nicolas Puech, descendiente de la familia, nunca se sumó a ese holding. Protagonizó una "
            "disputa legal entre 2013 y 2014 sobre el tamaño de su participación. Aquí conviene "
            "detenerse en la naturaleza exacta del dato que sigue:")]
    o += [callout("LA TRAMPA",
        "[<b>INFERENCIA de prensa francesa</b> —Challenges, La Lettre— <b>no verificada contra ningún "
        "documento regulatorio</b>]: reportes publicados entre 2021 y 2023 describen una disputa de "
        "sucesión activa alrededor de Puech, hoy de unos 83 años — un hijo adoptivo, un asesor "
        "financiero suizo, y acercamientos reportados a LVMH para explorar la venta de su participación. "
        "Nada de esto figuraba como riesgo vivo en el expediente original de julio de 2026; fue el "
        "juicio adversarial de este documento (§8) quien lo señaló como un evento con ventana de riesgo "
        "concreta —dada la edad de Puech— dentro del propio horizonte a diez años del modelo de "
        "valoración, aterrizando justo antes de la fecha en que el pacto necesita renovarse por "
        "unanimidad. Se etiqueta, con toda intención, como inferencia de prensa y no como hecho de un "
        "filing regulatorio: es la clase de dato que se vigila, no que se da por sentado.")]
    o += [PageBreak()]
    return o


# ═══════════════════════════════════════════════════════════════════════════
def s8_variante():
    o = flag_titulo("§7 · Lo que el mercado ya sabe", "Percepción variante — o la falta de ella")
    o += [p("Antes de comprar cualquier acción cara vale la pena preguntarse: ¿sé algo que el resto del "
            "mercado no sabe? En Hermès, la respuesta honesta es no. Doce de trece analistas que cubren "
            "la acción recomiendan comprar, con un precio objetivo medio de aproximadamente 1.870 euros "
            "—por encima del precio de hoy— según datos de Investing.com del 3 de septiembre de 2026. "
            "No hay ninguna variante secreta que descubrir: el consenso ya sabe, con la misma claridad "
            "que este documento, que Hermès es un negocio extraordinario.")]
    o += [callout("EN ROMÁN PALADINO",
        "La variante aquí no es de información privilegiada; es de <b>disciplina</b>. El consenso paga "
        "hoy por diez años de éxito futuro con el mismo entusiasmo con que paga por el historial ya "
        "entregado, sin exigirse separar cuánto de ese historial es poder de fijar precio —indemostrable "
        "con los documentos que la propia empresa publica— y cuánto es capacidad física real de "
        "producir más. Aplicando con el mismo rigor que a cualquier otra tesis de esta cartera la regla "
        "de construir siempre el coste de capital desde el mercado y nunca heredarlo de un múltiplo de "
        "“empresas de calidad parecida”, la tasa de retorno esperada al ritmo de crecimiento "
        "defendible —entre 5,8% y 7,7% anual, centro ~6,4%— queda por debajo del propio coste de "
        "capital, entre 8,1% y 8,9%. Casi ningún analista del lado vendedor reporta esta brecha, porque "
        "casi ninguno construye su coste de capital desde cero.")]
    o += [p("Si no hay variante articulable más allá de esta disciplina, se registra así, sin "
            "disfrazarla de hallazgo. Es un consenso con más rigor de precio, no un consenso distinto.")]
    o += [PageBreak()]
    return o


# ═══════════════════════════════════════════════════════════════════════════
def s9_premortem():
    o = flag_titulo("§8 · El ejercicio del funeral imaginado", "El pre-mortem: cuatro formas de que esto salga mal")
    o += [p("Existe un ejercicio mental exigente pero disciplinado que consiste en imaginar, hoy, que "
            "dentro de unos años esta tesis resultó equivocada, y preguntarse por qué. No es pesimismo: "
            "es un funeral practicado con antelación, para reconocer los síntomas antes de que se "
            "vuelvan terminales. Cuatro mecanismos concretos, cada uno con su métrica y su ventana de "
            "tiempo — se escriben y se congelan antes de calcular la valoración (§9), no después, para "
            "que puedan refutarla en vez de acomodarse a una conclusión que ya existía.")]
    o += [Spacer(1, 4), chart("charts/g7_premortem.png", 16.4), Spacer(1, 8)]
    o += [tabla([
        ["MECANISMO", "MÉTRICA DE ALARMA"],
        ["<b>1 · Fractura del pacto H51</b> antes de 2031, con Nicolas Puech en el centro",
         "Cualquier señal pública de venta de su participación fuera del círculo familiar, o de no "
         "renovación del pacto, antes de esa fecha."],
        ["<b>2 · Relajación de la escasez</b> bajo una séptima generación menos disciplinada",
         "Lead times de bolsos icónicos acortándose de forma sostenida, o marroquinería creciendo bajo "
         "+5% a tipo de cambio constante durante dos trimestres pese a capacidad creciente."],
        ["<b>3 · Desaceleración de China/Asia</b> más severa de lo esperado",
         "Crecimiento consolidado a tipo de cambio constante cae bajo +4% sostenido durante dos "
         "trimestres."],
        ["<b>4 · Riesgo reputacional en pieles exóticas</b>, activo desde 2015 (PETA)",
         "Escalada a boicot con impacto medible en las ventas de esa categoría."],
        ], [7.0*cm, 8.6*cm], font_sz=8.3)]
    o += [callout("PAUSA REFLEXIVA",
        "El “gemelo fallido” del mecanismo 2 —la empresa que en su día se parecía a esto y "
        "luego se rompió— es Gucci o Burberry: un heredero o una dirección relajan la escasez para "
        "perseguir crecimiento de corto plazo, y el aura de exclusividad se erosiona sin que nadie note "
        "el momento exacto en que se rompió. Es el riesgo que menos se vigila hoy — y el que el juicio "
        "adversarial de este documento (§9) más insistió en nombrar con fecha.")]
    o += [p("El más inmediato de los cuatro, y el que el ejercicio adversarial señaló como el falsable "
            "más duro y con fecha más cercana, llega con las ventas del tercer trimestre de 2026 (los "
            "primeros nueve meses del año), esperadas hacia mediados de octubre. Si el crecimiento "
            "orgánico consolidado a tipo de cambio constante cae por debajo de +4% —frente al +6,7% del "
            "segundo trimestre— y/o si Marroquinería y Talabartería crece por debajo de +3% a tipo "
            "constante, ese dato mataría simultáneamente dos cosas: la conclusión de que no hay trampa "
            "de valor (§9), y la base empírica sobre la que descansa toda la “g defendible” de "
            "este documento (§5). Revelaría que el crecimiento reciente dependía más de subir precios "
            "que de la capacidad real que el modelo asume como techo.")]
    o += [PageBreak()]
    return o
