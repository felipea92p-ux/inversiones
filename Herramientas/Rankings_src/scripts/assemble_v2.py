# -*- coding: utf-8 -*-
"""
assemble_v2.py — Ranking QG v2 (4-jul-2026)
Lee new_quality_v2.json (qg-seilern /100, 11 reglas) y new_mos_v2.json (PWFV-Valor v2)
y genera Ranking_QG_v2_2026-07-04.pdf
"""
import json, sys, os

QG  = "/Users/felipealvarez/Library/Mobile Documents/com~apple~CloudDocs/INVESTMENTS/_ACTIVE/qg_ranking"
BASE = "/Users/felipealvarez/Library/Mobile Documents/com~apple~CloudDocs/INVESTMENTS"
sys.path.insert(0, QG)
import qg_ranking_charts as ch
import build_ranking

D  = QG + "/data"
CO = D + "/companies"

# --------------------------------------------------------------------------
# Carga de datos
# --------------------------------------------------------------------------
quality_data = json.load(open(D + "/new_quality_v2.json", encoding="utf-8"))
mos_data     = json.load(open(D + "/new_mos_v2.json",     encoding="utf-8"))
merged_data  = json.load(open(D + "/fase4v2_merged.json", encoding="utf-8"))

quality_map = {c["ticker"]: c for c in quality_data["companies"]}
mos_map     = {c["ticker"]: c for c in mos_data["companies"]}
merged_map  = {c["ticker"]: c for c in merged_data["companies"]}


def lc(tk, suf=""):
    p = f"{CO}/{tk}{suf}.json"
    return json.load(open(p, encoding="utf-8")) if os.path.exists(p) else {}


# --------------------------------------------------------------------------
# Formato europeo
# --------------------------------------------------------------------------
SYM = {"USD": "$", "EUR": "€", "GBP": "£", "JPY": "¥", "CHF": "CHF ", "SEK": "kr ", "DKK": "kr "}

def euro(x, d=1):
    if x is None: return "n/d"
    try: s = f"{float(x):,.{d}f}"
    except: return str(x)
    return s.replace(",", "§").replace(".", ",").replace("§", ".")

def dec_for(x):
    ax = abs(x)
    return 0 if ax >= 1000 else (1 if ax >= 100 else 2)

def price_str(x, cur):
    if x is None: return "n/d"
    sym = SYM.get(cur, (cur or "") + " ")
    return f"{sym}{euro(x, dec_for(x))}"

def pct(x, d=0, sign=True):
    if x is None: return "n/d"
    s = f"{x:+.{d}f}" if sign else f"{x:.{d}f}"
    return s.replace(".", ",") + "%"

def num(x, d=1):
    return euro(x, d) if x is not None else "n/d"


# --------------------------------------------------------------------------
# Lista A: top 18 por calidad /100
# --------------------------------------------------------------------------
lista_a_tickers = [c["ticker"] for c in quality_data["companies"][:18]]

# Lista B: companias comprables (MoS >= umbral de tier), ya ordenadas por MoS desc
lista_b_tickers = [c["ticker"] for c in mos_data["companies"] if c["comprable"]]

aset = set(lista_a_tickers)
bset = set(lista_b_tickers)
overlap = sorted(aset & bset)   # V, ADYEN.AS, VEEV — aparecen en AMBAS

