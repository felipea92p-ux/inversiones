# -*- coding: utf-8 -*-
"""Portada · Resumen en treinta segundos · Aviso de estado"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, kpi_panel, S, C, cm
from reportlab.platypus import Spacer, PageBreak, NextPageTemplate, Paragraph
from reportlab.lib.styles import ParagraphStyle


def portada():
    t_emp = ParagraphStyle("te", fontName="Serif-B", fontSize=38, leading=42, textColor=C["tinta"])
    t_tag = ParagraphStyle("tg", fontName="Serif-I", fontSize=13.5, leading=19, textColor=C["gris"])
    t_sec = ParagraphStyle("ts", fontName="Sans-B", fontSize=9, leading=12, textColor=C["rojo"])
    return [
        Spacer(1, 5.7*cm),
        Paragraph("INFORMACIÓN PROFESIONAL · ANALÍTICA Y EDICIÓN CIENTÍFICA", t_sec),
        Spacer(1, 10),
        Paragraph("RELX PLC", t_emp),
        Spacer(1, 2),
        Paragraph("REL.L (Londres) · RELX (Nueva York)", ParagraphStyle(
            "tk", fontName="Sans-B", fontSize=10, leading=13, textColor=C["azul_noche"])),
        Spacer(1, 8),
        Paragraph("Cuatro monopolios de nicho que ya sobrevivieron a que el contenido se hiciera gratis "
                  "una vez — y ahora vuelven a jugarse lo mismo contra la IA generativa.", t_tag),
        Spacer(1, 4),
        Paragraph("El negocio es tan bueno como parece. El expediente queda cerrado igual: archivada con "
                  "veredicto NO, ratificado el 8 de septiembre tras un ejercicio adicional que apuntaba, "
                  "de forma casi tramposa, en la dirección contraria.", t_tag),
        Spacer(1, 1.4*cm),
        kpi_panel([("US$35,34 / 2.593p", "PRECIO 8-SEP-2026", "cotización de referencia<br/>de esta actualización"),
                   ("NO", "VEREDICTO — ARCHIVADA", "fijado el 4-sep, ratificado<br/>sin cambios el 8-sep"),
                   ("-37% vs +11-18%", "LA ASIMETRÍA QUE DECIDE", "downside &gt; upside, hoy,<br/>con cualquier beta razonable")]),
        Spacer(1, 0.85*cm),
        tabla([["FECHA", "PRECIO", "VEREDICTO", "QUÉ CAMBIÓ"],
               ["4 de septiembre de 2026", "£26,20 (2.620p)", "NO (recién degradado)", "Paso 10: asimetría ya desfavorable hoy"],
               ["8 de septiembre de 2026", "US$35,34 (2.593p)", "NO (confirmado)", "Recálculo de beta por completitud — sin efecto en el veredicto"]],
              [4.6*cm, 4.0*cm, 4.6*cm, 3.4*cm], font_sz=8.4),
        Spacer(1, 0.5*cm),
        M.p("<font size=8.4 color='#666054'><i>Segunda versión — método QG de 12 pasos, «Comprensión Primero con "
            "candado adversarial» (refundación 2026-07-19), sobre cinco Form 20-F (FY2021-FY2025) y Exhibit 15.2 "
            "de fuente primaria EDGAR, con veto del abogado del diablo en sesión limpia (Paso 10) y WACC "
            "bottom-up desde beta de mercado, nunca heredado de un tier de calidad. Añade el ejercicio de "
            "recálculo de beta del 8-sep-2026 y la decisión explícita de Felipe de no reabrir el veredicto por "
            "su resultado. Documento de trabajo personal. No es asesoramiento de inversión.</i></font>"),
        NextPageTemplate("Normal"), PageBreak()]


def resumen():
    o = flag_titulo("El resumen en treinta segundos", "Si solo lees una página, que sea esta")
    o += [p("<b>RELX es un negocio excelente. El veredicto sigue siendo NO, y esta actualización lo confirma sin "
        "tocarlo.</b> No «todavía no» — NO, archivada, con condiciones de reapertura explícitas y fechadas. "
        "Cuatro segmentos (Risk, Legal, STM, Exhibitions) cobran a profesionales por acceso a bases de datos "
        "propietarias y a las herramientas de trabajo incrustadas en cómo ya usan esos datos cada día: la "
        "biblioteca paga, no el investigador; la aseguradora consulta un histórico que ella misma alimentó; "
        "el abogado no puede permitirse citar mal un caso. Ningún knock-out se dispara en cinco ejercicios "
        "fiscales revisados, el ROIC sube todos los años desde 2021, y el margen operativo ajustado se expande "
        "sin excepción desde 2020. Nada de esto cambió entre el 4 y el 8 de septiembre.")]
    o += [p("<b>Lo que decide el NO no es un múltiplo caro ni un negocio roto: es la aritmética de la propia "
        "tesis.</b> Calculado con un WACC construido correctamente desde el mercado (7,5-8,5%, nunca heredado de "
        "ningún tier de calidad), el caso base cae dentro de un ±3% del precio de entonces, y la asimetría "
        "honesta es desfavorable: el escenario bajista (-37%) pesa más que el alcista razonable (+11% a +18%). "
        "Eso ya era así el 4 de septiembre, sin necesitar ningún dato nuevo — y es la razón por la que este es "
        "el único de los cinco casos de esta tanda cuyo veredicto llegó directamente a NO, no a NO COMPRAR "
        "TODAVÍA.")]
    o += [callout("PAUSA REFLEXIVA",
        "<b>Esta actualización del 8 de septiembre no reabre esa pregunta — la pone a prueba y la confirma.</b> "
        "Se corrió, solo por completitud, el mismo ejercicio de recálculo de beta que ese día se aplicó a las "
        "otras cuatro tesis de la tanda (CME, OBIC, TRI, CSU.TO): recalcular el beta incorporando explícitamente "
        "la ventana de pánico de IA generativa que golpeó a RELX el 7 de mayo de 2026 (-6,2% en un solo día, "
        "-28,6% pico-valle en el año). El resultado fue, de forma casi paradójica, un beta <b>más bajo</b> "
        "(0,342) que el original (0,64) — lo opuesto de lo que ocurrió en las otras tres tesis comparables. "
        "Tratado ingenuamente como señal, eso habría sugerido <i>más</i> descuento (-43,4%), no menos. Felipe "
        "decidió explícitamente no tratarlo como señal: el problema que sostiene el NO —la asimetría "
        "downside/upside— es independiente del beta, y perseguir el número que revierte el veredicto es "
        "exactamente el «methodology shopping» que el propio método existe para prohibir.")]
    o += [p("<b>El motivo de fondo sigue siendo un test que sigue abierto, no un precio.</b> En 2009, Google "
        "Scholar regaló la jurisprudencia y RELX sobrevivió moviendo el moat del texto al citador y a las "
        "herramientas de análisis. Diecisiete años después, Thomson Reuters compró Casetext y lanzó CoCounsel "
        "para intentar lo mismo con IA generativa, y el único dato comparativo disponible hoy —la guía que "
        "Thomson Reuters ya subió para 2026— corta en contra de RELX, no a favor. Eso no prueba que RELX esté "
        "perdiendo la carrera. Prueba que nadie, ni este documento, puede decir hoy que la está ganando.")]
    o += [p("<b>Y hay una ausencia que pesa en el momento exacto en que más debería pesar.</b> Tras la caída "
        "del 27% desde máximos de 52 semanas, ningún directivo compró acciones con dinero propio en los "
        "últimos doce meses — solo ventas mecánicas de sell-to-cover. No es una señal bajista por sí sola, "
        "pero es consistente con un precio en zona razonable, no de oportunidad.")]
    o += [hr(), p("<b>Las cifras que hay que retener:</b>")]
    o += [tabla([
        ["LA CIFRA", "QUÉ SIGNIFICA"],
        ["<b>-3% a +3%</b>",
         "Dónde cae el caso base del DCF (£25,5-26,9) frente al precio del 4-sep (£26,20), con el WACC construido "
         "correctamente. No hay descuento limpio: el precio ya sabía casi todo lo que este documento sabe."],
        ["<b>-37% frente a +11%/+18%</b>",
         "La asimetría real, sin cambios el 8-sep: el caso bajista genérico de madurez pesa más que el caso "
         "alcista razonable. Y el propio abogado del diablo encontró que ese -37% probablemente es "
         "<b>conservador</b> frente al riesgo específico de perder la carrera de IA en Legal — no es el peor "
         "caso, es el piso."],
        ["<b>0,64 → 0,342</b>",
         "El beta recalculado el 8-sep incorporando el pánico de IA de mayo-2026 bajó, no subió — el patrón "
         "inverso al de CME, TRI y CSU.TO ese mismo día. Habría sugerido más descuento, no menos. Felipe lo "
         "documentó y decidió no usarlo para reabrir el veredicto."],
        ["<b>Cero compras de insiders en 12 meses</b>",
         "Tras la caída del 27% desde máximos, ningún directivo compró con dinero propio — solo ventas mecánicas "
         "de LTIP vencidos. Ninguna señal de «esto está barato» viene de quien mejor conoce el negocio."]],
        [3.7*cm, 12.9*cm], font_sz=8.6)]
    o += [callout("LA TRAMPA",
        "Antes de seguir: este documento llegó al NO en dos tiempos, y conviene no confundirlos. El Paso 11 "
        "original, sin el veto del abogado del diablo, decía <b>NO COMPRAR TODAVÍA</b> — esperar a un precio o "
        "dato mejor. El Paso 10 encontró que esa redacción era generosa: la variable pendiente no es la "
        "paciencia, es si el moat de Legal sobrevive un ataque que el propio dossier no puede confirmar que está "
        "ganando. Por eso el veredicto se degradó a <b>NO</b>, el 4 de septiembre — antes de que existiera "
        "ningún ejercicio de beta. Lo que pasó el 8 de septiembre no es una segunda degradación: es la prueba de "
        "que el NO no dependía de ese dato para empezar, y sigue sin depender de él.")]
    return o + [PageBreak()]


def aviso_estado():
    o = flag_titulo("Aviso de estado", "Qué es definitivo en este documento y qué sigue pendiente de Felipe")
    o += [callout("PAUSA REFLEXIVA",
        "<b>Este es un veredicto PROVISIONAL en un único sentido —el mismo desde el 4 de septiembre.</b> Los "
        "pasos de círculo de competencia (Paso 1), monólogo previo (Paso 0) y percepción variante (Paso 7) "
        "quedan pendientes de que Felipe los complete o ratifique personalmente antes de considerar el "
        "veredicto definitivo — <b>especialmente si en algún momento implicara comprar</b>. Lo que sí es "
        "definitivo: el veto del abogado del diablo (Paso 10) ya se ejecutó en sesión limpia y sus objeciones "
        "fueron procesadas por escrito, como exige el método, y degradaron el veredicto provisional del Paso 11 "
        "de NO COMPRAR TODAVÍA a NO. Esa degradación es un producto del método, no un cajón de «vigilar» — queda "
        "documentada con sus falsadores en la última sección de este documento. El ejercicio de recálculo de "
        "beta del 8 de septiembre no reabrió ni tocó estos tres pasos pendientes: es una verificación adicional "
        "sobre el Paso 9 (valoración), documentada y resuelta sin cambiar el veredicto. Lo único que sigue "
        "pendiente es la ratificación personal de Felipe de esos tres pasos.")]
    return o + [PageBreak()]
