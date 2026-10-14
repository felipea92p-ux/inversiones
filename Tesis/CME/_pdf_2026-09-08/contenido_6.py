# -*- coding: utf-8 -*-
"""12 · Cuánto vale de verdad — WACC, la corrección de beta de hoy, DCF, DCF inverso, trampa de valor, asimetría"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, cm
from reportlab.platypus import PageBreak

def s12_valoracion():
    o = flag_titulo("12 · Cuánto vale de verdad",
                    "WACC bottom-up de mercado (Candado B) — nunca heredado de un tier de calidad — y la corrección de beta que llegó el 8-sep-2026")
    o += [p("<b>El problema que decidía toda esta sección hace cuatro días.</b> Beta de CME: <b>0,27</b> "
        "(HECHO, Yahoo Finance y stockanalysis.com, dos fuentes independientes, consultado 4-sep-2026). Con un "
        "WACC construido sobre ese beta (Rf≈4,77-4,80%, ERP≈4,2-4,5%): <b>Re≈6,0%, WACC≈5,9%</b> — el spread "
        "entre el coste de equity y el coste de deuda pre-impuesto de CME (≈5,3%, índice ICE BofA AA US "
        "Corporate) quedaba por debajo de 1 punto porcentual, económicamente implausible para el accionista, "
        "que es acreedor residual/subordinado. El documento del 4-sep ya lo descartó como input de decisión "
        "—correctamente— pero lo hizo con una banda de reemplazo relativamente ancha (7%-9%), sin una cifra "
        "puntual defendible. Ese vacío es el que se cierra hoy.")]
    o += [callout("EN ROMÁN PALADINO",
        "<b>Cómo se hizo la corrección de hoy, en cinco pasos, sin una sola cifra nueva inventada:</b><br/><br/>"
        "<b>1.</b> Una sesión de investigación separada corrió el método de 12 pasos, desde cero, sobre cinco "
        "tesis en paralelo (CME, OBIC/4684.T, TRI, RELX, CSU.TO) — sin haber leído los documentos de CME del "
        "4-sep de antemano.<br/>"
        "<b>2.</b> En las cinco empresas, de forma independiente, el abogado del diablo de esa ronda detectó el "
        "mismo defecto de origen: el beta usado para el WACC casi con certeza se midió en una ventana de calma "
        "que antecede al episodio de estrés o distorsión específico de cada acción.<br/>"
        "<b>3.</b> Aplicado a CME: 0,27 es el beta <i>más bajo</i> de sus cuatro pares bursátiles directos "
        "—CBOE 0,41, ICE 0,93, NDAQ 0,97— en la misma tesis que la sección 6 de este documento describe "
        "atacada por FMX, calificado por la propia gerencia de riesgo competitivo mayor. Un beta que no refleja "
        "ni siquiera el riesgo competitivo que el propio documento base ya declaraba como el más severo es la "
        "definición operativa de «beta baja = momentum circular».<br/>"
        "<b>4.</b> Corrección aplicada: beta = <b>0,65</b>, el promedio simple de los cuatro pares bursátiles "
        "(0,27+0,41+0,93+0,97 = 2,58 → 0,645).<br/>"
        "<b>5.</b> Validación cruzada independiente: el beta sectorial de Damodaran/NYU Stern para «Investments "
        "&amp; Asset Management» (dataset enero-2026) es <b>0,66</b> — a una centésima del promedio de los "
        "pares. Dos métodos que no se construyeron el uno a partir del otro llegando al mismo número es "
        "exactamente el tipo de convergencia que el método pide antes de confiar en una corrección.")]
    o += [chart("charts/03_beta_pares.png")]
    o += [tabla([
        ["ESCENARIO", "Re", "WACC", "ESTADO"],
        ["Beta crudo 0,27 (4-sep)", "~6,0%", "~5,9%", "RECHAZADO — spread con deuda AA- implausible"],
        ["Beta ajustado Bloomberg-style (4-sep)", "~7,0%", "~6,9%", "Referencia técnica únicamente"],
        ["<b>Beta corregido 0,65 (8-sep, decisión)</b>", "<b>~7,8%</b>", "<b>7,61%</b>",
         "<b>USADO PARA DECIDIR — validado cruzado (Damodaran 0,66)</b>"],
        ["Beta del sector inmediato ~0,70 (4-sep)", "~7,9%", "~7,7%", "Coincide con el corregido de hoy"],
        ["Piso conservador, beta=1,0 (4-sep)", "~9,2%", "~9,0%", "Techo de la banda defendible"]],
        [6.4*cm, 2.6*cm, 2.6*cm, 5.0*cm], font_sz=7.9)]
    o += [p("<b>El resultado más tranquilizador de esta corrección no es el número en sí, es dónde cae.</b> "
        "7,61% no aterriza en un territorio nuevo y ajeno a este documento: cae <i>dentro</i> de la banda de "
        "trabajo 7%-9% que el propio documento del 4-sep ya había defendido como razonable frente al beta "
        "crudo, casi encima del beta del sector inmediato (~0,70) que ese mismo documento proponía como ancla "
        "alternativa. Una validación construida por gente que no había visto esa banda llega, por su cuenta, "
        "casi al mismo sitio. Eso es lo que hace que esta corrección se trate como una confirmación robusta y "
        "no como un ajuste cosmético.")]
    o += [chart("charts/02_wacc_sensibilidad.png")]
    o += [hr(), p("<b>Valor intrínseco, descuento y gatillo — la cifra que decide el veredicto hoy.</b>")]
    o += [tabla([
        ["MÉTRICA", "ANTES (beta crudo 0,27)", "CORREGIDO HOY (beta 0,65)"],
        ["WACC", "6,49%", "<b>7,61%</b>"],
        ["Valor intrínseco por acción", "450,31 US$", "<b>338,79 US$</b>"],
        ["Descuento aparente vs. precio (279,81 US$)", "−37,9%", "<b>−17,41%</b>"],
        ["Gatillo de compra (MoS 30%, Bloque 2)", "315,22 US$", "<b>237,15 US$</b>"]],
        [6.0*cm, 5.3*cm, 5.3*cm], font_sz=8.4)]
    o += [callout("LA TRAMPA",
        "<b>Una precisión que este documento no puede saltarse: la tabla de arriba es una construcción "
        "independiente, no el mismo DCF del 4-sep con el beta cambiado.</b> El caso base del Paso 9 original "
        "(sección de abajo) usa owner earnings TTM ≈4.113 M US$, un WACC de 7,5% y un g terminal de 3,5%, y da "
        "357 US$. La cross-validación del 8-sep construyó su propio modelo, con su propio punto de partida y "
        "su propia curva de crecimiento, y con un WACC muy cercano (7,61% vs. 7,5%) llegó a 338,79 US$ — no "
        "357. La diferencia (≈5%) es exactamente el tipo de ruido que dos modelos independientes deberían "
        "producir cuando están de acuerdo en lo esencial pero no comparten cada supuesto línea por línea. "
        "<b>Este documento usa 338,79 US$ y su gatillo derivado (237,15 US$) para la decisión de hoy —es la "
        "cifra que incorpora el beta corregido—, pero no borra ni sustituye el 357 US$ del Paso 9 original: "
        "ambos quedan documentados, con su procedencia explícita, para que ningún lector confunda dos cálculos "
        "distintos con una sola cifra.</b>")]
    o += [p("<b>El colchón del knock-out de calidad se estrecha, no se rompe.</b> ROIC (~9,6%, medición propia "
        "de la cross-validación del 8-sep) sigue por encima del WACC corregido (7,61%) — el knock-out (c) "
        "(sección 9) sigue en PASA. Pero el colchón cae de ~3,7 puntos porcentuales (con el WACC preliminar de "
        "esa misma corrida) a ~2,0pp con el WACC final. La corrección de beta no mata la tesis de calidad, pero "
        "sí reduce el margen de error disponible antes de que el propio knock-out se invierta.")]
    o += [p("<b>Por qué el veredicto no escala a COMPRAR pese a que el beta corregido «ayuda» al caso alcista "
        "frente al beta crudo:</b> el abogado del diablo de la ronda del 8-sep, al estresar el caso, usó un ERP "
        "(5,0-5,5%) más alto que el ERP implícito vigente de Damodaran (4,2-4,5%) — lo que exageraba "
        "artificialmente el WACC estresado y, con él, el «descuento» aparente en sentido contrario. Corregido "
        "también ese ERP, incluso usando el beta más agresivo de los cuatro pares (NDAQ, 0,97), el WACC "
        "estresado da sólo ≈8,99% — que sigue sin cruzar el ROIC de 9,6%. El knock-out estructural de calidad "
        "se sostiene en ambas direcciones del ejercicio: ni el beta crudo optimista ni el ERP pesimista mal "
        "calibrado cambian la conclusión de fondo.")]
    o += [hr(), p("<b>DCF explícito a 10 años (Paso 9 original, 4-sep) — tabla de supuestos clave, sin "
        "modificar.</b>")]
    o += [tabla([
        ["SUPUESTO", "VALOR", "DE DÓNDE SALE"],
        ["Punto de partida: owner earnings TTM (FCF−SBC)", "≈4.113 M US$ (~11,4 US$/acción)", "10-Q Q2-2026"],
        ["Crecimiento inicial", "~8%", "Cercano al CAGR realizado 2021-2025 (~8,5%)"],
        ["Crecimiento terminal (año 10)", "3,5%",
         "<font color='#8C1410'><b>Marcado como supuesto plausible, NO verificado mecánicamente "
         "(Paso 10, Golpe 2) — ver sección 7</b></font>"],
        ["WACC empleado en el caso base del 4-sep", "7,5%", "Dentro de la banda defendible 7%-9%"],
        ["Garantías de clientes (158.100 M US$)", "Excluidas del cálculo", "No pertenecen a CME; sólo el spread retenido entra como línea aparte"]],
        [5.4*cm, 4.6*cm, 6.6*cm], font_sz=8.2)]
    o += [tabla([
        ["WACC / g terminal", "VALOR/ACCIÓN", "vs. precio 279,81 US$"],
        ["9,0% / 3,5% (piso conservador, 4-sep)", "~258 US$", "≈−8%"],
        ["7,61% (corregido hoy) / g propio de la corrida 8-sep", "338,79 US$", "≈+21%"],
        ["7,5% / 3,5% (caso base 4-sep, banda defendible)", "~357 US$", "≈+28%"],
        ["5,9% / 3,5% (beta crudo — muestra por qué era peligroso)", "~599 US$", "≈+114%"]],
        [8.8*cm, 3.8*cm, 3.8*cm], font_sz=8.6)]
    o += [p("La progresión completa ilustra el riesgo que ya advertía el documento del 4-sep: con un spread "
        "WACC−g de apenas 2,4 puntos (escenario de beta crudo), el múltiplo terminal implícito salta a ~43x "
        "owner earnings del año 10, frente a ~19x en el escenario de 9%. El punto corregido de hoy (7,61%) cae "
        "justo en el tramo donde ese múltiplo vuelve a ser razonable — otra forma de ver por qué la corrección "
        "de beta importa tanto para la disciplina de entrada.")]
    o += [p("<b>Escenario de tasas cayendo</b> (exigido explícitamente por el método, calculado en el Paso 9 "
        "original): Rf cayendo ~80pb reduce el WACC de ~7,7% a ~6,9% (ayuda a la valoración), pero golpea la "
        "línea de «investment income» de reinversión de colateral (2.819 M US$ brutos en 6 meses de 2026 sobre "
        "158.100 M US$ de performance bonds/guaranty fund, de los cuales 138.500 M están depositados en la Fed, "
        "10-Q, HECHO) — CME retiene sólo un spread neto de ese bruto, no el total, pero el recorte es real. "
        "Resultado neto: valor/acción sube de ~357 a <b>~401 US$ (+12%)</b> — efecto real pero mucho más modesto "
        "que una sensibilidad ingenua de «sólo bajar el WACC».")]
    o += [callout("LA TRAMPA",
        "<b>Hueco de evidencia declarado en el Paso 10 (Golpe 3, 4-sep) — sigue abierto hoy, sin cambios.</b> "
        "Este escenario de tasas cayendo se corrió de forma aislada, sin combinarlo con una caída simultánea de "
        "volumen/incertidumbre. El escenario correlacionado (Rf −80pb + volumen normalizándose + reversión "
        "parcial de margen) es exactamente el que el abogado del diablo identificó como ausente y más probable "
        "que el bajista aislado de esta sección. <b>No se pudo calcular con los hechos disponibles ni en el "
        "4-sep ni en esta actualización del 8-sep</b> — la corrección de hoy fue sobre beta/WACC, no sobre este "
        "hueco. Ver sección 13 y la predicción cuaternaria de la sección 15 para la tarea pendiente con fecha.")]
    o += [hr(), p("<b>DCF inverso (Rappaport-Mauboussin).</b> Al precio actual (279,81 US$) contra owner "
        "earnings TTM ≈4,1 mil millones de dólares, el yield implícito es ≈4,05% (múltiplo ≈24,7x). Con el WACC "
        "corregido hoy (7,61%), el mercado exige un crecimiento perpetuo de owner earnings de <b>≈3-4% anual</b> "
        "— sensiblemente por debajo del CAGR realizado 2021-2025 (~8,5%), pero ya no con el margen casi "
        "inexistente que exigía el WACC de beta crudo (5,9%, barra de entrada ~1,9%).")]
    o += [p("<b>Test de trampa de valor.</b> Revenue orgánico, margen operativo y ROIC <b>no se han "
        "deteriorado</b> — al contrario, mejoraron sostenidamente 2021-2025. No se detectó M&amp;A grande "
        "reciente que infle el crecimiento reportado. <b>Veredicto: no hay señales de trampa de valor "
        "clásica.</b> El riesgo real nunca fue «negocio roto», sino que el «descuento» que un WACC mal "
        "construido sugería era en gran parte artefacto de ese WACC — algo que la corrección de hoy confirma "
        "de forma cuantitativa: el descuento real es la mitad del que el beta crudo prometía.")]
    o += [hr(), p("<b>Asimetría riesgo/beneficio, con signo (Paso 9 original, sin recalcular hoy).</b>")]
    o += [chart("charts/01_valor_intrinseco.png")]
    o += [tabla([
        ["ESCENARIO", "VALOR/ACCIÓN", "vs. PRECIO ACTUAL"],
        ["Caso base 4-sep (WACC 7,5%, desaceleración ~8%→3,5% terminal)", "~357 US$",
         "<font color='#6C7E48'><b>+28%</b></font> — confianza degradada, ver sección 13"],
        ["Corregido hoy (beta 0,65, WACC 7,61%, cross-validación 8-sep)", "338,79 US$",
         "<font color='#C60C2A'><b>+21%</b></font> — insuficiente frente al 30% de MoS del Bloque 2"],
        ["Caso bajista propio, no centinela (WACC 9,5%, haircut −8% al owner earnings inicial por compresión de "
         "fee, crecimiento plano ~2,5-3%/año)", "~154 US$",
         "<font color='#8C1410'><b>−44%</b></font>"]],
        [8.6*cm, 3.2*cm, 4.6*cm], font_sz=7.9)]
    o += [p("<b>Asimetría: aproximadamente 0,65:1 (desfavorable)</b> — el caso bajista, construido con supuestos "
        "propios y no centinela, es de magnitud comparable o mayor a cualquiera de los dos casos alcistas. El "
        "propio valor del caso bajista (~154 US$) cae <b>por debajo</b> del ancla de entrada más profunda ya "
        "fijada en el gate vigente (200 US$) — información nueva a considerar para ese archivo, no una "
        "recomendación de moverlo.")]
    o += [callout("PAUSA REFLEXIVA",
        "Este caso bajista (~154 US$) <b>NO corre el escenario correlacionado</b> (tasas y volumen cayendo "
        "simultáneamente) que el abogado del diablo identificó como más probable que el aislado, y la "
        "corrección de beta de hoy no lo resuelve — son dos huecos distintos. Se desconoce si el resultado "
        "correlacionado sería mejor o peor que 154 US$ — es una tarea pendiente con fecha, no una cifra "
        "calculada. <b>Mientras no se resuelva, el ancla de 200 US$ debe tratarse como no verificada contra el "
        "propio caso bajista de esta tesis.</b>")]
    # Sin PageBreak aquí a propósito: el callout final de la sección 12 no llena
    # una página completa por sí solo (deja ~85% en blanco); se permite que la
    # sección 13 arranque en el espacio restante de esa misma página en vez de
    # desperdiciar una página casi vacía.
    return o