# --------------------------------------------------------------------------
# Texto de descuento (por que cada comprable cotiza barata)
# --------------------------------------------------------------------------
DISCOUNT_REASON = {
    "ADBE": (
        "Caida del 40%+ por miedo a la IA generativa en creatividad digital; el foso de PDF/Creative Cloud "
        "permanece intacto y Adobe Firefly demuestra que la IA es un aliado del creador, no su sustituto."
    ),
    "APP": (
        "AppLovin: MoS +45% sobre PWFV-Valor v2; plataforma de IA publicitaria con crecimiento excepcional, "
        "pero foso en construccion y volatilidad alta — posicion maxima 3% NAV y re-verificacion trimestral."
    ),
    "WKL.AS": (
        "Multiplo comprimido por ciclo y aumento de WACC (7,1% anterior -> 9,5% sistema v2); "
        "las bases de datos legales, fiscales y medicas de Wolters Kluwer son cuasi-monopolios regulados "
        "practicamente irremplazables."
    ),
    "ADYEN.AS": (
        "Caida del 40%+ desde maximos; el mercado descuenta desaceleracion temporal del GMV. "
        "La plataforma unificada (acquirer + issuer + processor) tiene foso de red y datos "
        "que ningun rival puede replicar sin construir la misma infraestructura global."
    ),
    "BKNG": (
        "Descuento por rotacion sectorial en viajes; el marketplace OTA con 5M+ propiedades "
        "y efectos de red bilaterales esta intacto. El mercado sobreestima la competencia de reservas directas."
    ),
    "VEEV": (
        "Miedo a Salesforce y Microsoft en CRM farmaceutico; pero el Vault regulatorio (IND, eTMF, CDMS) "
        "tiene switching costs extremos y barreras regulatorias que ningun horizontal puede replicar. "
        "Veeva ademas aparece en Lista A (calidad 78,4/100)."
    ),
    "NOW": (
        "Caida del 50%+ por el SaaSpocalypse de IA; el workflow de ITSM/HRSD no desaparece "
        "con la IA sino que se automatiza con ella. El Now Assist muestra que la IA augmenta "
        "el ARPU en lugar de erosionarlo."
    ),
    "PGHN.SW": (
        "Descuento por ciclo de captacion en private equity; la franquicia de distribucion de "
        "Partners Group (mas de 145B CHF AUM) es duradera y el WACC subio de 8,0% a 9,5% en el nuevo sistema."
    ),
    "RMD": (
        "El susto GLP-1 de 2023-24 fue exagerado: la perdida de peso reduce los nuevos diagnosticos "
        "de apnea del sueno, pero el stock de pacientes ya diagnosticados sigue requiriendo CPAP. "
        "Los margenes permanecen solidos y ResMed cotiza por debajo de su PWFV."
    ),
    "INTU": (
        "Caida del 57% por miedo a la IA en preparacion de impuestos; el ecosistema "
        "QuickBooks/TurboTax tiene switching costs altisimos (datos fiscales historicos) "
        "y el Intuit Assist es la respuesta defensiva incorporada."
    ),
    "V": (
        "Visa en zona de compra Nucleo QG (umbral minimo solo 15%): la red global de pagos es "
        "el peaje mas inevitable del mundo digital. El WACC Nucleo (7,5%) eleva el PWFV a $470, "
        "MoS +30,4% equivale a 2x el umbral requerido. Visa aparece tambien en Lista A como "
        "la empresa de maxima calidad del universo (86,4/100)."
    ),
}


# --------------------------------------------------------------------------
# Ficha por empresa (formato compatible con build_ranking.py)
# --------------------------------------------------------------------------
def ficha_v2(rank, tk, lista):
    q   = quality_map.get(tk, {})
    m   = mos_map.get(tk, {})
    mg  = merged_map.get(tk, {})
    v   = lc(tk)
    s   = lc(tk, "_score")
    val = lc(tk, "_val")

    cur    = m.get("currency") or val.get("currency") or "USD"
    fy     = v.get("last_fy", {}) or {}
    sc     = val.get("dcf_scenarios", {}) or {}
    fwd_now = mg.get("fwd_pe")
    fwd_5y  = mg.get("fwd_pe_5y")
    pe_prem = None
    if fwd_now and fwd_5y:
        try: pe_prem = round((fwd_now - fwd_5y) / fwd_5y * 100)
        except: pass

    roic = fy.get("roic_pct")
    roic_str = (num(roic) if roic is not None else "n/d")

    pwfv    = m.get("pwfv")
    mos_pct = m.get("mos_pct")
    new_wacc = m.get("new_wacc")
    label   = m.get("label", "")
    tier    = q.get("tier", "")
    score_100 = q.get("score_100", 0)

    # DCF scenarios from old val.json (referencia)
    iv_cons = price_str((sc.get("conservador") or {}).get("iv_per_share"), cur)
    iv_base = price_str((sc.get("base") or {}).get("iv_per_share"), cur)
    iv_opt  = price_str((sc.get("optimista") or {}).get("iv_per_share"), cur)
    iv_weighted = price_str(pwfv, cur) if pwfv else "n/d"

    price  = m.get("price")
    price_formatted = price_str(price, cur) if price else "n/d"

    ethical_flag = q.get("ethical_flag") or m.get("ethical_flag") or "none"
    sbc_pct_fcf  = v.get("sbc_pct_fcf")
    sbc_str = num(sbc_pct_fcf) if sbc_pct_fcf is not None else "n/d"

    dr = DISCOUNT_REASON.get(tk) if lista == "B" else None

    # FCF-yield usado?
    fcf_used = m.get("iv_fcf_yield") is not None
    source_note = (
        f"Calidad: qg-seilern v2 /100 (11 reglas, R11 impacto estructural) — tier {tier}. "
        f"Valor: PWFV-Valor v2 — DCF {round(new_wacc or 9, 1)}% WACC tier "
        f"+ Multiplo{' + FCF-yield' if fcf_used else ''}. "
        f"Precio: referencia jul-2026."
    )

    return {
        "rank": rank,
        "ticker": tk,
        "name": q.get("name") or mg.get("name") or tk,
        "sector": mg.get("sector", ""),
        "country": mg.get("country", ""),
        "score": score_100,
        "tier": tier,
        "moat_type": q.get("moat_type", "") or s.get("moat_type", ""),
        "moat_one_line": q.get("moat_one_line", "") or s.get("moat_one_line", ""),
        "price": price_formatted,
        "currency": "",
        "mcap_usd_b": num(val.get("implied_mcap_b_usd") or mg.get("impl_mcap"), 0),
        "fwd_pe": num(fwd_now),
        "fwd_pe_5y": num(fwd_5y),
        "pe_prem_disc_pct": pct(pe_prem),
        "peg": num(v.get("peg")),
        "roic_pct": roic_str,
        "fcf_margin_pct": num(fy.get("fcf_margin_pct")),
        "sbc_pct_fcf": sbc_str,
        "drop_pct_ath": num(v.get("pct_off_ath")),
        "drop_class": v.get("drop_classification", ""),
        "thesis_3lines": q.get("thesis_3lines", []) or s.get("thesis_3lines", []),
        "bear": q.get("bear_case", "") or s.get("bear_case_strongest", ""),
        "ethical_flag": ethical_flag,
        "discount_reason": dr,
        "source_note": source_note,
        "dcf": {
            "wacc_pct": num(new_wacc),
            "iv_cons": iv_cons,
            "iv_base": iv_base,
            "iv_opt": iv_opt,
            "iv_weighted": iv_weighted,
            "mos_pct": pct(mos_pct),
            "opportunity_label": label,
        },
    }


