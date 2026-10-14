# -*- coding: utf-8 -*-
"""Portada · Resumen · Aviso de estado · §1 El negocio desde cero"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, kpi_panel, S, C, cm
from reportlab.platypus import Spacer, PageBreak, NextPageTemplate, Paragraph, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER


def portada():
    t_emp = ParagraphStyle("te", fontName="Serif-B", fontSize=36, leading=40, textColor=C["tinta"])
    t_tag = ParagraphStyle("tg", fontName="Serif-I", fontSize=13, leading=18.5, textColor=C["gris"])
    t_sec = ParagraphStyle("ts", fontName="Sans-B", fontSize=9, leading=12, textColor=C["rojo"])
    return [
        Spacer(1, 6.6 * cm),
        Paragraph("DATOS Y ANALYTICS PARA SEGUROS · ESTADOS UNIDOS · NASDAQ: VRSK", t_sec),
        Spacer(1, 10),
        Paragraph("Verisk Analytics", t_emp),
        Spacer(1, 6),
        Paragraph("El agente estadístico que las aseguradoras de EE.UU. no eligieron pero necesitan",
                  t_tag),
        Spacer(1, 4),
        Paragraph("Un foso dual —regulatorio y de red de datos— que ningún hecho muestra roto, un motor de "
                  "crecimiento que la propia fórmula desmiente, y un precio que ya paga buena parte del "
                  "escenario cauteloso. Monólogo de 12 pasos, con veto de abogado-diablo en sesión limpia.",
                  t_tag),
        Spacer(1, 1.5 * cm),
        kpi_panel([
            ("185,79 US$", "PRECIO DE REFERENCIA",
             "cierre 4-sep-2026 · HECHO de mercado en vivo,<br/>confirmado de forma independiente"),
            ("207-272 US$", "RANGO DE VALOR · CASO BASE",
             "DCF explícito a 10 años, WACC central<br/>7,1% · glide 5%→6%→4% terminal"),
            ("NO COMPRAR TODAVÍA", "VEREDICTO (PROVISIONAL)",
             "degradado por el Candado A desde<br/>«NO DECIDIBLE» · ver §14"),
        ]),
        Spacer(1, 0.9 * cm),
        tabla([["FECHA DE SÍNTESIS", "ESTADO DEL VEREDICTO", "REVISIÓN OBLIGATORIA"],
               ["4 de septiembre de 2026", "PROVISIONAL — Pasos 0, 1 y 7 pendientes de Felipe",
                "10-Q de Q3-2026 (~fines oct-2026)"]],
              [5.53 * cm] * 3, font_sz=8.8),
        Spacer(1, 0.55 * cm),
        M.p("<font size=8.3 color='#666054'><i>Documento de trabajo personal, método QG «Comprensión "
            "Primero con candado adversarial» (refundación 2026-07-19). Sintetiza tres dossiers de agente "
            "(hechos/knockouts; moat/scuttlebutt/gestión; transcripts/valoración/pares) más un veto de "
            "abogado-diablo ejecutado en sesión separada y limpia. Fuente primaria dominante: EDGAR, "
            "CIK 1442145 (10-K FY2021-FY2025, 10-Q, DEF 14A, 8-K). Quartr y Bigdata.com no estuvieron "
            "disponibles en esta síntesis. No es asesoramiento de inversión.</i></font>"),
        NextPageTemplate("Normal"), PageBreak(),
    ]


def resumen():
    o = flag_titulo("2 · El resumen en treinta segundos",
                     "Si solo lees una página, que sea esta")
    o += [p("<b>Verisk le dice a las aseguradoras de EE.UU. cuánto cobrar por una póliza y cuánto vale un "
            "siniestro.</b> Es agente estadístico designado o licenciado en los 50 estados, Puerto Rico y "
            "D.C. — un rol semi-oficial dentro del propio marco regulatorio, no solo comercial — y se sienta "
            "encima de una base acumulada de más de 38.900 millones de registros de transacciones, alimentada "
            "en 2025 por 3.600 millones de registros nuevos que las propias aseguradoras le envían. Más del "
            "80% de sus ingresos son suscripción anual o contratos plurianuales prepagados. Ningún knock-out "
            "binario dispara: ni VIE, ni SBC excesivo, ni ROIC estructural por debajo del WACC, ni "
            "restatement, ni dependencia de un cliente o regulador único, ni deuda tóxica.")]
    o += [p("<b>Pero el motor de crecimiento clásico no aplica aquí, y ese es el primer hallazgo real de este "
            "documento.</b> La fórmula ingenua (reinversión bruta 41% × ROIC ~33%) da un 13-14% de "
            "crecimiento. Lo que de verdad ocurrió, verificado línea por línea contra cinco años de 10-K, es "
            "5,8%-8,7% anual — y el capex de crecimiento real ronda cero en 2024-2025. Verisk crece casi sin "
            "capital nuevo, lo cual es fortaleza (negocio ultra <i>capital-light</i>) y vulnerabilidad a la "
            "vez: si el poder de fijación de precios se erosiona, no hay «más reinversión» que lo compense.")]
    o += [p("<b>La gestión muestra continuidad, no ruptura</b> — Lee Shavel, CEO desde 2022, fue CFO de la "
            "casa cinco años antes — pero también un episodio real de indisciplina de M&amp;A (AccuLynx: "
            "contratado, cancelado, pérdida de 33,9 M US$, litigio abierto) y un patrón de insiders 100% "
            "vendedores en 2026, todos bajo planes 10b5-1 suscritos meses antes. Ni una sola compra en "
            "mercado abierto localizada.")]
    o += [p("<b>El WACC bottom-up es sólido y cruzado por tres fuentes independientes: 6,8%-7,4%, central "
            "≈7,0-7,1%.</b> Con eso, el DCF explícito a 10 años da tres cajas — BEAR ≈125-130 US$, BASE "
            "≈207-272 US$, BULL ≈360-375 US$ — y el precio de hoy, 185,79 US$, cae <b>entre el caso BEAR y "
            "el caso BASE</b>, no dentro de él. El DCF inverso confirma por qué: al precio actual, el mercado "
            "solo exige crecer un 3,3%-4,0% anual durante 10 años — muy cerca del escenario pesimista, lejos "
            "del «algoritmo histórico» de 6-8% que la propia gerencia reivindica.")]
    o += [callout("PAUSA REFLEXIVA",
        "La pregunta que decide este documento no es «¿es Verisk un buen negocio?» — probablemente sí, con "
        "un moat real y un balance sano. Es otra: <b>¿la desaceleración de 2025-2026 es ruido cíclico sobre "
        "un moat intacto, o el inicio de una erosión estructural por IA que los datos históricos, por "
        "definición, todavía no pueden mostrar?</b> La asimetría cruda (recompensa ≈+24% contra riesgo "
        "≈-32%, ratio ≈0,75:1) solo se vuelve atractiva si se apuesta con fuerza por la primera lectura — y "
        "esa apuesta de probabilidad, no la aritmética del DCF, es lo que el resto de este documento pone a "
        "prueba.")]
    o += [hr(), p("<b>Las tres cifras que hay que retener:</b>")]
    o += [tabla([
        ["LA CIFRA", "QUÉ SIGNIFICA"],
        ["<b>&gt;80% frente a 3,3%-4,0%</b>",
         "Más del 80% de los ingresos son suscripción o contrato plurianual prepagado — la parte protegida "
         "por el moat. Y sin embargo, al precio de hoy, el mercado solo exige crecer 3,3%-4,0% anual a 10 "
         "años para justificar la acción. <b>Es una brecha entre lo sólido del negocio y lo poco que el "
         "precio ya le exige — y esa brecha puede leerse como oportunidad o como advertencia.</b>"],
        ["<b>31-37% frente a ≈0%</b>",
         "El ROIC agregado histórico de Verisk (31,7%-35,1% TTM/FY2025, cifra de tercero no reproducida "
         "línea por línea) frente al capex de crecimiento real estimado en 2024-2025: prácticamente nulo. "
         "<b>El motor g=reinversión×ROIC queda formalmente descartado como soporte del caso alcista</b> — "
         "el crecimiento no viene de reinvertir capital, viene de poder de fijación de precios sobre un "
         "dataset ya construido."],
        ["<b>0,75:1 → 0,75-1,05:1</b>",
         "La asimetría cruda del DCF bajo ponderación simétrica 50/50 entre «ruido cíclico» y «erosión "
         "estructural» es 0,75:1 — no atractiva. El veto de abogado-diablo obligó a corregir esa simetría "
         "hacia 55-60%/40-45%, lo que deja el rango en 0,75:1-1,05:1. <b>Sigue por debajo del umbral de "
         "atractivo (≥1,4:1) en todo el rango.</b>"]],
        [3.9 * cm, 12.7 * cm], font_sz=8.7)]
    return o


def aviso_estado():
    o = flag_titulo("3 · Aviso de estado del documento",
                     "Antes de leer una sola cifra: qué parte de esto es de Felipe y qué parte es de un agente")
    o += [callout("PAUSA REFLEXIVA",
        "<b>El veredicto de este documento es PROVISIONAL.</b> Los Pasos 0, 1 y 7 del método —los tres "
        "dominios donde el candado exige el juicio de Felipe sin apelación, no el de ningún agente— aparecen "
        "en este documento como borradores de agente, escritos DESPUÉS de investigar. Eso viola el propio "
        "requisito metodológico: el Paso 0 debe escribirse de memoria, ANTES de investigar; el Paso 1 es un "
        "veto sin apelación que solo Felipe puede pronunciar; el Paso 7 exige que Felipe articule una "
        "percepción variante con un dato propio, no una que el agente le proponga. <b>El resto del documento "
        "—Pasos 2 a 12, incluido el veto de abogado-diablo— es un registro completo y utilizable del proceso "
        "adversarial, pero no reemplaza esos tres pasos.</b>")]
    o += [p("Concretamente, esto es lo que falta y por qué importa:")]
    o += [tabla([
        ["PASO", "QUÉ EXIGE EL MÉTODO", "ESTADO EN ESTE DOCUMENTO"],
        ["0 · Monólogo previo", "Escrito de memoria, ANTES de leer ningún dossier — es el ancla contra la "
         "que se mide el delta final.",
         "Borrador de agente, escrito DESPUÉS de los tres dossiers. Placeholder de formato, a descartar."],
        ["1 · Círculo de competencia", "Veto sin apelación de Felipe: si no puede sostener la tesis del "
         "negocio con sus propias palabras, el documento se archiva como «NO», sin importar el resto.",
         "Frase propuesta para validar, editar o rechazar (§4). Ningún agente puede decidir esto."],
        ["7 · Percepción variante", "Un dato verificable y no público, articulado por Felipe, que explique "
         "por qué el consenso está mal dimensionado.",
         "Candidato propuesto (§10), con la advertencia honesta de que puede no ser tan variante como "
         "parece — ver DCF inverso."]],
        [3.1 * cm, 6.9 * cm, 6.6 * cm], font_sz=8.3)]
    o += [p("El delta genuino entre lo que Felipe pensaba antes de investigar y lo que este documento "
            "concluye después solo puede calcularse cuando Felipe escriba su propio Paso 0 — y se marca como "
            "pendiente en el Paso 11, no se fabrica. Lo que sí está cerrado y puede leerse como definitivo es "
            "el candado A: el veto de abogado-diablo (§13) se ejecutó en una sesión separada, con contexto "
            "limpio, recibiendo solo los hechos estructurados de este documento — no el entusiasmo acumulado "
            "de las tres sesiones de investigación que lo precedieron.")]
    return o


def s1_negocio():
    o = flag_titulo("4 · Qué hace Verisk, explicado desde cero",
                     "Cobra una suscripción anual por ser la fuente común que 50 reguladores estatales "
                     "y miles de aseguradoras aceptan sin discutir")
    o += [p("Imagina una aseguradora de auto en Ohio que necesita fijar la prima de una póliza nueva. Para "
            "hacerlo bien necesita saber, con precisión actuarial, cuánto cuesta reparar ese modelo de coche, "
            "cuál es la siniestralidad histórica de esa zona postal, y qué formulario de póliza cumple con la "
            "regulación de Ohio. Puede intentar construir todo eso sola — o puede suscribirse a quien ya lo "
            "construyó, lo mantiene actualizado, y lo tiene aceptado por el regulador desde hace décadas.")]
    o += [p("<b>Eso es Verisk: no vende seguros, vende el sistema nervioso de datos y formularios sobre el "
            "que corre la industria aseguradora estadounidense.</b> Su designación como «agente estadístico» "
            "—licenciada o nombrada en los 50 estados de EE.UU., Puerto Rico y D.C. (HECHO, 10-K FY2025, "
            "p.6)— no es una etiqueta de marketing: es un estatus dentro de cómo los reguladores aprueban "
            "tarifas de seguros. Las aseguradoras le envían sus datos de transacciones (3.600 millones de "
            "registros en 2025, sobre una base acumulada de más de 38.900 millones), y a cambio reciben "
            "benchmarks y modelos de pérdida que serían imposibles de construir en solitario.")]
    o += [p("<b>Cómo cobra.</b> Más del 80% de los ingresos de 2025 vinieron de suscripción anual o acuerdos "
            "de largo plazo, prepagados (HECHO, 10-K FY2025, p.5). El resto —aproximadamente el 17% del "
            "total— es transaccional: ligado a volumen de siniestros, y por tanto a la frecuencia de eventos "
            "climáticos severos. Esa distinción entre ingreso protegido por contrato e ingreso transaccional "
            "expuesto al ciclo es la columna vertebral de todo lo que sigue en este documento.")]
    o += [p("<b>Dos productos hacen el trabajo pesado.</b> Los formularios y tarifas ISO —el lenguaje común "
            "que reguladores y aseguradoras usan para redactar pólizas— y Xactimate, el software de "
            "estimación de daños de propiedad que se volvió estándar de facto entre ajustadores de siniestros "
            "y contratistas. Ninguno de los dos es difícil de copiar técnicamente; los dos son difíciles de "
            "desplazar porque están incrustados en el flujo de trabajo diario de miles de clientes (HECHO, "
            "10-K FY2025, p.4).")]
    o += [p("<b>Una corrección que hay que hacer antes de seguir, porque cambia cómo se lee cualquier tabla "
            "de crecimiento anterior a 2023.</b> Una verificación adversarial independiente de las cifras de "
            "ingresos encontró que la tabla de «ingresos totales» 2021-2022 de la investigación original en "
            "realidad medía el segmento Insurance, no los ingresos consolidados de la compañía esos años "
            "—cuando Energy, Financial Services y 3E todavía formaban parte del grupo, antes de ser "
            "vendidos—. Ambas cifras son HECHO; miden cosas distintas, y mezclarlas produce una tasa de "
            "crecimiento que no existió:")]
    o += [tabla([
        ["AÑO", "SEGMENTO INSURANCE (aislado)", "INGRESOS CONSOLIDADOS (con Energy/FS/3E)"],
        ["2021", "2.206,9 M US$", "2.462,5 M US$"],
        ["2022", "2.437,0 M US$", "2.497,0 M US$"],
        ["Variación 2021→2022", "+10,4% (segmento aislado — NO usar como crecimiento de la empresa)",
         "+1,4% (consolidado — la cifra correcta para leer «crecimiento de Verisk» esos años)"]],
        [4.6 * cm, 6.2 * cm, 5.8 * cm], font_sz=8.3)]
    o += [p("Ningún knock-out ni ninguna conclusión de valoración de este documento depende de esta "
            "corrección — pero se documenta aquí, con la misma disciplina HECHO/INFERENCIA/SUPUESTO que rige "
            "todo lo demás, porque tratar el segmento Insurance como si fuera «Verisk entero» habría inflado "
            "artificialmente el crecimiento pre-2023.")]
    o += [p("<b>Quién le paga, y qué tan concentrado está.</b> Los 50 mayores clientes representaron el 42% "
            "de los ingresos en 2025 (43% en 2024, 45% en 2023) — una tendencia de <i>des</i>concentración, "
            "no de dependencia creciente, y ningún cliente individual supera aproximadamente el 3% (HECHO, "
            "10-K FY2025, Nota 5). Es una base de clientes madura: el crecimiento futuro depende más de "
            "vender más productos a los clientes que ya tiene que de sumar logos nuevos y grandes.")]
    o += [hr(), p("<b>Paso 0 y Paso 1 del método — lo que Felipe debe validar, no un agente (ver Aviso de "
            "estado).</b> Se dejan aquí, en el lugar donde el negocio ya se ha explicado desde cero, para que "
            "la validación sea posible sin releer el documento entero.")]
    o += [p("<i>Paso 0 — monólogo borrador, PENDIENTE de Felipe:</i> «Verisk es la empresa que le dice a las "
            "aseguradoras de EE.UU. cuánto cobrar por una póliza y cuánto vale un siniestro, usando un "
            "dataset que lleva décadas construyendo y un rol semi-oficial ante 50 reguladores estatales. Gana "
            "dinero por suscripción anual a ese dataset y a software (Xactimate) que se volvió el estándar de "
            "facto, no vendiendo algo fácil de copiar. Dudaría de esto si: (a) la IA generativa logra "
            "construir un sustituto igual de bueno con datos más baratos, o (b) el ciclo de precios de "
            "seguros P&amp;C, hoy blando, resulta ser más que un ciclo.» Este texto es un intento de agente, "
            "escrito DESPUÉS de investigar — viola el requisito de que el Paso 0 se escriba de memoria, ANTES "
            "de investigar. Felipe debe descartarlo y escribir el suyo, o registrar explícitamente que ya "
            "tenía una tesis previa de julio-2026 bajo el sistema retirado que contamina cualquier intento "
            "retroactivo de «monólogo previo» limpio.")]
    o += [p("<i>Paso 1 — círculo de competencia, PENDIENTE de Felipe (veto sin apelación):</i> frase "
            "propuesta para validar, editar o rechazar: «Verisk gana dinero porque las aseguradoras de EE.UU. "
            "necesitan una fuente común y neutral de tarifas actuariales y formularios de póliza para operar "
            "dentro del marco regulatorio estatal, y pagan una suscripción anual por acceso a esa fuente y a "
            "las herramientas que se volvieron el estándar operativo de la industria (Xactimate para estimar "
            "daños de propiedad).» Si Felipe no puede sostener esta frase con sus propias palabras, el Paso 1 "
            "dispara STOP y el documento queda archivado como «NO — círculo de competencia», sin importar "
            "cuán sólido sea el resto.")]
    return o + [PageBreak()]
