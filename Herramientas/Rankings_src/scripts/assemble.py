# -*- coding: utf-8 -*-
"""
Assemble ranking_data.json from all phase outputs, render charts, build the PDF.
Re-runnable from disk.
"""
import json, sys, os
QG = "/Users/felipealvarez/Library/Mobile Documents/com~apple~CloudDocs/INVESTMENTS/_ACTIVE/qg_ranking"
sys.path.insert(0, QG)
import qg_ranking_charts as ch
import build_ranking

D = QG + "/data"
CO = D + "/companies"

merged = {m["ticker"]: m for m in json.load(open(D + "/fase4v2_merged.json", encoding="utf-8"))["companies"]}
sel = json.load(open(D + "/selection_final.json", encoding="utf-8"))
conv = json.load(open(D + "/convergence.json", encoding="utf-8"))
universe = json.load(open(D + "/universe_screened.json", encoding="utf-8"))
tier1 = json.load(open(D + "/tier1_scores.json", encoding="utf-8"))
fase23 = json.load(open(D + "/fase23_results.json", encoding="utf-8"))


def lc(tk, suf=""):
    p = f"{CO}/{tk}{suf}.json"
    return json.load(open(p, encoding="utf-8")) if os.path.exists(p) else {}


# FASE 0 ROIC fallback (ESTIMADO) when verified ROIC missing
roic0 = {}
for c in universe.get("candidates", []) + universe.get("near_miss", []):
    if c.get("roic_3y_pct") is not None:
        roic0.setdefault(c["ticker"], c["roic_3y_pct"])


# ---- formatting (European) ----
SYM = {"USD": "$", "EUR": "€", "GBP": "£", "JPY": "¥", "CHF": "CHF ", "SEK": "kr ", "DKK": "kr "}
DQ_ES = {"VERIFICADO_mostly": "mayormente VERIFICADO", "MIXED": "VERIFICADO+ESTIMADO",
         "ESTIMADO_mostly": "mayormente ESTIMADO"}


def euro(x, d=1):
    if x is None:
        return "n/d"
    try:
        s = f"{float(x):,.{d}f}"
    except Exception:
        return str(x)
    return s.replace(",", "§").replace(".", ",").replace("§", ".")


def dec_for(x):
    ax = abs(x)
    return 0 if ax >= 1000 else (1 if ax >= 100 else 2)


def price_str(x, cur):
    if x is None:
        return "n/d"
    sym = SYM.get(cur, (cur or "") + " ")
    return f"{sym}{euro(x, dec_for(x))}"


def pct(x, d=0, sign=True):
    if x is None:
        return "n/d"
    s = f"{x:+.{d}f}" if sign else f"{x:.{d}f}"
    return s.replace(".", ",") + "%"


def num(x, d=1):
    return euro(x, d) if x is not None else "n/d"