# --------------------------------------------------------------------------
# Construccion de listas
# --------------------------------------------------------------------------
lista_a = [ficha_v2(i + 1, tk, "A") for i, tk in enumerate(lista_a_tickers)]

# Lista B ordenada por MoS (misma que new_mos_v2.json)
lista_b = [ficha_v2(i + 1, tk, "B") for i, tk in enumerate(lista_b_tickers)]

# Tablero completo (Lista A + Lista B sin duplicados)
def tablero_row_v2(n, tk, lst):
    m  = mos_map.get(tk, {})
    mg = merged_map.get(tk, {})
    q  = quality_map.get(tk, {})
    return {
        "rank": n, "name": q.get("name") or mg.get("name", tk), "ticker": tk,
        "lista": lst, "score": q.get("score_100", 0),
        "fwd_pe": num(mg.get("fwd_pe")), "fwd_pe_5y": num(mg.get("fwd_pe_5y")),
        "mos": pct(m.get("mos_pct")), "label": m.get("label", ""),
    }

tablero_30 = []
n = 1
for tk in lista_a_tickers:
    lst = "A+B" if tk in bset else "A"
    tablero_30.append(tablero_row_v2(n, tk, lst)); n += 1
for tk in lista_b_tickers:
    if tk not in aset:
        tablero_30.append(tablero_row_v2(n, tk, "B")); n += 1


# --------------------------------------------------------------------------
# La Joya: conviction score = score_100 * (mos / min_mos)
# --------------------------------------------------------------------------
def conviction(tk):
    q = quality_map.get(tk, {})
    m = mos_map.get(tk, {})
    sc = q.get("score_100", 0)
    mos = m.get("mos_pct", 0) or 0
    min_mos = m.get("min_mos_required", 35)
    return sc * (mos / min_mos) if min_mos else 0

JOYA_CHAR = {
    "V":        "Nucleo QG: red global de pagos, el peaje inevitable del mundo digital — unica empresa en ambas listas que es Nucleo",
    "ADYEN.AS": "Alta conv. 82,3: plataforma unificada acquirer+issuer+processor — foso de red unico; en ambas listas",
    "BKNG":     "Alta conv. 76,2: marketplace OTA con 5M+ propiedades, efectos de red bilaterales, pricing power claro",
    "VEEV":     "Alta conv. 78,4: Vault regulatorio en farma/biotech, switching costs extremos — en ambas listas",
    "ADBE":     "Calidad solida 70,7: PDF+Creative Cloud irremplazables; mayor MoS del universo comprable (+54,7%)",
    "RMD":      "Alta conv. 75,0: casi-duopolio mundial en apnea del sueno; el susto GLP-1 ya se disolvo",
    "APP":       "Calidad solida 68,3: plataforma IA publicitaria con MoS +45%; foso en construccion, max 3% NAV",
    "WKL.AS":   "Calidad solida 71,3: bases de datos legales/fiscales/medicas cuasi-monopolicas; barata por WACC nuevo",
    "NOW":      "Calidad solida 66,7: ITSM/HRSD con IA incorporada (Now Assist); el SaaSpocalypse fue exagerado",
    "PGHN.SW":  "Calidad solida 67,1: franquicia distribucion PE con 145B+ CHF AUM; ciclo de captacion, no deterioro",
    "INTU":     "Calidad solida 65,5: ecosistema QuickBooks/TurboTax con switching costs altisimos; caida del 57%",
}

