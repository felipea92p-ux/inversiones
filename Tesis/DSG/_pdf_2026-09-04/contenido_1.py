# -*- coding: utf-8 -*-
"""Portada · Resumen 30s · Aviso de estado · §1 El negocio desde cero · §2 El foso"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, kpi_panel, S, C, cm
from reportlab.platypus import Spacer, PageBreak, NextPageTemplate, Paragraph
from reportlab.lib.styles import ParagraphStyle


def portada():
    t_emp = ParagraphStyle("te", fontName="Serif-B", fontSize=36, leading=40, textColor=C["tinta"])
    t_tag = ParagraphStyle("tg", fontName="Serif-I", fontSize=13, leading=18, textColor=C["gris"])
    t_sec = ParagraphStyle("ts", fontName="Sans-B", fontSize=9, leading=12, textColor=C["rojo"])
    return [
        Spacer(1, 6.2*cm),
        Paragraph("SOFTWARE DE LOGÍSTICA Y CUMPLIMIENTO ADUANERO · AMÉRICA DEL NORTE", t_sec),
        Spacer(1, 10),
        Paragraph("The Descartes Systems Group", t_emp),
        Spacer(1, 5),
        Paragraph("TSX / Nasdaq: DSG / DSGX", t_tag),
        Spacer(1, 4),
        Paragraph("Un compounder aburrido-bueno que recicla casi todo lo que gana en comprar "
                  "empresas a un 13% de retorno, mientras el mercado le paga como si ganara mucho más.", t_tag),
        Spacer(1, 1.5*cm),
        kpi_panel([
            ("US$6.400M", "EV DE MERCADO (ACTUAL)", "EV/EBITDA ≈18,7-20x ·<br/>EV/Revenue 8,48x"),
            ("2.300-3.500", "RANGO DE VALOR (US$M) — CASO BASE", "DCF a WACC 9% central:<br/>−45% a −64% frente al EV de hoy"),
            ("NO COMPRAR TODAVÍA", "VEREDICTO — PROVISIONAL", "degradado por el candado del<br/>abogado del diablo (Paso 10)"),
        ]),
        Spacer(1, 1.0*cm),
        tabla([["FECHA DE SÍNTESIS", "ESTADO DEL VEREDICTO", "PRÓXIMO DATO DURO", "CANDADO A (ABOGADO-DIABLO)"],
               ["4 de septiembre de 2026", "PROVISIONAL — 2 sentidos", "6-K Q2 FY27, ~15-sep-2026", "Ejecutado — 3 golpes, 0 refutados"]],
              [4.15*cm]*4, font_sz=8.6),
        Spacer(1, 0.5*cm),
        M.p("<font size=8.2 color='#666054'><i>Documento de trabajo personal, maquetado sobre un dossier ya "
            "construido con fuente primaria (EDGAR/SEC, AIF, Management Information Circular) y verificado de "
            "forma adversarial. No es asesoramiento de inversión. El precio por acción en vivo no se pudo obtener "
            "en el momento de maquetar este documento — todas las cifras de valor se anclan al Enterprise Value, "
            "que es como el propio dossier construyó su valoración.</i></font>"),
        NextPageTemplate("Normal"), PageBreak()]


def resumen():
    o = flag_titulo("El resumen en treinta segundos", "Si sólo lees una página, que sea ésta")
    o += [p("<b>Descartes conecta a cientos de miles de transportistas, agentes de aduana, forwarders y "
        "gobiernos en más de 160 países</b> para mover mercancía a través de fronteras sin que nadie tenga "
        "que confiar a ciegas en el socio del otro lado. Es un negocio con balance impecable — cero deuda a "
        "largo plazo en cinco años seguidos, línea de crédito de hasta 500 millones sin usar — y márgenes "
        "que sostienen un ROIC del 12-14%.")]
    o += [p("<b>Y aun así, este documento no llega a COMPRAR.</b> No porque el negocio esté roto — los seis "
        "knock-outs binarios del método pasan limpio — sino porque tres cosas, verificadas con evidencia, "
        "cierran el camino:")]
    o += [p("<b>Primero: el crecimiento orgánico lleva tres años frenando</b> — 9,0% → 5,0% → 3,9% en los "
        "últimos tres cierres fiscales completos — antes de un salto reciente a 11,1% en el primer trimestre "
        "de FY27 que el propio management atribuye a volatilidad arancelaria y al fin del <i>de minimis</i> "
        "aduanero, no a un cambio de producto. Podría ser transitorio.")]
    o += [p("<b>Segundo: Descartes recicla ~95% de su beneficio operativo neto en comprar empresas</b>, pero "
        "el retorno individual de las tres adquisiciones que se comieron ese dinero en FY26 —3GTMS, Finale, "
        "Idelic— <b>no se ha divulgado</b>. El ROIC del 12,5-13,9% que sostiene todo el relato de crecimiento "
        "es retrospectivo y viene dominado por compras antiguas ya maduras. Es el hueco de evidencia más "
        "importante del documento, y un abogado del diablo en sesión limpia lo elevó de \"pendiente\" a "
        "\"bloqueante\".")]
    o += [p("<b>Tercero, y es lo que decide: con el WACC que la propia metodología obliga a usar, el precio "
        "no cuadra.</b> A un WACC bottom-up de ~9% —el que exige el candado de la casa contra heredar tasas "
        "de descuento por conveniencia— el DCF explícito a diez años arroja un Enterprise Value de "
        "US$2.300-3.500 millones. El mercado paga hoy US$6.400 millones. Para justificar ese precio, Descartes "
        "necesita sostener crecimiento de doble dígito durante <b>8 a 10 años más</b>, sin que el retorno "
        "marginal de sus compras se deteriore — una ventana más larga que la que suele durar una ventaja "
        "competitiva real en software vertical de tamaño mediano.")]
    o += [callout("PAUSA REFLEXIVA",
        "Antes de seguir, la pregunta que de verdad importa no es «¿es Descartes un buen negocio?» — "
        "probablemente sí lo es. Es: <b>¿cuánto de ese crecimiento de doble dígito, sostenido casi una "
        "década, estás dispuesto a dar por sentado al precio de hoy?</b> Ese es exactamente el tipo de "
        "pregunta que un veredicto de \"calidad extraordinaria\" tiende a hacer olvidar.")]
    o += [p("<b>La moat tiene dos capas, y sólo una sobrevivió intacta al escrutinio adversarial.</b> El "
        "cumplimiento aduanero y regulatorio es lock-in real — un fallo de migración no es perder "
        "productividad, es no poder nacionalizar mercancía. Pero el \"efecto de red\" que el dossier original "
        "trataba como hecho duro resultó ser, en gran parte, la empresa describiéndose a sí misma: no existe, "
        "dentro de la investigación hecha, un caso fechado y nombrado de un cliente citando coste de cambio "
        "de red al evaluar un competidor. Ese pilar del moat se degrada de HECHO a INFERENCIA.")]
    o += [hr(), p("<b>Las tres cifras que hay que retener:</b>")]
    o += [tabla([
        ["LA CIFRA", "QUÉ SIGNIFICA"],
        ["<b>8-10 años</b>",
         "El tiempo de crecimiento de doble dígito que el precio de hoy exige, calculado con el WACC "
         "bottom-up que la casa obliga a usar. Bajarlo a 5-6 años exigiría adoptar la beta de regresión "
         "más baja del mercado — exactamente lo que el candado de la casa prohíbe hacer por conveniencia."],
        ["<b>96% de $157M</b>",
         "La proporción del capital reinvertido en FY26 que fue a tres adquisiciones (3GTMS, Finale, Idelic) "
         "sin ROIC individual divulgado. Es la mecánica exacta que hundió a e2open — comprar caro en un "
         "\"mercado de vendedores\" sin saber si el retorno marginal aguanta."],
        ["<b>0 casos documentados</b>",
         "El número de episodios fechados y nombrados, encontrados en esta investigación, de un cliente "
         "enterprise citando coste de cambio de red al evaluar migrar a un competidor. Sin eso, la mitad "
         "del moat de Descartes es una hipótesis plausible, no un hecho verificado."]],
        [3.6*cm, 13.0*cm], font_sz=8.8)]
    o += [p("<b>Lo que sí cambia el veredicto, y pronto:</b> el 6-K del segundo trimestre fiscal (mayo-julio "
        "2026) reporta en la primera quincena de septiembre de 2026 — días desde la fecha de esta síntesis, "
        "no meses. Si el orgánico cae por debajo de 6% ahí, la hipótesis de \"salto transitorio\" queda "
        "confirmada de inmediato. Pero incluso si el orgánico se sostiene fuerte, <b>eso solo no basta</b>: "
        "hacen falta también el ROIC marginal de las tres compras y una reconciliación honesta de la beta.")]
    return o + [PageBreak()]


def aviso_estado():
    o = flag_titulo("Aviso de estado del documento", "Léase antes de tomar cualquier decisión de capital sobre esta tesis")
    o += [callout("PAUSA REFLEXIVA",
        "<b>Este veredicto es PROVISIONAL en dos sentidos distintos, y ninguno de los dos lo puede cerrar "
        "un agente.</b> Primero, refleja la degradación exigida por el candado del abogado del diablo tras "
        "su veto (Paso 10 — Sección 13 de este documento). Segundo, y más importante: <b>los Pasos 0 "
        "(monólogo previo), 1 (círculo de competencia) y 7 (percepción variante) del método están marcados "
        "en este documento como [BORRADOR DE AGENTE]</b> porque son juicios que, por diseño, solo Felipe "
        "puede certificar. Ningún agente puede sustituir su instinto ni declarar en su nombre que el "
        "componente regulatorio de <i>trade compliance</i> —una capa técnica específica dentro del moat de "
        "Descartes— está dentro de su círculo de competencia real. Sin esa certificación, ni siquiera "
        "\"NO COMPRAR TODAVÍA\" es, en sentido estricto, una conclusión completa.")]
    o += [p("Este documento sintetiza tres dossieres ya construidos con fuente primaria (EDGAR/SEC, AIF, "
        "Management Information Circular) más una verificación adversarial independiente que corrigió dos "
        "errores reales en el dossier original, no uno. Ambos importan para leer bien lo que sigue:")]
    o += [tabla([
        ["CORRECCIÓN", "QUÉ ESTABA MAL", "QUÉ CAMBIA"],
        ["Serie de crecimiento orgánico FY24",
         "El desglose orgánico/inorgánico de FY24 usaba una convención de cálculo distinta a la de FY25-FY26.",
         "Este documento usa en todo momento la serie corregida (misma convención, 5 años), verificada "
         "contra el propio filing."],
        ["Calendario fiscal de los gatillos (Pasos 8 y 12)",
         "El borrador original situaba el 6-K de Q2 FY27 en diciembre de 2026 y el de Q3 FY27 en marzo de 2027.",
         "Con año fiscal cerrando el 31 de enero, Q2 FY27 (may-jul 2026) reporta en realidad en la "
         "<b>primera quincena de septiembre de 2026</b> — días desde hoy — y Q3 FY27 hacia diciembre de "
         "2026. El catalizador pasó de \"lejano\" a \"inminente\"."]],
        [4.4*cm, 6.2*cm, 6.0*cm], font_sz=8.4)]
    o += [p("Se declara aquí, una sola vez para todo el documento, la degradación de fuente que lo atraviesa "
        "entero: <b>Quartr no estuvo disponible en ninguna de las tres sesiones de investigación</b> (cuenta "
        "sin suscripción activa). La sección de scuttlebutt (6) se construyó con 6-K/40-F de EDGAR más un "
        "único transcript completo de tercero, en vez de transcripts primarios con preguntas directas de "
        "analistas sobre pérdida de cuentas. El candado A (Sección 13) trata esta ausencia, combinada con el "
        "vacío de evidencia sobre el moat de red, como un factor <b>bloqueante en sí mismo</b> para cualquier "
        "veredicto de COMPRA — no un simple pendiente para la próxima ronda.")]
    return o + [PageBreak()]


def s1_negocio():
    o = flag_titulo("1 · Qué hace Descartes, explicado desde cero",
                    "El negocio entero cabe en una frase: pone una capa neutral entre todos los que mueven "
                    "mercancía a través de una frontera")
    o += [p("Imagina una fábrica en Ohio que compra componentes en Vietnam. Antes de que ese contenedor "
        "pueda entrar a Estados Unidos tiene que pasar por una cadena de intermediarios que no se conocen "
        "entre sí: el transportista marítimo, el agente de aduanas, el forwarder que organiza el último "
        "tramo por carretera, y la propia Aduana de EE.UU., que necesita saber exactamente qué es la carga, "
        "de dónde viene y si alguna de las partes involucradas está en una lista de sanciones. Cada uno de "
        "esos eslabones habla un idioma de datos distinto y tiene sus propios sistemas.")]
    o += [p("<b>Ahí es donde entra la Global Logistics Network (GLN) de Descartes.</b> Es una única capa que "
        "conecta a \"cientos de miles de organizaciones\" en más de 160 países [AIF FY2026, Sección 4.2] "
        "para investigación de comercio global, gestión de inventario y almacén, reserva de embarque, "
        "seguimiento, declaración regulatoria y liquidación/auditoría de factura. No transporta nada "
        "físicamente — es la capa de información y cumplimiento que hace que todos los demás eslabones "
        "puedan hablar entre sí y satisfacer al regulador sin reinventar la integración cada vez.")]
    o += [p("<b>El modelo de ingresos es de suscripción y uso</b>, cobrado en gran medida sobre volumen "
        "transaccional (envíos, declaraciones, mensajes procesados) más licencias de producto — la mecánica "
        "exacta de tarificación no está desglosada públicamente por línea, porque Descartes reporta un solo "
        "segmento operativo. Lo que sí es HECHO verificado es la estructura de clientes: no hay concentración "
        "de cliente único —Descartes trabaja a través de ~96 distribuidores y revendedores activos a "
        "31-ene-2026 [AIF FY2026, Sección 4.5]— y ningún cliente individual representó más del 10% del saldo "
        "de cuentas por cobrar en los cierres de enero de 2025 y 2026 [Nota 5 de los estados financieros].")]
    o += [p("<b>Sí hay una concentración que merece vigilarse, aunque no dispara ningún knock-out</b>: la "
        "geográfica. Los ingresos originados en Estados Unidos pasaron de 66,7% (FY24) a 67,5% (FY25) y "
        "68,1% (FY26) — una dependencia creciente de una sola jurisdicción, justo la que hoy genera la "
        "volatilidad regulatoria (aranceles, IEEPA, <i>de minimis</i>) que explica buena parte del salto de "
        "crecimiento reciente. Es una espada de doble filo: el mismo entorno que impulsa la demanda hoy "
        "podría normalizarse y quitarle ese impulso mañana.")]
    o += [p("<b>El balance es, en una palabra, limpio.</b> Deuda a largo plazo de cero dólares en cinco años "
        "fiscales consecutivos sin excepción, con una línea de crédito de US$350-500 millones completamente "
        "sin usar. Descartes no necesita apalancarse para crecer — lo cual, como se verá en la Sección 5 y "
        "de nuevo en la 12, es tanto su mayor fortaleza defensiva como la razón por la que el mecanismo de "
        "riesgo central de esta tesis no es de solvencia, sino de <i>capital mal asignado a un ritmo lento "
        "mientras el mercado paga como si fuera rápido</i>.")]
    return o + [PageBreak()]


def s2_foso():
    o = flag_titulo("2 · El foso: dos capas, y sólo una sobrevivió al escrutinio",
                    "Un negocio de red que casi murió una vez, y un moat que resultó tener menos densidad de la que decía tener")
    o += [p("El mecanismo de retención de Descartes tiene, según el propio dossier de investigación, dos "
        "capas distintas que conviene separar con cuidado — porque, como se explica más abajo, terminaron "
        "el proceso de verificación con estatus muy distinto.")]
    o += [p("<b>Capa 1 — efecto de red de doble cara.</b> Cuantos más transportistas, agentes y forwarders "
        "ya están conectados a la GLN, menor la fricción de integración para el siguiente cliente que se "
        "suma, y mayor el coste de salir: desconectarse no es dar de baja un software, es perder "
        "conectividad con los socios comerciales ya integrados [AIF FY2025, Sección 3.3]. Es el argumento "
        "clásico de valor de red — y es, casi palabra por palabra, cómo la propia compañía describe su "
        "ventaja competitiva en sus presentaciones regulatorias.")]
    o += [p("<b>Capa 2 — coste de cambio regulatorio.</b> Los módulos de declaración aduanera y cribado de "
        "partes sancionadas están mecanizados dentro de obligaciones legales con plazo, para clientes que "
        "incluyen \"agencias gubernamentales de aduanas y censo\" [AIF FY2026, Sección 4.4]. Aquí el coste "
        "de un fallo de migración no es \"perder productividad\": es no poder nacionalizar la mercancía a "
        "tiempo. Este tipo de lock-in es estructuralmente distinto y más duro que el de red.")]
    o += [callout("CASO HISTÓRICO",
        "En 2004, tras el colapso puntocom, Descartes estuvo cerca de la bancarrota. Muchos de sus primeros "
        "nodos de red eran empresas de logística ligadas a esa burbuja, y su quiebra en cascada revirtió el "
        "efecto de red en sentido contrario: menos nodos activos significaban menos valor por nodo, lo que "
        "empujaba a más abandono todavía. Arthur Mesher asumió el cargo de CEO en 2005 e inició una "
        "reconstrucción de una década sobre una base de clientes mucho más diversificada por sector. Es la "
        "prueba de estrés más dura que puede sufrir un moat de red — no \"¿aguanta un competidor?\", sino "
        "\"¿aguanta que la mitad de la comunidad desaparezca a la vez?\" — y el negocio sobrevivió, aunque "
        "por poco. <i>Nota de fuente: este episodio proviene de Wikipedia, no verificado contra prensa de "
        "época — se marca aquí explícitamente como el eslabón más débil de toda la cadena de evidencia del "
        "moat.</i>")]
    o += [p("<b>El contraste honesto que el propio dossier declara:</b> no hay concentración de cliente "
        "único que se pueda señalar como prueba del moat — es un moat de densidad agregada de red, no de "
        "contratos irrompibles con nombre propio. Eso reduce el riesgo de perder una cuenta ballena, pero "
        "también significa que el moat no se puede probar con un solo contrato: hay que probarlo con el "
        "comportamiento agregado de la red bajo estrés, o con un caso individual bien documentado. Ninguna "
        "de esas dos pruebas apareció, dentro del presupuesto de esta investigación, para un competidor "
        "concreto (Amber Road, GT Nexus, Kewill, INTTRA/WiseTech) arrebatando una cuenta específica con "
        "desenlace verificable.")]
    o += [p("<b>Ese vacío de evidencia no se quedó como una nota al pie.</b> Un abogado del diablo, "
        "trabajando en sesión limpia y sin el entusiasmo acumulado de esta síntesis (ver Sección 13 para el "
        "razonamiento completo), lo convirtió en un hallazgo con peso propio: el mecanismo dominante en "
        "redes logísticas B2B comparables —EDI VANs, project44, FourKites, SAP Business Network, el propio "
        "e2open antes de quebrar— es <b>multi-homing, no exclusividad</b>. \"Cientos de miles de "
        "organizaciones conectadas\" mide el alcance de la red, no el coste de cambio real de un cliente "
        "concreto. Sin un caso fechado y nombrado que lo contradiga, la Capa 1 (red) se reclasifica de "
        "HECHO a <b>INFERENCIA</b> en cualquier documento que herede este dossier, incluida cualquier "
        "actualización trimestral futura. La Capa 2 (regulatoria) sobrevivió el ataque intacta y se "
        "mantiene como HECHO.")]
    o += [p("<b>El moat combinado, entonces, es más estrecho de lo que decía el borrador original — no "
        "roto.</b> Un mecanismo verificado (cumplimiento regulatorio, difícil de replicar y con coste de "
        "fallo severo) más una hipótesis plausible pero sin probar (red). Es la diferencia entre \"doble "
        "mecanismo verificado\" y \"un mecanismo verificado más una promesa\" — y esa diferencia es exactamente "
        "la que separa un veredicto de COMPRA de uno de NO COMPRAR TODAVÍA cuando, además, el precio no "
        "sostiene el escenario optimista (Sección 12).")]
    return o
