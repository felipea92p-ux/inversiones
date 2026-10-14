# -*- coding: utf-8 -*-
"""13 · El abogado del diablo — dos rondas · 14 · El veredicto y lo que hace falta para cambiarlo"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, cm, S
from reportlab.platypus import PageBreak, Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT

# Párrafos con constantes tipo ENUM_LARGAS_SIN_ESPACIOS: alineación izquierda,
# no justificada, para no producir huecos gigantes al justificar una "palabra" larguísima.
_izq = ParagraphStyle("cuerpo_izq", parent=S["cuerpo"], alignment=TA_LEFT)
def pi(txt):
    return Paragraph(txt, _izq)

def s13_abogado():
    o = flag_titulo("13 · El abogado del diablo",
                    "Dos rondas completas, en sesión limpia, sin heredar el entusiasmo de la investigación. Su único mandato: refutar")
    o += [p("Esta tesis ha pasado por el veto del abogado del diablo <b>dos veces</b> en cuatro días — algo que "
        "no le ha pasado a ninguna otra revisión de CME hasta ahora. La primera ronda (4-sep) atacó el "
        "mecanismo, el motor de crecimiento y la asimetría. La segunda ronda (8-sep) llegó por una vía "
        "distinta: no fue convocada para revisar CME específicamente, sino que emergió de un ejercicio de "
        "cross-validación sobre cinco tesis en paralelo, y de ahí encontró un defecto que ninguna de las dos "
        "rondas anteriores había tocado.")]
    o += [hr(), p("<b>RONDA 1 — 4 de septiembre de 2026</b>", "h2")]
    o += [pi("<b>Veredicto adversarial recibido: OBJECIONES_QUE_EXIGEN_DEGRADAR_VEREDICTO</b> — no "
        "VETO_NO_HAY_CASO_HONESTO. El abogado no pide matar la tesis; pide que el veredicto no se quede en un "
        "«NO COMPRAR TODAVÍA» pasivo sin resolver por escrito lo que encontró. Candado A del método: cada "
        "objeción con mecanismo y fecha se clasifica como <b>ACEPTADA</b>, <b>REFUTADA CON EVIDENCIA NUEVA</b>, "
        "o <b>CONVERTIDA EN FALSADOR</b>. Ninguna objeción sustantiva queda sin marcar.")]
    o += [p("<b>Golpe 1 — El moat nunca se probó contra un rival con liquidez real.</b>")]
    o += [tabla([
        ["OBJECIÓN", "VEREDICTO", "QUÉ SE HIZO"],
        ["1a. El precedente LCH/SwapClear es específico del pool, no transferible: cada TAM nuevo enfrenta el "
              "mismo problema que CME no resolvió en 13 años.",
         "ACEPTADA",
         "Se añadió una nota explícita en las secciones 5 y 7 anclando esta lectura. No cambia el knock-out ni "
         "el veredicto de moat core — sí degrada la confianza en la parte del crecimiento futuro que depende de "
         "las líneas nuevas."],
        ["1b. El dato de share de FMX (ene-sep 2025) tiene más de un año de antigüedad frente a esta síntesis.",
         "ACEPTADA, no resuelta",
         "Presupuesto de búsqueda web agotado (0 de 200). Convertida en el falsable duro reforzado de la "
         "sección 15. Sigue sin resolverse en esta actualización del 8-sep."],
        ["1c. Los hechos no distinguen si la concentración de clearing firm es el mismo cliente acumulando o "
              "clientes distintos rotando.",
         "ACEPTADA como brecha real",
         "No cambia el knock-out (e). Degrada la confianza del mecanismo 4 del pre-mortem (sección 11), sin "
              "resolver — pendiente del 10-K FY2026."],
        ["1d. Kalshi como riel regulatorio paralelo, calificado de «sistémico» por el propio Duffy.",
         "CONVERTIDA EN FALSADOR — ya incorporado",
         "Ya vivía en el mecanismo 2 del pre-mortem con peso de riesgo activo. El abogado confirma que ya se "
              "trata correctamente."]],
        [5.4*cm, 3.4*cm, 7.8*cm], font_sz=7.4)]
    o += [p("<b>Síntesis Golpe 1:</b> el propio abogado concluye que esto «no alcanza para vetar el mecanismo "
        "core de futuros — ahí la evidencia de abril-2025 es real y no se niega solo por oficio». Esa lectura "
        "se acepta: el Candado 1 del moat (compensación de margen, escala actual) sobrevive el ataque. Lo que "
        "sí degrada es la confianza en que las líneas de crecimiento nuevas hereden ese moat.")]
    o += [callout("LA TRAMPA",
        "<b>Golpe 2 — Reinversión/g: el propio framework dice que esto debería encoger, y la tesis lo "
        "reescribió.</b> ACEPTADA EN SU TOTALIDAD, sin diluir. Ésta es la objeción más grave del ataque: la "
        "frase «el framework estándar NO aplica literalmente a este arquetipo» (sección 7 original) es la "
        "maniobra que el método existe para prohibir — neutralizar por declaración de excepción un resultado "
        "mecánico incómodo, en vez de dejar que ese resultado degrade la confianza en el g terminal usado en el "
        "DCF base.<br/><br/>"
        "No hay evidencia nueva que la refute: el dato que la resolvería —comportamiento del margen operativo "
        "en un trimestre de bajo volumen/volatilidad, análogo a 2017— no está en los hechos entregados, el "
        "propio abogado lo señaló como ausente, y esta síntesis no pudo obtenerlo. Es exactamente la honestidad "
        "que el método exige: la brecha se declara, no se rellena con una cifra inventada.<br/><br/>"
        "<b>Corrección aplicada:</b> (1) el g terminal de 3,5% pasa de «supuesto razonable» a «supuesto "
        "plausible pero no verificado mecánicamente». (2) El caso base (357 US$, +28%) se mantiene como cálculo "
        "válido, pero su peso en el veredicto se degrada. (3) Se registra como pre-condición abierta, con "
        "fecha: antes de usar el g terminal con confianza alta, hay que encontrar el dato de margen en bajo "
        "volumen. (4) La frase original no se borra — queda anclada a esta corrección.")]
    o += [p("<b>Golpe 3 — Asimetría: bien etiquetada como desfavorable, pero no corre el escenario más "
        "probable.</b> ACEPTADA. El bajista de la sección 12 sube WACC y recorta owner earnings como dos "
        "palancas aisladas; el escenario de tasas cayendo se corre aparte. El escenario correlacionado que los "
        "propios hechos sugieren como más probable —tasas y volumen cayendo simultáneamente— no está calculado, "
        "y no se puede reconstruir de forma confiable en esta etapa sin introducir precisión falsa. "
        "<b>Corrección aplicada:</b> se declara pre-condición dura antes de cualquier COMPRAR futuro: calcular "
        "el escenario correlacionado y confirmar si su valor por acción se mantiene por encima o cae por debajo "
        "de 200 US$. Sigue sin resolverse hoy — la corrección del 8-sep fue sobre beta/WACC, un input distinto.")]
    o += [callout("LECCIÓN TRANSFERIBLE",
        "<b>Falsable duro propuesto por el abogado de la Ronda 1, CONVERTIDO EN FALSADOR:</b> share de "
        "FMX/Fenics en SOFR futures (ADV) vs. CME &gt; 3% del ADV combinado, sostenido durante un mes calendario "
        "completo, en cualquier momento antes del 16-nov-2026. Se adopta como predicción falsable en la sección "
        "15 — alarma temprana, de ventana más corta y umbral menos exigente que la ya existente en el "
        "pre-mortem (&gt;5% sostenido 2 trimestres).")]
    o += [p("<b>Veredicto de la Ronda 1.</b> La tesis <b>no sobrevive intacta</b> el ataque: el golpe al moat "
        "core (Golpe 1) no alcanza para vetarlo, pero los Golpes 2 y 3 sí impactan de lleno y <b>tienen "
        "mecanismo, fecha, y no se resuelven con los hechos entregados</b>. Se resuelven degradando "
        "explícitamente la confianza en el caso base de valoración y añadiendo pre-condiciones duras con fecha "
        "antes de cualquier reapertura hacia COMPRAR.")]
    # Sin PageBreak aquí a propósito (mismo criterio que entre secciones 12 y 13):
    # forzarlo dejaba la página del veredicto de la Ronda 1 con ~75% en blanco.
    o += [Spacer(1, 10), hr(), Spacer(1, 4)]
    o += [p("<b>RONDA 2 — 8 de septiembre de 2026 (cross-validación independiente, 5 tesis en paralelo)</b>", "h2")]
    o += [pi("Esta ronda es distinta en su origen: no llegó porque alguien pidiera revisar CME de nuevo, sino "
        "porque una sesión que corría el método de 12 pasos desde cero sobre otras cuatro empresas —sin haber "
        "leído los documentos de CME del 4-sep— tropezó con el mismo tipo de defecto en las cinco, incluida "
        "CME. Esa es la clase de hallazgo que ningún abogado del diablo interno, por disciplinado que sea, "
        "puede producir por sí solo: necesita un investigador que no sepa que está mirando el mismo problema "
        "otra vez.")]
    o += [tabla([
        ["OBJECIÓN", "VEREDICTO", "QUÉ SE HIZO"],
        ["2a. El beta bursátil de CME (0,27) se midió, con toda probabilidad, en una ventana de calma que no "
              "refleja el riesgo competitivo real — es el más bajo de sus 4 pares directos (CBOE 0,42, ICE 0,93, "
              "NDAQ 0,97) mientras la propia tesis llama a FMX «el riesgo competitivo más serio en dos "
              "décadas». Hallazgo convergente, 5 de 5 empresas del lote, de forma independiente.",
         "ACEPTADA — corrección aplicada",
         "Beta corregido a 0,65 (promedio de los 4 pares), validado cruzado contra el beta sectorial de "
              "Damodaran (0,66). WACC: 6,49%→7,61%. Valor intrínseco: 450,31→338,79 US$. Descuento: "
              "−37,9%→−17,41%. Gatillo de compra: 315,22→237,15 US$. Ver sección 12 para el detalle completo."],
        ["2b. El propio abogado de esta ronda, al estresar el caso corregido, usó un ERP (5,0-5,5%) más alto "
              "que el ERP implícito vigente de Damodaran (4,2-4,5%) — lo que habría exagerado artificialmente "
              "el WACC estresado y amenazado con romper el knock-out ROIC&gt;WACC en sentido contrario.",
         "REFUTADA CON EVIDENCIA NUEVA",
         "Con el ERP correcto de Damodaran, incluso usando el beta más agresivo de los 4 pares (NDAQ, 0,97), el "
              "WACC estresado da sólo ≈8,99% — sigue sin cruzar el ROIC de 9,6%. El knock-out de calidad se "
              "sostiene en ambas direcciones del ejercicio: ni el beta crudo optimista de la Ronda 0 ni el ERP "
              "pesimista mal calibrado de esta Ronda 2 cambian la conclusión de fondo."]],
        [5.6*cm, 3.6*cm, 7.4*cm], font_sz=7.4)]
    o += [callout("CASO HISTÓRICO",
        "<b>Por qué este hallazgo deja de ser una corazonada y pasa a ser un patrón.</b> El sesgo «beta baja = "
        "momentum circular» —una beta medida sobre un valor en máximos o en calma que retroalimenta un WACC "
        "artificialmente bajo, que a su vez «crea» un margen de seguridad que no existe— ya estaba fichado como "
        "sospecha en el marco de inversión de Felipe antes de esta ronda. Lo que la Ronda 2 aporta no es la "
        "idea, sino la confirmación empírica: cinco abogados del diablo, en cinco sesiones que no se "
        "comunicaron entre sí, deteniéndose en el mismo defecto en las cinco empresas que revisaron. Eso ya no "
        "se puede tratar como una anomalía de CME — es una advertencia permanente sobre cómo este marco debe "
        "tratar cualquier beta que llegue de un agregador de mercado sin pasar primero por el filtro de «¿este "
        "número refleja el riesgo que el resto de esta misma tesis ya describió?».")]
    o += [p("<b>Veredicto de la Ronda 2.</b> Confirma NO COMPRAR TODAVÍA, sin cambio de categoría. La "
        "corrección de beta mueve el descuento aparente muy por debajo del 30% que exige el Bloque 2 para "
        "gatillar compra — si acaso, hace el caso de espera <i>más</i> claro que antes, no menos, porque retira "
        "la ambigüedad de tener dos números de descuento (−37,9% con el beta crudo, algo intermedio con la "
        "banda 7-9%) y deja uno solo, validado de forma cruzada. Los dos huecos de evidencia de la Ronda 1 "
        "(escenario bajista correlacionado, comportamiento del margen en bajo volumen) siguen abiertos y sin "
        "cambios — esta ronda corrigió beta/WACC, no esos dos huecos.")]
    # Sin PageBreak aquí a propósito: el párrafo final de la sección 13 se corta
    # de forma natural dejando solo 3 líneas en la página siguiente; forzar un
    # salto justo después desperdiciaba el resto de esa página antes de la 14.
    return o

def s14_veredicto():
    o = flag_titulo("14 · El veredicto y lo que hace falta para cambiarlo",
                    "NO COMPRAR TODAVÍA — confirmado por tercera vez en cuatro días, con la valoración ahora sobre una base más sólida")
    o += [p("<b>NO COMPRAR TODAVÍA.</b>", "h_seccion")]
    o += [p("Sigue siendo provisional en un sentido acotado, ya señalado en el aviso de estado: los pasos de "
        "monólogo previo, círculo de competencia y percepción variante son borradores de agente pendientes de "
        "que Felipe los escriba o ratifique personalmente. Eso no cambia con este veredicto.")]
    o += [pi("<b>Por qué la categoría del veredicto no cambia</b> (sigue siendo «NO COMPRAR TODAVÍA» y no «NO» "
        "ni «NO DECIDIBLE»): ninguna de las dos rondas del abogado del diablo pidió matar la tesis "
        "(OBJECIONES_QUE_EXIGEN_DEGRADAR_VEREDICTO en ambas, nunca VETO_NO_HAY_CASO_HONESTO). Además, el hecho "
        "más simple y menos disputable de todo el documento —el precio (HECHO, 279,81 US$, 8-sep-2026)— por sí "
        "solo ya sostiene «no comprar ahora» con independencia de todo el debate de WACC/g: está muy por encima "
        "de ambas anclas (235/200) sin necesitar el DCF para llegar a esa conclusión. Tampoco hay evidencia de "
        "negocio roto (ningún knock-out se activó, moat core no vetado, test de trampa de valor negativo) que "
        "justifique escalar a «NO». Y sí hay evidencia suficiente para decidir una dirección (esperar) aunque "
        "partes del cálculo interno queden con confianza degradada — eso no es lo mismo que «NO DECIDIBLE», que "
        "se reserva para cuando ni siquiera pudiera argumentarse una dirección.")]
    o += [p("<b>Delta respecto al monólogo inicial de esta actualización (8-sep):</b> el punto de partida del "
        "día era «confirmar o romper, con evidencia nueva y fechada, el gate ya vigente». La evidencia nueva no "
        "rompió nada — pero tampoco fue neutral: cambió la razón por la que la tesis dice que hay que esperar. "
        "Antes del 8-sep, el caso de espera descansaba en un precio por encima del gate más una valoración con "
        "un rango ancho y poco resuelto (258-401 US$, dominado por la incertidumbre sobre qué beta usar). Hoy "
        "descansa en un precio por encima del gate más una valoración puntual, validada de forma cruzada e "
        "independiente, que converge con el propio ancla del gate. El veredicto es el mismo; la calidad de la "
        "evidencia que lo sostiene es mayor.")]
    o += [callout("LA TRAMPA",
        "<b>Qué SÍ cambia respecto a la versión del 4-sep — la actualización real, no cosmética:</b><br/><br/>"
        "<b>1.</b> El WACC deja de tratarse como una banda ancha (7-9%) sin punto central defendido y pasa a "
        "tener una cifra puntual validada de forma cruzada: <b>7,61%</b>, con beta 0,65. El «descuento» que "
        "importa para la decisión deja de ser el −37,9% del beta crudo (ya descartado el 4-sep, pero sin "
        "reemplazo puntual) y pasa a ser <b>−17,41%</b> — insuficiente frente al 30% del Bloque 2, y la razón "
        "cuantitativa exacta de por qué.<br/><br/>"
        "<b>2.</b> El gatillo de compra recalculado con esa disciplina (237,15 US$) converge con el ancla ya "
        "fijada en gates.md (235 US$) por un camino completamente independiente — dos construcciones distintas "
        "llegando casi al mismo número. Esto no mueve gates.md (fuera del alcance de este documento) pero sí "
        "refuerza la confianza en que esa ancla nunca fue arbitraria.<br/><br/>"
        "<b>3.</b> Lo que NO cambia: los dos huecos de evidencia de la Ronda 1 (escenario bajista correlacionado "
        "sin calcular; comportamiento del margen operativo en bajo volumen sin verificar) siguen abiertos, sin "
        "resolver, y siguen siendo pre-condición dura antes de cualquier futuro COMPRAR — independientemente de "
        "qué tan bien calibrado esté ahora el WACC.")]
    o += [p("<b>Dos pre-condiciones duras, con fecha, antes de que esta tesis pueda escalar a COMPRAR en el "
        "futuro</b> — heredadas sin cambios de la Ronda 1, e independientes de la corrección de beta:")]
    o += [tabla([
        ["#", "PRE-CONDICIÓN"],
        ["(a)", "Calcular el escenario bajista correlacionado (Rf −80pb + normalización de volumen/incertidumbre "
                "+ reversión parcial de margen operativo) y confirmar si su valor por acción queda por encima o "
                "por debajo de 200 US$."],
        ["(b)", "Encontrar o construir evidencia del comportamiento del margen operativo de CME en un trimestre "
                "de volumen/volatilidad por debajo del promedio histórico (análogo a 2017), para poder tratar "
                "el g terminal de 3,5% como verificado en vez de plausible-no-verificado."]],
        [1.0*cm, 15.6*cm], font_sz=8.4)]
    o += [p("<b>Sin (a) y (b) resueltos, un futuro veredicto de COMPRAR en esta tesis no cumpliría el Candado A "
        "del método</b> aunque el precio cayera a la zona del gate y aunque el WACC siga tan bien calibrado como "
        "hoy.")]
    o += [p("<b>Con esa salvedad, la evidencia de esta actualización sigue reafirmando el gate ya vigente</b> "
        "(«NO COMPRAR TODAVÍA — entrada 235/200, gate bloqueante al 16-nov-2026»), por tres razones, la primera "
        "suficiente por sí sola:")]
    o += [tabla([
        ["RAZÓN", "EVIDENCIA"],
        ["1 · Precio", "HECHO, no depende de ningún supuesto del DCF: CME cotiza 279,81 US$, muy por encima de ambos anclas de entrada."],
        ["2 · Valoración con WACC validado de forma cruzada",
         "El valor intrínseco corregido (338,79 US$, WACC 7,61%) da un descuento de −17,41% — muy por debajo "
         "del 30% que exige el Bloque 2. Ya no es un rango ancho de 258-401 US$: es una cifra puntual, "
         "confirmada por dos investigaciones independientes."],
        ["3 · Asimetría desfavorable, con hueco de cálculo declarado",
         "El caso bajista propio (0,65:1, ≈154 US$) ya cae por debajo del ancla más profunda; el escenario "
         "correlacionado no calculado podría ser peor, no mejor — se trata como abierto, no resuelto a favor "
         "de la tesis."]],
        [3.6*cm, 13.0*cm], font_sz=8.2)]
    o += [p("Ningún knock-out se activó y el moat core superó su prueba de estrés más reciente, por lo que esto "
        "<b>sigue sin ser un veredicto de NO</b> — es una empresa de calidad, con un mecanismo de moat core "
        "verificado y una gestión razonablemente bien incentivada (con la salvedad de insider selling sin "
        "compras, sección 8), cotizando por encima del rango que la evidencia sostiene, sin margen de seguridad "
        "defendible al precio actual, <b>y con dos huecos de evidencia específicos, fechados, que deben "
        "cerrarse antes de que el caso alcista de esta tesis pueda tratarse como probado.</b>")]
    # Sin PageBreak aquí a propósito: el párrafo de cierre de la sección 14 termina
    # a ~30% de la página y forzarlo dejaba el resto en blanco antes de la 15.
    return o