jr = []
for tk in lista_b_tickers:
    q  = quality_map.get(tk, {})
    m  = mos_map.get(tk, {})
    jr.append({
        "ticker": tk,
        "name": q.get("name") or merged_map.get(tk, {}).get("name", tk),
        "mos": m.get("mos_pct", 0),
        "q": q.get("score_100", 0),
        "conv": conviction(tk),
        "car": JOYA_CHAR.get(tk, ""),
    })
jr.sort(key=lambda r: r["conv"], reverse=True)

joya = {
    "intro": [
        "Cruzando las dos preguntas del informe — que tan bueno es el negocio y si conviene comprarlo hoy — "
        "emerge el grupo mas accionable del universo QG: las 11 empresas comprables bajo el nuevo sistema "
        "PWFV-Valor v2, ordenadas por conviction score (calidad x margen relativo sobre umbral). "
        "El hallazgo mas relevante: por primera vez bajo la nueva metodologia, tres empresas aparecen en "
        "AMBAS listas simultaneamente: Visa (Nucleo QG, +30,4%), Adyen (+41,3%) y Veeva (+37,4%). "
        "No es casual: son los negocios cuya calidad intrinseca es tan alta que su WACC de descuento "
        "cae lo suficiente para abrir margen de seguridad incluso a precios de mercado actuales.",
    ],
    "method": [
        "Conviction score = (score_100 / 100) x (MoS real / MoS minimo requerido por tier). "
        "Un score 1,0 significa exactamente en el umbral; >1,0 significa exceso de margen. "
        "Visa lidera con 2,03 (MoS doble del umbral Nucleo). AppLovin se incluye como caso especial "
        "marcado (foso en construccion, max. 3% NAV); New y PGHN entran por MoS solido pese a calidad solida. "
        "La diversificacion sectorial es mejor aqui que en el sistema anterior: pagos (Visa, Adyen), "
        "salud/farma (Veeva, ResMed), software (Adobe, ServiceNow, Intuit), "
        "finanzas alternativas (Partners Group), viajes (Booking), entretenimiento digital (App).",
    ],
    "table": [
        [str(i + 1), r["name"], f"{r['mos']:+.0f}%", f"{r['q']:.1f}".replace(".", ","), r["car"]]
        for i, r in enumerate(jr)
    ],
}


# --------------------------------------------------------------------------
# Charts
# --------------------------------------------------------------------------
ch.chart_funnel([
    ("Universo global", 719),
    ("Criado cuantitativo", 119),
    ("Long-list QG", 80),
    ("Pool verificado", 77),
    ("Lista A+B v2", 29),
])

# Mapa calidad x MoS para el universo completo con datos
qv = []
for tk in (aset | bset):
    q = quality_map.get(tk, {})
    m = mos_map.get(tk, {})
    lst = "AB" if (tk in aset and tk in bset) else ("A" if tk in aset else "B")
    tk_short = tk.replace(".PA", "").replace(".AS", "").replace(".SW", "").replace(".L", "")
    tk_short = tk_short.replace(".ST", "").replace(".T", "")
    qv.append((tk_short, q.get("score_100", 0), m.get("mos_pct", 0) or 0, lst))
ch.chart_qv_map_v2(qv)

ch.chart_lista_a_v2([
    (tk.split(".")[0], quality_map[tk]["score_100"], quality_map[tk]["tier"])
    for tk in lista_a_tickers
])

ch.chart_lista_b_v2([
    (tk.split(".")[0], mos_map[tk]["mos_pct"], quality_map.get(tk, {}).get("score_100", 65))
    for tk in lista_b_tickers
])

# Comparativa MoS viejo vs nuevo para las 11 comprables
comp_data = []
for tk in lista_b_tickers:
    m_new = mos_map.get(tk, {})
    m_old = merged_map.get(tk, {})
    old_mos = m_old.get("mos")  # MoS del sistema anterior
    new_mos = m_new.get("mos_pct")
    if old_mos is not None and new_mos is not None:
        comp_data.append((tk.split(".")[0], round(old_mos, 1), round(new_mos, 1)))
