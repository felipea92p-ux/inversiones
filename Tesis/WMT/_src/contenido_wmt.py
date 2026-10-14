# -*- coding: utf-8 -*-
"""CONTENIDO · Tesis Ultra QG — Walmart Inc. (WMT).
Fuente única de todo el análisis: Tesis/WMT/2026-09-12_UltraTesis_WMT_metodo12_borrador.md
(método de 12 pasos "Comprensión Primero con candado adversarial"). Cero recálculo aquí,
solo maquetación. Separación estricta contenido/diseño: cero import de estilos ad-hoc
salvo los dos centrados de portada."""
import motor_qg as M
from reportlab.platypus import Spacer, PageBreak, NextPageTemplate, Image, Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import cm
from paleta_qg import PALETA as P

CM = 1 * cm
COLW_FULL = [8.5 * cm, 8.5 * cm]
COLW3 = [5.5 * cm, 5.5 * cm, 5.6 * cm]

TITULO_CENTRO = ParagraphStyle("titulo_centro", fontName="Serif-B", fontSize=27,
    leading=32, alignment=TA_CENTER, textColor=M.C["tinta"])
SUB_CENTRO = ParagraphStyle("sub_centro", fontName="Serif-I", fontSize=13,
    leading=18, alignment=TA_CENTER, textColor=M.C["gris"])
FOOT_CENTRO = ParagraphStyle("foot_centro", fontName="Sans-B", fontSize=8.6,
    leading=13, alignment=TA_CENTER, textColor=M.C["azul_noche"])


# ═══════════════════════════════════════════════════════════════ PORTADA
def portada():
    out = [Spacer(1, 6.8 * CM)]
    out.append(Paragraph("WALMART INC.", TITULO_CENTRO))
    out.append(Spacer(1, 4))
    out.append(Paragraph(
        "NYSE: WMT &nbsp;·&nbsp; Consumo defensivo / Minorista de gran escala",
        ParagraphStyle("t2", parent=TITULO_CENTRO, fontSize=15, leading=19)))
    out.append(Spacer(1, 10))
    out.append(Paragraph(
        "“Comprar mucho, vender barato, rotar rápido” contra "
        "“el precio ya paga una década de aceleración digital”",
        SUB_CENTRO))
    out.append(Spacer(1, 26))
    out.append(M.kpi_panel([
        ("NO COMPRAR TODAVÍA", "VEREDICTO", "Calidad real · precio no lo sostiene hoy"),
        ("US$107,15", "PRECIO 11-SEP-2026", "EV≈US$889.000M · ≈78,5x owner earnings"),
        ("6,6%–7,3%", "WACC DE MERCADO", "Bottom-up, Candado B — nunca de tier"),
    ]))
    out.append(Spacer(1, 30))
    out.append(Paragraph(
        "Tesis nueva · Método QG de 12 pasos (“Comprensión Primero con candado adversarial”, "
        "refundación 2026-07-19) · Candado A (abogado-diablo) ejecutado en sesión limpia · "
        "12-sep-2026", FOOT_CENTRO))
    out.append(NextPageTemplate("Normal"))
    out.append(PageBreak())
    return out


# ═══════════════════════════════════════════════════ NOTA DE ALCANCE / CHANGELOG
def nota_alcance():
    out = M.flag_titulo("Nota de alcance",
        "Por qué este documento no lleva radar de 11 reglas Seilern ni zonas de MoS por tier")
    out.append(M.p(
        "Esta tesis se produjo con el método QG de 12 pasos (“Comprensión Primero con candado "
        "adversarial”), la política vigente desde el 19-jul-2026 para toda tesis nueva. Ese método "
        "reemplaza por completo a <b>qg-seilern</b> y <b>val-mos</b> — ambas retiradas explícitamente y "
        "prohibidas para tesis nuevas — porque el sistema de 11 reglas ponderadas producía un ranking "
        "por debajo de su propio ruido (71,3% de pares del top-30 estadísticamente indistinguibles). "
        "El propio estándar editorial de esta maqueta (economist-qg) todavía instruye correr qg-seilern "
        "y val-mos para llenar las secciones de calidad y valoración — esa instrucción quedó "
        "desactualizada tras la refundación y se ignora aquí a propósito."))
    out.append(M.p(
        "Lo que este documento SÍ presenta, en su lugar, es el monólogo evidenciado completo de los "
        "12 pasos: círculo de competencia, knock-outs binarios HECHO-only, mecanismo del moat, "
        "scuttlebutt, motor de reinversión (g = tasa de reinversión × ROIC incremental), gestión leída "
        "como texto, percepción variante, pre-mortem fechado, WACC bottom-up de mercado, DCF inverso, "
        "y el veto bloqueante de <b>abogado-diablo</b> en sesión limpia — ejecutado y adjudicado "
        "objeción por objeción, no como ceremonia."))
    out.append(M.callout("LECCIÓN TRANSFERIBLE",
        "Un canon editorial también puede quedar obsoleto. La disciplina correcta no es maquetar el "
        "documento que el molde espera, sino el que refleja el método vigente — y decirlo por escrito, "
        "no en silencio."))
    out.append(PageBreak())
    return out


