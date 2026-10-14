# -*- coding: utf-8 -*-
"""2 · El foso en profundidad · 3 · Scuttlebutt · 4 · El motor de crecimiento"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, S, C, cm
from reportlab.platypus import Spacer, PageBreak


def foso():
    o = flag_titulo("2 · El foso en profundidad",
                    "Un mecanismo con cuatro patas, ya probado en tribunales — y una quinta pregunta que este documento no cierra")
    o += [p("El mecanismo del moat de Mastercard no es un dato aislado como “buen ROIC” — el buen ROIC es el "
        "síntoma. El mecanismo, descrito literalmente, tiene cuatro componentes:")]
    o += [tabla([
        ["MECANISMO", "CÓMO OPERA"],
        ["<b>Efecto de red bilateral con umbral de aceptación</b>",
         "Más comercios que aceptan la tarjeta hacen más atractivo emitirla o llevarla; más tarjetahabientes hacen "
         "más atractivo aceptarla. Ningún participante individual puede replicar unilateralmente la aceptación en "
         "más de 200 países — tendría que convencer, al mismo tiempo, a millones de comercios y miles de bancos."],
        ["<b>Coste de cambio técnico real</b>",
         "Integrar un banco emisor con autorización, tokenización, liquidación, disputas y cumplimiento normativo "
         "(EMV, PCI-DSS) es del mismo orden de magnitud que atarse a un proveedor de <i>core-banking</i>: migrar "
         "exige re-certificar productos enteros y re-emitir rangos BIN (los números que identifican al banco "
         "emisor en cada tarjeta)."],
        ["<b>Escala compartida en datos de fraude</b>",
         "Cada emisor adicional que se conecta mejora la señal de detección de fraude (Decision Intelligence) "
         "para todos los demás participantes de la red — un efecto de red que ningún competidor pequeño puede "
         "igualar por diseño."],
        ["<b>Marca + regulación que consolida, no destruye, el duopolio</b>",
         "Paradójicamente, la atención regulatoria sobre Visa y Mastercard ha tendido, en la práctica, a reforzar "
         "su posición conjunta frente a terceros en lugar de abrir el mercado a nuevos entrantes de tarjeta."]],
        [5.0*cm, 11.6*cm], font_sz=8.6)]
    o += [p("<b>El test de Sleep: ¿el ahorro de escala va al cliente, a la empresa, o se lo come un competidor?</b> "
        "En Mastercard, va a la empresa, y lo nuevo del 8-sep lo reconfirma sin matices. La tasa de intercambio "
        "combinada de Visa y Mastercard en Estados Unidos subió de 2,02% (2010) a 2,36% (2025), con los "
        "<i>network fees</i> creciendo aproximadamente un 30% más rápido que el valor transaccionado en los "
        "últimos cinco años (HECHO, litigio de comerciantes, resumido por Payments Dive/CardTraq 2026). El margen "
        "operativo GAAP de Mastercard se expandió de 53,4% (2021) a 57,6% (2025) — y <b>siguió subiendo hasta "
        "60,2% en Q2 2026</b> (HECHO, earnings release 2Q26 cruzado con GuruFocus).")]
    o += [chart("charts/07_margen_operativo_actualizado.png")]
    o += [callout("LA TRAMPA",
        "Bajo el marco de Sleep, un margen que se expande porque la escala no se comparte con el cliente <b>no es "
        "una señal de fortaleza pura</b> — es una invitación a la disrupción por rieles más baratos. Eso es "
        "exactamente lo que están intentando UPI en India, Pix en Brasil, y ahora <b>Wero en Europa</b> (ver "
        "abajo), y es lo que motivó que la Financial Conduct Authority del Reino Unido abriera, el 6 de mayo de "
        "2026, una investigación de competencia contra Mastercard y Visa (HECHO, PYMNTS.com). El mismo número que "
        "hace atractivo el negocio hoy es el que alimenta el riesgo regulatorio de mañana — ver Sección 11 y "
        "Sección 12.")]
    o += [p("<b>El episodio histórico real que este moat ya sobrevivió.</b> En <i>United States v. Visa U.S.A., "
        "Inc. and MasterCard International Inc.</i>, el Departamento de Justicia de EE.UU. demandó a ambas redes "
        "por una regla de exclusividad que prohibía a los bancos miembros emitir tarjetas de American Express o "
        "Discover al mismo tiempo que Visa o Mastercard. El fallo, contrario a Visa y Mastercard, llegó el "
        "<b>9 de octubre de 2001</b> (jueza Barbara Jones, Tribunal del Distrito Sur de Nueva York); el Segundo "
        "Circuito lo confirmó en 2003; la Corte Suprema denegó el certiorari el <b>4 de octubre de 2004</b> (HECHO: "
        "Washington Post, 4-oct-2004; Justia, 163 F. Supp. 2d 322). Citibank anunció en diciembre de 2004 que "
        "empezaría a emitir tarjetas American Express (HECHO: 8-K de American Express, dic-2004).")]
    o += [p("<b>El desenlace, dos décadas después, es la lección que importa.</b> Cuando se quitó el único candado "
        "<i>legal</i> que protegía la exclusividad de Visa y Mastercard, el mercado casi no se movió: en 2025, "
        "veinte años después, Visa y Mastercard seguían controlando conjuntamente más del 80% del volumen de "
        "tarjetas de crédito en Estados Unidos (HECHO: Payments Dive/CardTraq 2026). El motor real de su posición "
        "nunca fue la regla de exclusividad — fue la escala de red ya acumulada, que ninguna sentencia judicial "
        "puede desarmar de un plumazo.")]
    o += [p("<b>Contraste con el ritmo real de crecimiento.</b> Duplicar el negocio en diez años exige un 7,2% de "
        "crecimiento anual compuesto (CAGR). El CAGR real 2022→2025 fue de aproximadamente 13,8% (2023→2025: "
        "~14,3%), con una guía de gerencia para FY2026 de “el extremo alto de un dígito doble bajo” (~11-12%) "
        "(HECHO: 8-K FY2025; transcript Q2 2026). El caso base de “duplicar en diez años” es, si acaso, "
        "conservador frente al ritmo reciente — pero ese ritmo está inflado por la normalización post-pandemia del "
        "volumen transfronterizo, la inflación nominal de 2022-2023, y aproximadamente 3 puntos porcentuales de "
        "crecimiento inorgánico vía la adquisición de Recorded Future dentro del segmento de Servicios de Valor "
        "Añadido (VAS).")]
    o += [callout("PAUSA REFLEXIVA",
        "El mecanismo descrito arriba responde bien al ataque histórico de <i>switching</i> de marca dentro del "
        "modelo de cuatro partes (2001-2004; y su repetición reciente, Capital One/Discover). Pero <b>no nombra ni "
        "cuantifica</b> el vector de sustitución tecnológica cuenta-a-cuenta (A2A) patrocinado por bancos centrales "
        "—Pix, UPI, SEPA Instant—, que es un régimen de rieles paralelo y gratuito, no un competidor dentro del "
        "mismo modelo de cuatro partes. Éste es un hueco real del mecanismo, no cerrado por la evidencia "
        "disponible: se convierte en un mecanismo de pre-mortem explícito y falsable en la Sección 9 (mecanismo "
        "#5), añadido después de que el abogado del diablo lo señalara en el Paso 10 — ver Sección 14.")]
    o += [p("<b>Lo nuevo del 8-sep hace este hueco más concreto, no más abstracto.</b> Wero —el rail de pagos "
        "cuenta-a-cuenta de la European Payments Initiative— resolvió en la práctica el problema de arranque de "
        "dos lados que hasta ahora protegía a Mastercard: los ~14 bancos fundadores de Wero (BNP Paribas, "
        "Deutsche Bank, ING, Santander, entre otros) son los mismos emisores de tarjetas Visa y Mastercard en "
        "esos países (HECHO). El checkout de comercio electrónico con Wero ya está vivo en Alemania (nov-2025) y "
        "Francia/Bélgica (ene-2026), con ~50 millones de usuarios y más de 1.100 entidades financieras "
        "integradas; el pago sin contacto (NFC) en tienda física está previsto para 2026-2027. Es el mismo "
        "mecanismo #5 ya fichado el 4-sep — pero con un reloj europeo que ya está corriendo, no un riesgo lejano "
        "en Brasil o India.")]
    return o + [PageBreak()]


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
    o += [p("<b>Lo que el 8-sep añade a este cuadro no son palabras, es un juzgado.</b> El 9 de junio de 2026, "
        "el juez Brian Cogan (Distrito Este de Nueva York) calificó de <i>“fair, reasonable, and adequate”</i> el "
        "acuerdo enmendado de interchange en EE.UU. —aprobación judicial PRELIMINAR, no definitiva (HECHO: "
        "Payments Dive, PYMNTS)—. Los términos: -10 puntos básicos en la tasa de intercambio combinada durante "
        "5 años, y un tope de 125 puntos básicos en tarjetas de consumo estándar durante 8 años. Es la primera "
        "vez en dos décadas de litigio que un regulador o un tribunal logra poner una cifra y una fecha concretas "
        "sobre la mesa — no retórica, un número. Toca la renta del banco emisor (interchange), no la cuota de "
        "red propia de Mastercard, y todavía enfrenta apelaciones (resolución completa no antes de ~2029) — pero "
        "el precedente de que “esta vez sí hay un número” cambia la conversación de la Sección 9.")]
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
        "tres años (aceleró de 38,5% a 40,6% en el último año, con VAS creciendo 22,9% interanual, "
        "13.320 M US$), creciendo a tasas aproximadamente el doble que el negocio de red “puro” (HECHO, 10-K "
        "FY2025, Nota Revenue Disaggregation R61.htm)— no de capital nuevo desplegado.")]
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
        ["Regulación", "<b>El limitante más concreto y con evidencia activa</b> — topes de interchange (ahora con "
         "una cifra judicial preliminar: -10pb/5a), la CCCA en el Congreso de EE.UU., la investigación de la "
         "FCA, el litigio en el Reino Unido, y ahora Wero en Europa. Ver Sección 9."]],
        [3.2*cm, 13.4*cm], font_sz=8.5)]
    o += [p("<b>Años de pista (juicio propio de esta síntesis, INFERENCIA, no HECHO):</b> visiblemente entre "
        "5 y 8 años de runway claro, dado el momentum de VAS —que acelera, no se estabiliza— y la desaceleración "
        "ya guiada por la propia gerencia (de 15-16% hacia el “extremo alto de un dígito doble bajo”, ~11-12%), "
        "antes de una convergencia probable hacia tasas de crecimiento más bajas. La convergencia completa hacia "
        "un ritmo tipo-PIB tomaría entre 10 y 15 años en ausencia de disrupción — pero el riesgo regulatorio y de "
        "desintermediación (Sección 9), con Wero, la CCCA y el GENIUS Act convergiendo en 2027 según el abogado "
        "del diablo del 8-sep, podría comprimir esta ventana más rápido de lo que el caso base asume.")]
    o += [callout("LECCIÓN TRANSFERIBLE",
        "La primera versión de este documento trató la brecha de 5,3 puntos porcentuales como un dato neutro a "
        "explicar (“es mix y margen, no capital”), sin extraer la implicación obligada: un margen que ya se "
        "expandió 4,2 puntos porcentuales en cuatro años tiene un techo aritmético, y la propia guía de gerencia "
        "ya confirma la desaceleración que este motor predeciría si se tomara en serio. El abogado del diablo "
        "(Paso 10, ver Sección 13) señaló correctamente que esto era <b>confirmation bias</b> — ajustar la "
        "narrativa para que el marco siguiera teniendo razón, en vez de dejar que el dato cuestionara el marco. "
        "El falsador correspondiente (Sección 15) fijaba el umbral en 57,6% para el cierre de FY2026 completo. "
        "<b>El dato del 8-sep (60,2% en Q2 2026) ya lo supera</b> — DEGRADADO hasta el cierre real del año fiscal "
        "(feb-2027), pero es evidencia en contra de que el techo sea inminente, no a favor. La brecha entre g "
        "implícito y CAGR real de NOPAT sigue sin resolverse: puede que el motor clásico simplemente no aplique "
        "bien a este arquetipo de negocio, o puede que el margen tenga más recorrido del que el propio Paso 10 "
        "asumió. Ninguna de las dos lecturas está todavía confirmada — y esa misma incertidumbre es la que un "
        "abogado del diablo independiente usa el 8-sep para pedir un escalón de compresión en el DCF alrededor "
        "de 2027, no una línea plana a 10 años (ver Sección 13).")]
    return o + [PageBreak()]