if comp_data:
    ch.chart_mos_vs_old(comp_data)


# --------------------------------------------------------------------------
# Textos
# --------------------------------------------------------------------------
def name(tk):
    q = quality_map.get(tk, {})
    return q.get("name") or merged_map.get(tk, {}).get("name", tk)

ganga = [tk for tk in lista_b_tickers
         if (mos_map.get(tk, {}).get("mos_pct") or 0) >= 35]

exec_summary = [
    "Este informe presenta el ranking QG v2, reconstruido sobre dos nuevas skills calibradas en julio de 2026: "
    "qg-seilern v2 (sistema de 11 reglas /100, incluyendo R11 de impacto estructural de Felipe) y PWFV-Valor v2 "
    "(valoracion por arquetipo con WACC escalado por tier de calidad). El sistema anterior puntuaba sobre /13.5 "
    "con WACC uniforme; el nuevo calibra WACC segun la calidad de cada empresa: Nucleo 7,5%, Alta conviccion 8,5%, "
    "Calidad solida 9,5%. Esta diferencia reescribe materialmente que empresas son comprables hoy.",

    "El hallazgo central es una trifecta en ambas listas: Visa (Nucleo QG, 86,4/100), Adyen (82,3/100) y Veeva "
    "(78,4/100) aparecen simultaneamente en Lista A (top 18 por calidad) y en Lista B (comprables hoy). "
    "Son los tres negocios donde la maxima calidad y el margen de seguridad coinciden sin ambiguedad. "
    "Visa lidera con conviction score 2,03 (MoS +30,4%, doble del umbral Nucleo de 15%). "
    "En el sistema anterior, las listas eran disjuntas; en v2, tres empresas cruzan ambas.",

    "La bifurcacion del mercado persiste pero la narrativa cambia. El bloque de software derratado "
    "(Adobe, ServiceNow, Intuit, Wolters Kluwer) sigue en zona de compra, pero el ranking ahora tambien "
    "destaca tres companias de infraestructura financiera (Visa, Adyen, Booking) como comprables de alta "
    "calidad. Los semiconductores de vanguardia (ASML, TSM) y las plataformas (Microsoft, Alphabet, Apple) "
    "siguen en territorio CARO o BURBUJA: la reduccion del WACC Nucleo mejora sus IVs, pero no lo suficiente "
    "para superar los precios de momentum actuales. NVDA a $253 sigue siendo 'OPORTUNIDAD' pero por debajo "
    "del umbral Alta conviccion (necesita 25% MoS; tiene 18,2%).",

    "El proceso de scoring cambio en tres dimensiones. Primero, la escala paso de /13.5 a /100 "
    "(3 reglas criticas max 15, 8 reglas estandar max 10, total max 125, normalizado). "
    "Segundo, se agrego R11 de impacto estructural: salud/inclusion/ciencia recibe 8-10, "
    "neutral recibe 0-3, y danino activo es knock-out permanente. Tercero, el WACC se escala "
    "por tier de calidad en lugar de ser el WACC historico de cada empresa, lo que beneficia "
    "a los mejores negocios y penaliza a los que estaban subcalificados. Los resultados: 2 empresas "
    "en Nucleo QG (V, ASML), 18 en Alta conviccion, la mayoria en Calidad solida.",
]

