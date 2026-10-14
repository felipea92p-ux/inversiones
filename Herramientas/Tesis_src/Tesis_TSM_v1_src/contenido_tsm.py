# -*- coding: utf-8 -*-
"""CONTENIDO · Tesis Ultra TSM v2.1. Solo prosa/datos. Importa motor_qg (diseño) y dcf_tsm (números).
v2.1 (2026-07-10): verificación adversarial final del ancla de valoración. Se agrega a §9 un
cross-check de ROIC incremental (con cita de fuente y sus dos caveats de comparabilidad/sesgo) y
se ancla explícitamente la prima geopolítica permanente del WACC a probabilidades de horizonte
largo (Metaculus/Manifold, verificadas en vivo) en vez de mercados de eventos de corto plazo.
CERO cambios en PWFV, WACC, zonas o veredicto — dcf_tsm.py sube a v1.1 solo para documentar el
cross-check, no una corrección. Ver changelog().
v2.0 (2026-07-09): refresco editorial de voz narrativa — metáforas de ajedrez/geopolítica sostenidas
como hilo conductor, curiosidades verificadas sobre Morris Chang y la cultura operativa de TSMC,
jerga técnica explicada en su primer uso por sección. Cero cambios en números/veredicto — ver
changelog() y dcf_tsm.py (intacto)."""
from reportlab.platypus import Spacer, PageBreak, NextPageTemplate, Paragraph
from reportlab.lib.units import cm
from reportlab.lib.styles import ParagraphStyle
import motor_qg as M
from motor_qg import C
import dcf_tsm as D

def sp(h=6): return Spacer(1, h)
def ch(name, w=16.4): return M.chart(f"charts/{name}.png", w)
DISCLAIMER = ("Este score mide CALIDAD del negocio, no valoración ni margen de seguridad. "
              "Score alto &ne; comprar.")

# ══════════════════════════════════════════════════════════════════════════
def portada():
    nombre = ParagraphStyle("nm", fontName="Serif-B", fontSize=31, leading=34, textColor=C["tinta"])
    tick = ParagraphStyle("tk", fontName="Sans-B", fontSize=12.5, leading=16, textColor=C["rojo"])
    tag = ParagraphStyle("tg", fontName="Serif-I", fontSize=12.5, leading=17, textColor=C["gris"])
    meta = ParagraphStyle("meta", fontName="Serif", fontSize=9.5, leading=13, textColor=C["tinta"])
    fn = ParagraphStyle("fn", fontName="Serif-I", fontSize=8, leading=11, textColor=C["gris"])
    out = [Spacer(1, 2.0*cm),
        Paragraph("TAIWAN SEMICONDUCTOR MFG. CO.", nombre),
        Paragraph("NYSE: TSM &nbsp;·&nbsp; El monopolio de facto de la fabricación de punta &nbsp;·&nbsp; "
                  "el mejor negocio de este análisis, con el mayor riesgo de cola de todos", tick),
        sp(14),
        Paragraph("72% del mercado global de fundición, ganando cuota. Márgenes en récord histórico, "
                  "creciendo cada trimestre. Y sin embargo, casi el 100% de esa producción de punta está "
                  "físicamente concentrada en un territorio disputado, con un plan de auto-inutilización "
                  "ya confirmado por un ex-presidente de la empresa. El mercado, en 2026, decidió reducir "
                  "el descuento por ese riesgo justo cuando la evidencia dice lo contrario.", tag),
        sp(20),
        M.kpi_panel([
            (f"{D.es(D.SCORE_QG,1)}/100", "CALIDAD QG", f"tier {D.TIER_QG} (75-84)"),
            (f"US${D.PWFV}", "VALOR (PWFV)", f"vs US${D.es(D.PRECIO,0)} hoy · zona {D.ZONA_HOY}"),
            (f"{D.es(D.MULT_NORMALIZADO,1)}x", "MÚLTIPLO OWNER EARNINGS", "vs techo del tier 30x"),
        ]),
        sp(16), M.hr(),
        Paragraph(f"<b>6 de julio de 2026</b> &nbsp;·&nbsp; Precio US${D.es(D.PRECIO,2)} &nbsp;·&nbsp; "
                  f"Market cap ~US${D.es(D.MKTCAP,0)}B &nbsp;·&nbsp; Horizonte 5–10 años &nbsp;·&nbsp; "
                  f"Documento de convicción N&ordm; 19", meta),
        M.hr(),
        Paragraph("Eje CALIDAD (sistema qg-seilern de 11 reglas, verificado sin corrección) y eje PRECIO "
                  "(val-mos v3: PWFV-Valor, detector de trampas, MoS por tier, candado duro anti-sobrepago) "
                  "calculados por separado y cruzados solo al final. Uso personal; no es asesoría de inversión registrada.", fn),
        NextPageTemplate("Normal"), PageBreak()]
    return out

