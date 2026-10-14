# -*- coding: utf-8 -*-
"""10 · Qué creo distinto del consenso · 11 · El pre-mortem"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, cm
from reportlab.platypus import PageBreak, Spacer

def s10_percepcion():
    o = flag_titulo("10 · Qué creo distinto del consenso",
                    "Percepción variante genuina de Felipe (Paso 7) — BORRADOR DE AGENTE, pendiente de ratificación personal")
    o += [callout("PAUSA REFLEXIVA",
        "<b>[BORRADOR DE AGENTE — PENDIENTE DE QUE FELIPE LO ESCRIBA O RATIFIQUE PERSONALMENTE. NO ES SU JUICIO "
        "REAL.]</b><br/><br/>"
        "Propuesta tentativa a ratificar, corregir o descartar por Felipe: <i>«La percepción variante candidata "
        "no es 'el mercado subestima a CME' — es la inversa. El mercado, vía un beta de 0,27 (un outlier "
        "incluso dentro de su propio sector: ICE 0,93, NDAQ 0,97, CBOE 0,41), estaba pagando por una "
        "covarianza con el mercado tan baja que rayaba en lo implausible — un WACC de ~5,9% dejaba el spread "
        "entre el coste de equity y el coste de la propia deuda AA- de CME en menos de 1 punto porcentual, algo "
        "que no debería sostenerse para el acreedor residual de la empresa.<br/><br/>"
        "Lo que la corrección del 8-sep confirma, con una investigación que no había leído esta tesis antes, es "
        "exactamente esa sospecha: el 'descuento' de −37,9% que arrojaba un DCF con ese beta no era una "
        "oportunidad real sino un artefacto de medición, y la variante genuina sigue siendo: 'este no es un "
        "compounder barato, es un compounder de calidad probada cotizando cerca de su valor razonable corregido "
        "(338,79 US$), con la ventana de entrada dictada por el gate de precio (235/200) y ahora también por un "
        "gatillo de valoración recalculado (237,15 US$) que converge con él, no por un error de mercado que ya "
        "haya sido explotado.'»</i>")]
    o += [chart("charts/03_beta_pares.png")]
    o += [p("El gráfico ya incorpora la corrección de hoy: la barra roja de la derecha es el beta que este "
        "documento usa para decidir (0,65), construido como el promedio simple de los cuatro pares y validado "
        "de forma cruzada contra el beta sectorial de Damodaran (0,66) — dos fuentes independientes convergiendo "
        "en el mismo número. La distancia entre el beta crudo de CME (0,27) y el resto del grupo —tan grande "
        "como la distancia entre CBOE y sus pares más caros en riesgo (ICE, NDAQ)— es la evidencia visual de "
        "por qué esta corrección no era opcional.")]
    o += [p("<b>Por qué este paso queda marcado como borrador y no como conclusión:</b> el método exige que la "
        "percepción variante sea el juicio propio de Felipe, formado con independencia del entusiasmo de la "
        "sesión de investigación — exactamente el sesgo que el abogado del diablo existe para auditar desde "
        "fuera, en las dos rondas que ya se ejecutaron (secciones 12 y 13). Adoptar la propuesta del agente sin "
        "pasarla por ese filtro personal repetiría, en una escala más pequeña, el mismo problema que el método "
        "corrige en el Paso 0 y el Paso 1: sustituir el juicio de Felipe por el de quien investigó — algo que ni "
        "siquiera dos validaciones adversariales convergentes deberían dispensar.")]
    # Sin PageBreak aquí a propósito: la sección 10 es corta y forzarlo dejaba
    # ~85% de la página en blanco antes de la 11. Se deja fluir.
    return o

def s11_premortem():
    o = flag_titulo("11 · El pre-mortem",
                    "Cuatro mecanismos específicos del arquetipo exchange/clearing, cada uno con métrica observable y fecha — escritos antes de decidir el veredicto")
    o += [p("Ninguno de los cuatro mecanismos siguientes es del tipo «podría bajar el margen». Todos tienen una "
        "métrica concreta, un umbral numérico y una ventana temporal, escritos antes de fijar el veredicto de "
        "la sección 14 para que no puedan amoldarse al resultado.")]
    o += [tabla([
        ["#", "EL MECANISMO", "MÉTRICA OBSERVABLE", "VENTANA"],
        ["1", "<b>Fragmentación sostenida de liquidez en el producto ancla</b> (SOFR/Treasuries) por un rival "
              "con cross-margining suficiente. Distinto del ataque de fee bajo temporal ya fallido en abr-2025: "
              "el riesgo real es un consorcio con bolsillos profundos subsidiando liquidez durante años, no semanas.",
         "Share de ADV de SOFR futures de FMX (u otro rival) sostenido &gt;5% durante 2 trimestres consecutivos, "
         "o caída abrupta del ahorro de margen diario reportado (hoy ~95.000 M US$/día)",
         "Próximos 4-6 trimestres<br/>(hasta medio 2027)"],
        ["2", "<b>Desintermediación regulatoria vía mercados de predicción</b> (Kalshi) operando fuera del "
              "régimen de márgenes SPAN. La propia gerencia lo calificó de riesgo sistémico, no sólo competitivo.",
         "Resolución adversa del litigio CFTC sobre el contrato de crudo 24/7, o pérdida de exclusividad "
         "regulatoria de CME en mercados de eventos/predicción",
         "Próximos 12 meses<br/>(litigio en curso)"],
        ["3", "<b>Normalización del régimen de «incertidumbre»</b> que sostiene el crecimiento reciente. En "
              "9 de 9 trimestres analizados (feb-2023 a jul-2026), la gerencia atribuyó el crecimiento de "
              "volumen casi exclusivamente a incertidumbre macro/geopolítica/de tasas, nunca a ganancia "
              "estructural de cuota.",
         "ADV/interés abierto interanual cae de forma sostenida por debajo de +3% durante 2 o más trimestres "
         "consecutivos",
         "16-nov-2026 o los<br/>dos trimestres siguientes"],
        ["4", "<b>La concentración de clearing firm</b> (patrón recurrente de línea base, ≥10% en 4 de los "
              "últimos 6 años) se convierte en apalancamiento de negociación real.",
         "Ingresos de clearing &amp; transaction fees por contrato caen mientras el ADV sube (compresión de "
         "take rate divorciada del volumen)",
         "Próximos 2-3 años fiscales<br/>(10-K FY2026, ~feb-2027)"]],
        [0.6*cm, 7.6*cm, 5.7*cm, 2.7*cm], font_sz=7.4)]
    o += [p("<b>Nota de verificación abierta sobre el mecanismo 4:</b> los hechos disponibles no permiten saber "
        "si la concentración corresponde al mismo cliente acumulando año a año o a clientes distintos rotando "
        "— brecha declarada por el abogado del diablo en el Paso 10, sin resolver.")]
    o += [callout("DATO CURIOSO",
        "El mecanismo 1 de este pre-mortem —fragmentación sostenida de liquidez por un rival con bolsillos "
        "profundos— es, en sustancia, la misma amenaza que la actualización de hoy usó para justificar por qué "
        "el beta de CME no podía quedarse en 0,27. Un pre-mortem bien escrito y un WACC bien construido deberían "
        "mirar en la misma dirección: si un mecanismo aparece en el pre-mortem como riesgo con mecanismo y "
        "fecha, el coste de capital no puede tratarlo como si no existiera. Esa es, en una frase, la corrección "
        "de hoy.")]
    o += [hr(), p("<b>Filtro Munger, aplicado antes del veredicto:</b>")]
    o += [tabla([
        ["EJE", "LECTURA"],
        ["Invertir el problema<br/>(¿cómo destruiría yo este negocio?)",
         "Subsidiaría liquidez de forma sostenida (años, no meses) en el producto ancla con capital de bolsillos "
         "profundos, mientras cabildeo para que un vehículo tipo mercado de predicción opere fuera del régimen "
         "de márgenes SPAN — atacando simultáneamente ambos candados del moat. El test de estrés de abril de "
         "2025 sugiere que esto no ha funcionado hasta ahora, pero duró una semana, no años."],
        ["Redundancia",
         "Financiera, alta (D/EBITDA ≈0,8x, AA-/Aa3, covenants con margen amplio). Regulatoria, más frágil: la "
         "designación SIFMU es simultáneamente un activo y una dependencia sin «backup» si el régimen cambia."],
        ["Punto de no retorno",
         "Si el share de un producto ancla migra de forma sostenida más allá de cierto umbral (no observado hoy "
         "— FMX en 0,3%), el efecto de red se revierte y es estructuralmente difícil de recuperar. El propio "
         "precedente de CME contra LCH SwapClear en USD IRS (98% de share retenido por el incumbente) confirma "
         "que el mecanismo protege a quien tiene el pool hoy, no a CME por naturaleza."]],
        [3.8*cm, 12.8*cm], font_sz=8.3)]
    # Sin PageBreak aquí a propósito: la tabla del pre-mortem termina a ~30%
    # de la página y forzarlo dejaba el resto en blanco antes de la sección 12.
    return o