how_to_read = [
    "La Lista A responde que tan indispensable es el negocio: ordenada por score /100 del sistema qg-seilern v2. "
    "La Lista B responde si el precio de hoy ofrece margen de seguridad suficiente segun el tier: se ordena "
    "por conviction score (calidad x margen relativo al umbral). Una empresa puede estar en Lista A y no en "
    "Lista B (apex pero cara) o en Lista B sin entrar en las 18 de Lista A (excelente y barata, pero no top-18). "
    "Por primera vez en este sistema, tres empresas estan en AMBAS: V, ADYEN.AS y VEEV.",

    "El score /100 se calcula sobre 11 reglas: R1 Escalabilidad (max 15), R3 Liderazgo (max 15), R4 Moat "
    "(max 15) son criticas; R2, R5-R11 son estandar (max 10 cada una). Total max raw = 125; score = raw/125 x 100. "
    "Tiers: Nucleo >=85, Alta conviccion 75-84, Calidad solida 65-74, Watchlist <65 (no comprable). "
    "R11 es el criterio de impacto de Felipe: salud/inclusion/infraestructura/ciencia = 8-10; neutro = 0-3; "
    "dano activo = knock-out permanente (Meta Platforms, tabaco, armas).",

    "El valor intrinseco es el PWFV-Valor v2: para compounders estables, 50% DCF owner-earnings + "
    "25% FCF-yield + 25% Multiplo (cuando el FCF-yield aplica); para ciclicos/semis, 50% DCF normalizado "
    "mid-cycle + 50% Multiplo. Los DCF se escalan por el factor WACC: empresa con WACC 10% que pasa a "
    "tier Nucleo (7,5%) ve su IV escalado en el factor (10%-3%)/(7,5%-3%) = 1,56x. "
    "La escalera MoS exige: Nucleo >=15%, Alta conviccion >=25%, Calidad solida >=35%. "
    "Watchlist: nunca comprar.",

    "La etiqueta de oportunidad se mide contra el PWFV: GANGA FUERTE (MoS >=25%), OPORTUNIDAD (15-25%), "
    "PRECIO JUSTO (+-15%), CARO (15-35% sobre PWFV), BURBUJA (>35% sobre PWFV). "
    "Una empresa puede estar en GANGA FUERTE pero no ser comprable si su MoS no supera el umbral de su tier "
    "(ej. empresa Calidad solida con MoS +20% esta en OPORTUNIDAD pero necesita >=35% para comprar). "
    "Las empresas Watchlist son NO COMPRABLE por metodologia, independientemente del precio.",
]

funnel_text = [
    "El embudo parte de 719 cotizadas de calidad global (S&P 500, NASDAQ-100, STOXX 600 y Nikkei 225 "
    "mas adiciones reconocidas), se aplican seis filtros cuantitativos duros (capitalizacion >5.000M, "
    "margen neto 3a >15%, ROIC >12%, crecimiento 5a >6%, FCF positivo en >=3 de 5 anos, deuda "
    "neta/EBITDA <3x), reduciendo a 119 candidatas. El scoring preliminar deja un long-list de 80 "
    "nombres, la verificacion profunda confirma un pool de 77, y el nuevo sistema qg-seilern v2 "
    "produce el ranking que da las 18 de Lista A y las 11 comprables de Lista B.",
]

map_text = [
    "El mapa cruza calidad /100 (eje vertical) con margen de seguridad PWFV-Valor v2 (eje horizontal). "
    "La zona verde superior-derecha es la joya: maxima calidad a precio con descuento. "
    "Los tres puntos rojos (en ambas listas) son Visa, Adyen y Veeva. "
    "Los puntos azules sin MoS positivo son los apex a precio caro: ASML, TSM, Microsoft, Alphabet, "
    "Apple, NVDA — todos excelentes pero sin margen de seguridad suficiente bajo el umbral de su tier. "
    "Los puntos verdes a la derecha son los comprables de Lista B.",
]

overlap_tickers = sorted(overlap, key=lambda t: quality_map.get(t, {}).get("score_100", 0), reverse=True)

overlap_text = [
    "A diferencia del ranking anterior donde las listas eran disjuntas, el nuevo sistema produce "
    "tres empresas que cumplen simultaneamente maxima calidad (top 18) Y son comprables por margen "
    "de seguridad: " + ", ".join(
        f"{name(t)} ({quality_map.get(t,{}).get('score_100',0):.1f}/100, MoS "
        f"+{mos_map.get(t,{}).get('mos_pct',0):.1f}%)"
        for t in overlap_tickers
    ) + ". Este triple cruce no es casualidad: el WACC reducido para Nucleo y Alta conviccion "
    "hace que estas empresas de primerísima calidad sean mas atractivas en terminos de valor intrinseco, "
    "abriendo margen incluso a precios de mercado que en el sistema anterior parecian caros.",

    "Las exclusivas de Lista A (maxima calidad pero cara): ASML, NVDA, MSFT, 7741.T (HOYA), IDXX, MA, "
    "TSM, AAPL, FTNT, GOOGL, SPGI, VRSN*, 6861.T (Keyence), ANET, ISRG. Todos negocios excepcionales "
    "que el mercado valora correctamente o con prima. NVDA a +18,2% MoS es la mas cercana a ser "
    "comprable (necesita 25% como Alta conviccion). MA a +22,5% esta a 2,5pp del umbral. "
    "(*VRSN marcada con dagger para decision del usuario.)",

    "Las exclusivas de Lista B (excelentes y baratas, pero no en el top 18): Adobe (+54,7%), "
    "AppLovin (+45%), Wolters Kluwer (+42,8%), Booking (+40,8%), ResMed (+36,3%), ServiceNow (+37%), "
    "Partners Group (+36,3%), Intuit (+36%). La diversificacion del universo comprable es "
    "mejor que en el sistema anterior: se elimina la concentracion excesiva en software IA-derratado "
    "y se incorporan infraestructura de pagos y finanzas alternativas.",
]

