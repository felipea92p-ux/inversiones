# -*- coding: utf-8 -*-
"""§12 cuánto vale de verdad · §13 el abogado del diablo · §14 el veredicto · §15 cierre"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, cm
from reportlab.platypus import PageBreak

def s12_valoracion():
    o = flag_titulo("12 · Cuánto vale de verdad",
                    "Todo el resultado depende, casi por entero, de un solo número que ni el emisor ni el mercado dejan usar con comodidad el extremo bajo")
    o += [p("Valorar Nemetschek exige primero fijar el coste del capital: la rentabilidad mínima que hay que "
        "exigirle a sus flujos de caja futuros para que merezca la pena el riesgo de tenerlos en vez de un bono "
        "sin riesgo. Aquí ese número —el WACC— no es un detalle técnico de fondo: <b>es la variable que decide el "
        "veredicto entero</b>, más que cualquier dato del negocio.")]
    o += [p("<b>WACC bottom-up, construido de mercado (candado B del método: nunca heredado de un tier de "
        "calidad):</b>")]
    o += [tabla([
        ["ESCENARIO", "BETA", "ERP", "WACC DESPUÉS DE IMPUESTOS"],
        ["Bajo", "0,55 (bruto, XETRA, 5 años)", "4,23% (Damodaran)", "<b>~5,4%</b>"],
        ["Central", "0,70", "4,8%", "<b>~6,3%</b>"],
        ["Alto", "0,85 (ajustado por cruce Hamada con pares EE.UU.)", "5,5%", "<b>~7,5%</b>"]],
        [2.8*cm, 6.8*cm, 3.0*cm, 4.0*cm], font_sz=8.6)]
    o += [p("Bund alemán a 10 años ~3,35% (3-4-sep-2026, cerca de máximos de 15 años); coste de deuda después de "
        "impuestos ~3,2%-3,9%; peso de deuda D/(D+E) de sólo 7%-10%, incluso post-HCSS. <b>El WACC está dominado "
        "casi por completo por el coste de equity, y el beta es el input que más mueve el resultado, con "
        "diferencia.</b>")]
    o += [callout("LA TRAMPA",
        "<b>Declaración explícita de confiabilidad del WACC, requerida por el método:</b> el rango bottom-up de "
        "5,4%-7,5% es matemáticamente correcto dado el beta medido en XETRA, pero <b>no se trata aquí como "
        "confiable como punto único</b>, por dos motivos concretos. <b>Primero:</b> el volumen medio diario de "
        "negociación es de sólo 138.887 acciones (~15,4 M € al día) para una compañía de más de 7.000 M € de "
        "capitalización —liquidez baja que hace sospechoso cualquier beta histórico calculado sobre ese papel. "
        "<b>Segundo:</b> hay dos líneas de evidencia independientes que apuntan a un WACC bastante más alto: el "
        "propio test de deterioro auditado por PwC (9,9%-13,9% en 2022-2025) y el WACC que el mercado parece "
        "exigir hoy, resuelto por DCF inverso (10,7%-11,9%). Que dos fuentes ajenas al análisis converjan en "
        "10%-14% mientras mi CAPM con beta histórico da 5,4%-7,5% es una señal fuerte de que el beta de XETRA está "
        "subestimando el riesgo sistemático real —<b>no una prueba, pero sí un motivo legítimo para no anclarse en "
        "el extremo bajo de mi propio rango.</b>")]
    o += [chart("charts/03_triangulacion_wacc.png")]
    o += [p("El §13 añade una <b>tercera fuente independiente</b> a esta triangulación: el beta re-apalancado "
        "(Hamada) de los cuatro pares cotizados en EE.UU. —0,74-1,36, todos por encima del beta bruto de "
        "Nemetschek (0,51-0,53) usado en el caso base. La triangulación de tres metodologías distintas "
        "—emisor/PwC, mercado/DCF inverso, pares/Hamada— es más difícil de descartar que cualquiera de las tres "
        "por separado.")]
    o += [chart("charts/05_beta_pares.png")]
    o += [hr(), p("<b>DCF explícito a 10 años</b>, con un sendero de crecimiento que decae desde el nivel guiado "
        "hacia un 2,5%-3% terminal:")]
    o += [tabla([
        ["ESCENARIO", "SENDERO DE CRECIMIENTO", "WACC", "VALOR"],
        ["BEAR", "10% → 3%", "7,5%", "<b>≈100 €/acción</b>"],
        ["BASE", "14% → 4%", "6,5%", "<b>≈171 €/acción</b>"],
        ["BULL", "16% → 6%", "5,5%", "<b>≈325 €/acción</b>"]],
        [3.0*cm, 5.0*cm, 2.8*cm, 5.8*cm], font_sz=8.8)]
    o += [chart("charts/01_rango_valor_vs_precio.png")]
    o += [callout("LA TRAMPA",
        "<b>Advertencia explícita, y es la más importante del documento:</b> incluso el escenario BEAR, construido "
        "con el extremo <i>alto</i> de mi propio rango bottom-up (7,5%), da un valor muy por encima del precio "
        "actual (63-68 €). <b>Esto no es una señal de compra obvia</b> —es una señal de que el resultado depende "
        "casi enteramente de aceptar que el WACC real está en mi rango 5,4%-7,5% y no en el rango 9,9%-14% que "
        "tanto el propio emisor como el mercado parecen usar. Si el WACC real fuera 10%-12% —el punto medio de "
        "las dos fuentes independientes citadas arriba, que ya supera el bookend “Alto” de 7,5% de mi propio DCF—, "
        "el valor razonable bajo el mismo sendero BEAR caería sustancialmente por debajo de 100 € —probablemente "
        "cerca de, o incluso por debajo de, el precio de mercado actual.")]
    o += [p("<b>DCF inverso (Rappaport-Mauboussin):</b> resolviendo qué WACC iguala el valor de empresa de mercado "
        "de hoy, dado el sendero de crecimiento guiado —no calculado con un WACC supuesto, sino despejado desde "
        "el precio real.")]
    o += [tabla([
        ["PRECIO HOY", "WACC IMPLÍCITO POR EL MERCADO"],
        ["63 €", "<b>11,9%</b>"],
        ["68 €", "<b>11,4%</b>"],
        ["75 €", "<b>10,7%</b>"]],
        [8.3*cm, 8.3*cm], font_sz=9.0)]
    o += [chart("charts/04_dcf_inverso_precio.png")]
    o += [p("Alternativamente: si se asume un WACC “razonable” de 9%-10% —más cercano al de los pares "
        "estadounidenses—, el crecimiento implícito en el precio de hoy es de sólo ~5%-10% en el primer año, "
        "decayendo a 3% —muy por debajo del 14%-15% guiado y batido durante nueve trimestres consecutivos.")]
    o += [p("<b>Test de trampa de valor.</b> El propio Informe Anual 2025 —fuente primaria, con el sesgo obvio de "
        "quien prefiere esa narrativa, pero corroborado independientemente por el patrón de scuttlebutt del §6— "
        "atribuye la caída del 53% desde el máximo histórico a una revalorización sectorial amplia del software, "
        "“en gran medida desconectada del desempeño operativo de las compañías” —no a deterioro de clientes, "
        "márgenes o contabilidad. No hay pérdida de clientes documentada, no hay deterioro de márgenes en las "
        "cifras reales, no hay red flag contable material. <b>No configura una trampa de valor clásica</b>, pero "
        "tampoco la descarta con certeza: el riesgo de disrupción de IA es real, no precificable por el CAPM "
        "—que sólo compensa riesgo sistemático—, y es la explicación más plausible de por qué el mercado exige un "
        "WACC 4-6,5 puntos por encima del bottom-up de libro de texto.")]
    o += [p("<b>Pares, sin rankear (candado C del método).</b> Autodesk, Trimble, Bentley Systems y Procore "
        "muestran, en distinto grado, la misma dinámica: transición a recurrencia, presión de margen de corto "
        "plazo, consolidación vía M&amp;A activa en todo el sector. Bentley —beta 0,98, más del 90% de ingresos "
        "recurrentes, NRR 109%— es el espejo de mecanismo de negocio más cercano y vale la pena vigilar cómo lo "
        "trata el mercado en los próximos trimestres, como referencia de un “compounder puro” sin el ruido de "
        "M&amp;A transformacional reciente de Nemetschek.")]
    o += [callout("PAUSA REFLEXIVA",
        "<b>La asimetría con signo, síntesis del §9 —léase junto con el §13, que la cuestiona con fuerza:</b> "
        "al alza, si el crecimiento guiado se sostiene (9 trimestres de track record en esa dirección) y el WACC "
        "“real” está más cerca de mi rango bottom-up (5,4%-7,5%) que del rango emisor/mercado (9,9%-14%), el "
        "potencial de revalorización supera el 45%-55% desde el precio actual incluso en el escenario BEAR. A la "
        "baja, si el WACC emisor/mercado (9,9%-14%) es el correcto —y hay ahora <b>tres</b> fuentes independientes "
        "que lo sugieren, no dos—, el precio actual ya refleja, o incluso sobreestima, un valor razonable bajo un "
        "sendero de crecimiento más lento (5%-10% fading a 3%), justo cuando el apalancamiento se ha multiplicado "
        "por HCSS y el segmento más rentable (Design) entra en dos años declarados como “challenging”. <b>Esta no "
        "es una asimetría limpia a favor de comprar: depende casi por completo de resolver una sola variable "
        "—el WACC verdadero— que este documento no puede resolver con los datos disponibles hoy, y que el §13 "
        "muestra que el precio de mercado de HOY ya está resolviendo en el sentido contrario al caso alcista.</b>")]
    return o + [PageBreak()]

def s13_veto():
    o = flag_titulo("13 · El abogado del diablo",
                    "Sesión limpia, sin heredar el entusiasmo ni el marco de la síntesis. Ya se ejecutó, y su valor es exactamente ese: no haber estado en la sala")
    o += [p("El Candado A del método (no negociable) exige que ningún veredicto de COMPRA se emita sin que el "
        "agente <i>abogado-diablo</i> revise el documento completo en sesión limpia. <b>Este paso ya se "
        "ejecutó</b> el 4-sep-2026. Devolvió tres objeciones centrales, un diagnóstico de sesgo, y un falsador "
        "duro. Cada pieza se procesa aquí contra la evidencia ya recogida en los §9-12, con veredicto explícito.")]
    o += [tabla([
        ["#", "LA OBJECIÓN", "VEREDICTO"],
        ["1", "<b>“El moat es prestado (regulatorio/idioma), no propio, y ya perdió la plaza más grande y "
              "contestable del mundo (EE.UU.).”</b>",
         "ACEPTADA, con corrección de encuadre: no es un evento reciente, es condición heredada desde mediados-2000s "
         "(§5). Sub-punto sobre el tamaño del mercado de EE.UU. degradado de HECHO implícito a SUPUESTO sin cita."],
        ["2", "<b>“El motor de reinversión×ROIC es casi cosmético; el crecimiento real es deuda comprando "
              "ingresos, no un motor orgánico.”</b>",
         "ACEPTADA EN SUSTANCIA, con refutación puntual de una cifra mal citada (ver abajo). La conclusión dura "
         "—crecimiento estructuralmente comprado, no ganado— se sostiene."],
        ["3", "<b>“La asimetría alcista completa depende de rechazar al auditor Y al mercado a la vez, no sólo al "
              "mercado.”</b>",
         "ACEPTADA CON EVIDENCIA — el golpe más fuerte. Reclasificada de falsador futuro a HECHO PRESENTE YA "
         "CONFIRMADO."]],
        [0.6*cm, 9.4*cm, 6.0*cm], font_sz=8.0)]
    o += [p("<b>Objeción 1, en detalle.</b> El núcleo no es un hecho nuevo: es una lectura más dura de algo que el "
        "propio §5 ya documentaba —el moat “falla” en proyectos greenfield y en EE.UU. Autodesk/Revit sigue "
        "dominante. El abogado no contradice al dossier; lo confirma y le quita el matiz suavizante. <b>Se acepta "
        "la conclusión: el moat de Nemetschek es regional, apoyado en parte en la lengua y el código de "
        "construcción local, no sólo en superioridad de producto.</b> La corrección de encuadre: “ya perdió la "
        "plaza más grande y contestable del mundo” describe una condición estructural preexistente desde "
        "mediados de la década de 2000 (Graphisoft/Revit), <b>no</b> un evento nuevo dentro del período analizado "
        "(2021-2026) —esto no debilita el golpe, corrige su framing temporal. La observación sobre la contradicción "
        "openBIM/lock-in (§4) es una crítica lógica válida como inferencia razonable, sin peso numérico adicional. "
        "Y la propuesta del abogado de buscar una encuesta de adopción de software en escuelas de arquitectura "
        "angloparlantes se adopta formalmente como Mecanismo 6 del pre-mortem (§11).")]
    o += [p("<b>Objeción 2, en detalle.</b> El abogado escribió “el ROIC ‘orgánico’ &gt;400% que se usa para "
        "defender la calidad del motor”. <b>Esa cifra no existe en el dossier como ROIC</b>: la tabla del §7 "
        "reporta una ratio de reinversión (capex+M&amp;A neto)/NOPAT de ~386% en 2024 —es decir, el año de "
        "GoCanvas la empresa reinvirtió ~3,9 veces su NOPAT en M&amp;A, no que el ROIC fuera 386%. El ROIC "
        "reportado en la misma tabla es 18%-32% en todos los años, nunca por encima de 32%. <b>Este sub-punto se "
        "refuta con evidencia directa de la propia tabla del §7</b> —un error de cita del abogado (confundió el "
        "denominador de la fórmula de reinversión con el ROIC), no un hallazgo nuevo; se corrige explícitamente "
        "para que no se propague en versiones futuras. Con esa corrección, la sustancia se sostiene sin reservas: "
        "el crecimiento de Nemetschek es estructuralmente comprado, no ganado por reinversión orgánica a ROIC "
        "alto, y el propio ROIC consolidado cayó de 28%-32% a 18%-24% exactamente cuando entró GoCanvas "
        "—consistente con dilución de calidad del capital reinvertido, no sólo con ruido contable.")]
    o += [callout("LA TRAMPA",
        "<b>Objeción 3, la más fuerte de las tres, porque no introduce ningún dato nuevo</b> —sólo aplica el peso "
        "correcto a datos que el propio §12 ya contenía. Todos los números —WACC bottom-up 5,4%-7,5%, WACC del "
        "test de deterioro del propio emisor 9,9%-13,9%, WACC implícito por el mercado 10,7%-11,9%— <b>ya estaban "
        "en el §12 antes de este ataque</b>, incluida la advertencia explícita que ya reconocía que un WACC real "
        "de 10%-12% hundiría el valor razonable por debajo del precio actual. La pieza nueva y válida: el beta "
        "Hamada de los cuatro pares de EE.UU. (0,74-1,36), que el propio dossier ya había usado parcialmente para "
        "su escenario “Alto” (beta 0,85) sin situarlo junto a las otras dos fuentes para ver la triangulación "
        "completa. <b>Re-etiquetado del “falsador duro”:</b> el abogado lo presenta como condición futura (“si el "
        "precio cae a 63 € o menos entre hoy y marzo-2027...”). Pero el precio de hoy (3-4-sep-2026) <b>ya está</b> "
        "en 63-68 € —el falsador ya está activado hoy, no es una predicción pendiente. Al precio de hoy, el WACC "
        "implícito (11,4%-11,9%) ya iguala o supera el techo del propio rango de deterioro auditado del emisor "
        "(9,9%-13,9%) para al menos alguna división. <b>Reclasificado de “CONVERTIDA EN FALSADOR” a “HECHO "
        "PRESENTE YA CONFIRMADO”</b>, con mayor peso en el veredicto que un simple gatillo futuro.")]
    o += [p("<b>Diagnóstico de sesgo — “Anclaje/confirmación en la elección de beta-WACC”: ACEPTADA sin "
        "reservas.</b> Es una autocrítica metodológica correcta y coherente con el propio Candado B (WACC siempre "
        "bottom-up de mercado, nunca heredado). El caso base de esta síntesis (§12) usó el beta bruto más bajo "
        "(0,51-0,53) como ancla de trabajo pese a que el documento ya reconocía —antes de este ataque— dos "
        "señales en sentido contrario (emisor, mercado), y sólo tras esta revisión se añade la tercera (pares "
        "Hamada). El patrón de “quedarse con la primera cifra porque genera la asimetría más atractiva” es "
        "precisamente lo que el Candado B existe para bloquear, y en este caso el bloqueo no operó del todo hasta "
        "esta revisión adversarial.")]
    o += [p("<b>Puntos que la sesión NO desarrolló, y quedan abiertos, no resueltos por este pase:</b> "
        "<b>(2)</b> si “no hay compra de insider ejecutivo” es una señal más fuerte de lo que el documento le "
        "concede —sigue como lo dejó el §6/§8, vacío documentado, sin resolver. <b>(3)</b> el mecanismo de salida "
        "de Thoma Bravo en el JV de Build &amp; Construct —sigue como incógnita abierta, sin resolver. Ambos "
        "quedan marcados explícitamente como pendientes de una segunda pasada adversarial.")]
    o += [callout("PAUSA REFLEXIVA",
        "<b>Veredicto formal del abogado del diablo:</b> OBJECIONES_QUE_EXIGEN_DEGRADAR_VEREDICTO. Ninguna de las "
        "tres objeciones fue refutada en su sustancia (sólo se corrigió una cifra mal citada dentro de la "
        "Objeción 2, sin cambiar su conclusión). La Objeción 3 usa evidencia que ya vivía dentro del propio §12 "
        "pero que no había sido pesada con la severidad que merece: el precio de mercado de HOY ya implica un "
        "WACC que iguala el techo del rango que el propio auditor de Nemetschek usa en su test de deterioro. "
        "<b>Esto no es una condición hipotética para el futuro: es el estado presente de los datos.</b> "
        "<b>No hay veto total</b> —no hay fraude, no hay fuga de clientes documentada, el drawdown tiene "
        "explicación sectorial corroborada por scuttlebutt independiente, y el negocio orgánico sigue generando "
        "ROIC de calidad—, por lo que el veredicto no baja a “NO”. Pero las tres objeciones, sumadas, exigen que "
        "el veredicto (§14) deje de tratar “el mercado se equivoca” como la lectura por defecto y pase a tratarla "
        "como la hipótesis que necesita probarse con evidencia nueva, no la que ya se da por buena.")]
    return o + [PageBreak()]

def s14_veredicto():
    o = flag_titulo("14 · El veredicto, y qué lo cambiaría",
                    "Sin limbo y sin “depende”: una espera activa, con la carga de la prueba desplazada")
    o += [p("<b>NO COMPRAR TODAVÍA</b> — reforzado, y con condiciones de reversión más duras que en el borrador "
        "previo al §13.", "h_seccion")]
    o += [p("<b>Qué cambió respecto al borrador pre-veto:</b> la categoría del veredicto no cambia —sigue sin "
        "haber knockout, sigue sin haber fraude ni fuga de clientes, el ROIC orgánico sigue siendo de calidad—, "
        "pero el <b>centro de gravedad se desplaza</b>. Antes del §13, el documento trataba “el mercado se "
        "equivoca sobre el riesgo de Nemetschek” como una hipótesis abierta con probabilidad razonable a favor. "
        "Después del §13, esa hipótesis queda como la que <b>necesita ser probada con evidencia nueva antes de "
        "comprar</b>, no como el escenario base implícito —porque el propio precio de mercado de hoy, sin "
        "necesidad de esperar ningún evento futuro, ya converge con el rango de riesgo que usa el propio auditor "
        "de la compañía. Se retira, concretamente, una condición de reversión que el borrador previo ofrecía "
        "(“que el mercado re-valorice hacia mi WACC bottom-up”) porque el §13 muestra que esa condición ya está "
        "siendo contradicha por el precio actual, no que esté pendiente de cumplirse.")]
    o += [p("<b>Razonamiento resumido:</b> ningún knockout se activa y el negocio orgánico es de calidad "
        "demostrada —ROIC 20%-30% frente a un WACC estructural más bajo en mi propio rango bottom-up, moat real "
        "aunque acotado geográficamente y ahora formalmente reconocido como “prestado” en parte del marco "
        "regulatorio local, scuttlebutt sin evidencia de deterioro competitivo. Pero el caso de valoración no es "
        "limpio: depende de una sola variable no resuelta (el WACC verdadero), y ahora <b>tres</b> fuentes "
        "independientes (emisor/PwC, DCF inverso de mercado, pares Hamada) convergen por encima de mi rango "
        "bottom-up, con el precio de hoy ya reflejando ese WACC más alto. El filtro Munger (§8) muestra que el "
        "escenario adverso —M&amp;A cara + transición interna difícil + repreciación sectorial simultáneas— ya "
        "está en marcha, no es hipotético. Hay múltiples mecanismos de pre-mortem con fecha concreta (§11, "
        "2027-2028) todavía sin resolver, y el Candado A (§13) ya se ejecutó y devolvió objeciones que exigen "
        "degradar, no un veto total.")]
    o += [p("<b>Este no es un “NO”:</b> la evidencia de calidad orgánica es demasiado sólida para descartar la "
        "empresa de forma permanente, y no hay ningún mecanismo de fraude, pérdida de clientes o ruptura "
        "estructural del negocio que justifique esa categoría. <b>Tampoco es “NO DECIDIBLE”:</b> hay evidencia "
        "suficiente y de buena jerarquía para razonar la forma de la decisión. <b>Es una espera activa, con la "
        "carga de la prueba ahora sobre el caso alcista, no sobre el bajista.</b>")]
    o += [p("<b>Condiciones que moverían el veredicto a COMPRAR</b> (revisadas y endurecidas tras el §13):")]
    o += [tabla([
        ["#", "CONDICIÓN"],
        ["a", "Una recalculación defendible del beta/WACC que <b>no</b> dependa sólo del beta bruto de baja "
              "liquidez de XETRA —por ejemplo con más historia de negociación, con una canasta de comparables "
              "europeos de mejor ajuste, o con un cruce Hamada que se acerque al rango bottom-up en vez de "
              "alejarse. <b>No basta con esperar a que “el mercado cambie de opinión”</b>, porque el mercado de "
              "hoy ya está del lado contrario."],
        ["b", "El informe FY2026 (~mar-2027) confirma el crecimiento guiado sin activar ninguno de los seis "
              "mecanismos de pre-mortem del §11 (incluido el nuevo Mecanismo 6 de erosión generacional)."],
        ["c", "Resolución explícita, con evidencia nueva, de los dos puntos que el §13 dejó abiertos sin "
              "desarrollar: insider buying ejecutivo, mecanismo de salida de Thoma Bravo."],
        ["d", "Felipe completa personalmente los Pasos 0, 1 y 7 (§3) y su juicio no contradice el marco de este "
              "documento de forma material."]],
        [0.8*cm, 15.1*cm], font_sz=8.4)]
    o += [p("<b>Condiciones que moverían el veredicto a NO:</b> cualquier impairment de fondo de comercio en "
        "Manage, GoCanvas o HCSS en los informes FY2026-FY2028 (Mecanismos 1 y 3 del §11); deuda neta pro-forma "
        "por encima de 750 M € en el informe FY2026; o confirmación de la encuesta de adopción generacional de "
        "Revit por encima del 70% en mercados angloparlantes (Mecanismo 6) combinada con desaceleración del ARR "
        "de Nemetschek.")]
    return o + [PageBreak()]

def s15_cierre():
    o = flag_titulo("15 · Cierre: predicción falsable, glosario y advertencias",
                    "Escrita antes de conocer el resultado, con fecha y umbral — es lo único que permite calificar el proceso, no la suerte")
    o += [p("<b>Predicción principal.</b> En el informe anual FY2026 de Nemetschek SE (publicación esperada "
        "~marzo-2027), se cumplirán simultáneamente:")]
    o += [tabla([
        ["#", "CONDICIÓN"],
        ["a", "Crecimiento orgánico consolidado dentro del rango guiado 14%-15% en moneda constante."],
        ["b", "Margen EBITDA en el rango 32%-33% guiado."],
        ["c", "Deuda neta post-HCSS reportada por debajo de 700 M €."],
        ["d", "Ningún cargo de deterioro de fondo de comercio en las divisiones Manage o Build &amp; Construct."]],
        [0.8*cm, 15.1*cm], font_sz=8.6)]
    o += [callout("PAUSA REFLEXIVA",
        "<b>Falsación:</b> si CUALQUIERA de los cuatro elementos falla de forma material —crecimiento por debajo "
        "de 12% ex-FX, margen EBITDA por debajo de 31%, deuda neta por encima de 750 M €, o cualquier impairment—, "
        "la lectura de “ruido sectorial sin deterioro fundamental” que sostiene el marco de este documento queda "
        "<b>falsificada</b>, y el caso debe reabrirse hacia NO, no simplemente ajustarse.")]
    o += [p("<b>Predicción secundaria, con fecha propia.</b> La mezcla de suscripción en el segmento Design "
        "alcanzará ~70% a cierre de 2026, según el objetivo declarado por management. Si en el informe FY2026 esa "
        "cifra está por debajo de 65%, la transición “challenging” de 2027 que management ya anticipa será peor "
        "de lo que la propia compañía espera, y refuerza el Mecanismo 2 del §11.")]
    o += [p("<b>Predicción añadida tras el §13, con umbral verificable en tiempo real —no de informe.</b> Si "
        "Nemetschek cotiza en XETRA por debajo de 63 €/acción en cualquier sesión entre hoy (4-sep-2026) y la "
        "publicación del informe FY2026 (~primera semana de marzo de 2027), el WACC implícito por el mercado "
        "supera el 11,9% —por encima del techo del propio rango de deterioro auditado del emisor (9,8%-13,9%) "
        "para al menos alguna división— y el caso alcista de esta tesis pasa de “el mercado no ve lo que yo veo” "
        "a “tengo razón contra el mercado y contra el auditor de la propia empresa a la vez”, el umbral que el "
        "§13 identifica como el que mata la asimetría. <b>Nota: al precio de cierre disponible en este dossier "
        "(63-68 €, 3-4-sep-2026) esta condición ya está parcial o totalmente activada</b> —se documenta como "
        "estado presente, no sólo como gatillo futuro.")]
    o += [hr(), p("<b>GLOSARIO</b>", "h2")]
    terms = [
        ("BIM", "Building Information Modeling: un modelo digital del edificio entero —geometría, materiales, "
                "costes, cronograma— que arquitecto, ingeniero y constructora comparten durante toda la vida "
                "del proyecto."),
        ("openBIM / IFC", "El estándar abierto (Industry Foundation Classes) que permite abrir un archivo BIM en "
                "cualquier software compatible. Nemetschek lo defiende frente al formato propietario de Autodesk."),
        ("Vorstand / Aufsichtsrat", "Estructura dual del gobierno corporativo alemán: el Vorstand gestiona el "
                "día a día; el Aufsichtsrat supervisa y nombra al Vorstand, sin gestionarlo."),
        ("Familienstiftung", "Fundación patrimonial familiar. La GVN Familienstiftung controla el 45,07% de los "
                "votos de Nemetschek."),
        ("SE (Societas Europaea)", "Forma jurídica de sociedad anónima europea. Nemetschek SE reporta bajo IFRS "
                "auditado (Geschäftsbericht), no ante la SEC de EE.UU."),
        ("VIE", "Entidad de interés variable: estructura donde el control se ejerce por contrato, no por "
                "propiedad accionarial mayoritaria. No aplica a la estructura de HCSS (72/28 directo)."),
        ("SAR / LTIP", "Stock Appreciation Rights / Long-Term Incentive Plan: compensación ejecutiva ligada al "
                "valor de la acción, vía equity."),
        ("WACC", "Coste medio ponderado del capital: la rentabilidad mínima exigible a una inversión dado su "
                "riesgo. Cuanto más alto, menos vale hoy cualquier flujo de caja futuro."),
        ("Beta", "Cuánto se mueve una acción cuando se mueve el mercado. Beta 1 = igual; 0,5 = la mitad."),
        ("Beta re-apalancado (Hamada)", "Ajuste que permite comparar el beta de empresas con distinta estructura "
                "de deuda, quitando y volviendo a poner el apalancamiento de cada una."),
        ("ERP (prima de riesgo de mercado)", "Lo que la bolsa debe rendir por encima del bono sin riesgo para "
                "compensar su volatilidad."),
        ("DCF (descuento de flujos)", "Proyectar el dinero futuro de una empresa y traerlo a valor de hoy con el "
                "coste de capital."),
        ("DCF inverso", "En vez de preguntar cuánto vale la empresa dado un WACC, pregunta qué WACC hace que el "
                "precio de hoy sea correcto."),
        ("ROIC", "Retorno sobre el capital invertido: cuánto beneficio genera una empresa por cada euro de capital "
                "que emplea."),
        ("NOPAT", "Beneficio operativo neto después de impuestos, antes de gastos financieros."),
        ("g = reinversión × ROIC", "La tasa de crecimiento de estado estacionario que predice reinvertir una "
                "fracción del beneficio a un retorno dado."),
        ("Test de sleep", "¿Duerme tranquilo quien tiene el foso, sabiendo que un rival con más dinero no puede "
                "quitarle el negocio? Separa un foso real de una ventaja temporal."),
        ("Moat (foso)", "La ventaja que impide a un rival quitarte el negocio aunque tenga más dinero y mejor "
                "tecnología."),
        ("Trampa de valor", "Una acción que parece barata por un múltiplo bajo, pero cuyo negocio se está "
                "deteriorando de verdad — el múltiplo bajo refleja el deterioro, no una oportunidad."),
        ("Knockout binario", "Un criterio de sí/no que descarta una empresa de plano, sin puntuación ni matiz, si "
                "se activa."),
        ("Scuttlebutt", "Método de Philip Fisher: preguntarle a todo el mundo alrededor de una empresa —clientes, "
                "competidores, proveedores— en vez de sólo a la propia empresa."),
        ("Pre-mortem", "Imaginar que la inversión ya fracasó y escribir la autopsia, con métrica y fecha, antes de "
                "invertir, no después."),
    ]
    o += [tabla([["TÉRMINO", "QUÉ SIGNIFICA"]] + [[f"<b>{a}</b>", b] for a, b in terms],
                [4.2*cm, 12.4*cm], font_sz=8.0)]
    o += [M.hr(), M.p("<b>ADVERTENCIAS Y HUECOS DECLARADOS</b>", "h2")]
    o += [p("<b>Etiquetado de la evidencia.</b> Todo dato de este documento procede de una de tres categorías: "
        "<b>HECHO</b> (fuente primaria: Geschäftsbericht IFRS auditado, comunicados EQS-News, transcripts de "
        "resultados, con documento y fecha), <b>INFERENCIA</b> (cálculo propio o dato de estudio de mercado "
        "secundario) y <b>SUPUESTO</b> (asunción justificada, explícitamente marcada). Este documento no ha hecho "
        "research nuevo: consolida evidencia ya recogida y verificada por otros agentes en la sesión, y el veto "
        "del abogado del diablo ya ejecutado en sesión limpia (§13).")]
    o += [p("<b>Los huecos que siguen abiertos, en orden de importancia:</b>")]
    o += [tabla([
        ["#", "EL HUECO", "POR QUÉ IMPORTA"],
        ["1", "<b>La correlación de la cartera con el mercado y el beta “verdadero” de NEM son, en el fondo, un "
              "juicio no cerrado</b> —tres fuentes (emisor, mercado, pares) sugieren un WACC de 10%-12%, pero "
              "ninguna es una medición directa e indiscutible.",
         "Es la variable de la que cuelga el veredicto entero, más que cualquier dato del negocio."],
        ["2", "El percentil histórico de persistencia de crecimiento (Chan-Karceski-Lakonishok, ~10%-15%) <b>no "
              "está verificado</b> en esta sesión.",
         "Sostiene la lectura de que NEM está en una cola histórica poco poblada de crecimiento sostenido — sin "
         "verificar, es sólo una intuición con nombre académico."],
        ["3", "La encuesta de adopción de Revit/Autodesk en escuelas de arquitectura angloparlantes (Mecanismo 6, "
              "§11) <b>no se localizó</b> en este dossier.",
         "Es la pieza que convertiría el supuesto de erosión generacional del moat de SUPUESTO a HECHO."],
        ["4", "Si “no hay compra de insider ejecutivo” es una señal más fuerte de lo que el documento le concede "
              "—punto (2) que el §13 dejó explícitamente sin desarrollar.",
         "Pesa sobre la lectura del filtro Munger (§8) y sobre cuánta convicción cabe en la ausencia de esa "
         "señal."],
        ["5", "El mecanismo de salida de Thoma Bravo en el JV de Build &amp; Construct —punto (3) que el §13 "
              "dejó explícitamente sin desarrollar.",
         "Es una incógnita de estructura de capital futura sobre el 28% del segmento de mayor crecimiento del "
         "grupo."],
        ["6", "La caracterización de EE.UU. como “el mercado AEC más grande y de mayor crecimiento del planeta” "
              "—degradada de HECHO implícito a SUPUESTO en el §13.",
         "Probablemente cierto, pero no debe citarse como HECHO en futuras versiones sin una cita verificable."]],
        [0.6*cm, 7.6*cm, 7.7*cm], font_sz=7.7)]
    o += [p("<b>Sobre la precisión.</b> No hay puntuación ni ranking en este documento: el sistema de puntuación "
        "de esta casa se retiró en julio de 2026. Ninguna cifra se reporta con más precisión que el ruido de su "
        "propia variable —y en este caso, el propio mercado, el propio auditor y los propios pares miden ese "
        "ruido por nosotros: tres fuentes independientes, ninguna con acceso a las otras dos, convergen en un "
        "rango de WACC que mi propio cálculo bottom-up no alcanza a explicar.")]
    o += [M.hr()]
    o += [p("<i>Documento de trabajo personal, síntesis de 4 de septiembre de 2026. Método QG de 12 pasos, "
        "“Comprensión Primero con candado adversarial”. Veredicto PROVISIONAL: Pasos 0, 1 y 7 pendientes del "
        "juicio personal de Felipe (§3). No es asesoramiento de inversión, no procede de un asesor registrado y "
        "no debe usarse como recomendación para terceros. Rentabilidades pasadas no garantizan rentabilidades "
        "futuras.</i>", "nota")]
    return o
