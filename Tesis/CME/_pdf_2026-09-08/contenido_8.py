# -*- coding: utf-8 -*-
"""15 · Diario — predicciones falsables · 16 · Cierre"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, cm
from reportlab.platypus import PageBreak

def s15_diario():
    o = flag_titulo("15 · Diario",
                    "Predicciones falsables con fecha (Paso 12) — incluyendo las dos que añade esta actualización del 8-sep")
    o += [p("Toda tesis de esta casa —se compre o no— registra predicciones con métrica, umbral y fecha, "
        "escritas antes de conocer el resultado. Es lo único que permite calificar el proceso más adelante en "
        "vez de calificar la suerte. Las dos últimas de la tabla son nuevas, escritas hoy, y quedan tan "
        "expuestas a quedar mal como cualquiera de las heredadas del 4-sep.")]
    o += [tabla([
        ["#", "PREDICCIÓN FALSABLE", "FECHA"],
        ["1 · Principal<br/>(Paso 9)",
         "Si el ADV/interés abierto interanual cae de forma sostenida por debajo de +3% durante 2 o más "
         "trimestres consecutivos, la demanda ligada al régimen de «incertidumbre» se está normalizando: el "
         "crecimiento terminal de 3-4% que el mercado exige hoy dejaría de estar respaldado por la tendencia "
         "reciente, y el caso de «barato» quedaría debilitado, no confirmado.",
         "16-nov-2026 o los<br/>dos trimestres siguientes"],
        ["2 · Secundaria<br/>(Paso 8)",
         "Si el share de ADV de FMX en SOFR futures se mantiene por debajo de 1%, la tesis de moat intacto se "
         "refuerza; si supera 5% de forma sostenida en 2+ trimestres, la sección 5 (el foso) debe reabrirse "
         "antes de cualquier decisión de compra.",
         "10-K FY2026<br/>(~feb-2027)"],
        ["3 · Bis<br/>(Ronda 1)",
         "Si en cualquier momento el share de FMX/Fenics en SOFR futures supera 3% del ADV combinado "
         "CME+FMX, sostenido durante un mes calendario completo —un salto de 10x sobre el máximo histórico "
         "conocido (0,3%)—, eso mata el pilar central del moat que sostiene el g terminal de 3,5%, y las "
         "secciones 5 y 12 deben reabrirse de inmediato. Fuente de seguimiento: Clarus/FT o volumen publicado "
         "por CME Group.",
         "Antes del<br/>16-nov-2026"],
        ["4 · Terciaria<br/>(cliente)",
         "Si el 10-K FY2026 reporta un tercer año consecutivo de concentración ≥10% en una sola clearing firm "
         "(tras 2024 y 2025), el patrón recurrente de línea base pasaría de «4 de 6 años» a «3 de 3 años "
         "consecutivos» — un cambio de régimen que ameritaría escalar la vigilancia del knock-out (e) a un peso "
         "mayor en el próximo pre-mortem.",
         "10-K FY2026<br/>(~feb-2027)"],
        ["5 · Cuaternaria<br/>(pre-condición<br/>COMPRAR)",
         "Antes de escalar a COMPRAR deben resolverse por escrito, con fecha: (a) el escenario bajista "
         "correlacionado (Rf −80pb + volumen/incertidumbre normalizándose + reversión parcial de margen), "
         "confirmando si su valor por acción queda por encima o por debajo de 200 US$; y (b) evidencia del "
         "comportamiento del margen operativo de CME en un trimestre de bajo volumen/volatilidad (análogo a "
         "2017), para verificar mecánicamente el g terminal de 3,5%. Sin ambas, un futuro COMPRAR no cumple el "
         "Candado A del método.",
         "Antes de cualquier<br/>reapertura a COMPRAR"],
        ["6 · Quinta<br/>(NUEVA 8-sep,<br/>beta)",
         "Si la próxima medición de beta bursátil de CME (ventana de mercado renovada, ~sep-2027) converge "
         "hacia el rango 0,60-0,70 —cerca del promedio de pares (0,65) y del sectorial de Damodaran (0,66)—, "
         "la corrección de hoy queda confirmada como estructural, no como ruido de un solo día. Si en cambio "
         "retrocede por debajo de 0,40 sin que el perfil competitivo de CME haya mejorado de forma verificable "
         "(FMX contenido, Kalshi resuelto), la corrección de hoy debe reabrirse: podría ser ella misma un "
         "sobre-ajuste puntual, no una medición mejor.",
         "~Sep-2027<br/>(próxima ventana de beta)"],
        ["7 · Sexta<br/>(NUEVA 8-sep,<br/>ERP)",
         "Si el ERP implícito vigente de Damodaran subiera lo suficiente para que el WACC estresado —calculado "
         "con el beta más agresivo de los 4 pares (NDAQ, 0,97)— superase el ROIC de CME (~9,6%), el knock-out "
         "(c) debe reabrirse de inmediato, con la misma urgencia que si el ROIC hubiera caído. Hoy ese WACC "
         "estresado (≈8,99%) deja un colchón de apenas 0,6pp bajo el ROIC — el margen más estrecho de los tres "
         "knock-outs de esta tesis.",
         "Cada actualización<br/>trimestral del ERP"]],
        [2.6*cm, 10.7*cm, 3.3*cm], font_sz=7.3)]
    # Sin PageBreak aquí a propósito: la tabla de predicciones se corta de forma
    # natural dejando solo 2 filas en la página siguiente; forzar un salto justo
    # después desperdiciaba el resto de esa página antes de la sección 16.
    return o

def s16_cierre():
    o = flag_titulo("16 · Cierre",
                    "Glosario y advertencias finales")
    o += [hr(), M.p("<b>GLOSARIO</b>", "h2")]
    terms = [
        ("Beta", "Cuánto se mueve una acción cuando se mueve el mercado. Beta 1 = igual; 0,5 = la mitad; 1,5 = amplifica. El de CME pasó de 0,27 (input más disputado del documento del 4-sep) a 0,65 (corregido, promedio de 4 pares, validado contra Damodaran)."),
        ("Beta baja = momentum circular", "Sesgo ya fichado en el marco de inversión de Felipe: una beta medida sobre un valor en calma retroalimenta un WACC artificialmente bajo, que a su vez «crea» un margen de seguridad que no existe. Confirmado hoy 5 de 5 en un lote de cinco tesis distintas."),
        ("Candado A / B / C", "Los tres no negociables del método: (A) veto del abogado del diablo antes de toda compra; (B) WACC siempre bottom-up de mercado, nunca heredado de un tier de calidad; (C) prohibición de rankear sin pasar el test de ruido."),
        ("Compensación cruzada (cross-margining)", "Netear el riesgo de posiciones correlacionadas dentro de la misma cámara para exigir menos colateral. El mecanismo concreto detrás del Candado 1 del moat de CME."),
        ("Cámara de compensación (clearing house)", "La institución que se interpone entre comprador y vendedor de un futuro y garantiza a ambos. El negocio entero de CME."),
        ("DCF (descuento de flujos de caja)", "Proyectar el dinero futuro de una empresa y traerlo a valor de hoy con el coste de capital."),
        ("DCF inverso", "En vez de proyectar flujos para hallar un valor, se parte del precio actual para hallar qué crecimiento tendría que cumplirse para justificarlo."),
        ("ERP (prima de riesgo de mercado)", "La rentabilidad extra que un inversor exige por asumir el riesgo de la bolsa en vez de un bono sin riesgo. Usar un ERP mal calibrado puede exagerar el WACC estresado en cualquier dirección, como casi ocurrió en la Ronda 2 de esta tesis (sección 13)."),
        ("Knock-out binario", "Un hecho que, de activarse, mata la tesis sin necesidad de más análisis (Paso 2 del método)."),
        ("Owner earnings", "Flujo de caja libre menos retribución en acciones (SBC) — la aproximación de Buffett al beneficio real distribuible."),
        ("Pre-mortem", "Imaginar que la inversión ya fracasó y escribir la autopsia — antes de invertir, no después, con métrica y fecha."),
        ("ROIC", "Retorno sobre el capital invertido — si una empresa crea o destruye valor con el dinero que emplea."),
        ("Tasa de reinversión", "Capex de crecimiento (capex total menos depreciación de mantenimiento) dividido entre NOPAT. En CME, negativa los cinco años analizados."),
        ("WACC (coste de capital)", "La rentabilidad mínima que un inversor exige para asumir el riesgo de una empresa. Bono sin riesgo + prima de mercado × beta, ponderado por la estructura de capital. El de CME subió de 6,49% a 7,61% con la corrección de beta del 8-sep."),
    ]
    o += [tabla([["TÉRMINO", "QUÉ SIGNIFICA"]] + [[f"<b>{a}</b>", b] for a, b in terms],
                [4.2*cm, 12.4*cm], font_sz=7.9)]
    o += [M.hr(), M.p("<b>ADVERTENCIAS Y HUECOS DECLARADOS</b>", "h2")]
    o += [p("<b>Etiquetado de la evidencia.</b> Todo dato de este documento procede de una de tres categorías: "
        "<b>HECHO</b> (fuente primaria: 10-K, 10-Q, DEF 14A, 8-K, Forms 4 de la SEC, con documento y fecha), "
        "<b>INFERENCIA</b> (cálculo propio o dato de agregador) y <b>SUPUESTO</b> (asunción justificada). Un "
        "dato clave sin verificar degrada la cifra correspondiente; el veredicto máximo sobre una cifra "
        "degradada es VIGILAR, nunca COMPRAR.")]
    o += [p("<b>Huecos de evidencia abiertos, en orden de importancia:</b>")]
    o += [tabla([
        ["#", "EL HUECO", "POR QUÉ IMPORTA"],
        ["1", "El escenario bajista correlacionado (tasas y volumen cayendo a la vez) no está calculado — sigue "
              "sin resolverse tras la corrección de beta del 8-sep.",
         "Pre-condición dura antes de COMPRAR (sección 14). Podría situar el bajista por debajo de 154 US$."],
        ["2", "El comportamiento del margen operativo en un trimestre de bajo volumen no está en los hechos disponibles.",
         "Es el único dato que verificaría mecánicamente el g terminal de 3,5% usado en el caso base del 4-sep."],
        ["3", "El dato de share de FMX en SOFR futures tiene más de un año de antigüedad.",
         "Presupuesto de búsqueda web agotado. Cubierto por el falsable duro reforzado de la sección 15."],
        ["4", "No se distingue si la concentración de clearing firm es un cliente acumulando o clientes rotando.",
         "Afecta el peso que debe dársele al mecanismo 4 del pre-mortem (sección 11)."],
        ["5", "No se cubrieron comentarios directos de Deutsche Börse o LSEG en el scuttlebutt.",
         "Presupuesto de scuttlebutt agotado antes de llegar a esas fuentes."],
        ["6", "El valor intrínseco corregido (338,79 US$) y el caso base original (357 US$) proceden de dos "
              "modelos DCF independientes, no del mismo modelo con un solo input cambiado.",
         "Nueva desde el 8-sep. Ambas cifras quedan documentadas por separado en la sección 12 para no "
              "confundir dos construcciones distintas con una sola cifra definitiva."]],
        [0.7*cm, 7.6*cm, 8.2*cm], font_sz=7.5)]
    o += [callout("PAUSA REFLEXIVA",
        "<b>Qué queda pendiente de que Felipe complete o ratifique personalmente</b> antes de que este "
        "documento pueda tratarse como definitivo: el monólogo previo (Paso 0), el círculo de competencia "
        "(Paso 1) y la percepción variante (Paso 7) — los tres marcados como borrador de agente en las "
        "secciones donde aparecen. Las dos rondas del abogado del diablo (4-sep y 8-sep) ya se ejecutaron en "
        "sesión limpia y sus resultados ya están incorporados; no dependen del juicio personal de Felipe para "
        "tener validez.")]
    o += [M.hr()]
    o += [p("<i>Documento de trabajo personal, 8 de septiembre de 2026 — segunda actualización sobre la síntesis "
        "del 4-sep-2026. No es asesoramiento de inversión, no procede de un asesor registrado y no debe usarse "
        "como recomendación para terceros. Rentabilidades pasadas no garantizan rentabilidades futuras. Fuentes "
        "primarias: cinco 10-K FY2021-FY2025, XBRL (companyfacts), DEF 14A 2026, Forms 4 (jun-2025 a jun-2026). "
        "Fuentes de mercado: stockanalysis.com, Yahoo Finance, GuruFocus, Damodaran/NYU Stern (ERP y beta "
        "sectorial, ene-2026), Treasury.gov (UST 10y), FRED (índice ICE BofA AA US Corporate) — consultadas "
        "2026-09-03/04 y 2026-09-08. Limitaciones de acceso declaradas: Quartr sin suscripción activa, "
        "Bigdata.com agotado de créditos, presupuesto de WebSearch de la sesión del 4-sep agotado — toda la "
        "investigación primaria se reconstruyó vía SEC EDGAR directo. La corrección de beta/WACC del 8-sep "
        "procede de una cross-validación independiente sobre un lote de cinco tesis, documentada en la "
        "Actualización 2026-09-08 del dossier fuente.</i>", "nota")]
    return o