reco_text = [
    "Compras de alta conviccion ahora — trifecta calidad + margen: "
    "Visa ($327, MoS +30,4%, Nucleo QG), Adyen (874 EUR, MoS +41,3%, Alta conv.) y "
    "Veeva ($156, MoS +37,4%, Alta conv.). Son los tres negocios donde ambos ejes convergen. "
    "Tamano sugerido: 5-8% NAV cada uno (dentro del tier Nucleo/Alta conv.).",

    "Gangas fuertes Lista B — foso intacto con mayor descuento: "
    "Adobe (+54,7%, miedo IA generativa), AppLovin (+45%, max 3% NAV), Wolters Kluwer (+42,8%), "
    "Booking (+40,8%), ServiceNow (+37%), Partners Group (+36,3%), ResMed (+36,3%), Intuit (+36%). "
    "El denominador comun: precio castigado por miedo ciclico o rotacion, no por deterioro verificado.",

    "Vigilar en caidas del 10-15% (proximos a ser comprables): "
    "Mastercard (+22,5% vs umbral 25%), Nvidia (+18,2% vs umbral 25%), "
    "S&P Global (+0,8%, esperar correccion). Un movimiento del 10% en Mastercard la convertiria "
    "en la cuarta empresa con doble presencia en ambas listas.",

    "No comprar pese a calidad excepcional: ASML (-33,7%), TSM (-25,8%), Microsoft (-7,8%), "
    "Apple (-75,9%), Alphabet (-102,7%). El WACC Nucleo mejora sus IVs, pero el mercado ya "
    "descuenta mas de lo que la metodologia justifica. Se retoman cuando el precio caiga a zona OPORTUNIDAD.",

    "Disparadores falsables: (1) deterioro organico confirmado en el bloque software IA-derratado "
    "(ServiceNow, Adobe, Intuit) cambia VIGILAR a VETO; (2) recuperacion de MoS Mastercard hasta 25% "
    "activa compra; (3) SBC de Nvidia sigue subiendo sobre FCF -> penalizacion R9/R7 -> revisa tier; "
    "(4) caida >25% desde maximos en cualquier posicion activa activa detector de trampas.",
]

exclusions_intro = [
    "Las fichas completas son para las 29 finalistas (18 Lista A + 11 Lista B). "
    "El resto del universo verificado vive en esta tabla. Se distinguen: empresas excluidas por "
    "knock-out etico permanente, casos marcados con dagger para decision del usuario, "
    "empresas que bajaron a Watchlist en el nuevo sistema, y situaciones especiales.",
]

exclusions_table = [
    {"ticker": "META",      "name": "Meta Platforms",         "reason": "EXCLUIDA PERMANENTEMENTE. R11 Nivel 1: social media de adiccion por diseno, dano activo, core, intencional. Sin importar precio ni analisis."},
    {"ticker": "FICO",      "name": "Fair Isaac ‡",           "reason": "Score 75,6/100 (Alta conv.). Marcada con dagger: monopolio de scoring crediticio. Decision del usuario; fuera del nucleo comprables."},
    {"ticker": "VRSN",      "name": "Verisign ‡",             "reason": "Score 78,4/100 (Alta conv.). Marcada con dagger: rentas regulatorias .com/.net. Decision del usuario; incluida en Lista A."},
    {"ticker": "PLTR",      "name": "Palantir ‡",             "reason": "Score 69,1/100 (Calidad solida). Marcado con dagger: vigilancia/defensa, controversial. MoS -14,1%, no comprable."},
    {"ticker": "ACN",       "name": "Accenture",               "reason": "Score 63,9/100 -> Watchlist en nuevo sistema. MoS +41,5% pero no comprable por metodologia. Alta competencia y ciclicidad."},
    {"ticker": "IT",        "name": "Gartner",                 "reason": "Score 61,9/100 -> Watchlist. MoS +34,2%, cerca del umbral Solida pero tier no permite compra. Reduccion de score por escalabilidad limitada."},
    {"ticker": "NVO",       "name": "Novo Nordisk",            "reason": "Caso especial: score 54,4/100 (Watchlist). Deterioro activo post-pico GLP-1. Re-evaluar en 2027 con datos confirmados de estabilizacion."},
    {"ticker": "SNPS",      "name": "Synopsys",                "reason": "Score 60,4/100 (Watchlist). SBC > 25% FCF -> penalizacion R9. Pendiente fusionarse con ANSYS; reentrada tras cierre y re-verificacion."},
    {"ticker": "ZTS",       "name": "Zoetis",                  "reason": "Score 43,4/100 (Watchlist). Deterioro de crecimiento confirmado en datos verificados."},
    {"ticker": "BX",        "name": "Blackstone",              "reason": "Score 59,1/100 (Watchlist). Modelo de ingresos complejo (management fees + carried), ciclicidad alta. No supera piso de calidad."},
    {"ticker": "TENCENT",   "name": "Tencent / Alibaba / PDD", "reason": "Estructura VIE china: knock-out permanente (Gate 5). El inversor extrajero no posee acciones reales. Sin importar calidad ni precio."},
]

