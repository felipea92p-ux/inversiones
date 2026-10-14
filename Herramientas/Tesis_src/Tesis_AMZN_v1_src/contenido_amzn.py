# -*- coding: utf-8 -*-
"""CONTENIDO · Tesis Ultra AMZN v3.0 (refresco editorial, 9-jul-2026). Solo prosa/datos.
Importa motor_qg (diseño) y dcf_amzn (números). v3.0 reescribe en profundidad la voz
narrativa (metáforas de ajedrez/historia/naturaleza, curiosidades verificadas de la
historia y cultura de Amazon, jerga técnica explicada en cada sección) — CERO cambios
en números, tiers o veredicto respecto a v2.0. Eje CALIDAD intacto (80,2, Alta
convicción); eje VALORACIÓN intacto (WACC 10,4%, PWFV $108, MoS −56%, detector GRIS,
veredicto ESPERAR)."""
from reportlab.platypus import Spacer, PageBreak, NextPageTemplate, Paragraph
from reportlab.lib.units import cm
from reportlab.lib.styles import ParagraphStyle
import motor_qg as M
from motor_qg import C
import dcf_amzn as D

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
        Paragraph("AMAZON.COM, INC.", nombre),
        Paragraph("NASDAQ: AMZN &nbsp;·&nbsp; Plataforma / marketplace &nbsp;·&nbsp; el flywheel original", tick),
        sp(14),
        Paragraph("El volante de Bezos gira más rápido que nunca: unidades +15%, AWS acelerando a +28%, "
                  "publicidad a 72.000 millones. Pero el flujo de caja libre es NEGATIVO, la deuda se "
                  "duplicó en un trimestre para pagar un capex de 200.000 millones, y la mitad del "
                  "beneficio del trimestre es una revalorización contable de Anthropic. A un 12% de su "
                  "máximo histórico, el mercado no descuenta ninguna de esas tensiones. Gran negocio; "
                  "el precio es el problema.", tag),
        sp(20),
        M.kpi_panel([
            (f"{D.es(D.SCORE_QG,1)}/100", "CALIDAD QG", f"tier {D.TIER_QG} (75–84)"),
            (f"US${D.PWFV}", "VALOR (PWFV)", f"vs US${D.es(D.PRECIO,0)} hoy · zona {D.ZONA_HOY}"),
            (f"+{D.es(D.PRIMA,0)}%", "PRIMA sobre VALOR", f"MoS {D.es(D.MOS_HOY,0)}% → {D.VEREDICTO}"),
        ]),
        sp(16), M.hr(),
        Paragraph(f"<b>9 de julio de 2026</b> &nbsp;·&nbsp; Precio US${D.es(D.PRECIO,2)} &nbsp;·&nbsp; "
                  f"Máximo 52s US${D.es(D.ATH,2)} (−12%) &nbsp;·&nbsp; Horizonte 5–10 años &nbsp;·&nbsp; "
                  f"Documento de convicción N&ordm; 16", meta),
        M.hr(),
        Paragraph("Eje CALIDAD (sistema qg-seilern de 11 reglas) y eje PRECIO (val-mos: PWFV-Valor, "
                  "detector de trampas, MoS por tier) calculados por separado y cruzados solo al final. "
                  "Uso personal; no es asesoría de inversión registrada.", fn),
        NextPageTemplate("Normal"), PageBreak()]
    return out

