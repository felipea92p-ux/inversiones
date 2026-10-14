# -*- coding: utf-8 -*-
"""15 · Cierre — predicciones falsables, glosario, advertencias"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, cm
from reportlab.platypus import PageBreak

def s15_cierre():
    o = flag_titulo("15 · Cierre",
                    "Predicciones falsables con fecha (Paso 12), glosario y advertencias finales")
    o += [p("Toda tesis de esta casa —se compre o no— registra predicciones con métrica, umbral y fecha, "
        "escritas antes de conocer el resultado. Es lo único que permite calificar el proceso más adelante en "
        "vez de calificar la suerte.")]
    o += [tabla([
        ["#", "PREDICCIÓN FALSABLE", "FECHA"],
        ["Principal<br/>(heredada del Paso 9)",
         "Si el ADV/interés abierto interanual cae de forma sostenida por debajo de +3% durante 2 o más "
         "trimestres consecutivos, la demanda ligada al régimen de «incertidumbre» se está normalizando: el "
         "crecimiento terminal de 3-4% que el mercado exige hoy dejaría de estar respaldado por la tendencia "
         "reciente, y el caso de «barato» quedaría debilitado, no confirmado.",
         "16-nov-2026 o los<br/>dos trimestres siguientes"],
        ["Secundaria<br/>(competitiva, Paso 8)",
         "Si el share de ADV de FMX en SOFR futures se mantiene por debajo de 1%, la tesis de moat intacto se "
         "refuerza; si supera 5% de forma sostenida en 2+ trimestres, la sección 5 (el foso) debe reabrirse "
         "antes de cualquier decisión de compra.",
         "10-K FY2026<br/>(~feb-2027)"],
        ["Secundaria-bis<br/>(falsable duro del abogado, Paso 10)",
         "Si en cualquier momento el share de FMX/Fenics en SOFR futures supera 3% del ADV combinado "
         "CME+FMX, sostenido durante un mes calendario completo —un salto de 10x sobre el máximo histórico "
         "conocido (0,3%)—, eso mata el pilar central del moat que sostiene el g terminal de 3,5%, y las "
         "secciones 5 y 12 deben reabrirse de inmediato. Umbral deliberadamente exigente para no ser un "
         "falsable barato, pero real y verificable mes a mes. Fuente de seguimiento: Clarus/FT o volumen "
         "publicado por CME Group.",
         "Antes del<br/>16-nov-2026"],
        ["Terciaria<br/>(concentración de cliente)",
         "Si el 10-K FY2026 reporta un tercer año consecutivo de concentración ≥10% en una sola clearing firm "
         "(tras 2024 y 2025), el patrón recurrente de línea base pasaría de «4 de 6 años» a «3 de 3 años "
         "consecutivos» — un cambio de régimen que ameritaría escalar la vigilancia del knock-out (e) a un peso "
         "mayor en el próximo pre-mortem.",
         "10-K FY2026<br/>(~feb-2027)"],
        ["Cuaternaria<br/>(pre-condición dura para COMPRAR, Paso 10)",
         "Antes de escalar a COMPRAR deben resolverse por escrito, con fecha: (a) el escenario bajista "
         "correlacionado (Rf −80pb + volumen/incertidumbre normalizándose + reversión parcial de margen), "
         "confirmando si su valor por acción queda por encima o por debajo de 200 US$; y (b) evidencia del "
         "comportamiento del margen operativo de CME en un trimestre de bajo volumen/volatilidad (análogo a "
         "2017), para verificar mecánicamente el g terminal de 3,5%. Sin ambas, un futuro COMPRAR no cumple el "
         "Candado A del método.",
         "Antes de cualquier<br/>reapertura a COMPRAR"]],
        [2.2*cm, 11.4*cm, 3.0*cm], font_sz=7.3)]
    o += [hr(), M.p("<b>GLOSARIO</b>", "h2")]
    terms = [
        ("Beta", "Cuánto se mueve una acción cuando se mueve el mercado. Beta 1 = igual; 0,5 = la mitad; 1,5 = amplifica. El de CME (0,27) es el input más disputado de todo el documento."),
        ("Candado A / B / C", "Los tres no negociables del método: (A) veto del abogado del diablo antes de toda compra; (B) WACC siempre bottom-up de mercado, nunca heredado de un tier de calidad; (C) prohibición de rankear sin pasar el test de ruido."),
        ("Compensación cruzada (cross-margining)", "Netear el riesgo de posiciones correlacionadas dentro de la misma cámara para exigir menos colateral. El mecanismo concreto detrás del Candado 1 del moat de CME."),
        ("Cámara de compensación (clearing house)", "La institución que se interpone entre comprador y vendedor de un futuro y garantiza a ambos. El negocio entero de CME."),
        ("DCF (descuento de flujos de caja)", "Proyectar el dinero futuro de una empresa y traerlo a valor de hoy con el coste de capital."),
        ("DCF inverso", "En vez de proyectar flujos para hallar un valor, se parte del precio actual para hallar qué crecimiento tendría que cumplirse para justificarlo."),
        ("Knock-out binario", "Un hecho que, de activarse, mata la tesis sin necesidad de más análisis (Paso 2 del método)."),
        ("Owner earnings", "Flujo de caja libre menos retribución en acciones (SBC) — la aproximación de Buffett al beneficio real distribuible."),
        ["Pre-mortem", "Imaginar que la inversión ya fracasó y escribir la autopsia — antes de invertir, no después, con métrica y fecha."],
        ("ROIC", "Retorno sobre el capital invertido — si una empresa crea o destruye valor con el dinero que emplea."),
        ("Tasa de reinversión", "Capex de crecimiento (capex total menos depreciación de mantenimiento) dividido entre NOPAT. En CME, negativa los cinco años analizados."),
        ("WACC (coste de capital)", "La rentabilidad mínima que un inversor exige para asumir el riesgo de una empresa. Bono sin riesgo + prima de mercado × beta, ponderado por la estructura de capital."),
    ]
    o += [tabla([["TÉRMINO", "QUÉ SIGNIFICA"]] + [[f"<b>{a}</b>", b] for a, b in terms],
                [4.2*cm, 12.4*cm], font_sz=8.0)]
    o += [M.hr(), M.p("<b>ADVERTENCIAS Y HUECOS DECLARADOS</b>", "h2")]
    o += [p("<b>Etiquetado de la evidencia.</b> Todo dato de este documento procede de una de tres categorías: "
        "<b>HECHO</b> (fuente primaria: 10-K, 10-Q, DEF 14A, 8-K, Forms 4 de la SEC, con documento y fecha), "
        "<b>INFERENCIA</b> (cálculo propio o dato de agregador) y <b>SUPUESTO</b> (asunción justificada). Un "
        "dato clave sin verificar degrada la cifra correspondiente; el veredicto máximo sobre una cifra "
        "degradada es VIGILAR, nunca COMPRAR.")]
    o += [p("<b>Huecos de evidencia abiertos, en orden de importancia:</b>")]
    o += [tabla([
        ["#", "EL HUECO", "POR QUÉ IMPORTA"],
        ["1", "El escenario bajista correlacionado (tasas y volumen cayendo a la vez) no está calculado.",
         "Pre-condición dura antes de COMPRAR (sección 14). Podría situar el bajista por debajo de 154 US$."],
        ["2", "El comportamiento del margen operativo en un trimestre de bajo volumen no está en los hechos disponibles.",
         "Es el único dato que verificaría mecánicamente el g terminal de 3,5% usado en el caso base."],
        ["3", "El dato de share de FMX en SOFR futures tiene más de un año de antigüedad.",
         "Presupuesto de búsqueda web agotado. Cubierto por el falsable duro reforzado de esta sección."],
        ["4", "No se distingue si la concentración de clearing firm es un cliente acumulando o clientes rotando.",
         "Afecta el peso que debe dársele al mecanismo 4 del pre-mortem (sección 11)."],
        ["5", "No se cubrieron comentarios directos de Deutsche Börse o LSEG en el scuttlebutt.",
         "Presupuesto de scuttlebutt agotado antes de llegar a esas fuentes."]],
        [0.7*cm, 7.6*cm, 8.2*cm], font_sz=7.7)]
    o += [callout("PAUSA REFLEXIVA",
        "<b>Qué queda pendiente de que Felipe complete o ratifique personalmente</b> antes de que este "
        "documento pueda tratarse como definitivo: el monólogo previo (Paso 0), el círculo de competencia "
        "(Paso 1) y la percepción variante (Paso 7) — los tres marcados como borrador de agente en las "
        "secciones donde aparecen. El veto del abogado del diablo (Paso 10) ya se ejecutó en sesión limpia y su "
        "resultado ya está incorporado; no depende del juicio personal de Felipe para tener validez.")]
    o += [M.hr()]
    o += [p("<i>Documento de trabajo personal, 4 de septiembre de 2026. No es asesoramiento de inversión, no "
        "procede de un asesor registrado y no debe usarse como recomendación para terceros. Rentabilidades "
        "pasadas no garantizan rentabilidades futuras. Fuentes primarias: cinco 10-K FY2021-FY2025, XBRL "
        "(companyfacts), DEF 14A 2026, Forms 4 (jun-2025 a jun-2026). Fuentes de mercado: stockanalysis.com, "
        "Yahoo Finance, GuruFocus, Damodaran/NYU Stern (ERP), Treasury.gov (UST 10y), FRED (índice ICE BofA AA "
        "US Corporate) — consultadas 2026-09-03/04. Limitaciones de acceso declaradas: Quartr sin suscripción "
        "activa, Bigdata.com agotado de créditos, presupuesto de WebSearch de la sesión agotado — toda la "
        "investigación primaria se reconstruyó vía SEC EDGAR directo.</i>", "nota")]
    return o
