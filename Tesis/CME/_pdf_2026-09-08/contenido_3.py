# -*- coding: utf-8 -*-
"""6 · Lo que dicen quienes lo rodean (scuttlebutt) · 7 · El motor de crecimiento"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, cm
from reportlab.platypus import PageBreak

def s6_scuttlebutt():
    o = flag_titulo("6 · Lo que dicen quienes lo rodean",
                    "Un rival con diez bancos detrás lo intentó de frente, y el dato de mayor valor no es una encuesta: es un evento de estrés real")
    o += [p("<b>El ataque más serio y actual está en curso, y hasta ahora ha fallado en la prueba de estrés más "
        "dura disponible.</b> FMX Futures Exchange —respaldado por BGC Group y Howard Lutnick— lanzó futuros de "
        "SOFR el 23 de septiembre de 2024, sin cobrar comisión «hasta nuevo aviso», atacando directamente el "
        "contrato de tasas más grande del mundo (HECHO, FOW oct-2024; fmxfutures.com). Resultado: CME mantuvo "
        "<b>más del 99,99%</b> de cuota de mercado en futuros de SOFR a fin de 2024; FMX alcanzó sólo "
        "<b>≈0,11%→0,3%</b> en los primeros tres trimestres de 2025 (HECHO, Clarus FT).")]
    o += [callout("PAUSA REFLEXIVA",
        "El dato de mayor valor de todo el scuttlebutt no es una encuesta ni una entrevista: es un evento de "
        "estrés real, no solicitado. En la semana del anuncio de aranceles (7 de abril de 2025), <b>los "
        "volúmenes de FMX cayeron un 66%</b> (de ~3.000 contratos/día en marzo a 928/día), mientras <b>CME "
        "marcaba récords de 12,5 millones (4-abr) y 11,7 millones de lotes (7-abr)</b>, más del doble de su "
        "promedio de marzo (HECHO, FOW, 11-abr-2025). Es exactamente el mecanismo predicho por la teoría del "
        "moat: bajo presión real, el trader vuelve al pool más profundo aunque sea más caro en fee nominal — "
        "porque lo que compra en el pool profundo no es un precio, es la certeza de poder salir.")]
    o += [p("<b>Una corrección de prensa que conviene hacer explícita:</b> el «40% de cuota» de FMX en "
        "Treasuries que circula en algunos medios corresponde a <b>FMX UST</b>, una plataforma separada de "
        "trading <i>cash</i> de bonos del Tesoro — no compite con la franquicia de futuros de CME. En futuros de "
        "Treasuries propiamente dichos, FMX operó sólo <b>31 contratos en julio de 2025</b> (HECHO, FOW): "
        "irrelevante hasta ahora.")]
    o += [p("<b>El trimestre más reciente, en cifras propias de la empresa</b> (2T-2026, HECHO, comunicado CME "
        "Group 22-jul-2026): descrito por la propia gerencia como <i>«the strongest [half] in CME Group's "
        "history»</i>. ADV de 29,8 millones de contratos (segundo mejor 2T histórico), 94% del volumen "
        "originado por clientes institucionales, ingresos de datos de mercado +20% interanual —el 33º trimestre "
        "consecutivo de crecimiento en esa línea—, ahorros de margen citados en la llamada de 27.000 millones de "
        "dólares diarios, y 1.200 millones devueltos en capital (468 M en dividendos + 695 M en recompras). "
        "Lanzamientos nuevos: cripto 24/7 (1.500 millones de dólares operados en los primeros 8 fines de "
        "semana), single stock futures (22 nombres, orientado a minorista) y «compute futures» (renta de "
        "capacidad de GPU vía Silicon Data).")]
    o += [callout("LA TRAMPA",
        "<b>El riesgo competitivo nuevo de 2026, y la propia gerencia lo trata como sistémico, no como relaciones "
        "públicas.</b> Duffy sobre el auge de los mercados de predicción (Kalshi) y los perpetuos cripto: "
        "<i>«la auto-liquidación de un mercado del tamaño del de acciones de EE.UU. podría ser muy riesgosa "
        "sistémicamente»</i> (HECHO, comunicado 2T-2026). Y hay litigio regulatorio activo: CME demandó a la "
        "CFTC por el «stay» del contrato de crudo 24/7 de un rival, que Duffy describió como <i>«inconsistencia "
        "regulatoria»</i>. Es la vía por la que un competidor podría replicar la exposición económica de CME "
        "operando fuera del régimen de márgenes SPAN — atacando el Candado 1 del moat sin necesitar más "
        "liquidez que la de CME, sólo un marco regulatorio distinto.")]
    o += [p("<b>Presupuesto de scuttlebutt agotado antes de cubrir comentarios directos de Deutsche Börse o "
        "LSEG</b> — hueco de evidencia declarado, no evitado, consistente con la disciplina de datos de la casa.")]
    o += [callout("DATO CURIOSO",
        "El dato de share de FMX en SOFR futures citado arriba (ene-sep 2025) tenía ya más de un año de "
        "antigüedad frente a la síntesis del 4-sep-2026. Se intentó actualizarlo con datos de 2026 durante la "
        "finalización de esa tesis; el presupuesto de búsqueda web de la sesión estaba agotado — hueco de "
        "evidencia declarado, no resuelto, y sigue sin resolverse en esta actualización del 8-sep. El abogado "
        "del diablo lo convirtió en un falsable duro reforzado (ver secciones 13 y 15): si el share de FMX en "
        "SOFR futures supera el 3% del ADV combinado, sostenido un mes calendario completo, antes del "
        "16-nov-2026, las secciones 5 y 12 deben reabrirse de inmediato.")]
    o += [p("<b>Lo que esta sección tiene que ver con la corrección de beta de la sección 12, dicho sin rodeos:</b> "
        "un rival respaldado por un grupo con capital propio significativo, atacando el contrato ancla sin "
        "cobrar comisión, calificado por el propio CEO de «el riesgo competitivo más serio en dos décadas» en "
        "las notas de esta investigación, es exactamente el tipo de riesgo que un beta de mercado bien medido "
        "debería reflejar en el coste de capital de CME. Que el beta bursátil crudo (0,27) no lo reflejara en "
        "absoluto —siendo, de hecho, el más bajo de sus cuatro pares— es la contradicción que la actualización "
        "de hoy resuelve.")]
    return o + [PageBreak()]

def s7_motor():
    o = flag_titulo("7 · El motor: reinversión, ROIC y cuánta pista queda",
                    "El marco mecánico estándar produce aquí un resultado espurio — y hay que decirlo antes de usar cualquier número")
    o += [p("g = tasa de reinversión × ROIC incremental es el marco estándar para medir cuánto crecimiento "
        "«se gana» un negocio reinvirtiendo su propio dinero. Aplicado a CME sin matices, produce un número "
        "que contradice de forma directa lo que de verdad ocurrió:")]
    o += [tabla([
        ["(US$M)", "FY2021", "FY2022", "FY2023", "FY2024", "FY2025"],
        ["Capex total", "127,2", "89,7", "76,4", "94,0", "83,5"],
        ["D&amp;A de mantenimiento", "147,8", "134,9", "126,0", "115,1", "107,5"],
        ["<b>Capex de crecimiento (total − D&amp;A)</b>", "<b>−20,6</b>", "<b>−45,2</b>", "<b>−49,6</b>",
         "<b>−21,1</b>", "<b>−24,0</b>"],
        ["NOPAT", "≈2.069", "≈2.325", "≈2.670", "≈3.051", "≈3.231"],
        ["<b>Tasa de reinversión mecánica</b>", "<b>≈−1,0%</b>", "<b>≈−1,9%</b>", "<b>≈−1,9%</b>",
         "<b>≈−0,7%</b>", "<b>≈−0,7%</b>"],
        ["ROIC", "≈7%", "≈8%", "≈10%", "≈11%", "≈12%"]],
        [4.6*cm, 2.4*cm, 2.4*cm, 2.4*cm, 2.4*cm, 2.4*cm], font_sz=7.9)]
    o += [chart("charts/04_motor_reinversion.png")]
    o += [p("<b>HECHO:</b> los cinco años, el capex total fue menor que la depreciación de PP&amp;E — el capex de "
        "crecimiento neto es negativo todos los años, y por tanto también la tasa de reinversión mecánica. "
        "Aplicado literalmente, el marco daría un <b>g negativo espurio</b>, que contradice el crecimiento real "
        "observado: <b>CAGR de ingresos 2021-2025 ≈8,5% anual</b>, con margen operativo expandiendo todos los "
        "años sin una sola reversión (56,0%→60,1%→61,6%→64,1%→64,9%). El propio 10-K confirma la guía de capex "
        "mínima hacia adelante: <i>«In 2026, we expect capital expenditures to total approximately "
        "$85.0 million»</i> (10-K FY2025, Item 7).")]
    o += [p("<b>INFERENCIA sobre el mecanismo real de g:</b> el crecimiento de CME no se financia con capex "
        "capitalizado sino con (i) apalancamiento operativo sobre una plataforma electrónica ya construida, "
        "(ii) gasto tecnológico llevado a resultados en vez de capitalizado, y (iii) estructuración vía joint "
        "ventures o licencias de bajo capital —S&amp;P DJI, ex-OSTTRA, FanDuel Prediction Markets, aporte de "
        "sólo 10,2 millones de dólares— en lugar de M&amp;A apalancada.")]
    o += [callout("LA TRAMPA",
        "<b>Corrección obligatoria, forzada por el abogado del diablo en el Paso 10 (Golpe 2, 4-sep-2026), "
        "aceptada en su totalidad y sin diluir.</b> Declarar «este framework no aplica a este arquetipo» en el "
        "momento exacto en que el dato mecánico da g negativo es la maniobra que el método existe para "
        "prohibir: neutralizar por declaración de excepción un resultado incómodo, en vez de dejar que ese "
        "resultado degrade la confianza en el input que depende de él.<br/><br/>"
        "<b>Consecuencia operativa:</b> el motor alternativo (apalancamiento operativo + JVs de bajo capital) "
        "<b>no está probado con evidencia mecánica independiente</b> — el aporte medido de las JVs es trivial "
        "(FanDuel: 0,16% de los ingresos de 2025), lo que deja casi todo el peso del crecimiento reciente en la "
        "expansión de margen (+890 puntos básicos, 2021-2025), y esa expansión es bidireccional con el volumen, "
        "que la propia gerencia atribuye a un «régimen de incertidumbre» cíclico en <b>9 de 9</b> llamadas "
        "trimestrales analizadas. <b>El g terminal de 3,5% usado en el DCF base (sección 12) debe leerse como un "
        "supuesto NO verificado mecánicamente</b>, no como un número neutral y defendible por igual en toda "
        "condición. El dato que resolvería la objeción —comportamiento del margen operativo en un trimestre de "
        "volumen/volatilidad por debajo del promedio histórico, análogo a 2017 (VIX~11)— no está en los hechos "
        "entregados ni pudo obtenerse en esta síntesis (presupuesto de búsqueda agotado). Es una brecha de "
        "evidencia real, declarada, que sigue abierta en esta actualización — la corrección de hoy es sobre "
        "beta/WACC (sección 12), no sobre este hueco.")]
    o += [p("<b>Percentil histórico aproximado</b> (ancla obligatoria: Chan-Karceski-Lakonishok 2003 — el "
        "crecimiento de beneficios NO persiste por encima del azar en el universo amplio no filtrado). "
        "INFERENCIA, con rango deliberadamente ancho: cinco años consecutivos de expansión de margen sin una "
        "sola reversión, junto a un CAGR de ~8,5%, es un patrón de consistencia poco común — situaría a CME "
        "aproximadamente en el <b>tercio superior</b> de persistencia de crecimiento a 5 años del universo no "
        "filtrado. Es una estimación cualitativa, no un percentil calculado sobre una base de datos específica, "
        "y el propio hallazgo de CKL 2003 obliga a la cautela: consistencia pasada no garantiza persistencia "
        "futura por encima del azar.")]
    o += [p("<b>Qué limita el crecimiento:</b>")]
    o += [tabla([
        ["LIMITANTE", "LECTURA"],
        ["Capital desplegable", "NO es una restricción real — la reinversión requerida es mínima (~85 M US$/año de capex guiado)."],
        ["Techo de demanda", "El limitante más citado por la propia gerencia (9 de 9 trimestres): el «régimen de incertidumbre» macro/geopolítica/de tasas — un motor cíclico, no estructuralmente garantizado."],
        ["Talento", "Limitante secundario para este arquetipo — moat de red, no intensivo en talento especializado escaso."],
        ["Regulación", "Limitante activo y creciente: litigio CFTC sobre crudo 24/7, y el riesgo de que un competidor (Kalshi) opere fuera del régimen de márgenes SPAN."],
        ["Masa crítica por producto nuevo", "El limitante más específico del arquetipo — cada línea nueva necesita liquidez crítica propia; el precedente LCH/SwapClear muestra que CME no siempre gana esa carrera."]],
        [4.4*cm, 12.2*cm], font_sz=8.4)]
    o += [p("<b>Años de pista:</b> INFERENCIA, sin falsa precisión — no hay una cifra de TAM de derivados "
        "listados globales para contrastar la cuota implícita (hueco de evidencia declarado). El núcleo del "
        "negocio (clearing/transacción, ~81% de ingresos, estable 2021-2025) no muestra señales de agotamiento. "
        "Pero gran parte del crecimiento reciente está atado a un régimen de incertidumbre que, por definición, "
        "no es permanente, y las líneas nuevas son apuestas sin historial dentro de la ventana de 5 años "
        "analizada. Una pista de varios años en el núcleo parece defendible; la desaceleración desde ~8% hacia "
        "un terminal de 3-4% en un horizonte de 10 años (usada en el DCF de la sección 12) es un supuesto "
        "<b>plausible pero no verificado mecánicamente</b> — ni heroico ni excesivamente conservador, pero "
        "tampoco confirmado con el dato que lo probaría.")]
    # Sin PageBreak aquí a propósito: este párrafo termina a ~30% de la página
    # y forzarlo dejaba el resto en blanco antes de la sección 8.
    return o
