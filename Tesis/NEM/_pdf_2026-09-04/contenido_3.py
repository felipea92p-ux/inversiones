# -*- coding: utf-8 -*-
"""§8 gestión e incentivos · §9 knockouts · §10 percepción variante · §11 pre-mortem"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, cm
from reportlab.platypus import PageBreak

def s8_gestion():
    o = flag_titulo("8 · La gestión: quién manda, cómo cobra, y una coincidencia que merece pregunta",
                    "Ninguna prueba de fraude. Sí una decisión de capital enorme, financiada con deuda, en el peor momento narrativo posible")
    o += [p("<b>Estructura de propiedad.</b> La familia fundadora controla el 45,07% de los derechos de voto a "
        "través de la <i>GVN Familienstiftung</i> —una minoría de bloqueo de facto sobre cualquier decisión que "
        "requiera mayoría cualificada. El 2 de julio de 2026, Georg Nemetschek transfirió acciones a esa fundación "
        "<b>sin contraprestación</b>, justo antes del cierre de HCSS. La prensa lo leyó como un anclaje defensivo "
        "de control ante una posible opa —una interpretación de prensa, no una declaración oficial de motivo, y "
        "digna de la pregunta explícita: <b>¿qué sabía la familia sobre la vulnerabilidad del precio en ese "
        "momento?</b> Este documento no tiene evidencia para responderla; sólo para plantearla.")]
    o += [p("<b>Continuidad ejecutiva.</b> El CEO Padrines y la CFO Öfverström renovaron contrato hasta 2028 —señal "
        "de estabilidad, sin cambios de equipo en medio de la mayor operación de la historia del grupo.")]
    o += [p("<b>Voto de descarga de responsabilidad (AGM, 21-may-2026): 97,17% a favor.</b> Pero esta votación "
        "ocurrió <b>antes</b> del grueso de la caída bursátil de verano y antes del cierre de HCSS, por lo que "
        "no debe leerse como un voto de confianza sobre la decisión de capital más reciente y más controvertida "
        "del año —es un voto sobre un año anterior, no sobre este.")]
    o += [p("<b>La decisión de asignación de capital más relevante del período: HCSS.</b> $2.400 millones, "
        "aproximadamente 20 veces el EBITDA 2025 de la comprada —la mayor adquisición de la historia del grupo, "
        "cuestionada abiertamente por el mercado en cuanto a precio, factor citado explícitamente por la prensa "
        "financiera alemana como uno de los motores de la caída. La estructura de joint venture con Thoma Bravo "
        "(72% Nemetschek / 28% Thoma Bravo) reduce el desembolso de caja inmediato —aproximadamente $1.000 "
        "millones reales frente a los $2.400 millones de valor de empresa— pero también diluye la propiedad total "
        "del segmento de mayor crecimiento del grupo y crea un socio de private equity con su propio horizonte de "
        "salida. <b>El mecanismo de liquidez futuro de Thoma Bravo no está documentado en las fuentes "
        "disponibles</b> —una incógnita abierta que el §13 debía presionar y no cerró del todo.")]
    o += [p("<b>Compras con dinero propio:</b> ver §6 —señal positiva pero modesta (consejeros de supervisión, no "
        "ejecutivos, ~90-100 mil € cada uno), con precedente de mal timing en la misma compañía, y sin ninguna "
        "compra ejecutiva documentada en 2026.")]
    o += [hr(), p("<b>El filtro Munger, obligatorio antes de cualquier veredicto:</b>")]
    o += [tabla([
        ["EJE", "LECTURA"],
        ["<b>Incentivos</b>",
         "Compensación ejecutiva vía SAR/LTIP (equity, dilución mínima: 1%-3,5% del FCF) —razonablemente alineada. "
         "Pero ninguna compra en mercado abierto del CEO o la CFO con dinero propio en 2026: un vacío real, no un "
         "relleno con inferencia optimista. El control familiar (45% de voto) reduce el riesgo de agencia clásico "
         "pero también reduce la influencia de los accionistas minoritarios."],
        ["<b>Invertir el problema</b>",
         "Si quisiera diseñar el escenario que hace fracasar esta tesis, haría exactamente lo que Nemetschek ya "
         "hizo: pagar ~20 veces EBITDA por la mayor adquisición de su historia, financiada con deuda nueva, justo "
         "cuando el segmento más rentable entra en una transición de varios años calificada de difícil por la "
         "propia dirección, en medio de una repreciación sectorial de software por riesgo de IA. <b>El escenario "
         "adverso no es hipotético: ya está parcialmente en marcha.</b>"],
        ["<b>Redundancia</b>",
         "El balance mostró capacidad real de desapalancarse rápido en 2024-2025 (deuda neta de −294,6 M € a "
         "−107,5 M € en un año, gracias a un FCF pre-M&amp;A de 389,5 M €) —margen de maniobra demostrado, no sólo "
         "prometido. Ese margen se pondrá a prueba de nuevo con los ~450-527 M € adicionales de deuda por HCSS."],
        ["<b>Punto de no retorno</b>",
         "El cierre de HCSS (1-jul-2026) es irreversible. El capital ya está comprometido —aunque parcialmente en "
         "papel/JV, no todo en caja— y el socio Thoma Bravo tiene su propio horizonte de salida sobre el 28% del "
         "segmento combinado: una incógnita de estructura de capital futura que sigue sin resolver."]],
        [3.0*cm, 13.6*cm], font_sz=8.4)]
    return o + [PageBreak()]

def s9_knockouts():
    o = flag_titulo("9 · Los seis knockouts binarios",
                    "Ninguno se activa. El punto de mayor tensión real no está en esta lista")
    o += [tabla([
        ["KNOCKOUT", "VEREDICTO", "EVIDENCIA"],
        ["VIE (entidad de interés variable)", "NO SE ACTIVA",
         "HECHO — consolidación por control accionarial directo; HCSS será ~72% Nemetschek / 28% Thoma Bravo como "
         "minoritario directo, no un VIE contractual."],
        ["SBC &gt; 50% del FCF ajustado, ≥3 años", "NO SE ACTIVA por margen enorme",
         "HECHO (gasto SAR) + inferencia con piso de resolución 1%-3,5% del FCF cada año (AR 2023/2024/2025)."],
        ["ROIC &lt; WACC estructural, ≥3 años", "NO SE ACTIVA, ni cerca",
         "Inferencia propia: ROIC 20%-30% en todos los años vs. WACC bottom-up del propio emisor 7%-14% "
         "(AR 2021-2025, notas de goodwill)."],
        ["Restatement / contabilidad no fiable", "NO SE ACTIVA en el sentido que busca el knockout",
         "HECHO — ajuste técnico de fondo de comercio 2021 dentro del plazo IFRS 3 de 12 meses, no un IAS 8; "
         "auditoría sin salvedades los 5 años. Mancha menor de transparencia, no señal de fraude."],
        ["Dependencia de cliente/regulador único", "NO SE ACTIVA",
         "HECHO, declaración explícita y repetida en 5 informes: “no significant concentration of credit risks "
         "with any single customer”."],
        ["Deuda tóxica", "NO SE ACTIVA",
         "HECHO — préstamo sindicado + Schuldschein plain-vanilla, covenants cumplidos, desapalancando activamente "
         "en 2025 (deuda neta −294,6 M € → −107,5 M € en un año)."]],
        [3.5*cm, 3.2*cm, 9.9*cm], font_sz=7.9)]
    o += [callout("LA TRAMPA",
        "<b>El punto de mayor tensión real no está en la lista de knockouts.</b> La concentración de fondo de "
        "comercio más intangibles —aproximadamente dos tercios del balance— y el colchón estrecho de 59,7 M € en el "
        "test de deterioro 2025 de la división Manage (sensible a +3,4 puntos de WACC o a una caída del 49,8% del "
        "flujo terminal) no disparan ningún knockout. Pero ambos son focos legítimos de vigilancia: el §11 los "
        "convierte en mecanismos de pre-mortem con fecha concreta.")]
    return o + [PageBreak()]

def s10_percepcion():
    o = flag_titulo("10 · Percepción variante (borrador de agente — pendiente de Felipe)",
                    "Una hipótesis candidata a probar, no una convicción — y el propio Paso 9/10 la complican")
    o += [callout("PAUSA REFLEXIVA",
        "<b>[Paso 7 del método — BORRADOR DE AGENTE. Esto NO es la convicción real de Felipe; es un intento de un "
        "agente de simular el ejercicio para que Felipe lo sustituya por el suyo antes de que este documento "
        "pueda tratarse como completo.]</b>")]
    o += [p("La hipótesis candidata: el mercado podría estar fusionando dos señales que la evidencia de "
        "scuttlebutt (§6) sugiere que son distintas —<b>(a)</b> una re-valoración sectorial del software por "
        "riesgo de disrupción de IA, que es real y no descartable, con <b>(b)</b> un deterioro operativo "
        "idiosincrático de Nemetschek, del cual no se encontró evidencia en 9 trimestres de transcripts ni en el "
        "desempeño de los cuatro pares del mismo trimestre. <b>Si esa fusión de señales es un error del mercado, "
        "hay una brecha de percepción explotable.</b>")]
    o += [p("Pero el §12 (y ahora el §13) complican esta hipótesis de forma importante: el WACC que el propio "
        "mercado parece exigir hoy (10,7%-11,9%) coincide sorprendentemente bien con el WACC que el propio "
        "emisor usa internamente para su test de deterioro de fondo de comercio (7%-14%, con los años recientes "
        "2022-2025 en el tramo 9,9%-13,9%). <b>Es decir: puede que el mercado no esté cometiendo un error de "
        "fusión de señales, sino que esté precificando correctamente un riesgo que el CAPM con beta histórico de "
        "XETRA simplemente no captura bien, por baja liquidez del papel.</b>")]
    o += [p("<b>Felipe debe decidir, con su propio juicio, cuál de las dos lecturas cree y por qué —este "
        "documento no puede tomar esa decisión por él.</b> El §13 deja este dilema sin resolver a favor de la "
        "lectura optimista: la carga de la prueba se desplazó hacia quien sostenga (a), y ese desplazamiento es "
        "en sí mismo el hallazgo más importante del veto del abogado del diablo.")]
    return o + [PageBreak()]

def s11_premortem():
    o = flag_titulo("11 · Pre-mortem: seis mecanismos, con fecha",
                    "Escrito con métrica y ventana, no con vaguedad — para que no pueda amoldarse al resultado")
    o += [tabla([
        ["#", "EL MECANISMO", "CÓMO SE MIDE", "VENTANA"],
        ["1", "<b>Impairment/desaceleración en Build &amp; Construct (HCSS).</b> Falsificaría la promesa explícita "
              "de la CFO (“accretive by 2028”).",
         "Cualquier deterioro de fondo de comercio de HCSS/GoCanvas, o crecimiento orgánico combinado del segmento "
         "por debajo de dígito único alto durante dos trimestres seguidos en 2027-2028.",
         "Informes FY2026-FY2028"],
        ["2", "<b>Fracaso de la transición de suscripción en Design.</b> El “año difícil” declarado se convertiría "
              "en estancamiento estructural, no transición ordenada.",
         "Mezcla de suscripción en Design por debajo del ~90% objetivo a cierre de 2027, o crecimiento orgánico de "
         "Design por debajo de dígito único medio dos trimestres seguidos en 2027.",
         "Trimestres de 2027, confirmado en FY2027 (~mar-2028)"],
        ["3", "<b>Impairment en la división Manage.</b> El colchón más estrecho de las cuatro divisiones "
              "(59,7 M €, FY2025) se materializa.",
         "Cualquier cargo de deterioro de fondo de comercio de Manage en el informe anual.",
         "FY2026 (~mar-2027) y FY2027 (~mar-2028)"],
        ["4", "<b>Tensión de apalancamiento post-HCSS.</b> El desapalancamiento rápido de 2024-2025 no se repite "
              "con una adquisición 3-4 veces mayor.",
         "Deuda neta pro-forma por encima de 550-700 M € en el informe FY2026, o necesidad de ampliar capital / "
         "renegociar covenants dentro de los 24 meses posteriores al cierre de HCSS (antes de jul-2028).",
         "Informes FY2026-FY2027"],
        ["5", "<b>Disrupción de IA nativa (vigilancia, no núcleo).</b> El “riesgo narrativo” se confirma como "
              "estructural, no como pánico transitorio.",
         "Evidencia verificable de un competidor nativo de IA capturando cuota material, o desaceleración del ARR "
         "de NEM por debajo de dígito doble bajo mientras los pares aceleran.",
         "2027-2028, vigilancia continua"],
        ["6", "<b>Erosión generacional del talento BIM</b> (añadido tras §13). El supuesto no verificado del §5 "
              "pasaría de SUPUESTO a HECHO.",
         "Encuesta de adopción de software en programas de arquitectura/ingeniería angloparlantes (tipo NAAB/AIA "
         "o equivalente europeo) mostrando &gt;70% de escuelas usando Revit/Autodesk como estándar.",
         "2026-2027, sin informe único — hoy no localizada en este dossier"]],
        [0.6*cm, 6.1*cm, 7.0*cm, 2.9*cm], font_sz=7.5)]
    o += [callout("LECCIÓN TRANSFERIBLE",
        "Fíjate en la asimetría de estos seis mecanismos: <b>ninguno tiene ya un dato confirmado en su contra</b> "
        "—a diferencia de otros pre-mortems de esta casa donde parte del escenario adverso ya estaba ocurriendo "
        "con dato en la mano. Aquí los seis son condiciones futuras, con ventana, no señales ya activas. Eso no "
        "los hace menos reales: los hace, todavía, no confirmados. La única pieza que <i>sí</i> ya está activa hoy "
        "vive en la valoración (§12), no en el negocio —y por eso el veredicto (§14) pesa la valoración con más "
        "fuerza que el pre-mortem operativo.")]
    return o + [PageBreak()]
