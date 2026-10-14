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
        Spacer(1, 6.6*cm),
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
        Paragraph("No cobra por el dato: cobra por estar incrustado en cómo un abogado, un investigador o "
                  "una aseguradora ya hacen su trabajo todos los días. La pregunta de este documento no es "
                  "si el negocio es bueno — lo es — sino si el precio de hoy ya lo sabe.", t_tag),
        Spacer(1, 1.6*cm),
        kpi_panel([("£26,20", "PRECIO ACTUAL", "cotización de referencia<br/>usada en todo el documento (Paso 9)"),
                   ("£25,5-26,9", "VALOR INTRÍNSECO, CASO BASE", "WACC bottom-up 8,0%,<br/>reinversión conservadora"),
                   ("NO", "VEREDICTO", "tras el veto del abogado<br/>del diablo (Paso 10)")]),
        Spacer(1, 1.0*cm),
        tabla([["FECHA", "PRECIO", "VEREDICTO", "HORIZONTE DE TESIS"],
               ["4 de septiembre de 2026", "£26,20 (2.620p)", "NO", "10 años o más"]],
              [4.15*cm]*4, font_sz=9),
        Spacer(1, 0.5*cm),
        M.p("<font size=8.4 color='#666054'><i>Construido con el método QG de 12 pasos — «Comprensión Primero "
            "con candado adversarial» (refundación 2026-07-19) — sobre cinco Form 20-F (FY2021-FY2025) y "
            "Exhibit 15.2 de fuente primaria EDGAR, con veto del abogado del diablo en sesión limpia (Paso 10) "
            "y WACC construido bottom-up desde beta de mercado, nunca heredado de un tier de calidad. Documento "
            "de trabajo personal. No es asesoramiento de inversión.</i></font>"),
        NextPageTemplate("Normal"), PageBreak()]


