# -*- coding: utf-8 -*-
"""5. Gestión e incentivos · 6. Knock-outs · 7. Percepción variante · 8. Pre-mortem"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, cm
from reportlab.platypus import PageBreak


def s5_gestion():
    o = flag_titulo("5 · Gestión e incentivos",
                     "Lo que de verdad mide la compensación, y una ventana de gobierno de 2,5 "
                     "meses que nadie explicó por escrito")
    o += [p("<b>Qué mide realmente la compensación.</b> El bono anual = salario base × factor de "
        "desempeño de la empresa × factor individual, donde el factor de empresa se determina por "
        "<b>ROIC y crecimiento de ingreso neto</b> — nunca por crecimiento de ingresos sin más ni "
        "por precio de la acción [MIC 2026, p.12-13]. Candado duro: en todos los Grupos "
        "Operativos salvo uno, se descuenta una tasa libre de riesgo (5%) del ROIC antes de "
        "calcular el bono — sin superar ese umbral, no hay bono. <b>El 75% del bono neto de "
        "impuestos</b> debe invertirse obligatoriamente en acciones, en escrow mínimo 4 años.")]
    o += [p("<b>Evidencia de pay-for-performance con cifra propia de la empresa:</b> la "
        "compensación de los NEO (altos ejecutivos designados) subió +39% entre 2020 y 2025, "
        "frente a un TSR (retorno total al accionista) de +106% en el mismo periodo — los "
        "ejecutivos capturaron menos de la mitad del crecimiento de valor generado. Los bonos de "
        "los NEO (salvo Presidente y CFO) están atados al ROIC del Grupo Operativo específico que "
        "dirigen, no al de la Corporación completa — evita que un ejecutivo se beneficie del "
        "trabajo ajeno.")]
    o += [p("<b>Sucesión, con fecha exacta verificada dos veces</b> (dossier original + "
        "adversarial, cero discrepancias): Leonard renunció como Presidente el <b>25 de "
        "septiembre de 2025</b>; Miller fue nombrado Presidente el mismo día. Leonard no se "
        "postuló a reelección al Consejo en la AGM del 15 de mayo de 2026, pero asistió a 9 de 10 "
        "reuniones del Consejo durante todo FY2025 y sigue como asesor, <i>«con un foco particular "
        "en apoyar la estrategia de Accionista Minoritario Permanentemente Comprometido de la "
        "Corporación»</i> — es decir, queda enganchado al lado más nuevo y menos probado del "
        "modelo (participaciones minoritarias tipo Asseco), no a la máquina de adquisiciones "
        "tradicional. Leonard renunció voluntariamente a todo salario y bono en 2023-2025 "
        "(compensación NIL).")]
    o += [callout("LA TRAMPA",
        "<b>Gobernanza inusual en la transición.</b> Miller <b>no era miembro del Consejo</b> "
        "cuando asumió la Presidencia — no se presentó a reelección el 13 de mayo de 2025 y fue "
        "nombrado al Consejo recién el <b>9 de diciembre de 2025</b>, más de dos meses después de "
        "asumir el cargo. Ventana de ~2,5 meses en que el nuevo Presidente operó <b>sin asiento "
        "formal</b> en el Consejo que supervisa la asignación de capital — sin explicación "
        "documentada del motivo.")]
    o += [p("<b>Perfil de Miller:</b> cofundó Trapeze Group en 1988, primera adquisición de CSI en "
        "1995; más de 30 años con CSI/Volaris — no es un outsider, es historia fundacional de la "
        "máquina misma. Su compensación reportada de 2025 (aún como Executive Chairman de Volaris) "
        "fue <b>menor</b> que en 2024 y 2023 — bajó el año en que fue ascendido. <b>Renunció "
        "voluntariamente a todo salario y bono con efecto desde el 1 de enero de 2026</b> — "
        "trabaja hoy por cero compensación en efectivo, igual que Leonard antes. Su «skin in the "
        "game» viene de tenencia previa: 254.533 acciones comunes de CSI (~1,2% de la compañía) "
        "más participaciones sustanciales en Topicus.com y Lumine Group — no se puede establecer "
        "<i>cuándo</i> las construyó ni a qué precio (SEDI bloqueado, laguna).")]
    o += [p("<b>Matiz sobre riesgo «key man» puro.</b> El hurdle rate y la aprobación de "
        "adquisiciones no son prerrogativa personal del Presidente — son responsabilidad explícita "
        "del Consejo (<i>«Ajustar periódicamente los hurdle rates... Revisar y aprobar todas las "
        "adquisiciones de negocio por encima de ciertos umbrales»</i>, Board Mandate), y el Chief "
        "Investment Officer lleva en la casa desde 1995 — 30 años de continuidad institucional en "
        "la función de originación, independiente de quién ocupe la Presidencia. Esto no elimina "
        "el riesgo de sucesión (el juicio idiosincrático de Leonard sigue siendo un intangible no "
        "replicable automáticamente), pero descarta la lectura de «key man puro sin red de "
        "contención».")]
    o += [p("<b>¿El motor de M&amp;A sigue intacto?</b> — dato central, corregido tras "
        "verificación. El ritmo de despliegue de capital se <b>acelera</b> bajo Miller, no se "
        "encoge: caja neta en adquisiciones ≈US$1.436M en H1-2026 vs ≈US$548M en H1-2025 (cifras "
        "corregidas), un salto material. No hay evidencia en el expediente de relajación del "
        "hurdle rate — sólo de mayor volumen desplegado. Pregunta abierta, no resuelta: ¿el ritmo "
        "más rápido es compatible con mantener la disciplina, o el propio ritmo es en sí mismo una "
        "señal a vigilar? (Ver mecanismo R2, sección 8.)")]
    o += [p("<b>Banderas de gobierno:</b> sin código de conducta y ética escrito a nivel de "
        "holding — mitigado parcialmente por contratos de empleo y códigos a nivel de subsidiaria. "
        "Sin política que restrinja el uso de instrumentos de cobertura (swaps, collars) sobre las "
        "acciones en escrow — hueco real, sin evidencia de uso. KPMG audita desde 1995, 30 años "
        "sin cambio — estabilidad extrema con la contrapartida de menor independencia estructural "
        "a tan largo plazo. Resultado numérico del say-on-pay 2026 no accesible — laguna "
        "declarada.")]
    o += [hr(), p("<b>El filtro Munger, antes de seguir</b>", "h3")]
    o += [p("<b>Incentivos:</b> genuinamente alineados en el diseño formal — bono ligado a ROIC "
        "con umbral de tasa libre de riesgo, 75% en escrow 4 años, bonos de NEO atados a la unidad "
        "que dirigen. Pero tanto Leonard como Miller operan hoy con compensación en efectivo NIL — "
        "su «skin in the game» es tenencia preexistente, no compra activa financiada por bono "
        "nuevo. Esto es neutral-a-positivo (no hay incentivo perverso de maximizar bono a corto "
        "plazo) pero significa que el mecanismo de «compra obligatoria con dinero de bono» —el que "
        "sí se verifica con cifras exactas en los otros cuatro NEO (Baksh, Bender, Van Poelje, "
        "McKay, con montos y fechas)— no aplica a las dos personas que más importan para la tesis "
        "de sucesión.")]
    o += [p("<i>Nota post-Paso 10: el sesgo de confirmación que el abogado del diablo identificó "
        "sobre este mismo filtro se detalla en la sección 10.</i>", "nota")]
    return o + [PageBreak()]


def s6_knockouts():
    o = flag_titulo("6 · Los hechos que podrían romper la tesis",
                     "Seis knock-outs binarios, cinco años de estados financieros auditados, cero "
                     "activados — con la fiabilidad de la fuente declarada sin adornos")
    o += [p("Catálogo fijo, cinco años fiscales (2021-2025) más el intermedio 2T-2026, sobre "
        "Estados Financieros Auditados por KPMG y el AIF FY2024.")]
    o += [callout("LA TRAMPA",
        "<b>Nota de fiabilidad.</b> La verificación adversarial no pudo re-acceder hoy a los 5 "
        "Estados Financieros Auditados ni al AIF (URLs rotas/404 en el momento de la "
        "verificación) — todo lo que depende exclusivamente de ellos queda <b>DEGRADADO por falta "
        "de re-cruce</b>, no por error detectado. Lo que sí se re-cruzó hoy contra el Informe "
        "2T-2026 y el MIC 2026 (sucesión, estructura de deuda, CFO/FCFA2S semestral, serie de "
        "Licencias) coincidió de forma exacta o casi exacta.")]
    o += [tabla([
        ["#", "KNOCK-OUT", "RESULTADO Y EVIDENCIA"],
        ["(a)", "Estructura VIE / entidad de propósito especial",
         "<b>NO se marca.</b> Cero apariciones de «variable interest entity»/«VIE»/«structured "
         "entity» en los 5 Estados Financieros y el AIF; consolidación por control accionario "
         "estándar IFRS 10 [degradado por falta de re-cruce hoy]."],
        ["(b)", "SBC &gt; 50% del FCF ajustado durante ≥3 años",
         "<b>NO se marca.</b> SBC≈0% en los 5 años, confirmado por ausencia de línea de "
         "«share-based payments» en el flujo de caja y por negación textual explícita cada año: "
         "«no significant... share-based payments attributed to the key management personnel» "
         "[degradado]."],
        ["(c)", "ROIC &lt; WACC estructural durante ≥3 años",
         "<b>NO se marca, con margen amplio.</b> Bajo el método más conservador (ROIC base EBIT, "
         "mínimo observado 15,5% en 2022) y el WACC preliminar más alto de la banda (~10,5%), el "
         "spread se mantiene positivo los 5 años. Con el WACC bottom-up final (6,6-8,5%), el "
         "margen es aún mayor. Descansa sobre cifras no re-cruzadas hoy — «NO se marca» sobre "
         "HECHOs degradados, no limpios."],
        ["(d)", "Restatement / reexpresión de ingresos",
         "<b>NO se marca.</b> Sin apariciones de «restat*»/«re-express*»/«correction of error» "
         "ligadas a ingresos; único hallazgo es una reclasificación de presentación del pasivo "
         "IRGA en FY2025 (no una reexpresión de resultados), reconciliada numéricamente: "
         "US$1.855M − US$389M = US$1.466M, cuadra exacto."],
        ["(e)", "Dependencia de un único cliente o regulador",
         "<b>NO se marca.</b> «No single customer accounted for more than 2% of our total "
         "revenues in fiscal 2024» [AIF FY2024, p.23]. Distribución geográfica diversificada "
         "(45% EE.UU./9% Canadá/33% RU-Europa/13% resto). Laguna: cifra equivalente FY2025 no "
         "confirmada (AIF fiscal 2025 no publicado)."],
        ["(f)", "Deuda tóxica",
         "<b>HECHOS reales, NO alcanzan el umbral.</b> Dos incumplimientos de covenant en 5 años "
         "(2022: cuatro préstamos a término de subsidiarias, resuelto 2023; 2025: un préstamo de "
         "US$51M, administrativo, «unrelated to the financial performance of the entity»). Ambos "
         "confinados a deuda sin recurso, inmateriales frente a US$16.171M de activos totales, sin "
         "contagio a la matriz. Patrón recurrente cada ~3 años (vigilar, no knockout). Las "
         "Debentures (tasa reseteable, PIK, hoy 8,6-8,9%) son un híbrido subordinado, no deuda "
         "senior limpia — flag para el WACC, no para este knockout."]],
        [0.9*cm, 3.6*cm, 12.5*cm], font_sz=7.7)]
    o += [p("<b>Ningún knockout se activa.</b> El expediente pasa a los pasos de comprensión del "
        "negocio.")]
    return o + [PageBreak()]


def s7_percepcion():
    o = flag_titulo("7 · Qué creo distinto del consenso",
                     "Percepción variante — todavía borrador de agente, pendiente de que Felipe "
                     "decida si es realmente su tesis")
    o += [p("<i><b>[BORRADOR DE AGENTE — PENDIENTE DE QUE FELIPE LO ESCRIBA/RATIFIQUE "
        "PERSONALMENTE, NO ES SU JUICIO REAL]</b></i>", "nota")]
    o += [p("Propuesta tentativa de qué podría estar viendo Felipe que el mercado no está pesando "
        "correctamente: <i>«El mercado está tratando el -34,6% de drawdown de CSU como si fuera "
        "una historia de ruptura del modelo por IA — pero el mismo complejo completo de "
        "adquirentes seriales de software vertical (Roper -22,5%, OpenText -38,1%, Descartes "
        "-27,8%, Topicus -44,5%, Lumine -53,6%) cayó de forma correlacionada en la misma ventana, "
        "lo que sugiere un de-rating sectorial/factorial, no una ruptura idiosincrática de CSU. Si "
        "la tesis bajista fuera específica de CSU, no debería explicar por qué Topicus y Lumine "
        "—el mismo manual aplicado en otros mercados, sin el ruido de sucesión de Leonard— cayeron "
        "aún MÁS que la matriz.»</i>")]
    o += [p("Ésta es una hipótesis a probar, no una conclusión — Felipe debe decidir si esto es "
        "realmente lo que ve de forma diferente al consenso, o si es sólo una narrativa conveniente "
        "para justificar el precio. El riesgo de esta percepción variante, si es errónea, es "
        "precisamente que el de-rating correlacionado sea correcto — que el mercado sí esté viendo, "
        "de forma agregada y anticipada, comoditización real del software vertical/nicho por IA "
        "que aún no aparece limpiamente en ningún transcript individual leído en la sección 3.")]
    o += [callout("PAUSA REFLEXIVA",
        "<b>Nota post-Paso 10 (Golpe 3):</b> el abogado del diablo demuestra —ver sección 10— que "
        "esta misma observación (de-rating correlacionado de 6 comparables) es la evidencia que la "
        "sección 9 usó para construir una banda de WACC «de prudencia» de 7,5%-8,5%, y que el "
        "cálculo de asimetría headline de esa misma sección la ignoró en la práctica al anclarse "
        "en r=7,0%. Si Felipe ratifica esta percepción variante como su tesis real, debe hacerlo "
        "sabiendo que, al WACC que él mismo consideró más defendible dado ese de-rating "
        "correlacionado, el margen de seguridad que aquí se cita como «favorable» <b>no sobrevivió "
        "el recálculo</b>.")]
    return o + [PageBreak()]


def s8_premortem():
    o = flag_titulo("8 · El pre-mortem",
                     "Cinco mecanismos específicos de un adquirente en serie de software vertical "
                     "descentralizado — no genéricos de «la empresa podría ir mal»")
    o += [tabla([
        ["MECANISMO", "MÉTRICA OBSERVABLE", "VENTANA"],
        ["<b>R1 ·</b> Desaceleración de Mantenimiento por debajo del umbral de reinversión "
         "sostenible. Una caída sostenida reduce la caja disponible para reinvertir sin subir "
         "apalancamiento.",
         "Crecimiento orgánico FX-ajustado de Mantenimiento &lt;3% durante 2 trimestres "
         "consecutivos. <b>Estado: 2T-2026 ya imprimió 2%.</b>",
         "Confirmación o refutación con el 3T-2026 (~nov-2026)."],
        ["<b>R2 ·</b> Erosión del hurdle rate bajo presión de desplegar capital más rápido. La "
         "aceleración del ritmo de M&amp;A (+~162% H1-26 vs H1-25) podría señalar relajación de "
         "estándares para «mantener el ritmo».",
         "ROIC incremental (base EBIT) cayendo y manteniéndose por debajo de ~10% durante 2 años "
         "fiscales consecutivos.",
         "Primer dato limpio con los EEFF Auditados FY2026 y FY2027 (~1T-2027 y 1T-2028)."],
        ["<b>R3 ·</b> Brecha de calidad en la asignación de capital de la cohorte post-sucesión. "
         "El juicio idiosincrático de Leonard podría no transferirse limpiamente a Miller.",
         "ROIC realizado sobre adquisiciones cerradas desde el 25-sep-2025 en adelante, a 2-3 "
         "años vista, vs. banda histórica pre-sucesión (~15-35% EBIT/EBITA).",
         "Primer dato legible ~FY2027-2028 (maduración de unidades recién adquiridas)."],
        ["<b>R4 ·</b> Comoditización de nichos verticales por IA reduciendo barreras de entrada. "
         "El propio factor de riesgo de la compañía lo advierte por escrito.",
         "Crecimiento orgánico FX-ajustado de Licencias negativo ≥4 trimestres consecutivos, Y "
         "margen EBITA total &lt;23,5% durante 2 años consecutivos.",
         "A través de FY2027."],
        ["<b>R5 ·</b> Originación de negocio nuevo perdiendo frente a un competidor de producto, "
         "dentro de un vertical ya conquistado. (Añadido en el Paso 10, Golpe 1.)",
         "En el 3T-2026: (i) Mantenimiento NO rebota sobre 3% (≤2% o cae más) Y/O (ii) aparece un "
         "<b>segundo vertical</b> con caída atribuida explícitamente a pérdida de cuota "
         "competitiva. Cualquiera de las dos basta.",
         "3T-2026, ~5-6 nov-2026. <b>BLOQUEANTE para cualquier COMPRAR.</b>"]],
        [5.9*cm, 6.4*cm, 4.7*cm], font_sz=7.6)]
    o += [p("<b>R5 merece una nota aparte.</b> Es distinto de R1 y R4. R1 mide si el cliente "
        "<i>retenido</i> deja de pagar suficiente; R4 mide comoditización general por IA. R5 mide "
        "algo más específico y más grave: que un rival de escala le arrebate a CSU la posición "
        "dominante <i>dentro de un nicho que ya controlaba</i>, demostrando que el switching-cost "
        "moat (sección 2) no es una barrera contra un ataque competitivo directo, sólo contra la "
        "indiferencia del cliente satisfecho. Altera-vs-Epic es el primer caso en curso de este "
        "mecanismo, no resuelto.")]
    o += [hr(), p("<b>Invertir el problema — ¿cómo destruiría yo este negocio?</b>", "h3")]
    o += [p("(1) Aceleraría el ritmo de M&amp;A sin ajustar el hurdle rate, comprando crecimiento "
        "con capital cada vez más caro o de peor calidad bajo presión de «demostrar» que el modelo "
        "sigue funcionando post-Leonard; (2) centralizaría la toma de decisiones, rompiendo la "
        "descentralización que es la fuente real de la disciplina de cientos de unidades "
        "independientes; (3) dejaría que la comoditización por IA avance sin resistencia en varios "
        "nichos simultáneamente hasta que el patrón de subida de precios de 3-9%/año deje de "
        "sostenerse sin fuga de clientes.")]
    o += [p("<b>Redundancia:</b> alta a nivel operativo — la función de originación/evaluación de "
        "M&amp;A tiene 30 años de continuidad institucional (CIO desde 1995), cientos de unidades "
        "operativas independientes, ningún punto único de fallo a nivel de unidad. Baja a nivel de "
        "juicio de asignación de capital en la cúspide — ahí sí hay concentración en el sucesor, "
        "con el precedente de que Leonard mismo era, según el propio expediente, un intangible no "
        "replicable.")]
    o += [p("<b>Punto de no retorno:</b> no observado todavía. Sería: (a) ROIC&lt;WACC estructural "
        "3+ años (knockout c, hoy con margen amplio); (b) relajación formal del hurdle rate por el "
        "Consejo (sin evidencia); (c) un evento de refinanciación forzada a nivel matriz "
        "(descartado — posición de caja neta positiva ~US$1,4B a nivel CSI matriz, línea de "
        "crédito de US$1.085M enteramente sin usar).")]
    return o + [PageBreak()]
