# -*- coding: utf-8 -*-
"""Portada · Resumen en treinta segundos · Aviso de estado · El negocio · El foso"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, kpi_panel, S, C, cm
from reportlab.platypus import Spacer, PageBreak, NextPageTemplate, Paragraph, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER


def portada():
    t_emp = ParagraphStyle("te", fontName="Serif-B", fontSize=36, leading=40, textColor=C["tinta"])
    t_tag = ParagraphStyle("tg", fontName="Serif-I", fontSize=13.2, leading=18.5, textColor=C["gris"])
    t_sec = ParagraphStyle("ts", fontName="Sans-B", fontSize=9, leading=12, textColor=C["rojo"])
    return [
        Spacer(1, 4.6*cm),
        Paragraph("REDES DE PAGO · INFRAESTRUCTURA FINANCIERA GLOBAL", t_sec),
        Spacer(1, 10),
        Paragraph("Mastercard Incorporated", t_emp),
        Paragraph("NYSE: MA", ParagraphStyle("tk", fontName="Sans-B", fontSize=11, leading=15,
                                             textColor=C["azul_noche"], spaceBefore=4)),
        Spacer(1, 8),
        Paragraph("No presta, no arriesga, no vende nada que se toque.", t_tag),
        Spacer(1, 3),
        Paragraph("Cobra un peaje diminuto cada vez que dos desconocidos que nunca se hablan "
                  "—un banco emisor y un comercio— necesitan confiar el uno en el otro sin conocerse.", t_tag),
        Spacer(1, 1.0*cm),
        kpi_panel([("580,98 US$", "PRECIO VIVO", "IBKR MCP, 4-sep-2026,<br/>cruzado con stockanalysis.com"),
                   ("590-730 US$", "VALOR INTRÍNSECO (caso base)", "piso de resolución del DCF<br/>explícito a 10 años, Paso 9"),
                   ("NO COMPRAR<br/>TODAVÍA", "VEREDICTO", "mantenido tras el veto del<br/>abogado del diablo, Paso 10-11")]),
        Spacer(1, 0.7*cm),
        tabla([["FECHA", "PRECIO (dato vivo)", "VEREDICTO", "HORIZONTE"],
               ["4 de septiembre de 2026", "580,98 US$", "NO COMPRAR TODAVÍA",
                "Largo plazo — condicionado al Paso 11"]],
              [4.15*cm]*4, font_sz=8.8),
        Spacer(1, 0.45*cm),
        M.p("<font size=8.2 color='#666054'><i>Construido con el método QG de 12 pasos, "
            "“Comprensión Primero con candado adversarial” (refundación 2026-07-19): monólogo evidenciado, "
            "nunca un score. Incluye el veto de abogado del diablo en sesión limpia (Candado A, ya ejecutado) "
            "y un WACC calculado siempre bottom-up de mercado, nunca heredado de un tier de calidad (Candado B). "
            "Documento de trabajo personal — no es asesoramiento de inversión registrado.</i></font>"),
        Spacer(1, 0.25*cm),
        M.p("<font size=7.8 color='#8C1410'><i><b>Veredicto PROVISIONAL:</b> pendiente de que Felipe complete "
            "personalmente los Pasos 0, 1 y 7 antes de considerarlo definitivo. Ver Aviso de estado, página siguiente.</i></font>"),
        NextPageTemplate("Normal"), PageBreak()]


def resumen():
    o = flag_titulo("El resumen en treinta segundos", "Si sólo lees una página, que sea ésta")
    o += [p("<b>El veredicto es NO COMPRAR TODAVÍA — y el veto del abogado del diablo, ejecutado en sesión limpia, "
        "lo endureció en vez de moverlo.</b> No porque el negocio esté roto: los seis knock-outs binarios del "
        "método están limpios con margen amplio, el ROIC se mueve entre 61,1% y 93,3% frente a un coste de capital "
        "de 7,5%-8,0% —un colchón de 8 a 12 veces—, y el test de trampa de valor es negativo en los nueve últimos "
        "trimestres revisados. Mastercard es, con los números en la mano, un negocio extraordinario.")]
    o += [p("<b>El problema no es la calidad del negocio: es que el precio no compensa el riesgo de cola que el "
        "propio análisis, hasta hace poco, ni siquiera intentaba medir.</b> El motor de reinversión (g = tasa de "
        "reinversión × ROIC incremental) sólo explica un g del 10,3% — pero el crecimiento real del beneficio "
        "operativo neto (NOPAT) fue de 15,6%-15,7% anual entre 2021 y 2025. Esa brecha de 5,3 puntos porcentuales "
        "no viene de más capital invertido: viene de que el margen operativo GAAP se expandió de 53,4% a 57,6% en "
        "cuatro años, un movimiento que tiene, por definición aritmética, un techo. La guía de la propia gerencia "
        "para 2026 —“el extremo alto de un dígito doble bajo”, ~11-12%— ya apunta hacia ese techo, no hacia el "
        "15,6% histórico.")]
    o += [p("Y hay una cola de riesgo que, hasta el veto del Paso 10, no estaba en ningún número. La exposición "
        "combinada del litigio de interchange —el caso principal en el Reino Unido más otros cinco procesos— suma "
        "aproximadamente 17.200 millones de dólares, frente a una reserva contable de apenas ~800 millones. La "
        "Financial Conduct Authority británica abrió el 6 de mayo de 2026 una investigación de competencia contra "
        "Mastercard, Visa y PayPal a la vez. El caso bajista que este documento manejaba —una simple compresión de "
        "múltiplo, sin tocar el margen— no incorporaba ninguna de las dos cosas. Por eso ese caso bajista, y la "
        "razón “5:1” que se apoyaba en él, quedan retirados como argumento hasta que se recalculen formalmente.")]
    o += [p("<b>El beta que ancla el coste de capital tampoco está cerrado.</b> Tres fuentes convergen en 0,74-0,76 "
        "—y ese número coincide, casi al dígito, con el de Visa, el comparable de negocio más parecido que existe— "
        "pero dos outliers (0,58 y 0,82) no están reconciliados con una regresión propia. Si el beta real hacia "
        "adelante es más alto que el triangulado, el WACC sube y el rango de valor intrínseco (590-730 US$) se "
        "desplaza hacia abajo, potencialmente por debajo del precio de hoy (580,98 US$). El propio dossier de "
        "valoración lo resume mejor que cualquier síntesis: <i>“MA no está claramente barata ni claramente "
        "cara”</i>.")]
    o += [callout("EN ROMÁN PALADINO",
        "La pregunta que decide este documento no es “¿puede Mastercard duplicar su tamaño en diez años?” "
        "—probablemente sí, si nada se rompe—. La pregunta real, la que el Paso 3 deja abierta para el Paso 8, es: "
        "<b>“¿qué tendría que romperse para que el crecimiento caiga a la mitad de su ritmo reciente, y aun así "
        "el caso base sobreviva?”</b> Este documento no tiene todavía una respuesta cerrada — y mientras no la "
        "tenga, pagar el precio de hoy es apostar a que la respuesta es “nada”.")]
    o += [hr(), p("<b>Las cifras que hay que retener:</b>")]
    o += [tabla([
        ["LA CIFRA", "QUÉ SIGNIFICA"],
        ["<b>8x a 12x</b>",
         "El margen entre el ROIC (61,1%-93,3% en los últimos cinco años) y el WACC bottom-up (7,5%-8,0%). "
         "Bajo cualquier lectura razonable, este knock-out no se acerca a dispararse — el negocio no está en duda."],
        ["<b>10,3% frente a 15,6%-15,7%</b>",
         "El g que predice el motor clásico de reinversión (g = reinversión × ROIC) frente al CAGR real del "
         "beneficio operativo neto 2021-2025. La brecha viene de expansión de margen, no de capital nuevo — "
         "y el margen tiene techo aritmético. El propio abogado del diablo señaló que tratar esto como neutro "
         "era autocomplacencia con el marco, no una explicación."],
        ["<b>17.200 M US$ frente a ~800 M US$</b>",
         "La exposición combinada declarada de la cola de litigio de interchange (Reino Unido, Portugal, Países "
         "Bajos, ATM Operators, U.S. Liability Shift) frente a la reserva acumulada en libros. El bear case "
         "original no metía este número en el P&amp;L — sólo en el múltiplo."],
        ["<b>0,74-0,76 frente a 0,58 / 0,82</b>",
         "El beta que ancla el WACC: tres fuentes convergen (incluida Visa, el comparable más cercano), pero dos "
         "outliers no están reconciliados con una regresión propia. Es la mayor fuente de incertidumbre del "
         "rango de valor intrínseco."],
        ["<b>590-730 US$ frente a 580,98 US$</b>",
         "El rango razonable de valor intrínseco (piso de resolución) frente al precio vivo del 4-sep-2026. "
         "El precio cae en el borde inferior del rango — ni claramente barato ni claramente caro."]],
        [4.1*cm, 12.5*cm], font_sz=8.6)]
    o += [callout("PAUSA REFLEXIVA",
        "Antes de seguir, una pregunta honesta: si el negocio subyacente está intacto —y lo está, con nueve de "
        "nueve trimestres de crecimiento orgánico de doble dígito— ¿por qué no comprar hoy mismo? Porque “el "
        "negocio es bueno” y “el precio de hoy me paga por el riesgo que corro” son dos preguntas distintas, "
        "y este documento existe precisamente para no dejar que la primera responda por la segunda. El veredicto "
        "de este documento sigue siendo, además, <b>provisional</b> — ver la página siguiente.")]
    return o + [PageBreak()]


def aviso_estado():
    o = flag_titulo("Aviso de estado del documento", "Por qué este veredicto todavía no es definitivo")
    o += [callout("PAUSA REFLEXIVA",
        "<b>Este es un veredicto PROVISIONAL.</b> Los pasos de círculo de competencia (Paso 1), monólogo previo "
        "(Paso 0) y percepción variante (Paso 7) quedan pendientes de que Felipe los complete o ratifique "
        "personalmente antes de considerar este veredicto definitivo, <b>especialmente si implicara comprar</b>. "
        "Lo que sigue en estas páginas es la síntesis evidenciada de tres dossiers de investigación independientes "
        "más un veto de abogado del diablo ya ejecutado en sesión limpia (Paso 10, Candado A) — el documento tiene "
        "ya su forma cerrada según el método, pero tres piezas de juicio personal e intransferible siguen siendo "
        "propuestas tentativas de agente, marcadas explícitamente como tales en las secciones correspondientes, "
        "no como la conclusión real de Felipe.")]
    o += [p("Esto no es una formalidad decorativa. El método QG de 12 pasos distingue entre lo que un agente puede "
        "verificar contra fuente primaria —hechos, cifras, citas, cálculos— y lo que sólo Felipe puede juzgar "
        "porque depende de su propia memoria, su propio umbral de honestidad intelectual y su propia lectura del "
        "consenso de mercado. Ningún agente puede sustituir esos tres juicios sin que el documento deje de servir "
        "para lo que fue diseñado: protegerlo de su propio entusiasmo, no confirmarlo.")]
    o += [p("El riesgo de saltarse este candado es menor en este caso concreto —el veredicto de esta versión es de "
        "cautela (NO COMPRAR TODAVÍA), no de compra— pero no es cero: un NO COMPRAR TODAVÍA mal fundado en un "
        "círculo de competencia no ratificado tampoco es una base sólida para las condiciones de reversión que "
        "este documento fija en la Sección 14. Si en algún momento futuro este documento —o una revisión suya— "
        "se usa para justificar una compra, los Pasos 0, 1 y 7 deben estar resueltos por Felipe mismo, no por un "
        "borrador de agente.")]
    return o + [PageBreak()]


def negocio():
    o = flag_titulo("1 · El negocio explicado desde cero",
                    "Mastercard no mueve dinero: mueve la certeza de que el dinero va a llegar")
    o += [p("Imagina que vas a un mercado extranjero y quieres comprar algo con una moneda que el vendedor no "
        "reconoce. Ninguno de los dos se fía del otro: tú no sabes si el vendedor te va a entregar lo prometido, "
        "y él no sabe si tu dinero vale lo que dices que vale. Ahora imagina que aparece un tercero de confianza "
        "universal que le dice al vendedor “entrégaselo, yo te garantizo el pago”, y al mismo tiempo le dice "
        "a tu banco “cóbrale a tu cliente, yo respondo si algo falla”. Ese tercero no presta el dinero, no "
        "se queda con el riesgo de que no pagues —eso es trabajo de tu banco emisor—, y no vende nada físico. "
        "Sólo garantiza que la transacción es segura, y cobra un céntimo por hacerlo posible. Ese tercero es, "
        "literalmente, Mastercard.")]
    o += [p("<b>Lo que Mastercard NO hace, dicho primero porque es lo que más se confunde:</b> no emite tarjetas, "
        "no extiende crédito y no recibe intereses de los tarjetahabientes. Eso lo hacen los bancos emisores "
        "—Citibank, Santander, Banorte, el banco que te dio tu tarjeta—. Mastercard opera lo que el propio 10-K "
        "FY2025 llama el <i>modelo de cuatro partes</i>: el tarjetahabiente, el banco emisor de la tarjeta, el "
        "comercio, y el banco adquirente que procesa el cobro del comercio. Mastercard es el árbitro que se sienta "
        "en medio de los cuatro y fija los estándares técnicos, las tarifas de intercambio por defecto, las reglas "
        "de disputa cuando algo sale mal, y la liquidación final entre miles de emisores y millones de comercios "
        "que jamás se hablan directamente entre sí.")]
    o += [callout("LA METÁFORA",
        "Piensa en Mastercard como el sistema de control de tráfico aéreo de un país, no como una aerolínea. "
        "No es dueña de los aviones (los bancos), no vende los boletos (el crédito), y no es dueña del aeropuerto "
        "(el comercio). Pero sin ella, ningún avión sabría cuándo puede despegar sin chocar con otro. Cobra una "
        "tarifa mínima por cada vuelo que coordina, y esa tarifa existe precisamente porque coordinar sin ella "
        "sería, para cualquier aerolínea individual, imposible de replicar sola.")]
    o += [p("<b>Cómo cobra, en la práctica.</b> Cada vez que se desliza, se inserta o se acerca una tarjeta "
        "Mastercard a un terminal, la red autoriza la transacción en fracciones de segundo, la enruta hacia el "
        "banco emisor correcto, gestiona la liquidación entre los bancos, y guarda los datos que alimentan su "
        "sistema de detección de fraude (Decision Intelligence). Por todo eso cobra una fracción minúscula del "
        "valor de cada transacción — pero lo cobra sobre un volumen bruto de dólares (GDV, <i>Gross Dollar "
        "Volume</i>) de 10,6 billones de dólares al año (HECHO, 10-K FY2025). El coste marginal de procesar una "
        "transacción adicional es casi cero: la infraestructura de red ya existe, ya está pagada, y cada "
        "transacción extra es casi pura utilidad.")]
    o += [p("<b>Por qué esto no es un negocio replicable por cualquiera con capital.</b> No basta con tener dinero "
        "para construir una red de pagos: hace falta que decenas de miles de bancos emisores y decenas de millones "
        "de comercios, en más de 200 países, decidan simultáneamente conectarse a la misma red — y eso no ocurre "
        "porque alguien lo desee, ocurre porque cada participante adicional hace la red más valiosa para todos los "
        "demás. Ésa es la raíz del mecanismo que la Sección 2 desarrolla en detalle: el foso no es una patente, "
        "no es una marca, no es siquiera la tecnología — es la escala de la red misma, acumulada durante décadas.")]
    return o + [PageBreak()]


def foso():
    o = flag_titulo("2 · El foso: por qué el cliente no se va",
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
        "En Mastercard, va a la empresa. La tasa de intercambio combinada de Visa y Mastercard en Estados Unidos "
        "subió de 2,02% (2010) a 2,36% (2025), con los <i>network fees</i> creciendo aproximadamente un 30% más "
        "rápido que el valor transaccionado en los últimos cinco años (HECHO, litigio de comerciantes, resumido "
        "por Payments Dive/CardTraq 2026). El margen operativo GAAP de Mastercard se expandió de 53,4% (2021) a "
        "57,6% (2025).")]
    o += [callout("LA TRAMPA",
        "Bajo el marco de Sleep, un margen que se expande porque la escala no se comparte con el cliente <b>no es "
        "una señal de fortaleza pura</b> — es una invitación a la disrupción por rieles más baratos. Eso es "
        "exactamente lo que están intentando UPI en India y Pix en Brasil, y es lo que motivó que la Financial "
        "Conduct Authority del Reino Unido abriera, el 6 de mayo de 2026, una investigación de competencia contra "
        "Mastercard y Visa (HECHO, PYMNTS.com). El mismo número que hace atractivo el negocio hoy es el que "
        "alimenta el riesgo regulatorio de mañana — ver Sección 9 y Sección 11.")]
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
        "Añadido (VAS). La pregunta que queda abierta para la Sección 11 no es “¿puede duplicar en diez años?” "
        "sino <b>“¿qué tendría que romperse para que el crecimiento caiga a la mitad de su ritmo reciente y aun "
        "así el caso base sobreviva?”</b>")]
    o += [callout("PAUSA REFLEXIVA",
        "El mecanismo descrito arriba responde bien al ataque histórico de <i>switching</i> de marca dentro del "
        "modelo de cuatro partes (2001-2004; y su repetición reciente, Capital One/Discover). Pero <b>no nombra ni "
        "cuantifica</b> el vector de sustitución tecnológica cuenta-a-cuenta (A2A) patrocinado por bancos centrales "
        "—Pix, UPI, SEPA Instant—, que es un régimen de rieles paralelo y gratuito, no un competidor dentro del "
        "mismo modelo de cuatro partes. Éste es un hueco real del mecanismo, no cerrado por la evidencia "
        "disponible: se convierte en un mecanismo de pre-mortem explícito y falsable en la Sección 11 (mecanismo "
        "#5), añadido después de que el abogado del diablo lo señalara en el Paso 10 — ver Sección 13.")]
    return o + [PageBreak()]
