# -*- coding: utf-8 -*-
"""13 · El abogado del diablo · 14 · El veredicto y lo que hace falta para cambiarlo"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, cm, S
from reportlab.platypus import PageBreak, Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT

# Párrafos con constantes tipo ENUM_LARGAS_SIN_ESPACIOS: alineación izquierda,
# no justificada, para no producir huecos gigantes al justificar una "palabra" larguísima.
_izq = ParagraphStyle("cuerpo_izq", parent=S["cuerpo"], alignment=TA_LEFT)
def pi(txt):
    return Paragraph(txt, _izq)

def s13_abogado():
    o = flag_titulo("13 · El abogado del diablo",
                    "Ejecutado en sesión limpia el 4-sep-2026, sin heredar el entusiasmo de esta investigación. Su único mandato: refutar")
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
         "sección 15."],
        ["1c. Los hechos no distinguen si la concentración de clearing firm es el mismo cliente acumulando o "
              "clientes distintos rotando.",
         "ACEPTADA como brecha real",
         "No cambia el knock-out (e). Degrada la confianza del mecanismo 4 del pre-mortem (sección 11), sin "
              "resolver — pendiente del 10-K FY2026."],
        ["1d. Kalshi como riel regulatorio paralelo, calificado de «sistémico» por el propio Duffy.",
         "CONVERTIDA EN FALSADOR — ya incorporado",
         "Ya vivía en el mecanismo 2 del pre-mortem con peso de riesgo activo. El abogado confirma que ya se "
              "trata correctamente."]],
        [5.4*cm, 3.4*cm, 7.8*cm], font_sz=7.5)]
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
        "y no se puede reconstruir de forma confiable en esta etapa sin introducir precisión falsa.")]
    o += [p("<b>Corrección aplicada:</b> se declara pre-condición dura antes de cualquier COMPRAR futuro, "
        "incluso si el precio cae a la zona 235/200: calcular el escenario bajista correlacionado y confirmar "
        "si su valor por acción se mantiene por encima o cae por debajo de 200 US$. Mientras no se ejecute, el "
        "ancla de 200 US$ se trata como <b>no verificada contra el propio caso bajista de esta tesis</b> — no "
        "se cambia unilateralmente aquí (gates.md es la única fuente de verdad de gates), pero la brecha queda "
        "anotada con fecha.")]
    o += [p("<b>Sesgo probable señalado por el abogado:</b> ACEPTADO como diagnóstico correcto. Confirmation "
        "bias anclado en la sección de reinversión/g, con huella textual identificada arriba. La corrección del "
        "Golpe 2 es, precisamente, la respuesta a ese sesgo.")]
    o += [callout("LECCIÓN TRANSFERIBLE",
        "<b>Falsable duro propuesto por el abogado, CONVERTIDO EN FALSADOR:</b> share de FMX/Fenics en SOFR "
        "futures (ADV) vs. CME &gt; 3% del ADV combinado, sostenido durante un mes calendario completo, en "
        "cualquier momento antes del 16-nov-2026. Se adopta como predicción falsable adicional en la sección "
        "15 — alarma temprana, de ventana más corta y umbral menos exigente que la ya existente en el "
        "pre-mortem (&gt;5% sostenido 2 trimestres). Ambas conviven: ésta es la señal de alerta anticipada; la "
        "original es la de confirmación estructural.")]
    o += [p("<b>Veredicto del Paso 10.</b> La tesis <b>no sobrevive intacta</b> el ataque, en los mismos "
        "términos que concluyó el propio abogado: el golpe al moat core (Golpe 1) no alcanza para vetarlo, pero "
        "los Golpes 2 y 3 sí impactan de lleno y <b>tienen mecanismo, fecha, y no se resuelven con los hechos "
        "entregados</b>. Por la regla dura del método —nunca dejar un veredicto sin objeciones resueltas por "
        "escrito— estas dos objeciones se resuelven aquí: degradando explícitamente la confianza en el caso "
        "base de valoración y añadiendo pre-condiciones duras con fecha antes de cualquier reapertura hacia "
        "COMPRAR. Ver sección 14.")]
    return o + [PageBreak()]

def s14_veredicto():
    o = flag_titulo("14 · El veredicto y lo que hace falta para cambiarlo",
                    "NO COMPRAR TODAVÍA — reafirmado, pero degradado en su contenido respecto a la versión pre-Paso 10")
    o += [p("<b>NO COMPRAR TODAVÍA.</b>", "h_seccion")]
    o += [p("Sigue siendo provisional en un sentido acotado, ya señalado en el aviso de estado: los pasos de "
        "monólogo previo, círculo de competencia y percepción variante son borradores de agente pendientes de "
        "que Felipe los escriba o ratifique personalmente. Eso no cambia con este veredicto.")]
    o += [pi("<b>Por qué la categoría del veredicto no cambia</b> (sigue siendo «NO COMPRAR TODAVÍA» y no «NO» "
        "ni «NO DECIDIBLE»): el veredicto del abogado del diablo fue OBJECIONES_QUE_EXIGEN_DEGRADAR_VEREDICTO, "
        "no VETO_NO_HAY_CASO_HONESTO — no hay instrucción de matar la tesis. Además, el hecho más simple y "
        "menos disputable de todo el documento —el precio (HECHO, 281,24-281,47 US$, 4-sep-2026)— por sí solo "
        "ya sostiene «no comprar ahora» con independencia de todo el debate de WACC/g: está muy por encima de "
        "ambas anclas (235/200) sin necesitar el DCF para llegar a esa conclusión. Tampoco hay evidencia de "
        "negocio roto (ningún knock-out se activó, moat core no vetado, test de trampa de valor negativo) que "
        "justifique escalar a «NO». Y sí hay evidencia suficiente para decidir una dirección (esperar) aunque "
        "partes del cálculo interno queden con confianza degradada — eso no es lo mismo que «NO DECIDIBLE», que "
        "se reserva para cuando ni siquiera pudiera argumentarse una dirección.")]
    o += [callout("LA TRAMPA",
        "<b>Qué SÍ cambia respecto a la versión pre-Paso 10 — la degradación real, no cosmética:</b><br/><br/>"
        "<b>1.</b> El rango de valoración (258-401 US$) y en particular el caso base (357 US$, +28%) "
        "<b>dejan de tratarse como determinantes de «qué tan barato» estará CME</b> cuando el precio toque el "
        "gate. El g terminal de 3,5% que lo sostiene es un supuesto plausible pero NO verificado "
        "mecánicamente. El caso base sigue siendo un cálculo válido dentro de la banda WACC 7-9%, pero no debe "
        "usarse como justificación de convicción alcista hasta que esa brecha se cierre.<br/><br/>"
        "<b>2.</b> El ancla de entrada más profunda (200 US$) <b>se trata como no verificada contra el propio "
        "caso bajista de esta tesis</b>. El bajista propio ya calculado (~154 US$) cae por debajo de 200 US$, "
        "pero no corre el escenario correlacionado que la propia evidencia sugiere como más probable. Si ese "
        "escenario resulta peor que 154 US$, la posición podría quedar comprada por debajo del propio valor "
        "intrínseco bajista incluso entrando en el ancla «disciplinada». Esto no es una recomendación de mover "
        "gates.md — es información nueva, fechada, para quien reabra ese archivo antes del 16-nov-2026.")]
    o += [p("<b>Dos pre-condiciones duras, con fecha, antes de que esta tesis pueda escalar a COMPRAR en el "
        "futuro</b> — independientemente de que el precio caiga a la zona 235/200:")]
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
        "del método</b> aunque el precio cayera a la zona del gate.")]
    o += [p("<b>Con esa salvedad, la evidencia de esta síntesis sigue reafirmando el gate ya vigente</b> "
        "(«NO COMPRAR TODAVÍA — entrada 235/200, gate bloqueante al 16-nov-2026»), por tres razones, la primera "
        "suficiente por sí sola:")]
    o += [tabla([
        ["RAZÓN", "EVIDENCIA"],
        ["1 · Precio", "HECHO, no depende de ningún supuesto del DCF: CME cotiza ≈278-281 US$, muy por encima de ambos anclas de entrada."],
        ["2 · Valoración con WACC defendible, confianza ahora acotada",
         "El rango de valor razonable (7-9% WACC) es ≈258-401 US$/acción — compatible con «modestamente "
         "sobrevalorado» a «moderadamente infravalorado», no con el descuento de −37,9% del beta crudo "
         "(descalificado como input de decisión). El extremo alcista pesa menos que antes del Paso 10."],
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
    return o + [PageBreak()]
