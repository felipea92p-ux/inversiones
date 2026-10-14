# -*- coding: utf-8 -*-
"""9 · Knock-outs binarios · 10 · Percepción variante · 11 · El pre-mortem"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, cm
from reportlab.platypus import PageBreak


def knockouts():
    o = flag_titulo("9 · Los hechos que podrían romper la tesis",
                    "El catálogo fijo de knockouts binarios del Paso 2 del método — con su fuente y su resultado, no una opinión")
    o += [p("El método exige revisar seis knockouts binarios antes de avanzar a cualquier otro paso — cada uno "
        "se marca o no se marca con evidencia citada, nunca con una impresión general. Cinco de los seis no se "
        "marcan. El sexto —ROIC frente a WACC— es el hallazgo central de todo este dossier, sigue sin "
        "resolverse incluso después del veto del abogado del diablo, y el 8 de septiembre recibió una segunda "
        "prueba independiente que se detalla más abajo.")]
    o += [tabla([
        ["#", "KNOCKOUT", "RESULTADO Y FUENTE"],
        ["(a)", "<b>Estructura VIE</b>", "NO SE MARCA. Verificado dos veces, cita idéntica verbatim en FY2025 y "
            "FY2023: <i>«no consolidation requirements under Topic 810 of the ASC»</i> {10-K FY2025, Nota 1, "
            "presentado 2026-02-11}."],
        ["(b)", "<b>SBC &gt;50% del FCF ajustado ≥3 años</b>", "NO SE MARCA. Máximo observado en 5 años: 9,5% "
            "(2022, año de la fusión IHS Markit). Resto de años: 3,7%-5,2%. Verificado exacto, sin discrepancia."],
        ["(c)", "<b>ROIC &lt; WACC estructural ≥3 años</b>", "<font color='#C60C2A'><b>ABIERTO, no resuelto — "
            "y corroborado por una segunda vía de cálculo el 8-sep-2026 (ver más abajo).</b></font> Con el WACC "
            "preliminar (8,5%-9,5%) sólo 2 años quedan por debajo (FY2022 8,0%, FY2023 7,0%); FY2024 (10,0%) y "
            "FY2025 (11,7%) quedarían por encima. Pero con el WACC <b>auditado</b> que la propia compañía usa "
            "para valorar la participación no controladora del JV S&amp;P Dow Jones Indices —9% (FY2021) → 10% "
            "(FY2023) → 10,8% (FY2025), critical audit matter— FY2022 y FY2023 siguen por debajo, FY2024 queda "
            "en zona gris, y FY2025 supera el WACC auditado por menos de 100 puntos básicos. <b>Es plausible que "
            "el knockout SÍ se dispare, 2022-2024, tres años consecutivos.</b>"],
        ["(d)", "<b>Restatement</b>", "NO SE MARCA. Casilla sin marcar en portada del 10-K FY2025 y de los años "
            "intermedios revisados; sin mención de reexpresión en el texto de los tres 10-K leídos."],
        ["(e)", "<b>Dependencia de cliente único / regulador</b>", "MATIZADO, no knockout puro. Ningún cliente "
            "supera 10% de ingresos consolidados {10-K FY2025}. Pero Ratings —30,8% de ingresos "
            "consolidados— depende de mantener el registro NRSRO ante la SEC y equivalentes UE/UK: una "
            "concentración de riesgo regulatorio en casi un tercio del negocio consolidado."],
        ["(f)", "<b>Deuda tóxica</b>", "NO SE MARCA. Deuda 100% senior notes no garantizados, cupón fijo, "
            "vencimientos escalonados hasta 2062. Covenant único (deuda/flujo de caja ≤4:1) «nunca excedido» "
            "{10-K FY2025, p.65}. El salto de deuda de 4.100 a 11.000 M US$ en 2022 coincide con la fusión, sin "
            "señal de estrés."]],
        [0.8*cm, 4.0*cm, 11.4*cm], font_sz=7.6)]
    o += [callout("LA TRAMPA",
        "Hay una hipótesis que atenúa parcialmente la lectura del knockout (c), sin resolverla: el capital "
        "invertido de base «orgánica» —excluyendo el goodwill y los intangibles de la fusión IHS Markit— es "
        "<b>negativo</b> todos los años posteriores a la fusión. El negocio heredado de S&amp;P Global standalone "
        "genera retornos indefinidamente altos sobre capital tangible, y la compresión de ROIC observada es en "
        "parte un artefacto de cómo se contabilizó una fusión pagada mayoritariamente en acciones —el conteo de "
        "acciones diluidas saltó +32% en 2022—, no necesariamente destrucción de valor económico. Esto es una "
        "hipótesis razonable, <b>no un hecho que resuelva el knockout.</b>")]
    o += [p("<b>Actualización 2026-09-08 — una segunda vía de cálculo llega al mismo sitio.</b> Cuatro días "
        "después de escribir lo anterior, una sesión de trabajo distinta —corriendo el mismo método de 12 pasos "
        "en paralelo para MA y CPRT— evaluó S&amp;P Global desde cero, sin haber leído este documento. Su Paso "
        "2 recalculó el ROIC con una definición <i>distinta</i> de capital invertido: bruto en vez de ajustado "
        "—deuda más patrimonio menos caja, con el goodwill íntegro de la fusión IHS Markit en el denominador, "
        "sin el ajuste de «base orgánica» que este documento discute arriba—. El resultado: <b>ROIC 5,4% "
        "(FY2023) → 7,8% (FY2024) → 9,1% (FY2025)</b>, con el knockout (c) disparado tres años consecutivos "
        "frente al WACC preliminar de 9,3%. Es una cifra distinta a la «base ampliada» de este documento —lo "
        "cual es esperable, porque parte de una definición de capital invertido más estricta—, pero apunta en "
        "la misma dirección exacta: el ROIC de S&amp;P Global, calculado por dos caminos independientes, ronda "
        "o queda por debajo de cualquier versión razonable del WACC en los años más recientes.")]
    o += [callout("EN ROMÁN PALADINO",
        "Esto no es un hallazgo nuevo — es una corroboración de la aritmética. Nadie le dio a esa segunda "
        "sesión el número al que tenía que llegar; llegó sola, por su propio camino, a un lugar compatible con "
        "lo que este documento ya sostenía. Eso vale más que si el mismo analista hubiera repetido el mismo "
        "cálculo dos veces: es la diferencia entre pedirle a alguien que revise tu suma y pedirle a alguien que "
        "haga la cuenta de cero sin enseñarle la tuya, y que llegue igual al mismo sitio.")]
    o += [p("<b>Pero el diseño de esa segunda sesión trataba cualquier disparo del knockout como un STOP "
        "mecánico, sin apelación</b> — a diferencia de este documento, que tuvo acceso al WACC auditado del JV "
        "de Índices y trató la ambigüedad entre WACC preliminar y WACC auditado como «no resuelta», dejando "
        "correr el proceso completo hasta el veto del abogado del diablo (Paso 10, sección 13) antes de fijar "
        "un veredicto. Consultado sobre la discrepancia de diseño, <b>Felipe resolvió el 8-sep-2026 mantener el "
        "tratamiento de este documento: el knockout (c) sigue ABIERTO, no cerrado como STOP.</b> La razón: la "
        "sesión paralela no tenía el dato del WACC auditado del JV —su STOP mecánico es un defecto de diseño de "
        "esa sesión concreta, no evidencia nueva que deba mover el veredicto por sí sola. El falsador que "
        "resolvería esto de verdad ya está fijado y con fecha: si el WACC auditado del JV de Índices en el 10-K "
        "FY2026 (~feb-2027) llega a <b>≥11,0%</b>, el veredicto de esta tesis pasa de NO COMPRAR TODAVÍA a NO. "
        "Hasta entonces, «abierto» significa exactamente eso: ni descartado, ni confirmado.")]
    return o + [PageBreak()]


def percepcion():
    o = flag_titulo("10 · Qué creo distinto del consenso",
                    "Percepción variante — marcada, como exige el método, con su estado real de borrador")
    o += [callout("PAUSA REFLEXIVA",
        "<b>[BORRADOR DE AGENTE — PENDIENTE DE QUE FELIPE LO ESCRIBA O RATIFIQUE PERSONALMENTE, NO ES SU "
        "JUICIO REAL]</b>")]
    o += [p("Propuesta tentativa, sin convicción real todavía: <i>«El mercado trata a S&amp;P Global post-spin "
        "como un ‘toll compounder’ homogéneo de 4 segmentos, pero puede que no esté diferenciando bien el mix "
        "interno: Ratings e Indices (switching cost regulatorio/contractual duro, márgenes 60-70%+) tienen un "
        "mecanismo de moat categóricamente distinto al de Market Intelligence (20-36% de margen, el segmento "
        "que la propia empresa señala como más expuesto a la desintermediación por IA). Si el múltiplo "
        "consolidado que paga el mercado está calibrado sobre el mix ‘bueno’ (Ratings/Indices) sin descontar "
        "suficientemente el segmento más débil, hay un error de valoración dentro del propio precio de mercado "
        "— no necesariamente al alza ni a la baja del conjunto, sino de composición.»</i>")]
    o += [p("Esto es una hipótesis a validar o descartar por Felipe, no una convicción establecida por este "
        "documento. No se ha hecho ningún trabajo adicional para separar el múltiplo implícito de cada "
        "segmento dentro del precio consolidado de hoy — sería el siguiente paso lógico si Felipe decide que "
        "esta línea de pensamiento merece perseguirse. La sesión del 8 de septiembre tampoco avanzó en esto: se "
        "limitó al Paso 2 (sección 9), sin llegar a este punto del método.")]
    return o + [PageBreak()]


def premortem():
    o = flag_titulo("11 · El pre-mortem",
                    "Seis mecanismos específicos que matarían esta tesis — cada uno con su métrica observable y su ventana temporal")
    o += [p("Escrito antes de conocer el precio objetivo, como exige el método, para que ningún riesgo pueda "
        "amoldarse al resultado de la valoración. Cinco mecanismos vienen del análisis original; el sexto lo "
        "añadió el abogado del diablo (Golpe 2, sección 13) y se incorpora aquí con su propio umbral.")]
    o += [tabla([
        ["#", "MECANISMO", "MÉTRICA OBSERVABLE Y UMBRAL", "VENTANA"],
        ["1", "<b>Desintermediación por crédito privado.</b> Emisiones que evitan estructuralmente el rating "
              "público NRSRO erosionan la base direccionable de Ratings — la propia compañía ya lo reconoce "
              "como frente activo, no hipotético.",
         "Crecimiento del «billed issuance» de Ratings divergiendo negativamente y de forma sostenida frente al "
         "mercado total de deuda. <b>Umbral reforzado tras el veto: margen segmentado de crédito privado "
         "&lt;55%</b> (frente al 64% de Ratings tradicional) cuando se divulgue.",
         "2 trimestres consecutivos, revisable hasta el reporte de FY2027 (~feb-2028); el chequeo de margen "
         "es revisable ya desde el próximo 10-K (~feb-2027)."],
        ["2", "<b>Deslinde regulatorio</b> — repetición de Dodd-Frank 939A, pero esta vez consumado. Basel, "
              "ESMA o reguladores bancarios de EE.UU. eliminan efectivamente la referencia obligatoria a "
              "ratings NRSRO en el cálculo de capital regulatorio bancario.",
         "Cualquier norma FINAL (no propuesta) del Comité de Basilea, ESMA o reguladores bancarios federales "
         "de EE.UU. que remueva el uso de ratings externos en el risk-weighting de capital.",
         "Sin fecha fija — revisión anual mínima durante 3-5 años, en cada ciclo de implementación de "
         "Basilea y reforma de mercados de capitales UE."],
        ["3", "<b>Comoditización del índice de referencia.</b> Un gestor de activos grande logra que una masa "
              "crítica de AUM migre a índices propios o gratuitos, rompiendo el lock-in de «estándar de facto» "
              "del que depende Indices.",
         "Crecimiento de AUM en productos vinculados a S&amp;P/DJI por debajo del crecimiento total de AUM "
         "pasivo del mercado, o compresión de la tasa efectiva de fee de Indices más rápida que el crecimiento "
         "de AUM.",
         "Trazable en cada 10-K/10-Q, vigilar 2-4 años."],
        ["4", "<b>Sustitución de Market Intelligence por herramientas nativas de IA.</b> La propia compañía ya "
              "declara este riesgo por escrito — un producto basado en LLM sustituye de forma material la "
              "suscripción a terminales tipo Capital IQ.",
         "Crecimiento orgánico o tasa de retención/renovación de Market Intelligence deteriorándose de forma "
         "sostenida frente a Ratings/Indices.",
         "Próximos 4-8 trimestres, dado el ritmo de adopción de herramientas de IA en el sector."],
        ["5", "<b>Mala asignación de capital vía M&amp;A acumulativo sin candado de ROIC.</b> El patrón de "
              "adquisiciones pequeñas «no materiales» se acumula sin que el paquete de incentivos (sección 8) "
              "capture el riesgo, repitiendo en pequeña escala el patrón de la fusión IHS Markit.",
         "Aparición de un cargo de impairment de goodwill (actualmente cero) o ROIC volviendo a caer de forma "
         "sostenida tras una adquisición grande.",
         "Continua, revisar en cada 10-K anual."],
        ["6", "<b>Contaminación cíclica del crecimiento orgánico reportado.</b> El 6%-9% de 2025 que ancla la "
              "fase temprana del DCF puede estar compuesto, en fracción no cuantificada, por el ciclo de "
              "emisión de deuda y la apreciación de mercado en el AUM de Indices — no motor compuesto propio.",
         "Datos primarios de emisión de deuda (SIFMA/Refinitiv) mostrando deceleración a dígito simple bajo "
         "en 2026-2027, combinados con AUM ligado a S&amp;P/DJI decelerando en un año de mercado plano. Si "
         "ambos ocurren a la vez, la fase de fade del caso base debe recalcularse con una tasa de arranque "
         "más baja.",
         "2026-2027, revisable en cada trimestre con datos de emisión disponibles."]],
        [0.6*cm, 5.1*cm, 6.9*cm, 3.6*cm], font_sz=7.2)]
    return o + [PageBreak()]
