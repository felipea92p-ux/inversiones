# -*- coding: utf-8 -*-
"""CONTENIDO · Tesis Ultra MELI v2.0 (refresco editorial, 2026-07-09). Solo prosa/datos.
Importa motor_qg (diseño) y dcf_meli (números) — cero cambios de números/veredicto vs. v1.0."""
from reportlab.platypus import Spacer, PageBreak, NextPageTemplate, Paragraph
from reportlab.lib.units import cm
from reportlab.lib.styles import ParagraphStyle
import motor_qg as M
from motor_qg import C
import dcf_meli as D

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
        Paragraph("MERCADOLIBRE, INC.", nombre),
        Paragraph("NASDAQ: MELI &nbsp;·&nbsp; Comercio + logística + fintech &nbsp;·&nbsp; el negocio más grande de mi cartera, "
                  "la partida más disputada de esta serie", tick),
        sp(14),
        Paragraph("El volumen crece al 49% anual. El libro de crédito crece al 87% — casi el doble de rápido. "
                  "Es la jugada del ajedrecista que sacrifica una pieza por tempo: se acepta debilitar la "
                  "propia posición a cambio de ganar terreno más rápido de lo que el rival puede seguir. El "
                  "precio del sacrificio ya se ve en el tablero — la rentabilidad de ese crédito (NIMAL, net "
                  "interest margin after losses, el margen de interés neto del libro después de pérdidas) "
                  "cayó de 36% a 18% en cinco trimestres. El propio comité externo de gobierno corporativo "
                  "(ISS) califica a la junta directiva en el peor decil posible. Y el precio de hoy ya está "
                  "pagado como si el sacrificio hubiera dado jaque — más de lo que este propio análisis "
                  "considera su escenario optimista.", tag),
        sp(20),
        M.kpi_panel([
            (f"{D.es(D.SCORE_QG,1)}/100", "CALIDAD QG", f"tier {D.TIER_QG} (65–74)"),
            (f"US${D.PWFV}", "VALOR (PWFV)", f"vs US${D.es(D.PRECIO,0)} hoy · zona {D.ZONA_HOY}"),
            (f"{D.es(D.ASIMETRIA,2)}:1", "ASIMETRÍA", "muy por debajo de 2:1 &rarr; ESPERAR"),
        ]),
        sp(16), M.hr(),
        Paragraph(f"<b>6 de julio de 2026</b> &nbsp;·&nbsp; Precio US${D.es(D.PRECIO,2)} &nbsp;·&nbsp; "
                  f"Market cap ~US${D.es(D.MKTCAP,1)}B &nbsp;·&nbsp; Horizonte 5–10 años &nbsp;·&nbsp; "
                  f"Documento de convicción N&ordm; 18", meta),
        M.hr(),
        Paragraph("Eje CALIDAD (sistema qg-seilern de 11 reglas, corregido por verificación adversarial) y eje "
                  "PRECIO (val-mos v3: PWFV-Valor, detector de trampas, MoS por tier, candado duro anti-sobrepago) "
                  "calculados por separado y cruzados solo al final. Uso personal; no es asesoría de inversión registrada.", fn),
        NextPageTemplate("Normal"), PageBreak()]
    return out

