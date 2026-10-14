# -*- coding: utf-8 -*-
"""§3 scuttlebutt · §4 el motor de crecimiento · §5 gestión e incentivos"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, cm
from reportlab.platypus import PageBreak


def s6_scuttlebutt():
    o = flag_titulo("3 · Lo que dicen quienes lo rodean",
                    "Scuttlebutt limitado por presupuesto de búsqueda agotado — se documenta lo encontrado, se declara lo que falta")
    o += [p("<b>Limitación operativa, declarada sin adornos.</b> El presupuesto de WebSearch de la sesión de "
        "origen se agotó (200/200) antes de empezar esta sección; todo lo que sigue se obtuvo vía WebFetch a "
        "URLs conocidas, sin rastreo de prensa japonesa especializada (5ch, ITmedia, Nikkei xTECH), foros "
        "sectoriales, ni comparativas de guidance-vs-resultado de rivales en los últimos trimestres. La "
        "sesión de cierre (Paso 10) intentó dos búsquedas adicionales dirigidas específicamente a este hueco "
        "—competencia OBIC frente a freee/Money Forward en PYME— y se topó con el mismo presupuesto agotado "
        "a nivel de cuenta. <b>El hueco permanece abierto, no por falta de intento sino por límite de "
        "herramienta.</b> La validación cruzada del 8-sep no tenía este hueco en su mandato —su único foco "
        "era el escrutinio de beta sobre cinco tesis— y no aporta nada nuevo aquí.")]
    o += [p("<b>Money Forward (TSE:3994)</b>, el comparador cloud/PYME japonés más citado, es la pieza más "
        "sólida del scuttlebutt disponible: factura ¥56.100 millones TTM (OBIC es ~2,4 veces su tamaño) y "
        "crece +28,3% interanual frente al +11,5% de OBIC; cotiza a un PER de 86,3x frente a los ~28x de "
        "OBIC; el consenso lo marca “Hold” con un objetivo -24% desde su propio precio, mientras OBIC cotiza "
        "cerca de su consenso (+7%) [HECHO, stockanalysis.com, ficha TYO:3994, 2026-09-04].")]
    o += [callout("EN ROMÁN PALADINO",
        "Esto es una lectura cualitativa, <b>no una comparación de calidad</b>: no son rivales frontales en "
        "la mayoría de las cuentas hoy. Money Forward vende SaaS nativo-cloud a pymes y startups; OBIC vende "
        "ERP consultivo a medida para empresas medianas-grandes. Pero el terreno de colisión crece por ambos "
        "lados — OBIC sube de gama hacia cuentas grandes, Money Forward madura hacia cuentas más grandes — "
        "y ésa es exactamente la fricción que el pre-mortem de este documento vigila con una fecha concreta.")]
    o += [p("<b>Works Applications / Works Human Intelligence</b>, el rival histórico en nómina/RRHH: la "
        "única fuente disponible (Wikipedia, citando Bloomberg 2015) está desactualizada a 2015-2017 — "
        "“mayor vendedor japonés de software de nómina/RRHH” con más de 7.000 clientes en 2016, privatizada "
        "desde 2011. No representa necesariamente su posición competitiva actual, y al ser privada no hay "
        "datos financieros recientes disponibles.")]
    o += [p("<b>La “cuesta del 2025” de SAP</b> (<i>2025-nen no gake</i>), el ángulo japonés del fin de soporte de SAP "
        "ECC, no se pudo confirmar con especificidad: el intento de acceder a la página de METI devolvió "
        "error 403; Wikipedia sólo confirma, en genérico, que la mayoría de sistemas ECC alcanzaban fin de "
        "mantenimiento mainstream a fines de 2025, sin cifra de mercado japonés [HECHO parcial, genérico, "
        "sin especificidad].")]
    o += [p("<b>Huecos explícitos, no rellenados, con intento fallido ya documentado:</b> comentarios de "
        "clientes o excompleados en foros japoneses; guidance-vs-resultado real de SAP Japan y Oracle "
        "NetSuite Japan en 2-3 trimestres recientes; disclosure financiero reciente de Works Human "
        "Intelligence; y —el más urgente tras el Paso 10— un episodio competitivo nombrado y fechado en el "
        "segmento PYME frente a freee o Money Forward. Se recomienda un pase de verificación con presupuesto "
        "de búsqueda fresco antes de que cualquier hallazgo de esta sección sostenga por sí solo un knockout "
        "o un veredicto.")]
    return o + [PageBreak()]


def s7_motor():
    o = flag_titulo("4 · El motor de crecimiento",
                    "g = tasa de reinversión × ROIC incremental — y aquí la fórmula clásica se rompe")
    o += [p("La fórmula de Damodaran para estimar el crecimiento mecánico de un negocio es simple: cuánto "
        "reinvierte, multiplicado por cuánto rinde esa reinversión. Aplicada a OBIC con la definición "
        "clásica (reinversión neta = capex − D&amp;A; tasa de reinversión = reinversión neta / NOPAT, "
        "impuesto SUPUESTO al 30%), el resultado es sorprendente:")]
    o += [tabla([
        ["EJERCICIO", "CAPEX−D&amp;A (¥M)", "TASA DE REINVERSIÓN", "ROIC DEL AÑO", "g MECÁNICO IMPLÍCITO"],
        ["FY2022", "−609", "−1,6%", "27,53%", "≈ −0,4%"],
        ["FY2023", "−1.392", "−3,2%", "26,05%", "≈ −0,8%"],
        ["FY2024", "+1.195", "+2,4%", "25,37%", "≈ +0,6%"],
        ["FY2025", "−619", "−1,1%", "24,33%", "≈ −0,3%"],
        ["FY2026", "−476", "−0,8%", "23,51%", "≈ −0,2%"]],
        [2.4 * cm, 3.4 * cm, 3.6 * cm, 3.4 * cm, 3.8 * cm], font_sz=8.4)]
    o += [p("<i>[INFERENCIA — cálculo propio sobre HECHOs del dossier de knockouts; tasa de impuesto 30% es "
        "SUPUESTO, no una cifra efectiva verificada.]</i>", "nota")]
    o += [chart("charts/07_motor_crecimiento.png")]
    o += [p("<b>Lectura honesta: la fórmula mecánica se rompe para este arquetipo de negocio.</b> El g "
        "implícito por esta vía es esencialmente cero o levemente negativo los cinco ejercicios — y sin "
        "embargo los ingresos crecieron entre +8,7% y +12,0% cada año de la ventana, sin una sola caída. La "
        "razón, ya diagnosticada por el dossier de hechos: OBIC no reinvierte vía activo fijo (el capex "
        "quedó por debajo de la D&amp;A en 4 de 5 años); reinvierte vía <b>OPEX expensado de inmediato</b> "
        "—contratación de consultores e ingenieros, formación interna, I+D no capitalizado— que el proxy "
        "capex-D&amp;A no captura en absoluto [INFERENCIA]. El capital operativo neto es de apenas "
        "~¥12.000 millones frente a ¥88.823 millones de beneficio operativo.")]
    o += [callout("LA TRAMPA",
        "Esta sección calcula y reconoce la contradicción entre la g mecánica (~0%) y el crecimiento "
        "observado (7-12%) — pero la primera versión de este documento la resolvía sustituyendo, sin más "
        "corroboración, la g mecánica por la guía de ingresos de la propia gerencia. El abogado del diablo "
        "señaló que eso es exactamente el patrón que el candado adversarial existe para atrapar: descartar "
        "en silencio un input mecánico que decepciona y sustituirlo por otro que sí da el número que el caso "
        "alcista necesita.<br/><br/>"
        "<b>Esta objeción se acepta parcialmente.</b> La explicación causal alternativa —reinversión vía "
        "capital humano expensado— es una INFERENCIA razonable y consistente con el arquetipo de negocio "
        "(servicios profesionales/software asset-light, el mismo patrón de Visa, Mastercard o las "
        "consultoras), pero este dossier <b>no construyó un proxy empírico alternativo</b> (crecimiento de "
        "plantilla, o SG&amp;A como % de ingresos) que la corrobore de forma independiente antes de "
        "apoyarse en la guía de gerencia. Ese proxy queda como tarea pendiente explícita.")]
    o += [p("<b>g empírico real, el que sí se usa en el DCF (etiquetado SUPUESTO desde el origen):</b>")]
    o += [tabla([
        ["MEDIDA", "VALOR", "ORIGEN"],
        ["CAGR de ingresos, FY2022-FY2026 (4 años)", "<b>≈ 10,9%</b>", "cálculo propio sobre HECHO"],
        ["CAGR de ingresos, FY2017-FY2026 (década)", "<b>≈ 9,2%</b>", "irbank.net, serie corregida y verificada"],
        ["CAGR de owner earnings, FY2022-FY2026", "<b>≈ 17,8%</b>",
         "inflado por expansión de margen (60,5%→65,7%), ya cerca de su techo guiado (65,9% FY2027E) — "
         "<b>no debe extrapolarse al mismo ritmo</b>"],
        ["Guía propia FY2027E", "ingresos ¥148.700M (+10,0%), margen 65,9%", "HECHO, deck 2026-04-22, p.16"]],
        [6.0 * cm, 5.0 * cm, 5.6 * cm], font_sz=8.3)]
    o += [p("<b>Percentil histórico de la persistencia (marcado explícitamente como SUPUESTO cualitativo).</b> "
        "Contra el fondo de escepticismo estadístico de Chan-Karceski-Lakonishok 2003 —el crecimiento de "
        "beneficios no persiste por encima del azar en el universo general no filtrado— una trayectoria de "
        "32 ejercicios consecutivos de récord y 10 años sin una sola caída de ingresos, atravesando dot-com, "
        "GFC, Tōhoku, Abenomics y COVID, es estadísticamente atípica: la sitúo cualitativamente en el "
        "percentil superior (aprox. top 1-3%) de persistencia de crecimiento en cualquier universo amplio no "
        "filtrado. No se replicó el estudio CKL 2003 sobre una base de datos propia esta sesión: es una "
        "estimación cualitativa, no una medición.")]
    o += [p("<b>Un dato no descartado, convertido en falsador tras el Paso 10.</b> El propio crecimiento de "
        "ingresos por empleado (¥42,1M→¥58,5M) es igual de compatible con “reinversión en capital humano que "
        "compone” que con “cosecha de precio y mezcla hacia cuentas grandes sobre una base de clientes que "
        "no crece en volumen” — ninguna fuente consultada desagrega el crecimiento de ingresos entre volumen "
        "(nuevos contratos/nuevos clientes) y precio/mezcla. Se necesita, en filings futuros, una métrica de "
        "volumen independiente de la cifra de ingresos para diferenciar entre las dos historias.")]
    o += [p("<b>¿Qué limita el crecimiento?</b>")]
    o += [tabla([
        ["FACTOR", "LECTURA"],
        ["Capital desplegable", "<b>No es el cuello de botella.</b> Negocio asset-light, caja neta "
         "¥207.385M, cero deuda financiera."],
        ["Talento / modelo de contratación", "<b>Probablemente el límite más vinculante.</b> ~200 empleados "
         "hacen de instructores internos durante ~6 meses de onboarding de nuevos graduados, sin "
         "contratación lateral [HECHO, p.42]. Esto limita mecánicamente la velocidad a la que puede "
         "escalar capacidad de consultoría sin diluir la calidad que sostiene el propio moat."],
        ["Techo de demanda", "Parcial, mitigado por movimiento de gama. 100% de ingresos son japoneses, en "
         "un país con demografía envejecida; mitigado por el movimiento hacia clientes >¥100.000M (27%→29% "
         "en un año) y por el upsell de módulos de IA (2.428 solicitudes de patente acumuladas relacionadas "
         "con IA a marzo-2026, frente a 1.235 en marzo-2022)."],
        ["Regulación", "No es un límite hoy — es, de hecho, la fuente del moat: la complejidad regulatoria "
         "japonesa actúa como barrera de entrada."]],
        [4.3 * cm, 12.3 * cm], font_sz=8.4)]
    o += [p("<b>Años de pista estimados.</b> El propio modelo de valoración asume una desaceleración "
        "explícita a lo largo de 10 años (10,0%→3,5%), lo cual parece un caso central razonable dado el "
        "límite de talento y la demografía — pero podría ser más corto si el cuello de botella de "
        "contratación aprieta antes, o más largo si el upsell de IA sustituye eficazmente al TAM de nuevos "
        "clientes que se reduce. INFERENCIA/SUPUESTO, no una cifra defendible con precisión de un año. Nada "
        "de esto lo tocó la validación cruzada del 8-sep, cuyo alcance fue exclusivamente el beta.")]
    return o + [PageBreak()]


def s8_gestion():
    o = flag_titulo("5 · Gestión e incentivos",
                    "Un fundador de 88 años que todavía controla la casa, y un CEO operativo que cobra seis veces más porque no tiene su propiedad")
    o += [p("<b>Estructura de propiedad — empresa todavía controlada por su fundador, 58 años después.</b> "
        "Los grandes accionistas al 2026-03-31: MN Holdings con 19,51% (84.545 miles de acciones), Nihon "
        "Master Trust con 15,06% y Nihon Custody Bank con 5,23% (fiduciarios pasivos), Noda Yorihiro "
        "(fundador) con 3,32% personal, y Noda Mizuki con 3,20% [HECHO, "
        "OBIC Yūhō FY2026/3, p.22, sección de grandes accionistas]. Sumando las líneas visibles, la familia Noda controla "
        "al menos <b>~26%</b> del capital económico. Que MN Holdings sea el vehículo patrimonial de la "
        "familia es INFERENCIA razonable (patrón de apellido, contexto), no confirmada contra un informe de "
        "participaciones significativas.")]
    o += [p("Yorihiro Noda nació en 1938, fundó la compañía en 1968, fue presidente hasta 2013 y desde "
        "entonces es presidente representante del consejo [HECHO, p.30]. El CEO operativo, Shoichi "
        "Tachibana (n. 1961), entró en la empresa en 1985 y ascendió íntegramente por dentro "
        "(Osaka→Tokio→Yokohama→consejero en 2006→presidente en 2013) — 41 años en la casa, cero contratación "
        "lateral, participación personal mínima (212.000 acciones, ~0,05%).")]
    o += [callout("DATO CURIOSO",
        "La compensación es el dato más revelador de toda esta sección. El tope de retribución fija es de "
        "¥1.000M/año para consejeros; el bono variable está ligado explícitamente al <i>“tōki jun rieki”</i> "
        "(beneficio neto individual de la matriz, no consolidado, no una métrica de vanidad), con tope de "
        "0,5%/¥400M; y la retribución en <b>acciones restringidas</b> (no opciones) tiene un tope de "
        "¥600M/año, con el propósito declarado de “compartir valor con los accionistas” [HECHO, p.39]."
        "<br/><br/>"
        "Las cifras individuales de FY2026 son la prueba: <b>Tachibana (CEO, ~0,05% de propiedad) cobró "
        "¥811M</b> (base ¥432M + bono ¥270M + acciones restringidas ¥109M); <b>Noda (fundador, >20% de "
        "propiedad) cobró ¥135M</b> (base ¥120M + bono ¥15M + cero acciones restringidas) [HECHO, p.40, "
        "tabla 3]. El ejecutivo sin skin-in-the-game vía propiedad recibe casi 6 veces más, fuertemente "
        "ligado a acciones y a beneficio neto real; el fundador, ya expuesto vía propiedad, no necesita el "
        "incentivo adicional. <b>Es un diseño coherente, no un accidente.</b>")]
    o += [p("<b>La disciplina de capital confirma el diseño.</b> En FY2026 la compañía recompró y canceló "
        "6.000.000 de acciones (¥7.572M) [HECHO, p.25]. Para FY2027 tiene autorizado hasta 10.000.000 de "
        "acciones / ¥50.000M, con un ratio de retorno total (dividendo + recompra) del <b>110,7%</b> — más "
        "que el beneficio neto del año, financiado con caja acumulada [HECHO, deck 2026-04-22, diapositiva "
        "19]. Cero participaciones cruzadas por política (<i>seisaku hoyū kabushiki</i>) [HECHO, p.40] — sin arquitectura "
        "keiretsu de blindaje mutuo. No hay plan de stock options vigente: sólo acción restringida, mejor "
        "alineada que una opción porque no tiene la asimetría de “gano si sube, no pierdo si baja”.")]
    o += [p("<b>Nota de gobierno, sin sobre-interpretar.</b> La sección de riesgos enmarca la fuga de talento "
        "en torno a un escenario explícitamente hipotético de OPA hostil [HECHO, p.14] — lenguaje inusual, "
        "coherente con el propio relato de capital humano: <i>jimae-shugi</i> en formación (sacrificando ingresos de "
        "proyectos a corto plazo por acumulación de know-how) y <i>fukumi keiei</i> en compensación (bandas de sueldo "
        "suavizadas contra ventas de corto plazo a costa del cliente) [HECHO, p.42]. El auditor, EY Shin "
        "Nihon, lleva <b>24 años consecutivos</b> en el cargo [HECHO, p.37] — no infrecuente en Japón, donde "
        "no hay rotación obligatoria, pero un mandato largo digno de vigilancia. En la AGM del 2026-06-25 el "
        "consejo se amplió a 9 miembros con Kyoko Udagawa (ascendida internamente en 2025), y la "
        "representación femenina subió de 9,1% a 16,7% — de nuevo cantera interna [HECHO, p.33-35].")]
    o += [callout("LECCIÓN TRANSFERIBLE",
        "Incentivos bien alineados, sin señales de autoservicio ejecutivo, disciplina de capital real y "
        "consistente con la retórica. <b>El punto de vigilancia genuino no es de incentivos del día a día "
        "sino de sucesión</b> — ver el pre-mortem, mecanismo 3. Ninguna objeción del abogado del diablo, ni "
        "la validación cruzada del 8-sep, tocó esta sección: se mantiene intacta en ambas revisiones.")]
    return o + [PageBreak()]