def resumen():
    o = flag_titulo("El resumen en treinta segundos", "Si solo lees una página, que sea esta")
    o += [p("<b>RELX es un negocio excelente al que no le sobra margen de seguridad, y la respuesta de este "
        "documento es NO.</b> No «todavía no» — NO, con condiciones de reapertura explícitas y fechadas. "
        "Cuatro segmentos (Risk, Legal, STM, Exhibitions) cobran a profesionales por acceso a bases de datos "
        "propietarias y a las herramientas de trabajo incrustadas en cómo ya usan esos datos cada día: la "
        "biblioteca paga, no el investigador; la aseguradora consulta un histórico que ella misma alimentó; "
        "el abogado no puede permitirse citar mal un caso. Ningún knock-out se dispara en cinco ejercicios "
        "fiscales revisados, el ROIC sube todos los años desde 2021, y el margen operativo ajustado se expande "
        "sin excepción desde 2020.")]
    o += [p("<b>Y aun así, el precio de hoy no compensa el riesgo que queda abierto.</b> No porque el negocio "
        "esté roto — el test de trampa de valor lo descarta con fuerza — sino porque, calculado con un WACC "
        "construido correctamente desde el mercado (7,5-8,5%, no heredado de ningún tier de calidad), el caso "
        "base cae dentro de un ±3% del precio actual, y la asimetría honesta es desfavorable: el escenario "
        "bajista (-37%) pesa más que el alcista razonable (+11% a +18%).")]
    o += [p("<b>El motivo de fondo no es un múltiplo caro. Es un test que sigue abierto.</b> En 2009, Google "
        "Scholar regaló la jurisprudencia y RELX sobrevivió moviendo el moat del texto al citador y a las "
        "herramientas de análisis. Diecisiete años después, Thomson Reuters compró Casetext y lanzó CoCounsel "
        "para intentar lo mismo con IA generativa, y el único dato comparativo disponible hoy —la guía que "
        "Thomson Reuters ya subió para 2026— corta en contra de RELX, no a favor. Eso no prueba que RELX esté "
        "perdiendo la carrera. Prueba que nadie, ni este documento, puede decir hoy que la está ganando.")]
    o += [p("<b>Y hay una ausencia que pesa en el momento exacto en que más debería pesar.</b> Tras la caída "
        "del 27% desde máximos de 52 semanas, ningún directivo compró acciones con dinero propio en los "
        "últimos doce meses — solo ventas mecánicas de sell-to-cover. No es una señal bajista por sí sola, "
        "pero es consistente con un precio en zona razonable, no de oportunidad.")]
    o += [callout("PAUSA REFLEXIVA",
        "La pregunta que decide este documento no es «¿es RELX un buen negocio?» — lo es, con moat real "
        "evidenciado en episodios concretos que sobrevivió. Es: <b>¿compensa el precio de hoy la incertidumbre "
        "genuina de si ese moat sobrevive su segunda prueba?</b> Con la información disponible el 4 de septiembre "
        "de 2026, el cálculo de este mismo dossier dice que no. Confundir «negocio de calidad» con «comprable a "
        "cualquier precio» es, en este método, exactamente el error que el candado adversarial existe para atrapar.")]
    o += [hr(), p("<b>Las cifras que hay que retener:</b>")]
    o += [tabla([
        ["LA CIFRA", "QUÉ SIGNIFICA"],
        ["<b>-3% a +3%</b>",
         "Dónde cae el caso base del DCF (£25,5-26,9) frente al precio de hoy (£26,20), con el WACC construido "
         "correctamente. No hay descuento limpio: el precio ya sabe casi todo lo que este documento sabe."],
        ["<b>-37% frente a +11%/+18%</b>",
         "La asimetría real: el caso bajista genérico de madurez pesa más que el caso alcista razonable. Y el "
         "propio abogado del diablo encontró que ese -37% probablemente es <b>conservador</b> frente al riesgo "
         "específico de perder la carrera de IA en Legal — no es el peor caso, es el piso."],
        ["<b>10% frente a ~9,5-10%</b>",
         "Crecimiento subyacente de LexisNexis Legal en H1'26 frente a la guía que Thomson Reuters ya subió para "
         "su segmento Big-3 en 2026. Van empatados hoy — pero es la única carrera del dossier que sigue abierta, "
         "y el trading update de RELX de noviembre de 2026 la decide."],
        ["<b>Cero compras de insiders en 12 meses</b>",
         "Tras la caída del 27% desde máximos, ningún directivo compró con dinero propio — solo ventas mecánicas "
         "de LTIP vencidos. Ninguna señal de «esto está barato» viene de quien mejor conoce el negocio."]],
        [3.7*cm, 12.9*cm], font_sz=8.8)]
    o += [callout("PAUSA REFLEXIVA",
        "Antes de seguir: este documento llegó aquí en dos tiempos. El Paso 11 original, sin el veto del "
        "abogado del diablo, decía <b>NO COMPRAR TODAVÍA</b> — esperar a un precio o dato mejor. El Paso 10 "
        "encontró que esa redacción era generosa: la variable pendiente no es la paciencia, es si el moat de "
        "Legal sobrevive un ataque que el propio dossier no puede confirmar que está ganando. Por eso el "
        "veredicto se degradó a <b>NO</b>, con condiciones de reapertura explícitas — no es un cajón cerrado, "
        "es una puerta con llave y con la combinación escrita en la última sección.")]
    return o + [PageBreak()]


def aviso_estado():
    o = flag_titulo("Aviso de estado", "Qué es definitivo en este documento y qué sigue pendiente de Felipe")
    o += [callout("PAUSA REFLEXIVA",
        "<b>Este es un veredicto PROVISIONAL.</b> Los pasos de círculo de competencia (Paso 1), monólogo previo "
        "(Paso 0) y percepción variante (Paso 7) quedan pendientes de que Felipe los complete o ratifique "
        "personalmente antes de considerar el veredicto definitivo — <b>especialmente si en algún momento "
        "implicara comprar</b>. Lo que sí es definitivo: el veto del abogado del diablo (Paso 10) ya se ejecutó "
        "en sesión limpia y sus objeciones fueron procesadas por escrito, como exige el método, y degradaron el "
        "veredicto provisional del Paso 11 de NO COMPRAR TODAVÍA a NO. Esa degradación es un producto del "
        "método, no un cajón de «vigilar» — queda documentada con sus falsadores en la última sección de este "
        "documento. Lo único que sigue pendiente, y lo único que sigue pendiente, es la ratificación personal "
        "de Felipe de esos tres pasos.")]
    return o + [PageBreak()]