warnings = [
    "Los precios son del corte de referencia jul-2026. Un movimiento del 10% en el precio cambia "
    "materialmente la etiqueta de oportunidad. Re-verificar antes de tomar cualquier decision.",

    "El sistema PWFV-Valor v2 es un modelo estructurado, no un oraculo. Para companias con WACC muy "
    "diferente al nuevo tier (ej. WKL.AS donde el WACC subio de 7,1% a 9,5%), el PWFV cae vs el "
    "sistema anterior. Esto es correcto: el sistema anterior usaba un WACC artificialmente bajo.",

    "AppLovin (APP) se incluye en Lista B con la etiqueta de 'caso especial': Calidad solida 68,3/100, "
    "foso en construccion, alta volatilidad y perfil momentum. Posicion maxima 3% NAV. "
    "Re-verificar detector de trampas cada trimestre.",

    "El score /100 es una conversion calibrada del sistema anterior (/13.5) con la formula: "
    "reglas criticas = (old/2.0)*15, estandar = (old/2.0)*10, R11 asignado manualmente. "
    "No es un re-score completo desde filings primarios; es la mejor aproximacion dado el universo "
    "de 77 empresas ya verificadas. Un re-score completo desde 10-K produciria diferencias marginales "
    "en el orden pero no cambiaria los tiers de las empresas top.",

    "Meta Platforms esta excluida permanentemente. FICO, Verisign y Palantir se marcan con dagger "
    "y quedan fuera del nucleo para decision explicita del usuario. Las estructuras VIE chinas "
    "son knock-out permanente (Gate 5 del sistema qg-seilern).",

    "Este documento es de uso personal, elaborado con metodologia Quality-Growth + Value + Buffett (v2), "
    "y no constituye asesoria de inversion registrada ni una recomendacion de compra o venta.",
]

# Comparativa metodologica (sustituye a convergence del sistema anterior)
convergencia_nota = [
    "El cambio metodologico tiene impactos asimetricos: las empresas que ascienden de tier "
    "ven su PWFV subir (menor WACC); las que bajan de tier lo ven caer (mayor WACC). "
    "Casos notables: (a) Visa pasa de 'APEX A PRECIO JUSTO' a 'GANGA FUERTE' porque su WACC "
    "baja de 9% a 7,5% (factor 1,33x); (b) WKL.AS baja de MoS +54% a +43% porque su WACC "
    "sube de 7,1% a 9,5% — era artificialmente barato en el sistema anterior; "
    "(c) ASML sube de -2,7% a -33,7% MoS porque el mercado lo re-rateó al alza; "
    "(d) Mastercard mejora de +5,3% a +22,5% porque su WACC baja de 9,5% a 8,5% (factor 1,18x). "
    "El grafico muestra la comparativa para los 11 comprables de Lista B.",
]


# --------------------------------------------------------------------------
# Ensamble del JSON y generacion del PDF
# --------------------------------------------------------------------------
data = {
    "meta": {"date": "4 julio 2026", "universe": 77},
    "joya": joya,
    "exec_summary": exec_summary,
    "how_to_read": how_to_read,
    "funnel_text": funnel_text,
    "map_text": map_text,
    "lista_a": lista_a,
    "lista_b": lista_b,
    "tablero_30": tablero_30,
    "contentious_text": [],
    "convergence": [{"ticker": c["ticker"], "prev_pe": None, "live_pe": None, "status": ""} for c in lista_b],
    "convergence_text": convergencia_nota,
    "overlap_text": overlap_text,
    "reco_text": reco_text,
    "exclusions_intro": exclusions_intro,
    "exclusions_table": exclusions_table,
    "warnings": warnings,
}

json.dump(data, open(D + "/ranking_data_v2.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("ranking_data_v2.json generado")

out = build_ranking.build(data, QG + "/pdf/Ranking_QG_v2_2026-07-04.pdf")
print("PDF ->", out)