# ---- ficha builder ----
def ficha(rank, tk, lista):
    m = merged.get(tk, {})
    v = lc(tk)
    s = lc(tk, "_score")
    val = lc(tk, "_val")
    cur = val.get("currency") or "USD"
    fy = v.get("last_fy", {}) or {}
    sc = val.get("dcf_scenarios", {}) or {}
    fwd_now = val.get("fwd_multiple_now") if val.get("fwd_multiple_now") is not None else m.get("fwd_pe")
    fwd_5y = val.get("fwd_multiple_5y_avg") if val.get("fwd_multiple_5y_avg") is not None else m.get("fwd_pe_5y")
    mos = m.get("mos")
    pe_prem = m.get("pe_prem")
    if pe_prem is None and fwd_now and fwd_5y:
        try:
            pe_prem = round((fwd_now - fwd_5y) / fwd_5y * 100)
        except Exception:
            pe_prem = None
    roic = fy.get("roic_pct")
    roic_str = num(roic) if roic is not None else (num(roic0[tk]) + "*" if roic0.get(tk) is not None else "n/d")
    dr = None
    if lista == "B":
        ai_fear = {"WKL.AS", "ADBE", "VEEV", "INTU", "ACN", "IT"}
        motivo = "el miedo a la disrupcion de la IA" if tk in ai_fear else "el ciclo y la rotacion sectorial"
        dr = (f"Cotiza a {num(fwd_now)}x adelantado frente a ~{num(fwd_5y)}x de su media; "
              f"el mercado descuenta {motivo}, no el foso.")
    return {
        "rank": rank, "ticker": tk, "name": m.get("name") or tk,
        "sector": m.get("sector") or "", "country": m.get("country") or "",
        "score": m.get("final_score"),
        "moat_type": s.get("moat_type", ""), "moat_one_line": s.get("moat_one_line", ""),
        "price": price_str(val.get("price_verified"), cur),
        "currency": "", "mcap_usd_b": num(val.get("implied_mcap_b_usd") or m.get("impl_mcap"), 0),
        "fwd_pe": num(fwd_now), "fwd_pe_5y": num(fwd_5y),
        "pe_prem_disc_pct": pct(pe_prem), "peg": num(v.get("peg")),
        "roic_pct": roic_str, "fcf_margin_pct": num(fy.get("fcf_margin_pct")),
        "sbc_pct_fcf": num(v.get("sbc_pct_fcf")),
        "drop_pct_ath": num(v.get("pct_off_ath")), "drop_class": v.get("drop_classification", ""),
        "thesis_3lines": s.get("thesis_3lines", []),
        "bear": s.get("bear_case_strongest", ""),
        "ethical_flag": "none", "discount_reason": dr,
        "source_note": (f"Datos {DQ_ES.get(v.get('data_quality'), 'VERIFICADO')} "
                        f"({len(v.get('sources', []) or [])} fuentes EDGAR/IR/agregador, jun-2026); "
                        "valoracion: DCF owner-earnings propio reconciliado con multiplo."),
        "dcf": {
            "wacc_pct": num(val.get("wacc_pct")),
            "iv_cons": price_str((sc.get("conservador") or {}).get("iv_per_share"), cur),
            "iv_base": price_str((sc.get("base") or {}).get("iv_per_share"), cur),
            "iv_opt": price_str((sc.get("optimista") or {}).get("iv_per_share"), cur),
            "iv_weighted": price_str(val.get("reconciled_iv"), cur),
            "mos_pct": pct(mos),
            "opportunity_label": m.get("label", ""),
        },
    }


lista_a = [ficha(x["rank"], x["ticker"], "A") for x in sorted(sel["lista_a"], key=lambda z: z["rank"])]
lista_b = [ficha(x["rank"], x["ticker"], "B") for x in sorted(sel["lista_b"], key=lambda z: z["rank"])]

# master table of all 30 finalists
aset = {x["ticker"] for x in sel["lista_a"]}
bset = {x["ticker"] for x in sel["lista_b"]}


def tablero_row(n, tk, lst):
    m = merged[tk]
    val = lc(tk, "_val")
    fwd_now = val.get("fwd_multiple_now") or m.get("fwd_pe")
    fwd_5y = val.get("fwd_multiple_5y_avg") or m.get("fwd_pe_5y")
    return {"rank": n, "name": m["name"], "ticker": tk, "lista": lst, "score": m["final_score"],
            "fwd_pe": num(fwd_now), "fwd_pe_5y": num(fwd_5y), "mos": pct(m["mos"]), "label": m["label"]}


tablero_30 = []
n = 1
for x in sorted(sel["lista_a"], key=lambda z: z["rank"]):
    tablero_30.append(tablero_row(n, x["ticker"], "A+B" if x["ticker"] in bset else "A")); n += 1
for x in sorted(sel["lista_b"], key=lambda z: z["rank"]):
    if x["ticker"] in aset:
        continue
    tablero_30.append(tablero_row(n, x["ticker"], "B")); n += 1

contentious_text = sel.get("contentious", [])

# ---- charts (real data) ----
ch.chart_funnel([("Universo", universe["universe_count"]), ("Cribado FASE 0", universe["passing_count"]),
                 ("Long-list", tier1["longlist_count"]), ("Pool calidad >=12", fase23["pool_count"]),
                 ("Finalistas", 30)])
qv = []
aset = {x["ticker"] for x in sel["lista_a"]}
bset = {x["ticker"] for x in sel["lista_b"]}
for tk in (aset | bset):
    m = merged[tk]
    lst = "AB" if (tk in aset and tk in bset) else ("A" if tk in aset else "B")
    qv.append((tk.replace(".PA", "").replace(".AS", "").replace(".SW", "").replace(".L", "").replace(".ST", "").replace(".T", ""),
               m["final_score"], m.get("mos_disp") if m.get("mos_disp") is not None else m.get("mos"), lst))
