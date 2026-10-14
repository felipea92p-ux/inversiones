# -*- coding: utf-8 -*-
"""§8 Gestión e incentivos · §9 Knock-outs · §10 Percepción variante · §11 Pre-mortem"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, cm
from reportlab.platypus import PageBreak

def s8_gestion():
    o = flag_titulo("8 · Gestión e incentivos, leídos como texto",
                    "Continuidad cultural en la sucesión; ninguna compra discrecional de insider con dinero propio")
    o += [p("<b>Sucesión (HECHO, EDGAR).</b> El 1 de enero de 2026, Shailesh Jejurikar —COO, 36 años en la casa, "
        "previamente al mando de Fabric &amp; Home Care, el segmento más grande y exitoso— sucedió a Jon Moeller "
        "como CEO; Moeller pasó a Executive Chairman. El 29 de julio de 2026, P&amp;G anunció que Jejurikar también "
        "asumiría la presidencia del directorio desde el 1 de agosto de 2026, mientras Moeller se retira del "
        "consejo el 31 de julio de 2026 y de la compañía el 14 de agosto de 2026.")]
    o += [callout("LA TRAMPA",
        "Es continuidad cultural —promoción interna con décadas de antigüedad, el patrón histórico de P&amp;G— "
        "pero <b>concentra Chairman + CEO + President en una sola persona desde agosto de 2026</b>, reduciendo la "
        "separación formal entre quien dirige la operación y quien preside la supervisión del directorio, justo "
        "semanas antes de la fecha de este dossier. Es un dato de gobernanza a vigilar, no un juicio de valor por "
        "sí solo — pero el Filtro Munger de la sección 12 lo retoma como pérdida de contrapeso formal justo antes "
        "de esta decisión.")]
    o += [p("<b>Compensación (DEGRADADO — vía resúmenes secundarios del proxy, no lectura línea por línea del "
        "DEF 14A).</b> Salario base del CEO ~1,6 M US$, bono ~1,63 M US$, premio de largo plazo ~14 M US$ "
        "(Performance Stock Program + LTIP). Política de ownership obligatorio y clawback. Pendiente de "
        "verificación contra el PDF original antes de citarlo como HECHO duro — se etiqueta DEGRADADO por diseño, "
        "no se disfraza de dato firme.")]
    o += [p("<b>Quién compra y vende con dinero propio (HECHO, Forms 4/144 EDGAR, 2025-2026).</b>")]
    o += [tabla([
        ["QUIÉN", "QUÉ HIZO"],
        ["Jon Moeller (Executive Chairman saliente)", "Vendió 11.684 acciones (2-oct-2025, ~1,78 M US$) y presentó "
                                                        "Form 144 para 22.612 acciones más (14-ago-2026), en el "
                                                        "marco de su retiro."],
        ["Andre Schulten (CFO)", "Vendió acciones en dos ocasiones «para cubrir impuestos» de premios vencidos."],
        ["Shailesh Jejurikar (CEO)", "Recibió 16.195 acciones a 0,00 US$ como premio de compensación — no es una "
                                     "compra."],
        ["Janzaruk (Chief Accounting Officer)", "Vendió 359 acciones en mercado abierto."]],
        [5.8*cm, 10.8*cm], font_sz=8.6)]
    o += [p("<b>No se detectó ninguna compra discrecional en mercado abierto con dinero propio por parte de un "
        "ejecutivo o director en el período reciente disponible.</b> La compañía sí recompró acciones propias con "
        "caja corporativa (3,1 millones en mayo-2026 a 144,37 US$ y 2,8 millones en junio-2026 a 150,88 US$) — un "
        "dato distinto de convicción personal de insider. Lectura honesta: <b>ausencia de señal, ni positiva ni "
        "negativa</b> — común en compañías grandes donde el management ya está concentrado en acciones vía "
        "compensación histórica.")]
    return o

def s9_knockouts():
    o = flag_titulo("9 · Knock-outs mecánicos, binarios, HECHO-only",
                    "Verificado de forma adversarial contra fuente independiente: 72 puntos de datos XBRL sin una sola discrepancia")
    o += [p("Los seis knock-outs del catálogo del método son binarios: si uno se dispara, el proceso se detiene "
        "ahí sin excepción, sin importar lo que digan los pasos siguientes. Ninguno se disparó aquí.")]
    o += [tabla([
        ["KNOCK-OUT", "VEREDICTO", "EVIDENCIA (HECHO)"],
        ["(a) Estructura VIE", "<b>PASA</b>", "0 resultados en búsqueda de texto completo EDGAR «variable interest "
                                              "entity», CIK 80424, todos los 10-K desde 2001. Confirmado por segunda "
                                              "vía independiente."],
        ["(b) SBC &gt; 50% del FCF ajustado ≥3 años", "<b>PASA, con holgura amplia</b>", "SBC/FCF = 3,4%-4,0% en "
                                                       "cada uno de los 6 años FY2021-FY2026 (10-K, tablas XBRL). A "
                                                       "un orden de magnitud del umbral."],
        ["(c) ROIC &lt; WACC estructural ≥3 años", "<b>PASA</b>", "ROIC 19,8%-21,4% durante 6 años consecutivos. "
                                                    "El WACC bottom-up de la sección 12 (7,0%-7,5%) queda muy por "
                                                    "debajo — margen amplio."],
        ["(d) Restatement / reexpresión", "<b>PASA</b>", "0 10-K/A en la ventana FY2021-FY2026 (los 2 únicos "
                                          "10-K/A de la historia de P&amp;G —2008 y 2020— son correcciones de "
                                          "formato sin cambio de cifras, fuera de ventana). 13 hits de "
                                          "«restatement» en EDGAR corresponden a lenguaje de clawback o de póliza "
                                          "D&amp;O, ninguno documenta una reexpresión real. Auditor Deloitte &amp; "
                                          "Touche sin cambios ni salvedades."],
        ["(e) Dependencia de cliente/regulador único", "<b>PASA, queda como vigilancia cualitativa</b>", "Walmart "
                                                        "~15-16% de ventas 6 años consecutivos. Top-10 clientes "
                                                        "subiendo de 39% a 43% en 6 años. Muy por debajo de "
                                                        "cualquier umbral razonable de knock-out (~30-50%+). Sin "
                                                        "regulador único dominante (~180 países)."],
        ["(f) Deuda tóxica", "<b>PASA con holgura</b>", "Aa3 (Moody's, outlook elevado a POSITIVO sep-2026) / AA- "
                                                        "(S&amp;P, afirmado ene-2026, estable). Deuda neta/EBITDA "
                                                        "1,0x-1,3x estable, sin covenants en riesgo."]],
        [4.3*cm, 3.1*cm, 9.2*cm], font_sz=7.7)]
    o += [callout("PAUSA REFLEXIVA",
        "<b>Semáforo contable (diagnóstico, no veredicto).</b> VERDE en calidad de earnings (OCF/utilidad neta "
        "1,1x-1,3x sostenido), apalancamiento y auditor/controles. ÁMBAR en dos ítems que <b>no son knock-out</b> "
        "pero exigen vigilancia: <b>(i)</b> deterioro recurrente del mismo activo — Gillette se deterioró dos "
        "veces en la ventana ampliada (8.345 M US$ en FY2019, 1.341 M US$ en FY2024, este último con causa "
        "textual en el propio 10-K: «a higher discount rate, weakening of several currencies... and the impact of "
        "the non-core restructuring program»); <b>(ii)</b> tasa impositiva efectiva en ascenso sostenido "
        "(17,8%→20,8% en 4 años, ~300pb) — un viento en contra silencioso sobre la utilidad neta.")]
    o += [p("<b>Ningún knock-out se dispara. El proceso continúa.</b>")]
    return o

def s10_percepcion():
    o = flag_titulo("10 · Percepción variante", "Dominio J4 de la frontera: solo Felipe puede responder esta pregunta de forma válida")
    o += [callout("PAUSA REFLEXIVA",
        "<b>[BORRADOR DE AGENTE — PENDIENTE DE FELIPE.]</b> Solo Felipe puede declarar si tiene una percepción "
        "variante genuina, articulada con un dato verificable y NO público. Lo que sigue es el hallazgo honesto "
        "del agente sintetizador, no una respuesta válida a este paso.")]
    o += [p("<b>No se identificó, en ninguno de los tres dossiers de investigación, un dato genuinamente no "
        "público que sustente una percepción diferencial del consenso.</b> Toda la evidencia reunida —la "
        "desaceleración de cuatro años, la compresión de margen de FY2026, el WACC releverado más alto que la "
        "beta cruda, el descuento de flujos inverso que exige ~4% de crecimiento— proviene de fuentes públicas: "
        "EDGAR, 8-K, comunicados, prensa financiera.")]
    o += [p("Bajo la letra estricta del método, esto se registra literalmente como lo que es: <b>un desacuerdo de "
        "valoración con el mercado sobre datos públicos</b> —cuánto crecimiento futuro justifica el precio "
        "actual—, no una ventaja informacional propietaria.")]
    o += [callout("LA TRAMPA",
        "Esto no mata la tesis por sí solo: un desacuerdo de valoración con datos públicos sigue siendo una tesis "
        "legítima si la evidencia numérica es sólida, que lo es. Pero cambia su naturaleza. <b>Si Felipe no tiene "
        "un ángulo genuinamente no público</b> —checks de canal propios, conversación directa con un retailer, u "
        "otra fuente primaria que este dossier no cubrió—, <b>el método exige declarar aquí: «no hay percepción "
        "variante, hay consenso con pasos extra».</b> No se está comprando algo que el mercado no ve: se está "
        "comprando —o no— algo que el mercado sí ve y valora distinto.")]
    return o

def s11_premortem():
    o = flag_titulo("11 · Pre-mortem con fecha", "Escrito con la advertencia honesta de que no cumple pureza total de secuencia")
    o += [p("El gate ideal del método exige escribir el pre-mortem <i>antes</i> de conocer el resultado numérico "
        "de la valoración. Aquí, el rango de valor ya estaba parcialmente disponible en el dossier fuente, así "
        "que este pre-mortem se reconstruye post-hoc a partir de dossiers ya producidos y debe tratarse como tal "
        "— una desviación declarada, no ocultada, del proceso ideal.")]
    o += [tabla([
        ["#", "MECANISMO", "MÉTRICA Y VENTANA"],
        ["1", "<b>Erosión adicional de cuota en categorías defendidas con precio</b> (cuidado oral, cuidado del "
              "hogar). Marca privada/competidor de escala sigue ganando espacio de anaquel, replicando el patrón "
              "Gillette 2010-2016.",
         "% de combinaciones marca-canal de EE.UU. que mantienen/ganan cuota. <b>Si retrocede por debajo de ~30% "
         "durante 2 trimestres fiscales consecutivos</b> (checkpoint Q1/Q2 FY2027, oct-2026 y ene-2027), la "
         "«recuperación» reciente se confirma como temporal."],
        ["2", "<b>La compresión de margen operativo se vuelve estructural</b>, no de un solo trimestre. "
              "~1.000 M US$ después de impuestos de costos de insumos/aranceles guiados para FY2027 más la "
              "necesidad de invertir en precio erosionan el margen más allá de lo puntual de FY2026 (24,3%→22,7%).",
         "Margen operativo GAAP trimestral. <b>Si permanece por debajo de 22% durante ≥2 trimestres consecutivos "
         "de FY2027</b> (checkpoint 8-K Q2 FY2027, ~22-ene-2027)."],
        ["3", "<b>El plan de «balanced volume-price-mix» del nuevo CEO no se materializa.</b> Jejurikar apuesta a "
              "recuperar volumen bajando precio selectivamente; si el volumen no despega, la compañía queda "
              "atrapada entre menor precio y menor volumen a la vez.",
         "Componente de volumen del crecimiento orgánico por 8-K trimestral. <b>Ventana: FY2027 completo</b> "
         "(oct-2026 a jul-2027), checkpoint intermedio obligatorio ~22-ene-2027 — si el volumen permanece ≤0 en "
         "≥2 de los 4 trimestres, el mecanismo se confirma."],
        ["4", "<b>Tercer deterioro de un activo intangible núcleo</b> (Gillette u otro). El patrón repetido "
              "(2019, 2024) sugiere que el precio pagado por Gillette en 2005 sigue sin «digerirse» contablemente.",
         "Cualquier cargo de deterioro de intangible indefinido en el Item 7 / nota de goodwill del 10-K. "
         "<b>Ventana: hasta el 10-K FY2029</b> (ago-2029)."],
        ["5", "<b>Concentración de gobernanza coincide con una decisión de capital cuestionable.</b> Sin "
              "separación formal Chairman/CEO desde ago-2026, una decisión grande de M&amp;A o recompra a "
              "múltiplo alto podría carecer del contrapeso adecuado.",
         "Cualquier adquisición &gt;5.000 M US$ o programa de recompra acelerado sin due diligence pública "
         "robusta. <b>Ventana: próximos 24 meses</b> desde ago-2026 (hasta ago-2028)."]],
        [0.6*cm, 7.6*cm, 8.4*cm], font_sz=7.5)]
    return o + [PageBreak()]