# ═══════════════════════════════════════════════════════════ RESUMEN 30s
def resumen():
    out = M.flag_titulo("Resumen en treinta segundos", "Lo que hay que saber antes de leer el resto")
    out.append(M.kpi_panel([
        ("~78,5x", "MÚLTIPLO EV/OWNER EARNINGS", "Sobre owner earnings FY26 (US$11.320M)"),
        ("15%–18%", "g EXIGIDO A 10 AÑOS", "Por el precio de hoy (DCF inverso, Paso 9.3)"),
        ("0,3%–2%", "g MECÁNICO HONESTO", "Motor de reinversión, revisado tras el Candado A"),
    ]))
    out.append(Spacer(1, 10))
    out.append(M.p(
        "<b>Walmart es un negocio de calidad real</b>: sin knock-outs, ROIC 14-16% muy por encima del "
        "costo de capital, moat físico verificado en filing primario, y una gestión que diseñó sus "
        "incentivos explícitamente para evitar el juego de EPS vía recompras. <b>El precio de hoy no "
        "es el problema de calidad — es el problema de expectativa</b>: exige que el motor de "
        "publicidad y marketplace siga acelerando a un ritmo que el propio 10-K, leído sin atajos, "
        "todavía no muestra."))
    out.append(M.p(
        "Tres puntos críticos: <b>(1)</b> “Walmart Connect” —la publicidad que sostiene la "
        "narrativa de re-rating— no aparece ni una sola vez en el texto del 10-K FY2026; todo lo que "
        "hay sobre ella es prensa. <b>(2)</b> El primer cálculo de esta tesis descartó el ROIC "
        "incremental de un año (~0,3%) como “ruido” y lo sustituyó por un número más cómodo — "
        "el abogado-diablo lo cazó como la misma racionalización que ya causó un retiro de regla en "
        "esta casa en agosto-2026. <b>(3)</b> El semestre más reciente (H1 FY2027) ya muestra el "
        "síntoma: FCF cayendo pese a que el negocio operativo mejoró, porque el capex se disparó "
        "primero que el retorno."))
    out.append(M.callout("PAUSA REFLEXIVA",
        "Si el negocio no está roto y el precio tampoco es absurdo en términos absolutos "
        "(15-18% de crecimiento no es una fantasía para una empresa que ya hizo 14,4% este año), "
        "¿por qué NO COMPRAR TODAVÍA en vez de COMPRAR? Porque el precio exige que el BUEN año se "
        "convierta en la NORMA durante una década — y el dato más fresco disponible apunta en la "
        "dirección contraria."))
    out.append(PageBreak())
    return out


# ═══════════════════════════════════════════════════════════ CUADRO DE MANDO
def cuadro_mando():
    out = M.flag_titulo("Cuadro de Mando", "La única pieza que se refresca cada trimestre — tesis nueva, primer corte")
    out.append(M.p("<b>Bloque 1 — Estado de la posición</b>", "h3"))
    out.append(M.p(
        "Sin posición viva (confirmado vía IBKR MCP, 12-sep-2026). Precio US$107,15 (11-sep-2026). "
        "Sin “zona val-mos” —esa capa no se calculó, ver Nota de alcance—; el ancla de esta "
        "tesis es el DCF inverso del Paso 9.3: el precio implica un múltiplo de ~78,5x sobre owner "
        "earnings FY26, y un precio de entrada razonable para reabrir como candidata de compra se "
        "estima en <b>US$35-50/acción</b> (Paso 11). Veredicto operativo: <b>NO COMPRAR TODAVÍA</b>. "
        "Tramos: ninguno ejecutado, ninguno pendiente."))
    out.append(M.p("<b>Bloque 2 — Tracker de KPIs en semáforo</b>", "h3"))
    out.append(M.tabla([
        ["KPI", "Umbral de alerta", "Estado 12-sep-2026"],
        ["Comparables Walmart US (trimestral)", "&lt; +3%", "<font color=\"#B8860B\"><b>ÁMBAR</b></font> — +2,6% en Q2 FY2027 (el más lento en 6 años)"],
        ["FCF trimestral (OCF − capex)", "Caída YoY", "<font color=\"#8C1410\"><b>ROJO</b></font> — H1 FY2027: −US$1.400M YoY pese a OCF +US$1.400M"],
        ["ROIC incremental YoY (ΔNOPAT/ΔCapital)", "&lt; 5% por 2 años consecutivos", "<font color=\"#B8860B\"><b>ÁMBAR</b></font> — FY26: ~0,3-0,5% (1 año, ya en zona de alerta)"],
        ["Divulgación de “Walmart Connect” en 10-K", "Ausente", "<font color=\"#8C1410\"><b>ROJO</b></font> — Ausente en FY2026, hueco de evidencia abierto"],
    ], [6.6 * CM, 4.4 * CM, 6.0 * CM]))
    out.append(M.p("<b>Bloque 3 — Feedback loop de calibración</b>", "h3"))
    out.append(M.p(
        "No aplica: tesis nueva, sin predicción previa que calibrar. El Paso 12 (diario) fija las "
        "primeras cuatro predicciones falsables de esta posición — ver §12.", "nota"))
    out.append(M.p("<b>Bloque 4 — Operativo</b>", "h3"))
    out.append(M.p(
        "Último trigger: ninguno (primer corte). Próxima revisión obligatoria: resultados Q3 FY2027 "
        "(~nov-2026, indicador líder) y 10-K FY2027 (~mar-2027, falsador principal). Documento base: "
        "<i>Tesis/WMT/2026-09-12_UltraTesis_WMT_metodo12_borrador.md</i>; entrada añadida a "
        "<i>gates.md</i> el 12-sep-2026.", "nota"))
    out.append(PageBreak())
    return out


