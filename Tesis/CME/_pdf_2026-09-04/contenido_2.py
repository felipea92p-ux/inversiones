# -*- coding: utf-8 -*-
"""4 · El negocio explicado desde cero · 5 · El foso"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, cm
from reportlab.platypus import PageBreak

def s4_negocio():
    o = flag_titulo("4 · Qué hace CME, explicado desde cero",
                    "Círculo de competencia (Paso 1): si el mecanismo no cabe en una frase sin jerga, no se entiende de verdad")
    o += [p("Imagina a un fondo de pensiones que gestiona miles de millones y quiere protegerse de que suban "
        "los tipos de interés en Estados Unidos. Y al otro lado, un banco que quiere lo contrario: protegerse de "
        "que bajen. Los dos podrían buscarse el uno al otro y firmar un contrato directamente. Pero eso tiene un "
        "problema enorme: <b>¿y si dentro de seis meses, cuando toque liquidar, uno de los dos no puede pagar?</b> "
        "Nadie quiere depender de la solvencia de un desconocido al otro lado de un contrato a plazo.")]
    o += [p("<b>Ahí es donde se coloca CME, y ahí está todo el negocio.</b> CME se interpone entre las dos "
        "partes y se convierte en la contraparte de ambas: le compra al que vende y le vende al que compra. "
        "Ninguno de los dos tiene que confiar en el otro — sólo en CME. A cambio, exige que ambos depositen "
        "garantías antes de operar, y les cobra una comisión diminuta por cada contrato.")]
    o += [callout("EN ROMÁN PALADINO",
        "Propuesta de círculo de competencia, a ratificar o corregir por Felipe (Paso 1, borrador de agente): "
        "<i>«CME es el sitio donde la mayoría de los grandes traders de tasas y futuros del mundo compensan sus "
        "apuestas juntos, en la misma cámara; eso les permite necesitar menos colateral que si compensaran en "
        "dos sitios distintos, y por eso salirse de CME les sale caro en capital, no sólo en fee.»</i> Prueba "
        "del círculo de competencia: si Felipe no puede decir esto —o algo equivalente— sin mirar el dossier, "
        "el resto de la tesis debe tratarse con más escepticismo.")]
    o += [p("<b>El mecanismo concreto que hace que ese «depende menos colateral» sea real se llama compensación "
        "cruzada</b> (cross-margining, dentro del sistema SPAN de CME). Si un cliente tiene posiciones "
        "correlacionadas —por ejemplo, tasas SOFR, bonos del Tesoro, divisas e índices bursátiles— dentro de la "
        "<i>misma</i> cámara, CME puede netear el riesgo de unas contra otras y pedirle menos garantía en total. "
        "Si ese cliente traslada una sola de esas piezas a un rival, pierde el neteo y tiene que depositar "
        "colateral adicional real por todo lo que se queda en CME. <b>No es que cambiarse sea caro: es que el "
        "resto de tu cartera paga la factura de haberte ido.</b>")]
    o += [p("<b>La segunda pieza del mecanismo son los derechos de membresía.</b> Según el propio informe anual: "
        "<i>«Membership on one of our derivatives exchanges also enables customers to trade specific products at "
        "lower fees... In 2025, 85% of contract volume was from trades by members»</i> (HECHO, 10-K FY2025, "
        "pág. 6). El descuento no es por producto: es por relación completa con CME. Migrar el flujo de un solo "
        "producto arriesga el tier preferencial en toda la cuenta.")]
    o += [p("<b>Y aquí está el detalle que decide cuánto vale todo esto: a quién va el ahorro de escala.</b> "
        "El margen operativo de CME es del <b>64,9% GAAP / 69,4% ajustado</b> (2025, DEF 14A 2026) — márgenes de "
        "peaje, no de mercancía de consumo. CME transfiere eficiencia de capital a sus clientes (los "
        "72.000-95.000 millones de dólares diarios de ahorro de margen citados abajo), pero conserva el peaje "
        "en sí. En palabras del propio CEO, Terrence Duffy, en llamada de analistas: <i>«The cheapest cost to "
        "any participant is the transaction fee whereas the bid-offer is extremely expensive»</i> (HECHO, FOW, "
        "24-oct-2024).")]
    o += [p("<b>Lo que limita el crecimiento no es el capital.</b> La reinversión requerida es mínima —el propio "
        "10-K guía un capex 2026 de apenas <i>«approximately $85.0 million»</i>— por lo que CME no está "
        "restringida por acceso a capital (ver sección 7 para el detalle completo del motor de crecimiento). "
        "Lo que limita el negocio es cuánta incertidumbre, deuda y volatilidad hay en el mundo para negociar "
        "sobre ella: algo que CME no controla y que la propia gerencia citó como motor del crecimiento reciente "
        "en <b>9 de 9 llamadas trimestrales</b> analizadas (feb-2023 a jul-2026).")]
    return o + [PageBreak()]

def s5_foso():
    o = flag_titulo("5 · El foso: por qué el cliente no se va",
                    "Dos candados económicos específicos, y un precedente histórico de 2004 que ya los puso a prueba")
    o += [p("El mecanismo del moat de CME no es «liquidez» en abstracto: son dos candados económicos concretos, "
        "no transferibles a un rival sin años de acumulación de flujo, y hay que entenderlos por separado porque "
        "protegen cosas distintas.")]
    o += [p("<b>Candado 1 — compensación de margen entre productos correlacionados.</b> Ya descrito en la "
        "sección anterior: netear posiciones dentro de la misma cámara. El tamaño del beneficio que entrega, en "
        "dinero real: <b>ahorro diario promedio de margen ≈72.000 millones de dólares</b> (2025, 10-K FY2025, "
        "pág. 9), subiendo a <b>más de 95.000 millones al día</b> en el 2T-2026 (comunicado CME Group, "
        "22-jul-2026). Sólo el cross-margining con FICC/DTCC —la cámara de compensación de bonos del Tesoro— "
        "aporta <b>≈7.000 millones de dólares diarios</b> de ahorro adicional, con 12 miembros participantes a "
        "esa fecha (Suzanne Sprague, directora de operaciones, cita recogida por FOW, 24-oct-2024).")]
    o += [p("<b>Candado 2 — derechos de membresía exchange-specific.</b> El 85% del volumen de contratos en "
        "2025 provino de operaciones de miembros, que acceden a tarifas más bajas por el portafolio completo, "
        "no por producto (10-K FY2025, pág. 6, ya citado). Los dos candados se refuerzan entre sí: el ahorro de "
        "margen crece con la amplitud del portafolio que compensas en CME, y esa amplitud es exactamente lo que "
        "el tier de membresía premia.")]
    o += [callout("CASO HISTÓRICO",
        "<b>El precedente que este tipo de moat ya sobrevivió.</b> Eurex US lanzó contratos «look-alike» de "
        "futuros del Tesoro contra CBOT el 1 de febrero de 2004, con tarifas más bajas, identificando "
        "explícitamente el efecto de red de CBOT como la barrera a vencer. El desenlace, documentado en el "
        "propio caso judicial derivado (<i>U.S. Futures Exch., LLC v. Bd. of Trade of Chi., Inc.</i>) y en "
        "prensa especializada de la época: <i>«Eurex was never able to dent CBOT's dominance»</i>; Eurex US "
        "cesó operaciones en 2008 con menos del 1% de volumen capturado (HECHO, MarketsWiki, Finextra 2004). "
        "<b>Nota de precisión:</b> esto le ocurrió a CBOT antes de su fusión con CME en 2007 — la entidad legal "
        "no era CME, pero el mecanismo (red de liquidez concentrada + coste de fragmentación) es el mismo que "
        "opera hoy en la franquicia heredada.")]
    o += [p("<b>Y la disciplina obligatoria contra el entusiasmo: el propio CME perdió este juego una vez.</b> "
        "CME lanzó compensación de swaps de tasas de interés (IRS) en 2010 contra el dominio de LCH SwapClear. "
        "Hacia 2023, <b>LCH SwapClear seguía compensando ~98% del volumen de swaps IRS en dólares</b> "
        "(HECHO/INFERENCIA con matices de fuente, Risk.net). CME ganó tracción sólo en swaps denominados en "
        "reales brasileños y pesos mexicanos, no en el mercado grande de dólares.")]
    o += [callout("LA TRAMPA",
        "Este contraejemplo interno no es sólo una advertencia genérica: es el propio abogado del diablo quien, "
        "en el Paso 10, lo usó para argumentar que <b>cada expansión de mercado nueva que la tesis necesita "
        "para sostener su crecimiento futuro</b> —single stock futures, «compute futures», cripto 24/7— "
        "<b>enfrenta el mismo problema estructural que CME no resolvió en 13 años contra LCH: construir un pool "
        "de liquidez nuevo desde cero no hereda automáticamente el moat existente.</b> Esa lectura se aceptó sin "
        "diluir y queda incorporada aquí y en la sección 7 (el motor de crecimiento) y la sección 12 "
        "(valoración) — ver sección 13 para el detalle completo del intercambio con el abogado.")]
    o += [p("La conclusión de esta sección, antes de pasar al scuttlebutt: el moat protege con un mecanismo "
        "probado la franquicia núcleo (SOFR, Treasuries, y el resto del complejo de tasas e índices ya "
        "compensado en CME), pero no financia por sí solo el crecimiento hacia productos nuevos — esa es una "
        "carrera aparte, que CME no siempre gana. La sección 7 desarrolla la consecuencia exacta que esto tiene "
        "sobre el crecimiento terminal usado en la valoración.")]
    return o + [PageBreak()]