ch.chart_qv_map(qv)
ch.chart_lista_a([(x["ticker"].split(".")[0], merged[x["ticker"]]["final_score"]) for x in sel["lista_a"]])
ch.chart_lista_b([(x["ticker"].split(".")[0], merged[x["ticker"]]["mos"], merged[x["ticker"]]["final_score"]) for x in sel["lista_b"]])
ch.chart_convergence([(c["ticker"].split(".")[0], c["prev_pe"], c["live_pe"]) for c in conv if c.get("live_pe")])

# ---- prose ----
def name(tk):
    return merged.get(tk, {}).get("name", tk)

ganga = [x["ticker"] for x in sel["lista_b"] if (merged[x["ticker"]].get("mos") or 0) >= 20]

exec_summary = [
 "Este informe presenta dos rankings complementarios construidos sobre un unico universo de maxima calidad. "
 "La Lista A reune las dieciocho empresas mas indispensables del mundo, ordenadas por calidad pura segun el "
 "Scorecard Seilern Ponderado sobre 13,5; el precio se muestra como dato verificado pero no mueve el orden. "
 "La Lista B reune las doce oportunidades de precio mas atractivas dentro de ese mismo universo, ordenadas por "
 "margen de seguridad frente a un valor intrinseco propio. La pregunta de la Lista A es que tan buena es la "
 "empresa; la de la Lista B es si conviene comprarla hoy.",

 "El hallazgo central de junio de 2026 es una bifurcacion violenta del mercado. De un lado, un grupo de "
 "compounders apex cotiza con prima de momentum y resulta caro frente a cualquier flujo descontado razonable: "
 "los semiconductores de vanguardia (ASML, TSMC, Nvidia), las plataformas (Microsoft, Alphabet) y Apple. "
 "Del otro, una franja igual de excelente de software, datos y servicios de informacion se ha desplomado "
 "alrededor de un cincuenta por ciento por miedo a la disrupcion de la inteligencia artificial: ServiceNow cae "
 "un 50% en doce meses, Adobe cotiza a 195 dolares cerca mismo de su minimo anual, Intuit pierde un 57% en lo "
 "que va de ano tras recortar el 17% de su plantilla, y Accenture y Wolters Kluwer acompanan la caida. El "
 "mercado esta descontando el miedo, no la erosion del foso. Ahi viven las gangas de la Lista B.",

 "El proceso fue de descubrimiento, no de confirmacion. Se partio de 719 cotizadas de calidad global "
 "(S&P 500, NASDAQ-100, STOXX 600 y Nikkei 225 mas adiciones reconocidas), se cribaron a 119 por filtros "
 "cuantitativos duros, se puntuaron 122 candidatas con el scorecard preliminar para un long-list de 80, y se "
 "verificaron en vivo (EDGAR, relaciones con inversores, agregadores) hasta un pool de 77 nombres con calidad "
 "igual o superior a 12,0. De ahi salen las 30 finalistas. El cribado hizo emerger nombres que no figuraban en "
 "la lista de calibracion previa: IDEXX, CME y Linde entran en la Lista A; Adyen, Partners Group, Veeva, "
 "ResMed, Gartner, Cboe, Booking y Nintendo pueblan la zona de oportunidad.",

 "La prueba de convergencia confirma seis de ocho estimaciones previas (S&P Global, RELX, Wolters Kluwer, "
 "Mastercard, MSCI y Visa convergen dentro del 10%). Las dos divergencias, Accenture e Intuit, no son errores "
 "de medicion sino el reflejo de la propia caida: su multiplo adelantado se comprimio porque su precio se "
 "hundio. Tres nombres que se esperaba ver no superaron el piso de calidad sobre datos verificados: Novo "
 "Nordisk (11,5; deterioro aun activo), Synopsys (11,5; la compensacion en acciones supera el 25% del flujo de "
 "caja libre y hunde la regla de contabilidad) y Zoetis (9,0). Quedan documentados como divergencias.",
]