# ═══════════════════════════════════════════════════════════ §1 HISTORIA
def s1():
    out = M.flag_titulo("§1 · La historia detrás del veredicto", "El monólogo previo, congelado antes de investigar (Paso 0)")
    out.append(M.p(
        "Walmart es el minorista más grande del mundo por ingresos: gana dinero por volumen y "
        "rotación de inventario a márgenes operativos bajos (4,2%-4,4%), no por margen alto — el "
        "modelo “everyday low price” sostenido por una escala de compra y una densidad "
        "logística que ningún competidor generalista iguala. En los últimos años sumó dos motores de "
        "margen más alto que no existían hace una década: publicidad (Walmart Connect) y comisiones "
        "de marketplace de terceros, más Walmart+ como fidelización al estilo Prime."))
    out.append(M.p(
        "El monólogo previo (12-sep-2026, antes de mirar un solo dato nuevo) dudaba de tres cosas: "
        "el múltiplo re-rateado con fuerza en los últimos años; si el e-commerce de EE.UU. es rentable "
        "en unit economics reales o si la narrativa se apoya en publicidad que maquilla una logística "
        "de última milla que sigue perdiendo dinero; y si Amazon/Costco/Aldi limitan cuánto puede subir "
        "el margen sin dañar el posicionamiento de precio bajo. <b>Las tres dudas sobrevivieron la "
        "investigación — con más precisión y, en el caso del motor de reinversión, más gravedad de la "
        "anticipada.</b>"))
    out.append(M.callout("CASO HISTÓRICO",
        "El ataque más serio que el moat de Walmart ya sobrevivió, con fecha: la adquisición de Whole "
        "Foods por Amazon en junio de 2017, leída entonces como la entrada de una tecnológica con "
        "capital ilimitado a la distribución física de alimentos. Nueve años después, Walmart mantiene "
        "el liderazgo de cuota de comestibles en EE.UU. (~20,4% en 2026), pero con erosión lenta y "
        "concentrada exactamente en frescos — la categoría donde el moat físico debería ser más "
        "impenetrable."))
    out.append(PageBreak())
    return out


# ═══════════════════════════════════════════════ §2 CÍRCULO DE COMPETENCIA + MODELO
def s2():
    out = M.flag_titulo("§2 · Círculo de competencia y modelo de negocio", "Paso 1 del método — veto sin apelación si falla")
    out.append(M.p(
        "<b>Pregunta única: ¿se puede nombrar el mecanismo por el que Walmart gana dinero, en una "
        "frase, sin jerga de gestión?</b> Sí. Walmart compra a una escala que ningún competidor "
        "generalista iguala, fija precios deliberadamente bajos para maximizar la rotación de "
        "inventario y el volumen de caja, y gana dinero porque el ahorro de escala en compras y la "
        "eficiencia operativa por dólar de venta superan el margen bruto que sacrifica frente a un "
        "minorista de precio más alto. <b>PASA sin apelación.</b>"))
    out.append(M.p("<b>Segmentos (FY2026, HECHO de 10-K):</b>", "h3"))
    out.append(M.tabla([
        ["Segmento", "Ingresos totales", "Ingreso operativo", "% del total de ingresos"],
        ["Walmart U.S.", "US$485.599M", "US$25.158M", "68,1%"],
        ["Walmart International", "US$131.988M", "US$5.103M", "18,5%"],
        ["Sam's Club U.S.", "US$95.540M", "US$2.442M", "13,4%"],
        ["Consolidado", "US$713.163M", "US$29.825M", "100%"],
    ], [4.6 * CM, 4.4 * CM, 4.2 * CM, 3.8 * CM]))
    out.append(M.p(
        "E-commerce global ≈US$150.400M (FY26), +24% interanual — Walmart U.S. eCommerce "
        "US$99.600M, Walmart International US$35.800M, Sam's Club US$15.000M (todo HECHO, 10-K "
        "FY2026, Nota de Segmentos). “Walmart Connect” no aparece como línea propia en "
        "ningún filing — su crecimiento (+38%-46% interanual citado en prensa sobre las calls) es "
        "INFERENCIA, no HECHO.", "nota"))
    out.append(PageBreak())
    return out