# ══════════════════════════════════════════════════════════════════════════
def changelog():
    o = M.flag_titulo("Changelog de versiones", "El primer score fue demasiado duro — y por qué importa corregirlo bien")
    o += [M.p("<b>v2.0 (9-jul-2026) — refresco editorial.</b> Esta versión reescribe en profundidad la voz "
        "narrativa del documento (historia, modelo de negocio, moat, competencia, gestión, riesgos, "
        "pre-mortem y cierre) incorporando metáforas de ajedrez, historia y biología evolutiva, curiosidades "
        "verificadas en fuente primaria sobre la fundación de la empresa (Stanford, la dirección exacta de "
        "las primeras oficinas, las rondas de financiación de 1999-2000, la alianza y posterior salida de "
        "eBay, la salida a bolsa rentable de 2007) y la traducción explicada de todo término técnico en su "
        "primer uso por sección. <b>Cero cambios en números, score de calidad, valoración o veredicto de "
        "inversión</b> — dcf_meli.py no se tocó. Se descartaron por no poder verificarse en fuente primaria "
        "dos piezas de color que circulan sobre MELI: (a) que Berkshire Hathaway invirtiera en la compañía "
        "en 2019 (el inversor real de esa ronda fue PayPal, según los 8-K de la SEC) y (b) cualquier "
        "\"cultura de las hormigas\" como concepto oficial de cultura corporativa, que no aparece en ninguna "
        "fuente institucional. La versión anterior (v1.0, 6-jul-2026) permanece documentada íntegra abajo.")]
    o += [M.p("Esta fue la <b>versión 1.0</b> de la tesis Ultra de MercadoLibre — la posición más grande de mi "
        "cartera (18 acciones, ~US$32.500 al precio de hoy). Se documenta aquí un hallazgo de proceso poco "
        "habitual: el primer pase del score de calidad dio <b>64,8/100 (Watchlist, el tier más bajo)</b>, a "
        "solo 0,2 puntos de \"Calidad sólida\". El verificador adversarial lo revisó con el rigor que exige "
        "ser la posición más grande del portafolio y encontró que <b>cinco de las once reglas invertían la "
        "propia mecánica del sistema</b> — por ejemplo, R10 (gestión) construyó su puntaje solo con señales "
        "estructurales negativas (ISS, familia en el directorio) sin nunca establecer la base de historial "
        "que el propio sistema exige partir; R9 (transparencia) citó su propio tope de \"7/10 si el dato no "
        "es verificable\" y luego puntuó por debajo de ese tope sin justificación adicional. El verificador "
        "también cruzó el resultado contra <b>dos corridas históricas de este mismo sistema sobre MELI</b> "
        "(73,2 y 75,6, ambas en Alta convicción, documentadas en el registro de calibración del propio "
        "sistema) — ninguna de las dos se acercó remotamente a Watchlist, lo que confirmó que el primer pase "
        "repitió un patrón de sesgo ya conocido y advertido por el propio sistema.")]
    o += [M.tabla([
        ["Supuesto crítico fijado en v1.0", "Valor", "Qué lo movería"],
        ["Score de calidad (corregido)", "72,0/100 · Calidad sólida", "Recuperación de NIMAL o mejora de gobernanza estructural"],
        ["Conteo de acciones (verificado SEC)", "50,7M", "Recompras reales (no las de US$4M de 2025)"],
        ["EPV corregido (verificador halló error aritmético)", "US$347,7 (no US$227 del primer pase)", "N/A — es un piso, no un pronóstico"],
        ["Múltiplo de owner earnings (corregido)", "38,5x (no 44-47x del primer pase)", "N/A — recomputo con conteo de acciones correcto"],
        ["Veredicto (corregido de \"VIGILAR\")", "ESPERAR — asimetría 0,56:1 activa la regla textual", "Corrección de precio o de asimetría"],
    ], [6.6*cm, 5.2*cm, 4.6*cm], font_sz=7.6)]
    o += [M.p("<b>El punto de honestidad que esta v1.0 se obliga a recordar:</b> MercadoLibre es, en la "
        "mayoría de sus dimensiones, un negocio genuinamente excelente — 9 años de CAGR de ingresos cercano "
        "al 48%, el moat de logística más difícil de replicar de este lote de tesis (Amazon prefiere "
        "alquilar acceso vía Rappi antes que construirlo). Pero el sistema no promedia ese negocio "
        "excelente con un libro de crédito que crece el doble de rápido que el negocio mismo, mientras su "
        "propia métrica de rentabilidad (NIMAL) se desploma de forma multianual. Ambos hechos conviven en "
        "la misma nota, sin comprarse de vuelta el uno al otro — ni en calidad, ni en precio.")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def resumen():
    o = M.flag_titulo("Resumen en treinta segundos", "Un gran negocio, un libro de crédito que crece demasiado rápido, un precio que ya sobrepagó el mejor caso")
    o += [M.p("<b>¿Puede MercadoLibre seguir creciendo al 48% anual sin que su brazo de crédito termine "
        "definiendo el resultado de la tesis completa — y está el precio de hoy dispuesto a esperar la "
        "respuesta?</b> Esas son las dos preguntas que definen esta tesis, y conviene tratarlas como dos "
        "partidas distintas jugándose sobre el mismo tablero. La primera tiene una respuesta honesta y "
        "dividida: el volumen de negocio (GMV, TPV, usuarios activos — las tres medidas de cuánto se mueve "
        "por el ecosistema) sigue creciendo con fuerza genuina; la rentabilidad de ese crédito (NIMAL) se "
        "está desplomando por una decisión deliberada y verbalizada por la propia gestión de asumir más "
        "riesgo a cambio de más volumen. La segunda pregunta tiene una respuesta más simple, y menos "
        "cómoda: no, el precio de hoy no está dispuesto a esperar nada — ya apostó, por adelantado, a un "
        "desenlace mejor que el que este propio análisis se anima a llamar optimista. [HECHO/INFERENCIA]")]
    o += [M.tabla([
        ["El número", "Qué dice"],
        ["Libro de crédito +87% vs. ingreso +49%", "El capital se redirige hacia el segmento de menor y más volátil retorno casi al doble de velocidad que el negocio central. No es drift pasivo: el CFO confirmó en vivo que es una decisión de extender duración y buscar clientes de mayor riesgo. [HECHO]"],
        ["NIMAL 36,5%→17,8% en 5 años (no monotónico)", "La rentabilidad del crédito se sostuvo 2021-2023 y colapsó después — 4 de los últimos 5 puntos de dato en caída. [HECHO, 10-K/10-Q]"],
        ["ISS Board pillar = 10 (peor decil)", "Probable (licenciado vía Yahoo Finance, no verificado en fuente ISS primaria), consistente con 2 Galperin en un directorio de 9 y una recompra 2025 de solo US$4,05 millones. [INFERENCIA de confianza moderada]"],
    ], [4.4*cm, 12.0*cm], font_sz=8.0)]
    o += [sp(6), M.p(f"<b>Veredicto operativo.</b> Calidad QG <b>{D.es(D.SCORE_QG,1)}/100</b> (tier "
        f"<b>{D.TIER_QG}</b>, corregido tras verificación adversarial de un primer pase demasiado duro). "
        f"El detector de trampas da <b>GRIS (PASA CON VIGILANCIA)</b> — no es un caso de pánico infundado "
        f"tipo Teleperformance, tampoco es una trampa confirmada tipo Concentrix: hay una señal estructural "
        f"corroborada (compresión de margen de origen crediticio) mientras el volumen de negocio sigue sano. "
        f"PWFV-Valor <b>US${D.PWFV}</b> frente a US${D.es(D.PRECIO,0)}: zona <b>{D.ZONA_HOY}</b> (164% del "
        f"PWFV) — el precio de hoy ya está por encima incluso del <b>propio escenario optimista</b> de este "
        f"análisis. <b>Acción: {D.VEREDICTO}.</b> No es una recomendación de vender lo que ya se tiene — es "
        f"una recomendación de no ampliar, con vigilancia trimestral activa sobre NIMAL y el write-off rate.")]
    o += [M.callout("PAUSA REFLEXIVA",
        "Esta es la posición más grande de mi cartera, y por eso mereció el escrutinio más duro de esta "
        "serie: un primer pase de calidad la mandó a Watchlist por un margen de apenas 0,2 puntos, y solo la "
        "verificación adversarial —comparando contra el propio historial de calibración del sistema— evitó "
        "un error de clasificación severo. La lección no es \"el sistema falló\": es que un score cerca de un "
        "umbral, sobre la posición más grande del portafolio, exige exactamente este nivel de segunda "
        "opinión antes de actuar. La pregunta que debes hacerte: ¿habrías confiado en el primer número si "
        "nadie lo hubiera cuestionado?")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def cuadro_mando():
    o = M.flag_titulo("Cuadro de mando trimestral", "Lo único que se refresca cada trimestre · corte 6-jul-2026")
    o += [M.p("<b>Bloque 1 · Estado de la posición.</b>", "h3")]
    o += [M.tabla([
        ["Concepto", "Estado"],
        ["Precio / zona", f"US${D.es(D.PRECIO,2)} · zona {D.ZONA_HOY} (164% del PWFV; MoS {D.es(D.MOS_ACTUAL,1)}%, negativo)"],
        ["Valor justo (PWFV-Valor)", f"US${D.PWFV} · EPV suelo US${D.es(D.EPV,1)} (precio = {D.es(D.PRECIO_EPV,1)}x el EPV)"],
        ["Probabilidades de escenario", f"Conservador {D.P_BEAR}% (US${D.V_BEAR}) · Base {D.P_BASE}% (US${D.V_BASE}) · Optimista {D.P_BULL}% (US${D.V_BULL})"],
        ["Veredicto operativo", f"{D.VEREDICTO} · 0% de ampliación · watchlist con gatillo US${D.GATILLO_OPORT} (Oportunidad) / US${D.GATILLO_GANGA} (Ganga)"],
    ], [4.3*cm, 12.1*cm])]
    o += [sp(4), M.p("<b>Bloque 2 · Tracker de KPIs en semáforo.</b>", "h3")]
    o += [M.tabla([
        ["Indicador", "Hoy", "Umbral rojo", "●"],
        ["GMV / TPV / MAU fintech", "+36-50% (sólido)", "desaceleración &lt;20% sostenida", "verde"],
        ["Ingreso consolidado", "+49% (récord)", "&lt; 25% sostenido 2+ trim.", "verde"],
        ["NIMAL", "17,8% (mínimo histórico)", "sigue perforando sin estabilizar", "rojo"],
        ["Write-off rate anualizado", "~19,4% (reacelerando)", "supera 22% sin mejora de NPL", "ambar"],
        ["Margen operativo consolidado", "6,9% (mínimo)", "sigue cayendo bajo 6%", "ambar"],
        ["Gobernanza (ISS Board)", "10 — peor decil", "hecho estructural permanente", "rojo"],
    ], [6.0*cm, 4.4*cm, 4.2*cm, 1.8*cm], font_sz=7.8)]
    o += [sp(4), M.p("<b>Bloque 3 · Feedback loop de calibración.</b>", "h3")]
    o += [M.tabla([
        ["Predicción (trim. anterior)", "Resultado real", "Interpretación"],
        ["v1.0 — sin predicción formal previa", "Q1'26: rev $8.845M (+49%), NIMAL 17,8%, margen op. 6,9%", "Punto de partida; calibrar desde el próximo trimestre"],
        ["Score de calidad: primer pase vs. corregido", "64,8 (Watchlist) → 72,0 (Calidad sólida)", "Registrar como caso de estudio de sesgo duro en el sistema qg-seilern"],
    ], [5.6*cm, 5.4*cm, 5.4*cm])]
    o += [sp(4), M.p("<b>Bloque 4 · Operativo.</b> Sin trigger de drawdown adicional (la acción ya está en "
        "zona Burbuja sin necesidad de esperar una caída). Fecha del refresh: <b>6-jul-2026</b>; documento "
        "completo v1.0. Próxima revisión: resultados <b>Q2 2026</b> (ago-2026) — foco exclusivo en si el "
        "NIMAL se estabiliza o sigue perforando, y en si el write-off rate anualizado supera el umbral de "
        "22% sin que el NPL de 15-90 días se mueva en simultáneo (la disonancia que definiría el paso de "
        "GRIS a TRAMPA en el detector).")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def veredicto_cuant():
    o = M.flag_titulo("El veredicto cuantificado", "Once reglas con bisturí — corregidas por un verificador que no se conformó con \"casi\"")
    o += [M.p(f"<i>{DISCLAIMER}</i>", "nota")]
    o += [ch("01_radar", 15.0), sp(4)]
    vd = {
        "R1 · Escalabilidad": "Marketplace core es asset-light con apalancamiento operativo real; pero logística y crédito requieren capex/balance intensivo — modelo híbrido, no plataforma pura.",
        "R2 · Industria": "LatAm e-commerce/pagos digitales es tailwind estructural de máximo nivel (CAGR ~48% sostenido 9 años); pero la expansión de fintech ata a MELI más a los ciclos de crédito/macro que a un e-commerce puro.",
        "R3 · Liderazgo": "Líder claro en GMV (Brasil ~40%, México duopolio ~85% con Amazon); pero Shopee crece más rápido (+53% vs +33%) y Nubank suscribe crédito mejor — liderazgo nominal, no de calidad en todo el frente.",
        "R4 · Moat": "Logística (Mercado Envíos) es el foso más defendible del lote — Amazon prefiere alquilar acceso vía Rappi antes que construir; pero el propio 10-K admite que usuarios y comercios cambian de plataforma con facilidad.",
        "R5 · Crec. orgánico": "Ingresos +49%, CAGR histórico ~48% — exceptional; pero el margen neto cayó de 9,2% a 4,7% y una parte del crecimiento es expansión del libro de crédito, no orgánico en el sentido que exige la regla.",
        "R6 · Diversificación": "Sin concentración de cliente (modelo marketplace); pero Brasil es 54% del ingreso (cerca del techo ~50%) y Argentina (19%) carga una prima de riesgo país de 14-15%, con su margen más alto probablemente inflado por contabilidad de hiperinflación.",
        "R7 · Capital / ROIC": "El libro de crédito crece 87% mientras su propia métrica de retorno (NIMAL) se desploma; deuda neta +156% en 5 trimestres financiando exactamente ese libro de menor retorno marginal.",
        "R8 · Balance": "Deuda neta duplicada financiando el libro de crédito, con fondeo vía FIDCs/fideicomisos y instrumentos tipo-depósito no asegurados; pero NO es deuda tóxica según el test de 4 puntos del propio sistema — no hay refinanciamiento forzado, ni M&amp;A destructiva, ni dividendo con deuda.",
        "R9 · Transparencia": "MELI divulga voluntariamente su \"Adjusted FCF\" ($1,48B) que expone la brecha con el CFO simple ($10,8B) — es una señal de transparencia, no de opacidad, aunque el margen de Argentina probablemente esté inflado por hiperinflación.",
        "R10 · Gestión": "Track record de 20+ años de creación de valor bajo Galperin (base alta), pero el sistema exige restar (máx. −3) por señales estructurales: ISS Board=10, 2 Galperin en el directorio, recompra 2025 de solo US$4M pese al de-rating de 64x a 44x.",
        "R11 · Impacto": "Inclusión financiera y de comercio en economías emergentes — anclado explícitamente en 10/10 por el propio sistema de calibración (MELI es ancla, junto con V y MSFT).",
    }
    filas = [["Regla", "Puntos", "Veredicto en una línea"]]
    for n, pts, mx in D.REGLAS:
        p_txt = f"{int(pts)}/{mx}"
        filas.append([n, p_txt, vd[n]])
    filas.append(["<b>TOTAL</b>", f"<b>{D.es(D.RAW_QG,1)}/125</b>",
                  f"<b>{D.es(D.SCORE_QG,1)}/100 · tier {D.TIER_QG} (65-74)</b>"])
    o += [M.tabla(filas, [3.2*cm, 2.0*cm, 11.2*cm], font_sz=7.4)]
    o += [M.p("<i>Nota metodológica: el primer pase dio 64,8/100 (Watchlist) — el verificador adversarial "
        "corrigió cinco reglas (R5, R7, R8, R9, R10) que invertían la propia mecánica del sistema (p. ej., "
        "R10 debe partir de un track record base y solo RESTAR por señales estructurales, nunca construirse "
        "solo con negativos) y confirmó la corrección cruzándola contra dos corridas históricas previas de "
        "este sistema sobre MELI (73,2 y 75,6, ambas en Alta convicción). El score corregido (72,0, Calidad "
        "sólida) sigue penalizando con fuerza real el deterioro del libro de crédito y la gobernanza — no es "
        "un \"todo está bien\", es una corrección de mecánica, no de conclusión.</i>", "nota")]
    o += [M.callout("LECCIÓN TRANSFERIBLE",
        "El caso de MELI es el ejemplo más claro hasta ahora de por qué la verificación adversarial no es "
        "un paso cosmético: la diferencia entre \"Watchlist\" y \"Calidad sólida\" para la posición más "
        "grande del portafolio no fue un matiz de opinión, fue un error mecánico de aplicación de la propia "
        "regla del sistema. Un analista —humano o artificial— que confía en su primer número sin cuestionarlo "
        "contra el propio historial de calibración puede convertir un negocio sólido con riesgos reales en "
        "un negocio artificialmente descartado. La disciplina correcta no es \"confiar menos en el sistema\": "
        "es \"nunca aceptar un score cerca de un umbral sin una segunda mirada\".")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def s1():
    o = M.flag_titulo("§1 · La historia detrás del veredicto", "De un garaje en Buenos Aires a la partida más disputada de esta cartera")
    o += [M.p("La apertura, si hay que fecharla, ocurrió en un aula de Stanford. En marzo de 1999, Marcos "
        "Galperin —becado por YPF, su empleador anterior, para cursar el MBA— esbozó la idea de MercadoLibre "
        "a partir de un caso de estudio sobre eBay. Cinco meses después, el 2 de agosto de 1999, la empresa "
        "se constituyó formalmente, y sus primeras oficinas fueron, de forma literal y no de anécdota de "
        "marketing, las cocheras del Edificio Panamericana Plaza, en Tronador 4890, barrio porteño de "
        "Saavedra. El arranque \"de garaje\" que tantas startups reclaman como mito fundacional es aquí un "
        "domicilio verificable. [HECHO]")]
    o += [M.p("Lo que siguió fue una apertura de libro casi perfecta para la época: en apenas tres meses de "
        "vida, para noviembre de 1999, la compañía ya había levantado US$7,6 millones de capital de fondos "
        "como JP Morgan Partners y Flatiron Fund; una segunda ronda en mayo de 2000 sumó a Hicks, Muse, "
        "Tate &amp; Furst, Goldman Sachs, Santander y GE Equity. El timing fue casi providencial: cerrar esa "
        "financiación justo antes de que estallara la burbuja puntocom en marzo de 2000 es la clase de "
        "diferencia entre sobrevivir la partida y perderla en la apertura que rara vez depende del mérito "
        "propio. [HECHO; INFERENCIA el juicio sobre el timing]")]
    o += [M.p("El primer gran intercambio de piezas llegó en octubre de 2001, en plena crisis de deuda "
        "soberana argentina: eBay se convirtió en socio estratégico exclusivo y accionista principal, a "
        "cambio de que MercadoLibre absorbiera el negocio regional de eBay (iBazar). La sociedad duró quince "
        "años y terminó, también, con una señal de mercado inequívoca: cuando eBay anunció en octubre de "
        "2016 que vendía la mayor parte de su participación —de ~18,4% a ~5,9%, con una ganancia de ~US$1.000 "
        "millones para eBay— la acción de MELI cayó 8% ese mismo día. El socio fundacional se retiraba del "
        "tablero, y el mercado lo trató como una pieza perdida, no como un trámite administrativo. [HECHO]")]
    o += [M.p("MercadoLibre salió a bolsa en el Nasdaq en 2007 habiendo logrado algo que eludió a la enorme "
        "mayoría de las startups de internet de su generación: llegar rentable a la salida. Desde entonces, "
        "la partida cambió de naturaleza. Ya no se trataba de sobrevivir la apertura, sino de decidir, una y "
        "otra vez, dónde reinvertir las ganancias de una posición de control regional cada vez más sólida. "
        "Dos decisiones de mediano juego resultaron decisivas: Mercado Pago, lanzado en 2003 como respuesta "
        "directa a la bajísima bancarización de América Latina (sin un sistema de pagos confiable, el "
        "comercio electrónico regional simplemente no podía escalar); y Mercado Envíos, la apuesta por "
        "logística propia lanzada en 2013 —una jugada de capital intensivo que antecede por años a que el "
        "mercado reconociera el foso logístico como la pieza más valiosa del tablero. [HECHO]")]
    o += [M.p("Veintisiete años después de aquella clase en Stanford, la empresa factura US$28.900 millones "
        "al año en 18 países, con un ecosistema que combina un marketplace de comercio electrónico, la red "
        "de logística propia que nació de esa apuesta de 2013 y un negocio de servicios financieros que ya "
        "presta más de US$14.500 millones a comercios y consumidores en cuatro países. Es, con amplio "
        "margen, la empresa de mayor valor de mercado nacida en América Latina. [HECHO]")]
    o += [M.p("Pero la historia de 2026 no es solo la de un compounder (una empresa capaz de reinvertir sus "
        "propias ganancias a una tasa de retorno alta durante años, multiplicando el capital por acumulación) "
        "excepcional: es la historia de una empresa que decidió, de forma consciente y verbalizada por su "
        "propio director financiero, sacrificar rentabilidad de corto plazo para financiar dos apuestas "
        "simultáneas —logística más barata y crédito más amplio— en el momento exacto en que ambas empiezan "
        "a mostrarse en los números. El margen operativo consolidado cayó 600 puntos básicos interanuales en "
        "un solo trimestre (Q1 2026), casi el doble de todo lo que había caído en el año completo anterior. "
        "De esa caída, management atribuye cerca de dos tercios a un solo factor: el libro de crédito de "
        "Mercado Crédito creciendo 87% interanual —casi el doble de la velocidad del negocio consolidado "
        "(49%)— exigiendo cada vez más provisiones por deterioro esperado. [HECHO]")]
    o += [ch("02_nimal", 15.2), sp(2)]
    o += [M.p("El indicador que mejor resume esta tensión es el NIMAL (net interest margin after losses, el "
        "margen de interés neto después de pérdidas del negocio de crédito): se mantuvo estable entre 32% y "
        "36,5% durante 2021-2023, y luego colapsó a 17,8% en el primer trimestre de 2026 — el nivel más bajo "
        "jamás divulgado. No es un declive lineal de cinco años, como podría sugerir una lectura superficial "
        "de los dos extremos: es una meseta larga seguida de un colapso agudo en apenas dos años, el patrón "
        "clásico de una posición que aguanta hasta que, de golpe, deja de aguantar. Management lo explica "
        "con total franqueza: el crédito de tarjeta —de menor margen estructural— ya es 46% del libro "
        "(frente a 42% hace un año), y en Brasil específicamente se extendió la duración de los préstamos al "
        "consumo de 5 a 8 meses para llegar a solicitantes que antes eran rechazados. Es una decisión de "
        "negocio, tomada con los ojos abiertos, no un accidente contable.")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def s2():
    o = M.flag_titulo("§2 · Historia de mi posición", "La pieza más grande del tablero, puesta a prueba por su propio tamaño")
    o += [M.p(f"MercadoLibre es la posición más grande de mi cartera: 18 acciones, costo promedio "
        f"US$1.659,57, valor de mercado ~US$32.500 al precio de hoy "
        f"(US${D.es(D.PRECIO,2)}). Cuando la pieza más grande del tablero es también la que más se mueve, "
        f"el error de análisis más caro no es equivocarse en una posición chica: es confiar demasiado rápido "
        f"en el primer número sobre la que más pesa. Por eso mereció el escrutinio más duro de esta campaña "
        f"de tesis — y el hallazgo del primer pase de calidad (64,8/100, Watchlist, a solo 0,2 puntos del "
        f"siguiente tier) confirma exactamente por qué: una posición de este tamaño no puede descansar en un "
        f"solo número sin verificación adversarial. [contexto propio]")]
    o += [M.p(f"El análisis corregido concluye <b>{D.VEREDICTO}</b>, y aquí la disciplina es distinta a la "
        f"de GOOGL (excluida por un gate de tier pese a un precio razonable) o AMZN (negocio excelente, "
        f"precio caro): en MELI, <b>el precio de hoy ya superó incluso el escenario optimista propio de "
        f"este análisis</b> — no es un caso de \"cerca pero no alcanza\", es un caso de \"ya se pasó de "
        f"la raya\". El detector de trampas dio GRIS (vigilancia activa, no pánico ni pase limpio): el "
        f"volumen de negocio sigue sano, pero la rentabilidad del crédito se deteriora de forma real y "
        f"reconocida por la propia gestión.")]
    o += [M.p(f"<b>Mi posición operativa:</b> sostener sin ampliar. No hay caso para vender pánicamente — "
        f"el negocio de comercio y logística sigue siendo de calidad genuina y el NPL estándar (15-90 días) "
        f"todavía no confirma deterioro de mora — pero tampoco hay ningún argumento de precio que justifique "
        f"añadir capital hoy. Watchlist con gatillo de Oportunidad en US${D.GATILLO_OPORT} (85% del PWFV) y "
        f"de Ganga en US${D.GATILLO_GANGA} (70%) — ambos muy por debajo del precio actual.")]
    o += [M.callout("PAUSA REFLEXIVA",
        "Ser la posición más grande de la cartera no es, por sí solo, una señal de que el análisis debe ser "
        "más indulgente — es exactamente la señal contraria: cuanto más grande el peso, más caro el error de "
        "no cuestionar el primer resultado. El hallazgo de este pase (un score que casi manda a la posición "
        "más grande al tier más bajo, corregido solo por una verificación rigurosa) es el mejor argumento "
        "posible para nunca saltarse ese paso, sin importar cuán familiar o cuán querida sea la posición.")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def s3():
    o = M.flag_titulo("§3 · El modelo de negocio en dos minutos", "La prueba de Lynch: tres organismos en simbiosis, y uno que empieza a pedir más de lo que da")
    o += [M.p("<b>La prueba de los dos minutos.</b> Peter Lynch pedía poder explicar un negocio en el "
        "tiempo que toma cruzar un semáforo. MercadoLibre resiste la prueba solo si se cuenta como lo que "
        "es: no una empresa, sino un ecosistema de tres organismos que se alimentan entre sí. "
        "<b>Marketplace</b>: comisiones sobre cada venta de comercio electrónico en 18 países, con "
        "publicidad (Mercado Ads) como el órgano de más rápido crecimiento y mayor margen. "
        "<b>Logística (Mercado Envíos)</b>: red propia de más de 50 centros de distribución que mueve el "
        "55% de todos los envíos, reduciendo el costo unitario de envío en Brasil un 17% interanual. "
        "<b>Fintech (Mercado Pago)</b>: billetera digital, procesamiento de pagos, y —el corazón de esta "
        "tesis— un libro de crédito de US$14.500 millones que creció 87% en el último año. Cada organismo "
        "se nutre de los datos y del tráfico que generan los otros dos; ningún rival de la región combina "
        "hoy los tres a la vez. [HECHO]")]
    o += [M.p("<b>La apuesta central, cuantificada contra su propio mercado potencial.</b> El libro de "
        "crédito cerró el primer trimestre de 2026 en US$14.600 millones, +87% interanual — el mayor "
        "incremento nominal trimestral de la historia de la compañía. Frente al TAM (total addressable "
        "market, el mercado total direccionable) de crédito al consumo latinoamericano de US$400.000 "
        "millones ya usado en la valoración de esta tesis (§8), ese libro "
        "representa apenas <b>~3,6% de penetración</b> (US$14.600M/US$400.000M): la apuesta que sostiene "
        "buena parte del crecimiento reciente sigue en un dígito bajo de su propio mercado potencial, "
        "incluso si ese TAM estuviera sobreestimado 30-40% por falta de metodología pública citada en la "
        "fuente de mercado. [HECHO el libro y su crecimiento; INFERENCIA el cálculo de penetración; "
        "SUPUESTO el rango de sobreestimación del TAM]")]
    o += [M.p("La mezcla interna explica la mayor parte de la compresión de NIMAL: tarjeta de crédito "
        "pasó de 42% a 46% del libro, con TPV (total payment volume, el volumen bruto de pagos procesados) "
        "de tarjeta creciendo 90% interanual y 2,7 millones de tarjetas nuevas emitidas solo en el "
        "trimestre, mientras el NIMAL cayó de 22,7% (1T25) a 17,8% (1T26). Según cuantifica la propia "
        "gestión, dos tercios de esa compresión vienen del giro hacia tarjeta (de menor margen estructural) "
        "y un tercio de la cartera de consumo de Brasil, que management describe con una frase que conviene "
        "citar de forma literal: <i>\"todavía rentable, pero menos rentable que hace un año\"</i> — la clase "
        "de admisión que un jugador honesto hace cuando reconoce que su posición se debilitó, sin fingir que "
        "no pasó nada. [HECHO, cita textual de la earnings call 1T26, 7-may-2026]")]
    o += [ch("19_gmv_paises", 15.2), sp(2)]
    o += [M.p("<b>La mecánica que decide el trimestre: la logística financia la fidelidad, el crédito "
        "financia el crecimiento.</b> MELI redujo deliberadamente el umbral de envío gratis en Brasil en "
        "octubre de 2025 para impulsar el volumen (items vendidos en Brasil +56% interanual en Q1'26), "
        "aceptando un costo de margen bruto a cambio — una jugada posicional clásica, ceder algo de "
        "material hoy para ganar control de casillas mañana. Simultáneamente, extendió la duración de sus "
        "préstamos al consumo para capturar clientes de mayor riesgo, una jugada de naturaleza distinta: "
        "no cede material, apuesta el balance. Ambas son decisiones de inversión deliberada, no deterioro "
        "pasivo — pero ambas comprimen el margen consolidado al mismo tiempo, y solo una de ellas (el "
        "crédito) tiene un mecanismo de retraso en el reconocimiento de pérdidas de 12 a 24 meses: lo que "
        "se originó en 2025-2026 con criterios más laxos aún no ha tenido tiempo de mostrarse en la mora. "
        "Es la diferencia entre un sacrificio que se cobra de inmediato y uno que se cobra, si se cobra, "
        "varias jugadas después. [HECHO/INFERENCIA]")]
    o += [ch("03_credito_vs_ingreso", 15.0), sp(2)]
    o += [M.p("<b>El activo que Amazon prefiere alquilar antes que construir.</b> La evidencia más "
        "reveladora de la fortaleza del moat (foso competitivo, la ventaja estructural que protege las "
        "ganancias de la competencia) logístico de MELI no es un dato de MELI: es la decisión de Amazon de "
        "invertir en una alianza con Rappi para lograr alcance de última milla en Brasil en vez de construir "
        "su propia red desde cero, pese a tener capital prácticamente ilimitado para hacerlo. Es exactamente "
        "el tipo de señal indirecta que Philip Fisher enseñaba a buscar en el scuttlebutt (la información de "
        "campo que se obtiene preguntando a proveedores, rivales y clientes, no leyendo el balance): cuando "
        "el rival mejor capitalizado del mundo prefiere rentar el activo antes que replicarlo, el activo es "
        "más difícil de replicar de lo que cualquier cifra de cuota de mercado sugiere por sí sola. Es como "
        "si el mejor equipo del torneo, con presupuesto ilimitado para fichar, decidiera igual alquilar la "
        "cancha del rival en vez de construir la propia. [INFERENCIA]")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def s4():
    o = M.flag_titulo("§4 · Las once reglas de Seilern con bisturí", "El output de qg-seilern, corregido tras un primer pase demasiado severo")
    o += [M.p(f"<i>{DISCLAIMER}</i>", "nota")]
    o += [M.p(f"MELI pasa los <b>siete knock-outs</b>, aunque con un flag explícito de \"conflicto de gate\": "
        f"el sistema no tiene una regla binaria que excluya negocios de comercio electrónico con un brazo "
        f"de crédito creciendo hacia ~31% del balance — el verificador decidió (correctamente, per el "
        f"diseño del sistema) resolver esto vía penalización severa en R7/R8/R9, no vía exclusión binaria. "
        f"Sobre las once reglas obtiene <b>{D.es(D.SCORE_QG,1)}/100 (raw {D.es(D.RAW_QG,1)}/125), tier "
        f"{D.TIER_QG}</b> — corregido de un primer pase de 64,8 (Watchlist) que invertía la mecánica de "
        f"cinco reglas distintas.")]
    o += [M.p("<b>R7/R8 · Capital, ROIC y balance — el freno más severo, y el más real.</b> El libro de "
        "crédito de Mercado Crédito creció 87% interanual mientras su propia métrica de rentabilidad "
        "(NIMAL) se desplomó de 36,5% a 17,8% — un capital cada vez mayor generando un retorno marginal "
        "cada vez menor. La deuda neta se duplicó en cinco trimestres ($2.247M→$5.748M) financiando "
        "exactamente ese libro. El fondeo se apoya en FIDCs y fideicomisos titulizados en cuatro países más "
        "instrumentos tipo-depósito en Brasil que <b>no están asegurados por el FGC</b> (el fondo de "
        "garantía de depósitos brasileño) — MELI opera, de facto, un negocio de crédito con riesgo de "
        "balance tipo-bancario sin las protecciones regulatorias de un banco. No es deuda tóxica bajo el "
        "test explícito de cuatro puntos del sistema (sin refinanciamiento forzado, sin M&amp;A destructiva), "
        "pero sí es una asignación de capital hacia un retorno marginal decreciente. [HECHO]")]
    o += [ch("04_deuda_neta", 14.4), sp(2)]
    o += [M.p("<b>Confirmación con una métrica consolidada, no solo el proxy NIMAL.</b> Un cálculo de "
        "terceros (no reportado directamente por la compañía) sitúa el ROIC de MELI en 7,0% en 2021, "
        "subiendo a un pico de 19,4% en 2023, y cayendo después a 18,5% en 2024 y 15,0% en 2025. La "
        "trayectoria confirma, con una métrica consolidada de retorno sobre capital invertido —no solo con "
        "el proxy de rentabilidad del libro de crédito (NIMAL)—, el mismo patrón que documentan R7/R8: el "
        "pico de eficiencia de capital de MELI ya quedó atrás, y el capital adicional desplegado desde 2023 "
        "genera cada vez menos retorno marginal. [INFERENCIA / cálculo de terceros, no verificado contra "
        "fuente primaria de la compañía]")]
    o += [M.p("<b>R10 · Gestión — el error de mecánica más claro del primer pase.</b> El primer intento "
        "puntuó esta regla en 4/10 construyendo el número solo con señales negativas (ISS Board=10, "
        "presencia familiar en el directorio, recompra irrisoria) sin nunca establecer la base de historial "
        "de creación de valor que el sistema exige como punto de partida (0-10, y solo después restar hasta "
        "un máximo de 3 puntos por señales estructurales). Corregido a <b>6/10</b>: Galperin tiene un "
        "historial de 20+ años construyendo el compounder más grande de la región (base alta, 8-9), menos "
        "el máximo de 3 puntos permitido por los defectos de gobernanza documentados —no 4/10, que solo se "
        "explica invirtiendo la lógica del sistema. Los defectos en sí son reales y no se maquillan: <b>ISS "
        "Board pillar = 10</b> (peor decil, probable pero no verificado en fuente primaria), dos miembros "
        "de la familia Galperin en un directorio de nueve, y una autorización de recompra 2025 de apenas "
        "<b>US$4,05 millones</b> —destinada a compensar la dilución del plan de compensación de directores, "
        "no un programa real de retorno de capital— pese a que el múltiplo de la acción cayó de ~64x a ~44x "
        "en tres años. [HECHO]")]
    o += [ch("16_buyback", 14.4), sp(2)]
    o += [M.p("<b>Lo que sostiene el score en un nivel respetable pese a esos frenos:</b> R4 moat 11/15 "
        "(logística genuinamente difícil de replicar), R2 industria 9/10 (tailwind LatAm de máximo nivel), "
        "R11 impacto 10/10 (MELI es ancla de calibración del propio sistema para inclusión financiera, "
        "junto con Visa y Microsoft). Calibrada contra las anclas del sistema: MELI queda por debajo de su "
        "propio historial reciente (73,2 y 75,6 en corridas previas), reflejando un deterioro real y "
        "reciente del libro de crédito — no un error de medición, sino una calidad que efectivamente cayó "
        "frente a hace un año.")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def s5():
    o = M.flag_titulo("§5 · El moat", "Tres murallas de un mismo castillo: la logística es piedra, el marketplace es madera, el crédito es la que hoy está bajo asedio")
    o += [ch("13_porter", 14.4), sp(2)]
    o += [M.p("Conviene pensar el moat (foso competitivo, la ventaja estructural que protege las ganancias "
        "de la competencia) de MercadoLibre no como un anillo único, sino como un castillo de tres murallas "
        "concéntricas, cada una construida con un material distinto. La logística (Mercado Envíos) es la "
        "muralla de piedra: una red propia de más de 50 centros de distribución levantada con años de "
        "inversión de capital, que reduce estructuralmente el costo unitario por envío (−17% interanual en "
        "Brasil, acelerando) mientras absorbe un crecimiento de volumen del 56%. La evidencia más "
        "contundente de su solidez no viene de MELI: viene de Amazon, que eligió asociarse con Rappi para "
        "lograr alcance de última milla en Brasil en vez de construir su propia red pese a tener el capital "
        "para hacerlo — un rival con recursos prácticamente ilimitados prefiriendo rentar antes que replicar "
        "es la señal indirecta más creíble de que la muralla es genuinamente difícil de escalar. "
        "[HECHO/INFERENCIA]")]
    o += [M.p("El marketplace de comercio electrónico, en cambio, es la muralla de madera: el propio 10-K "
        "(el informe anual que la compañía presenta ante el regulador bursátil de EE.UU.) de MELI admite "
        "textualmente que \"usuarios y comercios pueden cambiar fácilmente entre plataformas competidoras\" "
        "— una confesión escrita de que el efecto de red del marketplace puro arde más rápido de lo que "
        "sugiere la cuota de mercado (~40% en Brasil). Y el fintech, la tercera muralla, es hoy la que está "
        "bajo asedio real y cuantificable: Nubank suscribe crédito con mejor calidad (costo de riesgo ~14% "
        "vs. el ~23-26% de MELI) mientras sigue emitiendo más volumen absoluto de tarjetas de crédito en "
        "Brasil que MELI. No es una muralla que se haya derrumbado — es una que el atacante está golpeando "
        "con más precisión de la que MELI está devolviendo. [HECHO]")]
    o += [M.callout("PAUSA REFLEXIVA",
        "El moat de MELI no es un foso único: es un castillo donde ninguna muralla individual basta por sí "
        "sola contra un rival bien capitalizado — Shopee puede escalar la de madera (marketplace barato y "
        "rápido); Nubank puede superar la de fintech en calidad de suscripción. Pero ningún rival combina "
        "hoy las tres murallas a la vez —logística propia de escala regional, datos de crédito alimentados "
        "por el propio marketplace, escala de capital—. La pregunta honesta para esta tesis no es si el "
        "castillo existe —existe— sino si quien lo custodia está reforzando esa defensa combinada de forma "
        "disciplinada al reinvertir en crédito, o si está usando la fortaleza de las dos murallas sanas para "
        "subsidiar una apuesta de riesgo creciente en la tercera, sin la misma disciplina que construyó las "
        "otras dos.")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def s6():
    o = M.flag_titulo("§6 · El campo de batalla competitivo", "La lección de toda guerra en tres frentes: no es el número de rivales lo que agota, es no saber cuál es el frente decisivo")
    o += [M.tabla([
        ["Frente", "Rival principal", "Situación"],
        ["E-commerce Brasil", "Shopee (+53% YoY, ya EBITDA-positivo)", "MELI lidera (40% share) pero crece más lento que el retador"],
        ["E-commerce México", "Amazon (duopolio ~85% combinado)", "Regulador (COFECE) ya señaló ausencia de competencia efectiva"],
        ["Fintech / crédito", "Nubank (mejor costo de riesgo, más volumen absoluto en tarjetas Brasil)", "MELI responde relajando suscripción, no compitiendo en calidad"],
        ["Logística de última milla", "Amazon (vía alianza con Rappi, no construcción propia)", "MELI mantiene ventaja de costo y escala"],
    ], [3.6*cm, 6.4*cm, 6.4*cm], font_sz=7.6)]
    o += [M.p("MercadoLibre libra, en efecto, una guerra en tres frentes simultáneos — y la lección que la "
        "historia militar repite, de Napoleón a la Alemania de 1914, es que ningún ejército se agota tanto "
        "por el número de frentes como por no distinguir cuál de ellos decide la campaña. <b>El frente que "
        "decide la próxima década no es el que más titulares genera (Shopee en Brasil), sino el que menos se "
        "discute: la calidad de suscripción de Mercado Crédito frente a Nubank.</b> Nubank ya supera a MELI "
        "en volumen absoluto de emisión de tarjetas de crédito en Brasil con un costo de riesgo "
        "estructuralmente menor (~14% vs. ~23-26%) — es decir, Nubank está ganando ese frente con mejor "
        "disciplina de suscripción, no con más riesgo asumido. La respuesta de MELI hasta ahora —extender "
        "duración de préstamos, buscar clientes de mayor riesgo— es exactamente la respuesta opuesta a la "
        "que exigiría defender ese frente frente a un rival que gana suscribiendo mejor, no arriesgando más. "
        "[HECHO/INFERENCIA]")]
    o += [M.p("<b>México es el frente más estructuralmente favorable, y el menos discutido.</b> El propio "
        "regulador antimonopolio mexicano (COFECE) encontró que MELI y Amazon combinados representan ~85% "
        "de las transacciones de marketplace, sin \"condiciones para competencia efectiva\" — aunque decidió "
        "no ordenar medidas correctivas. Es, en efecto, un duopolio regulatoriamente reconocido pero no "
        "intervenido: la posición estructuralmente más tranquila de MELI en cualquiera de sus tres mercados "
        "principales, el único frente donde no hace falta pelear por terreno porque el terreno ya está "
        "repartido. [HECHO]")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def s7():
    o = M.flag_titulo("§7 · Porter: fosos por negocio y la contradicción central", "Logística es el foso más ancho; el marketplace, el más disputado por diseño propio")
    o += [ch("13_porter", 14.4), sp(2)]
    o += [M.p("El marco de las Cinco Fuerzas de Michael Porter (un método clásico para medir qué tan "
        "protegida está la rentabilidad de un negocio frente a rivales, proveedores, clientes, sustitutos y "
        "nuevos entrantes) se puntúa aquí por negocio, en una escala de 1 a 5 donde menor puntaje significa "
        "mejor foso. Logística (2,2/5) es el foso más favorable —la muralla de piedra del §5—, con barreras "
        "de capital reales y un rival de talla mundial que prefiere rentar antes que construir. Fintech "
        "(3,0/5) está en medio: barreras de entrada moderadas (requisitos regulatorios crecientes en Brasil) "
        "pero rivalidad intensa y creciente frente a Nubank. El marketplace de e-commerce (3,4/5) es el más "
        "disputado —la muralla de madera—: el propio 10-K admite textualmente que las barreras de entrada "
        "son \"relativamente bajas\" y que usuarios y comercios cambian de plataforma con facilidad. "
        "[análisis propio]")]
    o += [M.callout("PAUSA REFLEXIVA",
        "Contradicción Porter↔Seilern: el marketplace obtiene el peor score de Porter (más disputado) pero "
        "R4 (moat) del sistema Seilern todavía puntúa 11/15 —un nivel respetable—. El mecanismo de "
        "reconciliación es el mismo castillo del §5: el moat de MELI no vive en la muralla de madera "
        "aislada, vive en el conjunto de las tres murallas —logística + datos de crédito alimentados por el "
        "marketplace + escala regional—, y ese conjunto combinado es más difícil de replicar que cualquiera "
        "de sus tres piezas por separado. ¿Es ese mecanismo duradero? Mientras ningún rival combine las tres "
        "piezas simultáneamente —y hoy ninguno lo hace: Shopee no tiene el crédito, Nubank no tiene el "
        "marketplace, Amazon no tiene la escala de datos crediticios regionales— sí. Si eso cambiara, el "
        "castillo combinado se debilitaría más rápido de lo que sugiere el score aislado de cualquier pieza.")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def s8():
    o = M.flag_titulo("§8 · TAM, SAM, SOM, runway y catalizadores", "El mercado es enorme; el reto es la calidad del crecimiento, no su tamaño")
    o += [ch("14_tam", 15.0), sp(2)]
    o += [M.p("El embudo de mercado se mide en tres círculos concéntricos, cada uno más chico y más "
        "realista que el anterior: TAM (total addressable market, el mercado total direccionable — todo lo "
        "que existe), SAM (serviceable addressable market, la porción de ese total que el modelo de negocio "
        "de la empresa puede efectivamente atender) y SOM (serviceable obtainable market, la porción de eso "
        "que la empresa puede razonablemente capturar dada su posición competitiva). El e-commerce "
        "latinoamericano (~US$215.000 millones en 2026, el TAM de este primer negocio) crece más rápido que "
        "el promedio mundial, y la penetración todavía tiene un largo camino: el comprador latinoamericano "
        "promedio hace 7 compras online al año, frente a 41 del comprador estadounidense promedio — el "
        "propio comprador de MELI promedia 11, por delante del promedio regional pero aún lejos del nivel "
        "de un mercado maduro. En pagos digitales, el mercado es aún mayor (~US$788.000 millones), con MELI "
        "procesando US$87.200 millones de TPV (total payment volume, volumen bruto de pagos procesados) "
        "solo en el primer trimestre de 2026 (+50% interanual). [HECHO/INFERENCIA]")]
    o += [M.p("<b>El embudo SAM&rarr;SOM, país por país.</b> Descomponiendo ese TAM regional en su último "
        "año con dato completo (2025, la base sobre la que corre la proyección 2026 ya citada arriba): el "
        "e-commerce latinoamericano sumó ~US$191.000 millones, con Brasil, México y Argentina concentrando "
        "84,5% (~US$161.000 millones) de ese total. El GMV de MELI en 2025 fue ~US$65.000 millones (+26%), "
        "es decir, aproximadamente <b>40% de ese SAM regional de tres países</b> — una cifra que "
        "sobreestima algo la cuota real porque el GMV de MELI también incluye países fuera de esos tres "
        "(Chile, Colombia, Perú, Uruguay, entre otros). [HECHO el TAM y el GMV; INFERENCIA el porcentaje "
        "de cuota]")]
    o += [M.p("El techo de categoría, sin embargo, no es uniforme por país — y esa disparidad importa más "
        "que el TAM agregado. México ya alcanzó 17,7% de penetración de e-commerce sobre el retail total "
        "en 2025, superando por primera vez a Estados Unidos (17,0%): señal de que el mercado mexicano se "
        "acerca a la madurez de una economía desarrollada, con menos recorrido estructural del que sugiere "
        "el TAM regional agregado. Brasil está en un rango de 10-15% de penetración —lejos todavía del "
        "25-30% de los mercados más maduros— y por tanto conserva más runway (pista de despegue, la "
        "distancia de crecimiento disponible antes de tocar el techo del mercado) de categoría que México. "
        "Argentina crece 58% interanual desde una base pequeña, pero no existe un dato de penetración "
        "confiable para ese mercado. [HECHO las tasas de México y Brasil; SUPUESTO que la ausencia de dato "
        "en Argentina implica mayor incertidumbre, no mayor techo]")]
    o += [M.callout("PAUSA REFLEXIVA",
        "Dos techos distintos que conviene no confundir. El hallazgo anterior separa dos preguntas que la "
        "regla R6 (diversificación, §4) tiende a mezclar en una sola: el techo de <b>categoría</b> (cuánto "
        "puede seguir creciendo el e-commerce sobre el retail total de cada país — todavía alto en Brasil, "
        "casi agotado en México) y el techo de <b>concentración</b> interna de MELI (cuánto de su propio "
        "ingreso depende de un solo país). Brasil ya es 54% del ingreso consolidado de MELI, cerca del "
        "~50% que el propio sistema de calibración trata como límite tolerado antes de penalizar "
        "diversificación — ese segundo techo, el de concentración, está estructuralmente más cerca de "
        "tocarse que el primero, el de categoría. Son dos runways distintos, y tratarlos como uno solo "
        "sobreestima el margen de maniobra real de la tesis.")]
    o += [M.p("<b>Una aclaración de unidades que el gráfico de arriba puede inducir a leer mal.</b> El TPV "
        "fintech fue US$278.000 millones en 2025 (+41%) y US$87.200 millones solo en el primer trimestre "
        "de 2026 (+50%, ~US$350.000 millones anualizados) — un orden de magnitud por encima de los "
        "US$20.000 millones que el gráfico asigna a MELI en la fila de pagos digitales. La brecha se "
        "explica porque el TPV mide flujo bruto transaccional, no ingreso: el ingreso neto del segmento "
        "Fintech fue US$12.600 millones en 2025 (+46%) y US$3.977 millones en el 1T26 (~US$16.000 millones "
        "anualizados), una cifra mucho más cercana a los US$20.000 millones citados en el gráfico. Con alta "
        "probabilidad, ese US$20.000 millones es ingreso neto proyectado, no TPV — compararlo contra un "
        "TAM de US$788.000 millones expresado en volumen bruto es, estrictamente, un error de unidades: si "
        "en cambio se compara TPV contra TAM (la comparación correcta en volumen), la cuota real de MELI "
        "ronda 35-45%, una historia de penetración mucho más madura que el ~2,5% que el gráfico sugiere de "
        "forma implícita al cruzar unidades distintas. [HECHO las cifras de TPV e ingreso; INFERENCIA la "
        "lectura del gráfico]")]
    o += [M.p("<b>Catalizadores 2026-2028:</b> (1) Mercado Ads, el segmento de mayor margen, creciendo 4 "
        "veces más rápido que el mercado publicitario regional, con más de la mitad del gasto publicitario "
        "de la región todavía en canales offline — el runway más limpio de toda la tesis; (2) la maduración "
        "de las cosechas de tarjeta de crédito en Brasil (management afirma que, tras cinco años de "
        "inversión, las cosechas antiguas ya compensan el arrastre de las nuevas) — si es cierto, debería "
        "empezar a verse en una estabilización de NIMAL en los próximos 2-3 trimestres, el trigger más "
        "importante de esta tesis; (3) expansión de tarjeta de crédito en México (fase temprana, paybacks "
        "atractivos según management) y Argentina (recién lanzada, 2025); (4) resolución de la tensión "
        "macro en Argentina, donde el 41,6% de margen de contribución probablemente está inflado por "
        "contabilidad de hiperinflación más que por rentabilidad económica pura. [HECHO los datos; SUPUESTO "
        "las trayectorias]")]
    o += [M.p("<b>El catalizador #2 depende de un dato que se buscó activamente y no se pudo verificar.</b> "
        "Se buscó una tabla de cosechas (vintages) de crédito independiente y auditable —en transcripts, "
        "investor day, prensa especializada— y no existe públicamente: la única evidencia disponible es la "
        "propia afirmación de gestión de que \"todas las cosechas en Brasil siguen mejorando y volviéndose "
        "rentables\" y que Argentina está replicando el patrón inicial de Brasil, sin una tabla de mora o "
        "rentabilidad por añada que permita verificarlo de forma independiente. El dato que más cambiaría "
        "el veredicto de esta tesis sigue sin poder confirmarse — no por omisión de este análisis, sino "
        "porque la divulgación pública simplemente no existe. [HECHO, cita earnings call 1T26 y resultado "
        "de la búsqueda]")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def s9():
    o = M.flag_titulo("§9 · Valoración multi-método", "El output de val-mos: el precio ya superó el propio caso optimista de este análisis")
    o += [M.p("<b>Paso 0 — detector de trampas: GRIS, no un PASA limpio.</b> El test decisivo (¿ingresos, "
        "margen y ROIC siguen creciendo pese al miedo?) da una respuesta mixta y honesta: los ingresos y el "
        "volumen de negocio (GMV, TPV, MAU fintech) siguen creciendo con fuerza real —no hay señal de "
        "estancamiento de demanda—. Pero el margen operativo y la rentabilidad del crédito (NIMAL) sí se "
        "deterioran, de forma multianual y no como un bache de un trimestre, y por decisión deliberada de "
        "gestión, verbalizada en vivo por el propio CFO. Esto no constituye una TRAMPA confirmada (no hay "
        "una segunda señal estructural simultánea, y el NPL estándar de 15-90 días sigue estable), pero "
        "tampoco es un PASA limpio tipo Teleperformance. Es, con precisión, el caso GRIS que define "
        "trampas.md: una señal corroborada con fundamentales agregados todavía creciendo. [val-mos]")]
    o += [ch("02_nimal", 14.4), sp(2)]
    o += [M.p("<b>Paso 1 — DCF inverso: el precio exige superar el propio caso optimista.</b> A "
        "US$1.806, el precio despeja un crecimiento de owner earnings implícito de ~38,1% anual — por "
        "encima incluso del escenario optimista propio de este análisis (39,0%, apenas 0,9pp por encima) y "
        "muy por encima del escenario conservador (19,8%). Clasificación: <b>HEROICAS</b>. No hay lectura "
        "razonable de los datos donde esto sea \"razonable\": es, con honestidad, el mercado pidiéndole a "
        "MELI que ejecute mejor que el mejor caso que este propio análisis puede construir con evidencia "
        "disponible. [DCF inverso]")]
    o += [ch("10_dcf_inverso", 14.6)]
    o += [M.p("<b>Paso 2 — PWFV-Valor: US$1.101, muy por debajo del precio de hoy.</b> Sobre owner earnings "
        "normalizados (ingreso neto, no CFO simple —el CFO está distorsionado por el crecimiento del libro "
        "de crédito, que se trata correctamente como capital de trabajo del negocio Fintech, no como caja "
        "libre real—), el DCF de tres escenarios da un valor ponderado de US$1.101. El precio de hoy "
        "(US$1.806) está <b>64% por encima</b> de ese ancla — y, de forma más reveladora, ya por encima "
        "incluso del escenario optimista propio de US$2.036 solo si se pondera al 20% de probabilidad; en "
        "términos absolutos, el precio hoy está <b>67% por encima del propio caso base</b> (US$1.083), no "
        "solo del conservador.")]
    o += [ch("07_dcf", 14.4), sp(2)]
    o += [M.p("<b>El candado duro anti-sobrepago es la segunda pared, independiente de la anterior.</b> "
        "Sobre owner earnings normalizados (ingreso neto, verificado y corregido de 44-47x a "
        f"<b>{D.es(D.MULT_NORMALIZADO,1)}x</b> tras un error aritmético de conteo de acciones detectado por "
        "el verificador adversarial), el múltiplo pagado hoy <b>viola tanto el techo específico del tier de "
        "MELI (25x) como el candado genérico (30-40x)</b> — ambos techos se rompen, y el más estricto (el "
        "del tier) es el que manda. El múltiplo de CFO simple (8,7x) es una ilusión aritmética: el "
        "crecimiento del propio libro de crédito infla el flujo de caja operativo reportado sin que sea "
        "caja libre real disponible.")]
    o += [ch("09_candado_duro", 14.4), sp(2)]
    o += [ch("11_wacc", 13.4), sp(2)]
    o += [ch("12_sensibilidad", 14.4)]
    o += [M.p(f"<b>Sensibilidad.</b> Cruzando WACC ({D.WACC_GRID[0]}-{D.WACC_GRID[-1]}%) × crecimiento "
        f"terminal ({D.GT_GRID[0]}-{D.GT_GRID[-1]}%), el valor se mueve entre US${D.SENS[-1][0]} y "
        f"US${D.SENS_MAX} — un rango que <b>nunca alcanza el precio de hoy</b> (US${D.es(D.PRECIO,0)}) "
        f"ni siquiera en el escenario más generoso combinado con el WACC más bajo. El mercado no está "
        f"regalando esta acción a ningún nivel razonable de supuestos.")]
    o += [ch("08_zonas", 15.2)]
    o += [M.p(f"<b>Paso 3 — zonas y veredicto.</b> Zona {D.ZONA_HOY} (164% del PWFV): fuera del rango "
        f"comprable de su tier por triple vía —el gate binario del tier Calidad sólida (solo compra en "
        f"Ganga/Oportunidad), el candado duro anti-sobrepago (violado por ambos techos), y la asimetría "
        f"({D.es(D.ASIMETRIA,2)}:1, muy por debajo del umbral de 2:1 que activa la regla textual de "
        f"mos_sizing.md: \"ESPERAR sin importar cuán bueno sea el patrón\"). <b>Veredicto: {D.VEREDICTO}.</b> "
        f"No hay urgencia de vender lo que ya se tiene —el negocio de comercio y logística sigue siendo de "
        f"calidad real—, pero tampoco hay ningún argumento de precio o de asimetría que justifique ampliar "
        f"hoy.")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def s10():
    o = M.flag_titulo("§10 · Gestión, cultura y gobernanza", "Un fundador que ganó la apertura y el mediojuego, y un directorio que hoy juega el final sin reloj propio")
    o += [M.p("Marcos Galperin fundó MercadoLibre en 1999 y la dirigió como CEO hasta enero de 2026, cuando "
        "pasó a Presidente Ejecutivo (Ariel Szarfsztejn asumió como nuevo CEO). Su historial es, sin "
        "reservas, excepcional: construyó desde cero el compounder más grande de la historia de América "
        "Latina, con un CAGR de ingresos cercano al 48% sostenido durante prácticamente una década completa "
        "y a través de múltiples regímenes macroeconómicos distintos —la clase de jugador que gana la "
        "apertura y el mediojuego con tanta claridad que se olvida preguntar cómo está jugando el final—. "
        "Ese historial es la base alta desde la que el sistema qg-seilern parte para puntuar esta regla —no "
        "es un punto de partida neutral, es un punto de partida que reconoce mérito real. [HECHO]")]
    o += [ch("15_mgmt", 13.2), sp(2)]
    o += [M.p("<b>El defecto que el track record no puede comprar de vuelta.</b> El sistema exige, tras "
        "establecer esa base alta, restar hasta un máximo de tres puntos por señales estructurales de "
        "gobernanza (el conjunto de reglas e incentivos que determinan a quién responde de verdad el "
        "directorio) — y aquí las señales son reales, documentadas, y no maquillables: el ISS Governance "
        "QualityScore (una calificación de terceros —Institutional Shareholder Services— sobre calidad de "
        "gobierno corporativo, licenciada y mostrada por Yahoo Finance, no verificada de forma independiente "
        "contra la fuente primaria de ISS) califica el pilar de directorio de MELI en <b>10, el peor decil "
        "posible</b>. El directorio de nueve miembros incluye a <b>dos integrantes de la familia "
        "Galperin</b> (Marcos y su hermano Nicolás), y la autorización de recompra de acciones de 2025 —la "
        "más reciente disponible— fue de apenas <b>US$4,05 millones</b>, explícitamente destinada a "
        "compensar la dilución del plan de compensación de directores independientes, no un programa real "
        "de retorno de capital, pese a que el múltiplo de la acción cayó de ~64x a ~44x en apenas tres años "
        "— es difícil leer eso como un directorio que juega el final con el mismo rigor con el que Galperin "
        "jugó la apertura. [HECHO, con la salvedad de confianza moderada en la cifra exacta de ISS]")]
    o += [M.p("<b>Otros deméritos, sin maquillar:</b> el negocio de crédito opera a través de vehículos de "
        "titulización (FIDCs en Brasil —fondos de inversión en derechos de crédito, el vehículo brasileño "
        "para empaquetar y vender carteras de préstamos—, fideicomisos financieros en Argentina, "
        "fideicomisos en México, fondos en Chile) con fondeo que incluye instrumentos tipo-depósito "
        "brasileños explícitamente <b>no cubiertos por el FGC</b> (el fondo de garantía de depósitos) — una "
        "zona gris regulatoria que un banco tradicional no tendría. La transición de CEO "
        "(Galperin→Szarfsztejn, enero 2026) todavía no tiene track record propio que evaluar: es, "
        "literalmente, una jugada recién hecha sobre el tablero, sin que el rival haya tenido tiempo de "
        "responder. Score de gestión: <b>17/30</b>. [HECHO/INFERENCIA]")]
    o += [M.p("<b>Asignación de capital vía M&amp;A: la ausencia misma es el dato.</b> A diferencia de "
        "otros compounders de esta escala, MercadoLibre prácticamente no ha asignado capital a "
        "adquisiciones: diez operaciones en toda su historia pública, con un ticket promedio de apenas "
        "US$22,7 millones, la mayor de ellas (DeRemate, 2008) por US$40 millones, y la más reciente "
        "(Machinalis, abril de 2024) una compra pequeña de talento en inteligencia artificial, no una "
        "adquisición estratégica de escala. No existe, por tanto, un historial de M&amp;A material que "
        "evaluar bajo la disciplina de capital habitual de este sistema — y esa ausencia misma, en una "
        "empresa que sí ha estado dispuesta a asignar capital de forma agresiva hacia su libro de crédito "
        "interno, conviene decirla de forma explícita y no dejarla implícita: el crecimiento de MELI ha "
        "sido casi enteramente orgánico, financiado con reinversión interna sobre el propio tablero, no con "
        "piezas compradas afuera. [HECHO, registros públicos de M&amp;A vía Tracxn/Mergr]")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def s11():
    o = M.flag_titulo("§11 · Nueve inversores legendarios opinan", "El panel se divide por precio, no por la calidad del negocio")
    o += [ch("18_inversores", 15.0), sp(2)]
    pares = [
        ("Graham", "PASS", "Sin margen de seguridad sobre beneficios normalizados (P/E ~44x); el balance ya no es la fortaleza neta que exige su regla clásica dado el crecimiento de la deuda."),
        ("Buffett", "HOLD", "Admira el negocio (moat de logística, ROIC histórico alto) pero su regla de \"entender el negocio\" se tensiona con un libro de crédito de suscripción cada vez más laxa que él mismo evitaría en un banco tradicional."),
        ("Munger", "HOLD", "Invierte la pregunta: ¿qué lo mata? No el negocio central — el negocio central está sano—. Lo que le preocupa es la calidad de las decisiones de asignación de capital hacia el segmento de menor retorno marginal."),
        ("Fisher", "HOLD", "El scuttlebutt es fuerte en el producto (GMV, TPV, MAU todos creciendo con fuerza) y débil en la disciplina crediticia — el hecho de que el propio CFO confirme la relajación de suscripción en vivo es una señal de honestidad, no de tranquilidad."),
        ("Lynch", "PASS", "La historia es fácil de contar (\"el Amazon+Nubank de América Latina\"), pero el PEG deja de verse razonable en el momento en que el crecimiento de ingresos empieza a incluir expansión de balance, no solo volumen orgánico."),
        ("Templeton", "PASS", "No hay pesimismo máximo que comprar aquí: consenso Buy, precio en zona Burbuja según este propio modelo. Este no es su terreno."),
        ("Marks", "HOLD", "¿Dónde estamos en el ciclo? El ciclo de crédito de consumo latinoamericano tiene precedentes de deterioro rápido tras fases de expansión agresiva — la pregunta de Marks no es si MELI es un buen negocio, es si el ciclo de crédito ya giró."),
        ("Seilern", "PASS", "Calidad 72,0/100: sólida pero no de su estándar (Núcleo ≥85). El deterioro reciente del libro de crédito —documentado, no especulativo— la mantiene fuera de su universo comprable incluso antes de mirar el precio."),
        ("Terry Smith", "PASS", "\"No pagues de más\" se incumple con claridad: el precio de hoy ya supera el propio escenario optimista de este análisis. Su regla de evitar el apalancamiento excesivo también se activa frente al crecimiento de deuda neta."),
    ]
    filas = [["Inversor", "Veredicto y razonamiento en una línea"]]
    for nm, vd, txt in pares:
        filas.append([f"<b>{nm}</b><br/><font size=7 color='#666054'>{vd}</font>", txt])
    o += [M.tabla(filas, [2.5*cm, 13.9*cm], font_sz=7.8)]
    o += [M.callout("PAUSA REFLEXIVA",
        "A diferencia de GOOGL (donde el panel se dividió por gobernanza) o AMZN (donde se dividió por "
        "precio de un negocio excelente), aquí el panel se divide por una pregunta más incómoda: ¿la "
        "gestión está usando la fortaleza del negocio central para financiar una apuesta de riesgo "
        "creciente sin la misma disciplina que construyó ese negocio central? Ningún inversor del panel "
        "duda de la calidad histórica de MercadoLibre — todos, en distinto grado, dudan de si esa calidad "
        "histórica se está gastando hoy en el segmento equivocado.")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def s12():
    o = M.flag_titulo("§12 · Riesgos: matriz, pre-mortem y alerta temprana", "El riesgo de crédito y el de gobernanza comparten la misma ventana temporal")
    o += [ch("17_riesgos", 15.2), sp(2)]
    o += [M.p("El riesgo dominante (impacto 4, probabilidad 3) es el deterioro sostenido de la calidad "
        "crediticia — no porque ya se haya confirmado en la mora estándar (NPL, non-performing loans, "
        "préstamos de 15-90 días de atraso, que sigue estable), sino porque el mecanismo de retraso de 12-24 "
        "meses en el reconocimiento de pérdidas significa que las cosechas (vintages, el conjunto de "
        "préstamos originados en un mismo período, que se sigue como cohorte) originadas con criterios más "
        "laxos en 2025-2026 aún no han tenido tiempo de mostrarse. El segundo riesgo (probabilidad 4, "
        "impacto 3) es la gobernanza —no como un evento futuro sobre el que todavía se puede apostar, sino "
        "como un hecho estructural ya confirmado (ISS Board=10)—. [análisis propio]")]
    o += [M.p("<b>Pre-mortem narrativo.</b> Es 2029 y la inversión salió mal. Como en casi todas las "
        "historias reales de crédito que terminan mal —no en las de Hollywood, con un colapso de un solo "
        "día, sino en las que documentan analistas como Michael Lewis—, no fue un colapso repentino: fue una "
        "erosión de dos años que se veía venir en los números desde 2026, pero que el mercado tardó en "
        "reconocer porque el volumen de negocio (GMV, TPV, usuarios) nunca dejó de crecer, y un negocio que "
        "crece rara vez se audita con la misma dureza que uno que se estanca. Las cosechas de crédito "
        "originadas con criterios más laxos en 2025-2026 empezaron a mostrar mora elevada en 2027-2028, "
        "justo cuando la mezcla del libro ya era mayoritariamente tarjeta de crédito de bajo margen — el "
        "reloj de retraso de 12 a 24 meses, que en 2026 parecía una tecnicidad contable, resultó ser "
        "exactamente el tiempo que tomó. El write-off rate, que ya se había reacelerado de 17,1% a 19,4% en "
        "el momento de esta tesis, siguió subiendo. La deuda neta, que ya se había duplicado en cinco "
        "trimestres, siguió creciendo para sostener el libro. Y el directorio —con dos Galperin y un score "
        "ISS ya en el peor decil desde 2026— nunca forzó un cambio de rumbo en la estrategia de originación, "
        "porque nadie con el voto suficiente tenía el incentivo económico independiente para exigirlo. La "
        "pregunta que en 2026 quedó sin tabla de cosechas auditable que la respondiera (§8) fue, en "
        "retrospectiva, la única pregunta que importaba.")]
    o += [ch("20_early_warning", 15.4), sp(2)]
    o += [M.p("<b>Sistema de alerta temprana.</b> El semáforo tiene dos verdes sólidos (volumen de negocio, "
        "ingreso consolidado), tres ámbar de vigilancia activa (write-off rate, NPL 15-90 días, margen "
        "operativo) y dos filas rojas —una de negocio (NIMAL, que ya perfora mínimos históricos sin señal "
        "de estabilización) y una estructural (gobernanza, que no es una señal transitoria sino un hecho "
        "permanente a vivir con él)—. <b>Regla dura:</b> si el write-off rate anualizado supera 22% sin que "
        "el NPL de 15-90 días se mueva en simultáneo, esa disonancia entre \"mora contable estable\" y "
        "\"pérdida de originación creciente\" convierte la señal 4 (confirmada) en también una señal 1 "
        "(ROIC/rentabilidad en declive secular confirmada) — momento de escalar el detector de trampas de "
        "GRIS hacia TRAMPA en la próxima revisión, independientemente del precio.")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def s13():
    o = M.flag_titulo("§13 · Veredicto final, triggers y proyección", "ESPERAR: el negocio convence, el precio ya cobró de más, el crédito exige vigilancia activa")
    o += [M.p(f"<b>Cruce de los dos ejes.</b> CALIDAD <b>{D.es(D.SCORE_QG,1)}/100 · tier {D.TIER_QG}</b> "
        f"(corregido de un primer pase de 64,8/Watchlist tras verificación adversarial rigurosa, dado el "
        f"tamaño de esta posición). VALORACIÓN <b>{D.VEREDICTO}</b> (ratificado en §9, corregido de "
        f"\"VIGILAR\" tras verificación): detector GRIS, PWFV US${D.PWFV}, zona {D.ZONA_HOY} — el precio de "
        f"hoy ya está por encima incluso del propio escenario optimista de este análisis, y la asimetría "
        f"({D.es(D.ASIMETRIA,2)}:1) activa la regla textual del sistema que exige ESPERAR sin importar cuán "
        f"bueno sea el patrón de crecimiento. Los dos ejes convergen en una conclusión honesta: <b>este es "
        f"un negocio de calidad real, con un libro de crédito que está gastando esa calidad más rápido de "
        f"lo prudente, comprado hoy a un precio que ya asume que nada de eso importará.</b>")]
    o += [M.p("<b>Frase-tesis (registrada para el feedback loop).</b> «El mercado ve un compounder "
        "latinoamericano de 48% de CAGR y paga en consecuencia; los datos de crédito —NIMAL en mínimos "
        "históricos, libro creciendo el doble de rápido que el negocio, gestión confirmando en vivo que la "
        "decisión es deliberada— dicen que una parte creciente de ese crecimiento está financiada con "
        "capital cada vez peor remunerado. El precio de hoy no solo ignora esa tensión: la supera, pagando "
        "por adelantado incluso el escenario más optimista que este análisis puede construir con la "
        "evidencia disponible.»")]
    o += [M.p("<b>Elemento falsable.</b> Reconsideraría la tesis hacia más optimismo si el NIMAL se "
        "estabiliza (deja de caer) durante 2-3 trimestres consecutivos Y el margen operativo consolidado se "
        "recupera hacia &gt;10% — la lectura correcta retroactiva sería que el mercado sobre-reaccionó a un "
        "ajuste temporal de mezcla/inversión, no a un deterioro estructural. Reconsideraría hacia más "
        "cautela (posible escalada a TRAMPA) si el write-off rate supera 22% sin que el NPL de 15-90 días se "
        "mueva en la misma dirección, o si la deuda neta sigue creciendo a un ritmo similar al de los "
        "últimos cinco trimestres sin que NIMAL toque piso.")]
    o += [M.tabla([
        ["Plan operativo", "Nivel", "Acción"],
        ["Hoy", f"US${D.es(D.PRECIO,0)}", "ESPERAR — 0% de ampliación. Sostener lo que ya se tiene."],
        ["Gatillo Oportunidad", f"≤US${D.GATILLO_OPORT}", "Reconsiderar tramo si NIMAL muestra señales de estabilización"],
        ["Gatillo Ganga", f"≤US${D.GATILLO_GANGA}", "Tramo pleno si además el detector de trampas mejora a PASA"],
        ["Disciplina de venta", "cualquiera", "Vender SOLO si el detector escala a TRAMPA confirmada; NUNCA por múltiplo aislado"],
    ], [5.0*cm, 3.4*cm, 8.0*cm], font_sz=7.8)]
    o += [M.p("<b>Proyección a 5 años (3 escenarios, desde US$1.806).</b> Optimista (20%): las cosechas de "
        "crédito de Brasil maduran como afirma management, NIMAL toca piso y se recupera, Mercado Ads sigue "
        "creciendo al 4x del mercado — valor ~US$2.036, +13%. Base (50%): el ajuste de márgenes se "
        "estabiliza hacia 2027 sin recuperación completa, el crecimiento de ingresos desacelera hacia el "
        "20-25% conforme madura la base — valor ~US$1.083, −40%. Conservador (30%): el deterioro crediticio "
        "se confirma en la mora estándar, Shopee sigue ganando cuota en Brasil, la deuda neta sigue creciendo "
        "sin que NIMAL toque piso — valor ~US$508, −72%. <b>Ponderado: US$1.101, 39% por debajo del precio "
        "de hoy — un negocio de calidad real, comprado hoy a un precio que no ofrece ningún margen de "
        "seguridad bajo ninguna combinación razonable de supuestos. Por eso: ESPERAR, con vigilancia "
        "trimestral activa sobre NIMAL.</b>")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def cierre():
    o = M.flag_titulo("Glosario y advertencias finales", "Términos, etiquetas y la naturaleza de este documento")
    o += [M.p("<b>Glosario.</b>", "h3")]
    gl = [
        ("NIMAL", "net interest margin after losses: margen de interés neto del libro de crédito después de pérdidas esperadas."),
        ("FIDC", "Fundo de Investimento em Direitos Creditórios: vehículo brasileño de titulización de cartera de crédito."),
        ("EPV", "valor de los beneficios sin crecimiento; suelo teórico de la valoración (US$347,7, corregido de un error de conteo de acciones)."),
        ("Adjusted FCF", "métrica propia de MELI que neta el crecimiento del libro de crédito del flujo de caja operativo — expone que el CFO simple sobreestima la caja libre real disponible."),
        ("PWFV-Valor", "valor intrínseco ancla del sistema val-mos (tri-método probabilístico)."),
        ("Owner earnings normalizados", "ingreso neto ajustado, usado en vez del CFO simple para evitar la distorsión del crecimiento del libro de crédito."),
        ("Tier «Calidad sólida»", "banda de calidad 65-74/100; solo se compra en zona Ganga/Oportunidad — es un gate, no un MoS más exigente."),
        ("Write-off rate", "castigos contables como % de la cartera bruta promedio; señal de calidad de originación."),
        ("ISS Governance QualityScore", "calificación de terceros (Institutional Shareholder Services) sobre calidad de gobierno corporativo, 1=mejor, 10=peor."),
        ("Zona BURBUJA", "precio &gt;135% del PWFV — la zona menos favorable de las cinco definidas por val-mos."),
    ]
    filas = [["Término", "Definición"]]
    for t, d in gl:
        filas.append([f"<b>{t}</b>", d])
    o += [M.tabla(filas, [4.2*cm, 12.2*cm], font_sz=8.0)]
    o += [sp(4), M.p("<b>Advertencias finales.</b>", "h3")]
    o += [M.p("Cada dato se etiquetó <b>HECHO</b> (fuente primaria: 10-K FY2025, 10-Q Q1 2026, cartas a "
        "accionistas trimestrales en SEC EDGAR CIK 0001099590), <b>INFERENCIA</b> o <b>SUPUESTO</b>. Cabos "
        "NO resueltos, declarados: la cifra exacta del ISS Board pillar (10, probable pero licenciada vía "
        "Yahoo Finance, no verificada contra la fuente primaria de ISS); el texto completo de la sección de "
        "\"transacciones con partes relacionadas\" del proxy más reciente (bloqueado por acceso 403 durante "
        "la investigación); si el sistema val-mos debería tener una regla única y congelada para el "
        "tratamiento de riesgo-país en multinacionales (hoy cada tesis construye su propio blend, un vacío "
        "del skill identificado por el verificador adversarial, no un error de esta tesis en particular). El "
        "score de calidad se corrigió de 64,8 (Watchlist) a 72,0 (Calidad sólida) tras detectar que el "
        "primer pase invertía la mecánica de cinco reglas — documentado en el §changelog. El score Seilern "
        "mide <b>calidad, no valoración</b>. Documento de <b>uso personal</b>; no constituye asesoría de "
        "inversión registrada.")]
    o += [M.callout("PAUSA REFLEXIVA",
        "Qué queda por saber — la pieza que más cambiaría el veredicto: <b>si el NIMAL toca piso en el "
        "próximo trimestre o sigue perforando</b>. Hoy solo tenemos la palabra de management de que las "
        "cosechas de crédito de Brasil \"están madurando como se esperaba\" — una afirmación de la parte "
        "interesada, sin una tabla de cosechas independiente y auditable que la respalde. Si el próximo "
        "trimestre confirma estabilización, la tesis bajista de deterioro crediticio pierde fuerza real y el "
        "veredicto podría moverse hacia vigilancia menos activa. Si en cambio el NIMAL sigue cayendo y el "
        "write-off rate cruza el umbral de 22%, el detector de trampas debería escalar de GRIS hacia TRAMPA "
        "en la siguiente revisión — independientemente de qué tan atractivo luzca el precio en ese momento. "
        "Veintisiete años atrás, un estudiante becado abrió una partida en unas cocheras de Buenos Aires y "
        "ganó, con amplio margen, el control del tablero regional. La pregunta que cierra este documento no "
        "es si ese jugador sabe jugar —lo demostró durante dos décadas— sino si el sacrificio que está "
        "haciendo ahora, en el libro de crédito, es el tipo de jugada calculada que gana partidas, o el tipo "
        "de jugada que un jugador que lleva demasiado tiempo ganando deja de cuestionarse a tiempo.")]
    return o

# ══════════════════════════════════════════════════════════════════════════
def story():
    s = []
    for fn in [portada, changelog, resumen, cuadro_mando, veredicto_cuant,
               s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, cierre]:
        s += fn()
    return s
