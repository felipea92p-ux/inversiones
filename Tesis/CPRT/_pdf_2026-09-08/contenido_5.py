# -*- coding: utf-8 -*-
"""15 Diario — predicciones falsables · 16 Cierre"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, cm
from reportlab.platypus import PageBreak, Spacer, KeepTogether

def diario():
    o = [KeepTogether(flag_titulo("15 · Diario — predicciones falsables, con fecha",
                    "Cuatro predicciones que se pueden ganar o perder — el punto entero de escribirlas antes, no después"))]
    o += [p("El método de esta casa exige que toda tesis deje una predicción que se pueda falsar, con fecha, "
        "escrita antes de conocer el resultado — para poder calificar el proceso más adelante, no el desenlace. "
        "El diario de esta tesis tiene ahora cuatro entradas: las tres del 4-sep, ratificadas sin cambios de "
        "contenido, y una nueva del 8-sep que reemplaza en urgencia —no en sustancia— a la primaria.")]
    o += [p("<b>Predicción primaria, de corto plazo — la más cercana y vinculante de las cuatro.</b> Al reporte "
        "del año fiscal FY2026 (cerrado 31-jul-2026, esperado ~10-sep-2026 — <b>en aproximadamente dos días desde "
        "esta síntesis</b>): si el margen operativo del segmento EE.UU. de año completo cierra por debajo de "
        "37,0% Y el crecimiento de ingresos por servicio EE.UU. de año completo es ≤0%, el veredicto pasa "
        "directamente a <b>NO</b>, sin necesidad de una sesión de síntesis nueva. Si ninguna condición se cumple, "
        "es la primera evidencia real a favor de que la compresión de margen y la desaceleración doméstica eran "
        "cíclicas, y reabre la vía hacia COMPRAR si además el precio no ha subido en la misma proporción. Un "
        "resultado mixto sostiene NO COMPRAR TODAVÍA sin cambio de categoría, pero mantiene la vara de entrada "
        "endurecida de la Sección 14.")]
    o += [callout("PAUSA REFLEXIVA",
        "<b>Nuevo falsador con fecha, del 8-sep — sobre el eje que más ha cambiado en cuatro días: el mecanismo "
        "de desintermediación (Mecanismo 2), no solo el margen.</b> En el reporte del año fiscal completo FY2027 "
        "de Copart (~10-sep-2027), el crecimiento interanual de unidades de subasta domésticas EE.UU. deberá "
        "haber sido negativo o plano (&lt;+1%) en al menos 3 de los 4 trimestres fiscales de FY2027, <b>mientras "
        "el car parc de EE.UU.</b> (S&amp;P Global Mobility/IHS) <b>se mantiene positivo en la misma ventana</b> "
        "— confirmando que el frenazo es estructural (pérdida de cuota + retención agresiva de aseguradoras vía "
        "el mecanismo que el caso Progressive ilustraría, si se confirma), no cíclico, y que el gatillo de 23,09 "
        "US$ estaba inflado por una base de Año 1 optimista. Si en cambio 3 de los 4 trimestres de FY2027 "
        "muestran unidades EE.UU. creciendo igual o por encima del car parc, la tesis «bache cíclico reversible» "
        "queda confirmada. Esta predicción no sustituye a la primaria — llega un año después y responde a una "
        "pregunta distinta (cuota, no margen) — pero es la que de verdad zanja si el caso Progressive era ruido "
        "o señal.")]
    o += [p("<b>Predicción secundaria, heredada y ratificada, sobre el eje de precio, horizonte largo.</b> Si al "
        "cierre del año fiscal 2028 (31-jul-2028) los ingresos por servicio acumulados desde FY2025 no muestran "
        "un crecimiento compuesto de al menos ≈15%-18% —el mínimo consistente con volver a una trayectoria de "
        "~5%-6% CAGR, el piso del escenario base de este documento— la tesis de «precio razonable, sin margen de "
        "seguridad» se inclina hacia sobrevaloración adicional y el veredicto debería revisarse hacia NO. Si el "
        "crecimiento acumulado supera ≈22%-25% —consistente con validar el ~7,4%+ que el mercado ya está "
        "pagando— reforzaría que el precio actual, aunque no barato, tampoco está mal calibrado, y podría abrir "
        "el camino a COMPRAR si además el precio no ha subido en la misma proporción.")]
    o += [p("<b>Predicción terciaria, heredada y ratificada, sobre el eje de moat/mecanismo, horizonte medio.</b> "
        "Si para el cierre del año fiscal 2027 (31-jul-2027) el margen operativo del segmento EE.UU. no se ha "
        "estabilizado por encima de 38%, el Mecanismo 3 del pre-mortem (erosión de poder de fijación de precios, "
        "no solo absorción táctica de inflación) quedaría parcialmente confirmado, y debería pesar en contra de "
        "cualquier escalamiento a COMPRAR incluso si el precio cae. Queda en gran parte subsumida por la "
        "predicción primaria, pero se mantiene como respaldo si el resultado del FY2026 es mixto.")]
    o += [hr()]
    o += [p("<b>Acción concreta antes del 10-sep-2026, la única no atada a una fecha de reporte:</b> verificar el "
        "caso Progressive/RB Global contra fuente primaria (10-Q, 10-K, transcript de resultados, o comunicado "
        "de RB Global), delegado a <i>verificador</i>. Es, hoy, el dato individual de mayor apalancamiento sobre "
        "el veredicto de toda esta tesis — más que cualquier ajuste fino al WACC o al terminal del DCF.", "cuerpo")]
    return o + [Spacer(1, 14)]

def cierre():
    o = [KeepTogether(flag_titulo("16 · Cierre",
                    "Glosario, y las advertencias que no deberían quedar en letra pequeña"))]
    o += [p("<b>Glosario breve</b>", "h2")]
    terms = [
        ("Ajustador (claims adjuster)", "El empleado de la aseguradora que decide si un coche siniestrado se repara o se declara pérdida total."),
        ("Beta", "Cuánto se mueve una acción cuando se mueve el mercado. Beta 1 = igual; el de Copart es 1,01-1,04 según la fuente y fecha de corte."),
        ("Cross-validación", "Una segunda sesión de síntesis, corrida desde cero por otro equipo de agentes sin leer el documento base de antemano, usada para contrastar el veredicto de forma independiente."),
        ("DCF inverso", "En vez de proyectar flujos para hallar un valor, se parte del precio de hoy y se resuelve qué crecimiento sostenido lo justificaría."),
        ("D&amp;A", "Depreciación y amortización — el gasto contable que aproxima el desgaste de los activos y del software."),
        ("DEGRADADO", "Etiqueta de esta casa para un dato citado pero no verificado contra fuente primaria — no se trata como HECHO ni se descarta, se marca y se delega a verificación."),
        ("Knock-out binario", "Una condición de descarte que se dispara o no se dispara — no se puntúa ni se rankea."),
        ("Owner earnings", "El efectivo que un dueño podría extraer del negocio sin dañar su capacidad futura de generar caja — la base del DCF de esta casa."),
        ("Pérdida total (total loss)", "Cuando el coste de reparar un coche supera su valor, menos el valor de salvamento: la aseguradora paga el valor del coche en vez de arreglarlo."),
        ("Pre-mortem", "Imaginar que la inversión ya fracasó y escribir la autopsia antes de invertir, no después."),
        ("ROIC incremental", "El retorno que genera el capital NUEVO que se invierte, distinto del ROIC promedio de todo el capital ya desplegado."),
        ("Salvage value", "El valor de un coche ya siniestrado, vendido tal cual, a un desguace, reciclador o reconstructor."),
        ("Tasa de reinversión", "La proporción del beneficio (u owner earnings) que se destina a capex de crecimiento, en vez de repartirse."),
        ("VIE (Variable Interest Entity)", "Una entidad que se consolida por control contractual, no por propiedad mayoritaria — un patrón de riesgo contable que Copart no presenta."),
        ("WACC", "Coste promedio ponderado del capital — la tasa mínima de retorno exigida, construida desde el beta, la prima de riesgo y la estructura de capital reales."),
    ]
    o += [tabla([["TÉRMINO", "QUÉ SIGNIFICA"]] + [[f"<b>{a}</b>", b] for a, b in terms],
                [4.2*cm, 12.4*cm], font_sz=8.0)]
    o += [M.hr(), p("<b>ADVERTENCIAS Y HUECOS DECLARADOS</b>", "h2")]
    o += [p("<b>Etiquetado de la evidencia.</b> Todo dato de este documento procede de una de tres categorías: "
        "<b>HECHO</b> (fuente primaria: SEC EDGAR, con documento, sección y fecha), <b>INFERENCIA</b> (cálculo "
        "propio o dato de agregador) y <b>SUPUESTO</b> (asunción justificada, marcada como tal explícitamente en "
        "cada sección) — con una cuarta etiqueta, <b>DEGRADADO</b>, para lo citado por un ejercicio adversarial "
        "sin verificación independiente (el caso Progressive es el ejemplo central de esta actualización). Un "
        "dato clave sin verificar degrada la cifra que sostiene, y el veredicto máximo posible sobre esa cifra "
        "es VIGILAR, no COMPRAR — el criterio operativo de esta casa.")]
    o += [p("<b>Lo que sigue abierto, en orden de importancia — actualizado con las tareas nuevas del 8-sep:</b>")]
    o += [tabla([
        ["#", "EL HUECO", "POR QUÉ IMPORTA"],
        ["1", "<b>El caso Progressive/RB Global (cuota ~25%→~10%, nov-2025) no está verificado contra fuente "
         "primaria.</b> (Nuevo, 8-sep.)",
         "Es el dato individual de mayor apalancamiento sobre el veredicto en este momento — más que cualquier "
         "ajuste al WACC o al terminal del DCF. Delegado a verificador como acción de máxima prioridad."],
        ["2", "<b>Los Pasos 0, 1 y 7 son borrador de agente, no el juicio real de Felipe.</b>",
         "Es la razón por la que este veredicto sigue siendo PROVISIONAL pese a dos rondas de cross-validación "
         "independiente. Ninguna cifra de valoración lo resuelve — solo Felipe puede."],
        ["3", "El margen operativo EE.UU. de FY2024 (~41,2%), usado por el abogado del diablo del 4-sep para "
         "argumentar aceleración de la compresión, no fue verificado contra el 10-K de FY2024 (EDGAR caído, "
         "HTTP 503, durante la redacción).",
         "El reporte del FY2026, en días, hará la pregunta discutible de todas formas con el año más reciente."],
        ["4", "Willis Johnson (mayor tenedor individual, ~5,7% del total en circulación) no fue verificado en la "
         "muestra de 18 Form 4 revisados.",
         "Es el insider con mayor participación económica directa; su comportamiento de compra/venta queda fuera "
         "de este documento."],
        ["5", "Scuttlebutt de compradores, desmontadores y exportadores, y serie histórica completa de "
         "guidance-vs-resultado real de Copart.",
         "El acceso a búsqueda web general estaba agotado y los sustitutos quedaron bloqueados por CAPTCHA, no "
         "forzado, por política. Vacío declarado, no relleno con inferencia."],
        ["6", "El spin-off de IAA desde KAR Holdings (~2019), la exclusividad del pilar «inserción en la "
         "decisión del ajustador» frente a software de terceros, y el beta de estrés (1,3-1,5) del Golpe 4.",
         "Todos marcados SUPUESTO — de conocimiento general, hipótesis razonable, o sensibilidad propuesta sin "
         "fuente concreta, sin verificación primaria en esta sesión."]],
        [0.7*cm, 7.5*cm, 8.4*cm], font_sz=7.5)]
    o += [p("<b>Sobre la precisión y el método.</b> Este documento no contiene score, tier ni ranking: el sistema "
        "de puntuación de esta casa se retiró el 19 de julio de 2026. El veredicto es un monólogo evidenciado, "
        "con tres candados no negociables — (A) veto del abogado del diablo en sesión limpia antes de toda "
        "COMPRA, ejecutado dos veces sobre esta tesis (4-sep y 8-sep) con el mismo resultado, todavía en piloto "
        "retroactivo; (B) WACC siempre bottom-up de mercado, nunca heredado de un tier de calidad, re-confirmado "
        "en 9,83% el 8-sep; (C) prohibición de rankear sin pasar el test de ruido, respetada aquí al comparar "
        "contra pares del sector, nunca contra otras candidatas de la cartera.")]
    o += [callout("CASO HISTÓRICO",
        "Vale la pena notar lo que NO cambió entre el 4 y el 8 de septiembre, porque dice tanto como lo que sí "
        "cambió: ningún knock-out se reabrió, el mecanismo del moat de tres pilares sigue con dos de ellos "
        "intactos, el test de trampa de valor se sostiene, y el WACC bottom-up llegó, de forma independiente, "
        "prácticamente al mismo número (9,7%-9,83%). Una segunda mirada que confirma el marco de la primera, en "
        "vez de encontrar que todo estaba mal calculado, es exactamente la clase de robustez que un proceso "
        "adversarial bien diseñado debería producir — y es distinta de la robustez que produciría una segunda "
        "mirada que simplemente repitiera el trabajo de la primera sin intentar romperla.")]
    o += [M.hr()]
    o += [p("<i>Documento de trabajo personal. Síntesis base del 04 de septiembre de 2026, con una segunda "
        "cross-validación independiente del 08 de septiembre de 2026 integrada sección por sección, no como "
        "apéndice. Los Pasos 0-9 originales se reproducen en su lógica tal como los entregó la síntesis inicial; "
        "el Paso 10 (veto del abogado del diablo, sesión limpia) se ejecutó dos veces, y ambas capas de "
        "corrección quedan explícitas en el texto, sin reescribir retroactivamente el contenido que corrigen. No "
        "es asesoramiento de inversión, no procede de un asesor registrado y no debe usarse como recomendación "
        "para terceros. Rentabilidades pasadas no garantizan rentabilidades futuras. Veredicto PROVISIONAL — ver "
        "Sección 3.</i>", "nota")]
    return o