# ══════════════════════════════════════════════════════════════════════════
def changelog():
    o = M.flag_titulo("Changelog de versiones", "El único freno real es una sola variable — y esta v2.1 la aísla con precisión")
    o += [M.p("<b>v2.1 (10-jul-2026) — verificación adversarial final del ancla de valoración.</b> Un "
        "ataque dedicado intentó mover PWFV/WACC/zona/veredicto por dos vías: (1) recomputando en vivo "
        f"el ROIC incremental de TSM (fuente: stockanalysis.com, balance sheet + income statement "
        "FY2021-FY2025, coincide al millón de NT$ con el Form 20-F) sobre cinco ventanas distintas, y "
        "(2) verificando en vivo las probabilidades de mercado que sostienen la prima geopolítica del "
        "WACC. <b>Ningún número de valoración cambió</b> — el ataque no encontró base para mover el "
        f"ancla de US${D.PWFV}; corregidos los dos defectos que sí encontró, el sesgo residual apunta a "
        "que el ancla es conservadora, no agresiva. Qué se agregó a §9 con honestidad sobre sus "
        f"límites: el ROIC incremental (caso central {D.pct(D.ROIC_INCR_CENTRAL)} sobre la ventana "
        f"2021-2025, mínimo probado {D.pct(D.ROIC_INCR_MINIMO)}, todas las ventanas por encima del WACC) "
        "corrobora R7 y la lectura de \"capex con historial probado\", con la advertencia explícita de "
        "que es MENOS comparable con el mismo cálculo hecho para AWS de lo que una lectura superficial "
        "sugeriría (activos de toda la compañía sobre varios años, no activos de segmento sobre un año) "
        "y con un sesgo de contaminación por expansión de margen sobre capital preexistente que no se "
        "había declarado antes. La prima permanente de WACC se ancla ahora explícitamente a "
        f"probabilidades de horizonte largo ({D.pct(D.PROB_INVASION_2027)} acumulado a 2027, "
        f"{D.pct(D.PROB_INVASION_2030)} a 2030, {D.PROB_FUENTE}) en vez de un mercado de eventos de "
        "corto plazo, descartado a propósito por ser más ruidoso y de horizonte equivocado para un "
        "ajuste que compensa un riesgo a perpetuidad, no un evento de 6-12 meses.")]
    o += [M.p("<b>v2.0 (9-jul-2026) — refresco editorial de voz narrativa.</b> Esta versión reescribe en "
        "profundidad la prosa narrativa (historia, modelo de negocio, moat, competencia, gestión, riesgos, "
        "pre-mortem y cierre) con metáforas de ajedrez e historia geopolítica sostenidas como hilo "
        "conductor, e incorpora curiosidades verificadas en fuente primaria sobre los tres rechazos "
        "profesionales previos de Morris Chang, la financiación fundacional de 1987 (gobierno de Taiwán + "
        "Philips), su retorno de 2009 y su retiro definitivo de 2018 con la estructura de \"dos capitanes\" "
        "(Liu/Wei), y la fricción cultural documentada entre la cultura operativa taiwanesa y la fábrica de "
        "Arizona. Toda jerga técnica nueva (yield, ASIC, PDK, wafer, silicon shield, EUV) quedó explicada "
        "entre paréntesis en su primer uso por sección. <b>CERO cambios en números, score de calidad, PWFV "
        "o veredicto de inversión</b> — dcf_tsm.py permanece exactamente igual a la v1.0; el Cuadro de "
        "Mando, el veredicto cuantificado y todas las tablas con cifras de calidad/valoración quedaron en "
        "el mismo registro seco, sin metáfora. En el proceso se verificó un dato ya presente en v1.0 "
        "(gobierno de Taiwán como socio fundacional de 1987, 48% de participación vía National Development "
        "Fund) que no había sido explicitado antes en el cuerpo de la tesis pese a ser relevante para la "
        "discusión de gobernanza de §10 — se agregó como contexto histórico, sin alterar ningún número del "
        "eje cuantitativo.")]
    o += [M.p("Esta es la <b>versión 1.0</b> de la tesis Ultra de TSMC. A diferencia de las tesis anteriores "
        "de esta campaña, aquí el score de calidad se verificó <b>sin ninguna corrección material</b> — el "
        "verificador adversarial confirmó el 78,4/100 (Alta Convicción) recomputando la aritmética por tres "
        "métodos independientes (suma secuencial, agrupación crítica/estándar, y método de brechas al "
        "máximo), los tres coincidiendo en raw=98,0. El hallazgo más importante de esta v1.0 no es una "
        "corrección de score: es un <b>vacío explícito del propio sistema qg-seilern</b>, señalado tanto "
        "por el agente de scoring como por su verificador: <b>no existe un knock-out gate para "
        "\"concentración geográfica de punto único de falla\"</b> — el riesgo de que casi el 100% de la "
        "producción de punta esté físicamente en un solo territorio geopolíticamente disputado se canaliza "
        "enteramente a través de R6 (2/10, el mayor detractor del scorecard), no a través de una exclusión "
        "binaria. Sin esa penalización, TSM anotaría 85+ y calificaría para Núcleo — es decir, <b>la "
        "clasificación completa de esta empresa depende de una sola variable de ponderación.</b>")]
    o += [M.tabla([
        ["Supuesto crítico fijado en v1.0", "Valor", "Qué lo movería"],
        ["Prima de riesgo geopolítico en el WACC", "+250pb (punto medio de rango 150-400pb defendible)", "Resolución (en cualquier dirección) de la tensión Taiwán-China"],
        ["PWFV ancla (con prima)", "US$236/ADR", "Sin prima geopolítica sería US$360 — una diferencia de −34% solo por este ajuste"],
        ["Precio de referencia del modelo DCF", "~US$477 (máximo histórico, 30-jun-2026)", "La cotización en vivo hoy (US$442,35) sostiene la misma conclusión"],
        ["Gate de concentración geográfica", "NO EXISTE en qg-seilern; se resuelve vía R6", "Decisión de canon: ¿merece un gate G8 dedicado?"],
    ], [6.4*cm, 5.6*cm, 4.4*cm], font_sz=7.5)]
    o += [M.p("<b>El punto de honestidad que esta v1.0 se obliga a recordar:</b> TSMC es, en casi todas las "
        "dimensiones de negocio puro, la empresa de mayor calidad de todo este portafolio — moat casi "
        "imposible de replicar, márgenes en expansión constante sin un solo trimestre de deterioro, balance "
        "en caja neta positiva. El sistema no ignora nada de eso: lo reconoce con un 78,4/100. Pero tampoco "
        "permite que esa excelencia compre de vuelta el hecho de que el mercado, en 2026, está reduciendo "
        "el descuento por el riesgo de Taiwán justo cuando la evidencia (retraso del paquete de armas de "
        "EEUU, simulacros militares, un plan de auto-inutilización ya confirmado) no mejora. Los dos hechos "
        "conviven en la misma tesis, sin comprarse de vuelta el uno al otro.")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def resumen():
    o = M.flag_titulo("Resumen en treinta segundos", "El mejor negocio de la cartera, con el mayor riesgo de cola — y un precio que ya no lo refleja")
    o += [M.p("<b>¿Puede seguir existiendo una empresa que fabrica casi todos los semiconductores de punta "
        "del mundo desde un único territorio geopolíticamente disputado, y cuánto vale esa empresa si se "
        "toma en serio ese riesgo en la tasa de descuento, no solo en la narrativa?</b> Esas son las dos "
        "preguntas que definen esta tesis. La primera tiene una respuesta que el propio negocio contesta "
        "con hechos: TSMC gana cuota de mercado, expande márgenes cada trimestre, y sus rivales (Samsung, "
        "Intel) siguen sin poder igualar su volumen a escala. La segunda pregunta tiene una respuesta más "
        "incómoda: cuando se aplica honestamente la prima de riesgo que ese hecho geopolítico exige, el "
        "valor justo cae 34% — y el precio de hoy ya está muy por encima incluso de esa versión más cara. "
        "[HECHO/INFERENCIA]")]
    o += [M.tabla([
        ["El número", "Qué dice"],
        ["72,3% de cuota global de fundición, ganando", "TSMC no solo lidera: está ampliando la brecha con el resto de la industria combinada. Ningún trimestre de deterioro de negocio en toda la ventana analizada. [HECHO]"],
        ["+250pb de prima geopolítica → PWFV cae 34%", "El único ajuste de tasa de descuento por el riesgo de Taiwán mueve el valor justo de US$360 a US$236 — sin tocar un solo supuesto de crecimiento u operación. [val-mos]"],
        ["73,8x-79,5x owner earnings vs. techo 30x", "El candado duro anti-sobrepago se viola por un margen enorme, incluso usando el año más favorable (2026e) en vez del trailing. [val-mos]"],
    ], [4.0*cm, 12.4*cm], font_sz=8.0)]
    o += [sp(6), M.p(f"<b>Veredicto operativo.</b> Calidad QG <b>{D.es(D.SCORE_QG,1)}/100</b> (tier "
        f"<b>{D.TIER_QG}</b>, verificado sin corrección — R6 concentración geopolítica en 2/10 es el único "
        f"freno real). El detector de trampas da <b>PASA</b> limpio: no hay ningún elemento del negocio "
        f"que respalde una narrativa bajista — todo lo contrario, los fundamentales aceleran. PWFV-Valor "
        f"<b>US${D.PWFV}</b> (con prima geopolítica, ancla primaria) frente a US${D.es(D.PRECIO,0)}: zona "
        f"<b>{D.ZONA_HOY}</b> — el precio duplica el valor justo. <b>Acción: {D.VEREDICTO}.</b> No es un "
        f"veredicto de \"negocio malo\": es un veredicto de \"precio que ya cobró por adelantado un "
        f"crecimiento superior al que la propia gerencia, en modo optimista, se compromete a entregar\".")]
    o += [M.callout("PAUSA REFLEXIVA",
        "Esta es la única tesis de la campaña donde el freno es 100% de precio y 0% de negocio — el "
        "detector de trampas dio PASA limpio, sin matices. Eso hace la disciplina más difícil, no más "
        "fácil: es mucho más tentador \"hacer una excepción\" para un negocio que se ve tan bien en cada "
        "métrica operativa. La pregunta que debes hacerte: ¿comprarías TSMC sabiendo que el 34% del valor "
        "justo depende enteramente de cuánto peso le des a un riesgo que, por definición, no se ha "
        "materializado todavía?")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def cuadro_mando():
    o = M.flag_titulo("Cuadro de mando trimestral", "Lo único que se refresca cada trimestre · corte 6-jul-2026")
    o += [M.p("<b>Bloque 1 · Estado de la posición.</b>", "h3")]
    o += [M.tabla([
        ["Concepto", "Estado"],
        ["Precio / zona", f"US${D.es(D.PRECIO,2)} · zona {D.ZONA_HOY} (187% del PWFV con prima; 123% sin prima, aún Caro)"],
        ["Valor justo (PWFV-Valor)", f"US${D.PWFV} (con prima geopolítica) · US${D.PWFV_SIN_PRIMA} (sensibilidad, sin prima) · EPV suelo US${D.es(D.EPV,1)}-{D.es(D.EPV_FY26E,1)}"],
        ["Probabilidades de escenario", f"Conservador {D.P_BEAR}% (US${D.V_BEAR}) · Base {D.P_BASE}% (US${D.V_BASE}) · Optimista {D.P_BULL}% (US${D.V_BULL})"],
        ["Veredicto operativo", f"{D.VEREDICTO} · 0% de ampliación · watchlist con gatillo US${D.GATILLO_OPORT} (Oportunidad) / US${D.GATILLO_GANGA} (Ganga)"],
    ], [4.3*cm, 12.1*cm])]
    o += [sp(4), M.p("<b>Bloque 2 · Tracker de KPIs en semáforo.</b>", "h3")]
    o += [M.tabla([
        ["Indicador", "Hoy", "Umbral rojo", "●"],
        ["Margen operativo consolidado", "58,1% (récord)", "cae &lt; 45% sostenido", "verde"],
        ["Ingreso HPC/IA (crecimiento)", "+48% YoY (2025)", "&lt; 25% sostenido 2+ trim.", "verde"],
        ["ROE anualizado", "40,5% (récord)", "cae &lt; 25%", "verde"],
        ["EV/EBITDA vs. mediana 10 años", "+124% (estirado)", "sigue expandiéndose sin pausa", "ambar"],
        ["Concentración top-2 clientes", "36% (convergiendo)", "supera 45% combinado", "ambar"],
        ["Riesgo geopolítico Taiwán/China", "drills + retraso de armas EEUU", "hecho estructural, no transitorio", "rojo"],
    ], [6.0*cm, 4.4*cm, 4.2*cm, 1.8*cm], font_sz=7.8)]
    o += [sp(4), M.p("<b>Bloque 3 · Feedback loop de calibración.</b>", "h3")]
    o += [M.tabla([
        ["Predicción (trim. anterior)", "Resultado real", "Interpretación"],
        ["v1.0 — sin predicción formal previa", "Q1'26: rev +40,6% USD, margen op. 58,1%, ROE 40,5%", "Punto de partida; calibrar desde el próximo trimestre"],
        ["Prima geopolítica de +250pb en el WACC", "Zona Burbuja (con prima) vs. Caro (sin prima)", "Vigilar si el mercado empieza a exigir esta misma prima"],
    ], [5.6*cm, 5.4*cm, 5.4*cm])]
    o += [sp(4), M.p("<b>Bloque 4 · Operativo.</b> Trigger de re-análisis inmediato (no solo trimestral): "
        "cualquier escalada real de tensión en el Estrecho de Taiwán (más allá de drills rutinarios), o "
        "una segunda venta confirmada de Samsung/Intel a un cliente top-10 de TSM más allá del caso Tesla "
        "AI6 ya conocido. Fecha del refresh: <b>6-jul-2026</b>; documento completo v1.0. Próxima revisión: "
        "resultados <b>Q2 2026</b> (jul-2026) — foco en si el guidance de CAGR de 25% se sostiene o se "
        "revisa, y en la evolución de la concentración de clientes.")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def veredicto_cuant():
    o = M.flag_titulo("El veredicto cuantificado", "Once reglas con bisturí — un solo freno real, verificado sin corrección")
    o += [M.p(f"<i>{DISCLAIMER}</i>", "nota")]
    o += [ch("01_radar", 15.0), sp(4)]
    vd = {
        "R1 · Escalabilidad": "Modelo de capacidad (no plataforma pura) con márgenes en expansión constante pese a capex de 33-44% de ventas; el techo se limita por ser un modelo intensivo en capital, no por debilidad de ejecución.",
        "R2 · Industria": "Guidance de management elevado a ~25% CAGR (desde ~20%); tailwind estructural real, aunque con riesgo de ciclo de capex de IA que el sistema pondera con cautela.",
        "R3 · Liderazgo": "72,3% de cuota global de fundición, ganando terreno; líder por margen y capacidad, no solo por tamaño nominal — la exención de \"infraestructura esencial\" del propio sistema aplica aquí.",
        "R4 · Moat": "Multi-moat casi imposible de replicar (US$28.000M por fábrica competidora + curva de aprendizaje de procesos); descontado ligeramente por la dependencia de proveedor único (ASML) y el primer caso real de doble-abastecimiento (Samsung/Tesla).",
        "R5 · Crec. orgánico": "Margen neto 39,4%→50,5%, ingresos +35-40% interanual, 100% orgánico — el caso más limpio de máxima puntuación de toda la campaña.",
        "R6 · Diversificación": "El único freno real: dos clientes &gt;15% cada uno (convergiendo hacia ~20%) y casi el 100% de la producción de punta concentrada físicamente en Taiwán, con un plan de auto-inutilización de fábricas ya confirmado ante escenario de invasión.",
        "R7 · Capital / ROIC": "ROIC estimado ~35-44%, de élite incluso frente a pares de capacidad intensiva; capex disciplinado y guiado por demanda visible, no especulativo.",
        "R8 · Balance": "Caja neta positiva de magnitud extraordinaria; la deuda es, literalmente, un error de redondeo frente al efectivo — el caso de referencia del propio sistema para balance sólido.",
        "R9 · Transparencia": "Semáforo de tres señales limpio (conversión de caja, ratio de acumulaciones, brecha GAAP/no-GAAP); descontado un punto por el silencio total del 20-F sobre riesgo de Taiwán en términos explícitos.",
        "R10 · Gestión": "Ejecución excepcional bajo C.C. Wei (cumple y supera guidance elevado); descontado por la consolidación de Presidente+CEO desde 2024 y el rol de TSMC como instrumento geopolítico de dos gobiernos.",
        "R11 · Impacto": "Infraestructura crítica que habilita cómputo global (salud, ciencia, comunicaciones); por debajo del nivel máximo reservado para soluciones estructurales directas a problemas humanos (inclusión financiera, salud).",
    }
    filas = [["Regla", "Puntos", "Veredicto en una línea"]]
    for n, pts, mx in D.REGLAS:
        p_txt = f"{int(pts)}/{mx}"
        filas.append([n, p_txt, vd[n]])
    filas.append(["<b>TOTAL</b>", f"<b>{D.es(D.RAW_QG,1)}/125</b>",
                  f"<b>{D.es(D.SCORE_QG,1)}/100 · tier {D.TIER_QG} (75-84)</b>"])
    o += [M.tabla(filas, [3.2*cm, 2.0*cm, 11.2*cm], font_sz=7.4)]
    o += [M.p("<i>Nota metodológica: verificación adversarial confirmó la aritmética por tres métodos "
        "independientes (todos raw=98,0) sin encontrar error. El hallazgo principal no fue una corrección "
        "de número sino un vacío de diseño: el sistema qg-seilern no tiene un gate dedicado para "
        "concentración geográfica de punto único de falla catastrófico — el riesgo se canaliza enteramente "
        "vía R6, por decisión explícita de diseño (\"el knock-out VIE + exclusiones cubren lo grave\"), no "
        "por descuido. Sin la penalización de R6, TSM anotaría 85+ (Núcleo) — toda la clasificación cuelga "
        "de esa sola variable.</i>", "nota")]
    o += [M.callout("LECCIÓN TRANSFERIBLE",
        "TSMC es la prueba de que un score de calidad alto no es, ni debe ser, un promedio simple de "
        "virtudes: es una nota que un solo riesgo suficientemente severo puede dominar por completo, sin "
        "importar cuán excelente sea todo lo demás. El sistema podría haber promediado la excelencia "
        "operativa de TSMC con su riesgo geográfico y llegar a un número artificialmente cómodo. En cambio, "
        "R6 en 2/10 —el peor score individual de toda esta campaña de tesis, empatado con la gobernanza de "
        "GOOGL— asegura que ese riesgo pese lo que merece pesar, incluso en la empresa de mejor negocio "
        "puro de todo el portafolio.")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def s1():
    o = M.flag_titulo("§1 · La historia detrás del veredicto", "El hombre a quien rechazaron tres veces terminó inventando un tablero donde nadie más podía jugarle")
    o += [M.p("Antes de fundar TSMC, Morris Chang perdió tres veces la partida que más quería ganar. En "
        "1983, a los 52 años, Texas Instruments —la empresa a la que había dedicado 25 años de carrera— lo "
        "pasó por alto para el puesto máximo de CEO. Se fue a presidir General Instrument y fracasó también "
        "ahí en menos de un año. Aterrizó luego en Taiwán como jefe del instituto tecnológico estatal ITRI, "
        "y hasta ese cargo terminó chocando con casi todo el personal a su cargo. Para 1987, cuando fundó "
        "TSMC, Chang no era un visionario en ascenso: era un ejecutivo de 56 años al que las jerarquías que "
        "conocía habían descartado tres veces seguidas. [HECHO]")]
    o += [M.p("Su jugada, sin embargo, no fue insistir en el tablero donde ya había perdido —diseñar chips "
        "y competir de frente contra Texas Instruments, Intel o cualquier otro gigante integrado—: fue "
        "inventar un tablero distinto, donde esas mismas empresas dejaban de ser rivales para convertirse "
        "en clientes. Cuando buscó capital para esa apuesta, tanto Intel como su propio ex-empleador Texas "
        "Instruments se negaron a invertir. Terminó siendo Philips —un fabricante holandés de "
        "semiconductores de segundo nivel, no un gigante— quien aportó capital y licencias de tecnología a "
        "cambio de una participación de casi 28%; el otro gran socio fue el propio gobierno de Taiwán, que "
        "cubrió cerca de la mitad de los US$220 millones de capital inicial a través de su fondo nacional "
        "de desarrollo, quedándose con 48% de la empresa. Ese fondo estatal sigue en el accionariado casi "
        "cuarenta años después (6,38% hoy, ver §10) — no es un dato anecdótico: es el primer hilo de una "
        "tensión entre lo comercial y lo geopolítico que atraviesa toda esta tesis. [HECHO]")]
    o += [M.p("La apuesta central de Chang —hoy conocida como \"fundición pura\" (pure-play foundry): una "
        "empresa que solo fabrica los chips que otros diseñan, sin competir jamás con ellos— fue, en "
        "esencia, negarse a jugar ajedrez contra sus propios clientes. Apple, Nvidia, AMD y Qualcomm "
        "diseñan sus chips y se los entregan a TSMC para fabricarlos con la tranquilidad de que TSMC nunca "
        "lanzará un producto competidor con lo que aprendió de ellos. Esa neutralidad estratégica, sostenida "
        "sin excepción durante cuatro décadas, es en sí misma un foso competitivo (moat, ver §5): ningún "
        "cliente le teme al fabricante que eligió no jugar su juego. [HECHO]")]
    o += [M.p("Chang se retiró como CEO en 2005, a los 74 años, pero volvió en 2009, a los 78, en plena "
        "crisis financiera global —el detonante fue que su sucesor Rick Tsai había disfrazado despidos de "
        "\"evaluaciones de desempeño\", generando un resentimiento interno que Chang decidió revertir "
        "personalmente, ofreciendo recontratar a los afectados—. Su primera decisión al volver fue apostar "
        "en la dirección contraria a la que dictaba el miedo del momento: mientras el resto de la industria "
        "recortaba inversión, Chang lanzó un programa de capex multimillonario a contraciclo para asegurar "
        "el liderazgo de TSMC antes de que la recuperación llegara. Cuando la economía global se recuperó, "
        "TSMC salió de la crisis más dominante de lo que había entrado. Esa misma disciplina —invertir "
        "cuando otros dudan, sin desviarse del plan de capacidad— es, casi dos décadas después, la que "
        "explica por qué el capex de 2026 salta 30% interanual justo cuando la demanda de IA es más "
        "incierta que nunca (ver §8). [HECHO]")]
    o += [ch("03_plataformas", 15.2), sp(2)]
    o += [M.p("La historia de 2026 es la de una empresa que ganó, de forma casi accidental, la lotería de "
        "la infraestructura de IA: cuando Nvidia, Google, Amazon, Microsoft y Meta compiten ferozmente por "
        "quién diseña el mejor chip de inteligencia artificial, todos ellos —sin excepción— dependen de "
        "TSMC para fabricarlo. Es una posición insólita en cualquier tablero competitivo: cinco reyes "
        "rivales que solo pueden moverse sobre la misma casilla. El ingreso de la plataforma HPC/IA pasó de "
        "representar 43% del ingreso total en 2023 a 61% en el primer trimestre de 2026, con management "
        "elevando su guía de crecimiento a cinco años de ~20% a ~25% anual —una revisión al alza "
        "inusualmente agresiva para una empresa de este tamaño—. [HECHO]")]
    o += [M.p("Pero la historia de 2026 tiene un segundo capítulo, menos cómodo: en enero de ese año, China "
        "realizó simulacros militares de cerco a Taiwán con fuego real; Xi Jinping declaró públicamente que "
        "\"la reunificación es imparable\"; y un paquete de armas estadounidense de US$14.000 millones para "
        "Taiwán —el mayor jamás propuesto— fue retrasado personalmente por el propio presidente "
        "estadounidense, quien lo describió como una \"ficha de negociación\" en sus conversaciones con Xi. "
        "Un ex-presidente de TSMC ya confirmó públicamente que la empresa tiene un plan de "
        "auto-inutilización de sus fábricas ante un escenario de invasión. Chang pudo elegir invertir a "
        "contraciclo en 2009 porque el riesgo que enfrentaba era financiero, y los riesgos financieros se "
        "compran con paciencia y capital. El riesgo de 2026 es distinto en su naturaleza: no hay "
        "contra-jugada de capex que reubique una isla. Estos no son riesgos hipotéticos de manual: son "
        "hechos ya ocurridos, documentados por fuentes primarias, en el mismo año que esta tesis se está "
        "escribiendo. [HECHO]")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def s2():
    o = M.flag_titulo("§2 · Historia de mi posición", "Una posición mediana en el mejor negocio de la cartera, con el mayor riesgo de cola")
    o += [M.p(f"TSMC es una posición mediana en mi cartera (24 acciones, costo promedio US$440,83, valor de "
        f"mercado ~US$10.616 al precio de hoy). No es una "
        f"convicción de tamaño como MELI, pero sí una pieza que exige una disciplina particular en el "
        f"tablero: es, por prácticamente cualquier métrica operativa, el mejor negocio puro de todo este "
        f"análisis de portafolio —y a la vez la única tesis donde el freno completo es de precio, no de "
        f"calidad de negocio. [contexto propio]")]
    o += [M.p(f"El análisis frío concluye <b>{D.VEREDICTO}</b>, y aquí la disciplina es distinta a la de "
        f"MELI (donde el negocio mismo mostraba deterioro real) o GOOGL (excluida por un gate de tier "
        f"pese a un precio razonable): en TSMC, <b>el negocio no tiene ningún defecto material</b> —el "
        f"detector de trampas dio PASA limpio— y el freno completo viene de una sola variable de "
        f"valoración: la prima de riesgo geopolítico que el WACC debe incorporar. Aplicada honestamente "
        f"(+250 puntos básicos), esa prima por sí sola mueve el valor justo un 34% hacia abajo, y el "
        f"precio de hoy ya está muy por encima incluso de la lectura más generosa (sin prima).")]
    o += [M.p(f"<b>Mi posición operativa:</b> sostener sin ampliar, con vigilancia activa —no pasiva—, como "
        f"quien mantiene una pieza fuerte en el tablero sin arriesgar un movimiento adicional mientras el "
        f"resto de la partida sigue abierta. Hay gatillos de precio cuantificados y relativamente cercanos "
        f"en términos relativos (una caída de 50-65% desde el máximo activaría la zona de "
        f"Oportunidad/Ganga). No hay ningún argumento de calidad de negocio para vender lo que ya se tiene.")]
    o += [M.callout("PAUSA REFLEXIVA",
        "¿Cómo se distingue \"esperar el precio correcto en el mejor negocio de la cartera\" de "
        "\"racionalizar no vender algo que no quiero soltar\"? La respuesta honesta: TSMC exige la "
        "disciplina más difícil de las tres posiciones de esta ronda de tesis, precisamente porque el "
        "negocio es tan bueno que resulta tentador ignorar la prima de riesgo geopolítico como \"ruido de "
        "fondo\". El sistema existe exactamente para resistir esa tentación en el momento en que más cuesta "
        "resistirla.")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def s3():
    o = M.flag_titulo("§3 · El modelo de negocio en dos minutos", "La prueba de Lynch: el único jugador al que todos necesitan y ninguno puede reemplazar")
    o += [M.p("<b>La prueba de los dos minutos</b> —el ejercicio que Peter Lynch recomendaba para poder "
        "explicar cualquier negocio en el tiempo que tarda un ascensor en subir unos pisos—. TSMC fabrica "
        "los semiconductores más avanzados del mundo para clientes que diseñan sus propios chips pero no "
        "tienen (o no quieren tener) la capacidad de fabricarlos —un modelo llamado \"fundición pura\" "
        "(pure-play foundry)—. No compite con sus clientes: Apple diseña el chip de su iPhone, Nvidia "
        "diseña su GPU de IA, pero ambos recurren a TSMC para producirlo físicamente. TSMC gana dinero "
        "cobrando por cada oblea de silicio (wafer, el disco delgado de material semiconductor sobre el "
        "que se graban los circuitos) procesada, con un margen que aumenta cuanto más avanzado —y más caro "
        "de fabricar— es el proceso. [HECHO]")]
    o += [ch("05_foundry_share", 15.2), sp(2)]
    o += [M.p("<b>La mecánica que decide la década: el cuello de botella no está donde todos miran.</b> La "
        "narrativa popular sobre la escasez de chips de IA se centra en la capacidad de fabricar obleas "
        "—el paso que todo el mundo entiende—. Pero la restricción real y más aguda está un paso más "
        "adelante, en un proceso mucho menos conocido: el empaquetado avanzado (CoWoS, Chip-on-Wafer-on-"
        "Substrate: la técnica que suelda varios chips distintos en un solo módulo de alto rendimiento). "
        "Es la pieza del tablero que casi nadie mira porque no tiene el glamour del diseño de chips, y sin "
        "embargo es la que decide cuántas GPU de IA puede vender Nvidia en un trimestre dado. TSMC está "
        "triplicando esa capacidad entre 2024 y 2027, y aun así la demanda supera la oferta: Nvidia sola "
        "reservó más de la mitad de la capacidad de CoWoS de 2026-2027. Quien controla ese cuello de "
        "botella no es Nvidia, ni ningún diseñador de chips: es TSMC. [HECHO/INFERENCIA]")]
    o += [M.p("<b>Lo ya ejecutado frente a lo todavía prometido.</b> Vale la pena separar, dentro de esa "
        "expansión de CoWoS, lo que ya ocurrió de lo que sigue siendo plan —la misma disciplina que "
        "aplicaría un analista escéptico ante cualquier guidance de management demasiado optimista—. La "
        "capacidad pasó de ~35.000 obleas/mes en 2024 a 75.000-80.000 obleas/mes ya en producción efectiva "
        "al cierre de 2025 —una duplicación real, no proyectada, verificable en reportes de cadena de "
        "suministro (TrendForce/Silicon Analysts) [HECHO]—. La proyección de 120.000-140.000 obleas/mes "
        "para el cierre de 2026 y de hasta 170.000 para fines de 2027 sigue siendo, en cambio, mayormente "
        "plan futuro: reportado por la cadena de suministro pero sin que TSMC lo haya guiado oficialmente "
        "con esa granularidad en sus propios calls [INFERENCIA]. El primer tramo ya está probado; el "
        "segundo todavía exige que la ejecución se sostenga sin fricción durante dos años más.")]
    o += [ch("06_cowos", 15.0), sp(2)]
    o += [M.p("<b>El activo que ni Samsung ni Intel han logrado replicar en veinte años de intentarlo.</b> "
        "Construir una fábrica competidora de 2 nanómetros (2nm, la unidad de medida del proceso de "
        "fabricación más avanzado actual — cuanto menor el número, más pequeño y eficiente el transistor) "
        "cuesta aproximadamente US$28.000 millones —y ese costo hay que repetirlo en cada nueva generación "
        "de proceso, como pagar de nuevo la entrada de un torneo cada vez que sube de categoría—. Samsung "
        "y Intel han invertido decenas de miles de millones cada uno intentando cerrar la brecha, y aun así "
        "ninguno ha logrado capturar volumen significativo de los clientes más exigentes en el nodo más "
        "avanzado. El primer caso real de doble-abastecimiento (Tesla llevando su próximo chip AI6 "
        "parcialmente a Samsung) es una grieta genuina en esa narrativa de monopolio absoluto —pero sigue "
        "siendo, por ahora, la excepción que confirma la regla. [HECHO]")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def s4():
    o = M.flag_titulo("§4 · Las once reglas de Seilern con bisturí", "El output de qg-seilern, verificado sin corrección — un solo freno real")
    o += [M.p(f"<i>{DISCLAIMER}</i>", "nota")]
    o += [M.p(f"TSMC pasa los <b>siete knock-outs</b> sin ambigüedad —el sistema incluso nombra "
        f"explícitamente a TSMC como \"capacidad de élite\" exenta de penalización por intensidad de "
        f"capex—. Sobre las once reglas obtiene <b>{D.es(D.SCORE_QG,1)}/100 (raw {D.es(D.RAW_QG,1)}/125), "
        f"tier {D.TIER_QG}</b> — verificado sin corrección por tres métodos aritméticos independientes. "
        f"Una sola regla concentra casi todo el descuento frente a lo que, de otro modo, sería un score de "
        f"Núcleo:")]
    o += [M.p("<b>R6 · Diversificación — el único freno real, y el más severo de toda la campaña.</b> Dos "
        "clientes representan más del 15% del ingreso cada uno (~19% y ~17%, convergiendo el uno hacia el "
        "otro), y los diez clientes principales concentran el 78% del ingreso total —una concentración de "
        "clientes ya severa por sí sola—. Pero el componente decisivo de esta regla es geográfico: casi el "
        "100% de la producción de semiconductores de punta del mundo está físicamente concentrada en un "
        "solo territorio, Taiwán, cuya situación geopolítica con China se ha deteriorado de forma "
        "documentable durante 2026 —simulacros militares con fuego real, retraso de un paquete de armas "
        "estadounidense de US$14.000 millones descrito por el propio presidente de EEUU como \"ficha de "
        "negociación\"—. Un ex-presidente de TSMC ya confirmó públicamente un plan de auto-inutilización "
        "de las fábricas ante un escenario de invasión. Score: 2/10, el más bajo de toda esta campaña de "
        "tesis. [HECHO]")]
    o += [ch("04_concentracion_clientes", 14.4), sp(2)]
    o += [M.p("<b>El hallazgo de proceso más importante de esta tesis: el sistema no tiene un gate "
        "dedicado para este tipo de riesgo.</b> Tanto el agente de scoring como su verificador adversarial "
        "revisaron explícitamente los siete knock-outs (G1-G7) del sistema qg-seilern buscando uno que "
        "cubriera \"concentración geográfica catastrófica de punto único de falla\" — y ambos concluyeron, "
        "de forma independiente, que <b>no existe tal gate</b>. El sistema resuelve el riesgo de Taiwán "
        "enteramente a través de R6, por diseño explícito (el archivo de reglas indica que \"el knock-out "
        "VIE + exclusiones cubren lo grave\"), no por descuido. Es una decisión de diseño defendible, pero "
        "significa que <b>toda la diferencia entre \"Alta Convicción\" (78,4) y \"Núcleo\" (85+) para TSMC "
        "cuelga de una sola variable de ponderación</b> — vale la pena que quede documentado con esa "
        "precisión, en vez de disolverse en el promedio general del score.")]
    o += [M.p("<b>R7 · Capital/ROIC, con cifras que sostienen la etiqueta \"disciplinado\" más allá de la "
        "narrativa.</b> La política de dividendo de TSMC es explícita y pública: \"sostenible y creciente "
        "cada año, nunca por debajo del período anterior\" —el dividendo trimestral subió de NT$3,0 (2010) "
        "a NT$4,5 (2015) y a NT$6,0 en el pago de julio de 2026, sin un solo recorte en al menos 15 años, "
        "con un payout ratio moderado de ~30-31% de las utilidades [HECHO]—. Las recompras, en cambio, son "
        "históricamente triviales y de propósito técnico —compensar la dilución de planes de acciones a "
        "empleados, no devolver capital de forma material—: el programa de junio de 2024 fue de apenas "
        "~US$100 millones, frente a un capex anual de US$40.900 millones ese mismo año [HECHO]. En M&A, la "
        "evidencia es negativa por ausencia: no hay adquisiciones relevantes en la última década; el "
        "precedente más citado es 2007, cuando TSMC amplió su participación en Vanguard International "
        "Semiconductor y declaró explícitamente que \"no tenía intención de fusionarse\" con esa compañía "
        "[HECHO]. El capex es, por diseño más que por falta de oportunidades, el único vehículo real de "
        "asignación de capital de la empresa [INFERENCIA]. Esa disciplina se confirma también en el track "
        "record de guidance de capex: en ninguno de los últimos cinco años (2021-2025) la gerencia falló "
        "el rango que ella misma guio —aunque tiende a aterrizar en los extremos del rango según el ciclo "
        "(2023 y 2024 en el extremo bajo, 2025 en el extremo alto), no en el punto medio [HECHO/INFERENCIA]—.")]
    o += [M.p("<b>Lo que sostiene el score en un nivel excepcional pese a ese freno:</b> R5 crecimiento "
        "orgánico 10/10 (el caso más limpio de máxima puntuación de toda la campaña), R8 balance 10/10 "
        "(caja neta positiva de magnitud extraordinaria), R4 moat 13/15 y R3 liderazgo 13/15 (dominio "
        "casi monopólico, ganando cuota activamente). Calibrada contra las anclas del sistema: TSMC queda "
        "cerca del techo de Alta Convicción, con Núcleo a un solo ajuste de ponderación de distancia.")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def s5():
    o = M.flag_titulo("§5 · El moat", "Cuatro murallas que ni veinte años de inversión rival han logrado escalar")
    o += [ch("13_porter", 14.0), sp(2)]
    o += [M.p("Un foso competitivo (moat, en la terminología de Warren Buffett: la ventaja estructural que "
        "protege las ganancias de una empresa de la erosión por competencia) rara vez se sostiene en una "
        "sola defensa. El de TSMC combina cuatro murallas simultáneas, cada una defendible por separado: "
        "(1) <b>escala de capital</b> — US$28.000 millones para una fábrica competidora de 2nm, repetido "
        "en cada generación de proceso, como una cuota de entrada que sube cada vez que el juego se pone "
        "más difícil; (2) <b>curva de aprendizaje de procesos</b> acumulada durante casi cuarenta años, "
        "que Samsung e Intel no han logrado igualar pese a inversión masiva —el conocimiento operativo "
        "tácito no se compra, se acumula turno a turno—; (3) <b>control del cuello de botella real</b> "
        "—el empaquetado avanzado (CoWoS), no la oblea, es lo que realmente limita la oferta de chips de "
        "IA, y TSMC lo controla directamente—; y (4) <b>costos de cambio</b> (switching costs: lo que le "
        "cuesta a un cliente abandonar un proveedor, más allá del precio) severos para cualquier cliente "
        "que quiera migrar un diseño a otra fundición, dado los ciclos de diseño de 2-4 años y la "
        "certificación de IP/PDK (Process Design Kit, el conjunto de reglas y modelos específico de cada "
        "fábrica que un diseño de chip debe respetar) propia de cada proceso. [HECHO/INFERENCIA]")]
    o += [M.p("La única grieta genuina, no hipotética: Samsung ganó su primer contrato real de un cliente "
        "de primer nivel —el próximo chip AI6 de Tesla, en un acuerdo de US$16.500-17.000 millones, el "
        "mayor contrato de fundición individual en la historia de Samsung—. No es una brecha en la "
        "muralla; es la primera prueba, después de veinte años de intentos fallidos, de que un cliente "
        "sofisticado y bien capitalizado está dispuesto a asumir el riesgo de doble-abastecimiento en un "
        "chip crítico de IA. Sigue siendo la excepción, no la regla —Intel Foundry, en contraste, todavía "
        "no tiene \"clientes externos significativos a escala\" según su propio lenguaje de riesgo ante la "
        "SEC— pero es una grieta real, no una amenaza rumoreada. [HECHO]")]
    o += [M.callout("PAUSA REFLEXIVA",
        "El proveedor que sostiene todo este moat —ASML, con un monopolio absoluto sobre la litografía "
        "EUV (Extreme Ultraviolet, la tecnología de grabado óptico necesaria para fabricar en los nodos "
        "más avanzados)— es, paradójicamente, la única fuerza de Porter genuinamente adversa para TSMC. "
        "Es la ironía central del moat: TSMC construyó cuatro murallas casi perfectas alrededor de su "
        "fortaleza, pero no controla la cantera de la que sale la piedra. No controla su propio insumo "
        "más crítico; depende por completo de un único proveedor. La mitigación es real (TSMC es el "
        "cliente más grande y estratégicamente importante de ASML, con prioridad de asignación), pero no "
        "elimina la dependencia estructural. Es la única grieta en un moat que, de otro modo, se acerca a "
        "lo que Buffett llamaría un foso económico perfecto.")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def s6():
    o = M.flag_titulo("§6 · El campo de batalla competitivo", "Dos rivales invierten decenas de miles de millones; ninguno ha movido la pieza que importa")
    o += [M.tabla([
        ["Rival", "Estado del proceso de punta", "Situación"],
        ["Samsung Foundry", "Rendimiento de 2nm volátil (40-70% según fuente/fecha)", "Primer contrato real de cliente top-tier (Tesla AI6, $16.500-17.000M)"],
        ["Intel Foundry", "18A en producción de volumen desde fin-2025", "Sin clientes externos significativos a escala (lenguaje propio ante la SEC); pérdidas operativas de $2.300-3.200M/trimestre"],
        ["SMIC / GlobalFoundries", "Nodos maduros, sin ambición de punta declarada", "No compiten en el segmento que importa para esta tesis"],
    ], [3.4*cm, 6.6*cm, 6.4*cm], font_sz=7.6)]
    o += [M.p("<b>La brecha de proceso se está cerrando en el papel, no en la práctica.</b> Los tres "
        "rivales (TSMC, Samsung, Intel) ahora se anuncian en nodos \"de 2 nanómetros\" —una convergencia "
        "de marketing que, vista de lejos, sugiere una carrera pareja—. Pero el rendimiento real a escala "
        "de volumen (yield, el porcentaje de chips fabricados que salen sin defectos y son vendibles) "
        "sigue siendo muy distinto: TSMC reporta rendimientos de 60-80% en su N2, mientras Samsung reporta "
        "cifras dispersas e inconsistentes entre 40% y 70% según la fuente y la fecha —una variabilidad "
        "que en sí misma es una señal de menor control de proceso, como un ajedrecista cuyo tiempo por "
        "jugada varía sin ningún patrón—. La brecha práctica de rendimiento-a-volumen se estima en "
        "1,5-2,5 años a favor de TSMC, incluso cuando la brecha de nomenclatura de nodo (\"todos dicen "
        "2nm\") nunca ha sido más estrecha en la última década. [HECHO/INFERENCIA]")]
    o += [M.p("<b>El giro hacia chips de IA a medida (ASICs, Application-Specific Integrated Circuits: "
        "chips diseñados a medida para una sola tarea, en vez de chips de propósito general) no es una "
        "amenaza para TSMC — es, en la práctica, neutral a positivo.</b> Google (TPU), Amazon (Trainium), "
        "Microsoft (Maia) y Meta (MTIA) están construyendo sus propios chips de IA para reducir su "
        "dependencia de las GPU de Nvidia —cada uno cree estar jugando una partida distinta, escapando del "
        "proveedor común—. Pero <b>todos y cada uno de esos chips a medida se fabrican en TSMC</b>, en su "
        "mayoría sobre el mismo nodo de 3 nanómetros. El \"sustituto\" de la GPU de Nvidia no es un "
        "sustituto de la oblea de TSMC: es, simplemente, un jugador distinto sentado a la misma mesa. "
        "[HECHO]")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def s7():
    o = M.flag_titulo("§7 · Porter: cinco fuerzas y la contradicción central", "Posición casi ideal para un incumbente — salvo por un único proveedor")
    o += [ch("13_porter", 14.4), sp(2)]
    o += [M.p("Las Cinco Fuerzas de Porter describen una posición estructuralmente cercana a la ideal para "
        "un incumbente: amenaza de nuevos entrantes prácticamente nula (1/5, barreras de capital y "
        "técnicas extremas), rivalidad moderada-baja (2/5, Samsung e Intel invierten pero no capturan cuota "
        "significativa), sustitutos neutros-a-favorables (2/5, los ASICs personalizados también se "
        "fabrican en TSMC), y poder de clientes moderado (2/5, la concentración es real pero se invierte "
        "en dependencia porque los clientes no tienen alternativa de volumen). La única fuerza claramente "
        "adversa es el poder de proveedores (4/5): ASML tiene un monopolio absoluto sobre la litografía EUV "
        "que TSMC necesita para fabricar en los nodos más avanzados. [análisis propio]")]
    o += [M.callout("PAUSA REFLEXIVA",
        "Contradicción Porter↔Seilern: Porter puntúa la posición competitiva general de TSMC como casi "
        "ideal (ponderado 2,2/5, muy favorable), mientras R6 del sistema Seilern la penaliza severamente "
        "(2/10). El mecanismo de reconciliación: Porter mide la dinámica de mercado —competidores, "
        "clientes, proveedores, sustitutos— mientras R6 mide algo distinto y más fundamental: el riesgo de "
        "que el activo físico completo deje de existir o de operar por una causa ajena a la dinámica "
        "competitiva. Ningún rival puede replicar el moat de TSMC compitiendo mejor; solo un evento "
        "geopolítico podría neutralizarlo de un plumazo. Son dos preguntas distintas, y el sistema hace "
        "bien en no promediarlas en un solo número.")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def s8():
    o = M.flag_titulo("§8 · TAM, SAM, SOM, runway y catalizadores", "El mercado ya es de TSMC; el reto es defender el cuello de botella, no ganar cuota")
    o += [ch("14_tam", 15.0), sp(2)]
    o += [M.p("El mercado global de fundición (~US$190.000 millones en 2026) creció 30% interanual solo en "
        "el primer trimestre —muy por encima de cualquier estimado de crecimiento a largo plazo—, "
        "confirmando que la demanda de IA está corriendo por delante de cualquier modelo de \"estado "
        "estacionario\". TSMC ya captura ~72% de ese mercado y más del 92% proyectado del segmento de punta "
        "(&lt;5nm) específicamente —el margen de ganancia de cuota adicional es limitado no porque el "
        "negocio se esté agotando, sino porque ya domina casi por completo el segmento que importa. "
        "[HECHO/INFERENCIA]")]
    o += [M.p("<b>Catalizadores 2026-2028:</b> (1) rampa del nodo N2 (2 nanómetros), con management "
        "confirmando que será estructuralmente más rentable que N3 incluso durante la fase de ramp-up; (2) "
        "expansión de capacidad de empaquetado avanzado CoWoS de ~35.000 obleas/mes (2024) a ~170.000 "
        "obleas/mes (2027e) —triplicando la capacidad del cuello de botella real de la IA—; (3) "
        "diversificación geográfica en Arizona (con rentabilidad ya confirmada en su primer año completo, "
        "aunque parcialmente favorecida por subsidios del CHIPS Act) y Japón; (4) el guidance de CAGR de "
        "cinco años ya elevado de ~20% a ~25%, con la propia gerencia elevando también el guidance de "
        "crecimiento de aceleradores de IA de ~50% a 56-59%. [HECHO los datos; SUPUESTO las trayectorias]")]
    o += [M.p("<b>La apuesta central de 2026, en una sola cifra: dónde va el capex incremental.</b> La "
        "gerencia reasignó su capex 2026 casi por completo hacia el nodo N3/N2 avanzado y el empaquetado "
        "CoWoS para capturar este ciclo: el guidance salta a US$52.000-56.000 millones —el extremo alto "
        "del rango, +30% interanual y récord histórico de la compañía—, con más del 70% dirigido "
        "específicamente a nodos avanzados [HECHO, guidance Q1 2026]. La mejor evidencia de que la "
        "gerencia no solo cumple sino que supera su propia proyección: el guidance de ingresos por "
        "aceleradores de IA pasó de \"CAGR medio-40%\" para 2024-2029 (dado en la call de resultados de "
        "Q4 2024) a \"CAGR medio-alto 50%\" (dado en la call de Q4 2025) —una revisión al alza de la "
        "propia gerencia sobre su propia guía, no una lectura optimista de un analista externo [HECHO]—.")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def s9():
    o = M.flag_titulo("§9 · Valoración multi-método", "El output de val-mos: el negocio pasa limpio, el precio no")
    o += [M.p("<b>Paso 0 — detector de trampas: PASA, sin matices.</b> El test decisivo (¿ingresos, margen "
        "y ROE siguen creciendo pese a la narrativa bajista?) responde SÍ de forma inequívoca y en todas "
        "las dimensiones simultáneamente: margen operativo 42,6%→58,1%, margen neto 39,4%→50,5%, ROE "
        "32,7%→40,5%, ingresos +35-40% interanual. Ningún trimestre de deterioro en toda la ventana "
        "analizada. El overlay de burbuja sectorial (aplicado al conjunto correcto de comparables — "
        "fundiciones rentables, no la periferia especulativa de IA) confirma solo 1-2 de 7 señales activas, "
        "insuficiente para activar el candado sectorial reforzado. [val-mos]")]
    o += [ch("02_margenes", 14.4), sp(2)]
    o += [M.p("<b>Paso 1 — DCF inverso: el precio exige superar el propio guidance ya elevado de la "
        "gerencia.</b> Al precio de referencia del modelo (~US$477), el crecimiento implícito de owner "
        "earnings es 36,0% (con prima geopolítica en el WACC) o 26,3% (sin prima) — en ambos casos por "
        "encima del guidance de management (~25%, ya una revisión al alza inusual). Clasificación: "
        "<b>HEROICAS</b> en ambos escenarios, aunque el caso sin prima es un HEROICAS de margen estrecho "
        "(solo 1,3 puntos porcentuales por encima del guidance). [DCF inverso]")]
    o += [ch("10_dcf_inverso", 14.6)]
    o += [M.p("<b>Paso 2 — PWFV-Valor: la prima geopolítica, por sí sola, mueve el valor 34%.</b> Sobre "
        "owner earnings normalizados, el DCF de tres escenarios da US$360 sin ajuste por riesgo país, y "
        "<b>US$236 incorporando honestamente una prima de +250 puntos básicos por la concentración "
        "geográfica de Taiwán</b> (confirmada como severa y estructural por la verificación adversarial "
        "del eje calidad). Es el ajuste de tasa de descuento más grande de toda esta campaña de tesis, y "
        "se aplica aquí como ancla primaria —explícitamente, no como default silencioso— precisamente "
        "porque R6 ya estableció que este riesgo es real, no hipotético. La prima, al ser permanente "
        "(se aplica a perpetuidad en el WACC, no a un solo año), se ancla deliberadamente a "
        f"probabilidades de <b>horizonte largo</b>, verificadas en vivo y exactas: {D.pct(D.PROB_INVASION_2027)} "
        f"acumulado a 2027 y {D.pct(D.PROB_INVASION_2030)} a 2030 ({D.PROB_FUENTE}) — no al spot de "
        "corto plazo de mercados de eventos (más ruidoso y de horizonte equivocado para lo que este "
        "ajuste está compensando).")]
    o += [ch("11_wacc", 13.4), sp(2)]
    o += [M.p(f"<b>Cross-check — ROIC incremental, verificado en vivo (10-jul-2026).</b> Para probar si "
        "el capex de punta (N3/N2/CoWoS) realmente convierte en utilidad, se recomputó ΔUtilidad "
        f"operativa/ΔActivos sobre cinco ventanas de 2021 a 2025 ({D.ROIC_INCR_FUENTE}). El caso central "
        f"(ciclo completo 2021→2025) da <b>{D.pct(D.ROIC_INCR_CENTRAL)}</b>; la ventana más favorable "
        f"probada (2023→2025) da {D.pct(D.ROIC_INCR_RECIENTE)}; incluso la ventana más débil probada "
        f"(2021→2023, que no es una elección generosa: es la más conservadora) da {D.pct(D.ROIC_INCR_MINIMO)} "
        f"— <b>las cinco ventanas superan ambos WACC</b> ({D.es(D.WACC_SIN_PRIMA,2)}%-{D.es(D.WACC,2)}%). "
        f"Un solo año de la serie fue negativo ({D.pct(D.ROIC_INCR_NEG_2022_23)}, 2022→2023), reportado "
        "sin ocultarlo. Dos advertencias, no dos objeciones: primero, este cálculo es MENOS comparable "
        "con el mismo ejercicio hecho para AWS de lo que la analogía \"ambos con ROIC incremental sólido\" "
        "sugiere a primera vista — AWS se mide sobre activos DE SEGMENTO en una ventana de 1 año; TSM no "
        "reporta segmentos, así que aquí se usan activos DE TODA LA COMPAÑÍA sobre ventanas de 1 a 5 "
        f"años (la ventana literalmente equivalente a la de AWS, 2024→2025, da {D.pct(D.ROIC_INCR_AWS_EQUIV)} "
        "sobre activos — más favorable aún que el caso central, así que la diferencia metodológica no "
        "esconde nada desfavorable). Segundo, el método de dos puntos asume que el retorno de la base de "
        "capital vieja se mantuvo constante y le atribuye todo el aumento de utilidad al capital nuevo: "
        "parte de la expansión de margen operativo (42,6%→58,1% entre 2023 y Q1'26) es la maduración real "
        "de N3 bajo prueba, pero parte podría ser poder de fijación de precios sobre fábricas ya "
        "existentes antes de 2021 — un sesgo que ninguna versión anterior de esta tesis había declarado. "
        "Ninguna de las dos advertencias mueve el número por sí sola; ambas quedan documentadas para que "
        "el lector sepa exactamente qué tan fuerte es esta pata del argumento.")]
    o += [M.p("<b>El candado duro anti-sobrepago es la segunda pared, independiente de la anterior.</b> "
        f"Sobre owner earnings de 2025 (año base, deprimido por el pico de capex), el múltiplo pagado hoy "
        f"es <b>{D.es(D.MULT_NORMALIZADO,1)}x</b>; incluso usando la lectura más favorable posible (owner "
        f"earnings estimados de 2026, con ingresos guiados a crecer &gt;30%), el múltiplo es "
        f"<b>{D.es(D.MULT_FY26E,1)}x</b> — ambas lecturas violan por un margen amplio tanto el techo "
        f"específico del tier de TSM (30x) como el candado genérico (30-40x), y este candado <b>no tiene "
        f"excepción de tier ni de patrón</b>: es la única pared del sistema sin excepciones.")]
    o += [ch("09_candado_duro", 14.4), sp(2)]
    o += [ch("12_sensibilidad", 14.4)]
    o += [M.p(f"<b>Sensibilidad.</b> Cruzando WACC ({D.WACC_GRID[0]}-{D.WACC_GRID[-1]}%, ya incluyendo la "
        f"prima geopolítica) × crecimiento terminal ({D.GT_GRID[0]}-{D.GT_GRID[-1]}%), el valor se mueve "
        f"entre US${D.SENS[-1][0]} y US${D.SENS_MAX} — un rango que <b>nunca alcanza el precio de hoy</b> "
        f"ni siquiera en el escenario más generoso combinado con el WACC más bajo del rango.")]
    o += [ch("08_zonas", 15.2)]
    o += [ch("16_ev_ebitda", 13.6)]
    o += [M.p(f"<b>Paso 3 — zonas y veredicto.</b> Zona {D.ZONA_HOY} (con prima geopolítica) o Caro (sin "
        f"prima, referencia de sensibilidad): ambas lecturas convergen en \"no comprar hoy\". El EV/EBITDA "
        f"actual está 124% por encima de la propia mediana de 10 años de TSMC —una segunda métrica, sin "
        f"relación con el DCF, que confirma el mismo estiramiento extremo por una vía completamente "
        f"independiente—. El candado de expectativas (activado por la clasificación HEROICAS) exige zona "
        f"Ganga específicamente, no solo Oportunidad, y sube el MoS exigido de 25% a 35%. <b>Veredicto: "
        f"{D.VEREDICTO}.</b> A diferencia de un veredicto pasivo, VIGILAR refleja que el detector de "
        f"trampas dio PASA limpio y que hay gatillos de precio cuantificados y relativamente cercanos.")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def s10():
    o = M.flag_titulo("§10 · Gestión, cultura y gobernanza", "Ejecución excepcional, con dos límites estructurales que ningún track record compra de vuelta")
    o += [M.p("Cuando Morris Chang se retiró definitivamente en junio de 2018 —esta vez sin retorno, a "
        "diferencia de su reaparición de 2009 (ver §1)—, no dejó un sucesor único: dividió el poder entre "
        "Mark Liu como Presidente y C.C. Wei como CEO, una estructura de \"dos capitanes\" diseñada "
        "explícitamente para que ninguna persona concentrara el control total de la empresa que él mismo "
        "había fundado tres décadas antes. [HECHO]")]
    o += [M.p("C.C. Wei ha sido CEO desde 2018 y, desde junio de 2024, también Presidente, tras suceder a "
        "Mark Liu —la estructura de \"dos capitanes\" que Chang diseñó duró exactamente seis años—. Su "
        "historial de ejecución en solitario es notable incluso para los estándares de esta campaña de "
        "tesis: guías de crecimiento elevadas (de ~20% a ~25% de CAGR a cinco años) que la propia empresa "
        "ha superado en los trimestres siguientes, márgenes en expansión constante, y una rampa de "
        "Arizona que llegó a producción de volumen antes de lo originalmente planeado y ya es rentable en "
        "su primer año completo. [HECHO]")]
    o += [ch("15_mgmt", 13.2), sp(2)]
    o += [M.p("<b>Los dos límites que el sistema no puede ignorar.</b> Primero, el que ya se anticipó: "
        "consolidar Presidente y CEO en una sola persona deshace, exactamente, la separación de poder que "
        "Chang había diseñado a propósito seis años antes —una concentración de poder, no una falta de "
        "competencia, pero un retroceso de gobernanza medible frente al propio diseño del fundador—. "
        "Segundo, y más importante: TSMC no es un actor puramente comercial en sus decisiones de expansión "
        "geográfica y asignación de capital. El Fondo Nacional de Desarrollo de Taiwán mantiene una "
        "participación de 6,38% —la misma institución estatal que, en 1987, aportó la mitad del capital "
        "fundacional de la empresa (ver §1); no controladora hoy, pero simbólicamente significativa—, y la "
        "empresa ha confirmado un compromiso de inversión de US$165.000 millones en Estados Unidos en "
        "parte como concesión política a la presión comercial de Washington, no como decisión de "
        "asignación de capital puramente basada en retorno. El propio C.C. Wei ha tenido que desmentir "
        "públicamente reportes de que el gobierno estadounidense buscaba una participación accionaria en "
        "la empresa —una señal de que la cuestión de la influencia estatal (de ambos gobiernos) está "
        "activamente en disputa, no resuelta. [HECHO]")]
    o += [M.p("<b>La fricción cultural de Arizona, un dato operativo y no solo simbólico.</b> La cultura "
        "de TSMC en Taiwán incluye turnos nocturnos obligatorios de 12 horas y llamadas de emergencia a "
        "mitad de la noche para mantener las fábricas funcionando las 24 horas —una disciplina operativa "
        "que, sostenida durante casi cuarenta años, es en sí misma parte del moat: nadie replica ese ritmo "
        "de trabajo por decreto—. Trasplantar esa cultura a Arizona ha generado choques visibles y "
        "documentados: empleados estadounidenses reportan tensión frente a expectativas de horario "
        "\"estilo Taiwán\" que no forman parte del contrato implícito del mercado laboral local. [HECHO] "
        "No es un dato menor para leer la dilución de margen que la propia gerencia admite abiertamente: "
        "Arizona resta 2-3 puntos porcentuales al margen bruto consolidado durante 2026, ampliándose a 3-4 "
        "puntos al escalar la operación [HECHO, guidance oficial]. Pero en ningún call reciente (revisados "
        "los transcripts de Q1 a Q4 de 2025 y 2026) la gerencia ha publicado una comparación explícita del "
        "ROIC de Arizona frente al de Taiwán [HECHO por ausencia]. Que esa cifra no exista en el discurso "
        "corporativo, cuando sí existe con precisión para la dilución de margen, es razonable leerlo como "
        "que el retorno de ese capex forzado por Washington hoy es inferior al retorno doméstico —aunque "
        "esto es, explícitamente, un supuesto y no una cifra confirmada [SUPUESTO justificado].")]
    o += [M.p("<b>Lo que esto significa en la práctica:</b> un accionista minoritario debe asumir que, en "
        "una crisis genuina, el directorio y la gestión de TSMC podrían verse obligados a tomar decisiones "
        "—como priorizar el suministro al gobierno o ejército de EEUU sobre clientes comerciales, o "
        "activar el plan de auto-inutilización ya confirmado— que no son necesariamente las que un actor "
        "puramente comercial elegiría. Score de gestión: <b>20/30</b>. [HECHO/INFERENCIA]")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def s11():
    o = M.flag_titulo("§11 · Nueve inversores legendarios opinan", "El negocio convence a todos; el riesgo geopolítico y el precio dividen al panel")
    o += [ch("18_inversores", 15.0), sp(2)]
    pares = [
        ("Graham", "PASS", "Sin margen de seguridad bajo ninguna lectura razonable de beneficios normalizados; su regla de balance se cumple con holgura, pero eso no compensa un múltiplo que rompe cualquier candado clásico."),
        ("Buffett", "PASS", "Admira el moat (posiblemente el más ancho de este portafolio) pero su famosa regla del \"círculo de competencia\" geopolítico —y su propia decisión histórica de reducir exposición a Taiwán— pesa más que la calidad del negocio."),
        ("Munger", "HOLD", "Invierte la pregunta: ¿qué lo mata? No la ejecución —es impecable—. Lo que le preocupa es un evento de cola binario que ningún múltiplo de seguridad puede compensar del todo."),
        ("Fisher", "HOLD", "El scuttlebutt es abrumadoramente positivo en el producto (cuota, márgenes, guidance elevado y cumplido); pero su disciplina de \"comprar cuando el precio lo permite\" no está satisfecha hoy."),
        ("Lynch", "PASS", "La historia es fácil de contar (\"todos los chips de IA del mundo pasan por aquí\"), pero el PEG deja de verse razonable cuando el crecimiento implícito ya supera el propio guidance elevado de la gerencia."),
        ("Templeton", "PASS", "No hay pesimismo máximo que comprar: consenso alcista, precio cerca de máximos históricos. Este no es su terreno hoy, aunque podría serlo tras una corrección genuina de sentimiento geopolítico."),
        ("Marks", "HOLD", "¿Dónde estamos en el ciclo? El descuento geopolítico se está reduciendo justo cuando el riesgo subyacente no mejora — la definición casi de manual de un mercado que extrapola \"nada ha pasado\" hacia \"nada pasará\"."),
        ("Seilern", "HOLD", "Calidad 78,4/100: Alta Convicción, a un ajuste de ponderación de Núcleo. Su estándar de calidad está satisfecho; su disciplina de precio, no."),
        ("Terry Smith", "HOLD", "\"No pagues de más\" se incumple con el candado duro violado por un margen amplio; pero reconoce que este es, con diferencia, el negocio de mayor calidad intrínseca de esta ronda de análisis."),
    ]
    filas = [["Inversor", "Veredicto y razonamiento en una línea"]]
    for nm, vd, txt in pares:
        filas.append([f"<b>{nm}</b><br/><font size=7 color='#666054'>{vd}</font>", txt])
    o += [M.tabla(filas, [2.5*cm, 13.9*cm], font_sz=7.8)]
    o += [M.callout("PAUSA REFLEXIVA",
        "A diferencia de MELI (donde el panel dudaba de la disciplina de asignación de capital) o GOOGL "
        "(donde dudaba de la gobernanza), aquí el panel no encuentra ningún defecto de negocio que "
        "objetar — la división es puramente sobre cómo pesar un riesgo binario y geopolítico que, por "
        "definición, no se puede modelar con la misma precisión que un flujo de caja. Es la tesis más "
        "incómoda de construir de toda esta campaña, precisamente porque el negocio no da ninguna excusa "
        "fácil para justificar cautela.")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def s12():
    o = M.flag_titulo("§12 · Riesgos: matriz, pre-mortem y alerta temprana", "Un solo riesgo de impacto máximo domina toda la matriz")
    o += [ch("17_riesgos", 15.2), sp(2)]
    o += [M.p("El riesgo dominante (impacto 5, probabilidad 2) es un bloqueo o cuarentena naval de Taiwán "
        "—no una invasión, escenario considerado menos probable y más disruptivo para los propios intereses "
        "chinos—. En ajedrez, un jaque mate no exige capturar al rey: basta con quitarle todas las casillas "
        "a las que puede moverse. Un bloqueo logra el mismo efecto sobre TSMC sin disparar un solo tiro: "
        "corta el acceso de la isla al mundo con un umbral militar mucho menor que una invasión y sin un "
        "\"evento gatillo\" claro que active una respuesta automática de EEUU. El segundo riesgo "
        "(probabilidad 4, impacto 4) es, de hecho, el más simple de los dos: la valoración ya está "
        "estirada incluso antes de considerar el riesgo geopolítico. [análisis propio]")]
    o += [M.p("<b>Un segundo riesgo de concentración geográfica, distinto del militar: el límite físico "
        "del propio territorio.</b> Más allá del riesgo de bloqueo o invasión, TSMC podría absorber hasta "
        "~24% del consumo eléctrico total de Taiwán para 2030 [HECHO], y un reporte de 2024 estimó que la "
        "red eléctrica de la isla solo tiene margen para ~20 fábricas grandes adicionales antes de tocar "
        "el techo de suministro [HECHO] —como una especie que ya ocupa casi todo el hábitat disponible de "
        "su propio ecosistema, sin espacio físico para seguir creciendo donde nació—. En agua, la planta "
        "de reciclaje de Tainan alcanzará 36.000 toneladas/día para 2026, cubriendo ~60% de la necesidad "
        "local de TSMC [HECHO]: un mitigante parcial, no una solución total, del mismo límite físico. Este "
        "riesgo no compite con el geopolítico ni lo reemplaza —son dos restricciones distintas al mismo "
        "territorio único— pero confirma que incluso en un escenario sin ningún deterioro militar, la "
        "concentración en Taiwán tiene un techo de infraestructura que eventualmente exige diversificación "
        "geográfica real, no solo simbólica. [análisis propio]")]
    o += [ch("19_riesgo_taiwan", 15.4), sp(2)]
    o += [M.p("<b>Pre-mortem narrativo.</b> Es 2030 y la inversión salió mal. ¿Qué pasó? No fue "
        "necesariamente una invasión: fue un bloqueo naval de varias semanas en 2027, suficiente para "
        "detener el 90% del comercio marítimo de Taiwán sin que China disparara un solo misil contra "
        "territorio estadounidense o japonés —el escenario que los críticos del \"escudo de silicio\" "
        "(silicon shield, la teoría de que la dependencia mundial de los chips de TSMC disuadiría a China "
        "de atacar Taiwán) llevaban años advirtiendo como el más probable y el menos preparado—. El precio "
        "de TSM, que en 2026 ya cotizaba con un descuento geopolítico en contracción, no tenía ningún "
        "colchón de valoración cuando el riesgo se materializó. La lección retrospectiva no fue \"TSMC era "
        "un mal negocio\" —seguía siendo el mejor fabricante del mundo, el mismo que en 2009 supo invertir "
        "a contraciclo cuando el riesgo que enfrentaba era financiero (ver §1)— sino \"el precio nunca "
        "reflejó honestamente la probabilidad, por baja que fuera, de un evento de cola con impacto total, "
        "porque ese riesgo no se compra con más capex ni se resuelve con mejor ejecución\".")]
    o += [ch("20_early_warning", 15.4), sp(2)]
    o += [M.p("<b>Sistema de alerta temprana.</b> El semáforo tiene tres verdes sólidos (margen, "
        "crecimiento de IA, ROE), tres ámbar de vigilancia activa (múltiplo estirado, concentración de "
        "clientes, un segundo caso de doble-abastecimiento) y una fila roja permanente (el riesgo "
        "geopolítico de Taiwán) que no es una alerta transitoria sino un hecho estructural a vivir con él. "
        "<b>Regla dura:</b> cualquier escalada real de tensión militar (más allá de drills rutinarios ya "
        "descontados) o una segunda venta confirmada de Samsung/Intel a un cliente top-10 más allá del caso "
        "Tesla debería activar una revisión inmediata del tier de calidad y de la prima geopolítica en el "
        "WACC, sin esperar al ciclo trimestral normal.")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def s13():
    o = M.flag_titulo("§13 · Veredicto final, triggers y proyección", "VIGILAR: el mejor negocio de la cartera, a un precio que no deja margen para el riesgo que sí existe")
    o += [M.p(f"<b>Cruce de los dos ejes.</b> CALIDAD <b>{D.es(D.SCORE_QG,1)}/100 · tier {D.TIER_QG}</b> "
        f"(verificado sin corrección, confirmado por tres métodos aritméticos independientes). VALORACIÓN "
        f"<b>{D.VEREDICTO}</b> (ratificado en §9): detector PASA limpio, PWFV US${D.PWFV} (con prima "
        f"geopolítica), zona {D.ZONA_HOY} — el candado duro violado por un margen amplio incluso en la "
        f"lectura más favorable, y el precio ya por encima del propio guidance elevado de management "
        f"traducido a valor. Los dos ejes convergen en una conclusión poco habitual para esta campaña: "
        f"<b>no hay ningún defecto de negocio que objetar — el freno completo es que el precio de hoy no "
        f"deja ningún margen para un riesgo de cola que, por definición, no se puede eliminar del modelo, "
        f"solo pesar correctamente.</b> Una verificación adversarial dedicada (10-jul-2026) intentó mover "
        f"este ancla por dos vías —ROIC incremental y probabilidades geopolíticas— y no encontró base "
        f"para hacerlo: US${D.PWFV} se sostiene, con un sesgo residual hacia conservador, no agresivo "
        f"(ver §9 y changelog).")]
    o += [M.p("<b>Frase-tesis (registrada para el feedback loop).</b> «TSMC es, con diferencia, el mejor "
        "negocio puro de este portafolio: moat casi imposible de replicar, márgenes en récord, balance en "
        "caja neta positiva, sin un solo trimestre de deterioro. Pero casi el 100% de esa excelencia está "
        "físicamente concentrada en un territorio cuya tensión geopolítica se documentó, no se especuló, "
        "durante 2026 — y el mercado decidió justo este año reducir el descuento por ese riesgo en vez de "
        "ampliarlo. El precio de hoy no solo ignora esa tensión: apuesta activamente a que seguirá "
        "reduciéndose.»")]
    o += [M.p("<b>Elemento falsable.</b> Reconsideraría la tesis hacia comprar si el precio cae a la zona "
        "de Oportunidad o Ganga por razones de sentimiento general de mercado (no por deterioro real del "
        "negocio, que el detector de trampas confirma que no existe hoy). Reconsideraría la tesis hacia "
        "más cautela si una segunda venta de Samsung o Intel a un cliente top-10 se confirma en los "
        "próximos 4-6 trimestres (evidencia de que el moat se erosiona más rápido de lo modelado), o si la "
        "tensión geopolítica escala más allá de drills rutinarios.")]
    o += [M.tabla([
        ["Plan operativo", "Nivel", "Acción"],
        ["Hoy", f"US${D.es(D.PRECIO,0)}", "VIGILAR — 0% de ampliación. Sostener lo que ya se tiene."],
        ["Gatillo Oportunidad", f"≤US${D.GATILLO_OPORT}", "Reconsiderar tramo si el detector sigue PASA"],
        ["Gatillo Ganga", f"≤US${D.GATILLO_GANGA}", "Tramo satélite pleno (el tier no permite núcleo)"],
        ["Disciplina de venta", "cualquiera", "Vender SOLO si el moat se rompe de verdad (2do caso Samsung/Intel confirmado); NUNCA por múltiplo aislado"],
    ], [5.0*cm, 3.4*cm, 8.0*cm], font_sz=7.8)]
    o += [M.p("<b>Proyección a 5 años (3 escenarios, desde el precio de referencia del modelo ~US$477, con "
        "prima geopolítica).</b> Optimista (25%): la demanda de IA sostiene el guidance elevado de 25% "
        "CAGR, la tensión de Taiwán no escala, el descuento geopolítico se mantiene estable — valor ~US$339, "
        "−29%. Base (50%): crecimiento converge hacia el guidance de management sin sorpresas, la tensión "
        "geopolítica ni escala ni se resuelve — valor ~US$232, −51%. Conservador (25%): Samsung/Intel ganan "
        "más terreno del esperado, o la tensión geopolítica se materializa parcialmente (sin llegar a "
        "bloqueo total) — valor ~US$142, −70%. <b>Ponderado: US$236, muy por debajo del precio de hoy bajo "
        "cualquier escenario razonable que incorpore honestamente el riesgo de Taiwán. Por eso: VIGILAR, "
        "con gatillos de precio cuantificados y activos.</b>")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def cierre():
    o = M.flag_titulo("Glosario y advertencias finales", "Términos, etiquetas y la naturaleza de este documento")
    o += [M.p("Esta tesis abrió con un hombre a quien rechazaron tres veces antes de que inventara un "
        "tablero donde nadie más podía jugarle. Cierra con la misma pregunta sin resolver desde 1987: "
        "¿cuánto vale un monopolio cuando el tablero entero está construido sobre una sola casilla que "
        "ninguna jugada de negocio puede mover? Los términos técnicos de este documento y sus advertencias "
        "metodológicas quedan documentados abajo, en el mismo registro seco que exige cualquier número que "
        "decida dinero real.")]
    o += [M.p("<b>Glosario.</b>", "h3")]
    gl = [
        ("Fundición pura (pure-play foundry)", "modelo de negocio donde la empresa solo fabrica chips diseñados por terceros, sin competir jamás con sus clientes en el diseño."),
        ("CoWoS", "Chip-on-Wafer-on-Substrate: tecnología de empaquetado avanzado que conecta múltiples chips — el cuello de botella real de la producción de IA, no la oblea."),
        ("Yield (rendimiento)", "porcentaje de chips fabricados en una oblea que salen sin defectos y son vendibles; la métrica que separa un nodo \"anunciado\" de un nodo realmente dominado a escala."),
        ("EPV", "valor de los beneficios sin crecimiento; suelo teórico de la valoración (US$49,2-69,3 según año base y prima geopolítica)."),
        ("EUV", "litografía ultravioleta extrema: la tecnología de fabricación de punta que ASML monopoliza globalmente."),
        ("PWFV-Valor", "valor intrínseco ancla del sistema val-mos (tri-método probabilístico)."),
        ("Prima geopolítica", "ajuste explícito de la tasa de descuento por riesgo de concentración geográfica catastrófica — aquí, +250 puntos básicos sobre un rango defendible de 150-400pb."),
        ("Escudo de silicio (silicon shield)", "teoría de que la dependencia mundial de los chips de TSMC disuadiría a China de atacar Taiwán — citada aquí como marco de referencia del pre-mortem (§12), no como garantía."),
        ("Tier «Alta Convicción»", "banda de calidad 75-84/100; MoS exigido 25% (35% si se activa el candado de expectativas), techo 30x, posición satélite únicamente."),
        ("VEU", "Validated End-User: autorización de EEUU que permite importar herramientas de fabricación sin licencia individual — la de la fábrica de TSMC en Nanjing expiró en dic-2025."),
        ("Candado duro anti-sobrepago", "techo de múltiplo sin excepción de tier ni de patrón; aquí violado por un margen de 1,7x-2,5x incluso con el año más favorable."),
        ("Zona BURBUJA", "precio &gt;135% del PWFV — la zona menos favorable de las cinco definidas por val-mos."),
    ]
    filas = [["Término", "Definición"]]
    for t, d in gl:
        filas.append([f"<b>{t}</b>", d])
    o += [M.tabla(filas, [4.2*cm, 12.2*cm], font_sz=7.8)]
    o += [sp(4), M.p("<b>Advertencias finales.</b>", "h3")]
    o += [M.p("Cada dato se etiquetó <b>HECHO</b> (fuente primaria: Form 20-F FY2025, earnings release y "
        "presentación de inversionistas Q1 2026), <b>INFERENCIA</b> o <b>SUPUESTO</b>. Cabos NO resueltos, "
        "declarados: la identidad exacta de los clientes 1 y 2 (el 20-F nunca nombra clientes por "
        "confidencialidad; el mercado los asume Apple y Nvidia respectivamente, pero esto es INFERENCIA "
        "externa, no una divulgación de la empresa); la capacidad exacta de CoWoS y su tasa de utilización "
        "(no divulgada numéricamente en el 20-F, solo estimados de terceros); si el sistema val-mos debería "
        "tener una regla única y congelada para el tratamiento de riesgo-país/geopolítico en WACC (hoy cada "
        "tesis construye su propio ajuste — un vacío del skill identificado en la verificación de esta "
        "tesis y de la de MELI, no un error de esta tesis en particular); si el sistema qg-seilern debería "
        "tener un gate G8 dedicado a concentración geográfica catastrófica de punto único de falla, en vez "
        "de canalizar el riesgo enteramente vía R6. El score Seilern mide <b>calidad, no valoración</b>. "
        "Documento de <b>uso personal</b>; no constituye asesoría de inversión registrada.")]
    o += [M.callout("PAUSA REFLEXIVA",
        "Qué queda por saber — la pieza que más cambiaría el veredicto: <b>una estimación de probabilidad "
        "de conflicto en el Estrecho de Taiwán con el rigor de un mercado de predicción líquido y "
        "verificable</b>, no la dispersión actual entre fuentes (4,9% a 22% según metodología) que este "
        "análisis tuvo que promediar de forma necesariamente imprecisa. Si esa cifra existiera y confirmara "
        "el extremo bajo del rango, la prima geopolítica de 250pb sería excesivamente conservadora y el "
        "PWFV subiría materialmente. Si confirmara el extremo alto, incluso 250pb resultaría insuficiente. "
        "La segunda pieza, de similar importancia: si Samsung o Intel logran una segunda venta confirmada a "
        "un cliente top-10 en los próximos 4-6 trimestres — el dato que determinaría si el caso Tesla AI6 "
        "fue una excepción o el inicio de un patrón.")]
    return o

# ══════════════════════════════════════════════════════════════════════════
def story():
    s = []
    for fn in [portada, changelog, resumen, cuadro_mando, veredicto_cuant,
               s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, cierre]:
        s += fn()
    return s