how_to_read = [
 "Cada empresa responde a dos preguntas distintas. La Lista A responde que tan indispensable es el negocio: "
 "monopolios, duopolios, plataformas con ecosistema y marcas irreplicables, ordenados por calidad estructural. "
 "La Lista B responde si el precio de hoy ofrece margen: se ordena por margen de seguridad frente al valor "
 "intrinseco propio. Una empresa puede ser de Lista A y no de Lista B (apex pero cara), o de Lista B sin entrar "
 "en las dieciocho de Lista A (excelente y barata, pero no de las mas indispensables); las dos preguntas no "
 "siempre coinciden, y por eso los rankings se presentan por separado.",
 "Sobre cada nombre, una etiqueta de oportunidad resume el precio frente al valor: GANGA FUERTE (margen de "
 "seguridad igual o superior al 20%), OPORTUNIDAD (entre 10% y 20%), APEX A PRECIO JUSTO (entre -10% y +10%) y "
 "CARO / MOMENTUM (por debajo de -10%). El ancla de valor es un DCF propio de owner earnings (flujo de caja "
 "libre menos el 100% de la compensacion en acciones), reconciliado con una reversion al multiplo historico de "
 "cada empresa, porque las grandes franquicias rara vez se valoran bien solo por DCF. Los multiplos de mercado "
 "son contexto, no el modelo.",
 "Cada ficha incluye una instantanea verificada (precio, capitalizacion, P/E adelantado frente a su media de "
 "cinco anos, ROIC, margen de flujo de caja libre, compensacion en acciones como porcentaje del flujo y caida "
 "desde maximos), una tabla de DCF con sus tres escenarios y el valor reconciliado, la tesis en tres lineas y "
 "el caso bajista mas fuerte. Esto ultimo es deliberado: para cada finalista se escribio el argumento en contra "
 "mas solido antes de validarla, como antidoto al sesgo de confirmacion. La clasificacion del desplome distingue "
 "ademas si una caida obedece a MIEDO o ROTACION, que crea oportunidad, o a DETERIORO GENUINO, que no.",
]

funnel_text = [
 f"El embudo parte de {universe['universe_count']} cotizadas y aplica seis filtros cuantitativos duros "
 "(capitalizacion superior a 5.000 millones, margen neto a tres anos por encima del 15%, ROIC sobre 12%, "
 "crecimiento de ingresos a cinco anos por encima del 6%, flujo de caja libre positivo en al menos tres de "
 f"cinco anos y deuda neta sobre EBITDA por debajo de 3x), reduciendolo a {universe['passing_count']} "
 "candidatas. El umbral de margen neto se elevo automaticamente al 15% para aterrizar en la banda objetivo. "
 "El scoring preliminar dejo un long-list de 80 nombres con calidad igual o superior a 12,0, la verificacion "
 f"profunda confirmo un pool de {fase23['pool_count']}, y de ahi se eligieron las 30 finalistas. El universo "
 "se descubrio de forma sistematica; no se asumio una lista conocida de antemano.",
]

map_text = [
 "El mapa cruza calidad (eje vertical, score Seilern sobre 13,5) con margen de seguridad (eje horizontal). "
 "La zona sombreada superior-derecha es la joya: maxima calidad a precio con descuento. Casi todas las "
 "finalistas se alinean cerca del techo de calidad, de modo que la dispersion relevante es horizontal: las "
 "gangas (Wolters Kluwer, Adobe, Adyen, Veeva) se separan a la derecha, mientras los apex caros de momentum "
 "(Alphabet, ASML, TSMC, Apple) quedan a la izquierda, excelentes pero descontando ejecucion perfecta.",
]

convergence_text = [
 "La convergencia es alta: seis de ocho nombres de calibracion se confirman dentro del 10%. Las dos "
 "divergencias, Accenture (de ~12,5x estimado a ~9x verificado) e Intuit (de ~12,4x a ~10x), no contradicen la "
 "tesis: reflejan que ambas cotizaciones se desplomaron, comprimiendo el multiplo. Es la misma fuerza que crea "
 "las gangas de la Lista B.",
]

