# -*- coding: utf-8 -*-
"""§13 el abogado del diablo · §14 el veredicto y qué lo cambiaría · §15 cierre"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, S, C, cm
from reportlab.platypus import Spacer, PageBreak


def s10_abogado():
    o = [hr()]
    o += flag_titulo("13 · El abogado del diablo (Paso 10, ejecutado en sesión limpia)",
                    "Resultado formal: OBJECIONES_QUE_EXIGEN_DEGRADAR_VEREDICTO — el Candado A no se viola por omisión, pero exige un cambio real, no cosmético")
    o += [p("Cada objeción recibe una de tres etiquetas: <b>ACEPTADA</b> (el ataque es válido y se incorpora al "
        "veredicto), <b>REFUTADA CON EVIDENCIA</b> (el ataque no resiste un dato ya verificado), o "
        "<b>CONVERTIDA EN FALSADOR</b> (ni el documento ni el ataque tienen hoy el dato para zanjarlo, así que "
        "se transforma en una condición de falsación futura, fechada y con fuente exigida). El valor de este "
        "paso es precisamente el contexto limpio: no hereda el entusiasmo de la sesión que escribió el resto "
        "del documento.")]
    o += [callout("PAUSA REFLEXIVA",
        "<b>Golpe 1 — \"El moat: estás promediando un agujero con un balón lleno.\"</b> La cifra agregada de "
        "\"Home Care\" (octavo trimestre consecutivo de ganancia de cuota) puede esconder perfectamente una "
        "pérdida de cuota estructural en la subcategoría específica golpeada por el ciberataque de 2023 y hoy "
        "atacada por Reckitt — exactamente donde el 10% de cuota que \"no volvió\" podría estar concentrado. "
        "<b>Veredicto: ACEPTADA y CONVERTIDA EN FALSADOR.</b> No es un dato nuevo, es la corrección de un sesgo "
        "de interpretación: el documento original trataba ese hueco como neutral, quedando implícitamente a "
        "favor de Clorox, cuando la carga de la prueba debería repartirse de forma pareja. Se convierte en el "
        "<b>falsador principal</b> (ver \"Qué lo cambiaría\"), con requisito más estricto: la fuente debe ser "
        "un panel independiente (Circana/IRI o Nielsen), nunca una cifra autorreportada por ninguna de las dos "
        "partes.")]
    o += [callout("PAUSA REFLEXIVA",
        "<b>Golpe 2 — \"El motor de g: el caso base asume una inflexión que los propios números de reinversión "
        "contradicen.\"</b> El escenario BASE (margen FCF 9%→11%, g terminal 2,0%) no tiene ni un solo "
        "trimestre de capex de crecimiento positivo ni de volumen orgánico positivo que lo sostenga — la tasa "
        "de reinversión de FY2026 es negativa (−1,7%), y el CAGR real de ventas FY22-FY26 es negativo. "
        "Ponderar el escenario BAJISTA al mismo nivel que el BASE (ambos ~35% internamente) trata como "
        "igualmente probables una recuperación sin evidencia y una continuación lineal de la tendencia real. "
        "<b>Veredicto: ACEPTADA.</b> Es un ataque cuantitativo: compara una asunción del modelo contra una "
        "serie de datos ya presentes en el mismo documento que apuntan en la dirección contraria. Dos "
        "correcciones quedan incorporadas: (i) el equity implícito del caso BASE (US$101-109) se reclasifica "
        "de \"centro de gravedad\" a <b>límite superior razonable</b>; (ii) el rango recompensa:riesgo de "
        "1,3:1-1,9:1 se declara <b>probablemente optimista</b>. La reconstrucción completa del DCF con "
        "escenarios reponderados queda como tarea pendiente explícita para la próxima iteración.")]
    o += [callout("PAUSA REFLEXIVA",
        "<b>Golpe 3 — \"La asimetría: el propio número ya perdió, y el downside no es una cola normal.\"</b> "
        "1,3:1-1,9:1 ya incumple el umbral ≥3:1 sin ataque adicional. Además, el escenario bajista no es una "
        "simple compresión de múltiplo sino un escenario de balance apalancado (deuda neta/EBITDA 4,2x-4,8x, "
        "patrimonio contable ~US$252M, capital de trabajo −US$949M): un tercer recorte de guía dispararía "
        "presión de calificadoras → mayor costo de deuda → mayor compresión de equity, un bucle convexo que un "
        "promedio ponderado lineal no captura. <b>Veredicto: ACEPTADA, sin necesidad de evidencia "
        "adicional</b> — el propio Paso 9 ya reporta el fallo del umbral; el ataque cierra el argumento de que "
        "ese número, leído de forma lineal, <b>sobreestima</b> la recompensa relativa al riesgo real.")]
    o += [p("<b>Sesgo probable — \"Halo del consumidor\".</b> El prior de \"obviamente la gente sigue comprando "
        "Clorox\" permite aceptar sin fricción una cifra agregada y autorreportada (octava racha de cuota) "
        "mientras la evidencia de Reckitt —de primera mano, en la subcategoría dañada por el ciberataque— se "
        "etiqueta con más escrutinio. Es un doble estándar de evidencia a favor de la marca que el propio "
        "Felipe usa como consumidor. <b>Veredicto: ACEPTADA.</b> Corrección incorporada: ninguna de las dos "
        "cifras autorreportadas (ni la de Clorox ni la de Reckitt) se trata como suficiente por sí sola — solo "
        "un panel independiente resuelve la pregunta.")]
    o += [p("<b>Objeciones de la lista de prioridades original no resueltas por el abogado-diablo en esta "
        "sesión</b>: la contradicción S&amp;P BBB (10-K) vs. el titular de prensa \"B\", y la discrepancia "
        "interna sobre Moody's post-GOJO, <b>no fueron abordadas explícitamente</b>. Veredicto: <b>PENDIENTE — "
        "no se cierra en ninguna dirección</b>. Aplicando la misma disciplina que exige el propio sesgo "
        "probable de arriba, este documento no asume ni la lectura benigna ni la severa como ganadora. Queda "
        "asignado a <code>verificador</code> antes de que cualquier versión futura de esta tesis use la "
        "calificación crediticia —en cualquier dirección— como apoyo de un argumento.")]
    o += [hr()]
    o += [p("<b>Veredicto adversarial del Paso 10, incorporado literalmente</b>: <i>\"La tesis NO sobrevive "
        "intacta el ataque. No sobrevive como catalizador hacia una futura compra — sobrevive, como mucho, como "
        "razón para seguir mirando desde la banca.\"</i> El ataque no derriba el negocio de raíz —el ROIC por "
        "encima del WACC incluso en el peor año no fue objetado ni refutado—, pero sí derriba el "
        "<b>encuadre</b> con el que el borrador original presentaba \"NO COMPRAR TODAVÍA\": un encuadre que "
        "trataba el \"todavía\" como una espera pasiva a un trimestre más, cuando la evidencia —dos recortes de "
        "guía ya consumados, reinversión negativa, asimetría que ya falla su propio umbral— apunta a que el "
        "problema no se resuelve solo con el paso del tiempo, sino con datos duros específicos que hoy no "
        "existen en el expediente.")]
    return o


def s11_veredicto():
    o = [hr()]
    o += flag_titulo("14 · El veredicto, y qué lo cambiaría",
                    "NO COMPRAR TODAVÍA — versión endurecida. No es una espera pasiva: es una condición con escalamiento automático pre-comprometido")
    o += [p("La categoría de veredicto no cambia —este documento nunca llegó a COMPRAR, así que el Candado A "
        "no estaba en juego de forma directa—, pero el <b>encuadre y la certeza sí se degradan</b> de forma "
        "explícita, tal como exige un resultado de OBJECIONES_QUE_EXIGEN_DEGRADAR_VEREDICTO:")]
    o += [tabla([
        ["#", "QUÉ CAMBIA"],
        ["1", "<b>La asimetría no es \"insuficiente pero cercana\": es insuficiente y probablemente "
         "sobreestimada.</b> El rango 1,3:1-1,9:1 ya incumple el umbral ≥3:1; tras el Golpe 3, se declara que "
         "probablemente sobreestima la recompensa relativa al riesgo real, porque trata un downside apalancado "
         "y convexo como si fuera una cola simétrica de un promedio lineal."],
        ["2", "<b>El caso base del DCF (US$101-109) se reclasifica de \"escenario central\" a \"límite "
         "superior razonable\".</b> La evidencia de reinversión negativa (FY2026) y de crecimiento real "
         "negativo (CAGR 5 años) no sostiene todavía la inflexión de margen que ese escenario asume. El precio "
         "actual (US$93) debe leerse como más cercano al centro de una distribución correctamente escéptica de "
         "lo que la redacción original sugería."],
        ["3", "<b>El \"todavía\" deja de ser una espera pasiva.</b> Se convierte en una condición con "
         "escalamiento automático pre-comprometido: el fallo de cualquiera de los falsadores de abajo mueve el "
         "veredicto directamente a NO en la próxima revisión — no a \"seguir vigilando\" ni a un nuevo ciclo "
         "de \"todavía\"."],
        ["4", "<b>Dos huecos de evidencia permanecen abiertos</b>, sin cerrarse a favor de ninguna lectura: "
         "(i) la contradicción S&amp;P BBB vs. titular \"B\" y la discrepancia sobre Moody's, pendiente de "
         "<code>verificador</code>; (ii) el desglose de cuota de toallitas por panel independiente, pendiente "
         "— es el falsador principal."]],
        [0.8*cm, 15.8*cm], font_sz=8.4)]
    o += [p("<b>Lo que sigue sosteniendo la tesis, sin que el Paso 10 lo haya tocado</b>: ningún knock-out "
        "binario se dispara; el ROIC se mantiene por encima de un WACC bottom-up confiable (6,3-6,8%) incluso "
        "en el peor de los cinco años reportados (FY2026, ~13-15%); el WACC en sí no fue objetado por el "
        "abogado-diablo y se mantiene sin cambios; el covenant de cobertura de intereses se cumple con amplio "
        "margen (~8,9x vs. mínimo 4,0x); el plan de desapalancamiento se financia con FCF propio, sin necesidad "
        "de emitir equity ni refinanciar en condiciones adversas.")]
    o += [p("CLX permanece en el radar como <b>posición de vigilancia activa, no como candidato en trayectoria "
        "hacia COMPRAR</b>. Cualquier futura actualización que quiera mover el veredicto hacia COMPRAR debe, "
        "además de correr un nuevo Paso 10 en sesión limpia (Candado A), cerrar primero los dos huecos de "
        "evidencia con datos de fuente primaria o de panel independiente — no con una nueva lectura más "
        "optimista de los mismos datos ya disponibles.")]
    o += [hr(), p("<b>Qué lo cambiaría — predicción falsable con fecha (Paso 12, revisado tras el Paso 10)</b>")]
    o += [tabla([
        ["FALSADOR", "FUENTE Y FECHA", "REGLA"],
        ["Cuota Circana/IRI/Nielsen en toallitas desinfectantes (PRINCIPAL, exigido por el abogado-diablo)",
         "Panel independiente, nunca autorreportado. Lectura de 12 semanas más cercana a la llamada de "
         "resultados de 1T-FY2027 — ~primera semana de nov-2026.",
         "Plana o por debajo del nivel de salida del 4T-FY26 → pérdida estructural, veredicto a NO. "
         "Recuperación secuencial clara → Golpe 1 resuelto a favor de la tesis (no basta por sí solo para "
         "COMPRAR)."],
        ["Apalancamiento neto/EBITDA", "10-Q 2T-FY2027 (cierra ~31-dic-2026), presentación ~feb-2027.",
         "Debe estar por debajo de 4,0x (vs. 4,2-4,8x actual) con trayectoria de desapalancamiento visible "
         "trimestre a trimestre."],
        ["Guía FY2027 (orgánico +3,5-4,5%, EPS $5,70-$6,00)", "Cualquier 8-K entre este documento y feb-2027.",
         "Sin un tercer recorte de guía. Ya hubo dos en FY2026."],
        ["Calificación crediticia (gate nuevo, sin fecha límite dura)",
         "Resolución de la contradicción S&amp;P BBB vs. \"B\" y de Moody's, vía <code>verificador</code>.",
         "Un segundo escalón de rebaja confirmado (BBB-/Baa2) es, por sí solo, un cuarto disparador de "
         "degradación a NO, incluso si los tres falsadores anteriores no fallan."]],
        [4.3*cm, 5.3*cm, 7.0*cm], font_sz=7.7)]
    o += [callout("PAUSA REFLEXIVA",
        "<b>Regla de falsación unificada</b>: si <i>cualquiera</i> de los tres falsadores con fecha falla —"
        "cuota Circana plana o peor en nov-2026, apalancamiento aún ≥4,0x en el 10-Q de feb-2027, o una tercera "
        "revisión a la baja de la guía FY2027 en cualquier momento antes de esa fecha—, el veredicto de este "
        "documento se mueve directamente a NO en su próxima revisión. <b>No hay una tercera categoría de "
        "\"seguir vigilando otro trimestre más\"</b>: el propio Paso 10 estableció que esa salida ya fue usada "
        "dos veces (dos recortes de guía en FY2026) y que apoyarse en ella de nuevo repetiría el mismo error "
        "que el ataque señaló.")]
    return o


def cierre():
    o = [hr()]
    o += flag_titulo("15 · Cierre", "Diario, predicción falsable, glosario y advertencias")
    o += [p("<b>Entrada de diario (formato diario-decisiones.md)</b> — este documento no registra una compra "
        "ni una venta ejecutada; registra una decisión de <b>no actuar todavía</b>, con su propia falsación "
        "pre-comprometida:")]
    o += [tabla([
        ["CAMPO", "CONTENIDO"],
        ["Fecha de síntesis", "2026-09-04"],
        ["Ticker / empresa", "CLX — The Clorox Company"],
        ["Decisión", "NO COMPRAR TODAVÍA (versión endurecida tras Paso 10) — provisional, pendiente Pasos 0/1/7"],
        ["Precio de referencia", "US$93,06 (cierre regular, 4-sep-2026)"],
        ["Predicción falsable #1", "Cuota Circana/IRI/Nielsen en toallitas desinfectantes, lectura de 12 "
         "semanas ~primera semana de nov-2026: plana o peor que el 4T-FY26 → falsifica \"deterioro "
         "transitorio\", veredicto a NO."],
        ["Predicción falsable #2", "Deuda neta/EBITDA en el 10-Q de 2T-FY2027 (~feb-2027): si sigue ≥4,0x, "
         "falsifica la trayectoria de desapalancamiento guiada."],
        ["Predicción falsable #3", "Cualquier tercer recorte de la guía FY2027 antes de feb-2027 confirma el "
         "patrón de sobreestimación de gestión por tercera vez consecutiva."],
        ["Revisión obligatoria", "Trimestral — se califica el proceso de esta decisión, no el resultado del "
         "precio."]],
        [4.3*cm, 12.3*cm], font_sz=8.3)]
    o += [callout("LECCIÓN TRANSFERIBLE",
        "El error que este documento evita repetir no es de análisis: es de <b>encuadre</b>. Una tesis previa "
        "(sistema retirado, jul-2026) comunicó un apalancamiento guiado de ~3,6x sin verificarlo contra el "
        "resultado real, y el resultado real —4,25x-4,8x— llegó casi una vuelta completa de EBITDA peor. La "
        "lección no es \"desconfía de Clorox\": es <b>\"nunca heredes una cifra de apalancamiento comunicada "
        "antes del cierre de la adquisición sin re-verificarla contra el 10-K real\"</b>. Aplica a cualquier "
        "empresa que anuncie una compra grande financiada con deuda, no solo a ésta.")]
    o += [p("<b>Glosario</b>")]
    o += [tabla([
        ["TÉRMINO", "DEFINICIÓN EN ESTE DOCUMENTO"],
        ["Trust good", "Bien cuya calidad el consumidor no puede verificar en el punto de compra; la marca "
         "sustituye esa información."],
        ["Candado A / B / C", "A: veto bloqueante de abogado-diablo antes de toda COMPRA. B: el WACC siempre "
         "se calcula bottom-up de mercado, nunca se hereda de un tier. C: prohibición de rankear o comparar "
         "calidad entre empresas — solo lecturas descriptivas."],
        ["HECHO / INFERENCIA / SUPUESTO",
         "HECHO: dato verificado contra fuente primaria (10-K, DEF 14A, Form 4). INFERENCIA: lectura razonable "
         "sin verificación línea por línea. SUPUESTO: insumo de modelo (WACC, márgenes) declarado como tal."],
        ["Piso de resolución / NOPAT",
         "Piso de resolución: presentar un rango honesto en vez de fingir precisión que los datos no sostienen. "
         "NOPAT: utilidad operativa neta después de impuestos — base del DCF inverso y del cálculo de g."],
        ["ROIC / WACC", "Retorno sobre el capital invertido, y el costo de ese capital. Un negocio crea valor "
         "cuando el primero excede al segundo de forma sostenida."],
        ["Falsador", "Un dato futuro, fechado y de fuente exigida, cuyo resultado obliga a mover el veredicto "
         "en una dirección específica — no una \"señal a vigilar\" sin consecuencia."]],
        [3.1*cm, 13.5*cm], font_sz=8.0)]
    o += [p("<b>Advertencias</b>")]
    o += [p("Documento de trabajo personal, no es asesoramiento de inversión. El veredicto es "
        "<b>PROVISIONAL por partida doble</b>: (i) el Paso 10 ya se ejecutó y está incorporado; (ii) los Pasos "
        "0, 1 y 7 siguen como borrador de agente, pendientes del juicio real de Felipe. Quartr no estuvo "
        "disponible en ninguna de las tres sesiones de investigación; las citas de management en calls de "
        "resultados vienen de prensa financiera cruzada contra el 10-K, no de transcripción verbatim, y quedan "
        "DEGRADADAS un escalón. Dos huecos de evidencia —la calificación crediticia (S&amp;P BBB vs. titular "
        "\"B\", Moody's) y el desglose de cuota de toallitas desinfectantes por panel independiente— están "
        "formalmente asignados a <code>verificador</code> y no deben usarse en ninguna dirección hasta "
        "resolverse. Este documento reemplaza cualquier sistema retirado (qg-seilern, val-mos, ultra-tesis-qg, "
        "tesis-forja, consejo-maestros, ranking-qg); no contiene score ni tier, y ninguna cifra de esta tesis "
        "se hereda de esos sistemas.")]
    return o
