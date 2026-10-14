# -*- coding: utf-8 -*-
"""15 · Diario · 16 · Cierre"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, cm
from reportlab.platypus import PageBreak


def diario():
    o = flag_titulo("15 · Diario: predicciones falsables, con fecha",
                    "Paso 12 del método — lo único que permite calificar el proceso más adelante en vez de calificar la suerte")
    o += [p("Toda tesis de esta casa —se compre o no— registra una predicción con métrica, umbral y fecha. Las "
        "cuatro primeras vienen del cierre del 4-sep; la quinta se añade hoy, y no es una predicción sobre el "
        "negocio: es una predicción sobre el propio proceso de decisión, la clase de entrada de diario que el "
        "método exige cuando una corroboración cruzada ocurre a mitad de camino.")]
    o += [tabla([
        ["#", "PREDICCIÓN FALSABLE", "FECHA"],
        ["1", "<b>Sobre continuidad del moat/crecimiento:</b> si en el reporte de FY2027 el crecimiento "
              "orgánico a moneda constante cae dos trimestres consecutivos por debajo del 6% guiado, o el "
              "margen operativo ex-Mobility deja de expandirse trimestre a trimestre, la tesis de continuidad "
              "que sostiene el caso base del DCF queda falseada.",
         "~feb-2028"],
        ["2", "<b>Sobre el knockout (c), Falsador Duro adoptado del abogado del diablo:</b> el WACC de la "
              "materia crítica de auditoría del JV S&amp;P Dow Jones Indices. Umbral: si es ≥11,0% "
              "(continuando 9%→10%→10,8%) y el DCF sigue anclado en Ke≈9,3%/WACC≈8,5%-9,0% sin recalcular, "
              "el caso base actual (~360 US$) cae al rango hoy etiquetado como bajista (~260-280 US$). Si "
              "para esa fecha no se ha reconciliado explícitamente contra el DCF, el veredicto provisional "
              "pasa de «NO COMPRAR TODAVÍA» a «NO». <b>Éste es, tras la corroboración del 8-sep, el falsador "
              "individual más importante de todo el documento.</b>",
         "~feb-2027"],
        ["3", "<b>Sobre el vector de salida del moat de Ratings vía crédito privado:</b> si el 10-K FY2026 o "
              "un 10-Q intermedio desglosa el % de ingresos de Ratings proveniente de crédito privado y su "
              "margen segmentado resulta &lt;55% (frente al 64% de Ratings tradicional en FY2025), la objeción "
              "del Golpe 1 queda confirmada como erosión activa del moat, no sólo como riesgo declarado — el "
              "veredicto debe revisarse hacia «NO» salvo evidencia compensatoria clara en otro frente.",
         "2026-2027"],
        ["4", "<b>Sobre la contaminación cíclica del crecimiento orgánico:</b> si en 2026-2027 los datos "
              "primarios de emisión de deuda muestran deceleración a dígito simple bajo Y el AUM ligado a "
              "S&amp;P/DJI decelera en un año de mercado plano, queda demostrado que el 6%-9% de 2025 fue "
              "mayoritariamente beta cíclica — la fase de arranque del DCF base debe recalcularse con una "
              "tasa de partida más baja, y el caso base pasa a estar por debajo de ~360 US$.",
         "2026-2027"],
        ["5", "<b>[Nueva, del 8-sep] Sobre la propia disciplina de tratar el knockout (c) como «abierto» y "
              "no como STOP:</b> Felipe decidió el 8-sep mantener el tratamiento no-STOP de este documento "
              "pese a que una sesión paralela, con diseño distinto, habría detenido el proceso en el Paso 2. "
              "Predicción falsable sobre el propio proceso: si para el falsador duro de la predicción 2 "
              "(~feb-2027) NO se ha completado la reconstrucción del WACC corporativo consolidado prometida en "
              "la sección 14(c) —es decir, si esta tesis llega a la fecha de vencimiento del falsador sin haber "
              "hecho el trabajo que la propia casa se comprometió a hacer—, eso debe registrarse como un fallo "
              "de proceso de esta casa, no sólo como una incertidumbre de mercado sin resolver. Calificar el "
              "proceso, no sólo el resultado, es la regla que gobierna el diario de decisiones.",
         "~feb-2027"]],
        [0.7*cm, 12.9*cm, 2.4*cm], font_sz=7.5)]
    o += [callout("LECCIÓN TRANSFERIBLE",
        "La predicción 5 es distinta de las otras cuatro, y vale la pena decir por qué se incluye. Las "
        "predicciones 1-4 son apuestas sobre qué hará el negocio o el mercado. La predicción 5 es una apuesta "
        "sobre si esta casa hará el trabajo que dijo que haría. Un método que sólo audita sus predicciones sobre "
        "el mundo, y nunca sus propias promesas de seguimiento, termina acumulando falsadores que nadie revisa "
        "a tiempo. Registrar esto aquí, hoy, es más barato que descubrir en feb-2027 que el trabajo prometido "
        "en la sección 14 nunca se hizo.")]
    return o + [PageBreak()]


def cierre():
    o = flag_titulo("16 · Cierre",
                    "Glosario y las advertencias que este documento no puede omitir")
    o += [p("<b>Glosario</b>", "h2")]
    terms = [
        ("NRSRO", "«Nationally Recognized Statistical Rating Organization»: el registro que otorga la SEC a "
                   "una calificadora de crédito. La base legal del moat de Ratings."),
        ("Moat (foso)", "El mecanismo que impide a un rival quitarte el negocio aunque tenga más dinero y "
                          "mejor tecnología. En S&amp;P Global es regulatorio y contractual, no técnico."),
        ("WACC", "Coste promedio ponderado del capital: la tasa mínima de retorno que un negocio debe superar "
                  "para crear valor. Se construye bottom-up de mercado (Rf + beta×ERP para el equity, coste de "
                  "deuda post-tax, ponderados por estructura de capital)."),
        ("Owner earnings", "El beneficio que de verdad le queda al dueño de un negocio después de toda la "
                             "reinversión necesaria para mantenerlo — distinto del beneficio contable."),
        ("DCF inverso", "En vez de proyectar flujos para hallar un valor, se parte del precio de mercado y se "
                         "pregunta qué crecimiento tendría que cumplirse para justificarlo."),
        ("ROIC", "Retorno sobre el capital invertido: cuánto beneficio genera una empresa por cada dólar de "
                  "capital que emplea. Se compara siempre contra el WACC, nunca en aislado. Este documento usa "
                  "dos definiciones de capital invertido —«base ampliada» y «capital invertido bruto»— que dan "
                  "cifras distintas pero coinciden en el patrón: el ROIC ronda o queda por debajo del WACC en "
                  "los años más recientes."),
        ("Knockout binario", "Un hecho que, de confirmarse, descalifica una tesis sin necesidad de seguir "
                               "analizando — se marca sí/no con evidencia citada, nunca con una puntuación."),
        ("VIE", "Entidad de interés variable («Variable Interest Entity»): una estructura societaria que puede "
                 "requerir o no consolidación contable según normas específicas (ASC Topic 810)."),
        ("AUM", "Activos bajo gestión («Assets Under Management»): el dinero que un fondo o vehículo de "
                 "inversión gestiona. La base sobre la que Indices cobra sus «asset-linked fees»."),
        ("Critical audit matter", "Una materia que el auditor externo de una empresa identifica como de "
                                    "riesgo elevado y juicio significativo — requiere revelación y escrutinio "
                                    "adicional en el informe de auditoría."),
        ("Corroboración cruzada", "Cuando dos procesos independientes, sin compartir método ni conocer el "
                                    "resultado del otro, llegan a la misma conclusión cualitativa por caminos "
                                    "distintos. No sustituye a resolver la pregunta de fondo, pero eleva la "
                                    "confianza en que la primera respuesta no fue un artefacto de un solo "
                                    "método elegido a modo."),
    ]
    o += [tabla([["TÉRMINO", "QUÉ SIGNIFICA"]] + [[f"<b>{a}</b>", b] for a, b in terms],
                [3.6*cm, 13.0*cm], font_sz=8.0)]
    o += [hr()]
    o += [p("<b>ADVERTENCIAS Y HUECOS DECLARADOS</b>", "h2")]
    o += [p("<b>Etiquetado de la evidencia.</b> Todo dato de este documento procede de una de tres categorías: "
        "<b>HECHO</b> (fuente primaria: SEC EDGAR —10-K, 10-Q, 8-K, DEF 14A de CIK 0000064040—, Treasury.gov, "
        "con documento, sección y fecha), <b>INFERENCIA</b> (cálculo propio o dato de agregador) y "
        "<b>SUPUESTO</b> (asunción justificada, sin fuente primaria que la confirme). Un dato clave sin "
        "verificar degrada la cifra que sostiene, y una cifra DEGRADADA limita el veredicto máximo posible a "
        "VIGILAR — regla que ya se aplicó al owner earnings base de la sección 12.")]
    o += [p("<b>Fuente adicional consultada en la sesión de finalización del 4-sep:</b> "
        "«Rankings/El_Foso_y_el_Peaje_2026-09-03.pdf» (10 páginas, leído íntegro 2026-09-04) — usado "
        "exclusivamente para la reconciliación del Golpe 3 (sección 13); no se trató como fuente primaria de "
        "datos financieros de S&amp;P Global, sólo como documento comparativo de método a auditar por su propia "
        "procedencia.")]
    o += [p("<b>Sobre la sesión de corroboración del 8-sep:</b> corrió en paralelo con MA y CPRT, sin haber "
        "leído este documento de antemano. Su aportación se limitó al Paso 2 (ROIC, sección 9) — no se "
        "re-corrieron los Pasos 3 a 9 de esta tesis, porque esa sesión no llegó tan lejos en su propio proceso "
        "antes de detenerse. No hay, por tanto, evidencia fresca de mercado que añadir a las secciones 5 a 12 "
        "de este documento más allá de esa corroboración aritmética puntual.")]
    o += [p("<b>Nota de fuentes de todo el documento:</b> Quartr no estuvo disponible en ninguna de las tres "
        "investigaciones de base (cuenta sin plan Pro activo). Todo el trabajo se hizo directamente sobre SEC "
        "EDGAR, Treasury.gov y dos fuentes de mercado (stockanalysis.com, finviz.com) para beta y "
        "capitalización, más Damodaran/NYU Stern para la ERP. La jerarquía de fuentes del método se respetó: "
        "filings primarios &gt; comunicados 8-K con cita del CEO &gt; datos de mercado de dos fuentes cruzadas "
        "&gt; prensa secundaria, marcada como tal en cada caso donde se usó.")]
    o += [p("<b>Sobre la precisión.</b> No hay puntuación ni ranking en este documento: el sistema de "
        "puntuación de esta casa se retiró el 19 de julio de 2026. Ninguna cifra se reporta con más precisión "
        "que el ruido de su propia variable — el propio caso base declara su owner earnings como cifra "
        "DEGRADADA, y el DCF inverso se presenta como rango, no como punto.")]
    o += [callout("PAUSA REFLEXIVA",
        "Lo que queda pendiente de Felipe, resumido una última vez: los Pasos 0 (monólogo previo), 1 (círculo "
        "de competencia) y 7 (percepción variante) son, en este documento, borrador de agente — no el juicio "
        "real de Felipe, exactamente igual que el 4-sep. El veredicto NO COMPRAR TODAVÍA reduce el riesgo "
        "inmediato de esa brecha, porque no hay una compra pendiente de ejecutarse sobre un juicio prestado. "
        "Pero si la evidencia futura —el Falsador Duro de febrero de 2027, el margen de crédito privado, la "
        "descomposición de ciclo— empujara este veredicto hacia COMPRAR, esos tres pasos deben completarse o "
        "ratificarse por Felipe antes de comprometer capital. Es la condición que este documento no puede "
        "satisfacer por sí solo, y la corroboración cruzada del 8-sep no la satisface tampoco: confirma "
        "aritmética, no reemplaza juicio propio.")]
    o += [p("<i>Documento de trabajo personal, elaborado el 4 de septiembre de 2026 con el método Quality "
        "Growth de 12 pasos — «Comprensión Primero con candado adversarial» — sobre 3 dossiers independientes "
        "de fuente primaria, 1 verificación adversarial y 1 veto de abogado del diablo en sesión limpia; "
        "actualizado el 8 de septiembre de 2026 con precio vivo y con la corroboración cruzada independiente "
        "del ROIC descrita en la sección 9. No es asesoramiento de inversión, no procede de un asesor "
        "registrado y no debe usarse como recomendación para terceros. Rentabilidades pasadas no garantizan "
        "rentabilidades futuras.</i>", "nota")]
    return o