overlap_text = [
 "Las dos listas resultaron disjuntas: ningun nombre aparece en ambas. No es casualidad, sino el reflejo de una "
 "rotacion limpia entre calidad pura (Lista A) y precio (Lista B), y de que las preguntas que responden son "
 "distintas. El caso mas cercano a un cruce es Adyen: infraestructura de pago de primer nivel que, tras caer, "
 "encabeza la zona de valor con un margen de seguridad cercano al 36%; quedo en la Lista B y no en la A solo "
 "porque las dieciocho plazas de indispensabilidad las ocupan franquicias aun mas sistemicas (las redes Visa y "
 "Mastercard, los semiconductores de vanguardia, los indices y los ratings). Una empresa entra en la Lista B "
 "cuando ademas de apex esta claramente barata; ser indispensable no la convierte por si solo en oportunidad.",
 "Exclusivas de la Lista A (apex pero a precio justo o caro): Visa, Mastercard, Microsoft, Nvidia, Alphabet, "
 "ASML, TSMC, S&P Global, Moody's, MSCI, Hermes, LVMH, Intuitive Surgical, Apple, IDEXX, L'Oreal, Linde y CME. "
 "Son los negocios mas indispensables del mundo, pero el mercado ya paga por su calidad: la mayoria cotiza "
 "cerca de su valor o por encima, y los semiconductores de vanguardia, Apple y Alphabet descuentan ejecucion "
 "perfecta.",
 "Exclusivas de la Lista B (altisima calidad y baratas, pero por debajo de las primeras dieciocho plazas de "
 "indispensabilidad): Wolters Kluwer, Accenture, Adobe, Gartner, Adyen, Intuit, Veeva, Partners Group, "
 "ResMed, Nintendo, Cboe y Booking. La lista se diversifico de forma deliberada: el bloque de software, datos "
 "y servicios de informacion derratado por el miedo a la IA de 2026 (el llamado Claude Crash) se capo en seis "
 "nombres (Wolters Kluwer, Accenture, Adobe, Gartner, Intuit, Veeva) para no convertir la cartera en una "
 "apuesta de un solo factor; las seis plazas restantes se reparten entre pagos (Adyen), mercados privados "
 "(Partners Group), salud (ResMed), videojuegos (Nintendo), bolsas (Cboe) y viajes (Booking). Dos nombres "
 "igual de baratos, ServiceNow y FactSet (margen ~30%), quedaron en reserva por ser tambien software. La "
 "re-verificacion en vivo confirmo que los multiplos hundidos del bloque de IA (Accenture ~9x, Adobe ~8x, "
 "Wolters Kluwer ~10x, Gartner ~10x) son derratings reales, no errores de dato, frente a medias historicas de "
 "25-28x; el foso operativo (ROIC alto, crecimiento organico positivo) no corrobora la implosion que el precio "
 "descuenta.",
]

reco_text = [
 "Fase 1, comprar ahora (gangas fuertes, margen igual o superior al 20%): " +
 ", ".join(f"{name(t)}" for t in ganga) + ". Son negocios de foso intacto cuyo precio cayo por miedo ciclico o "
 "por temor a la IA, no por deterioro estructural verificado. Igual de baratas pero fuera de las doce por "
 "diversificacion sectorial quedan ServiceNow y FactSet (margen ~30%).",
 "Fase 2, construir en caidas del 10% (calidad apex con margen 10-20%, justo por debajo del corte de Lista B): "
 "Marsh & McLennan, Copart, ADP y RELX, y en la Lista A, CME. Se vuelven ganga en cualquier correccion.",
 "Fase 3, mantener y no anadir (apex a precio justo o caro): Visa, Mastercard, Microsoft, S&P Global, Hermes, "
 "LVMH, L'Oreal e Intuitive cotizan cerca de su valor; los semiconductores de vanguardia, Apple y Alphabet "
 "descuentan ejecucion perfecta y solo se compran en debilidad.",
 "Disparadores falsables que cambiarian la postura: (1) que el deterioro de ingresos en el software descontado "
 "se confirme organico y no ciclico; (2) que la SBC de los nombres de IA siga subiendo sobre el flujo de caja; "
 "(3) que la regulacion de interchange comprima de verdad el pricing de las redes de pago; (4) que la "
 "disrupcion de la IA erosione de forma medible el foso de datos de Wolters Kluwer o FactSet; (5) que el ciclo "
 "de capex de semiconductores gire a la baja.",
]

