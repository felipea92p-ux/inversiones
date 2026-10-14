# -*- coding: utf-8 -*-
"""Contenido del informe: LOS 36 DE ULTRACALIDAD — ranking por mecanismo y valor intrínseco.
Separación estricta contenido/diseño: este archivo no define color ni tipografía, solo llama a motor_qg."""
import json
import motor_qg as M
from reportlab.platypus import Spacer, PageBreak, NextPageTemplate, KeepTogether
from reportlab.lib.units import cm

DATA_DIR = "../_trabajo"
filas = json.load(open(f"{DATA_DIR}/valor_intrinseco_v2_36_FINAL.json", encoding="utf-8"))
final36 = json.load(open(f"{DATA_DIR}/final36_v2.json", encoding="utf-8"))
BETA_TRAP = 0.85
FUERA = final36["fuera"]
por_ticker = {f["ticker"]: f for f in filas}
por_bloque = {1: [], 2: [], 3: []}
for f in final36["filas"]:
    por_bloque[f["bloque"]].append(f)

NOM_BLOQUE = {1: "INDESTRUCTIBLES", 2: "NÚCLEO", 3: "FRONTERA"}
SUB_BLOQUE = {
    1: "El mecanismo no tiene grieta medida — nivel 1 a 5 de la taxonomía, sin reloj arrancado.",
    2: "Economía igual de buena, pero con UN reloj ya fechado, o una medida clave degradada.",
    3: "Foso real y grande, con una grieta YA MEDIDA en filing — o donde el denominador no permite decidir.",
}
MARGEN = {1: "25%", 2: "30%", 3: "40%"}


def money(v, decimales=1):
    if v is None:
        return "—"
    s = f"{v:,.{decimales}f}"
    return s.replace(",", "@").replace(".", ",").replace("@", ".")


def pct(v, signo=True, decimales=1):
    if v is None:
        return "—"
    s = f"{v*100:+.{decimales}f}%" if signo else f"{v*100:.{decimales}f}%"
    return s.replace(".", ",")


