# -*- coding: utf-8 -*-
"""CONTENIDO · Tesis Ultra MSFT v2.0. Solo prosa/datos. Importa motor_qg (diseño) y dcf_msft (números).
v2.0 (2026-07-09): refresco editorial — voz narrativa enriquecida (metáforas de ajedrez/historia y de
biología evolutiva, curiosidades verificadas sobre Microsoft/Nadella, jerga técnica explicada en cada
sección). CERO cambios en números, tiers o veredicto de inversión: ese trabajo vive exclusivamente en
dcf_msft.py, que no se tocó."""
from reportlab.platypus import Spacer, PageBreak, NextPageTemplate, Paragraph
from reportlab.lib.units import cm
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER
import motor_qg as M
from motor_qg import C
import dcf_msft as D

def sp(h=6): return Spacer(1, h)
def ch(name, w=16.4): return M.chart(f"charts/{name}.png", w)
DISCLAIMER = ("Este score mide CALIDAD del negocio, no valoración ni margen de seguridad. "
              "Score alto &ne; comprar.")

# ══════════════════════════════════════════════════════════════════════════
def portada():
    nombre = ParagraphStyle("nm", fontName="Serif-B", fontSize=33, leading=36, textColor=C["tinta"])
    tick = ParagraphStyle("tk", fontName="Sans-B", fontSize=12.5, leading=16, textColor=C["rojo"])
    tag = ParagraphStyle("tg", fontName="Serif-I", fontSize=12.5, leading=17, textColor=C["gris"])
    meta = ParagraphStyle("meta", fontName="Serif", fontSize=9.5, leading=13, textColor=C["tinta"])
    fn = ParagraphStyle("fn", fontName="Serif-I", fontSize=8, leading=11, textColor=C["gris"])
    out = [Spacer(1, 2.1*cm),
        Paragraph("MICROSOFT CORP.", nombre),
        Paragraph("NASDAQ: MSFT &nbsp;·&nbsp; Software / cloud &nbsp;·&nbsp; infraestructura de la IA", tick),
        sp(14),
        Paragraph("Microsoft juega, a la vez, la partida más rentable del ajedrez corporativo (software "
                  "con coste marginal casi nulo) y la apuesta de infraestructura más cara de su historia: "
                  "190.000 millones de dólares al año construyendo las fábricas de la inteligencia "
                  "artificial. El mercado, al ver comprimirse el flujo de caja libre (FCF, el efectivo "
                  "que sobra tras pagar las cuentas y la inversión), la castigó con una caída del 20% y "
                  "le colgó su múltiplo más barato desde 2022. La pregunta no es si el negocio es bueno "
                  "—lo es, y de los mejores del mundo—. Es si ese capex colosal es reinversión de "
                  "altísimo retorno, la jugada que abre una nueva partida, o una sobre-construcción que "
                  "el precio ya no perdona.", tag),
        sp(20),
        M.kpi_panel([
            (f"{D.es(D.SCORE_QG,0)}/100", "CALIDAD QG", f"tier {D.TIER_QG} · empresa ancla"),
            (f"US${D.PWFV}", "VALOR (PWFV)", f"vs US${int(D.PRECIO)} hoy · zona {D.ZONA_HOY.split(' / ')[0]}"),
            (f"+{D.MOS_HOY}%", "MARGEN vs VALOR", f"exigido {D.MOS_EXIG}% → {D.VEREDICTO}"),
        ]),
        sp(16), M.hr(),
        Paragraph(f"<b>6 de julio de 2026</b> &nbsp;·&nbsp; Precio US${D.es(D.PRECIO,2)} &nbsp;·&nbsp; "
                  f"Máximo 52s US${int(D.ATH)} (−31%) &nbsp;·&nbsp; Horizonte 5–10 años &nbsp;·&nbsp; "
                  f"Documento de convicción N&ordm; 15", meta),
        M.hr(),
        Paragraph("Eje CALIDAD (sistema qg-seilern de 11 reglas) y eje PRECIO (val-mos: PWFV-Valor, "
                  "detector de trampas, MoS por tier) calculados por separado y cruzados solo al final. "
                  "Uso personal; no es asesoría de inversión registrada.", fn),
        NextPageTemplate("Normal"), PageBreak()]
    return out