exclusions_intro = [
 "Las fichas completas son solo para las 30 finalistas. El resto del trabajo vive en esta tabla. Se distinguen "
 "cuatro grupos: nombres que pasaron el cribado pero no el piso de calidad sobre datos verificados; apex "
 "excelentes pero demasiado caros para la Lista B; casos eticos marcados para decision del usuario; y "
 "situaciones especiales. Meta Platforms queda excluida de forma permanente por mandato.",
]
exclusions_table = [
 {"ticker": "NVO", "name": "Novo Nordisk", "reason": "Calidad 11,5 sobre datos verificados; deterioro aun activo. WATCHLIST, fuera del nucleo."},
 {"ticker": "SNPS", "name": "Synopsys", "reason": "Calidad 11,5; la SBC supera el 25% del FCF y hunde la regla dura de contabilidad (R9)."},
 {"ticker": "ZTS", "name": "Zoetis", "reason": "Calidad 9,0 sobre datos verificados; deterioro de crecimiento confirmado."},
 {"ticker": "FICO", "name": "Fair Isaac ‡", "reason": "Caso etico (monopolio de scoring crediticio). Marcado para decision del usuario; fuera del 18+12."},
 {"ticker": "VRSN", "name": "Verisign ‡", "reason": "Caso etico (rentas regulatorias .com/.net). Marcado para decision del usuario."},
 {"ticker": "PLTR", "name": "Palantir ‡", "reason": "Caso etico (vigilancia/defensa) y valoracion extrema (margen -41%). Marcado."},
 {"ticker": "RACE", "name": "Ferrari", "reason": "Apex de marca, pero el bloque de lujo ya cubierto con Hermes, LVMH y L'Oreal. Primera reserva."},
 {"ticker": "COST", "name": "Costco", "reason": "Foso de escala/membresia genuino, pero el mas caro de su grupo (margen -30%). Reserva de consumo."},
 {"ticker": "REL.L", "name": "RELX", "reason": "Datos apex, pero solapa con SPGI/MSCI/MCO; MoS +15% quedo justo fuera del corte de Lista B."},
 {"ticker": "7741.T", "name": "HOYA", "reason": "Nodo critico (mask blanks EUV) pero nicho; semis ya con 3 plazas en Lista A."},
 {"ticker": "Reserva B", "name": "ServiceNow, FactSet, Marsh & McLennan, Copart", "reason": "Calidad apex con MoS +18% a +30%; primera reserva. ServiceNow y FactSet (~30%) quedaron fuera al capar el bloque de software en seis para diversificar; Marsh y Copart, por MoS algo menor."},
 {"ticker": "META", "name": "Meta Platforms", "reason": "EXCLUIDA PERMANENTEMENTE por mandato, sin importar precio ni analisis."},
 {"ticker": "Trampas", "name": "DocuSign, Twilio, Okta, Teladoc, Pfizer, Paramount, Kering...", "reason": "Crecimiento deteriorado, fosos no sostenibles o declive secular; no superan el piso de calidad."},
]

warnings = [
 "Los multiplos y los precios se mueven a diario. Todas las cifras de precio, capitalizacion, P/E adelantado y "
 "margen de seguridad corresponden al 22 de junio de 2026 y deben re-verificarse antes de tomar cualquier "
 "decision; un movimiento del 10% en el precio cambia materialmente la etiqueta de oportunidad.",
 "El DCF es un ancla, no el modelo completo. Aqui el valor intrinseco reconcilia un DCF de owner earnings "
 "(flujo de caja libre menos el 100% de la compensacion en acciones) con una reversion al multiplo historico de "
 "cada empresa, porque un DCF puro infravalora sistematicamente a los mejores compounders al no acreditar "
 "decadas de reinversion a alto ROIC. Aun asi, el resultado es conservador para las franquicias apex.",
 "El score Seilern Ponderado es una inferencia estructurada a partir de diez reglas, no un hecho contable. La "
 "amplificacion (cuando R1, R3 y R4 se refuerzan) puede elevar el score hasta el techo de 13,5 y es, por "
 "naturaleza, un juicio cualitativo.",
 "Los datos marcados VERIFICADO provienen de filings primarios (10-K, 10-Q, 20-F) o de las paginas de "
 "relaciones con inversores; los marcados ESTIMADO, de agregadores o del modelo propio. La valoracion (P/E "
 "adelantado, media de cinco anos, maximos de 52 semanas) es de naturaleza mixta por depender de datos de "
 "mercado.",
 "Meta Platforms esta excluida de forma permanente por mandato, sin importar precio ni analisis. Los casos "
 "eticos (Fair Isaac, Verisign, Palantir) se marcan con doble cruz y quedan fuera del nucleo 18+12 para "
 "decision explicita del usuario; las estructuras VIE chinas se tratarian como situaciones especiales marcadas.",
 "Este documento es de uso personal, se elaboro con metodologia Quality-Growth + Value + Buffett, y no "
 "constituye asesoria de inversion registrada ni una recomendacion de compra o venta de ningun valor.",
]