# ═══════════════════════════════════════════════════ §3 KNOCK-OUTS
def s3():
    out = M.flag_titulo("§3 · Knock-outs mecánicos, binarios, HECHO-only", "Paso 2 del método — cualquiera de estos, disparado, cierra el proceso")
    out.append(M.tabla([
        ["Knock-out", "Umbral", "Dato (10-K FY2026, HECHO)", "¿Dispara?"],
        ["Estructura VIE", "Material", "“inmateriales”, declarado por la empresa", "NO"],
        ["SBC / FCF ajustado ≥3a", "&gt;50%", "13,8% (FY24) → 21,9% (FY25) → 24,1% (FY26)", "NO — vigilar tendencia"],
        ["ROIC &lt; WACC estructural ≥3a", "3 años", "ROIC 14,5-17,6% vs. WACC 6,6-7,3%", "NO"],
        ["Restatement de ingresos", "Cualquiera", "Flag XBRL “error correction” = false", "NO"],
        ["Dependencia cliente/regulador único", "Material", "“sin ingresos materiales de un solo cliente”", "NO"],
        ["Deuda tóxica / covenants", "Cualquiera", "AA/Aa2/AA, sin covenants sobre dividendos/recompras", "NO"],
    ], [4.6 * CM, 2.6 * CM, 6.4 * CM, 3.4 * CM]))
    out.append(M.p(
        "<b>Ningún knock-out disparado.</b> Los seis con evidencia estructurada "
        "{documento, página/sección, fecha} completa — 10-K FY2026, CIK 0000104169, Accession "
        "0000104169-26-000055, presentado 13-mar-2026.", "nota"))
    out.append(PageBreak())
    return out


# ═══════════════════════════════════════════════════ §4 MOAT + SCUTTLEBUTT
def s4():
    out = M.flag_titulo("§4 · El moat y el scuttlebutt", "Pasos 3 y 4 del método")
    out.append(M.p("<b>Mecanismo, tres capas:</b>", "h3"))
    out.append(M.p(
        "<b>(1)</b> Escala de compra + densidad logística que se autorrefuerzan — verificado en filing "
        "primario. <b>(2)</b> Escala de datos de primera parte monetizada como negocio nuevo (Walmart "
        "Connect) — dirección correcta, magnitud NO verificada en 10-K. <b>(3)</b> “Precio bajo "
        "todos los días” como activo de marca/confianza, no comparación ítem por ítem."))
    out.append(M.p(
        "<b>Test de Sleep — el ahorro de escala ¿a quién va?</b> Evidencia mixta: el margen bruto de "
        "Walmart US subió ~158pb en Q2 FY2027 atribuido en parte a mix hacia publicidad — la empresa "
        "se queda el ahorro incremental. Al mismo tiempo, gestión anunció que usará ~US$2.900M de "
        "reembolsos arancelarios para <b>bajar precios</b>, no margen — pero esa fuente de capital es "
        "distinta a las utilidades de Connect, no prueba la retroalimentación declarada."))
    out.append(M.p("<b>Scuttlebutt (dossier, presupuesto de 2h ya consumido, con fecha de cada fuente):</b>", "h3"))
    out.append(M.tabla([
        ["Fuente", "Hallazgo"],
        ["CFRA (Arun Sundaram), 2026", "Amazon carece de presencia física suficiente para desplazar a Walmart en comestibles a corto plazo"],
        ["Numerator/Morgan Stanley, 2026", "Cuota de mercado US Walmart: 21,1%→20,6%→20,4% (2024→2025→2026), erosión concentrada en frescos"],
        ["TD Cowen (Oliver Chen), abr-2026", "Walmart supera a Target “en todas las métricas” desde la pandemia"],
        ["Prensa comparada earnings, 2026", "Costco P/E~56 (renovación 89,7%) vs. Walmart P/E~39 — el mercado premia distinto cada modelo"],
    ], [5.5 * CM, 11.1 * CM]))
    out.append(M.callout("PAUSA REFLEXIVA",
        "Si la capa #2 del moat (publicidad) no aparece ni una vez en el 10-K, ¿qué tan sólida es la "
        "narrativa de que el moat “se está profundizando”, frente a la lectura más simple de "
        "que el moat núcleo se mantiene con erosión lenta y la capa nueva es, hasta ahora, prensa?"))
    out.append(PageBreak())
    return out