# ══════════════════════════════════════════════════════════════════════════
def changelog():
    o = M.flag_titulo("Changelog de versiones", "Qué se fija en la v1.0 para poder auditarlo después")
    o += [M.p("Esta es la <b>versión 1.0</b> de la tesis Ultra de Microsoft bajo el estándar de dos ejes. "
        "Como no hay versión previa contra la que medir un delta, se documentan aquí los <b>supuestos "
        "iniciales más críticos</b> —los que, si cambian, moverían el veredicto— para blindar la tesis "
        "contra el <i>motivated reasoning</i> futuro. Con un compounder de esta calidad, la tentación es "
        "justificar la compra a cualquier precio «porque es Microsoft»; el estándar lo impide anclando el "
        "veredicto al margen de seguridad, no a la reputación.")]
    o += [M.tabla([
        ["Supuesto crítico fijado en v1.0", "Valor", "Qué lo movería"],
        ["Owner earnings normalizado (CFO − capex mantenim. − SBC)", "~US$115B", "Que el capex de crecimiento no plateaue en FY27-28"],
        ["Capex de mantenimiento (prudente, no heroico)", "~14% de ventas", "Que MSFT confirme una fracción distinta"],
        ["WACC (anclado al tier Núcleo)", f"{D.es(D.WACC,1)}%", "Cambio de tier QG o del riesgo de sobre-inversión"],
        ["PWFV-Valor (ancla de decisión)", f"US${D.PWFV}", "El ROIC incremental del capex de IA"],
        ["Detector de trampas", "PASA (2 alertas)", "Que el ROIC incremental de IA quede &lt; WACC"],
    ], [7.4*cm, 2.8*cm, 6.2*cm])]
    o += [M.p("<b>El punto de honestidad que esta tesis se obliga a recordar:</b> el corazón del caso es "
        "que el flujo de caja libre reportado (deprimido por el capex de crecimiento) <i>subestima</i> el "
        "poder de generación de Microsoft. Eso es cierto — pero es también exactamente el tipo de "
        "argumento que un alcista usa para justificar cualquier gasto. La disciplina está en el elemento "
        "falsable (§13): si el ROIC incremental del capex de IA queda por debajo del coste de capital "
        "durante ~8 trimestres, la «reinversión de fase» se convierte en «capital atrapado» y la tesis se "
        "rompe. La v1.0 fija esa línea por escrito para que el yo futuro no la mueva.")]
    o += [M.p("<b>Nota de versión — v2.0 (9-jul-2026).</b> Este refresco es exclusivamente editorial: se "
        "reescribió la voz narrativa del documento (metáforas de ajedrez, historia y biología evolutiva; "
        "curiosidades verificadas sobre Nadella y los orígenes de Microsoft; jerga técnica explicada en "
        "cada sección) para que sea más fácil de leer y de recordar. <b>Cero cambios en números, tiers o "
        "veredicto de inversión</b> — todos los datos, scores y umbrales de la v1.0 siguen vigentes tal "
        "cual, congelados en dcf_msft.py, que no se tocó en este refresco.")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def resumen():
    o = M.flag_titulo("Resumen en treinta segundos", "La pregunta operativa, tres números y un veredicto")
    o += [M.p("<b>¿Es el capex de 190.000 millones al año de Microsoft la reinversión disciplinada de un "
        "compounder (una empresa que reinvierte sus ganancias a alto retorno y las hace crecer como una "
        "bola de nieve) en la fase más rentable de su historia, o una sobre-construcción de "
        "infraestructura —una especie que se expande más rápido de lo que su territorio puede "
        "alimentar— que comprime el flujo de caja antes de que la monetización de la IA la justifique?</b> "
        "Toda la tesis vive en esa pregunta. El mercado respondió castigando la acción un 20% en doce "
        "meses y colgándole su múltiplo más barato desde 2022, mientras Azure (la nube de Microsoft) "
        "acelera a +40% y la IA ya factura a un ritmo anualizado (run-rate) de 37.000 millones de "
        "dólares (+123%). [HECHO]")]
    o += [M.tabla([
        ["El número", "Qué dice"],
        ["g implícita +7,7%", "A US$384 el precio descuenta ~8% de crecimiento de owner earnings a 10 años: menos que el escenario conservador, y muy por debajo de Azure +40%. El pesimismo está en el precio. [DCF inverso]"],
        ["P/FCF 39x → ~23x", "El P/FCF titular de 39x es un espejismo: el capex de CRECIMIENTO deprime el FCF. Normalizado, el owner-yield es ~4% y el P/OE ~23x — coherente con el P/E de 23x. [val-mos]"],
        ["MoS +26% &gt; 15% exigido", "El descuento vs valor intrínseco (PWFV US$520) supera con holgura el 15% que exige su tier Núcleo. Por eso: COMPRAR TRAMO. [val-mos]"],
    ], [3.7*cm, 12.7*cm])]
    o += [sp(6), M.p(f"<b>Veredicto operativo.</b> Calidad QG <b>{D.es(D.SCORE_QG,0)}/100</b> (tier "
        f"<b>{D.TIER_QG}</b>, empresa ancla): fosos entre los más anchos del mundo (Microsoft 365, "
        f"LinkedIn, Azure), ROIC de élite (31% / 47% ex-goodwill) y márgenes operativos en máximo "
        f"histórico (46,8%). PWFV-Valor <b>US${D.PWFV}</b> frente a US${int(D.PRECIO)}: zona "
        f"<b>{D.ZONA_HOY}</b> ({D.es(D.DCTO_HOY,1)}%). El detector de trampas da <b>PASA</b> (0 señales "
        f"estructurales plenas; 2 alertas de vigilancia: el ROIC en descenso de fase y los 196.600 "
        f"millones en leases fuera de balance). <b>Acción: {D.VEREDICTO}</b>, tramo inicial "
        f"{D.TRAMO_INI} del NAV, ampliable a {D.TECHO_POS} tras confirmarse que el capex hace plateau y "
        f"el FCF se descomprime. La asimetría es ~{D.es(D.ASIMETRIA,0)}:1: el escenario bajista "
        f"(US${D.V_BEAR}) casi toca el precio de hoy, mientras el valor ponderado (US${D.V_POND}) ofrece "
        f"un +35%.")]
    o += [M.callout("PAUSA REFLEXIVA",
        "Microsoft y Duolingo son la misma película con un final distinto — y vale la pena mirarlas una "
        "al lado de la otra porque el contraste es el mejor entrenamiento de disciplina que tengo. En "
        "ambas el mercado castiga un gasto que deprime una métrica de caja (la compensación en acciones, "
        "SBC, en una; el capex de IA en la otra) y le cuelga un múltiplo barato. La diferencia decisiva: "
        "en Duolingo el descuento (21%) quedaba corto del umbral que exige su tier y el moat estaba bajo "
        "un ataque no refutado → VIGILAR. En Microsoft el descuento (26%) supera el umbral de un tier "
        "superior, el detector de trampas pasa limpio, y la «herida» es un capex de crecimiento "
        "verificablemente demandado (Azure a +40%, restricción de oferta, no de demanda) → COMPRAR. La "
        "pregunta que importa: ¿estás comprando la calidad al descuento, o estás pagando por adelantado "
        "un retorno de capex que todavía no existe? El §9 argumenta lo primero; el §12 vigila activamente "
        "lo segundo, con reglas escritas de antemano para no engañarte a vos mismo cuando llegue el "
        "momento.")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def cuadro_mando():
    o = M.flag_titulo("Cuadro de mando trimestral", "Lo único que se refresca cada trimestre · corte 6-jul-2026")
    o += [M.p("<b>Bloque 1 · Estado de la posición.</b>", "h3")]
    o += [M.tabla([
        ["Concepto", "Estado"],
        ["Precio / zona", f"US${D.es(D.PRECIO,2)} · zona {D.ZONA_HOY} (+{D.MOS_HOY}% de MoS vs PWFV)"],
        ["Valor justo (PWFV-Valor)", f"US${D.PWFV} · ponderado por escenarios US${D.V_POND}"],
        ["Probabilidades de escenario", f"Bajista {D.P_BEAR}% (US${D.V_BEAR}) · Base {D.P_BASE}% (US${D.V_BASE}) · Alcista {D.P_BULL}% (US${D.V_BULL})"],
        ["Veredicto operativo", f"{D.VEREDICTO} · tramo inicial {D.TRAMO_INI} NAV · ampliar a {D.TECHO_POS} tras plateau de capex"],
    ], [4.3*cm, 12.1*cm])]
    o += [sp(4), M.p("<b>Bloque 2 · Tracker de KPIs en semáforo</b> (canarios de la fase de capex, VI.7).", "h3")]
    o += [M.tabla([
        ["Indicador", "Hoy", "Umbral rojo", "●"],
        ["Azure (moneda constante)", "+39% (acelerando)", "&lt; +25% cc", "verde"],
        ["Microsoft Cloud gross margin", "66% (−300 pb)", "&lt; 63–64% estructural", "ambar"],
        ["Capex / ventas (plateau)", "30,5% (subiendo)", "no hace plateau FY27-28", "ambar"],
        ["FCF económico (con leases)", "~US$51B", "&lt; US$45B", "ambar"],
        ["RPO concentración OpenAI", "~45% del backlog", "OpenAI renegocia / recorta", "ambar"],
        ["Margen operativo consolidado", "46,8% (récord)", "cae bajo 44%", "verde"],
    ], [6.0*cm, 4.4*cm, 4.2*cm, 1.8*cm])]
    o += [sp(4), M.p("<b>Bloque 3 · Feedback loop de calibración.</b>", "h3")]
    o += [M.tabla([
        ["Predicción (trim. anterior)", "Resultado real", "Interpretación"],
        ["v1.0 — sin predicción formal previa", "Q3 FY26: rev US$82,9B (+18%), Azure +40%, capex $30,9B", "Punto de partida; base para calibrar desde el próximo trimestre"],
        ["Zona predicha vs precio real", f"OPORTUNIDAD/GANGA a US${int(D.PRECIO)}", "El DCF/val-mos queda por calibrar contra la evolución del capex y el FCF"],
    ], [5.6*cm, 5.4*cm, 5.4*cm])]
    o += [sp(4), M.p("<b>Bloque 4 · Operativo.</b> Último trigger disparado: la <b>caída del ~20% en doce "
        "meses</b> (−31% desde el máximo de 52 semanas) por el shock de la guía de capex de $190B, que "
        "abrió la ventana de valoración. Fecha del refresh: <b>6-jul-2026</b>; se escribió el documento "
        "entero. Próxima revisión: resultados de <b>Q4 FY2026</b> (finales de julio 2026), con foco en el "
        "margen bruto de Microsoft Cloud, el ritmo de capex y cualquier señal de plateau.")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def veredicto_cuant():
    o = M.flag_titulo("El veredicto cuantificado", "Las once reglas Quality Growth, sin regalar puntos al ancla")
    o += [M.p(f"<i>{DISCLAIMER}</i>", "nota")]
    o += [ch("01_radar", 15.0), sp(4)]
    vd = {
        "R1 · Escalabilidad": "Coste marginal casi nulo, margen operativo 41,6%→46,8%; pero la fase IA lo vuelve semi-industrial (capex/ventas 12%→30%).",
        "R2 · Industria": "Cloud + IA + seguridad, tailwinds seculares &gt;10 años; lastran gaming (−7%) y Windows/Devices (−2%).",
        "R3 · Liderazgo": "#1 en productividad, seguridad y LinkedIn; #2 en cloud ganando cuota. Pero NO lidera en modelos IA (Anthropic) y el antitrust acecha el bundle.",
        "R4 · Moat": "Archipiélago de fosos interconectados (costes de cambio + red + escala). El frente IA está bajo ataque; el moat es de distribución, no de modelo.",
        "R5 · Crec. orgánico": "Ingresos +14,9% FY25, +18% Q3; orgánico y de doble dígito. El EPS titular está inflado por una ganancia no operativa de OpenAI.",
        "R6 · Diversificación": "Millones de clientes, geografía global, ningún cliente &gt;10% del P&amp;L; pero ~45% del backlog (RPO) depende de OpenAI.",
        "R7 · Capital / ROIC": "ROIC de élite (31% / 47% ex-goodwill) pero en descenso (44%→31%) y capex disparado. La cuña de la tesis.",
        "R8 · Balance": "Cero deuda tóxica, AAA de facto; pero la caja neta se erosionó (+$57B→+$9B) por finance leases que se triplicaron.",
        "R9 · Transparencia": "CFO/beneficio 1,36x, sin restatements; pero el EPS titular está contaminado por la línea no operativa de OpenAI. Usar el operativo.",
        "R10 · Gestión": "Nadella/Hood de clase mundial, una sola clase de acción; deméritos: ownership &lt;1% y Chairman+CEO combinado.",
        "R11 · Impacto": "Infraestructura de productividad y ciberseguridad #1 mundial a escala civilizatoria; no llega al máximo (reservado a salud/inclusión).",
    }
    filas = [["Regla", "Puntos", "Veredicto en una línea"]]
    for n, pts, mx in D.REGLAS:
        filas.append([n, f"{D.es(pts,2).rstrip('0').rstrip(',') if pts % 1 else int(pts)}/{mx}", vd[n]])
    filas.append(["<b>TOTAL</b>", f"<b>{D.es(D.RAW_QG,1)}/125</b>",
                  f"<b>{D.es(D.SCORE_QG,1)}/100 · tier {D.TIER_QG} (&ge;85)</b>"])
    o += [M.tabla(filas, [3.4*cm, 2.2*cm, 10.8*cm])]
    o += [M.p("<i>Nota metodológica: el score se calibró con el estándar alto de una empresa ancla, sin "
        "regalar puntos. Un negocio que se capitaliza como una utility (capex 30% de ventas) no puede "
        "puntuar al máximo en «baja intensidad de capital» (R7), por muy excepcional que sea su ROIC "
        "absoluto. El 86 refleja calidad Núcleo indiscutible con deméritos reales y honestos concentrados "
        "en la transición a la IA.</i>", "nota")]
    o += [M.callout("LECCIÓN TRANSFERIBLE",
        "Las empresas ancla son las más peligrosas de puntuar: la reputación empuja hacia el 95, y ese "
        "sesgo de halo destruye la calibración de todo el sistema. Un score honesto no premia el nombre; "
        "penaliza lo que hoy está peor —aquí, que Microsoft dejó de ser asset-light, que su ROIC "
        "incremental de la IA está sin probar, y que el 45% de su backlog descansa en una empresa que "
        "pierde 14.000 millones al año—. El 86 no dice «Microsoft es mediocre»; dice «Microsoft es "
        "excepcional atravesando un cambio real en la naturaleza de su modelo económico», y esa precisión "
        "es la que separa un veredicto útil de un aplauso.")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def s1():
    o = M.flag_titulo("§1 · La historia detrás del veredicto", "De vendedor de licencias a dueño de la infraestructura")
    o += [M.p("Toda buena historia de negocios tiene una apertura audaz, y la de Microsoft es de las "
        "mejores del ajedrez empresarial. En enero de 1975, Paul Allen le mostró a Bill Gates la portada "
        "de la revista <i>Popular Electronics</i> con la computadora Altair 8800, y ambos llamaron a su "
        "fabricante ofreciéndole un intérprete del lenguaje de programación BASIC que <b>todavía no "
        "existía</b>. Lo escribieron en ocho semanas, sin haber tocado jamás una Altair, con la ayuda de "
        "un tercer programador, Monte Davidoff. Funcionó en la demostración, y así nació Microsoft el 4 "
        "de abril de 1975, en Albuquerque, Nuevo México. [HECHO, Wikipedia / History.com / The New Stack] "
        "Cincuenta años después, la compañía sigue jugando variaciones de la misma apertura: apostar el "
        "negocio a un producto que todavía no está listo, con una convicción que solo se justifica en "
        "retrospectiva.")]
    o += [M.p("Cuando Satya Nadella tomó las riendas en febrero de 2014, heredó un tablero complicado: "
        "Microsoft dominaba Windows y Office pero había perdido la partida del móvil, y su cultura "
        "interna era legendariamente hostil —de las que premian tener siempre la razón, no aprender—. "
        "Once años después, es —de nuevo— la empresa más valiosa del mundo por momentos, con ingresos "
        "que pasaron de US$87.000 millones (2014) a <b>US$281.700 millones (FY2025)</b> y un margen "
        "operativo que <i>expande</i>, no se comprime, hasta el 45,6%. [HECHO] Nadella jugó dos "
        "movimientos, no uno: cambió la cultura corporativa (de «sabelotodo» a «aprendelotodo», "
        "institucionalizando el growth mindset —la idea, tomada de la psicóloga Carol Dweck, de que la "
        "capacidad se entrena y no es un rasgo fijo— cuyo libro le regaló su esposa Anu poco después de "
        "que asumiera) y apostó el futuro de la compañía a la nube. Azure, que casi no existía, es hoy el "
        "segundo proveedor de nube (infraestructura de computación alquilada por internet) del mundo y "
        "crece al 40%. [HECHO, Fortune / London Business School]")]
    o += [M.p("La historia de 2026 es el <b>tercer acto</b>: la inteligencia artificial. Aquí conviene "
        "recordar el error de cálculo más citado de la historia reciente de la compañía, porque mide la "
        "distancia entre el Microsoft de ayer y el de hoy. En 2007, semanas después del lanzamiento del "
        "iPhone, el entonces CEO Steve Ballmer declaró a USA Today: «No hay ninguna posibilidad de que el "
        "iPhone consiga una cuota de mercado significativa» —un teléfono de 500 dólares subsidiado, sin "
        "teclado físico—. [HECHO, USA Today, vía TechRadar/MacRumors] Fue la jugada que le costó a "
        "Microsoft una década de irrelevancia en móvil. El Microsoft de Nadella se movió antes que nadie "
        "en la apertura contraria: invirtió en OpenAI en 2019, integró GPT en todo su catálogo, y lanzó "
        "Copilot (la capa de asistentes de inteligencia artificial de Microsoft) sobre su base instalada "
        "de 446 millones de asientos de Microsoft 365. Pero ese liderazgo tiene un precio literal: para "
        "alojar la IA hace falta silicio, y el silicio es caro. Microsoft guía un capex (gasto de "
        "capital: la inversión en activos de larga duración, aquí sobre todo chips y centros de datos) "
        "de <b>~190.000 millones de dólares</b> para el año calendario 2026 —tres veces el de hace dos "
        "años—. [HECHO]")]
    o += [ch("06_margenes", 15.2), sp(2)]
    o += [M.p("Ese es el ADN de la tesis. Durante una década Microsoft fue una máquina de márgenes "
        "crecientes y capital ligero (asset-light: un negocio que crece sin necesitar mucho capital "
        "físico) — software puro, coste marginal casi nulo, retornos sobre el capital invertido (ROIC) "
        "de récord. La ola de la IA está <b>mutando</b> ese organismo —de asset-light a semi-industrial, "
        "como una especie que cambia de hábitat— y con él las métricas que definían su calidad: el ROIC "
        "baja, el flujo de caja libre (FCF: el efectivo que queda tras pagar las operaciones y la "
        "inversión) se comprime, la caja neta se agota. Nada de eso rompe el negocio; todo eso "
        "<i>cambia su naturaleza</i> mientras dure el súper-ciclo de inversión. La pregunta de toda la "
        "tesis es si ese cambio es una muda —una fase incómoda de la que se sale más fuerte, con el ROIC "
        "volviendo a subir cuando el capex encuentre su techo— o un callejón evolutivo sin salida: "
        "capital atrapado en activos que se deprecian antes de monetizar. El moat (foso competitivo: la "
        "ventaja estructural que protege las ganancias de la competencia) dice muda; el precio, "
        "castigado, todavía apuesta por el callejón sin salida.")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def s2():
    o = M.flag_titulo("§2 · Historia de mi posición", "Un ancla de cartera, a la que el mercado puso precio de rebaja")
    o += [M.p("Toda cartera necesita raíces, no solo ramas. Microsoft es una de las <b>empresas ancla</b> "
        "de mi marco Quality Growth —junto a Visa y MercadoLibre, es una de las referencias contra las "
        "que calibro la calidad de todo lo demás—. Es la clase de negocio que se quiere <i>tener</i> y "
        "dejar crecer durante una década, no negociar: fosos (moats, ventajas estructurales que protegen "
        "las ganancias) entre los más anchos del planeta, gestión de élite, retornos de récord. "
        "[contexto propio]")]
    o += [M.p("La diferencia con Duolingo —la tesis anterior— es el eje precio, no el eje calidad. Ahí el "
        "veredicto fue VIGILAR: gran negocio, pero el descuento quedaba corto y el moat estaba bajo "
        "ataque no refutado — una raíz sana, pero el suelo alrededor todavía en duda. "
        f"Aquí el veredicto frío es <b>{D.VEREDICTO}</b>: el mercado castigó a Microsoft un ~20% por el "
        f"shock del capex (el anuncio de gasto en infraestructura), y a US${int(D.PRECIO)} el margen de "
        f"seguridad —MoS, el colchón entre lo que pagás y lo que vale el negocio— (+{D.MOS_HOY}% vs un "
        f"valor intrínseco de US${D.PWFV}) supera con holgura el 15% que exige su tier Núcleo. La "
        "disciplina de val-mos (mi sistema propio de valoración) manda comprar por tramos, medir la "
        "caída (<i>drawdown</i>) desde el máximo —no desde lo que costó—, y ampliar solo cuando el "
        "fundamental confirme la tesis, no por cariño al nombre.")]
    o += [M.p(f"Mi posición operativa, por tanto: <b>construir posición por tramos</b>, como quien riega "
        f"un árbol ya plantado en vez de sembrar uno nuevo de golpe. Tramo inicial {D.TRAMO_INI} del NAV "
        f"<b>ya</b> (el margen de seguridad y el detector de trampas lo habilitan), y ampliar a "
        f"{D.TECHO_POS} solo cuando aparezca la señal verificable de que el capex hace plateau (toca "
        f"techo y deja de crecer) y el flujo de caja libre se descomprime (FY27-28). Por ser una «herida» "
        f"en parte autoinfligida —la decisión de gastar $190B es de la gestión, no un golpe del "
        f"mercado—, aplica la regla híbrida: entro ahora, pero el grueso de la posición espera la "
        f"confirmación del retorno, no la promesa.")]
    o += [M.callout("PAUSA REFLEXIVA",
        "El riesgo psicológico de un ancla no es el de una apuesta: nadie compra Microsoft por FOMO "
        "(miedo a quedarse afuera). El riesgo es sobredimensionar «porque nunca me voy a arrepentir de "
        "tener Microsoft» — el mismo instinto que lleva a un jardinero a regar de más una planta sana "
        "solo porque ya confía en ella. Pero la calidad no exime del precio: comprar el mejor negocio "
        "del mundo a 40 veces sus ganancias del dueño (owner earnings) sigue siendo una inversión "
        "mediocre. Esta tesis compra a ~23 veces porque el mercado confundió una fase de inversión con "
        "un deterioro — no porque el nombre lo merezca todo. Si ese descuento desaparece antes de "
        "completar la posición, dejo de comprar. No persigo el nombre; persigo el precio correcto para "
        "el nombre correcto.")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def s3():
    o = M.flag_titulo("§3 · El modelo de negocio en dos minutos", "La prueba de Lynch: tres segmentos, un flujo de licencias")
    o += [M.p("<b>La prueba de los dos minutos, a lo Peter Lynch.</b> Si tuvieras que explicarle este "
        "negocio a alguien en el tiempo que dura un semáforo, dirías: Microsoft le vende software a casi "
        "todas las empresas del mundo, casi siempre por suscripción, y les alquila la computadora "
        "gigante donde corren sus programas (la nube). Reporta en tres segmentos: <b>Productivity &amp; "
        "Business Processes</b> (Microsoft 365, LinkedIn, Dynamics — el software con el que la gente "
        "trabaja), <b>Intelligent Cloud</b> (Azure y los servidores — la infraestructura de fondo), y "
        "<b>More Personal Computing</b> (Windows, dispositivos, gaming y búsqueda — lo que queda del "
        "viejo Microsoft, el de antes de Nadella). Cobra por adelantado, con contratos plurianuales, lo "
        "que le da un backlog (compromisos de ingresos futuros ya firmados) de <b>633.000 millones de "
        "dólares</b> — 2,3 veces sus ingresos anuales. [HECHO] Es, en esencia, un club de suscripción "
        "empresarial con los márgenes de una empresa de software.")]
    o += [ch("02_segmentos", 15.2), sp(2)]
    o += [M.p("<b>La mecánica del margen es la clave del trimestre, y conviene mirarla como un "
        "balancín.</b> El segmento de productividad (donde vive Copilot, vendido como un complemento de "
        "alto margen sobre una infraestructura que ya está pagada y amortizada) <i>expande</i> su margen "
        "operativo al 60%. El segmento de nube (donde vive Azure, y donde pega de lleno la depreciación "
        "de los nuevos centros de datos de IA) es el <b>único que se comprime</b>: −180 puntos básicos, "
        "al 39,7%. Y sin embargo, el margen operativo <i>consolidado</i> —el balancín completo— está en "
        "máximo histórico (46,3%), porque el mix de negocio se desplaza hacia el software de mayor "
        "margen más rápido de lo que se comprime la nube. [HECHO] Es una empresa que absorbe la mayor "
        "ola de gasto de capital de su historia sin que su rentabilidad global se resienta — el "
        "equivalente corporativo de correr cuesta arriba sin perder el aliento.")]
    o += [ch("03_capex_fcf", 15.2), sp(2)]
    o += [M.p("<b>La tensión de la tesis, en un solo gráfico.</b> El capex (gasto de capital: la "
        "inversión en activos físicos de larga duración, aquí sobre todo chips y centros de datos) saltó "
        "de 20.600 millones (FY21) a 97.200 millones (últimos doce meses), y la guía apunta a ~190.000 "
        "millones para 2026 (contando arrendamientos financieros; ~107.000 millones de capex «puro»). "
        "Como consecuencia, el margen de flujo de caja libre (FCF: el efectivo que sobra después de "
        "pagar el negocio y toda la inversión) se comprimió del 33% al 23% —la primera compresión "
        "estructural de la era moderna de la empresa—. Pero cuidado con la lectura superficial: el "
        "<b>flujo de caja operativo</b> (la caja que genera el negocio antes de invertir) sigue creciendo "
        "con fuerza (+25%). No es que Microsoft gane menos caja; es que está eligiendo <b>reinvertirla</b> "
        "en vez de guardarla. Esa distinción —¿elección inteligente o exceso de confianza?— es todo el "
        "debate de valoración del §9.")]
    o += [ch("04_azure_ai", 15.0)]
    o += [M.p("<b>Economía de cohortes (cómo se comporta un mismo cliente con el tiempo), en el "
        "arquetipo del software.</b> Microsoft no divulga la retención neta de ingresos (NRR, cuánto "
        "crece el gasto de un mismo cliente año a año) de forma explícita —un punto ciego que hay que "
        "declarar—, pero los indicadores indirectos (proxies) son elocuentes: Microsoft 365 Consumer "
        "crece ingresos +33% con suscriptores creciendo solo +7%, señal de fuerte expansión del ingreso "
        "promedio por usuario (ARPU) vía mejor mix de producto (planes E5 + Copilot); y los <b>asientos "
        "pagados de Copilot pasaron de ~15 a &gt;20 millones en un trimestre</b> (+250% interanual), "
        "aunque todavía son solo ~4,4% de la base de 446 millones. La palanca de valor no es vender más "
        "asientos base —casi saturados ya en las grandes cuentas— sino la <b>penetración de Copilot</b> "
        "dentro de los asientos que ya tiene: cada 10 puntos de conversión valen ~16.000 millones anuales "
        "de ingreso recurrente con un margen de ~90%. [HECHO/INFERENCIA]")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def s4():
    o = M.flag_titulo("§4 · Las once reglas de Seilern con bisturí", "El output del sistema qg-seilern, sin maquillar")
    o += [M.p(f"<i>{DISCLAIMER}</i>", "nota")]
    o += [M.p(f"Microsoft pasa los <b>siete knock-outs</b> (los filtros eliminatorios previos del "
        f"sistema: estructura societaria limpia, sin acciones de voto dual tipo VIE, ROIC muy por encima "
        f"del coste de capital) con distinción, y —notable— con <b>dilución neta negativa</b>: las "
        f"recompras de acciones superan la emisión, así que la compensación en acciones (SBC) no diluye "
        f"a los accionistas actuales. Sobre las once reglas ponderadas obtiene <b>{D.es(D.SCORE_QG,1)}/100 "
        f"(raw {D.es(D.RAW_QG,1)}/125), tier {D.TIER_QG}</b> —confirma su estatus de empresa ancla, la "
        f"que sirve de vara para medir a las demás—. Es un negocio <b>excepcional</b>, y la nota queda "
        f"por debajo del techo por deméritos <b>reales y honestos</b>, no por ruido, todos concentrados "
        f"en un mismo punto: la mutación hacia la IA descrita en el §1.")]
    o += [M.p("<b>R7 · Capital / ROIC 7,5/10 — la mutación del modelo, otra vez.</b> El retorno sobre el "
        "capital invertido (ROIC) absoluto es de élite (31% con fondo de comercio incluido, 47% sin él), "
        "pero la <b>trayectoria es descendente</b> (44%→31% en dos años) y la intensidad de capital se "
        "disparó (capex sobre ventas del 12% al 30%). Una empresa que hoy se capitaliza como una utility "
        "(un negocio de infraestructura pesada y retornos regulados) no puede puntuar alto en «baja "
        "intensidad de capital», por muy extraordinario que siga siendo su retorno absoluto. El sistema "
        "no regala puntos por reputación. [HECHO/INFERENCIA]")]
    o += [ch("11_roic", 14.6), sp(2)]
    o += [M.p("<b>Nota de ROIC incremental (R7) — el retorno sobre cada dólar NUEVO invertido, no sobre "
        "el stock acumulado.</b> Es la variable que decide toda la tesis. El capex de IA deprime el ROIC "
        "<i>incremental</i> de corto plazo por pura mecánica contable: el capital invertido (el "
        "denominador de la fórmula) explota —el activo fijo neto casi se triplicó, de 95.600 a 283.200 "
        "millones en menos de tres años— antes de que la utilidad operativa neta del negocio de IA (el "
        "numerador, NOPAT) empiece a monetizar. Análisis honesto: <b>hoy los estados financieros muestran "
        "solo el lado del costo</b> (ROIC y FCF bajando = HECHO); el lado del retorno (monetización de IA "
        "a escala) es todavía promesa, no hecho contable. Señales que apoyan que es reinversión racional "
        "y no destrucción de valor: Azure acelerando a +40%, la IA facturando +123%, y una restricción de "
        "<i>oferta</i> (no de demanda: sobra quien quiera comprar, falta capacidad para vender). El "
        "veredicto se resuelve en ~8 trimestres. [INFERENCIA]")]
    o += [M.p("<b>Precedente propio: esta partida ya se jugó una vez, y Microsoft la ganó.</b> El patrón "
        "«reinversión ahora, retorno después» no es una promesa sin historial — Microsoft ya lo ejecutó "
        "en el ciclo de construcción de Azure. Entre FY2016 y FY2019 las adiciones a propiedad y equipo "
        "subieron de 8.343 a 13.925 millones de dólares (+68% acumulado en tres años) mientras Azure "
        "crecía +90% (FY17), +76% (FY18) y +64% (FY19) —desacelerando en tasa, pero no en dólares—. "
        "[HECHO, 10-K FY2019, SEC EDGAR] El margen operativo de Intelligent Cloud, lejos de derrumbarse, "
        "pasó de 35,7% (FY18) a 37,9% (FY20) pese al capex creciente. [HECHO, 8-K FY2020] El retorno "
        "agregado llegó con el rezago que hoy se le vuelve a pedir: el ROIC consolidado saltó a máximos "
        "históricos de 43,4% (FY2020) y 45,6% (FY2021), tres a cinco años después del pico de inversión "
        "de 2018-2019. [HECHO, stock-analysis-on.net sobre datos de 10-K] Es el mismo patrón temporal "
        "—capex sube, margen aguanta, ROIC vuelve a subir con rezago— que el capex de IA le exige repetir "
        "hoy; no es garantía de que el resultado se repita, pero sí un antecedente verificable propio, no "
        "una analogía prestada de otra empresa.")]
    o += [M.p("<b>R4 · Moat 9,5/10 — la regla estrella, con un asterisco.</b> El foso (moat: la ventaja "
        "estructural que mantiene a raya a la competencia) es un <b>archipiélago de islas "
        "interconectadas</b>: costes de cambio (el trabajo de migrar formatos y flujos de Microsoft 365), "
        "efecto red (Teams, y el grafo social de 1.300 millones de nodos de LinkedIn, donde cada usuario "
        "nuevo hace la red más valiosa para todos los demás), y una escala de capital que casi nadie "
        "puede replicar. Pero no llega al máximo porque el <b>frente de la IA está genuinamente bajo "
        "ataque</b>: Microsoft no lidera en modelos (Anthropic domina el mercado de API empresarial con "
        "~35% de cuota), OpenAI dejó de ser proveedor cautivo (murió el derecho de primera opción sobre "
        "su cómputo), y el foso de Microsoft en IA es de <i>distribución</i> —el canal por el que llega "
        "el producto—, no de tecnología. Se detalla en el §5. [HECHO/INFERENCIA]")]
    o += [M.p("<b>R9 · Transparencia 8/10 — el beneficio por acción (EPS) titular está contaminado.</b> "
        "El semáforo mecánico daría 10 (flujo de caja operativo sobre beneficio de 1,36x, devengos "
        "—accruals— negativos, sin re-expresión de resultados). Se ajusta a la baja porque el beneficio "
        "neto titular está inflado en ~9.500 millones por una <b>ganancia no operativa de la "
        "recapitalización de OpenAI</b> (una revalorización contable en libros, sin efectivo real de por "
        "medio), y porque la participación en OpenAI introduce ruido no operativo creciente "
        "(revalorizaciones periódicas más pérdidas por el método de participación patrimonial, que se "
        "aceleran con la quema de caja —<i>burn</i>— de OpenAI). Regla de esta tesis: valorar por ingreso "
        "operativo y flujo de caja, nunca por el EPS titular. [HECHO]")]
    o += [ch("05_owner_earnings", 14.6), sp(2)]
    o += [M.p("<b>Lo que sostiene el score de élite:</b> R3 liderazgo 9,5/10 (#1 en productividad, "
        "seguridad y LinkedIn; #2 en cloud ganando cuota), R6 diversificación 9/10, R1 escalabilidad "
        "9/10 (crecer sin que los costos crezcan al mismo ritmo), R8 balance 8,5/10. Calibrada contra las "
        "anclas del sistema, Microsoft queda <b>a la altura de Visa</b> en calidad pura de negocio, pero "
        "con un flanco que Visa no tiene: la mutación de su propio modelo económico, descrita en el §1. "
        "El debate de si comprar o no ya no es de calidad — es de precio, y ese es el eje del resto del "
        "documento.")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def s5():
    o = M.flag_titulo("§5 · El moat", "Un archipiélago de fosos — y el único que está bajo ataque")
    o += [M.p("El moat de Microsoft no es un foso: es un archipiélago de fosos interconectados que se "
        "refuerzan entre sí, como un sistema de islas defendidas por la misma flota. Ordenados por "
        "anchura (medida en las Cinco Fuerzas de Porter del §7, un marco que mide qué tan protegido está "
        "un negocio de la competencia — cuanto menor el número, más ancho el foso):")]
    o += [M.tabla([
        ["Foso", "Fuente de la ventaja", "Anchura (Porter /25)", "¿Bajo ataque?"],
        ["LinkedIn", "Efecto red + datos: 1.300M de perfiles, monopolio natural", "8 — máxima", "No"],
        ["Productividad (M365)", "Costes de cambio (formatos, macros, hábitos) + bundle", "9 — máxima", "No"],
        ["Cloud (Azure)", "Switching costs empresariales + escala de capital + híbrido", "14 — sólida", "Rivalidad sube"],
        ["IA", "Distribución (Copilot sobre 446M asientos), NO el modelo", "14 — de distribución", "SÍ — el frente clave"],
        ["Gaming", "Escala de contenido (COD, Halo, Minecraft) + Game Pass", "15 — de contenido", "Plataforma débil"],
    ], [3.6*cm, 5.9*cm, 3.4*cm, 3.0*cm])]
    o += [M.p("<b>La clave de la tesis competitiva, en términos de ajedrez.</b> Los dos motores de valor "
        "—Microsoft 365 y LinkedIn— controlan el centro del tablero (8-9/25, los <b>fosos más anchos del "
        "mundo cotizado</b>) y nadie amenaza esa posición: no hay rival que vaya a reunir simultáneamente "
        "a mil millones de profesionales, ni a reescribir cuarenta años de compatibilidad de formatos de "
        "Office. El frente disputado —la IA— es, hoy, apenas un peón en el flanco: <i>la menor "
        "contribución al beneficio</i> de los cinco. Esto es una estructura envidiable: Microsoft domina "
        "donde gana dinero y pelea de igual a igual donde está la opcionalidad futura, sin arriesgar el "
        "centro del tablero para hacerlo. [INFERENCIA]")]
    o += [M.callout("PAUSA REFLEXIVA",
        "La lección de 2026 es que en la guerra de la inteligencia artificial, la distribución vence al "
        "modelo — el canal le gana a la tecnología. El modelo se comoditiza (se convierte en un producto "
        "genérico e intercambiable) —OpenAI perdió su exclusividad, Anthropic lidera el mercado de API "
        "empresarial, Gemini sube, los modelos de código abierto (open-weight) presionan por abajo—. "
        "Microsoft lo sabía, y se reposicionó de «dueño de OpenAI» a «capa de distribución neutral»: "
        "Azure aloja a OpenAI <i>y</i> a sus rivales por igual, como un puerto que cobra peaje a todos "
        "los barcos sin importar bandera, y Copilot inyecta la IA en 446 millones de asientos que ningún "
        "modelo genérico alcanza por sí solo. Su foso de IA es, en el fondo, el mismo foso de Microsoft "
        "365 —la distribución—, no la tecnología del transformer (la arquitectura detrás de los modelos "
        "de lenguaje). La pregunta incómoda: ¿es ese moat de distribución tan durable como el efecto red "
        "de LinkedIn, o más frágil de lo que parece si la IA se vuelve un commodity que cualquiera "
        "integra sin necesitar a Microsoft en el medio? La vigilancia activa vive en el §12.")]
    o += [M.p("<b>El talón de Aquiles del moat.</b> El foso de distribución de IA descansa, en parte, "
        "sobre un solo contrato: el 45% del backlog (ingresos comerciales comprometidos, RPO) de 633.000 "
        "millones depende de OpenAI —una empresa que pierde ~14.000 millones al año, se comprometió a "
        "1,4 billones de dólares de cómputo que hoy no puede pagar, y ya diversifica hacia Oracle y AWS "
        "gracias a que la propia Microsoft le devolvió la libertad de cómputo en la reestructuración de "
        "2025—. Es la grieta clásica de cualquier gigante: la fortaleza está construida sobre roca en "
        "casi todos lados, menos en el punto exacto donde depende de que un tercero —y encima uno que "
        "quema caja— siga cumpliendo su palabra. Si OpenAI tropieza, ese backlog se revela más blando de "
        "lo que su tamaño sugiere. [HECHO/INFERENCIA de terceros]")]
    o += [ch("19_rpo", 15.2)]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def s6():
    o = M.flag_titulo("§6 · El campo de batalla competitivo", "Seis frentes, y el enemigo número uno no es un competidor")
    o += [M.p("Microsoft libra seis batallas distintas al mismo tiempo, en tableros con reglas "
        "distintas, y su posición varía enormemente entre ellas:")]
    o += [M.tabla([
        ["Frente", "Rival #1", "Posición de Microsoft"],
        ["Cloud (IaaS/PaaS)", "AWS (~28-30%)", "#2 (~21-25%) ganando 1-2 pp/año; pero AWS re-aceleró (+28%) y Google explotó (+63%)"],
        ["Productividad", "Google Workspace", "#1 empresa (~58%, 446M asientos); 58% de los que migran van Workspace→M365"],
        ["IA (modelo)", "Anthropic / Google", "Detrás: Anthropic ~35% del API empresarial. Microsoft lidera en DISTRIBUCIÓN, no en modelo"],
        ["Seguridad", "(fragmentado)", "#1 mundial por ingresos (~$37B run-rate, &gt;1,5M clientes)"],
        ["LinkedIn", "(ninguno directo)", "Cuasi-monopolio profesional (1.300M miembros)"],
        ["Gaming", "Sony PlayStation", "#3 en consolas (PS5 94M vs Xbox 34M); pivote a editor multiplataforma"],
    ], [3.0*cm, 3.2*cm, 10.2*cm])]
    o += [M.p("<b>La saturación del pastel de la nube, cuantificada.</b> Synergy Research ubica a los "
        "tres hiperescaladores (los tres grandes proveedores de nube) en conjunto en 63-68% de un mercado "
        "de infraestructura cloud de US$395.000 millones en 2025 (Azure ~20-23%, AWS ~29-33%, GCP "
        "~12-13%). [HECHO, Synergy Research] El espacio de ganancia incremental de cuota para Azure ya es "
        "limitado y depende de quitarle terreno a AWS o GCP —una guerra de trincheras, metro a metro—, "
        "no de conquistar mercado virgen sin explotar. [INFERENCIA] En seguridad, el propio Nadella "
        "describe el salto de ingresos de US$10.000 millones (2021) a US$20.000 millones (2023) como "
        "«consolidación» de clientes existentes sobre el stack de Microsoft (Entra, Defender, Purview) "
        "—venta cruzada (cross-sell) dentro de la base instalada, no conquista de clientes nuevos—, el "
        "mismo patrón de crecimiento por penetración, no por mercado nuevo, que se exige documentar en "
        "Copilot (§3). [HECHO, cita Nadella]")]
    o += [M.p("<b>El frente que decide la década es la IA</b>, y ahí Microsoft juega una partida "
        "distinta a la que el mercado teme. No compite por tener el mejor modelo —esa corona hoy la "
        "lleva Anthropic o Google, según qué prueba (benchmark) se mire—; compite por <b>distribuir</b> "
        "la IA a través de su base instalada, como un mayorista que no necesita fabricar el mejor "
        "producto, solo tener la mejor red de tiendas. Azure es la capa neutral que aloja todos los "
        "modelos; Copilot es el canal que los pone frente a 446 millones de trabajadores. La rivalidad "
        "en el modelo es feroz (5/5 en la escala de Porter, máxima intensidad), pero es exactamente el "
        "eslabón de la cadena donde Microsoft <i>menos</i> necesita ganar la pelea para ganar la guerra.")]
    o += [M.p("<b>La amenaza número uno no es un competidor — es el árbitro que puede cambiar las reglas "
        "a mitad de partido.</b> El mismo mecanismo que construye el foso —agrupar Microsoft 365, Teams, "
        "Azure, Copilot y seguridad en un paquete (bundle) irresistible— es el que atrae simultáneamente "
        "a la FTC estadounidense (investigación ampliándose sobre licenciamiento cloud y empaquetado), a "
        "la Unión Europea (evaluando si Azure es un «gatekeeper», un guardián de acceso, bajo la ley de "
        "mercados digitales, DMA) y a la CMA británica. La estructura de Porter dice «foso fuerte»; el "
        "vector de riesgo real es que un remedio antitrust obligue a <b>desagrupar</b> lo que hoy va "
        "junto —como forzar a separar las piezas de un reloj que solo funciona ensamblado—. La exposición "
        "legal <i>cuantificada</i> es trivial ($541 millones devengados en provisiones); el riesgo real "
        "es <b>estratégico</b>, no de multa. [HECHO]")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def s7():
    o = M.flag_titulo("§7 · Porter: fosos por segmento y el mecanismo de inmunidad", "Cinco Fuerzas foso por foso, y una contradicción que ilumina")
    o += [ch("12_porter", 14.8), sp(2)]
    o += [M.p("A diferencia de un negocio de un solo producto, las Cinco Fuerzas de Porter (el marco "
        "que mide cuánto presiona la competencia sobre las ganancias de un negocio) se puntúan en "
        "Microsoft <b>por segmento</b> (menor = mejor foso). El resultado es un archipiélago de climas "
        "distintos: desde LinkedIn (8/25, un cuasi-monopolio) y Microsoft 365 (9/25, la joya de la "
        "corona) hasta los frentes disputados de cloud e IA (14/25) y gaming (15/25). El promedio "
        "ponderado por contribución al valor —donde productividad y cloud pesan mucho más que gaming— es "
        "<b>~11,5/25: una estructura competitiva sólida a excelente</b>. [análisis propio]")]
    o += [M.callout("PAUSA REFLEXIVA",
        "Contradicción Porter↔Seilern: en el segmento de IA la fuerza «rivalidad» puntúa 5/5 (máxima "
        "adversidad — Anthropic, Google, OpenAI, modelos de código abierto) y sin embargo el moat global "
        "de Microsoft (regla R4) puntúa 9,5/10. ¿Cómo puede ser inmune a una fuerza que en teoría debería "
        "destrozarla? El mecanismo es el mismo que protege a ciertas especies de un depredador feroz: "
        "viven en un nicho distinto. Las flechas adversas de Porter atacan el <b>modelo de IA</b>, un "
        "terreno donde Microsoft deliberadamente <i>no</i> apostó su foso. Su ventaja no es tener el "
        "mejor <i>transformer</i> (la arquitectura de los modelos de lenguaje) —cede ese terreno sin "
        "pelear—, sino <b>distribuir cualquier modelo</b> a través de Azure y Copilot sobre 446 millones "
        "de asientos. La rivalidad de modelos pasa de largo por el eje equivocado, como un depredador "
        "terrestre frente a una presa que vive en el agua. ¿Es estructural ese mecanismo, o es solo "
        "suerte de posicionamiento? Mientras la distribución empresarial siga siendo la barrera real de "
        "adopción de IA —y hoy lo es—, sí es estructural. Si ese mecanismo fallara (si la IA se "
        "distribuyera sola, sin necesitar la base instalada de un gigante), el moat de IA se derrumbaría "
        "y con él una fracción de la opcionalidad. Por eso el frente de IA es a la vez el de mayor "
        "<i>upside</i> (potencial de subida) y el más vigilado.")]
    o += [M.p("Este es el rasgo distintivo de las empresas verdaderamente dominantes: son inmunes a "
        "fuerzas que arrasan con sus competidores porque compiten en un eje distinto por completo. Un "
        "rival de modelos puros (OpenAI, Anthropic) tiene la mejor tecnología y ningún foso de "
        "distribución ni de diversificación de ingresos; Microsoft tiene una tecnología de segunda fila "
        "y el mejor canal de distribución del mundo empresarial. En la historia de la tecnología "
        "corporativa, casi siempre gana el canal, no el mejor producto. [INFERENCIA]")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def s8():
    o = M.flag_titulo("§8 · TAM, SAM, SOM, runway y catalizadores", "El mercado direccionable más amplio del mundo cotizado")
    o += [ch("13_tam", 15.2), sp(2)]
    o += [M.p("Microsoft es el único jugador presente simultáneamente en las cinco capas de la "
        "tecnología empresarial —infraestructura, plataforma, aplicación de software como servicio "
        "(SaaS), IA y seguridad— más publicidad y gaming. El mercado total direccionable (TAM: el tamaño "
        "de la oportunidad si capturara el 100% de cada mercado en el que participa) que toca ronda los "
        "<b>2,4 billones de dólares en 2026</b>, camino de ~3,75 billones en 2030 — el territorio más "
        "amplio de cualquier empresa cotizada. [INFERENCIA sobre reports] Y es líder o número uno en "
        "cuatro de esos seis mercados, con penetración todavía baja en el más grande y de mayor "
        "crecimiento: la IA empresarial — la última frontera sin colonizar.")]
    o += [M.p("<b>El TAM agregado, desglosado por fuente.</b> Gartner proyecta un gasto mundial en TI de "
        "US$6,31 billones en 2026 [HECHO, Gartner, abr-2026]; IDC proyecta que el gasto en nube pública "
        "supere el billón de dólares en 2026, duplicándose hacia 2029 [HECHO, IDC]; y Gartner proyecta un "
        "gasto mundial en seguridad de la información de US$244.200 millones en 2026 [HECHO, Gartner]. "
        "Sobre los US$281.700 millones de ingresos FY2025 de Microsoft, la penetración real es de un solo "
        "dígito bajo sobre el gasto total en TI, y de un dígito medio sobre nube+seguridad combinadas. "
        "[INFERENCIA, cálculo propio] La cifra agregada de «2,4 billones» del párrafo anterior no es, por "
        "tanto, un TAM inflado sin ancla: es consistente con sumar TI+nube+seguridad+publicidad+gaming de "
        "fuentes independientes, y en ninguna de las capas individuales Microsoft se acerca a saturar el "
        "mercado direccionable.")]
    o += [M.p("<b>Verificación de consistencia con el DCF.</b> El doble método (top-down desde reports y "
        "bottom-up desde los ingresos reales de Microsoft) <b>reconcilia</b> en cuatro de seis mercados "
        "(seguridad, publicidad, gaming casi perfectos; cloud dentro de banda). La única divergencia "
        "grande es la IA empresarial, donde el TAM top-down (255.000 millones camino de 1,2 billones en "
        "2030) es enorme y la penetración de Microsoft es todavía baja (~37.000 millones de run-rate) — "
        "precisamente donde vive la opcionalidad de crecimiento. El escenario base de valoración no exige "
        "capturar ese TAM: le basta con que el capex haga plateau. [INFERENCIA]")]
    o += [M.p("<b>Catalizadores 2026–2028, por impacto en el valor:</b> (1) <b>Monetización de "
        "Copilot</b> —de 4,4% a 15-20% de conversión sobre 446M asientos = ~25-32.000 millones "
        "incrementales de margen ~90%—; (2) <b>digestión del capex → descompresión del FCF</b> —el "
        "catalizador no es más gasto sino su <i>plateau</i> en FY27-28, que liberaría violentamente el "
        "flujo de caja libre y forzaría una re-rating—; (3) <b>consolidación de seguridad</b> en la "
        "plataforma (ya es el mayor vendor del mundo); (4) <b>agentes de IA</b> facturados por consumo "
        "(amplía el TAM de «asientos» a «trabajo automatizado»); (5) LinkedIn y publicidad conversacional. "
        "El punto débil honesto: gaming (en declive) y Bing en búsqueda son los flancos flojos. [HECHO]")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def s9():
    o = M.flag_titulo("§9 · Valoración multi-método", "El output de val-mos: detector, PWFV-Valor, zonas — y por qué el FCF engaña")
    o += [M.p("<b>Paso 0 — detector de trampas (corre antes de valorar): PASA.</b> De las seis señales "
        "estructurales de trampa de valor, Microsoft no dispara ninguna plena, pero enciende <b>dos "
        "alertas serias de vigilancia</b>: (1) el ROIC en descenso —pero es de fase de inversión, no "
        "secular: el margen operativo <i>expande</i> a máximos—; y (2) la deuda «oculta» en leases —los "
        "arrendamientos financieros se triplicaron y hay 196.600 millones en leases de datacenter aún no "
        "iniciados, fuera del capex de caja—. Ninguna es un veto: Microsoft sigue en caja neta y es AAA de "
        "facto. <b>No es una trampa; es compresión de FCF/ROIC por fase de capex.</b> La única forma de "
        "que se convierta en trampa es que el ROIC incremental del capex quede estructuralmente por debajo "
        "del coste de capital. [val-mos]")]
    o += [M.p("<b>Corroboración independiente de la restricción de oferta.</b> El argumento de "
        "«restringido por capacidad, no por demanda» no descansa solo en la palabra de la propia "
        "Microsoft: TSMC advirtió en 2026 a Nvidia y Broadcom que no puede satisfacer toda la demanda de "
        "nodos avanzados por saturación de capacidad [HECHO, Computing.co.uk, abr-2026], y Nvidia describió "
        "sus GPUs de nube como «sold out», con ~US$500.000 millones en pedidos acumulados 2025-2026 "
        "[HECHO, transcripciones Nvidia Q1/Q3 FY26]. El propio Microsoft firmó US$107.000 millones en "
        "nuevos compromisos de infraestructura plurianual en un solo trimestre, y ha contratado 40 GW de "
        "capacidad energética renovable —19 GW ya operativos—, incluido el mayor PPA corporativo de la "
        "historia con Brookfield (10,5 GW adicionales 2026-2030). [HECHO, comunicado FY26 / "
        "DataCenterDynamics / Sustainability Magazine] Estos compromisos físicos y energéticos son "
        "verificables fuera de la narrativa de la propia compañía y son consistentes con «restringido por "
        "capacidad»: nadie firma 40 GW de energía ni sub-utiliza silicio que un proveedor externo (TSMC) "
        "dice no poder abastecer del todo.")]
    o += [ch("10_dcf_inverso", 14.8), sp(2)]
    o += [M.p("<b>Paso 1 — DCF inverso (la disciplina).</b> ¿Qué crecimiento descuenta el precio de hoy? "
        "Fijando el WACC base (8%) y el margen base, US$384 despeja un crecimiento de owner earnings de "
        "solo <b>~7,7% anual durante una década</b>. Eso está por debajo del CAGR histórico de ingresos "
        "(+13%), muy por debajo del crecimiento implícito de Azure (+40%) y de la IA (+123%), y hasta por "
        "debajo de mi propio escenario conservador (+8%). <b>El precio no descuenta crecimiento heroico; "
        "descuenta una desaceleración fuerte y/o que el capex destruya retorno.</b> Esa modestia de "
        "expectativas es, precisamente, la fuente de la oportunidad.")]
    o += [M.p("<b>Paso 2 — PWFV-Valor (el ancla de valoración probabilística) y el error de lectura del "
        "mercado.</b> El precio sobre flujo de caja libre (P/FCF) titular de 39x «grita caro» — y es la "
        "trampa óptica que hay que desarmar antes de seguir. Ese número es un <b>artefacto del capex de "
        "crecimiento</b>: el flujo de caja libre reportado (73.000 millones) resta el capex <i>total</i>, "
        "incluyendo la parte que expande capacidad futura, no solo la que repone lo existente. La "
        "métrica honesta del dueño (owner earnings: lo que realmente le queda al accionista después de "
        "mantener el negocio, no de hacerlo crecer) resta solo el capex de <b>mantenimiento</b> (~14% de "
        "ventas, fijado alto por prudencia) más la compensación en acciones (SBC) íntegra: eso da un "
        "owner earnings normalizado de <b>~115.000 millones</b>, un rendimiento del dueño (owner-yield) "
        "de ~4% y un múltiplo precio/owner-earnings (P/OE) de ~23x — coherente con el P/E de 22,9x, no "
        "con el 39x titular que asusta a primera vista. El PWFV-Valor (valor justo ponderado por "
        "escenarios) resultante es <b>US$520/acción</b>; el valor sin ningún crecimiento futuro (EPV, "
        "Earnings Power Value) es US$210 — el piso duro del negocio, incluso si nunca creciera un dólar "
        "más.")]
    o += [ch("05_owner_earnings", 14.6)]
    o += [ch("07_dcf", 13.6)]
    o += [M.p("<b>Tabla de nueve supuestos del DCF (la historia disfrazada de matemática):</b>")]
    o += [M.tabla([
        ["#", "Supuesto", "Elección", "Etiqueta"],
        ["1", "Crec. owner earnings, años 1–5", "~12% (Azure sostiene +30-35%, IA escala, Copilot penetra)", "INFERENCIA"],
        ["2", "Crec. owner earnings, años 6–10", "~8% (hacia PIB + prima)", "SUPUESTO"],
        ["3", "Crecimiento terminal", "3,0% (&le; risk-free)", "SUPUESTO"],
        ["4", "WACC", f"{D.es(D.WACC,1)}% (CAPM ~10,1%, anclado al tier Núcleo por caja neta)", "INFERENCIA"],
        ["5", "Owner earnings normalizado", "~US$115B (CFO − capex mantenim. 14% − SBC)", "INFERENCIA"],
        ["6", "ROIC incremental del capex de IA", "sin probar; base asume que supera el WACC en FY27-28", "SUPUESTO"],
        ["7", "Dilución neta anual por SBC", "~0 (recompras &gt; emisión; acciones bajan)", "HECHO"],
        ["8", "Ajuste FX", "revenue global; +15% cc vs +18% reportado → FX es viento de cola leve", "INFERENCIA"],
        ["9", "Fase de capital allocation", "reinversión orgánica intensiva + dividendo + recompra $60B", "HECHO"],
    ], [0.7*cm, 4.6*cm, 8.4*cm, 2.7*cm], font_sz=7.8)]
    o += [ch("17_wacc", 13.4), sp(2)]
    o += [ch("18_sensibilidad", 14.4)]
    o += [M.p("<b>Sensibilidad y verificación de cordura.</b> Bajo los supuestos del escenario base, el "
        "valor aguanta entre US$444 y US$655 cruzando WACC × crecimiento terminal: <b>incluso en el "
        "cuadrante más severo (WACC 9%, terminal 2%) el valor —US$444— supera el precio de hoy "
        "(US$384)</b>. Los métodos secundarios convergen dentro del ±15%: EV/EBITDA 16x (vs mediana 19,5x) "
        "y forward P/E FY27 ~19,4x para un compounder que crece owner earnings a doble dígito. El "
        "consenso de Wall Street es Strong Buy con precio objetivo medio ~US$561-582 (+46%) — mi PWFV de "
        "$520 es <i>más conservador</i> que la calle.")]
    o += [ch("09_multiplos", 14.8), sp(2)]
    o += [M.p("<b>La compresión de múltiplo (de-rating) es el corazón de la oportunidad.</b> Microsoft "
        "cotiza a 22,9 veces beneficios frente a una mediana propia de ~31 veces: un ~28% por debajo de "
        "su propia historia, el múltiplo más barato desde 2022-23, consecuencia directa de la caída del "
        "20% desde el máximo. El mercado, en pocos meses, pasó de valorarla como «software de "
        "hipercrecimiento» a «infraestructura de capital pesado con retorno incierto» — el mismo "
        "negocio, dos etiquetas de precio radicalmente distintas. La pregunta de la tesis es si esa "
        "reclasificación es correcta (el retorno sobre el capital realmente se rompió) o exagerada (solo "
        "el múltiplo se rompió, mientras el negocio sigue reinvirtiendo a alto retorno). El mercado paga "
        "por lo que ve en el estado de resultados de hoy, no por lo que se está construyendo detrás de "
        "esa cifra — y el detector de trampas y el DCF inverso (el ejercicio de preguntarle al precio "
        "qué tiene que creer para tener razón) dicen que, esta vez, el mercado está mirando la cifra "
        "equivocada.")]
    o += [ch("08_zonas", 15.4)]
    o += [M.p(f"<b>Paso 3 — zonas y margen de seguridad exigido.</b> Ancladas al PWFV-Valor de "
        f"US${D.PWFV}: hoy US${int(D.PRECIO)} cae en la frontera <b>OPORTUNIDAD/GANGA</b>, con un "
        f"descuento del {D.es(-D.DCTO_HOY,1)}%. El tier Núcleo exige un margen de seguridad de solo "
        f"<b>{D.MOS_EXIG}%</b> (la calidad justifica un umbral más bajo que un negocio de menor tier); "
        f"a US${int(D.PRECIO)} el MoS es +{D.MOS_HOY}%, muy por encima. La asimetría es ~{D.es(D.ASIMETRIA,0)}:1 "
        f"(recorrido al valor ponderado +35%, al alcista +67%; caída al bajista solo hasta US${D.V_BEAR}, "
        f"que casi toca el precio de hoy, con suelo adicional en el mínimo de 52 semanas de US${int(D.LOW_52)}). "
        f"<b>Esta vez el regalo sí está en el precio.</b>")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def s10():
    o = M.flag_titulo("§10 · Gestión, cultura y gobernanza", "Operadores de clase mundial, sin apenas piel en el juego")
    o += [M.p("Satya Nadella es uno de los mejores gestores del mundo cotizado, y el cambio de cultura "
        "descrito en el §1 no fue cosmético — tiene una raíz personal verificable. Poco después de "
        "asumir el cargo en 2014, Nadella visitó en cuidados intensivos a su hijo Zain, que había nacido "
        "con parálisis cerebral severa, y notó que prácticamente todos los dispositivos médicos que lo "
        "mantenían con vida corrían sobre Windows conectado a la nube. En su libro <i>Hit Refresh</i> "
        "(2017) describe ese momento como el catalizador de su obsesión declarada: «empoderar a cada "
        "persona y organización del planeta para lograr más». Zain falleció en 2022 a los 26 años; su "
        "familia donó 15 millones de dólares al Seattle Children's Hospital. [HECHO, Fortune / GeekWire] "
        "Vale la pena precisar, por honestidad histórica, que el fin del sistema de evaluación forzada "
        "por curva (<i>stack ranking</i>, que obligaba a marcar a un porcentaje fijo de empleados como "
        "bajo rendimiento) ocurrió en noviembre de 2013 —bajo Ballmer, antes de Nadella—; lo que Nadella "
        "hizo fue profundizar ese giro, no iniciarlo, institucionalizándolo en cómo se evalúa y asciende "
        "a los managers. [HECHO, HBR / SHRM] Con esa cultura reconstruida, ejecutó una de las mayores "
        "transformaciones corporativas de la historia —el giro a la nube— sin destruir el núcleo de "
        "licencias, y llevó los ingresos de US$87.000 millones a US$282.000 millones con márgenes en "
        "expansión. Amy Hood, la CFO desde 2013, es la arquitecta de la disciplina de márgenes; su "
        "credibilidad es precisamente lo que hizo que la guía de capex moviera tanto la acción — el "
        "mercado le cree, y por eso duele tanto cuando sorprende. [HECHO/INFERENCIA]")]
    o += [ch("14_mgmt", 13.4), sp(2)]
    o += [M.p("<b>El primer ciclo real de calibración expone que la gerencia se quedó corta, no que "
        "exageró.</b> El 1 de mayo de 2025, en la <i>call</i> de resultados de FY25 Q4, Hood guio que el "
        "capex de FY2026 «crecería a una tasa menor que FY2025» y con mayor mezcla de activos de vida "
        "corta. [HECHO, CFO Dive, cita directa] La realidad divergió en la dirección contraria a la que "
        "un escéptico del capex temería: el capex del trimestre cerrado en marzo de 2026 subió 84% "
        "interanual, y el 29 de abril de 2026 Hood elevó la guía de capex 2026 a ~US$190.000 millones, "
        "+61% interanual —una aceleración, no la desaceleración prometida un año antes—. [HECHO, CNBC "
        "29-abr-2026] El primer dato real de «lo prometido vs. lo entregado» sugiere que la demanda "
        "superó lo que la propia gerencia proyectaba, no que la gerencia infló el gasto para justificarse "
        "ante el mercado. Es la diferencia entre un general que subestima al enemigo y uno que miente "
        "sobre sus propias tropas — la primera es mala previsión; la segunda sería mala fe. Todo lo "
        "verificable apunta a lo primero. [INFERENCIA razonable dado el patrón]")]
    o += [M.p("<b>Gobernanza estructural, notablemente sólida.</b> Microsoft tiene <b>una sola clase de "
        "acción, un voto por acción</b> —un contraste enorme con las estructuras de voto dual de Meta o "
        "Alphabet, donde los fundadores mandan aunque vendan la mayoría de su participación económica—, "
        "un consejo 91% independiente, un director independiente principal con poderes robustos, "
        "mecanismos de recuperación de bonos (<i>clawback</i>) y requisitos de tenencia de acciones "
        "(Nadella debe mantener 15 veces su salario en acciones propias). La cultura de rendición de "
        "cuentas (<i>accountability</i>) es genuina, no de relaciones públicas: tras las brechas de "
        "seguridad de 2024, Nadella pidió él mismo al consejo <b>reducir su propio bono en más del "
        "50%</b>. [HECHO]")]
    o += [M.p("<b>Los deméritos, sin maquillar.</b> Primero, la <b>propiedad de los directivos (insider "
        "ownership) es trivial</b>: Nadella posee el 0,012% de la empresa; todos los directivos como "
        "grupo, menos del 1%. No hay «piel en el juego» patrimonial —la alineación es 100% contractual "
        "(bonos y acciones concedidas), no de dueño que arriesga su propio patrimonio—. Para el marco "
        "Seilern, es un demérito de propiedad: son gestores-empleados excepcionales, no fundadores-dueños "
        "jugándose su propio capital. Segundo, <b>Nadella es a la vez CEO y presidente del consejo</b> "
        "—el mayor agujero de gobernanza de la tesis, mitigado pero no eliminado por el director "
        "independiente principal—. Tercero, la <b>recompra de acciones es mecánica, sin disciplina de "
        "precio</b>: compra más cuando la acción sube, no menos, el error clásico de comprar caro. "
        "[HECHO]")]
    o += [M.p("<b>Asignación de capital: el pivote que lo domina todo.</b> El historial es impecable — "
        "dividendo subiendo 21 años seguidos (con un payout conservador del 24% del beneficio), recompra "
        "de $60.000 millones autorizada, y fusiones y adquisiciones que crean valor bajo Nadella "
        "(LinkedIn y GitHub integrados, Activision sin deterioros contables; ningún castigo de valor "
        "—<i>write-off</i>— como los de la era pre-Nadella). Hay un precedente directo de esta misma "
        "apuesta, y vale la pena contarlo porque es el mismo patrón que hoy se repite con el capex de "
        "IA: en 2019, cuando «modelo de lenguaje grande» era todavía jerga académica y ChatGPT ni "
        "siquiera existía, Nadella decidió invertir 1.000 millones de dólares en una entonces oscura "
        "OpenAI. Él mismo reveló después que Bill Gates le advirtió que sería «como prender fuego a mil "
        "millones de dólares». [HECHO, Yahoo Finance] Microsoft invirtió igual, y después amplió la "
        "apuesta a US$2.000 millones (2021) y ~US$10.000 millones (enero de 2023) —antes de que el "
        "mercado supiera que la IA generativa importaría—. Para 2025, Microsoft ya había reconocido "
        "~US$9.500 millones de ingresos derivados de esa relación, y en el juicio Musk-OpenAI de 2026 "
        "Nadella reveló que la compañía apuntaba a un retorno de ~US$92.000 millones sobre esa inversión "
        "original. [HECHO, CNBC / Cryptopolitan, 2026] Toda la asignación de capital de hoy está "
        "subordinada a que ese mismo patrón —convicción contraintuitiva, resultado que tarda años en "
        "confirmarse— se repita con los <b>~190.000 millones al año en capex de IA</b>. Es la mayor "
        "apuesta de capital de la historia de la empresa, y a diferencia de la apuesta de OpenAI, su "
        "ROIC incremental está <b>sin probar todavía</b>. Si Azure/IA monetiza, es coherente y brutal; si "
        "la demanda decepciona o el silicio se deprecia antes de monetizar, es la mayor destrucción de "
        "valor potencial de la historia de Microsoft. <b>El jurado delibera, y su veredicto llega en los "
        "próximos ~8 trimestres.</b> [HECHO/INFERENCIA]")]
    o += [M.p("<b>La aritmética detrás de «M&amp;A que crea valor».</b> LinkedIn costó US$26.200 millones "
        "en 2016, cuando facturaba ~US$3.700 millones con un EBITDA ajustado de ~US$780 millones (margen "
        "~21%). [HECHO, 8-K LinkedIn 2016] Hoy factura entre US$15.000 y US$17.800 millones, según la "
        "fuente. [HECHO/INFERENCIA, MD&amp;A Microsoft FY24-25] Asumiendo un margen operativo ~35% "
        "(típico del segmento Productividad; LinkedIn no se divulga por separado), el ingreso operativo "
        "implícito hoy —~US$5.500-6.000 millones al año— equivale a un retorno anual sobre el precio de "
        "compra de ~21-23%: el desembolso ya se habría «repagado» en utilidad operativa acumulada en menos "
        "de una década. [SUPUESTO, margen estimado por no divulgarse por separado] GitHub costó US$7.500 "
        "millones en 2018, cuando facturaba US$200-300 millones; alcanzó un ARR de US$1.000 millones en "
        "2022 y ~US$2.000 millones en 2024 —un crecimiento de ingresos de 7-10x en seis años—. [HECHO, "
        "Microsoft/TechCrunch] A los múltiplos típicos de software para desarrolladores (8-15x ventas), "
        "eso implicaría un valor <i>standalone</i> hoy de US$16.000-30.000 millones frente a un coste de "
        "adquisición de US$7.500 millones. [SUPUESTO, múltiplo de mercado aplicado] No es solo la "
        "afirmación de que «Nadella no destruye valor en M&amp;A»: con los números disponibles, es "
        "evidencia de que las dos adquisiciones grandes de su era generaron retornos muy por encima del "
        "coste de capital.")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def s11():
    o = M.flag_titulo("§11 · Nueve inversores legendarios opinan", "Consenso de compra amplio; la divergencia de Graham es la señal")
    o += [ch("16_inversores", 15.0), sp(2)]
    o += [M.p("Nueve maneras distintas de mirar el mismo tablero — el ejercicio no es un truco retórico, "
        "es una forma de estresar la tesis contra los puntos ciegos propios de cada escuela de "
        "inversión, antes de que el mercado los encuentre por mí.")]
    pares = [
        ("Graham", "HOLD", "El balance le gusta (caja neta, AAA), pero pagar ~23x owner earnings no es margen de seguridad grahamiano sobre activos. Su única pregunta que falla: no hay descuento sobre valor tangible. Espera un precio menor. <b>El único que no compra.</b>"),
        ("Buffett", "BUY", "Negocio entendible, foso ancho e irreplicable, gestión honesta y precio justo tras la corrección. El arquetipo que ama —aunque el conflicto de Gates le mantuvo históricamente fuera—. Su convicción es alta (8/10)."),
        ("Munger", "BUY", "Gran negocio, gestión de élite. Invierte la pregunta: ¿qué lo mata? Un over-build de capex sin retorno. Pero el core es una fortaleza inexpugnable y el precio descuenta el miedo. Comprar."),
        ("Fisher", "BUY", "El <i>scuttlebutt</i> es inmejorable: Nadella/Hood, I+D líder, runway de décadas en cloud+IA+seguridad. Su tipo de compounder de calidad para tener para siempre. Convicción alta (8/10)."),
        ("Lynch", "BUY", "La historia es cristalina (el software del trabajo del mundo + la infraestructura de la IA). El PEG es razonable: 23x sobre ~13% de crecimiento. Su única duda: ¿es el capex una diworsification? No — es el core."),
        ("Templeton", "BUY", "Pesimismo del mercado sobre el capex y el FCF; drawdown del 20%; múltiplo más barato desde 2022. Es su terreno contrarian: comprar cuando el gran negocio está temporalmente en desgracia por una razón caducable."),
        ("Marks", "BUY", "¿Dónde estamos en el ciclo? El sentimiento sobre el capex de IA está lavado. Segundo nivel: el mercado sobre-reaccionó a la óptica del FCF deprimido. Comprar con la cabeza fría, midiendo el riesgo del ROIC incremental."),
        ("Seilern", "BUY", "Calidad 86, tier Núcleo, fosos entre los más anchos del mundo. La transición IA le resta (capital-light bajo presión), pero sigue siendo una tenencia central del compounder de calidad. Comprar y sostener."),
        ("Terry Smith", "BUY", "«Compra buenas empresas, no pagues de más, no hagas nada.» A 23x forward vs 32x histórico, no está pagando de más por uno de los mejores negocios del mundo. La regla #2 se cumple: comprar/acumular."),
    ]
    filas = [["Inversor", "Veredicto y razonamiento en una línea"]]
    for nm, vd, txt in pares:
        filas.append([f"<b>{nm}</b><br/><font size=7 color='#666054'>{vd}</font>", txt])
    o += [M.tabla(filas, [2.5*cm, 13.9*cm], font_sz=8.2)]
    o += [M.callout("PAUSA REFLEXIVA",
        "Ocho de los nueve compran; solo Graham se abstiene. Esa divergencia, más que el consenso, es la "
        "señal útil. Graham no discute la calidad del negocio —discute que un negocio hecho de "
        "intangibles (marcas, software, relaciones) a 23 veces sus ganancias del dueño no ofrece el "
        "margen sobre <i>activos físicos</i> que su método exige; para él, comprar aquí es apostar a que "
        "el interés compuesto (compounding) siga su curso, no a un descuento sobre algo que se puede "
        "tocar y liquidar. Tiene razón dentro de su propio marco — es la misma razón por la que Graham "
        "nunca habría comprado See's Candies, la inversión que Munger convenció a Buffett de hacer y que "
        "cambió su filosofía para siempre. Pero los otros ocho —incluidos Seilern y Terry Smith, los más "
        "cercanos a la filosofía de esta cartera— responden que para un compounder de esta calidad, el "
        "margen de seguridad no viene del descuento sobre activos, sino de la matemática del propio "
        "crecimiento a alto retorno comprado a un múltiplo razonable. El consenso amplio contra la "
        "objeción solitaria de Graham es exactamente lo que distingue esta tesis de la de Duolingo, donde "
        "la divergencia era mucho más pareja y el veredicto terminó en VIGILAR, no en comprar.")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def s12():
    o = M.flag_titulo("§12 · Riesgos: matriz, pre-mortem y alerta temprana", "El único riesgo de impacto máximo es el capex sin retorno")
    o += [ch("15_riesgos", 15.2), sp(2)]
    o += [M.p("De los seis riesgos principales, <b>solo uno tiene impacto máximo (5): que el capex de IA "
        "de ~190.000 millones al año no gane su coste de capital</b> — que la «reinversión de fase» "
        "descrita en el §1 se revele, en retrospectiva, «capital atrapado». Es la misma lógica que rige "
        "en la naturaleza: una especie que invierte de más en un solo rasgo —aquí, capacidad de "
        "datacenter— apuesta a que el entorno la va a recompensar; si el entorno cambia antes de que ese "
        "rasgo pague, la inversión se convierte en lastre. El resto de los riesgos —la solvencia de "
        "OpenAI (45% del backlog), el antitrust, la desaceleración de Azure con la depreciación "
        "escalando— son serios pero no existenciales. La matriz lo dice sin rodeos: esta inversión se "
        "juega, en última instancia, en un solo eje: el retorno del capex.")]
    o += [M.p("<b>Pre-mortem narrativo (imaginar el fracaso antes de que ocurra, para reconocerlo a "
        "tiempo si empieza a pasar).</b> Es 2031 y esta inversión salió mal. ¿Qué pasó? La secuencia más "
        "creíble: primero, la demanda de IA se «digirió» (como le pasó a Azure en 2019 y 2023 — la nube "
        "también tuvo sus propias resacas de sobre-construcción), dejando a Microsoft con capacidad de "
        "datacenter depreciándose sin ingresos que la llenen, como una ciudad que construyó autopistas "
        "para un tráfico que nunca llegó; segundo, OpenAI —el 45% del backlog— recortó su compromiso o "
        "tropezó, revelando que una parte del ritmo de facturación (run-rate) de IA era financiación "
        "circular (Microsoft invierte en OpenAI, OpenAI compra Azure con ese mismo dinero); tercero, la "
        "depreciación acelerada de los chips gráficos (GPUs, con vidas útiles de apenas 2 a 6 años) se "
        "comió el crecimiento del beneficio operativo antes de que la monetización de alto margen "
        "(Copilot) alcanzara escala; cuarto, el ROIC incremental quedó por debajo del coste de capital, "
        "el múltiplo nunca se recuperó (no hubo re-rating), y la acción —comprada a US$384 pensando que "
        "era barata— resultó valor muerto durante años. En ajedrez esto se llama quedar con piezas mal "
        "desarrolladas en el medio juego: no es jaque mate inmediato, pero la partida ya está perdida en "
        "cámara lenta. <b>La primera ficha de ese dominó, la que hay que vigilar antes que ninguna otra, "
        "es que Azure desacelere mientras el capex sigue subiendo.</b>")]
    o += [ch("20_early_warning", 15.4), sp(2)]
    o += [M.p("<b>Sistema de alerta temprana (VI.7).</b> La fase de capex se vigila con canarios "
        "cuantificables —indicadores diseñados para fallar primero, como el canario en la mina, antes de "
        "que el daño sea irreversible—. Hoy el semáforo tiene dos verdes (Azure +39% en moneda constante, "
        "margen operativo consolidado en récord) y cuatro ámbar de vigilancia intensa: el <b>margen "
        "bruto de Microsoft Cloud</b> (66%, bajando), el <b>ratio capex/ventas</b> (30,5%, sin señales de "
        "plateau), el <b>FCF económico con leases</b> (arrendamientos financieros, ~$51B), y la "
        "<b>concentración de OpenAI en el RPO</b> (backlog de ingresos comprometidos, 45%). <b>Regla "
        "dura, fijada por escrito para que no la mueva el sesgo futuro:</b> si <b>dos o más</b> de estos "
        "ámbar viran a rojo —Azure bajo +25% en moneda constante con la depreciación escalando, o el "
        "margen bruto cloud rompiendo por debajo de 63-64% estructural, o el capex sin hacer plateau en "
        "FY27-28, o OpenAI renegociando materialmente su compromiso— la «compresión de fase» deja de ser "
        "una lectura optimista y se convierte en la señal 1 plena del detector de trampas (deterioro "
        "secular del ROIC), y la tesis vira de COMPRAR a VETO-TRAMPA. Esa es la línea que el §13 fija "
        "como falsable: no una sensación, una regla.")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def s13():
    o = M.flag_titulo("§13 · Veredicto final, triggers y proyección", "Comprar la calidad al descuento — con la mano en el gatillo del capex")
    o += [M.p(f"<b>Cruce de los dos ejes.</b> CALIDAD <b>{D.es(D.SCORE_QG,1)}/100 · tier {D.TIER_QG}</b> "
        f"(ratificado en el §4, sin overrides). VALORACIÓN <b>{D.VEREDICTO}</b> (ratificado en el §9): "
        f"detector de trampas PASA, PWFV-Valor US${D.PWFV}, zona OPORTUNIDAD/GANGA, MoS +{D.MOS_HOY}% muy "
        f"por encima del 15% exigido por el tier. Los dos ejes coinciden: <b>un negocio de calidad Núcleo "
        f"a un precio que ofrece margen de seguridad real.</b>")]
    o += [M.p("<b>Frase-tesis (ritual de compra, val-mos).</b> «El mercado castiga a Microsoft por "
        "invertir agresivamente en IA —el flujo de caja libre reportado se deprime (P/FCF 39x) y el ROIC "
        "baja de fase— y le cuelga el múltiplo más barato vs su propia historia en años (P/E 22,9x vs "
        "media 32x); pero el owner-earnings normalizado, que trata el capex de IA como <b>crecimiento y no "
        "mantenimiento</b>, sitúa el yield real en ~4% y el P/OE en ~23x, y el DCF inverso prueba que el "
        "precio solo exige ~7,7% de crecimiento cuando Azure crece +40%: se paga infraestructura de "
        "altísima calidad a precio de un negocio que dejó de crecer.»")]
    o += [M.p("<b>Elemento falsable (qué mataría la tesis).</b> La tesis se refuta si el <b>ROIC "
        "incremental del capex de IA queda estructuralmente por debajo del coste de capital</b> durante "
        "~8 trimestres. Señales verificables: (a) Azure desacelera bajo +25% en moneda constante mientras "
        "la depreciación acelerada escala; (b) el margen bruto de Microsoft Cloud rompe bajo 63-64% de "
        "forma sostenida; (c) el capex/ventas NO hace plateau en FY27-28 y el FCF económico sigue "
        "cayendo bajo ~$45B; (d) OpenAI (45% del RPO) renegocia o recorta materialmente su compromiso de "
        "$250B con Azure. Si <b>dos o más</b> se cumplen, deja de ser compresión de fase y pasa a "
        "VETO-TRAMPA.")]
    o += [M.tabla([
        ["Plan de entrada por tramos", "Precio", "MoS", "Acción"],
        ["Hoy", f"US${int(D.PRECIO)}", "+26%", f"COMPRAR tramo inicial {D.TRAMO_INI} del NAV"],
        ["Ampliación", f"US${int(D.LOW_52)}–{int(D.PRECIO)}", "≥26%", f"Subir a {D.TECHO_POS} solo tras plateau de capex + descompresión de FCF"],
        ["Zona de ganga extra", "&lt; US$390", "≥25%", "Añadir con convicción si el pánico general lo lleva ahí"],
        ["Disciplina de venta", "cualquiera", "—", "Vender SOLO por deterioro (detector en rojo o 2+ ámbar VI.7 a rojo), NUNCA por múltiplo caro"],
    ], [5.4*cm, 3.0*cm, 1.8*cm, 6.2*cm])]
    o += [M.p(f"<b>Sizing y disciplina.</b> Tramo inicial {D.TRAMO_INI} del NAV; techo de posición "
        f"{D.TECHO_POS} tras la descompresión de FCF. No califica para la categoría excepcional (hasta "
        f"15% del NAV) porque falta pánico general y zona GANGA inequívoca. Por ser una herida en parte "
        f"<b>autoinfligida</b> —el capex es decisión de la gestión—, aplica la regla híbrida: entro ahora "
        f"(el MoS y el detector lo habilitan), pero el grueso espera la confirmación del retorno. Reglas "
        f"de venta (tier Núcleo): se vende SOLO por deterioro del moat/tesis, <b>nunca</b> por múltiplo "
        f"caro; el <i>drawdown</i> se mide desde el máximo, no desde el costo. El techo de múltiplo del "
        f"tier (35x owner earnings) no se viola: a US${int(D.PRECIO)} se paga ~23x.")]
    o += [M.p("<b>Proyección a 5 años (3 escenarios).</b> Alcista (25%): la monetización de IA escala, "
        "Copilot supera el 20% de conversión, el capex se revela como reinversión de alto retorno y el "
        "mercado vuelve a pagar múltiplo de compounder — valor ~US$640, un +67%. Base (50%): el capex hace "
        "plateau en FY27-28, el FCF se descomprime, Azure sostiene +30-35% — valor ~US$520, un +35%. "
        "Bajista (25%): la IA se digiere mal, el ROIC queda atrapado, OpenAI decepciona — valor ~US$395, "
        "un +3%, con el suelo sostenido por el core (Office, seguridad, Azure base). El valor ponderado es "
        "US$520. <b>La asimetría (~3:1) es clara, y esta vez el precio ya cruzó el umbral de disciplina: "
        "es momento de empezar a comprar.</b>")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def cierre():
    o = M.flag_titulo("Glosario y advertencias finales", "Términos, etiquetas y la naturaleza de este documento")
    o += [M.p("<b>Glosario.</b>", "h3")]
    gl = [
        ("Azure", "la plataforma de nube (infraestructura) de Microsoft; el motor de crecimiento."),
        ("Capex de crecimiento vs mantenimiento", "el que expande capacidad nueva vs el que repone la existente; distinguirlos es clave para el owner earnings."),
        ("Copilot", "la capa de asistentes de IA de Microsoft, vendida como añadido sobre Microsoft 365."),
        ("EPV", "valor de los beneficios sin crecimiento (Earnings Power Value); suelo de la valoración."),
        ("Finance lease", "arrendamiento financiero; deuda de datacenter que no aparece en el capex de caja."),
        ("Owner earnings", "flujo del dueño: CFO menos capex de mantenimiento menos SBC; aquí supera al FCF reportado."),
        ("PWFV-Valor", "valor intrínseco ancla del sistema val-mos (probabilístico, por owner earnings)."),
        ("MoS", "margen de seguridad; descuento del precio frente al valor intrínseco."),
        ("ROIC incremental", "retorno sobre el capital NUEVO invertido; la variable que decide la tesis."),
        ("RPO", "obligaciones de desempeño remanentes; el backlog contractual de ingresos futuros."),
        ("SBC", "compensación en acciones; en Microsoft, neutralizada por las recompras (dilución neta ~0)."),
    ]
    filas = [["Término", "Definición"]]
    for t, d in gl:
        filas.append([f"<b>{t}</b>", d])
    o += [M.tabla(filas, [4.2*cm, 12.2*cm], font_sz=8.2)]
    o += [sp(4), M.p("<b>Advertencias finales.</b>", "h3")]
    o += [M.p("Cada dato se etiquetó <b>HECHO</b> (fuente primaria: 10-K FY2025, 10-Q Q3 FY2026, DEF 14A "
        "2025 en SEC EDGAR CIK 0000789019), <b>INFERENCIA</b> (derivado o calculado) o <b>SUPUESTO</b> "
        "(asunción justificada). Cabos NO auditados, declarados: las cifras de OpenAI (pérdidas, "
        "compromisos, run-rate) provienen de reportes de terceros —OpenAI es privada—, no de estados "
        "auditados; Microsoft no divulga NRR de Microsoft 365 ni el desglose de Azure como línea propia; "
        "el capex de mantenimiento (~14% de ventas) es un supuesto prudente, no una cifra divulgada. El "
        "score de calidad se corrigió a 86 tras detectar que la corrida original puntuó dos reglas fuera "
        "del rango 0-10. El score Seilern mide <b>calidad, no valoración</b>. Este es un <b>documento de "
        "uso personal</b>, no constituye asesoría de inversión registrada para terceros.")]
    o += [M.callout("PAUSA REFLEXIVA",
        "Qué queda por saber — la pieza de información que, si la tuviera, más cambiaría el veredicto: "
        "<b>el ROIC incremental del capex de IA</b>, y su indicador más limpio, la <b>tasa de utilización "
        "de la capacidad de los centros de datos</b> (qué porcentaje de esos servidores ya construidos "
        "está efectivamente generando ingresos). Microsoft no la divulga — es la pieza que falta en el "
        "tablero. Hoy la propia compañía insiste en que está «restringida por capacidad» (más demanda "
        "que oferta), lo que implicaría que el capex se monetiza apenas se enchufa: la tesis alcista, y "
        "la que sostiene esta compra. Si en los próximos trimestres aparecieran señales de capacidad "
        "ociosa (Azure desacelerando mientras la depreciación contable sigue subiendo), el veredicto "
        "sobre el ROIC incremental se inclinaría hacia «capital atrapado» y el detector de trampas "
        "debería reabrirse sin sentimentalismo, sin importar cuánto se aprecie el negocio. Sin ese dato "
        "exacto, vigilo por indicadores indirectos (proxies): el margen bruto de Microsoft Cloud, el "
        "ritmo del capex, y cualquier cambio en el lenguaje de «restringido por capacidad» en las "
        "próximas <i>calls</i> de resultados. Conseguir una lectura fiable de la utilización real es la "
        "prioridad de investigación de cara a Q4 FY2026 — el dato que separa la fe de la evidencia.")]
    return o

# ══════════════════════════════════════════════════════════════════════════
def story():
    s = []
    for fn in [portada, changelog, resumen, cuadro_mando, veredicto_cuant,
               s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, cierre]:
        s += fn()
    return s