# ══════════════════════════════════════════════════════════════════════════
def changelog():
    o = M.flag_titulo("Changelog de versiones", "Qué se fija en la v2.0 — y contra qué sesgo se blinda")
    o += [M.p("Esta es la <b>versión 2.0</b> de la tesis Ultra de Amazon bajo el estándar de dos ejes. "
        "Se documentan los supuestos críticos para auditarlos en el futuro. Esta tesis tiene, "
        "además, un blindaje específico: <b>el autor llega con sesgo alcista declarado en Amazon</b> "
        "(figura en el plan de cartera de junio de 2026 como convicción). El estándar existe exactamente "
        "para esto: que el sistema, no el entusiasmo, fije el gatillo. El resultado — ESPERAR, sin "
        "compra a US$244 — contradice el sesgo del autor y el consenso de Wall Street (Strong Buy, "
        "objetivo ~US$313). Esa incomodidad es una señal de que el proceso funcionó, no de que falló.")]
    o += [M.tabla([
        ["Supuesto crítico fijado en v2.0", "Valor", "Qué lo movería"],
        ["Owner earnings normalizado (CFO − mant. ≈ D&A − SBC)", "~US$58B (rango 55–75)", "Probar que el mantenimiento real es &lt; D&A, o que el capex ya rinde a márgenes AWS"],
        ["Ganancia Anthropic excluida al 100% del beneficio", "US$16,8B pre-tax Q1", "Nada: es no-caja, reversible y circular"],
        ["WACC declarado", "10,4% = CAPM propio (beta 1,47, ERP Damodaran 4,23%) ponderado con deuda", "Que el spread de crédito hyperscaler se comprima de vuelta tras el bono de 8-jul-2026"],
        ["PWFV-Valor (ancla)", f"US${D.PWFV} (banda defendible $92-121)", "Que el FCF se recupere a $80-100B+ manteniendo el crecimiento"],
        ["MoS exigido", "35% (25% tier + 10pp candado HEROICO)", "Que el DCF inverso deje de exigir ~20% de crecimiento"],
    ], [6.6*cm, 4.2*cm, 5.6*cm], font_sz=7.8)]
    o += [M.p("<b>El punto de honestidad (v1.0):</b> el score de calidad original salió 85,6 con dos reglas "
        "puntuadas fuera del rango permitido (R3=11,5 y R4=13 sobre un máximo de 10). El verificador "
        "adversarial lo cazó y recalculó a <b>80,2 — tier Alta convicción, no Núcleo</b> — lo que "
        "<i>sube</i> el margen de seguridad exigido del 15% al 25% (y al 35% con el candado de "
        "expectativas heroicas). Ese score de calidad NO se toca en esta v2.0.")]
    o += [M.callout("LECCIÓN TRANSFERIBLE",
        "<b>Cambio v1.0→v2.0: el WACC estaba regalado, no el veredicto.</b> La v1.0 usaba un WACC de "
        "9,0% construido como «8,5% escalón tier Alta + 0,5pp recargo» — un "
        "atajo de val-mos que nunca se contrastó contra el CAPM propio de Amazon. Una verificación "
        "adversarial dedicada reconstruyó el CAPM con datos de hoy (beta 1,47 de GuruFocus, Rf 4,55% del "
        "10Y UST, y el ERP implícito REAL de Damodaran de 4,23% — no el rango genérico 4,5-5,0% que usaba "
        "v1.0) y encontró que el WACC bottom-up honesto cae en 10,0-10,5%, con 10,4% como punto sostenido "
        "por una emisión sorpresa de bonos AMZN de US$25.000M el 8-jul-2026 (spreads hyperscaler "
        "ensanchándose — primera señal de mercado de crédito de que el súper-capex empieza a cobrar "
        "precio). El segundo hallazgo, más importante: el <b>ROIC incremental de AWS medido en el 10-K</b> "
        "(variación de operating income sobre variación de activos, FY25 vs FY24) da <b>~8,0%</b> — por "
        "debajo del WACC, y casi exacto al supuesto del escenario BAJISTA (8%), no al BASE (16%). Jassy "
        "confirmó en la call de Q1'26 el mecanismo de lag capex→facturación («6 a 24 meses»), lo que "
        "sesga ese 8,0% a la baja — pero la trayectoria real de márgenes AWS (39,5%→32,9%→35,4% FY→37,7% "
        "Q1'26) muestra una recuperación PARCIAL, no completa, un año después de iniciado el ciclo. Con "
        "esa evidencia se repesan los tres escenarios hacia el bajista (25/45/30% → 35/40/25%) y se "
        "escalan los tres valores por el WACC más bajo — los dos efectos casi se cancelan: el PWFV pasa "
        "de US$161 (WACC regalado) a <b>US$108</b> (WACC honesto + pesos corregidos), con banda defendible "
        "US$92-121. El detector pasa de PASA a <b>GRIS</b>: se suma la concentración de OpenAI (hasta "
        "US$138.000M en compromisos) a la ya conocida circularidad de Anthropic. El veredicto <b>ESPERAR "
        "sobrevive</b> — y no al filo: resiste incluso en el extremo más favorable a AMZN (US$121 PWFV, "
        "MoS −50%) que la verificación pudo construir razonablemente. Cambia el camino, no el destino.")]
    o += [M.p("<b>Qué cambia en la v3.0 (9-jul-2026, refresco editorial).</b> Se reescribió en "
        "profundidad la voz narrativa de las secciones de historia, modelo de negocio, moat, "
        "competencia, gestión, riesgos, pre-mortem y cierre — metáforas de ajedrez/historia/naturaleza, "
        "ocho curiosidades verificadas sobre la fundación y la cultura de Amazon (el garaje de 1994, el "
        "nombre «Cadabra», el origen del API Mandate detrás de AWS, la idea de Prime propuesta por un "
        "empleado, la regla de las dos pizzas, el método Working Backwards, la silla vacía del cliente, "
        "la filosofía Día 1/Día 2) y jerga técnica explicada en cada sección donde aparece por primera "
        "vez. <b>Cero cambios en números, tiers o veredicto de inversión</b>: el eje calidad sigue en "
        "80,2/Alta convicción y el eje valoración sigue en PWFV US$108/ESPERAR, tal como los fijó la "
        "verificación adversarial del 9-jul-2026 documentada arriba. Se re-ejecutó dcf_amzn.py como "
        "parte de este refresco y los cuatro auto-chequeos del módulo (REGLAS→RAW_QG, PWFV ponderado, "
        "ASIMETRIA, MOS_HOY) siguen pasando sin discrepancias — no se encontró ningún error aritmético "
        "nuevo que corregir.")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def resumen():
    o = M.flag_titulo("Resumen en treinta segundos", "La pregunta operativa, tres números y un veredicto")
    o += [M.p("<b>¿Puede el mejor flywheel del capitalismo justificar un precio que ya asume una década "
        "casi perfecta — mientras el flujo de caja libre es negativo, la deuda se duplica en un "
        "trimestre y la mitad del beneficio es una revalorización contable?</b> Esa es la pregunta. No "
        "es si Amazon es un gran negocio (lo es, y el volante gira más rápido que nunca); es si a "
        "US$244,59 — apenas un 12% bajo su máximo — queda algo de margen para el que compra hoy. [HECHO]")]
    o += [M.tabla([
        ["El número", "Qué dice"],
        ["FCF TTM −US$2,5B", "El flujo de caja libre COLAPSÓ: $38B (2024) → $11B (2025) → negativo. El capex de ~$200B se financia con deuda nueva (+$53B en un trimestre). [HECHO]"],
        ["g implícita ~20%", "El precio exige que los owner earnings crezcan ~20% anual una década — casi el doble del CAGR histórico de ingresos (11%). Expectativas HEROICAS → candado activo. [DCF inverso]"],
        [f"Prima +{D.es(D.PRIMA,0)}% sobre el valor", f"PWFV honesto ~US${D.PWFV} vs precio US$245: zona BURBUJA. Ni el escenario alcista (US${D.V_BULL}) alcanza el precio de hoy. Asimetría negativa. [val-mos]"],
    ], [3.7*cm, 12.7*cm])]
    o += [sp(6), M.p(f"<b>Veredicto operativo.</b> Calidad QG <b>{D.es(D.SCORE_QG,1)}/100</b> (tier "
        f"<b>{D.TIER_QG}</b>; el 85,6 original tenía un error aritmético que el verificador corrigió). "
        f"El detector de trampas da <b>{D.DETECTOR}</b> — Amazon no es una trampa de valor clásica: es el "
        f"problema inverso, un negocio excelente cotizando caro, con dos alertas de calidad-de-ingresos "
        f"(circularidad Anthropic+OpenAI) que impiden un PASA limpio. El foso está intacto o "
        f"ensanchándose en las cuatro líneas (marketplace, AWS, publicidad, logística). Pero el PWFV-Valor "
        f"es <b>US${D.PWFV}</b> y el precio US${D.es(D.PRECIO,0)}: <b>prima del +{D.es(D.PRIMA,0)}%, zona "
        f"{D.ZONA_HOY}, margen de seguridad {D.es(D.MOS_HOY,0)}%</b> cuando el tier exige +{D.es(D.MOS_EXIG,0)}% "
        f"(candado heroico). <b>Acción: {D.VEREDICTO} — 0% ahora; watchlist con gatillo en "
        f"US${D.GATILLO_T1}</b> (zona GANGA; tramo pleno ~US${D.GATILLO_PLENO}). Para el tenedor existente "
        f"aplica la regla dual: NO se vende un compounder de moat intacto por múltiplo caro — pero tampoco "
        f"se inicia ni amplía sin margen. La asimetría es negativa ({D.es(D.ASIMETRIA,2)}): el escenario "
        f"alcista compensa apenas una fracción de lo que arriesga el bajista.")]
    o += [M.callout("PAUSA REFLEXIVA",
        f"Tercera tesis, tercer final. Duolingo: calidad alta, castigo del −77%, descuento del 21% — corto "
        f"por 4 puntos → VIGILAR. Microsoft: calidad Núcleo, castigo del −20%, descuento del 26% — "
        f"suficiente → COMPRAR. Amazon: calidad alta, castigo de apenas −12%, PRIMA del +{D.es(D.PRIMA,0)}% "
        f"→ ESPERAR. Las tres comparten la misma tensión (un gasto colosal que deprime la caja) pero el "
        f"mercado las trató distinto: castigó de más a Duolingo, castigó lo justo a Microsoft, y a Amazon "
        f"no la castigó en absoluto. La pregunta que debes hacerte antes de seguir: ¿tu convicción alcista "
        f"en Amazon es sobre el negocio (correcta) o sobre la acción a este precio (que ya paga el éxito "
        f"completo)? El sistema separa esas dos cosas; el mercado, hoy, no.")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def cuadro_mando():
    o = M.flag_titulo("Cuadro de mando trimestral", "Lo único que se refresca cada trimestre · corte 9-jul-2026 (verificación val-mos)")
    o += [M.p("<b>Bloque 1 · Estado de la posición.</b>", "h3")]
    o += [M.tabla([
        ["Concepto", "Estado"],
        ["Precio / zona", f"US${D.es(D.PRECIO,2)} · zona {D.ZONA_HOY} (prima +{D.es(D.PRIMA,0)}% vs PWFV; MoS {D.es(D.MOS_HOY,0)}%)"],
        ["Valor justo (PWFV-Valor)", f"US${D.PWFV} · ponderado por escenarios US${D.V_POND} · EPV suelo US${D.EPV}"],
        ["Probabilidades de escenario", f"Bajista {D.P_BEAR}% (US${D.V_BEAR}) · Base {D.P_BASE}% (US${D.V_BASE}) · Alcista {D.P_BULL}% (US${D.V_BULL})"],
        ["Veredicto operativo", f"{D.VEREDICTO} · 0% del NAV · watchlist con gatillo US${D.GATILLO_T1} (GANGA) / US${D.GATILLO_PLENO} (pleno)"],
        ["Si ya se posee", "SOSTENER (moat intacto; no se vende compounder por múltiplo) — pero NO ampliar"],
    ], [4.3*cm, 12.1*cm])]
    o += [sp(4), M.p("<b>Bloque 2 · Tracker de KPIs en semáforo</b> (arquetipo plataforma, VI.7).", "h3")]
    o += [M.tabla([
        ["Indicador", "Hoy", "Umbral rojo", "●"],
        ["Unit growth WW (flywheel)", "+15% (máx post-covid)", "&lt; +8% sostenido", "verde"],
        ["AWS (crecimiento)", "+28% (acelerando)", "&lt; +20% con capex alto", "verde"],
        ["Margen retail NA", "7,9% (+160 pb)", "cae 2 trim. seguidos", "verde"],
        ["FCF (definición Amazon)", "−US$2,5B TTM", "sigue negativo en 2027", "rojo"],
        ["Deuda LP (financia capex)", "+US$53B en un trimestre", "otra duplicación sin plateau", "ambar"],
        ["Carrying value Anthropic", "US$32B (de $14,8B)", "down-round → reversión al P&amp;L", "ambar"],
        ["Capex-efficiency (&Delta;AWS/capex, proxy)", "0,16x (FY25) → 0,19x (Q1'26)", "sin umbral — indicador nuevo, leer con desfase 6-24 meses", "nuevo"],
    ], [6.0*cm, 4.4*cm, 4.2*cm, 1.8*cm])]
    o += [sp(3), M.p("<i>Proxy nuevo (todavía sin umbral duro): &Delta;AWS revenue / capex del año. "
        "US$21,1B de crecimiento de AWS (2024→2025) sobre US$131,8B de capex TTM ≈ 0,16x; con el dato "
        "más fresco, &Delta;AWS Q1'26 vs Q1'25 (US$8,3B) sobre capex Q1'26 (US$43,2B) ≈ 0,19x. Jassy "
        "reconoce en la call de Q1'26 un desfase de «six to 24 months» entre el desembolso y la primera "
        "facturación, sobre activos con vidas de «30-plus years for data centers, five to six years for "
        "chips» — así que este ratio del mismo año SUBESTIMA el retorno final; se lee como indicador "
        "adelantado conservador, no como ROIC terminal. Contexto: el margen de AWS se sostiene en 37,7% "
        "(Q1'26) en parte por acortar contablemente la vida útil de servidores/redes (6→5 años, ene-2025: "
        "−US$700M en operating income 2025, más −US$920M de cargo por retiro anticipado de equipo) — "
        "resiste comprimiendo la contabilidad, no porque el capex nuevo ya esté rindiendo. [HECHO las "
        "cifras y las citas; SUPUESTO la lectura del ratio]</i>", "nota")]
    o += [sp(4), M.p("<b>Bloque 3 · Feedback loop de calibración.</b>", "h3")]
    o += [M.tabla([
        ["Predicción (trim. anterior)", "Resultado real", "Interpretación"],
        ["v1.0 — sin predicción formal previa", "Q1'26: rev US$181,5B (+17%), OI 13,1% récord, AWS +28%", "Punto de partida; calibrar desde el próximo trimestre"],
        ["Zona predicha vs precio real", f"BURBUJA a US${D.es(D.PRECIO,0)}", "El sistema discrepa del consenso (Strong Buy, PT $313): registrar quién acierta"],
        ["Guía de capex 2026 (Jassy, call Q1'26)", "«Our plan is largely the same» — $200.000M confirmado sin revisión; cash capex trim. $43.200M", "Sin cifra de margen/ROIC objetivo: confianza cualitativa, no compromiso auditable"],
    ], [5.6*cm, 5.4*cm, 5.4*cm])]
    o += [sp(3), M.p("<i>Cita completa (10-Q/call Q1'26, 29-abr-2026): sobre el payback, Jassy dijo que "
        "el capex se desembolsa «typically six to 24 months before we start billing customers», sobre "
        "activos con vidas útiles de «30-plus years for data centers, five to six years for chips, "
        "servers, and networking gear», y que tiene «high confidence this will be monetized well» "
        "porque ya existen «customer commitments for a substantial portion» del capex 2026 de AWS — lo "
        "cual conecta con el backlog de US$364.000M (+93% i.a., vida media 5,5 años, excluye Anthropic). "
        "Ni Jassy ni Olsavsky dieron una cifra de margen objetivo, ROIC esperado o umbral de payback "
        "cuantificado: la ausencia misma es el dato que este tracker debe seguir cada trimestre. [HECHO "
        "las citas; INFERENCIA la lectura de la ausencia]</i>", "nota")]
    o += [sp(4), M.p("<b>Bloque 4 · Operativo.</b> Sin trigger de drawdown (la acción está a −12% del "
        "máximo; el re-análisis lo motivó el pedido explícito del dueño de la cartera, con la ventaja de "
        "fijar el ancla ANTES de una eventual corrección). Fecha del refresh: <b>9-jul-2026</b>; documento "
        "v2.0 (corrección val-mos sobre WACC/PWFV/detector, eje calidad sin cambios). Próxima revisión: "
        "resultados <b>Q2 2026</b> (finales de julio), con foco en el ritmo de capex, la deuda nueva y "
        "cualquier down-round o revalorización de Anthropic. Alertas de watchlist val-mos: <b>−25% desde "
        "máximo (~US$209) → revisar; −35% (~US$181) → candidata a tramo si el detector no empeora a "
        "alerta dura (rojo).</b>")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def veredicto_cuant():
    o = M.flag_titulo("El veredicto cuantificado", "Once reglas con bisturí — y un error aritmético corregido en público")
    o += [M.p(f"<i>{DISCLAIMER}</i>", "nota")]
    o += [ch("01_radar", 15.0), sp(4)]
    vd = {
        "R1 · Escalabilidad": "El flywheel expande márgenes (5,3%→11,5%), pero NO es asset-light: el modelo por capacidad más intensivo en capex de las megacaps (18% de ventas → ~$200B).",
        "R2 · Industria": "Cloud ~14,5%, publicidad ~14%, IA ~35% CAGR; e-commerce con penetración ~9% del retail: décadas de pista.",
        "R3 · Liderazgo": "#1 cloud, #1 e-commerce US, #1 paquetería US (superó a USPS/UPS/FedEx), #3 publicidad y el que más rápido gana. Multi-liderazgo pleno.",
        "R4 · Moat": "Multi-moat de máxima jerarquía: red de doble lado + switching costs AWS + densidad logística + datos de intención + silicio propio. Nota máxima.",
        "R5 · Crec. orgánico": "Ingresos +12-17% acelerando (unidades +15%); pero el beneficio de calidad está contaminado: el EPS normalizado ex-Anthropic está PLANO ($1,59→$1,60).",
        "R6 · Diversificación": "Millones de clientes, ningún cliente &gt;10%; retail aún US-pesado (NA ~59% de ventas).",
        "R7 · Capital / ROIC": "ROIC ~14-18%: por encima del WACC pero bajo el listón Seilern (~20%). Capex 18% de ventas, FCF negativo. La cuña de la tesis.",
        "R8 · Balance": "Aún ~+$21B netos, deuda IG no tóxica; pero la deuda LP casi se duplicó en UN trimestre y con leases ya sería deuda neta ~−$70B.",
        "R9 · Transparencia": "Señal GAAP-gap ROJA: el neto está inflado por Anthropic (no-caja, reversible, CIRCULAR). Techo 6/10. Usar owner earnings, nunca el P/E GAAP.",
        "R10 · Gestión": "Jassy operador de élite + Bezos 8,8% skin real + la retribución más limpia de las megacaps; restan: chair no independiente y conflicto Prometheus.",
        "R11 · Impacto": "Infraestructura de internet (AWS) + acceso/precios para 1.800M de consumidores; no llega al tier salud/inclusión.",
    }
    filas = [["Regla", "Puntos", "Veredicto en una línea"]]
    for n, pts, mx in D.REGLAS:
        p_txt = f"{D.es(pts,2).rstrip('0').rstrip(',') if pts % 1 else int(pts)}/{mx}"
        filas.append([n, p_txt, vd[n]])
    filas.append(["<b>TOTAL</b>", f"<b>{D.es(D.RAW_QG,2)}/125</b>",
                  f"<b>{D.es(D.SCORE_QG,1)}/100 · tier {D.TIER_QG} (75–84)</b>"])
    o += [M.tabla(filas, [3.4*cm, 2.2*cm, 10.8*cm])]
    o += [M.p("<i>Nota metodológica: la corrida original arrojó 85,6 con R3=11,5 y R4=13 — puntuaciones "
        "imposibles en una escala 0–10. El verificador adversarial las capó al máximo legal (10) y "
        "recalculó: 80,2, tier Alta convicción. La corrección importa doblemente: baja el tier Y sube el "
        "margen de seguridad exigido del 15% al 25%. Los umbrales del sistema son sin excepción: 84,9 no "
        "es Núcleo.</i>", "nota")]
    o += [M.callout("LECCIÓN TRANSFERIBLE",
        "Un sistema de scoring vale lo que valga su verificación. El agente que puntuó quiso premiar un "
        "liderazgo y un moat genuinamente excepcionales «rompiendo la escala» — el equivalente analítico "
        "de enamorarse. La escala existe porque la alternativa es la inflación de notas: si Amazon merece "
        "un 13 sobre 10, ¿qué merece Visa? El cap a 10 no niega la excelencia; niega la excepción. Y la "
        "consecuencia práctica es enorme: Alta convicción exige 25% de margen, Núcleo solo 15%. Puntuar "
        "con disciplina es, literalmente, la diferencia entre comprar y esperar.")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def s1():
    o = M.flag_titulo("§1 · La historia detrás del veredicto",
                       "El garaje que se convirtió en la máquina comercial más grande del mundo")
    o += [M.p("En 1994, a los treinta años, Jeff Bezos dejó un puesto lucrativo como vicepresidente en "
        "el fondo de cobertura (hedge fund, un vehículo de inversión con estrategias más agresivas que "
        "un fondo tradicional) D. E. Shaw aplicando lo que él mismo bautizó el «marco de minimización "
        "del arrepentimiento» (regret-minimization framework): se proyectó a los ochenta años y se "
        "preguntó de qué se arrepentiría más — de dejar Wall Street o de perderse el amanecer de "
        "internet. Escribió el plan de negocio en un viaje en auto de Nueva York a Seattle y montó la "
        "primera oficina en un garaje alquilado de unos 90 metros cuadrados en Bellevue, con escritorios "
        "hechos de puertas de madera sobre maderos de 4x4 — una economía de guerra que se volvió "
        "tradición interna. Su entonces esposa, MacKenzie Scott, llevaba la contabilidad y parte de las "
        "negociaciones de flete. La empresa iba a llamarse «Cadabra», por abracadabra, hasta que Bezos "
        "la rebautizó Amazon —por el río más caudaloso del planeta, y porque empieza con «A»—: quería un "
        "nombre que apareciera primero en cualquier listado y sonara tan inmenso como lo que soñaba "
        "construir. [HECHO]")]
    o += [M.p("Ese primer negocio —libros por correo— fue apenas la célula original de un organismo que "
        "después se ramificó como una radiación adaptativa (adaptive radiation: el fenómeno biológico "
        "por el que una especie ancestral, al colonizar nichos distintos, da lugar a variantes "
        "especializadas — los pinzones de Darwin en las Galápagos son el ejemplo de manual). El círculo "
        "que Bezos dibujó en una servilleta —precios bajos atraen clientes, más clientes atraen "
        "vendedores, más vendedores amplían la selección, la escala baja los costes, y los costes bajos "
        "permiten... precios más bajos— es el sistema circulatorio de ese organismo: el <i>flywheel</i> "
        "(volante de inercia, la metáfora de un mecanismo que, una vez en marcha, se retroalimenta y "
        "cuesta cada vez menos empujar). Treinta y dos años después, ese volante sigue girando y ha "
        "producido tres especies hijas que hoy valen más que el tronco original: AWS (la infraestructura "
        "de internet, nacida —como se detalla en el §5— de un efecto colateral no planeado), un imperio "
        "publicitario de US$72.000 millones, y la mayor red de paquetería de Estados Unidos, que ya "
        "superó a USPS, UPS y FedEx. Ingresos: US$743.000 millones; 60% de las unidades, vendidas por "
        "terceros. [HECHO]")]
    o += [M.p("La historia que importa para esta tesis es la de las <b>tres monetizaciones</b>. El "
        "retail casi no gana dinero por diseño (margen NA 7,9%, Internacional 3,6%): es el generador de "
        "tráfico, la sangre que circula. El dinero se gana en las capas montadas encima: <b>AWS</b> (18% "
        "de las ventas, 59% del beneficio operativo, margen 37,7%), la <b>publicidad</b> (crece +22-24% "
        "con márgenes estimados del 60-75%: es la explicación matemática de la expansión del margen "
        "retail), y la <b>suscripción Prime</b> (el pegamento de retención). Amazon es un iceberg: lo "
        "visible (la tienda) apenas gana; lo sumergido (nube, anuncios, logística) es de las máquinas de "
        "beneficio más finas del mundo. [HECHO/INFERENCIA]")]
    o += [ch("19_flywheel", 15.4), sp(2)]
    o += [M.p("Y en 2026 el volante gira más rápido que nunca — unidades +15%, el máximo desde la "
        "pandemia; AWS re-acelerando a +28%, su mejor trimestre en casi cuatro años —. Pero la empresa "
        "libró, en paralelo, la mayor campaña de capital de su historia corporativa: ~US$200.000 "
        "millones de capex en 2026, casi todo para centros de datos de inteligencia artificial. Es el "
        "patrón que cualquier lector de historia militar reconoce enseguida: la ofensiva que avanza tan "
        "rápido que las líneas de suministro dejan de alcanzarla. Consumió todo el flujo de caja libre y "
        "obligó, por primera vez en la historia moderna de la compañía, a financiar el avance con deuda "
        "masiva. El ADN de Amazon siempre fue reinvertir cada dólar ganado; la novedad de 2026 es que "
        "reinvierte <i>más de lo que gana</i>.")]
    o += [M.p("Amazon incluso institucionalizó el recordatorio de por qué apuesta así: durante años "
        "ocupó, en su campus de Seattle, un edificio bautizado literalmente «Day 1». En la carta a "
        "accionistas de 2016, Bezos lo explicó sin metáfora: «El día 2 es estancamiento. Le sigue la "
        "irrelevancia. Le sigue un declive doloroso y agudo. Le sigue la muerte. Y por eso siempre es el "
        "Día 1». El capex de 2026 es, en ese lenguaje, la apuesta de que gastar como si fuera el primer "
        "día —aunque signifique endeudarse— es menos peligroso que defender el balance y arriesgarse a "
        "la irrelevancia. El mercado, hoy, le compra esa apuesta sin descuento alguno; esta tesis "
        "pregunta si el precio ya la da por ganada de antemano. [HECHO la cita y el edificio; "
        "INFERENCIA la lectura]")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def s2():
    o = M.flag_titulo("§2 · Historia de mi posición", "El sesgo declarado — y el sistema que existe para frenarlo")
    o += [M.p("Amazon figura en mi plan de cartera desde junio de 2026 con <b>sesgo alcista "
        "declarado</b>: es una de las plataformas que quiero tener a largo plazo, por el flywheel, por "
        "AWS y por la publicidad. Esta tesis se construyó, en parte, esperando confirmar ese sesgo. "
        "[contexto propio]")]
    o += [M.p(f"<b>No lo confirmó — y ese es exactamente el valor del sistema.</b> Bezos usó su «marco "
        f"de minimización del arrepentimiento» para saltar al vacío en 1994; yo necesito la versión "
        f"inversa de esa misma disciplina — minimizar el arrepentimiento de pagar de más, no el de "
        f"quedarme afuera. El eje calidad salió donde esperaba (80,2, Alta convicción: negocio soberbio "
        f"con lastres reales de intensidad de capital y calidad de earnings). Pero el eje precio "
        f"dictaminó lo que mi entusiasmo no quería ver: a US$244, con la acción a solo −12% de su "
        f"máximo, <b>el mercado ya paga el éxito completo del capex de IA antes de que exista</b>. El "
        f"PWFV honesto (~US${D.PWFV}) queda {D.es(abs(D.MOS_HOY),0)}% por debajo del precio; ni siquiera "
        f"el escenario alcista (US${D.V_BULL}) lo alcanza. Una verificación adversarial dedicada, con "
        f"mandato de refutar la valoración, no pudo: encontró que el WACC de v1.0 estaba inflado por un "
        f"atajo de tier no contrastado contra el CAPM propio, lo corrigió a la baja (9,0%→10,4%) — pero "
        f"también encontró que el ROIC incremental medido de AWS (~8%) está por debajo de ese WACC, y "
        f"repesó los escenarios hacia el bajista. Los dos efectos casi se cancelan: el veredicto "
        f"sobrevive.")]
    o += [M.p(f"<b>Mi posición operativa, por tanto:</b> 0% ahora. Amazon entra a la <b>watchlist de "
        f"precio</b> (lista de vigilancia: el gatillo de compra queda anotado por escrito hoy, antes de "
        f"que el mercado se mueva, para que no lo decida la emoción del momento) de val-mos, con alertas "
        f"automáticas: revisar a −25% del máximo (~US$209), candidata a tramo a −35% (~US$181), y "
        f"<b>gatillo de compra en US${D.GATILLO_T1}</b> (zona GANGA), con "
        f"posición plena solo hacia US${D.GATILLO_PLENO} (el 35% de margen que exige el candado de "
        f"expectativas heroicas). Si la corrección nunca llega, no pasa nada: el coste de oportunidad de "
        f"esperar es infinitamente menor que el de comprar sin margen. Reglas anti-sesgo que me aplico "
        f"por escrito: no promediar a la baja sin re-correr el detector, y no convertir «me encanta el "
        f"negocio» en «cualquier precio vale».")]
    o += [M.callout("PAUSA REFLEXIVA",
        f"El error más caro del inversor de calidad no es comprar malas empresas: es pagar de más por las "
        f"buenas. Cisco en 2000 era un gran negocio; quien la compró en el pico tardó dos décadas en "
        f"recuperar su dinero mientras la empresa seguía creciendo. La pregunta que esta posición me "
        f"obliga a responder: si Amazon vale ~${D.PWFV} y cotiza a $245, ¿qué sé yo que el modelo no "
        f"sepa? Si la respuesta es «nada, pero el consenso dice $313», eso no es una tesis: es un "
        f"argumento de autoridad contra mi propio sistema.")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def s3():
    o = M.flag_titulo("§3 · El modelo de negocio en dos minutos", "La prueba de Lynch: una tienda que cobra peaje")
    o += [M.p("<b>La prueba de los dos minutos</b> (el test de Peter Lynch: si no podés explicar un "
        "negocio en lo que tarda un semáforo en cambiar, no lo entendés lo suficiente para invertir en "
        "él). Amazon vende de todo y lo entrega más rápido que nadie (la tienda); alquila su "
        "infraestructura informática al mundo (AWS); cobra a las marcas por aparecer primero "
        "(publicidad); y cobra una cuota por pertenecer al club (Prime). Reporta tres segmentos — North "
        "America (US$104B/trim), International (US$40B) y AWS (US$37,6B) — pero la lectura correcta es "
        "por capas: <b>el retail genera el tráfico; la publicidad, la suscripción y AWS generan el "
        "beneficio.</b> [HECHO]")]
    o += [ch("02_segmentos", 15.2), sp(2)]
    o += [M.p("<b>La mecánica del margen.</b> El margen operativo consolidado tocó un récord del 13,1% "
        "en Q1 2026 (desde 2,4% en 2022). Las palancas: (1) la <b>publicidad</b> — US$72.000 millones "
        "TTM creciendo +22%, con margen incremental casi puro, embebida dentro de los segmentos retail —; "
        "(2) la <b>productividad logística</b> — la regionalización de la red desde 2023 sigue bajando "
        "el coste por paquete —; y (3) <b>AWS</b> con margen del 37,7%. El retail de Amazon ya no es un "
        "negocio de vender cosas: es un negocio de <i>cobrar peaje</i> sobre el tráfico que las cosas "
        "generan. [HECHO/INFERENCIA]")]
    o += [M.p("<b>El origen de Prime desmonta el mito del genio solitario.</b> La idea no nació en la "
        "cabeza de Bezos: en 2004, un empleado llamado Charlie Ward propuso cobrar una cuota anual por "
        "adelantado a cambio de envío gratis. La reacción interna inicial fue de escepticismo — «¿está "
        "loco Charlie?», se preguntaban varios ejecutivos —. Bezos adoptó la idea y la llevó más lejos de "
        "lo que nadie había pedido: exigió que el envío fuera en dos días, algo que casi ningún minorista "
        "del mundo podía prometer entonces, lo que forzó una expansión agresiva de la red logística años "
        "antes de que esa red se convirtiera en el foso más profundo de la compañía (§5). Prime se lanzó "
        "en febrero de 2005 a US$79 al año; hoy sostiene ~US$25.000 millones de ingresos diferidos "
        "prepagados, una base de renovación extraordinariamente pegajosa. La lección que sobrevive: el "
        "mejor proceso de decisión de Amazon no depende de que Bezos tenga siempre la idea — depende de "
        "que la empresa sepa reconocer una buena idea ajena y ejecutarla con una disciplina que la "
        "mayoría de sus rivales no puede igualar. [HECHO]")]
    o += [M.p("<b>Economía de cohortes</b> (cohort economics: seguir a un mismo grupo de clientes en el "
        "tiempo en vez de mirar solo el promedio del período; arquetipo plataforma). Amazon no divulga "
        "GMV (volumen bruto de mercancía transaccionado), suscriptores Prime ni churn (tasa de "
        "cancelación) — puntos ciegos declarados —. Los proxies: el <b>unit growth del +15%</b> (máximo "
        "post-covid) prueba que el volante gira por volumen, no por precio; el mix 3P estable en ~60% de "
        "unidades con el revenue de servicios 3P creciendo +12% implica un <i>take rate</i> (la porción "
        "que Amazon se queda del GMV del vendedor externo) que sube secularmente (~50-60% all-in del GMV "
        "del vendedor, vs ~40% hace cinco años — la palanca de margen menos visible); y la suscripción "
        "crece +12% constante. [HECHO los reportados; INFERENCIA/benchmark el take rate]")]
    o += [ch("04_aws", 15.0)]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def s4():
    o = M.flag_titulo("§4 · Las once reglas de Seilern con bisturí", "El output de qg-seilern, verificado y corregido")
    o += [M.p(f"<i>{DISCLAIMER}</i>", "nota")]
    o += [M.p(f"Amazon pasa los <b>siete knock-outs</b> — incluido G4 (su ROIC del ~14-18% supera el "
        f"coste de capital, con la narrativa de inversión verificable que exige la regla) y G6 (el SBC, "
        f"2,7% de ventas y bajando desde el pico del 4,2%, no dispara; la dilución neta es moderada). "
        f"Sobre las once reglas obtiene <b>{D.es(D.SCORE_QG,1)}/100 (raw {D.es(D.RAW_QG,2)}/125), tier "
        f"{D.TIER_QG}</b> — corregido por verificación adversarial desde un 85,6 aritméticamente "
        f"inválido. Tres reglas lo separan del Núcleo, y las tres son <b>lastres reales, no "
        f"cosméticos</b>:")]
    o += [M.p("<b>R7 · Capital / ROIC 6/10 — el modelo por capacidad más pesado de las megacaps.</b> "
        "ROIC ~14,4% crudo (~16-18% limpio): por encima del WACC, por debajo del listón Seilern (~20%). "
        "El capex es el 18% de las ventas camino del ~27% (US$200B), el FCF colapsó de US$38B a "
        "NEGATIVO, y el capital incremental desplegado hoy (datacenters pre-ingreso) es una apuesta, no "
        "un retorno probado. La evidencia dura a favor: el backlog de AWS de US$364B (+93%), sin contar "
        "los &gt;$100B de Anthropic. [HECHO/INFERENCIA]")]
    o += [M.p("<b>Actualización Q1'26 (29-abr-2026): la guía no cambió — y esa ausencia es el dato.</b> "
        "Jassy confirmó en la earnings call que la guía de ~US$200.000M para 2026 «sigue vigente sin "
        "revisión» («I do not have a new update on capital. Our plan is largely the same»), con Olsavsky "
        "precisando un cash capex trimestral de US$43.200M, «principalmente para AWS y IA generativa». "
        "Sobre el mecanismo de payback fue inusualmente explícito: el capex se desembolsa «typically six "
        "to 24 months before we start billing customers», sobre activos con vidas de «30-plus years for "
        "data centers, five to six years for chips, servers, and networking gear» — y dijo tener «high "
        "confidence this will be monetized well» porque ya existen «customer commitments for a "
        "substantial portion» del capex 2026 de AWS, lo que conecta con el backlog de US$364.000M. Pero "
        "ni Jassy ni Olsavsky dieron una cifra de margen objetivo, ROIC esperado o umbral de payback "
        "cuantificado: la apuesta se defiende con lenguaje de confianza cualitativo, no con un compromiso "
        "numérico auditable trimestre a trimestre. [HECHO las citas; INFERENCIA la lectura de la "
        "ausencia]")]
    o += [M.p("<b>R9 · Transparencia 6/10 — la señal GAAP-gap es roja.</b> El neto del Q1 (US$30,3B) "
        "incluye <b>US$16,8B pre-tax de revalorización de Anthropic</b> — más de la mitad del beneficio "
        "antes de impuestos del trimestre —: no-caja, no recurrente, reversible y <b>circular</b> "
        "(Amazon financia a Anthropic, que gasta en AWS/Trainium, lo que revaloriza la participación de "
        "Amazon «sin que Anthropic pague un dólar»). El EPS normalizado ex-Anthropic es ~US$1,60 — "
        "<b>plano</b> contra los US$1,59 de hace un año. Sobre el año completo el efecto es ~15-19% del "
        "neto TTM (55% en el trimestre puntual). A favor: accruals fuertemente negativos (el CFO excede "
        "con mucho al neto), sin restatements. [HECHO, 10-Q]")]
    o += [ch("06_anthropic", 14.8), sp(2)]
    o += [M.p("<b>R8 · Balance 7,5/10 — el giro histórico.</b> La deuda de largo plazo casi se duplicó "
        "<b>en un solo trimestre</b> (US$65,6B → US$119,1B) para financiar el capex. La posición neta "
        "cayó de +$55B a +$21B, y contando los leases de largo plazo (US$91B) ya es deuda neta. La deuda "
        "es IG, larga y barata — no tóxica —, pero la dirección es inequívoca: <b>por primera vez, el "
        "flywheel no se paga solo.</b> [HECHO]")]
    o += [M.p("<b>Nota de ROIC incremental (R7).</b> El capex−D&amp;A (~US$81B TTM) es inversión "
        "discrecional pura cuyo retorno se prueba en 2027-28. Si rinde a márgenes AWS, el owner earnings "
        "normalizado escala hacia US$75B+ y esta tesis cambia; si es sobre-inversión, el FCF real es el "
        "que ya vemos (~cero). El whipsaw de vidas útiles de servidores (5→6→5 años según convenía al "
        "resultado) sugiere además que la D&amp;A contable <i>subestima</i> el coste económico del "
        "silicio de vida corta — lo que haría el owner earnings aún menor. [HECHO el whipsaw; "
        "INFERENCIA la lectura]")]
    o += [M.p("<b>Lo que sostiene el score alto:</b> R3 liderazgo 10/10 y R4 moat 10/10 (los máximos "
        "legales: multi-liderazgo y multi-moat genuinos), R2 industria 9/10, R6 diversificación 8,5/10. "
        "Calibrada contra las anclas: por debajo de Visa y Microsoft (posiciones más limpias, sin el "
        "lastre capex/Anthropic/FCF) y comparable a MercadoLibre en calidad de plataforma. El debate "
        "decisivo es de precio — y va en el §9.")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def s5():
    o = M.flag_titulo("§5 · El moat", "Cuatro fosos que se alimentan entre sí — ninguno bajo ataque estructural")
    o += [M.tabla([
        ["Foso", "Fuente de la ventaja", "Anchura (Porter /25)", "¿Bajo ataque?"],
        ["Logística", "Densidad de red: #1 carrier US (6.700M paquetes); coste marginal decreciente", "10 — el más profundo", "No (UPS/FedEx en retirada)"],
        ["Publicidad", "Datos de INTENCIÓN de compra (quién compró qué): el santo grial del closed-loop", "11 — el más rentable", "No (gana cuota al triopolio)"],
        ["AWS", "Switching costs (IAM, VPC, egress) + silicio propio (Trainium &gt;$20B run-rate)", "12", "Relativo (Azure/GCP crecen más)"],
        ["Marketplace", "Efecto red de doble lado (60% units 3P) + Prime como pegamento", "14 — el más disputado", "Walmart, TikTok Shop"],
    ], [3.2*cm, 6.8*cm, 3.2*cm, 3.1*cm], font_sz=7.8)]
    o += [M.p("<b>El origen de AWS es el mejor ejemplo de exaptación</b> (exaptation: el fenómeno "
        "evolutivo por el que un rasgo desarrollado para una función termina sirviendo, sin planearlo, "
        "para otra completamente distinta — las plumas que evolucionaron para aislar del frío y "
        "terminaron permitiendo el vuelo). En 2002 Bezos emitió una orden interna —conocida después como "
        "el «API Mandate»— que prohibía a cualquier equipo de Amazon acceder directamente a las bases de "
        "datos de otro equipo: todo dato y toda función debían exponerse a través de interfaces de "
        "servicio (APIs, los puntos de conexión estandarizados por los que un programa habla con otro) "
        "diseñadas, desde el primer día, para poder externalizarse. La orden no perseguía crear un "
        "negocio de nube; perseguía disciplina de ingeniería interna. Una década de esa disciplina fue "
        "lo que hizo posible construir AWS sobre cimientos ya pensados para venderse a terceros: el foso "
        "de switching costs (costes de cambio, la fricción y el riesgo que un cliente enfrenta al migrar "
        "de proveedor) que AWS disfruta hoy no se diseñó como arma competitiva — se heredó de una regla "
        "de higiene de software de hace veinticuatro años. [HECHO el mandato, documentado por "
        "exempleados de Amazon; INFERENCIA la lectura evolutiva]")]
    o += [M.p("<b>La lectura estructural.</b> A diferencia de Duolingo (moat blando bajo ataque de la "
        "IA) o incluso de Microsoft (frente IA disputado), <b>ninguno de los cuatro fosos de Amazon — "
        "que se alimentan entre sí como los órganos de un mismo organismo — está bajo ataque "
        "estructural</b>. La logística se profundiza (los rivales se retiran del last-mile, el tramo "
        "final de la entrega); la publicidad gana cuota al triopolio; AWS re-acelera con la ventaja de "
        "coste del silicio propio; y el marketplace absorbió el ataque de Temu/Shein (desinflado por "
        "tarifas). El único matiz honesto es <i>relativo</i>: AWS crece a la mitad que Azure y un tercio "
        "que Google Cloud — no pierde clientes, pero pierde cuota incremental del mercado nuevo. "
        "[HECHO/INFERENCIA]")]
    o += [M.callout("CASO HISTÓRICO",
        "La última vez que Amazon reinvirtió tan agresivamente que el mercado dudó — 2014-2015, cuando "
        "el capex de fulfillment y AWS parecía «gasto sin retorno» — la acción pasó dos años lateral y "
        "luego multiplicó por ocho: el capex ERA el moat haciéndose más ancho. El eco de ese precedente "
        "es la mejor carta alcista de hoy. La diferencia que impide copiar la conclusión: en 2015 Amazon "
        "cotizaba a ~2x ventas con el mercado ESCÉPTICO; hoy cotiza a 3,5x ventas con el mercado "
        "CREYENTE (Strong Buy unánime, PT $313). El mismo capex, la misma duda operativa — pero el precio "
        "de entrada opuesto. El precedente valida el negocio, no la compra.")]
    o += [M.p("<b>El talón de Aquiles no es competitivo: es contable-financiero.</b> El foso se financia "
        "ahora con deuda (+$53B en un trimestre) y la señal de demanda que lo justifica (el backlog de "
        "AWS) está parcialmente contaminada por la circularidad de Anthropic: el mismo dólar de Amazon "
        "aparece dos veces como buena noticia — como backlog contratado de AWS y como revalorización de "
        "su participación. Si el capex de los laboratorios de IA se enfría, la demanda «financiada por "
        "el proveedor» y la ganancia contable se evaporan <b>a la vez</b>. Esa correlación de riesgos es "
        "la vigilancia central del §12. [INFERENCIA sobre HECHOs]")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def s6():
    o = M.flag_titulo("§6 · El campo de batalla competitivo", "Cuatro frentes; el más peligroso no es el que parece")
    o += [M.tabla([
        ["Frente", "Rival #1", "Situación"],
        ["Cloud", "Microsoft Azure (+40%), Google (+63%)", "AWS #1 en cuota (~30%) pero #3 en crecimiento: gana en absoluto, cede en incremental"],
        ["E-commerce", "Walmart (único con flywheel físico-digital)", "AMZN ~38-40% del online US; Temu/Shein desinflados por tarifas; TikTok Shop crece en social"],
        ["Publicidad", "Google, Meta", "#3 con ~17% y el que MÁS RÁPIDO gana cuota (+24% vs Google +5,6%)"],
        ["Logística", "UPS, FedEx (en retirada)", "#1 carrier US; la rivalidad se invirtió: ahora AMZN les quita el freight"],
    ], [2.6*cm, 5.4*cm, 8.4*cm], font_sz=7.9)]
    o += [M.p("<b>El frente que decide la década es el cloud</b> — no porque AWS esté perdiendo (re-aceleró "
        "a +28%, su mejor dato en 15 trimestres, con US$364B de backlog), sino porque es donde se juega "
        "el retorno del capex de US$200B. La carrera tiene una particularidad casi ecológica: las tres "
        "nubes compiten por el mismo alimento escaso —energía y chips—, así que el crecimiento de cada "
        "una mide en parte <i>cuánta capacidad logró enchufar</i>, no solo cuánta demanda capturó, como "
        "tres especies disputándose el mismo territorio de caza en un año de sequía. La ventaja "
        "idiosincrática de Amazon es el <b>silicio propio</b>: Trainium (&gt;$20B run-rate, +triple "
        "dígito) le da un coste por token que Azure — atado a Nvidia — no puede igualar, y OpenAI y "
        "Anthropic ya comprometieron 7 GW combinados sobre él. [HECHO]")]
    o += [M.p("<b>Walmart es el rival más subestimado</b> — el único que libra la misma guerra en dos "
        "frentes a la vez. Es el único competidor del planeta con un volante físico-digital comparable: "
        "4.700 tiendas como mini-almacenes, e-commerce creciendo a doble dígito, Walmart Connect "
        "replicando el playbook publicitario y Walmart+ atacando a Prime. No amenaza la existencia de "
        "Amazon; amenaza su <i>tasa de crecimiento marginal</i> en el retail US — que es distinto, pero "
        "relevante para un precio que exige perfección. [HECHO/INFERENCIA]")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def s7():
    o = M.flag_titulo("§7 · Porter: fosos por segmento", "Estructura competitiva favorable en las cuatro líneas")
    o += [ch("12_porter", 14.8), sp(2)]
    o += [M.p("Las Cinco Fuerzas se puntúan por segmento (menor = mejor foso). El promedio ponderado "
        "(~11,75/25) describe una <b>estructura competitiva ancha y favorable</b>: barreras de entrada "
        "casi infinitas en logística y cloud (capital), poder sobre proveedores-vendedores 3P (Amazon "
        "fija las comisiones), y compradores atomizados retenidos por Prime. Las fuerzas adversas se "
        "concentran en dos puntos: la <b>rivalidad</b> en cloud (guerra de capex a tres bandas) y en "
        "retail (Walmart), y el <b>contrapeso regulatorio</b> — el juicio antitrust de la FTC (febrero "
        "2027) ataca precisamente el poder de Amazon sobre sus vendedores 3P, el corazón del flywheel. "
        "[análisis propio sobre 8-K/10-K]")]
    o += [M.callout("PAUSA REFLEXIVA",
        "Contradicción Porter↔Seilern — esta vez invertida. En Duolingo y Microsoft, Porter era adverso y "
        "el moat alto: había que explicar el mecanismo de inmunidad. En Amazon, Porter es FAVORABLE "
        "(11,75/25) y el moat es máximo (R4 10/10) — los marcos coinciden. Cuando calidad estructural y "
        "posición competitiva apuntan igual de alto, la única variable que queda para generar retorno es "
        "el PRECIO pagado. Un negocio perfecto comprado a precio perfecto rinde exactamente el coste de "
        "capital — y comprado por encima, menos. Por eso el §9 es, en esta tesis más que en ninguna, "
        "donde se decide todo.")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def s8():
    o = M.flag_titulo("§8 · TAM, SAM, SOM, runway y catalizadores", "Pista de sobra; el problema nunca fue el mercado")
    o += [ch("13_tam", 15.2), sp(2)]
    o += [M.p("Amazon toca cuatro mercados gigantes con penetración de un dígito en el mayor: el "
        "e-commerce global es ~US$4,5 billones dentro de un retail total de ~US$30 billones (Amazon "
        "captura ~9% del online mundial y ~1,4% del retail total); el cloud (~US$389B creciendo ~15%) "
        "donde es #1; la publicidad digital (~US$662B) donde es el #3 que más rápido gana; y la "
        "logística como opción real de tercer negocio (el precedente AWS: convertir un centro de coste "
        "en un negocio de plataforma). <b>El runway no es el problema y nunca lo fue.</b> "
        "[top-down HECHO de terceros; síntesis INFERENCIA]")]
    o += [M.p("<b>Reconciliación del TAM publicitario — global vs. solo EE.UU.</b> Los ingresos TTM de "
        "Amazon Ads (&gt;US$70.000M) sobre el TAM publicitario digital global 2026 (~US$662.300M, Grand "
        "View Research) dan ≈10,6% de cuota — coherente con la cifra independiente de eMarketer (9,0% de "
        "cuota global para 2026). El «~17%» citado en el §6 mide un universo distinto: la cuota de "
        "Amazon <i>solo del gasto publicitario digital de EE.UU.</i>, que eMarketer proyecta en 17,3% "
        "para 2026 (tercer lugar, detrás de Google 23,9% y Meta 20,9%). Ambas cifras son correctas — "
        "miden mercados distintos — y no deben promediarse ni confundirse. [HECHO ambas fuentes]")]
    o += [M.p("<b>Penetración e-commerce, desagregada — el runway doméstico real.</b> La fuente primaria "
        "gubernamental (Census Bureau) sitúa la penetración del e-commerce sobre el total de ventas "
        "minoristas de EE.UU. en <b>16,4% en Q1'26</b> (subiendo desde 15,9% un año antes) — más "
        "conservadora que el 22,5% que usa eMarketer con metodología distinta. Cruzando con la cuota de "
        "Amazon del e-commerce estadounidense (37,6%-40,5%, tabla §6), su cuota implícita del <b>retail "
        "total</b> de EE.UU. es apenas <b>≈6,2%</b> — el runway doméstico, medido sobre el pastel "
        "completo, es mayor de lo que sugiere mirar solo la cuota online. El contrapeso: la cuota de "
        "Amazon dentro del e-commerce ya no crece — tocó techo en 41,8% en 2021 y ha retrocedido desde "
        "entonces —, señal de saturación en la categoría core pese al TAM de retail total aún enorme. No "
        "existe un «Census internacional» equivalente al 9% global usado arriba y en el DCF; ese sigue "
        "siendo la mejor aproximación disponible. [HECHO Census/eMarketer; INFERENCIA el cálculo de "
        "cuota de retail total; SUPUESTO la ausencia de fuente primaria internacional única]")]
    o += [M.p(f"<b>Verificación de consistencia con el DCF.</b> Nótese la inversión del uso habitual: "
        f"aquí el TAM enorme no es el argumento de compra — es la explicación de por qué el mercado paga "
        f"prima. El escenario base del DCF (owner earnings +13% → +6%, WACC 10,4%) NO exige cuota heroica "
        f"de ningún TAM; aun así arroja US${D.PWFV}. Lo que exige el <b>precio</b> (~20% de crecimiento "
        f"por década) equivale a asumir que Amazon ejecuta a la perfección en los cuatro mercados a la "
        f"vez, sin de-rating y sin que el capex tropiece. La brecha entre lo que el negocio necesita y lo "
        f"que el precio asume ES la tesis. [INFERENCIA]")]
    o += [M.p("<b>Catalizadores 2026-2028</b> (que el precio ya descuenta, total o parcialmente): (1) "
        "la conversión del capex → si AWS mantiene +25-28% al monetizar el backlog de US$364B + "
        "Anthropic, el FCF reaparece hacia 2028; (2) <b>Trainium como negocio de silicio</b> (US$225B en "
        "compromisos); (3) la publicidad extendiéndose fuera de Amazon (Rufus, Netflix, CTV); (4) "
        "robótica y automatización del fulfillment (el margen NA hacia el 10%+); (5) el <b>plateau del "
        "capex</b> — el mismo catalizador de FCF que en Microsoft, solo que aquí el mercado ya lo paga "
        "por adelantado. [HECHO los datos; SUPUESTO las trayectorias]")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def s9():
    o = M.flag_titulo("§9 · Valoración multi-método", "El output de val-mos: gran negocio, precio de burbuja")
    o += [M.p("<b>Paso 0 — detector de trampas: GRIS.</b> Amazon no es una trampa de valor — es el "
        "problema <b>inverso</b>: no hay deterioro que el precio esconda; hay un precio que esconde la "
        "ausencia de deterioro... y de margen. De las seis señales duras, ninguna dispara: ROIC por "
        "encima del WACC promedio y con narrativa verificable; cuota estable o ganando; no es el "
        "disruptor; márgenes en récord. Pero una verificación adversarial (9-jul-2026) amplió las alertas "
        "no vetantes de dos a tres: la <b>contabilidad</b> (neto inflado por la revalorización circular "
        "de Anthropic — obliga a descartar el P/E GAAP), la <b>deuda naciente</b> (+$53B en un trimestre "
        "con FCF cero, y una emisión adicional sorpresa de $25.000M el 8-jul-2026 que ya ensancha "
        "spreads hyperscaler en todo el sector), y la <b>concentración de calidad-de-ingresos</b> — el "
        "backlog de AWS excluye hasta US$138.000M en compromisos de OpenAI, que se suman a Anthropic como "
        "segundo gran cliente-inversor circular. Tres alertas ya no es un PASA limpio: es <b>GRIS</b>. El "
        "detector sigue sin vetar; <b>la valoración es la que frena.</b> [val-mos]")]
    o += [ch("05_owner_earnings", 14.6), sp(2)]
    o += [M.p("<b>Paso 1 — owner earnings: la única caja que cuenta.</b> Las tres métricas de beneficio "
        "de Amazon están rotas para valorar: el neto GAAP está inflado por Anthropic; el FCF (−$2,5B) "
        "está aplastado por el capex de crecimiento; el EBITDA ignora que aquí la depreciación es un "
        "coste brutalmente real. La reconstrucción del dueño: CFO US$148,5B − capex de mantenimiento "
        "(proxy D&amp;A, US$70B) − SBC (US$20B) = <b>~US$58B</b> (rango honesto 55-75; bajista 42 si el "
        "silicio se deprecia en 2-3 años como argumenta el whipsaw). El yield del dueño sobre el market "
        "cap: <b>~2,2% — P/OE ~45x</b>. El verificador adversarial estresó esta construcción y concluyó "
        "que el ancla de $58B es «si acaso generosa, nunca heroica».")]
    o += [ch("10_dcf_inverso", 14.8)]
    o += [M.p("<b>Paso 2 — DCF inverso: el candado HEROICO.</b> A US$244,59 el precio despeja un "
        "crecimiento de owner earnings de <b>~20% anual durante una década</b> — casi el doble del CAGR "
        "histórico de ingresos (11,1%) y por encima de cualquier tasa base razonable para una empresa de "
        "US$2,6 billones. El único ancla que roza ese número es el consenso de EPS (+23%), que ya asume "
        "la monetización perfecta del capex. Cuando las expectativas embebidas son heroicas, el sistema "
        "activa el candado: <b>solo se compra en zona GANGA</b> y el MoS exigido sube 10 puntos "
        "(25% → 35%). Es la imagen especular de Microsoft, donde el precio descontaba 7,7% con Azure al "
        "40% — allí el pesimismo regalaba; aquí el optimismo cobra.")]
    o += [ch("07_dcf", 14.4)]
    o += [M.p("<b>Tabla de nueve supuestos del DCF:</b>")]
    o += [M.tabla([
        ["#", "Supuesto", "Elección", "Etiqueta"],
        ["1", "Crec. owner earnings, años 1–5", "~13% (AWS +18-25%, ads +18%, margen retail expande)", "INFERENCIA"],
        ["2", "Crec. owner earnings, años 6–10", "~6-8% (hacia PIB + prima)", "SUPUESTO"],
        ["3", "Crecimiento terminal", "3,0%", "SUPUESTO"],
        ["4", "WACC", "10,4% = CAPM propio (beta 1,47, Rf 4,55%, ERP Damodaran 4,23%) ponderado con deuda", "HECHO/INFERENCIA"],
        ["5", "Owner earnings base", "~US$58B (CFO − D&amp;A − SBC); NO se suma de vuelta capex de crecimiento", "INFERENCIA"],
        ["6", "ROIC incremental del capex", "sin probar; base asume rendimiento PARCIAL (no pleno)", "SUPUESTO"],
        ["7", "Dilución neta anual por SBC", "~+0,5% (SBC 2,7% de ventas y bajando)", "HECHO"],
        ["8", "Ajuste FX", "Intl +19% rep / +11% cc → FX viento de cola hoy; neutro a 10 años", "SUPUESTO"],
        ["9", "Fase de capital allocation", "Reinversión total apalancada con deuda — sin dividendo ni recompra material", "HECHO"],
    ], [0.7*cm, 4.5*cm, 8.5*cm, 2.7*cm], font_sz=7.8)]
    o += [ch("17_wacc", 13.4), sp(2)]
    o += [ch("18_sensibilidad", 14.4)]
    o += [M.p(f"<b>Sensibilidad — el gráfico más importante de la tesis.</b> Cruzando WACC (9,4-11,4%, "
        f"centrado en el 10,4% verificado) × crecimiento terminal (2-4%), el valor del escenario base se "
        f"mueve entre US${D.SENS[-1][0]} y US${D.SENS_MAX}. <b>Ninguna celda alcanza el precio de "
        f"US$244,59.</b> Para justificar el precio de hoy hay que asumir el escenario alcista Y bajar el "
        f"WACC simultáneamente — es decir, pagar por la perfección con descuento de bono, justo cuando el "
        f"propio mercado de crédito (bono AMZN del 8-jul-2026) empieza a exigir más, no menos. Los "
        f"métodos secundarios cuentan la misma historia con matices: el EV/EBITDA (16,8x vs mediana "
        f"27,6x) grita «barata», pero es la lente equivocada — ignora que la D&amp;A de US$70B es un "
        f"coste real y creciente; el P/OCF (17,7x) dice «razonable»; y la lente del dueño (P/OE ~45x) "
        f"dice lo que el DCF confirma. Cuando las lentes divergen así, val-mos manda usar la del dueño.")]
    o += [ch("09_multiplos", 14.8), sp(2)]
    o += [ch("08_zonas", 15.4)]
    o += [M.p(f"<b>Paso 3 — zonas y veredicto.</b> Ancladas al PWFV de US${D.PWFV}: GANGA ≤US${D.Z_GANGA}, "
        f"OPORTUNIDAD hasta US${D.Z_OPORT}, JUSTO hasta US${D.Z_JUSTO}, CARO hasta US${D.Z_CARO}, y "
        f"<b>BURBUJA por encima — donde está el precio de hoy (US${D.es(D.PRECIO,0)}, prima del "
        f"+{D.es(D.PRIMA,0)}%)</b>. La asimetría es negativa ({D.es(D.ASIMETRIA,2)}): al valor ponderado "
        f"hay {D.es(D.MOS_HOY,0)}%; al escenario alcista, ~{D.es((D.V_BULL/D.PRECIO-1)*100,0)}%; al "
        f"bajista, ~{D.es((D.V_BEAR/D.PRECIO-1)*100,0)}%. Contra el consenso (Strong Buy, PT US$313): la "
        f"calle valora sobre el EPS reportado que incluye a Anthropic y sobre EV/EBITDA — las dos lentes "
        f"que este sistema descarta por contaminadas. <b>Veredicto: {D.VEREDICTO}.</b> El gatillo se fija "
        f"donde el sistema recupera margen: primer tramo en US${D.GATILLO_T1}, posición plena hacia "
        f"US${D.GATILLO_PLENO}. Eso exige una corrección de ~{D.es(D.CAIDA_A_GANGA,0)}% desde el máximo — "
        f"rara, pero es exactamente el orden de magnitud que DUOL acaba de vivir y la que convierte "
        f"grandes negocios en grandes inversiones.")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def s10():
    o = M.flag_titulo("§10 · Gestión, cultura y gobernanza", "La retribución más limpia de las megacaps; la gobernanza formal, no tanto")
    o += [M.p("Andy Jassy (CEO desde 2021, fundador de AWS) es un operador de primer nivel con el track "
        "record ya en los números: margen operativo del 2,4% (2022) al 13,1% (récord), ~30.000 recortes "
        "corporativos con la tesis de «el startup más grande del mundo», y AWS re-acelerado. Jeff Bezos "
        "(Executive Chair) mantiene <b>8,8% de la empresa — US$230.000 millones de skin in the game "
        "real</b> (participación económica genuina, no solo simbólica), el mayor de cualquier megacap. "
        "[HECHO, DEF 14A]")]
    o += [ch("14_mgmt", 13.4), sp(2)]
    o += [M.p("<b>La cultura, en tres reglas que no están en ningún manual de RR.HH.</b> Desde los "
        "primeros años, Bezos institucionalizó dejar una silla vacía en las reuniones importantes: la "
        "silla del cliente, recordatorio físico de que la persona más importante de la sala nunca está "
        "presente. Impuso también la «regla de las dos pizzas»: ningún equipo debía ser mayor de lo que "
        "dos pizzas grandes pueden alimentar (entre seis y diez personas), para que la comunicación "
        "siguiera siendo directa y la burocracia no se acumulara — el equivalente organizacional a "
        "mantener las células pequeñas para que el organismo entero siga siendo ágil. Y desde 2004, casi "
        "todo proyecto grande —Kindle, AWS, Prime Video— se construye con el método «Working Backwards» "
        "(trabajar hacia atrás): el equipo escribe primero el comunicado de prensa y las preguntas "
        "frecuentes del producto terminado, antes de programar una sola línea de código, y solo avanza "
        "si ese borrador —a veces reescrito diez veces— convence genuinamente a un cliente imaginario. "
        "[HECHO]")]
    o += [M.p("<b>La cultura, medida en la nómina.</b> La estructura retributiva es la más limpia del "
        "S&amp;P 500: salario base congelado en US$365.000 para todos los ejecutivos desde hace más de "
        "una década, cero bonus, cero opciones, cero métricas de corto plazo — solo RSUs (unidades de "
        "acciones restringidas) a largo plazo. "
        "La prueba de simetría real: en 2022, cuando la acción cayó 50%, la «compensación realmente "
        "pagada» del CEO fue <b>negativa en $148 millones</b>. Pocas empresas del mundo pueden mostrar "
        "eso. [HECHO]")]
    o += [M.p("<b>Los deméritos, sin maquillar.</b> (1) <b>Gobernanza formal débil</b>: Bezos preside el "
        "consejo desde 1994 sin ser independiente, y el board recomendó votar EN CONTRA de un presidente "
        "independiente en 2026. (2) <b>Conflicto de dedicación</b>: Bezos es desde nov-2025 co-CEO de "
        "Project Prometheus, una startup de IA externa — el Executive Chair de Amazon compite por su "
        "propio tiempo (y potencialmente por talento de IA). (3) <b>La asignación de capital está en su "
        "punto de máxima tensión</b>: la casa que nunca pagó dividendo ni recompró de forma material "
        "ahora reinvierte MÁS de lo que genera, financiándose con deuda récord. El lifecycle es "
        "coherente con un ROIC incremental alto <i>si</i> el capex rinde — y esa condición está abierta. "
        f"Score de management: <b>{D.es(D.MGMT_TOTAL,0)}/30</b>. [HECHO/INFERENCIA]")]
    o += [sp(4), M.p("<b>Track record de M&amp;A y grandes apuestas de capital (última década).</b> "
        "Antes de puntuar «gestión» hay que revisar la partida completa, no solo la jugada de apertura "
        "que salió bien — el precedente favorable de AWS 2014-15:")]
    o += [M.tabla([
        ["Apuesta", "Resultado", "Detalle"],
        ["Whole Foods (2017)", "Éxito", "US$13.700M en efectivo; ancla del canal físico + integración Prime"],
        ["MGM Studios (2022)", "Éxito", "US$8.450M, ~40% más que otros postores (Apple, Comcast); contenido para Prime Video"],
        ["Fire Phone (2014)", "Fracaso", "Writedown de US$170M + US$83M en inventario sin vender; discontinuado en &lt;1 año"],
        ["Amazon Care (2019-2022)", "Fracaso", "Cerrado tras 3 años; la propia empresa admitió que «no es una oferta suficientemente completa» para clientes enterprise"],
        ["iRobot (2022-2024)", "Fracaso", "Acuerdo de US$1.700M terminado en ene-2024 por bloqueo de la UE; breakup fee de US$94M; iRobot despidió 31% de su plantilla meses después"],
    ], [3.6*cm, 2.3*cm, 10.5*cm], font_sz=7.9)]
    o += [M.p("El track record es, por tanto, <b>mixto</b> — dos aciertos grandes frente a al menos tres "
        "reversiones costosas —, lo cual sustenta el <b>3,5/5</b> ya asignado a la subcategoría «Track "
        "record M&amp;A» del score de gestión (desglose abajo) en vez de basarlo solo en el precedente "
        "de AWS. [HECHO los cinco casos; INFERENCIA la síntesis]")]
    o += [sp(2), M.p("<b>Desglose del score de gestión (6 dimensiones).</b>", "h3")]
    filas_mgmt = [["Dimensión", "Puntos /5"]]
    for dim, pts in D.MGMT:
        filas_mgmt.append([dim, D.es(pts, 1)])
    filas_mgmt.append(["<b>TOTAL</b>", f"<b>{D.es(D.MGMT_TOTAL,1)}/30</b>"])
    o += [M.tabla(filas_mgmt, [12.4*cm, 4.0*cm], font_sz=8.4)]
    o += [sp(4), M.p("<b>Estructura de capital: deuda en balance, no vehículos fuera de balance.</b> "
        "Amazon colocó &gt;US$53.000M en bonos en 2026 (US$37.000M en EE.UU. en 11 tramos + €14.500M en "
        "Europa en 8 tramos, con vencimientos a 30/40/50 años; el tramo en euros fue el mayor jamás "
        "colocado por un emisor corporativo en ese mercado) y comunicó que no planea emitir más deuda "
        "este año. [HECHO, CNBC 7-jul-2026] En paralelo, la industria migra hacia vehículos fuera de "
        "balance: &gt;US$120.000M de capex de datacenters de IA ya se trasladó a SPV financiados con "
        "crédito privado — Meta lo formalizó con su JV de US$27.000M con Blue Owl (Hyperion), Microsoft "
        "explora una estructura similar con BlackRock/GIP, y Google respalda vehículos como TeraWulf. "
        "<b>Amazon no ha anunciado una SPV/JV comparable</b>: sigue financiando el grueso de su capex de "
        "IA con deuda corporativa directa y flujo operativo propio, concentrando el apalancamiento en su "
        "propio balance en vez de aislarlo en una entidad de terceros con recurso limitado. [HECHO ambos "
        "hechos] A diferencia de sus comparables directos, el riesgo de sobre-construcción de "
        "infraestructura de IA recae íntegramente sobre el balance consolidado de AMZN — coherente con "
        "la señal ya roja de R8 (deuda LP casi duplicada en un trimestre). [INFERENCIA]")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def s11():
    o = M.flag_titulo("§11 · Nueve inversores legendarios opinan", "Cero compradores — el veto unánime es al precio, no al negocio")
    o += [ch("16_inversores", 15.0), sp(2)]
    pares = [
        ("Graham", "PASS", "P/OE 45x, FCF negativo, deuda duplicándose: no hay ni margen sobre activos ni sobre beneficios. Su pass más rotundo de la trilogía."),
        ("Buffett", "HOLD", "Adora el flywheel y a Bezos («el mejor hombre de negocios de nuestra era», dijo). Pero su regla #1 es el precio: a 45x la caja del dueño, esperaría — como esperó 20 años para comprar Apple al múltiplo correcto."),
        ("Munger", "HOLD", "Invierte la pregunta: ¿qué lo mata? Nada operativo — solo el precio pagado. «Un gran negocio a un precio malo es una mala inversión.» Sostendría; jamás iniciaría aquí."),
        ("Fisher", "HOLD", "El scuttlebutt es el mejor del panel (7/10): clientes que no se van, ejecución impecable, I+D líder. Compraría la calidad — pero incluso Fisher exigía «precio razonable», y 45x owner earnings no lo es."),
        ("Lynch", "HOLD", "La historia es fácil de contar, pero su PEG con el EPS normalizado PLANO es infinito este año. «Cualquier empresa es mala inversión al precio equivocado.»"),
        ("Templeton", "PASS", f"Compra en el punto de máximo pesimismo. Aquí hay máximo OPTIMISMO: Strong Buy unánime, PT 28% arriba, prima del {D.es(D.PRIMA,0)}%. Es exactamente el momento en que él vende, no compra."),
        ("Marks", "PASS", "¿Qué descuenta el precio? El éxito completo del capex de IA antes de probarse — y el ciclo de capex de IA está en euforia. Primer nivel: gran empresa. Segundo nivel: todos lo saben, y ya está en el precio."),
        ("Seilern", "HOLD", f"Calidad 80: alta pero no Núcleo (capital pesado, earnings contaminados). Y su disciplina de valoración nunca pagaría prima del {D.es(D.PRIMA,0)}% sobre el valor. En el banquillo."),
        ("Terry Smith", "HOLD", "Regla #2: «no pagues de más». A 45x owner earnings con FCF negativo, se paga de más por definición. Sostendría lo comprado barato; no añadiría un dólar hoy."),
    ]
    filas = [["Inversor", "Veredicto y razonamiento en una línea"]]
    for nm, vd, txt in pares:
        filas.append([f"<b>{nm}</b><br/><font size=7 color='#666054'>{vd}</font>", txt])
    o += [M.tabla(filas, [2.5*cm, 13.9*cm], font_sz=8.2)]
    o += [M.callout("PAUSA REFLEXIVA",
        "En Microsoft, ocho de nueve compraban. Aquí, CERO — y sin embargo nadie critica el negocio: la "
        "palabra que se repite en las nueve fichas es «precio». Cuando el panel entero converge en "
        "admirar la empresa y rechazar la acción, el mensaje es preciso: no hay nada que esperar del "
        "negocio (ya es excelente y todos lo saben) y todo que esperar del precio (que hoy no paga a su "
        "dueño ni el coste de capital). La divergencia relevante es contra el CONSENSO de Wall Street "
        "(Strong Buy, $313): ellos valoran el EPS que incluye a Anthropic; el panel valora la caja del "
        "dueño. El tiempo dirá qué lente era la correcta — y el feedback loop del Cuadro de Mando lo "
        "registrará.")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def s12():
    o = M.flag_titulo("§12 · Riesgos: matriz, pre-mortem y alerta temprana", "Los dos riesgos dominantes están correlacionados")
    o += [ch("15_riesgos", 15.2), sp(2)]
    o += [M.p("Los dos riesgos dominantes —el capex sin ROIC (retorno sobre el capital invertido) "
        "probado (prob 3 × impacto 5) y la reversión de Anthropic (3 × 4)— <b>no son independientes: "
        "son dos ríos que nacen de la misma montaña</b>. Si la monetización de la IA decepciona, los "
        "laboratorios recortan el capex, la demanda vendor-financed (financiada por el propio proveedor) "
        "de AWS se enfría, el backlog se ablanda, Anthropic sufre un down-round (una ronda de "
        "financiación a valuación más baja que la anterior) y los US$16,8B de ganancia contable se "
        "revierten contra el neto — todo en la misma ventana de trimestres. La cartera debe tratar esa "
        "correlación como un solo evento de cola (tail event: un desenlace de baja probabilidad pero "
        "alto impacto) con doble detonación. [INFERENCIA]")]
    o += [M.p("<b>Pre-mortem narrativo</b> (la técnica de imaginar el fracaso ya consumado y reconstruir, "
        "hacia atrás, cómo se llegó a él). Es 2031 y la inversión (comprada a US$244 en 2026) salió mal. "
        "¿Qué pasó? No quebró Amazon — el flywheel siguió girando, como sigue girando siempre. Lo que "
        "pasó fue más banal: la monetización de la IA llegó más lenta de lo prometido; el capex de "
        "US$200B se convirtió en US$85B anuales de depreciación que comprimieron el margen de AWS del "
        "37% al 29%; el owner earnings (la caja que le queda al dueño después de mantener el negocio, no "
        "la que reporta el GAAP) creció al 8%, no al 20% que el precio exigía; Anthropic se marcó a la "
        "baja en 2028 y el «beneficio» de 2026 se deshizo en público; y el múltiplo — construido sobre el "
        "EPS inflado — se normalizó. La acción no colapsó: simplemente pasó seis años yendo a ninguna "
        "parte mientras el negocio crecía por debajo de ella. La compañía nunca dejó de llamarlo Día 1 "
        "—pero el precio, para 2031, ya había decidido hacía tiempo que era Día 2. <b>El riesgo de pagar "
        "prima por perfección no es la ruina: es la década perdida.</b> Cisco 2000, Microsoft 2000, "
        "Walmart 2000 — todos grandes negocios, todos una generación para recuperar el precio pagado.")]
    o += [ch("20_early_warning", 15.4), sp(2)]
    o += [M.p(f"<b>Sistema de alerta temprana (VI.7).</b> El semáforo tiene una foto inusual: <b>los "
        f"verdes son del negocio, los rojos y ámbar son del precio y la contabilidad</b>. Unit growth "
        f"+15%, AWS +28%, margen retail expandiendo, publicidad +22% — el moat está sano. El FCF (flujo "
        f"de caja libre) negativo (rojo), la deuda duplicándose más una emisión adicional de $25.000M el "
        f"8-jul-2026 (ámbar), el carrying value (valor contable en libros) de Anthropic en US$32B más "
        f"hasta US$138.000M de compromisos OpenAI (ámbar) y el historial de whipsaw (vaivén) en las "
        f"vidas útiles (ámbar) son las tensiones. <b>Reglas duras:</b> (1) si "
        f"el FCF sigue negativo entrado 2027 con el capex sin plateau (meseta) → la señal de deuda se "
        f"vuelve "
        f"estructural; (2) un down-round de Anthropic u OpenAI → re-correr el detector entero por "
        f"escrito antes de cualquier decisión; (3) unit growth &lt;+8% o AWS &lt;+20% sostenidos, o el "
        f"ROIC incremental de AWS (~8% hoy) sin recuperarse por encima del WACC en 2-3 trimestres → el "
        f"flywheel se frena y el escenario bajista (US${D.V_BEAR}) toma el timón. Del lado de la compra: "
        f"<b>−25% desde máximo (~US$209) revisa, −35% (~US$181) prepara, US${D.GATILLO_T1} dispara.</b>")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def s13():
    o = M.flag_titulo("§13 · Veredicto final, triggers y proyección", "ESPERAR: la watchlist también es una posición")
    o += [M.p(f"<b>Cruce de los dos ejes.</b> CALIDAD <b>{D.es(D.SCORE_QG,1)}/100 · tier {D.TIER_QG}</b> "
        f"(ratificado en §4, con la corrección aritmética documentada). VALORACIÓN <b>{D.VEREDICTO}</b> "
        f"(ratificado en §9, corrección val-mos 9-jul-2026): detector {D.DETECTOR}, PWFV US${D.PWFV}, "
        f"zona {D.ZONA_HOY}, prima +{D.es(D.PRIMA,0)}%, MoS {D.es(D.MOS_HOY,0)}% contra un exigido de "
        f"+{D.es(D.MOS_EXIG,0)}%. Los dos ejes no podrían estar más de acuerdo: <b>gran negocio, gran "
        f"precio equivocado.</b> Sin overrides.")]
    o += [M.p(f"<b>Frase-tesis (registrada para el feedback loop).</b> «El mercado no teme nada en "
        f"Amazon — y ese es el problema: a US$244,59 (−12% del máximo) paga por el éxito completo del "
        f"capex de IA de US$200B antes de que exista un dólar de retorno probado, sobre un beneficio "
        f"inflado por la revalorización circular de Anthropic y con el flujo de caja libre en negativo; "
        f"el PWFV honesto sobre la caja del dueño es ~US${D.PWFV} (banda US$92-121), y ni el escenario "
        f"alcista (US${D.V_BULL}) alcanza el precio de hoy. El ROIC incremental de AWS, medido en el "
        f"10-K, es ~8% — por debajo de este WACC de 10,4%.»")]
    o += [M.p(f"<b>Elemento falsable (qué refutaría ESTA tesis de sobrevaloración).</b> Me equivoco y "
        f"habría que comprar más arriba de US${D.GATILLO_T1} si: (a) el <b>owner earnings normalizado "
        f"demuestra superar ~US$85-90B sostenidos</b> — es decir, se prueba que menos del 40% del capex "
        f"es mantenimiento y que los datacenters ya rinden a márgenes AWS; o (b) el <b>FCF se recupera "
        f"hacia US$80-100B en dos años sin sacrificar crecimiento</b> (la digestión del capex que el "
        f"precio asume se hace real); o (c), el gatillo específico de esta corrección: el <b>ROIC "
        f"incremental de AWS debe recuperarse por encima del WACC (10,4%) en los próximos 2-3 reportes "
        f"trimestrales</b> — si en vez de eso se mantiene o cae más cerca de 8%, el escenario bajista deja "
        f"de ser el 35% de probabilidad que hoy le asigno y pasa a ser el caso base. Cualquiera de las "
        f"primeras dos me obligaría a subir el PWFV y re-anclar las zonas — por datos, no por FOMO. El "
        f"registro queda escrito para auditarlo.")]
    o += [M.tabla([
        ["Plan operativo", "Nivel", "Acción"],
        ["Hoy", f"US${D.es(D.PRECIO,0)}", "ESPERAR — 0% del NAV. Watchlist activa. (Si ya se posee: sostener, NO ampliar)"],
        ["Alerta 1 (revisar)", "~US$209 (−25% del máx.)", "Re-correr detector + refrescar PWFV"],
        ["Alerta 2 (preparar)", "~US$181 (−35% del máx.)", "Candidata a tramo si detector no empeora a rojo"],
        ["Gatillo tramo 1 (3% NAV)", f"≤US${D.GATILLO_T1} (GANGA)", "Comprar primer tramo con falsable escrito"],
        ["Posición plena (4-5% NAV)", f"~US${D.GATILLO_PLENO} (MoS {D.es(D.MOS_EXIG,0)}%)", "Solo con capex en digestión y Anthropic/OpenAI sin reversión"],
    ], [5.2*cm, 4.4*cm, 6.8*cm], font_sz=8.0)]
    o += [M.p("<b>Reglas de venta duales (para el tenedor).</b> Amazon es tier Alta convicción con moat "
        "intacto: <b>no se vende por múltiplo caro</b> — vender un compounder por ancla de precio es el "
        "error Graham/GEICO. Se vendería solo por deterioro del negocio: detector en rojo, flywheel "
        "frenándose (unit growth &lt;8%), o el evento correlacionado Anthropic+capex. La asimetría del "
        "tenedor y la del comprador son distintas: el que ya la tiene cabalga un gran negocio con coste "
        "hundido; el que compra hoy paga la perfección por adelantado. Esta tesis habla al comprador.")]
    o += [M.p(f"<b>Proyección a 5 años (3 escenarios, desde US$244,59).</b> Alcista ({D.P_BULL}%): el "
        f"capex rinde a márgenes AWS, owner earnings +18%, y aun así el valor 2031 (~US$340-370) implica "
        f"~7-8% anual — <i>mediocre para el riesgo asumido</i>. Base ({D.P_BASE}%): digestión parcial, OE "
        f"+13%→+6% — la acción va lateral años hasta que el valor alcance al precio (~4-5% anual con "
        f"suerte). Bajista ({D.P_BEAR}%, el peso que sube tras la verificación de 9-jul-2026): la IA "
        f"decepciona, el ROIC incremental de AWS no recupera el WACC, doble detonación Anthropic+OpenAI, "
        f"de-rating a la lente del dueño — US${D.V_BEAR}-120, pérdida del 50-89%. <b>Esperada ponderada: "
        f"~+1-3% anual — por debajo del coste de capital. La matemática entera de esta compra solo "
        f"funciona a otro precio. Por eso: ESPERAR.</b>")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def cierre():
    o = M.flag_titulo("Glosario y advertencias finales", "Términos, etiquetas y la naturaleza de este documento")
    o += [M.p("<b>Glosario.</b>", "h3")]
    gl = [
        ("Backlog (AWS)", "obligaciones contratadas pendientes de reconocer: US$364B (+93%), sin contar Anthropic."),
        ("Circularidad (round-tripping)", "Amazon financia a Anthropic; Anthropic gasta en AWS; la valoración de Anthropic sube; Amazon contabiliza la ganancia."),
        ("Flywheel", "el volante de Bezos: precios→tráfico→vendedores→selección→costes→precios."),
        ("EPV", f"valor de los beneficios sin crecimiento; suelo teórico de la valoración (US${D.EPV})."),
        ("FCF (definición Amazon)", "flujo operativo menos capex neto; hoy NEGATIVO por el capex de IA."),
        ("Owner earnings", "CFO − capex de mantenimiento (≈D&A) − SBC ≈ US$58B: la caja del dueño."),
        ("PWFV-Valor", "valor intrínseco ancla del sistema val-mos (tri-método probabilístico)."),
        ("Candado HEROICO", "cuando el DCF inverso muestra expectativas heroicas: MoS exigido +10pp y compra solo en GANGA."),
        ("Take rate 3P", "lo que Amazon captura del GMV del vendedor (comisión+FBA+ads): ~50-60% all-in, subiendo."),
        ("Whipsaw de vidas útiles", "el vaivén 5→6→5 años en la depreciación de servidores, según convenía al resultado."),
    ]
    filas = [["Término", "Definición"]]
    for t, d in gl:
        filas.append([f"<b>{t}</b>", d])
    o += [M.tabla(filas, [4.2*cm, 12.2*cm], font_sz=8.2)]
    o += [sp(4), M.p("<b>Advertencias finales.</b>", "h3")]
    o += [M.p("Cada dato se etiquetó <b>HECHO</b> (fuente primaria: 10-K FY2025, 10-Q Q1 2026, DEF 14A "
        "2026 en SEC EDGAR CIK 0001018724, y 8-K de resultados), <b>INFERENCIA</b> o <b>SUPUESTO</b> — "
        "la misma disciplina que Amazon exige de sus propios equipos con el método Working Backwards: "
        "nada se escribe antes de resistir la pregunta de un lector escéptico. "
        "Cabos NO divulgados por Amazon, declarados: GMV, take rate exacto, suscriptores y churn de "
        "Prime, margen de publicidad, y el split silicio/edificios dentro del capex. El score de calidad "
        "se corrigió de 85,6 a 80,2 por error aritmético (dos reglas puntuadas sobre el máximo legal), "
        "detectado por el verificador adversarial — la corrección bajó el tier y subió el margen "
        "exigido. La valoración sobrevivió a su propio verificador adversarial, que la hizo más severa. "
        "Este veredicto (ESPERAR) discrepa frontalmente del consenso de Wall Street (Strong Buy, PT "
        "~US$313): la diferencia es la lente — EPS reportado vs caja del dueño. El score Seilern mide "
        "<b>calidad, no valoración</b>. Documento de <b>uso personal</b>; no constituye asesoría "
        "registrada.")]
    o += [M.callout("PAUSA REFLEXIVA",
        "Qué queda por saber — las dos piezas que más cambiarían el veredicto: <b>el split real del capex "
        "entre mantenimiento y crecimiento</b>, y si el <b>ROIC incremental de AWS</b> (~8% medido hoy) "
        "recupera el WACC en los próximos 2-3 trimestres. Si Amazon divulgara (o pudiera estimarse con "
        "confianza) que el mantenimiento real es muy inferior a la D&A — digamos US$45B en vez de US$70B "
        "— el owner earnings saltaría hacia US$85B, el PWFV hacia ~US$155 y este veredicto cambiaría de "
        "ESPERAR a VIGILAR: el mismo garaje de 1994, sencillamente, habría vuelto a apostar bien. En "
        "sentido contrario: si el whipsaw de vidas útiles se resuelve acortándolas "
        "(como la economía real del silicio sugiere) o el ROIC incremental no recupera el WACC, el owner "
        "earnings baja hacia US$42B y hasta el precio de GANGA sería caro. Prioridad de investigación: el "
        "detalle de PP&E por categoría del próximo 10-K, el margen trimestral de AWS (Q2'26) y cualquier "
        "disclosure de margen publicitario. Vuelo con el rango US$55-75B; el que afine ese número, afina "
        "toda la tesis.")]
    return o

# ══════════════════════════════════════════════════════════════════════════
def story():
    s = []
    for fn in [portada, changelog, resumen, cuadro_mando, veredicto_cuant,
               s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, cierre]:
        s += fn()
    return s