# ═══════════════════════════════════════════════════ §5 MOTOR DE REINVERSIÓN
def s5():
    out = M.flag_titulo("§5 · El motor de reinversión", "Paso 5 — g = tasa de reinversión × ROIC incremental (REVISADO tras Paso 10)")
    out.append(M.chart("charts/wmt_roic_wacc.png"))
    out.append(M.tabla([
        ["Partida (FY2026, HECHO 10-K salvo INFERENCIA marcada)", "Valor"],
        ["NOPAT = Operating income × (1−tasa impositiva)", "US$22.548M"],
        ["Capex de crecimiento = capex total − D&A", "US$12.439M"],
        ["Tasa de reinversión", "55,2%"],
        ["ROIC vigente (rango con/sin arrendamientos)", "14,5%-16,1%"],
        ["ROIC incremental estricto, un año (ΔNOPAT/ΔCapital)", "≈0,3%-0,5%"],
    ], [11.4 * CM, 5.2 * CM]))
    out.append(M.p(
        "La primera versión de esta tesis descartó el ROIC incremental estricto (0,3-0,5%) como "
        "“ruido de un año” y lo sustituyó por el ROIC vigente (~15%), dando g mecánico ≈8,3%, "
        "citando un precedente metodológico de esta casa (un análisis previo de Costco). <b>El "
        "abogado-diablo (Paso 10) mostró que el precedente no aplica</b>: Costco tenía capex "
        "deliberadamente lento y podía acelerar sin diluir retornos; Walmart ya reinvierte cerca de su "
        "ritmo máximo observable (capex +24% interanual en H1 FY2027), lo que hace MÁS, no menos, "
        "probable que el dólar marginal vaya a categorías de retorno decreciente. Dos movimientos "
        "estructurales simultáneos (margen operativo 4,4%→4,2% y tasa impositiva efectiva 23,4%→24,4%) "
        "en el mismo año que el capex se disparó no es un choque puntual — es un patrón."))
    out.append(M.callout("LECCIÓN TRANSFERIBLE",
        "“Descartar por ruido” un dato incómodo, sin una regla simétrica pre-registrada de qué "
        "cuenta como ruido, es la misma racionalización sin importar el nombre que se le ponga. Esta "
        "casa ya retiró una regla completa por ese patrón en agosto-2026 (medición de ruido fallida) — "
        "reaparecer en un contexto nuevo no lo hace menos grave."))
    out.append(M.p(
        "<b>g mecánico honesto, revisado: 0,3%-2%</b> (se abandona el punto de trabajo de 8,3%). Qué "
        "limita el crecimiento: a diferencia de Costco (limitada por ritmo de apertura de clubes), la "
        "huella física de Walmart ya está madura — el límite real es un techo de monetización digital "
        "(publicidad y marketplace compitiendo por el mismo presupuesto de proveedores que Amazon, "
        "Target Roundel, Kroger Precision Marketing e Instacart Ads).", "nota"))
    out.append(PageBreak())
    return out


# ═══════════════════════════════════════════════════ §6 GESTIÓN + PERCEPCIÓN VARIANTE
def s6():
    out = M.flag_titulo("§6 · Gestión, incentivos y percepción variante", "Pasos 6 y 7 del método")
    out.append(M.p("<b>Gestión (DEF 14A 2026, leída como texto — Dominio J3):</b>", "h3"))
    out.append(M.p(
        "La compensación variable de los NEOs (incluido el CEO) se ata a <b>ventas totales, ingreso "
        "operativo y ROI</b> — el comité rechaza explícitamente TSR relativo (“no creemos que sea "
        "la mejor forma de incentivar”) y, más importante, rechaza EPS como métrica reconociendo "
        "por escrito que “no están materialmente afectadas por las recompras de acciones” — "
        "exactamente el diseño anti-Goodhart que este paso busca, dicho por el propio comité, no "
        "inferido. Sucesión ordenada e interna: John Furner (19 años en la empresa) reemplazó a Doug "
        "McMillon el 1-feb-2026. De 203 Formularios 4 en 12 meses, 0 son compras discrecionales en "
        "mercado abierto — neutro-a-ligeramente-negativo, no una alarma."))
    out.append(M.p("<b>Percepción variante (Paso 7) — veredicto honesto:</b>", "h3"))
    out.append(M.p(
        "El consenso ya trata a Walmart como un “compounder digital-más-retail”, pagando ~39x "
        "utilidad diluida por esa tesis. El hallazgo central de este documento (el precio exige ~2x-más "
        "de lo que el motor entrega) es aritmética de DCF inverso, no un dato no público — y el propio "
        "mercado ya reaccionó a esta misma pregunta: la acción cayó <b>~8,9% en un solo día</b> "
        "(20-ago-2026) pese a superar expectativas, por la desaceleración de comparables en EE.UU. a "
        "+2,6% (el ritmo más lento en 6 años)."))
    out.append(M.callout("PAUSA REFLEXIVA",
        "<b>Variante débil, y se registra así sin disfrazarlo.</b> Esta tesis se acerca más a "
        "“consenso con pasos extra” que a una percepción genuinamente diferencial. No cierra "
        "el proceso, pero baja el techo de lo que este documento puede reclamar como ventaja propia."))
    out.append(PageBreak())
    return out