def esc(s):
    return (str(s or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


# ═════════════════════════════════════════════════════════════════════
# PORTADA
# ═════════════════════════════════════════════════════════════════════
def portada():
    story = [Spacer(1, 5.2 * cm)]
    story.append(M.p(
        '<font size="27"><b>LOS 36 DE ULTRACALIDAD</b></font>', "h_seccion"))
    story.append(M.p(
        "Ranking por durabilidad del mecanismo · cruce con valor intrínseco por acción",
        "h_sub"))
    story.append(Spacer(1, 14))
    story.append(M.kpi_panel([
        ("36", "EMPRESAS", "de un universo de 485, tras knock-outs binarios"),
        ("108", "AGENTES", "fundamentos + WACC + verificación, tres por empresa"),
        ("8/36", "CON MARGEN", "sólo 2 sin nota al pie sobre su beta"),
    ]))
    story.append(Spacer(1, 22))
    story.append(M.p(
        "Este documento reconstruye el ranking de calidad del archivo QG usando la "
        "<b>durabilidad del mecanismo a diez años</b> como puerta de entrada — no un score "
        "financiero — y cruza cada una de las 36 con su <b>valor intrínseco por acción</b>, "
        "calculado con costo de capital (WACC) específico de cada empresa por CAPM real "
        "(beta, costo de deuda y estructura de capital propios, sin piso mínimo) y una "
        "proyección explícita de owner earnings año por año a diez años, verificada en "
        "sesión limpia contra filing primario.", "cuerpo"))
    story.append(M.p(
        "<i>Documento de método dentro del marco propio de Felipe. No es asesoramiento de "
        "inversión personalizado y no soy asesor registrado. Nada de lo que sigue autoriza "
        "una compra por sí solo. Cifras vivas fechadas al 3-sep-2026; caducan.</i>", "nota"))
    story.append(NextPageTemplate("Normal"))
    story.append(PageBreak())
    return story


# ═════════════════════════════════════════════════════════════════════
# VEREDICTO PRIMERO
# ═════════════════════════════════════════════════════════════════════
def veredicto():
    story = M.flag_titulo("Veredicto primero", "Antes de la lista, lo que hay que saber para leerla")
    story.append(M.callout("PAUSA REFLEXIVA",
        "<b>Ocho de las 36 muestran margen de seguridad hoy — pero sólo dos sin advertencia.</b> "
        "Una versión anterior de este cruce usaba una tasa de descuento única (9,70%) para las 36, y "
        "eso producía lecturas irónicas: Nvidia salía \"barata\" porque el modelo aceptaba un año 10 "
        "que implicaba 2,7 veces sus ingresos actuales; Google salía como burbuja (+262%) porque su "
        "owner earnings restaba el 100% del capex de IA como si nada de él generara ingreso futuro. "
        "Se rehizo con costo de capital (WACC) específico de cada empresa —beta real, costo de deuda "
        "real, estructura de capital real, sin piso mínimo— y una proyección explícita de owner "
        "earnings a diez años, año por año."))
    story.append(M.p(
        "El resultado corrigió las dos ironías: Nvidia pasó de \"margen de seguridad\" del 24,5% a una "
        "<b>prima del 139,0%</b> — cara, como la intuición ya sospechaba, reflejo de un WACC de 15,6% "
        "(beta real 2,2, volatilidad genuina). Google bajó de +262,1% a <b>+71,5%</b> al corregir el "
        "owner earnings de 46.200 a 95.700 millones de dólares, separando por fin el capex de "
        "mantenimiento del de expansión. Y aparecieron ocho negocios con descuento real, no dos.", "cuerpo"))
    story.append(M.p(
        "<b>Pero sin piso mínimo en el WACC, el riesgo que el propio método ya midió reaparece.</b> "
        "Seis de esas ocho tienen un beta por debajo de 0,85 — el mismo umbral que marcó a Valeant y "
        "Hershey como trampas de valor en la calibración histórica de este archivo. Un beta bajo baja "
        "el WACC, y un WACC más bajo infla mecánicamente el valor calculado. Sólo S&amp;P Global y "
        "Copart no llevan esa marca. Este documento es una priorización empresa por empresa, no una "
        "orden de compra.", "cuerpo"))
    story.append(PageBreak())
    return story


# ═════════════════════════════════════════════════════════════════════
# METODOLOGÍA
# ═════════════════════════════════════════════════════════════════════
def metodologia():
    story = M.flag_titulo("Cómo se construyó",
                          "La puerta es el mecanismo; el dinero sólo veta; el precio se investiga, no se calcula")
    story.append(M.p("<b>1 · La puerta de calidad no es un score financiero.</b> "
        "Un borrador anterior de este mismo ejercicio usaba ROIC y goodwill como filtro de calidad, y "
        "eso mide un balance, no un foso: por ahí se colaban empresas bajo asedio estructural y se "
        "quedaban fuera negocios con mecanismos genuinamente duraderos que nunca habían sido puntuados "
        "alto. La versión final usa la taxonomía de siete niveles de durabilidad del juicio comparativo "
        "ciego (validado con ρ=0,969 entre dos rondas independientes de ocho jueces).", "cuerpo"))

    tabla_niveles = [
        ["Nivel", "Qué significa"],
        ["1", "Sin vector de disputa — ni tecnológico, ni regulatorio, ni de contraparte"],
        ["2", "Candado de coordinación: para irse hay que mover dos poblaciones a la vez"],
        ["3", "Ausencia de destino: el cliente no tiene a dónde ir"],
        ["4", "Peaje con la tarifa en manos propias"],
        ["5", "Candado impuesto por un tercero que no cambia de opinión"],
        ["6", "Mecanismo fuerte con una grieta ya medida en filing"],
        ["7", "La tarifa la fija otro, o el foso hay que recomprarlo cada año — no es ultracalidad"],
    ]
    story.append(M.tabla(tabla_niveles, col_w=[1.6 * cm, 15.4 * cm]))
    story.append(Spacer(1, 10))

    story.append(M.p("<b>2 · El dinero sólo veta, nunca promueve.</b> "
        "Un negocio con mecanismo elite pero ROIC por debajo del coste de capital (9,70%) cae por "
        "knock-out, sin apelación — así salió Waste Management, con vertederos a 38 años de vida "
        "permitida pero ROIC del 8,2%. Y a la inversa: un ROIC altísimo con goodwill que es el 97-117% "
        "del capital empleado (Adobe, Cadence) no basta para entrar al bloque de mayor calidad si el "
        "mecanismo tiene un reloj arrancado o una grieta medida.", "cuerpo"))

    story.append(M.p("<b>3 · El valor intrínseco se investiga con TRES agentes, no se calcula "
        "mecánicamente.</b> Uno proyecta el owner earnings año por año a diez años —separando capex de "
        "mantenimiento del de crecimiento con evidencia real, nunca restando el 100% de un boom de "
        "inversión— con cada tramo justificado contra TAM o cuota de mercado, no extrapolado "
        "mecánicamente. Otro investiga el WACC específico de esa empresa por CAPM real: beta a cinco "
        "años, costo de deuda real, estructura de capital real, sin piso mínimo. Un tercero, en sesión "
        "limpia, refuta a los dos anteriores y audita explícitamente si el owner earnings del año 10 "
        "implica una cuota de mercado creíble. El precio no entra en ningún momento de este proceso — "
        "sólo se cruza al final.", "cuerpo"))

    story.append(M.p("<b>4 · El DCF que convierte la proyección en valor por acción.</b> "
        "Diez flujos explícitos de owner earnings descontados al WACC propio de la empresa, más un "
        "término terminal de Gordon sobre el flujo del año 10 a la tasa de crecimiento perpetuo (g∞) "
        "que el propio agente propuso y el verificador auditó. El capital empleado no entra en este "
        "cálculo — sólo el owner earnings, la deuda real y el exceso de caja sobre el 2% de las ventas, "
        "para pasar de valor de empresa a valor de patrimonio y de ahí a valor por acción.", "cuerpo"))
    story.append(PageBreak())
    return story


# ═════════════════════════════════════════════════════════════════════
# BLOQUES DE CALIDAD
# ═════════════════════════════════════════════════════════════════════
def bloque_seccion(b):
    story = M.flag_titulo(f"Bloque {b} — {NOM_BLOQUE[b]}",
                          f"{SUB_BLOQUE[b]}  ·  Margen de seguridad exigido: {MARGEN[b]}")
    rows = [["#", "Empresa", "Nivel", "Mecanismo", "Vector abierto"]]
    for f in sorted(por_bloque[b], key=lambda x: x["orden"]):
        rows.append([
            str(f["orden"]),
            f'<b>{esc(f["ticker"])}</b><br/><font size="7.4">{esc(f["nombre"])}</font>',
            str(f["nivel_mecanismo"]),
            esc(f["mecanismo"]),
            esc(f["vector_y_reloj"] or "Ninguno documentado en esta pasada"),
        ])
    story.append(M.tabla(rows, col_w=[0.8 * cm, 2.6 * cm, 1.35 * cm, 6.05 * cm, 6.2 * cm], font_sz=7.6))
    story.append(PageBreak())
    return story


# ═════════════════════════════════════════════════════════════════════
# VALOR INTRÍNSECO — tabla completa
# ═════════════════════════════════════════════════════════════════════
def valor_intrinseco():
    story = M.flag_titulo("Valor intrínseco por acción",
                          "Las 36, ordenadas de mayor margen de seguridad a mayor prima sobre el valor")
    story.append(M.chart("charts/premio_descuento_36.png", w_cm=16.6))
    story.append(Spacer(1, 8))

    ordenadas = sorted(filas, key=lambda x: x["premio_descuento_pct"])
    rows = [["#", "Empresa", "Bl.", "VI/acc. (US$)", "Precio (US$)", "Premio/desc.", "WACC", "Beta", "Conf."]]
    for i, f in enumerate(ordenadas, 1):
        conf = f["confianza_final"] or "MEDIA"
        beta = f.get("beta")
        marca = ""
        if beta is not None and beta < BETA_TRAP:
            marca += " ¹"
        if f.get("refuta_proyeccion"):
            marca += " ²"
        if f.get("refuta_wacc"):
            marca += " ³"
        rows.append([
            str(i),
            f'<b>{esc(f["ticker"])}</b><br/><font size="7.2">{esc(f["nombre"])}</font>',
            str(f["bloque"]),
            money(f["valor_intrinseco_x_accion_usd"]),
            money(f["precio_actual_usd"]),
            pct(f["premio_descuento_pct"]) + marca,
            pct(f["wacc"], False, 2),
            f'{beta:.2f}' if beta is not None else "—",
            conf,
        ])
    story.append(M.tabla(rows, col_w=[0.7*cm, 2.7*cm, 0.9*cm, 2.3*cm, 2.1*cm, 2.3*cm, 1.5*cm, 1.3*cm, 1.6*cm],
                          font_sz=7.2))
    story.append(Spacer(1, 6))
    story.append(M.p(
        "¹ Beta por debajo de 0,85 — el mismo umbral que marcó a Valeant y Hershey como trampas de valor "
        "en la calibración histórica del método; ver §La huella dactilar sospechosa. "
        "² El verificador sustituyó la proyección de owner earnings a 10 años del investigador por la suya. "
        "³ El verificador sustituyó el WACC (beta y/o costo de deuda) del investigador por el suyo.",
        "nota"))
    story.append(PageBreak())
    return story


def hallazgos_undervalued():
    story = M.flag_titulo("El día que el método se corrigió a sí mismo",
                          "Nvidia y Google, antes y después de escuchar la objeción correcta")
    story.append(M.p(
        "La versión anterior de este cruce tenía un problema: Nvidia salía con margen de seguridad "
        "—como si estuviera barata— y Google salía con una prima del 262%, como si fuera una burbuja "
        "evidente. Las dos lecturas eran, con toda probabilidad, equivocadas.", "cuerpo"))
    story.append(M.p("<b>Nvidia — de \"barata\" a +139,0% de prima</b>", "h3"))
    story.append(M.p(
        "El modelo anterior componía un crecimiento del 50-80% durante varios años y metía el último "
        "de esos años, ya inflado, en una fórmula de perpetuidad: el resultado implicaba un owner "
        "earnings 2,7 veces superior a los ingresos TOTALES actuales de la empresa. Al pedir una "
        "proyección explícita año por año, el verificador aceptó el año 1 —un crecimiento del 90%, "
        "verificado contra el consenso real de 47 analistas— pero recortó la cola: el año 10 sigue "
        "siendo extraordinario, pero ya no imposible. Con su nuevo costo de capital (15,6%, reflejo de "
        "un beta real de 2,2 y una volatilidad genuina), Nvidia pasó a cotizar con una prima del 139% "
        "sobre su valor calculado. Cara, no barata — la lectura que la intuición ya sospechaba.", "cuerpo"))
    story.append(M.p("<b>Google — de +262,1% a +71,5% de prima</b>", "h3"))
    story.append(M.p(
        "La fórmula estándar de owner earnings resta todo el gasto de capital, sin distinguir entre "
        "mantenimiento y expansión. Alphabet está en medio de la mayor construcción de infraestructura "
        "de su historia —centros de datos para inteligencia artificial— y esa fórmula trataba cada "
        "dólar de esa construcción como si fuera necesario sólo para sostener el negocio de hoy, no "
        "para hacerlo crecer mañana. Al separar el capex de mantenimiento del de crecimiento con "
        "evidencia real, el owner earnings de partida subió de 46.200 a <b>95.700 millones de "
        "dólares</b> — más del doble. La prima bajó de 262% a 71,5%. Sigue cara, pero ya no como una "
        "burbuja: como un negocio excelente que el mercado paga con entusiasmo, no con delirio.", "cuerpo"))
    story.append(M.callout("LECCIÓN TRANSFERIBLE",
        "Ningún modelo es mejor que las preguntas que se le hacen. La corrección de Nvidia y Google no "
        "vino de cambiar la filosofía del método — vino de someterlo a la misma pregunta que un buen "
        "analista le haría a un colega: «¿de verdad crees que esta empresa va a valer eso, o el número "
        "simplemente salió así?»"))
    story.append(PageBreak())
    return story


# ═════════════════════════════════════════════════════════════════════
# CORRECCIONES METODOLÓGICAS
# ═════════════════════════════════════════════════════════════════════
def correcciones():
    story = M.flag_titulo("Tres correcciones hechas antes de fiarse del número",
                          "Verificadas antes de publicar, no después de que alguien preguntara")
    story.append(M.p("<b>TSM cotiza como ADR.</b> Un ADR de Taiwan Semiconductor equivale a cinco "
        "acciones ordinarias. El precio de mercado es por ADR, pero el recuento de acciones que "
        "EDGAR reporta es de acciones ordinarias — sin dividir por cinco, el valor por acción salía "
        "artificialmente bajo por ese mismo factor. Corregido antes del cálculo final.", "cuerpo"))
    story.append(M.p("<b>Straumann se verificó dos veces.</b> La primera pasada no logró acceder al "
        "informe anual auditado (bloqueo 403 en el sitio de la empresa); una segunda verificación, en "
        "sesión limpia, sí entró y encontró que la relación mantenimiento/crecimiento del capex estaba "
        "invertida: el capex real supera la depreciación en los cinco años auditados 2021-2025, no al "
        "revés como asumió el primer investigador. El owner earnings y la deuda se corrigieron a la "
        "baja.", "cuerpo"))
    story.append(M.p("<b>CME tenía la deuda mal cargada.</b> El dato de referencia decía \"0,0 "
        "millones\"; el 10-K FY2025 real reporta USD 3.422,3 millones — el tramo de corto plazo (el "
        "único que era cero, porque venció en marzo de 2025) había reemplazado al total de deuda en la "
        "ficha original.", "cuerpo"))
    story.append(M.callout("LECCIÓN TRANSFERIBLE",
        "Ninguna de las tres correcciones cambió el veredicto de calidad de la empresa afectada. Todas "
        "cambiaron un número que, sin corregir, habría producido un valor intrínseco falso por un "
        "error mecánico — no por un juicio equivocado sobre el negocio. Esa es la distinción que "
        "separa una tesis de un cálculo que salió mal."))
    story.append(PageBreak())
    return story


def confianza_baja():
    story = M.flag_titulo("La huella dactilar sospechosa",
                          "Por qué seis de las ocho gangas comparten algo que no debería ignorarse")
    story.append(M.p(
        "Este mismo método ya estudió por qué Hershey y Valeant parecían apuestas seguras y terminaron "
        "en desastre: las dos tenían un beta sorprendentemente bajo, que hizo que la tasa de descuento "
        "pareciera más baja de lo que el riesgo real justificaba. Un beta bajo suele leerse como "
        "«riesgo bajo», y ese riesgo bajo se traduce en un WACC más bajo, que a su vez infla "
        "mecánicamente el valor calculado.", "cuerpo"))
    story.append(M.p(
        "En este cruce, <b>seis de las ocho empresas con descuento tienen un beta por debajo de "
        "0,85</b> — el mismo umbral que marcó a Valeant: Thomson Reuters (0,20), CME (0,27), OBIC "
        "(0,47), RELX (0,64), Constellation Software (0,69) y Mastercard (0,74). Sólo S&amp;P Global "
        "(1,08) y Copart (1,03) tienen un beta que no exige ninguna explicación adicional.", "cuerpo"))
    story.append(M.callout("PAUSA REFLEXIVA",
        "Esto NO significa que las seis estén rotas. Cada agente que investigó su costo de capital "
        "recibió la instrucción explícita de escrutinarlas con el mismo rigor que a Valeant, y en "
        "varios casos encontró una explicación estructural defendible: CME cobra más cuando el mercado "
        "entra en pánico, no menos, porque su negocio es cubrir riesgo. Constellation Software tiene "
        "deuda casi nula. Pero «defendible» no es «confirmado». El propio agente que investigó a "
        "Thomson Reuters escribió, sin que se le pidiera suavizarlo, que cualquier valoración que use "
        "ese WACC sin cuestionar el beta primero <b>sobrestimará el valor de forma material</b>."))
    story.append(PageBreak())
    return story


# ═════════════════════════════════════════════════════════════════════
# EXPULSADAS Y LÍMITES
# ═════════════════════════════════════════════════════════════════════
def expulsadas():
    story = M.flag_titulo("Las que cayeron, con su motivo",
                          "Nada se excluyó a priori — cada una cayó por un hecho fechado")
    rows = [["Ticker", "Motivo"]]
    for t, m in FUERA[:16]:
        rows.append([f"<b>{esc(t)}</b>", esc(m)])
    story.append(M.tabla(rows, col_w=[2.2 * cm, 14.8 * cm], font_sz=7.4))
    story.append(PageBreak())
    return story


def limites():
    story = M.flag_titulo("Límites declarados", "Lo que este documento no prueba")
    puntos = [
        "El valor intrínseco de este documento ya no usa una tasa única ni el motor mecánico de B4. "
        "Usa un engranaje nuevo — WACC específico por empresa (CAPM real) y proyección explícita de "
        "owner earnings a diez años — construido a pedido explícito de Felipe tras ver que la tasa "
        "única producía a Nvidia «barata» y a Google como burbuja. Nada de esto es ejecutable como "
        "orden de compra por sí solo.",
        "El WACC se investigó SIN piso mínimo — decisión explícita de Felipe, a sabiendas de que un "
        "beta bajo puede inflar el valor calculado. Seis de las ocho candidatas con descuento llevan "
        "esa marca (ver §La huella dactilar sospechosa); sólo dos (S&amp;P Global, Copart) no la "
        "necesitan.",
        "El chequeo de plausibilidad del año 10 se hizo contra ingresos y cuota de mercado — no "
        "contra una recesión, una disrupción tecnológica no anticipada, o un cambio regulatorio.",
        "La columna «Brecha*» de las tablas de bloque de calidad (páginas anteriores) es del motor "
        "mecánico ANTERIOR (DCF inverso de una sola tasa) y sigue degradada — no se usó en absoluto "
        "para calcular el valor intrínseco de la tabla de esta sección.",
        "Siete de las 36 dependen de una única fuente primaria no auditada de forma cruzada "
        "(informe anual, sin segundo filing): Hermès, Constellation Software, HOYA, OBIC, Adyen, "
        "Straumann y Keyence.",
        "La venta de DUOL sigue ordenada sin ejecutar. Se declara aquí porque el candado C-11 lo exige "
        "mientras exista una caducidad vencida sin cerrar.",
        "Cero validación externa: esto mide durabilidad y valor estimados, no rentabilidad futura.",
    ]
    for pt in puntos:
        story.append(M.p(f"•  {pt}", "cuerpo"))
    story.append(Spacer(1, 10))
    story.append(M.callout("CASO HISTÓRICO",
        "La pregunta de cierre de todo documento de este método: ¿qué pieza de información, si "
        "apareciera mañana, más cambiaría este veredicto? Aquí son dos: un beta recalculado con "
        "precios primarios (no de agregador) para las seis candidatas marcadas, y una segunda ronda "
        "de verificación sobre los WACC más bajos del cruce (CME 6,49%, OBIC 6,20%, Thomson Reuters "
        "6,30%) para confirmar si la explicación estructural que cada agente encontró resiste un "
        "segundo escrutinio tan a fondo como el que ya salvó y corrigió a Straumann."))
    return story
