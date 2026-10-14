# -*- coding: utf-8 -*-
"""3 · Lo que dicen quienes lo rodean · 4 · El motor de crecimiento ·
5 · Gestión e incentivos · 6 · Los hechos que podrían romper la tesis"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, S, C, cm
from reportlab.platypus import Spacer, PageBreak


def scuttlebutt():
    o = flag_titulo("3 · Lo que dicen quienes lo rodean",
                    "Scuttlebutt: comparar lo que las empresas alrededor de Mastercard hacen con dinero real, no lo que dicen en las conference calls")
    o += [p("<b>Visa</b> — el comparador de modelo idéntico: ingresos de Q3 FY2026 +14%, volumen superior a "
        "4 billones de dólares por trimestre por primera vez en su historia, guía elevada (HECHO: 8-K de Visa, "
        "28-jul-2026). No hay señal de deserción de volumen hacia rieles alternativos en el comparable más "
        "cercano que existe.")]
    o += [p("<b>American Express</b> — el modelo cerrado (emite y presta a la vez): EPS de Q2 2026 +11%, "
        "<i>billed business</i> +9% —el ritmo más rápido en tres años—, guía de ingresos elevada al 10% "
        "(HECHO: 8-K de American Express, 24-jul-2026). Tampoco hay señal de <i>trade-down</i> hacia redes más "
        "baratas en el segmento premium.")]
    o += [p("<b>PayPal</b> — el disruptor histórico, el que llevaba una década prometiendo desintermediar a las "
        "redes de tarjeta: ingresos de Q2 2026 +5%, apenas un tercio del ritmo de Visa y American Express, con "
        "guía de Q3 débil tanto en ingresos como en beneficio por acción (HECHO: 8-K de PayPal, ago-2026). "
        "INFERENCIA: PayPal sigue dependiendo de los rieles de Visa y Mastercard para fondear sus billeteras "
        "digitales — no los ha reemplazado, y su propio crecimiento se desaceleró frente a las redes que "
        "supuestamente iba a desintermediar.")]
    o += [callout("DATO CURIOSO",
        "El 6 de mayo de 2026 la FCA británica abrió investigación contra Mastercard, Visa <b>y PayPal</b> a la "
        "vez, sobre priorización de opciones de pago en el checkout (HECHO: PYMNTS.com). En paralelo, grandes "
        "comerciantes —Walmart, la National Restaurant Association, Hugo Boss— objetaron formalmente en 2026 el "
        "acuerdo propuesto de interchange en EE.UU., alegando que otorga “demasiada inmunidad legal” "
        "(HECHO: Payments Dive 2026). Reguladores y comerciantes atacando de forma simultánea mientras el volumen "
        "sigue creciendo con fuerza es exactamente lo que predice el test de Sleep de la Sección 2: el moat es "
        "real, pero la falta de reparto del ahorro de escala genera fricción regulatoria acumulada.")]
    o += [p("<b>La señal más reveladora no está en las declaraciones públicas, sino en dónde ponen su dinero.</b> "
        "En junio de 2026, Visa y Mastercard se unieron a Stripe, Coinbase y aproximadamente 140 firmas más para "
        "lanzar el consorcio de stablecoins “Open USD” (HECHO: Payments Dive/Matterfact, jul-2026) — mientras "
        "públicamente ambas redes “restan importancia” al riesgo que las stablecoins representan para su modelo. "
        "INFERENCIA: cubrirse internamente con participación directa en el consorcio es una señal de percepción "
        "de riesgo más fidedigna que la retórica minimizadora en las conference calls — cuando el management "
        "invierte tiempo y capital en cubrirse de algo, es porque no está tan seguro de que no vaya a importar.")]
    return o + [PageBreak()]


def motor_crecimiento():
    o = flag_titulo("4 · El motor de crecimiento",
                    "g = tasa de reinversión × ROIC incremental — y por qué esta fórmula, aplicada literalmente, no explica todo lo que ha pasado")
    o += [p("El método exige reconstruir el motor de crecimiento desde los datos crudos, no aceptar el "
        "crecimiento reportado como una caja negra. Ninguno de los tres dossiers de investigación entregó este "
        "cálculo ya resuelto — se reconstruye aquí desde cero contra los estados financieros de cada 10-K:")]
    o += [tabla([
        ["AÑO<br/>FISCAL", "CAPEX DE<br/>CRECIMIENTO", "M&amp;A NETA<br/>(CAJA)", "REINVERSIÓN<br/>TOTAL", "NOPAT", "TASA DE<br/>REINVERSIÓN", "ROIC"],
        ["2021", "105 M US$", "4.436 M US$", "4.541 M US$", "8.499 M US$", "53,4%", "61,1%"],
        ["2022", "106 M US$", "313 M US$", "419 M US$", "10.375 M US$", "4,0%", "76,7%"],
        ["2023", "29 M US$", "0 US$", "29 M US$", "11.500 M US$", "0,3%", "80,9%"],
        ["2024", "100 M US$", "2.511 M US$", "2.611 M US$", "13.151 M US$", "19,9%", "79,9%"],
        ["2025", "106 M US$", "0 US$", "106 M US$", "15.231 M US$", "0,7%", "93,3%"]],
        [1.95*cm, 2.7*cm, 2.55*cm, 2.6*cm, 2.15*cm, 2.6*cm, 1.75*cm], font_sz=7.8)]
    o += [chart("charts/04_motor_reinversion.png")]
    o += [p("<b>Tasa de reinversión promedio ponderada (5 años): 7.706 M US$ / 58.756 M US$ ≈ 13,1%</b>, "
        "extremadamente irregular año a año (0,3%-53,4%), dominada por operaciones de M&amp;A discretas y no por "
        "un flujo de capex suave y predecible. <b>ROIC promedio simple: ~78,4%</b> (rango 61,1%-93,3%). "
        "<b>g implícito (reinversión × ROIC): 0,131 × 0,784 ≈ 10,3%.</b>")]
    o += [callout("LA TRAMPA",
        "<b>Hallazgo central de esta sección, y no trivial:</b> el CAGR real del NOPAT 2021-2025 fue de "
        "aproximadamente 15,6%-15,7% — supera el g implícito del motor por 5,3 puntos porcentuales. Aplicado "
        "literalmente, el motor g = reinversión × ROIC <b>infra-explica</b> el crecimiento real de Mastercard. "
        "La brecha proviene de expansión de margen y cambio de mix —VAS pasó de 37,0% a 40,6% del ingreso en "
        "tres años, creciendo a tasas aproximadamente el doble que el negocio de red “puro” (HECHO, 10-K FY2025, "
        "Nota Revenue Disaggregation R61.htm)— no de capital nuevo desplegado.")]
    o += [p("Esto es atípico frente al arquetipo de negocio para el que este motor fue diseñado —compounders "
        "intensivos en capital, tipo minorista que abre tiendas nuevas—: el crecimiento de Mastercard es "
        "mayoritariamente <b>apalancamiento operativo sobre una red cuyo coste marginal de servir una transacción "
        "adicional es casi cero</b>, financiado por retención de NOPAT que no se “reinvierte” en el sentido "
        "clásico — fluye hacia recompras de acciones, que casi se duplicaron de 2.000 M US$/trimestre en Q1 2024 "
        "a 4.900 M US$/trimestre en Q2 2026 (HECHO: transcript), amplificando el crecimiento por acción más allá "
        "del crecimiento del negocio subyacente.")]
    o += [p("<b>Anclaje contra tasa base.</b> Chan, Karceski y Lakonishok (2003, <i>Journal of Finance</i>) "
        "encontraron que el crecimiento de beneficios no persiste por encima del azar en el universo general no "
        "filtrado de empresas cotizadas entre 1951 y 1998 (una racha de cinco años: 3,0% observado frente a 3,1% "
        "esperado bajo independencia estadística). Mastercard lleva cinco años consecutivos de crecimiento de "
        "ingreso neto GAAP de doble dígito y NOPAT ~15,6% anual — una magnitud muy por encima de lo típico. Pero "
        "el hallazgo de Chan-Karceski-Lakonishok es sobre <b>persistencia</b>, no sobre magnitud: la racha pasada, "
        "por sí sola, no predice la próxima década mejor que el azar en el universo general de empresas. Lo que sí "
        "puede sostener persistencia por encima de ese prior es el mecanismo del moat (Sección 2) — no la "
        "extrapolación mecánica de la tendencia.")]
    o += [chart("charts/05_crecimiento_trayectoria.png")]
    o += [p("<b>Qué limita el crecimiento, punto por punto:</b>")]
    o += [tabla([
        ["FACTOR", "¿ES UN LÍMITE REAL?"],
        ["Capital desplegable", "No. El capex orgánico es apenas 1,5%-2,2% del ingreso; el flujo de caja libre "
         "genera holgura amplia. Mastercard podría desplegar mucho más capital si quisiera — el limitante no es "
         "financiero."],
        ["Techo de demanda", "<b>Sí — el limitante real.</b> El GDV global (10,6 billones de US$ en 2025) y el "
         "ritmo de conversión de efectivo a tarjeta en mercados emergentes. Llegar a ~77.000 M US$ de ingreso en "
         "2035 bajo la curva del caso base implicaría un GDV cercano a 25 billones de US$ — sin verificación "
         "externa del TAM global proyectado a 2035 (hueco declarado, presupuesto de búsqueda del dossier de "
         "valoración agotado en este punto)."],
        ["Talento", "No es un limitante vinculante para un negocio de red — la operación no depende de "
         "contratar a gran escala."],
        ["Regulación", "<b>El limitante más concreto y con evidencia activa</b> — topes de interchange, la CCCA "
         "en el Congreso de EE.UU., la investigación de la FCA, el litigio en el Reino Unido. Ver Sección 11."]],
        [3.2*cm, 13.4*cm], font_sz=8.5)]
    o += [p("<b>Años de pista (juicio propio de esta síntesis, INFERENCIA, no HECHO):</b> visiblemente entre "
        "5 y 8 años de runway claro, dado el momentum de VAS y la desaceleración ya guiada por la propia gerencia "
        "(de 15-16% hacia el “extremo alto de un dígito doble bajo”, ~11-12%), antes de una convergencia probable "
        "hacia tasas de crecimiento más bajas. La convergencia completa hacia un ritmo tipo-PIB tomaría entre 10 "
        "y 15 años en ausencia de disrupción — pero el riesgo regulatorio y de desintermediación (Sección 11) "
        "podría comprimir esta ventana más rápido de lo que el caso base asume.")]
    o += [callout("LECCIÓN TRANSFERIBLE",
        "La primera versión de este documento trató la brecha de 5,3 puntos porcentuales como un dato neutro a "
        "explicar (“es mix y margen, no capital”), sin extraer la implicación obligada: un margen que ya se "
        "expandió 4,2 puntos porcentuales en cuatro años tiene un techo aritmético, y la propia guía de gerencia "
        "ya confirma la desaceleración que este motor predeciría si se tomara en serio. El abogado del diablo "
        "(Paso 10, ver Sección 13) señaló correctamente que esto era <b>confirmation bias</b> — ajustar la "
        "narrativa para que el marco siguiera teniendo razón, en vez de dejar que el dato cuestionara el marco. "
        "Se corrige aquí y se convierte en falsador explícito en la Sección 15: si el margen operativo GAAP de "
        "FY2026 no supera el 57,6% ya alcanzado en FY2025, la “g excedente” desaparece por definición aritmética "
        "y el motor de reinversión —g≈10,3%— pasa a ser el techo real de crecimiento, no un piso conservador.")]
    return o + [PageBreak()]


def gestion():
    o = flag_titulo("5 · Gestión e incentivos",
                    "Leer la compensación y los Forms 4 como texto, no como relaciones públicas")
    o += [p("<b>Quién manda:</b> Michael Miebach, CEO desde enero de 2021 (HECHO: DEF 14A 2026, 27-abr-2026). "
        "Su compensación total en FY2025 fue de aproximadamente 35,4 M US$ (INFERENCIA — DEGRADADA, proviene de "
        "una fuente secundaria que resume la tabla de compensación (<i>Summary Compensation Table</i>), no "
        "verificada línea por línea contra el propio DEF 14A).")]
    o += [p("<b>Qué mide realmente la compensación.</b> El bono anual pagó 145% del objetivo en 2025, según el "
        "“corporate score”. Las PSU (unidades de acciones por desempeño) del ciclo 2025-2027 — 60% del "
        "incentivo de largo plazo (LTI) — se miden con tres métricas de un año (crecimiento de ingresos netos "
        "ajustado, EPS ajustado, ponderadas por igual), promediadas sobre el trienio, más un modificador de "
        "rentabilidad total al accionista (TSR) relativo frente al S&amp;P 500. El ciclo PSU 2023-2025 pagó 131,8% "
        "del objetivo (HECHO: DEF 14A 2026).")]
    o += [callout("LA METÁFORA",
        "Mastercard no le paga a su plana ejecutiva por la calidad de la red, ni por la satisfacción del comercio, "
        "ni por un ROIC explícito — le paga casi exclusivamente por crecimiento de ingresos, EPS y retorno "
        "relativo al índice. Es como pagarle a un piloto de avión sólo por la velocidad a la que llega, sin medir "
        "nunca si el aterrizaje fue seguro. Esto es exactamente coherente con el test de Sleep de la Sección 2: "
        "el sistema de incentivos empuja a maximizar el ritmo de crecimiento del ingreso, no a compartir las "
        "economías de escala con emisores y comercios — y eso alimenta, con el tiempo, la fricción regulatoria "
        "que hoy es uno de los mecanismos centrales del pre-mortem (Sección 11).")]
    o += [p("Dos ciclos consecutivos pagando más del 130% del objetivo es compatible tanto con un desempeño "
        "genuinamente excepcional como con metas conservadoras fijadas por el comité de compensación — es una "
        "señal de gobierno corporativo a vigilar, no una acusación. Existen políticas de <i>ownership "
        "guidelines</i>, período de retención posterior al <i>vesting</i>, prohibición de cobertura (<i>hedging</i>) "
        "y de pignoración (<i>pledging</i>) de acciones, y cláusulas de <i>clawback</i> (HECHO: DEF 14A 2026), "
        "pero los umbrales exactos de estas políticas están DEGRADADOS — pendientes de una lectura directa de las "
        "páginas 67-73 y 83 del propio documento.")]
    o += [p("<b>Quién compra y quién vende con dinero propio.</b> Una revisión de los Forms 4 presentados entre "
        "julio y septiembre de 2026 encontró que <b>todas</b> las transacciones de insiders detectadas fueron "
        "ventas bajo planes 10b5-1 preestablecidos (planes de venta programados con anticipación, diseñados para "
        "evitar acusaciones de uso de información privilegiada) — Miebach (tres ventas en agosto de 2026, a "
        "precios crecientes de 567 a 580 US$), Mehra (Chief Business Officer), Kirkpatrick y McLaughlin "
        "(HECHO: Forms 4, EDGAR).")]
    o += [callout("PAUSA REFLEXIVA",
        "<b>No se encontró ninguna compra en mercado abierto con dinero propio en 2025-2026.</b> En una mega-cap "
        "madura, la venta programada es diversificación racional del patrimonio personal, no necesariamente una "
        "señal bajista — los ejecutivos de la mayoría de las grandes compañías venden así. Pero la combinación de "
        "(a) cero compras discrecionales por parte de la cúpula ejecutiva y (b) una compensación que paga "
        "sistemáticamente entre 1,3 y 1,45 veces el objetivo es un patrón a vigilar, no a ignorar. El Filtro "
        "Munger de la Sección 14 vuelve sobre este punto: unos incentivos 100% orientados a crecimiento, sin "
        "métrica explícita de ROIC ni disciplina de capital, y cero compras con dinero propio.")]
    return o + [PageBreak()]


def knockouts():
    o = flag_titulo("6 · Los hechos que podrían romper la tesis",
                    "Los seis knock-outs binarios del método, re-verificados de forma independiente contra fuente primaria")
    o += [p("El catálogo de knock-outs es fijo y se aplica sobre el Dossier de Hechos, corregido aquí con las dos "
        "citas que la verificación adversarial encontró inexactas. En ningún caso cambia el veredicto del "
        "knock-out — pero el método no acepta una cita {documento, sección, fecha} que en realidad no dice lo que "
        "afirma decir, así que la evidencia sí se corrige donde hacía falta.")]
    o += [tabla([
        ["KNOCK-OUT", "RESULTADO", "EVIDENCIA Y MATIZ"],
        ["(a) Estructura VIE",
         "NO SE DISPARA",
         "Existe una política de consolidación de VIEs explícita en la Nota 1 de los 10-K FY2023 y FY2025: "
         "<i>“no había VIEs significativas que requirieran consolidación”</i> al 31-dic-2025 y 2024 "
         "(HECHO, accn 0001141391-26-000013 y 0001141391-24-000022, texto íntegro verificado contra EDGAR). "
         "La búsqueda original no había capturado este boilerplate — corregido aquí; el knock-out sigue sin "
         "dispararse, por la razón correcta."],
        ["(b) SBC &gt; 50% del FCF ajustado ≥3 años",
         "NO SE DISPARA",
         "SBC/FCF osciló entre 2,7% y 4,0% en FY2021-2025, verificado de forma independiente por dos "
         "reconstrucciones distintas desde XBRL crudo. Muy lejos del umbral."],
        ["(c) ROIC &lt; WACC estructural ≥3 años",
         "NO SE DISPARA, sin ambigüedad",
         "ROIC 61,1%-93,3% en los cinco años (cálculo propio reconstruido dos veces desde cero, coincide al "
         "millón) frente a un WACC bottom-up de 7,5%-8,0% (Sección 12) — un margen de 8x a 12x. No hay lectura "
         "razonable bajo la que este knock-out se acerque a dispararse."],
        ["(d) Restatement de ingresos",
         "NO SE DISPARA, pero la afirmación original era falsa",
         "El dossier original decía “no se encontró evidencia de restatement” — inexacto. El 10-K FY2023 tiene "
         "el flag iXBRL de portada <i>DocumentFinStmtErrorCorrectionFlag = TRUE</i> (HECHO, verificado contra el "
         "10-K real). Corresponde a una corrección inmaterial de la exposición estimada de liquidación "
         "(<i>settlement exposure</i>) al 31-dic-2022, sin impacto en ninguna partida de los estados financieros; "
         "el flag vuelve a FALSE en FY2024 y FY2025. No hubo restatement material de ingresos, utilidad, activos "
         "o patrimonio."],
        ["(e) Dependencia de cliente/regulador único",
         "NO SE DISPARA como knock-out estricto",
         "Un solo segmento reportable; EE.UU. representa 29-30% del ingreso, sin nota de concentración de "
         "cliente bajo ASC 280 (HECHO, 10-K FY2025, Nota Segment Reporting R117.htm). Matiz para la Sección 11: "
         "exposición difusa a decenas de regímenes de interchange simultáneos, no a un cliente o regulador "
         "único."],
        ["(f) Deuda tóxica",
         "NO SE DISPARA, pero “enteramente Senior Notes” era una sobre-generalización",
         "La deuda es predominantemente Senior Notes no garantizadas de tasa fija (1,00%-4,95%), más una "
         "porción menor de deuda local india (INR Term Loan, abr-2023, ~342 M US$) que el dossier original "
         "omitió. Deuda/EBITDA &lt;1,3x en los cinco años; calificación Aa3 (Moody's) / A+ (S&amp;P), ambas "
         "estables, confirmadas en un FWP de bonos del 4-jun-2026 (accn 0001193125-26-257761)."]],
        [3.6*cm, 2.9*cm, 9.5*cm], font_sz=7.7)]
    o += [callout("DATO CURIOSO",
        "Nota adicional no catalogada, material para la Sección 5 (Gestión): la cola de litigio de interchange "
        "es más extensa de lo que el dossier original había capturado. Además del caso principal en el Reino "
        "Unido (~13.000 M US$), existe un <b>segundo caso separado en el Reino Unido</b> (~1.300 M US$), más "
        "Portugal (500 M US$), Países Bajos (400 M US$), ATM Operators (~1.000 M US$) y U.S. Liability Shift "
        "Litigation (~1.000 M US$) — exposición combinada declarada de ~17.200 M US$ (HECHO, 10-K FY2025, "
        "Nota Legal and Regulatory Proceedings R111.htm). La reserva acumulada de litigio en libros es de "
        "apenas ~800 M US$; los pagos de acuerdos legales fueron de 647 M US$ (2025), 496 M US$ (2024) y "
        "929 M US$ (2023).")]
    o += [p("<b>Conclusión de esta sección:</b> los seis knock-outs binarios del catálogo fijo no se disparan. "
        "La evidencia fue re-verificada de forma independiente por dos investigadores distintos, con cifras "
        "reconstruidas desde cero contra XBRL crudo y contra el texto íntegro real de los 10-K —no solo el "
        "índice de notas—, así que el nivel de trazabilidad es alto. Dos de las seis citas originales contenían "
        "errores de redacción reales, ya corregidos arriba. El negocio subyacente pasa este filtro sin "
        "ambigüedad; lo que este documento discute a partir de aquí no es si el negocio está sano, sino si el "
        "precio de hoy compensa el riesgo que sí existe.")]
    return o + [PageBreak()]