# ═══════════════════════════════════════════════════ §7 PRE-MORTEM
def s7():
    out = M.flag_titulo("§7 · Pre-mortem con fecha", "Paso 8 del método — congelado ANTES de correr la valoración")
    filas = [
        ["Mecanismo", "Métrica observable", "Ventana"],
        ["La “rentabilidad” del e-commerce US es espejismo de mix (publicidad/marketplace), no de fulfillment",
         "Crecimiento de publicidad &lt;15-20% YoY por 2 trimestres sin compensación", "4-6 trimestres (~FY2028)"],
        ["El capex de automatización no rinde el ROIC incremental prometido",
         "Capex/ventas &gt;4% sin expansión de margen operativo por 2 años", "FY2027-FY2028"],
        ["La defensa de precio bajo fuerza a seguir absorbiendo aranceles/inflación",
         "Margen bruto ex-combustible cae &gt;50pb YoY por 2 trimestres, atribuido a aranceles", "4 trimestres (~2027)"],
        ["Flipkart/India: guerra de descuentos o endurecimiento regulatorio",
         "Pérdida operativa internacional ampliándose 2 trimestres, o cambio regulatorio indio", "4-6 trimestres"],
    ]
    out.append(M.tabla(filas, [6.0 * CM, 7.6 * CM, 3.0 * CM]))
    out.append(M.p(
        "Ninguno confirmado al 12-sep-2026 — son hipótesis de trayectoria congeladas antes del DCF, no "
        "defectos ya observados. El mecanismo #2 ya muestra su primer síntoma en H1 FY2027 (ver §8).", "nota"))
    out.append(PageBreak())
    return out


# ═══════════════════════════════════════════════════ §8 VALORACIÓN
def s8():
    out = M.flag_titulo("§8 · Valoración como pregunta falsable", "Paso 9 del método — WACC siempre de mercado (Candado B)")
    out.append(M.p("<b>8.1 — WACC bottom-up, con fuente y fecha declaradas:</b>", "h3"))
    out.append(M.tabla([
        ["Insumo", "Valor", "Fuente / fecha"],
        ["Beta — dos fuentes discrepantes", "0,415 (GuruFocus) / 0,59-0,60 (stockanalysis/Yahoo)", "jul/sep-2026"],
        ["Rf (Treasury 10Y)", "4,96%", "U.S. Treasury, 11-sep-2026"],
        ["ERP implícita (Damodaran)", "4,23%", "“Data Update 2 for 2026”, ref. ene-2026"],
        ["Kd de mercado (Rf + spread AA reciente)", "≈5,66%", "Emisión bono 10a, abr-2026, +70pb"],
        ["E/V (a valor de mercado)", "≈94,4%", "Mkt cap ≈US$850.100M vs. deuda US$50.411M"],
    ], [5.0 * CM, 7.0 * CM, 4.6 * CM]))
    out.append(M.p(
        "<b>WACC = rango 6,6%-7,3%, punto central ~7,0%.</b> No se elige un solo beta por conveniencia — "
        "se calcula el WACC con ambas fuentes y se reporta como rango (Candado C, piso de resolución). "
        "Nunca heredado de un tier de calidad.", "nota"))
    out.append(M.chart("charts/wmt_owner_earnings.png"))
    out.append(M.p("<b>8.2 — DCF inverso (protocolo Rappaport-Mauboussin):</b>", "h3"))
    out.append(M.chart("charts/wmt_dcf_inverso.png"))
    out.append(M.p(
        "EV≈US$889.000M (mkt cap US$850.100M + deuda US$50.411M − caja US$11.529M, 10-Q 31-jul-2026) "
        "frente a owner earnings FY26 US$11.320M ⇒ múltiplo ≈78,5x. Resolviendo a 10 años con fade a 3% "
        "terminal: <b>g exigido ≈15,3% (WACC 6,6%) a ≈17,8% (WACC 7,3%)</b>. Contra el g mecánico "
        "honesto (0,3%-2%, §5), la brecha es de un orden de magnitud, no “el doble” que sugería "
        "el primer cálculo antes del Candado A."))
    out.append(M.p("<b>8.3 — Trampa de valor, pares y asimetría:</b>", "h3"))
    out.append(M.p(
        "El test clásico de trampa de valor no aplica en forma canónica: no hay de-rating que probar — "
        "es la situación inversa (re-rating de 15-25x histórico a ~39x). Contexto de pares, descriptivo, "
        "sin ranking: Costco ~56x (modelo más simple y predecible), Walmart ~39x, Target/Kroger "
        "sustancialmente más bajos. <b>Asimetría, con signo: negativa.</b> El precio ya es el escenario "
        "optimista, no el central — si el crecimiento revierte hacia el motor mecánico, el múltiplo "
        "tiene espacio amplio para comprimirse hacia 20-25x sin que el negocio se rompa."))
    out.append(PageBreak())
    return out


