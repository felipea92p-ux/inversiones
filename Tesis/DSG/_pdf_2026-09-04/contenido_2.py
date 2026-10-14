# -*- coding: utf-8 -*-
"""§3 Scuttlebutt · §4 Motor de crecimiento · §5 Gestión e incentivos · §6 Knockouts"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, S, C, cm
from reportlab.platypus import Spacer, PageBreak, Paragraph


def s3_scuttlebutt():
    o = flag_titulo("3 · Scuttlebutt: lo que se ve desde fuera del filing",
                    "El paisaje competitivo se consolidó en 2025 — y esta tesis no tiene la voz directa de un solo cliente para juzgar qué significa eso")
    o += [p("<b>Consolidación competitiva, comparación directa entre dos años del mismo documento (HECHO).</b> "
        "En la AIF FY2025 (22-abr-2025), Descartes nombraba tres franquicias competidoras bajo el paraguas "
        "\"E2Open\" (antes Blu-Jay/Kewill, Amber Road, INTTRA). Un año después, en la AIF FY2026 "
        "(11-mar-2026), esas tres referencias fueron reemplazadas por una sola: \"WiseTech (antes INTTRA)\". "
        "Esto coincide con la adquisición real de e2open por WiseTech Global —USD 2.100 millones, anunciada "
        "el 25 de mayo de 2025 y cerrada el 4 de agosto de 2025— y no fue una venta desde la fortaleza: "
        "e2open llegó con ingresos FY2024 en caída (-4,2%) y una pérdida neta de aproximadamente USD 660 "
        "millones.")]
    o += [p("La lectura, sin veredicto todavía: el paisaje competitivo de Descartes en aduanas y cumplimiento "
        "pasó de tres o cuatro jugadores fragmentados (uno de ellos deteriorado) a un solo rival consolidado "
        "con más escala. No se encontró, dentro del presupuesto de esta investigación, evidencia de una "
        "pérdida de cuenta concreta de Descartes hacia WiseTech desde el cierre de esa operación — pero "
        "tampoco se encontró lo contrario. Es un vacío, no una tranquilidad.")]
    o += [p("<b>Los pares operativos sanos sugieren que el problema no es de categoría.</b> Manhattan "
        "Associates y Kinaxis, en el mismo sector adyacente de software de cadena de suministro, batieron "
        "guía en sus últimos resultados públicos con crecimiento SaaS/cloud fuerte (24-26% y 16-20% "
        "respectivamente). Esto es contexto de industria, no un ranking — el Candado C de la casa prohíbe "
        "convertir esta comparación en una puntuación—, pero reduce la probabilidad de que la desaceleración "
        "orgánica de Descartes sea un fenómeno de categoría generalizado. Apunta más a algo específico de la "
        "empresa: madurez del motor de M&amp;A, o cambio de mezcla de producto.")]
    o += [p("<b>Los huecos, declarados sin rodeos.</b> No hay reseñas cualitativas de clientes en esta "
        "investigación — G2 y Capterra devolvieron error 403 al intentar acceder— y no hay transcripts "
        "primarios de pares vía Quartr (degradación de fuente declarada al inicio de este documento, "
        "Sección 3). El scuttlebutt de esta tesis se apoya en datos estructurados de resultados públicos, "
        "no en voces directas de clientes evaluando alternativas. Es exactamente el tipo de hueco que el "
        "candado del abogado del diablo trata como agravante, no como nota al pie (ver Sección 13, "
        "respuesta al encargo (d)).")]
    return o + [PageBreak()]


def s4_motor():
    o = flag_titulo("4 · El motor de crecimiento: g = reinversión × ROIC",
                    "Descartes recicla casi todo lo que gana — la pregunta es a qué retorno, y ese dato falta exactamente donde más importa")
    o += [p("La identidad contable que explica cualquier compounder es simple: el crecimiento sostenible "
        "(g) es el producto de cuánto reinvierte una empresa de su beneficio operativo neto después de "
        "impuestos (NOPAT) y a qué retorno sobre el capital invertido (ROIC) lo hace. Cuanto más alto el "
        "ROIC sobre lo reinvertido, menos reinversión hace falta para el mismo crecimiento — y viceversa.")]
    o += [tabla([
        ["AÑO FISCAL", "CRECIMIENTO ORGÁNICO (corregido)", "REINVERSIÓN (Capex+M&amp;A neto / NOPAT)", "ROIC (metodología propia)", "ROIC (verificación independiente)"],
        ["FY22", "13,9%", "n.d.", "11,1%", "—"],
        ["FY23", "7,2%", "n.d.", "12,1%", "—"],
        ["FY24", "9,0%", "n.d.", "11,9%", "—"],
        ["FY25", "5,0%", "n.d.", "11,8%", "—"],
        ["FY26", "3,9%", "≈95% (US$5,7M capex + US$151,6M M&amp;A neto)", "12,5%", "13,9% (stockanalysis.com, 4-sep-2026)"],
        ["Q1 FY27", "11,1% (salto)", "n.d. (trimestral, no reconstruido)", "—", "—"]],
        [1.9*cm, 3.1*cm, 5.0*cm, 2.6*cm, 3.9*cm], font_sz=7.9)]
    o += [p("<b>El motor cuadra internamente como identidad contable</b>: g implícito FY26 ≈ 95% × 13,9% ≈ "
        "13,2%, cercano al crecimiento total real de FY26 (12%). Pero cuadrar la identidad no es lo mismo "
        "que validar la calidad del crecimiento. La lectura dura: <b>Descartes recicla prácticamente todo su "
        "NOPAT en comprar empresas a un ROIC blended modesto (11-14%)</b>. Un compounder que reinvierte al "
        "95% con un ROIC de 25-30% justificaría el titular de crecimiento sin ambigüedad. Aquí la "
        "reinversión es casi total sobre un ROIC apenas por encima de lo que probablemente sea su propio "
        "coste de capital (Sección 12).")]
    o += [chart("charts/03_capital_allocation_fy26.png")]
    o += [p("<b>Y aquí está el hueco de evidencia más importante de todo el documento.</b> El 96% del capital "
        "reinvertido en FY26 (~US$151,6M de US$157,3M) fue a tres adquisiciones concretas — 3GTMS (US$112,7M), "
        "Finale (~US$39,2M neto) e Idelic (US$25,3M) — compradas en lo que el propio CEO describe como un "
        "\"mercado de vendedores\": condiciones de fondos de capital privado activamente vendiendo activos "
        "(Ryan, Q2 FY26), no un foso permanente que garantice precios de entrada favorables. <b>No existe "
        "divulgación individual (no blended) del ROIC o payback de ninguno de los tres deals.</b> El ROIC "
        "blended de 12,5-13,9% es retrospectivo y está dominado por adquisiciones más antiguas y más baratas "
        "ya maduradas, como MacroPoint. No se sabe si 3GTMS, Finale e Idelic rinden igual, mejor o peor que "
        "ese blended.")]
    o += [chart("charts/02_crecimiento_organico.png")]
    o += [p("<b>Qué limita el crecimiento, hoy (HECHO + INFERENCIA):</b>")]
    o += [tabla([
        ["FACTOR", "LECTURA"],
        ["Pipeline y múltiplos de M&amp;A", "Condición de mercado favorable hoy (\"PE firms are in selling mode\", "
         "Ryan, Q2 FY26) — no un foso permanente; puede revertir y encarecer el pipeline."],
        ["ROIC marginal de deals recientes", "DESCONOCIDO — el hueco más importante del documento; "
         "elevado a bloqueante explícito por el Paso 10 (Sección 13, Golpe 2)."],
        ["Concentración geográfica EE.UU.", "68,1% de ingresos expuestos a un shock arancelario/regulatorio "
         "en una sola jurisdicción."],
        ["Motor orgánico estructural", "Más lento en 3 de los últimos 4 cierres completos (9,0%→5,0%→3,9%) "
         "antes del salto transaccional de Q1 FY27."]],
        [4.4*cm, 12.2*cm], font_sz=8.4)]
    o += [callout("LECCIÓN TRANSFERIBLE",
        "<b>e2open ejecutó, en apariencia, la misma jugada que Descartes: crecer por adquisiciones seriales "
        "en software de cadena de suministro.</b> Terminó con ingresos cayendo, una pérdida neta de ~USD 660 "
        "millones por impairment de goodwill, y fue absorbida por WiseTech a una fracción de su valoración "
        "de entrada. El mecanismo que la hundió no fue la estrategia de comprar crecimiento — fue que el "
        "ROIC marginal de esas compras cayó por debajo del coste de capital mientras la deuda que las "
        "financiaba seguía intacta. La lección transferible no es \"nunca compres empresas de roll-up\": es "
        "<b>nunca aceptes el ROIC blended histórico como prueba de que las compras nuevas rendirán igual</b> "
        "— exactamente la pregunta que Descartes todavía no ha respondido sobre 3GTMS, Finale e Idelic. La "
        "diferencia real y genuina a favor de Descartes es que financia todo esto con caja propia, no con "
        "deuda — un mitigante de solvencia, no una respuesta a la pregunta de retorno.")]
    o += [p("<b>Percentil histórico de persistencia de crecimiento (INFERENCIA desde memoria de literatura "
        "académica — marcado como SUPUESTO, sin verificación de fuente primaria en esta sesión):</b> la "
        "literatura sobre persistencia de crecimiento (Chan, Karceski &amp; Lakonishok y trabajo relacionado) "
        "encuentra de forma consistente que sostener crecimiento de doble dígito durante 8-10 años seguidos "
        "es estadísticamente raro — la mayoría de las empresas revierte a la media de su industria en pocos "
        "años. No se tiene la cifra exacta de percentil verificada hoy. El punto direccional que sí sostiene "
        "la evidencia propia de este dossier es que el propio DCF inverso de Descartes (Sección 12) "
        "<b>exige exactamente ese escenario poco frecuente</b> para justificar el precio actual.")]
    return o + [PageBreak()]


def s5_gestion():
    o = flag_titulo("5 · Gestión e incentivos",
                    "Doce años de mando estable, un bonus atado a una métrica que las compras inflan con facilidad, y ventas de insiders sin compras que las contrapesen")
    o += [p("<b>Trayectoria (HECHO).</b> Edward J. Ryan es CEO desde el 26 de noviembre de 2013 — más de 12 "
        "años— y lleva 26 años en la empresa. Tenencia larga, sin señales de rotación en la cúpula.")]
    o += [p("<b>Compensación e incentivos (HECHO, Circular del 27-abr-2026).</b> La compensación total de "
        "Ryan en FY26 fue de USD 10.438.129, creciente frente a FY25 (USD 8.402.372) y FY24 (USD 8.463.615), "
        "dominada por equity (más del 80%). <b>La bandera a vigilar:</b> el incentivo anual se pagó al "
        "máximo por \"sobre-desempeño frente a objetivos de EBITDA ajustado\" — una métrica no-GAAP definida "
        "por la propia empresa, no FCF ni ROIC. Esto sesga el incentivo ejecutivo hacia crecer el EBITDA "
        "ajustado —que las adquisiciones inflan con facilidad vía adiciones de vuelta— más que hacia "
        "disciplina de capital. Es coherente con, no contradictorio a, la reinversión del 95% del NOPAT "
        "observada en la Sección 4.")]
    o += [tabla([
        ["EJECUTIVO", "TENENCIA DE EQUITY (HECHO)", "NOTA"],
        ["Edward J. Ryan (CEO)", "USD 50,7M", "Mayormente RSU/PSU no vendidas; cero acciones comunes puras."],
        ["Brett (CFO)", "USD 22,2M", "—"],
        ["J. Scott Pagan", "USD 44,8M", "Incluye USD 18,2M en acciones comunes directas — la mayor "
         "tenencia en acciones puras de cualquier NEO."]],
        [4.3*cm, 3.6*cm, 8.7*cm], font_sz=8.4)]
    o += [p("<b>Comprador o vendedor con dinero propio (HECHO, fuente secundaria — agregador, no SEDI "
        "directo).</b> En 24 meses, seis insiders vendieron 174.126 acciones por CAD 21,7 millones; solo un "
        "insider —el Secretario Corporativo, no un NEO— compró, y fue simbólico: 730 acciones por "
        "CAD 100.287. Las ventas más grandes —Ryan por CAD 3,07M y Pagan por CAD 1,83M, ambas el "
        "13-abr-2026— coinciden con el mismo día de un ejercicio de opciones reportado en el Circular, un "
        "patrón consistente con \"cashless exercise\" mecánico (probablemente 10b5-1), no necesariamente "
        "convicción bajista discrecional.")]
    o += [p("Dicho esto, el patrón agregado de dos años es claro: <b>insiders vendedores netos consistentes, "
        "sin compra discrecional relevante de ningún NEO.</b> No es, por sí sola, una señal de alarma "
        "aislada — pero tampoco hay nada que la contrapese. Sin hallazgos materiales fuera de lo habitual "
        "en transacciones con partes relacionadas.")]
    o += [callout("PAUSA REFLEXIVA",
        "Un CEO con 12 años en el cargo y balance impecable inspira confianza casi por reflejo. Pero la "
        "pregunta correcta no es \"¿confío en Ryan?\" — es \"¿el sistema de incentivos que Descartes le "
        "diseñó empuja hacia lo mismo que le conviene al accionista de largo plazo?\". Un bonus atado a "
        "EBITDA ajustado, financiado por adquisiciones cuyo ROIC individual nadie divulga, es un sistema "
        "que recompensa el tamaño antes que la calidad del capital desplegado. Eso no es una acusación — "
        "es una estructura, y las estructuras predicen comportamiento mejor que las intenciones.")]
    return o


def s6_knockouts():
    o = flag_titulo("6 · Knock-outs binarios (Paso 2 del método)",
                    "El catálogo de fallos automáticos — si alguno se dispara, la tesis termina aquí sin necesidad de discutir valoración")
    o += [p("Catálogo aplicado sobre cinco años fiscales (FY22-FY26), todos re-derivados de forma "
        "independiente por verificación adversarial. <b>Los seis pasan limpio</b> — ninguna objeción del "
        "abogado del diablo recayó sobre este paso (Sección 13).")]
    o += [tabla([
        ["KNOCK-OUT", "RESULTADO", "EVIDENCIA"],
        ["1. Entidad de interés variable (VIE)", "NO se dispara",
         "Declaración directa de gerencia: \"We do not have any variable interests in variable interest "
         "entities\" [Ex-99.2 al 40-F FY26]."],
        ["2. SBC &gt; 50% del FCF ajustado, ≥3 años", "NO se dispara",
         "Serie SBC/FCF: 6,4% → 7,3% → 8,2% → 9,4% → 8,0% (FY22-FY26). Tendencia al alza en 4 de 5 años, "
         "pero un orden de magnitud por debajo del umbral."],
        ["3. ROIC &lt; WACC estructural, ≥3 años", "No evaluable como binario aquí",
         "Exige el WACC bottom-up de la Sección 12 (Candado B). ROIC propio 11,1%→12,1%→11,9%→11,8%→12,5% "
         "(serie plana), corroborado independientemente en 13,9% (stockanalysis.com) — dos metodologías, "
         "sin reconciliar, ambas en banda 11-14%."],
        ["4. Restatement contable", "NO se dispara",
         "Casilla \"No\" confirmada en el 40-F FY2025 y en el 40-F FY2026 — verificación adversarial revisó "
         "los dos años, no solo uno."],
        ["5. Dependencia de cliente/regulador único", "NO se dispara",
         "\"No single customer accounted for more than 10% of the accounts receivable balance as of "
         "January 31, 2026 and 2025\" [Nota 5]. Sí hay concentración geográfica a vigilar (no es knock-out): "
         "ingresos EE.UU. 66,7%→67,5%→68,1% (FY24-FY26)."],
        ["6. Deuda tóxica", "NO se dispara — extremo opuesto",
         "Deuda a largo plazo = US$0 en los cinco años sin excepción. Línea de crédito US$350-500M "
         "totalmente sin usar."]],
        [4.6*cm, 3.0*cm, 8.4*cm], font_sz=8.0)]
    o += [p("<b>Los seis knock-outs binarios pasan limpio — la tesis avanza a valoración con el negocio "
        "intacto.</b> Esto es lo que hace que el veredicto final de este documento (Sección 14) sea "
        "\"NO COMPRAR TODAVÍA\" y no \"NO\": ninguna de las tres únicas puertas hacia un \"NO\" definitivo del "
        "método —fallo de círculo de competencia certificado, knock-out disparado, o moat roto del todo— "
        "está cerrada. Lo que falla no es el negocio. Es el precio frente a la evidencia disponible sobre "
        "cuánto durará y a qué retorno se sostiene su crecimiento.")]
    return o + [PageBreak()]