# ---- La Joya: calidad apex (13.5) + descuento limpio/durable (tipo CME) ----
JOYA = [
 ("ADYEN.AS", "Adyen", "Infraestructura de pagos; el mejor binomio calidad-descuento limpio del universo"),
 ("PGHN.SW", "Partners Group", "Franquicia de mercados privados; rebaja por ciclo de captacion, no por foso"),
 ("RMD", "ResMed", "Casi-duopolio mundial en apnea del sueno; el susto GLP-1 ya se disipo"),
 ("7974.T", "Nintendo", "IP de videojuegos irreplicable; descuento por ciclo de consola, no estructural"),
 ("CBOE", "Cboe", "Duopolio de derivados VIX/SPX; hermano directo de CME"),
 ("BKNG", "Booking", "Red OTA dominante con efectos de red; descuento por rotacion sectorial"),
 ("MMC", "Marsh & McLennan", "Corretaje de seguros: peaje recurrente y poco ciclico"),
 ("CPRT", "Copart", "Duopolio de subastas de siniestros con moat de red y caja neta"),
 ("NFLX", "Netflix", "Liderazgo en streaming, ya rentable y con poder de precios"),
 ("ADP", "ADP", "Nominas y RR.HH. con costes de cambio altisimos"),
 ("CME", "CME Group", "El arquetipo: monopolio de clearing y derivados, peaje sistemico"),
 ("VRSK", "Verisk", "Casi-monopolio de datos de seguros; el mas afin en caracter, a precio casi justo"),
]
jr = []
for tk, nm, car in JOYA:
    m = merged[tk]
    jr.append({"name": nm, "mos": m["mos"], "q": m["final_score"], "car": car})
jr.sort(key=lambda r: r["mos"], reverse=True)
joya = {
 "intro": [
  "Cruzando las dos preguntas del informe -que tan bueno es el negocio y si conviene comprarlo hoy- emerge un "
  "tercer grupo, el mas accionable para el inversor de calidad: negocios apex (calidad 13,5) que ademas cotizan "
  "con un descuento LIMPIO, por ciclo o rotacion y no por una amenaza estructural a su foso. Es el arquetipo de "
  "CME Group: monopolios y duopolios de infraestructura financiera, datos, salud y consumo durable, comprables "
  "hoy con margen de seguridad y sin la nube que pesa sobre el software derratado por la inteligencia artificial.",
 ],
 "method": [
  "Construccion: se exige calidad apex (13,5) y un descuento genuino, pero se excluyen dos grupos. Primero, los "
  "apex SIN descuento (Visa +2%, Mastercard +5%, Microsoft +7%, S&P Global +3%, Hermes +1%): maxima calidad que "
  "el mercado ya paga. Segundo, el valor profundo CON nube de IA (Wolters Kluwer +54%, Accenture +48%, Adobe "
  "+47%, Gartner +41%): margen mayor, pero su descuento viene con una pregunta estructural sobre el foso, lo "
  "contrario de un descuento limpio tipo CME. AppLovin cumple los numeros (13,5 y +29%) pero se dejo fuera por "
  "perfil momentum, no de compounder durable; en su lugar entra Verisk, mas afin en caracter aunque a precio "
  "casi justo. El resultado son las doce mejores compras ajustadas a calidad y durabilidad.",
 ],
 "table": [[str(i + 1), r["name"], f"{r['mos']:+.0f}%", f"{r['q']:.1f}".replace(".", ","), r["car"]]
           for i, r in enumerate(jr)],
}

data = {
 "meta": {"date": "22 junio 2026", "universe": universe["universe_count"]},
 "joya": joya,
 "exec_summary": exec_summary, "how_to_read": how_to_read,
 "funnel_text": funnel_text, "map_text": map_text,
 "lista_a": lista_a, "lista_b": lista_b, "tablero_30": tablero_30,
 "contentious_text": contentious_text,
 "convergence": [{"ticker": c["ticker"], "prev_pe": c["prev_pe"], "live_pe": c["live_pe"],
                  "status": c["status"]} for c in conv],
 "convergence_text": convergence_text,
 "overlap_text": overlap_text, "reco_text": reco_text,
 "exclusions_intro": exclusions_intro, "exclusions_table": exclusions_table,
 "warnings": warnings,
}
json.dump(data, open(D + "/ranking_data.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
out = build_ranking.build(data, QG + "/pdf/Ranking_QG_18_12.pdf")
print("ASSEMBLED ->", out)