# ═══════════════════════════════════════════════════ §9 ABOGADO-DIABLO
def s9():
    out = M.flag_titulo("§9 · Candado A — veto de abogado-diablo", "Paso 10 — sesión limpia, sin el historial de esta investigación")
    out.append(M.p(
        "Agente en sesión nueva, recibiendo solo los hechos estructurados de los Pasos 1-2-3-5-6-7-9 "
        "— nunca esta prosa. Tarea única: atacar el moat, la tasa de reinversión y la asimetría con la "
        "pregunta “¿qué caso concreto habría cambiado esto?”."))
    out.append(M.tabla([
        ["Objeción del abogado-diablo", "Adjudicación"],
        ["Moat: la capa #2 (publicidad) no está en el 10-K; la erosión de cuota se concentra en frescos, "
         "donde el moat físico debería ser más fuerte",
         "ACEPTADA. Se rebaja la capa #2 de “mecanismo verificado” a “hipótesis de "
         "dirección correcta, magnitud no verificada”"],
        ["ROIC incremental: descartar 0,3% como ruido y usar el precedente de Costco es una "
         "racionalización — Costco podía acelerar capex, Walmart ya está a ritmo máximo",
         "ACEPTADA, sin evidencia nueva que la refute. Anulación optimista REVOCADA en el propio Paso 10, "
         "sin esperar al falsador de FY2027 — el indicador líder (H1 FY2027) ya apunta a la revocación"],
        ["Asimetría: el beta alto (más defendible para un retailer apalancado) y anclar el DCF en el "
         "mejor año fiscal (FY26) cuando H1 FY27 ya muestra reversión, favorecen al toro en ambos extremos",
         "ACEPTADA parcialmente. Punto de trabajo del WACC movido al extremo alto del rango ya declarado; "
         "advertencia de frescura del owner earnings reforzada, no recalculada (no hay FY27 completo aún)"],
    ], [6.0 * CM, 10.6 * CM]))
    out.append(M.callout("CASO HISTÓRICO",
        "El agente nombró explícitamente el sesgo: “anclaje metodológico reforzado por halo de "
        "calidad”, y citó el precedente ya registrado en la memoria del proyecto donde una regla "
        "de “descartar por ruido” violó cuatro candados y tuvo que retirarse "
        "(medición de ruido fallida, ago-2026). Mismo patrón, contexto nuevo — el Candado A hizo "
        "exactamente el trabajo para el que existe."))
    out.append(M.p(
        "<b>Consecuencia para el veredicto:</b> no cambia la dirección (seguía sin ser COMPRA antes del "
        "ataque, sigue sin serlo después), pero cambia la calidad del argumento — de “negocio "
        "excelente, precio exigente” a “motor de reinversión más débil de lo que la primera "
        "lectura sugería, cotizando a un precio que exige una aceleración sin evidencia de filing "
        "primario de que ya esté ocurriendo”."))
    out.append(PageBreak())
    return out


# ═══════════════════════════════════════════════════ §10 VEREDICTO FINAL
def s10():
    out = M.flag_titulo("§10 · Veredicto final, triggers y diario", "Pasos 11 y 12 del método")
    out.append(M.p(
        "<b>Veredicto: NO COMPRAR TODAVÍA.</b> Calidad real (sin knock-outs, ROIC muy por encima del "
        "WACC, moat núcleo verificado, incentivos de gestión bien diseñados) — pero el precio de hoy "
        "exige ~15-18% de crecimiento anual de owner earnings durante una década, y el motor de "
        "reinversión, medido sin sustituciones que no sobrevivieron el Candado A, entrega hoy apenas "
        "~0,3%-2%. No es NO (el moat núcleo no está roto) ni NO DECIDIBLE (la clase de referencia — "
        "mega-retailers cotizados — tiene más de 30 casos)."))
    out.append(M.p(
        "<b>Precio al que sí se sostendría:</b> con un g mecánico honesto en el rango bajo (~2-4%, "
        "dando el beneficio de la duda de que el 0,3% de un año es demasiado pesimista para "
        "extrapolar) y WACC 7,0%, el múltiplo sostenible ronda 25-35x — implicando un rango aproximado "
        "de <b>US$35-50/acción</b>, sin que el negocio tenga que romperse."))
    out.append(M.p("<b>Predicciones falsables, con fecha (Paso 12):</b>", "h3"))
    out.append(M.tabla([
        ["#", "Predicción", "Fecha / ventana"],
        ["1 (principal)", "10-K FY2027 con owner earnings +8% YoY Y ROIC incremental YoY &gt;10% revertiría la lectura de hoy",
         "~mar-2027"],
        ["2 (líder)", "Comparables US &lt;+3% y FCF trimestral sin revertir a positivo confirma el motor debilitándose",
         "Q3 FY2027, ~nov-2026"],
        ["3 (moat)", "“Walmart Connect” apareciendo como línea propia en un 10-K futuro resuelve el hueco de evidencia",
         "Continuo"],
        ["4 (precio)", "Acción &lt;~US$50 sin deterioro adicional de calidad reabre la tesis como candidata de COMPRA activa",
         "Continuo"],
    ], [2.2 * CM, 11.4 * CM, 3.0 * CM]))
    out.append(M.p(
        "Sin posición, sin operación ejecutada — no aplica registro en diario-decisiones.md (reservado "
        "a compras/ventas ejecutadas). El Candado A cambió materialmente la calidad del argumento de "
        "reinversión sin cambiar la dirección del veredicto — se registra como validación de que el "
        "candado no es ceremonia.", "nota"))
    out.append(PageBreak())
    return out


# ═══════════════════════════════════════════════════════════════ CIERRE
def cierre():
    out = M.flag_titulo("Cierre", "Glosario y advertencias")
    out.append(M.p("<b>Glosario breve:</b>", "h3"))
    out.append(M.p(
        "<b>Owner earnings</b> — FCF (flujo de caja operativo menos capex) menos compensación en "
        "acciones (SBC); aproximación de Buffett al efectivo distribuible real. "
        "<b>ROIC incremental</b> — retorno sobre el capital nuevo desplegado en un período, distinto "
        "del ROIC sobre el capital total ya invertido. <b>DCF inverso</b> — en vez de proyectar flujos "
        "para hallar un valor, se parte del precio de mercado y se despeja qué crecimiento implícito "
        "exige. <b>WACC bottom-up</b> — costo de capital construido desde beta, tasa libre de riesgo y "
        "prima de riesgo de mercado citadas con fuente, nunca heredado de una regla cualitativa.", "cuerpo"))
    out.append(M.p("<b>Advertencias finales:</b>", "h3"))
    out.append(M.p(
        "Todo dato lleva etiqueta HECHO (10-K/10-Q/DEF 14A, SEC EDGAR) / INFERENCIA (cálculo propio "
        "sobre líneas HECHO, o prensa sobre las calls) / SUPUESTO (elección declarada explícitamente, "
        "p. ej. la tasa impositiva usada en el escudo fiscal del WACC). Ningún dato de este documento "
        "proviene de qg-seilern ni de val-mos — ambas retiradas de la política del proyecto el "
        "19-jul-2026. Documento de uso personal, no constituye asesoría de inversión registrada.", "nota"))
    out.append(M.callout("PAUSA REFLEXIVA",
        "¿Qué queda por saber? La pieza que más cambiaría este veredicto es la que ya está fechada: "
        "si el 10-K FY2027 (~mar-2027) muestra a Walmart Connect divulgado como línea propia con "
        "magnitud verificable, y el ROIC incremental del año completo supera el 5-10% en vez del "
        "0,3-0,5% de este corte, la capa #2 del moat deja de ser hipótesis y el motor de reinversión "
        "deja de ser el punto más débil del documento."))
    return out


def story():
    s = []
    s += portada()
    s += nota_alcance()
    s += resumen()
    s += cuadro_mando()
    s += s1()
    s += s2()
    s += s3()
    s += s4()
    s += s5()
    s += s6()
    s += s7()
    s += s8()
    s += s9()
    s += s10()
    s += cierre()
    return s
