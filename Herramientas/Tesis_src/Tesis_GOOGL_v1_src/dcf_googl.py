# -*- coding: utf-8 -*-
"""FUENTE ÚNICA DE VERDAD · Tesis Ultra GOOGL v1.0 (corte 6-jul-2026).
Datos verificados en fuente primaria: 10-K FY2025 + 10-Q Q1 2026 + DEF 14A 2026
(SEC EDGAR CIK 0001652044). Ejes: qg-seilern (CALIDAD, corregido por verificador
adversarial: 66.2→65.4, tier Calidad sólida — NO Núcleo/Alta convicción) +
val-mos v3 (VALORACIÓN: zona JUSTO gatea el tier, candado duro violado vs techo 25x)."""

def es(x, dec=1):
    return f"{x:.{dec}f}".replace(".", ",")

def pct(x, dec=1):
    return es(x, dec) + "%"

# ── Identidad / mercado (6-jul-2026) ─────────────────────────────────────
PRECIO       = 365.71
ACCIONES     = 12150       # M (todas las clases, post-raise jun-2026)
MKTCAP       = 4.44        # US$T
EV           = 4.40        # US$T (caja neta positiva)
CAJA_NETA    = 49.3        # US$B
DEUDA_TOTAL  = 100         # US$B (post emisiones jun-2026, >$100B)

# ── EJE CALIDAD (qg-seilern, corregido por verificador) ──────────────────
SCORE_QG = 65.4
RAW_QG   = 81.75
TIER_QG  = "Calidad sólida"
REGLAS = [
    ("R1 · Escalabilidad",       11.25, 15),
    ("R2 · Industria",            8.0, 10),
    ("R3 · Liderazgo",           10.5, 15),
    ("R4 · Moat",                12.0, 15),
    ("R5 · Crec. orgánico",       8.0, 10),
    ("R6 · Diversificación",      8.0, 10),
    ("R7 · Capital / ROIC",       6.0, 10),
    ("R8 · Balance",              7.0, 10),
    ("R9 · Transparencia",        4.0, 10),
    ("R10 · Gestión",             3.0, 10),
    ("R11 · Impacto",             4.0, 10),
]
RADAR = [
    ("R1", 7.5), ("R2", 8.0), ("R3", 7.0), ("R4", 8.0), ("R5", 8.0),
    ("R6", 8.0), ("R7", 6.0), ("R8", 7.0), ("R9", 4.0), ("R10", 3.0), ("R11", 4.0),
]

# ── EJE VALORACIÓN (val-mos v3) ──────────────────────────────────────────
DETECTOR = "PASA"          # con nota de vigilancia en señal 3 (disrupción)
PWFV     = 427.5
EPV      = 103
V_POND   = 427.5
WACC     = 9.5
TERMINAL = 3.5
V_BEAR, P_BEAR = 290, 25
V_BASE, P_BASE = 430, 50
V_BULL, P_BULL = 560, 25
G_IMPL   = 10.5
G_GUIA   = 22.0           # crecimiento reciente Cloud/consolidado (no guía formal a 5a)
G_CAGR   = 14.4
G_CONS   = 6.5
DCF_CLASE = "RAZONABLES"
# Zonas (tier Calidad sólida: solo elegible en Ganga/Oportunidad — GATE, no solo MoS)
Z_GANGA  = round(PWFV * 0.70, 0)    # 299
Z_OPORT  = round(PWFV * 0.85, 0)    # 363
Z_JUSTO  = round(PWFV * 1.10, 0)    # 470
Z_CARO   = round(PWFV * 1.35, 0)    # 577
MOS_ACTUAL = 14.4
PRIMA_O_MOS = None          # no aplica (no hay prima, hay MoS insuficiente)
ZONA_HOY = "JUSTO"
VEREDICTO = "ESPERAR"
GATE_TIER = ("El tier 'Calidad sólida' (65-74) NO se compra fuera de zonas Ganga/Oportunidad: "
             "es un GATE binario, no un umbral de MoS más exigente. GOOGL está en JUSTO — excluida por regla.")
TECHO_MULT_TIER = 25       # x owner earnings — el techo del tier, más estricto que el candado genérico 30-40x
MULT_NORMALIZADO = 37.8    # x owner earnings normalizado
MULT_FCF_REAL = 69.1       # x FCF TTM real
MULT_PS = 11.0              # contraste diagnóstico (valoracion.md "distorsión por capex de
                             # crecimiento"): MKTCAP/REVENUE[2025] = 4440/402.8. Coherente con
                             # MULT_NORMALIZADO dado el margen (~33%) — no es un artefacto de FCF,
                             # el candado de 37,8x ya usaba earnings normalizados, no FCF crudo.
GATILLO_OPORT = 363
GATILLO_GANGA = 299

# ── Sensibilidad WACC × g terminal ───────────────────────────────────────
WACC_GRID = [8.5, 9.0, 9.5, 10.0, 10.5]
GT_GRID   = [2.5, 3.0, 3.5, 4.0, 4.5]
SENS = [
    [468, 483, 500, 519, 541],
    [438, 451, 466, 483, 502],
    [412, 424, 436, 452, 468],   # fila WACC 9,5 · col g 3,5 = 436 ≈ base
    [389, 399, 410, 424, 438],
    [368, 377, 387, 399, 411],
]
SENS_MAX = 541

# ── WACC construcción ────────────────────────────────────────────────────
RF   = 4.48
ERP  = 5.0
BETA = 1.20
COE_CAPM = round(RF + BETA * ERP, 1)

# ── Serie financiera anual (US$B) · FY cierra 31-dic ─────────────────────
YRS_FIN = ["2021", "2022", "2023", "2024", "2025", "TTM"]
REVENUE = [257.6, 282.8, 307.4, 350.0, 402.8, 422.5]
OP_INC  = [78.7, 74.8, 84.3, 112.4, 129.0, 138.1]
OP_MGN  = [30.6, 26.5, 27.4, 32.1, 32.0, 32.7]
NET_INC = [76.0, 60.0, 73.8, 100.1, 132.2, 160.2]
CFO     = [91.7, 91.5, 101.7, 125.3, 164.7, 174.4]
CAPEX   = [24.6, 31.5, 32.3, 52.5, 91.4, 109.9]
FCF     = [67.0, 60.0, 69.5, 72.8, 72.8, 64.4]
DYA     = [15.4, 15.4, 11.9, 15.3, 21.1, None]
SBC_PCT = [None, None, 7.3, 6.5, 6.2, 6.2]

# ── Segmentos (Q1'25 → Q1'26, US$M) ──────────────────────────────────────
SEG = [
    ("Google Services\n(Search+YouTube+Ads)", 89637, 32682, 40589),
    ("Google Cloud", 20028, 2177, 6598),
    ("Other Bets", 411, -1226, -2100),
]
SEG_TOTAL_Q1_26 = 109896

# ── KPIs Search/Cloud ─────────────────────────────────────────────────────
SEARCH_YOY_SERIE = ["Q1'25", "Q2'25", "Q3'25", "Q4'25", "Q1'26"]
SEARCH_GROWTH = [None, None, None, None, 19.1]
CLOUD_GROWTH = [32, 34, 34, 48, 63]      # % YoY, aceleración
CLOUD_MGN = [17.8, None, None, 30.1, 32.9]
CLOUD_RPO = 462.3   # US$B, +93% ~doblado QoQ
CTR_POS1_2023 = 7.3
CTR_POS1_2025 = 1.6   # -58%
ZERO_CLICK_PCT = 68.0
PAID_CLICKS_YOY = 13
CPC_YOY = 5

# ── Capex vs D&A (tensión central) ───────────────────────────────────────
CAPEX_2026E = 185       # midpoint 180-190B
GEMINI_MAU = 900        # M, mid-2026 (vs 750M Feb-2026, vs ChatGPT ~1B MAU / 4x en paid users)
CHATGPT_MAU = 1000

# ── Gain no-cash Anthropic-like (Q1'26) ──────────────────────────────────
EPS_Q1_REP = 5.11
EPS_Q1_NORM = 2.76
GAIN_Q1_PRETAX = 36.9   # US$B, "gain on equity securities"
GAIN_FY25 = 21.4        # US$B (menor magnitud)

# ── Múltiplos ─────────────────────────────────────────────────────────────
PE_TRAILING = 27.7
PE_MEDIANA_10A = 27.5
EV_SALES = 10.5
CONSENSO_PT = 430
CONSENSO_RATING = "Strong Buy"

# ── Porter por segmento (/25, menor = mejor foso) ────────────────────────
PORTER_SEG = [
    ("Google Cloud", 11),
    ("Search / Ads", 13),
    ("YouTube", 13),
]
PORTER_POND = 12.3

# ── TAM (US$B, 2026) ─────────────────────────────────────────────────────
MERCADOS = [
    ("Publicidad digital", 700, 280, "~37-40% de cuota"),
    ("Cloud / IA empresarial", 516, 80, "#3, 14% cuota, +63%"),
    ("Streaming de video (CTV)", 300, 60, "#1 tiempo-TV EEUU"),
    ("Robotaxi (Waymo, opción)", 46, 1, "opcionalidad, no en el precio"),
]

# ── Management (6 dimensiones, /5) → 18/30 ───────────────────────────────
MGMT = [
    ("Estructura de voto / alineación", 0.0),
    ("Independencia del consejo", 3.0),
    ("Compensación ejecutiva", 4.0),
    ("Partes relacionadas", 3.0),
    ("Disciplina de capital", 4.0),
    ("Transparencia / respuesta accionista", 4.0),
]
MGMT_TOTAL = 18.0

# Estructura de voto (el hallazgo central de gobernanza)
PAGE_VOTO = 27.4
BRIN_VOTO = 25.3
FUNDADORES_VOTO = 52.7
FUNDADORES_ECONOMIA = 6.2

# ── Riesgos (nombre, prob 1-5, impacto 1-5) ──────────────────────────────
RIESGOS = [
    ("Canibalización de Search por IA generativa", 3, 5),
    ("Desinversión estructural AdX/DFP (fallo Brinkema pendiente)", 3, 4),
    ("Gobernanza dual-class permanente (Page+Brin)", 5, 3),
    ("Fuga de talento de IA (Shazeer, Jumper)", 2, 3),
    ("Capex $185B sin ROIC probado + apalancamiento nuevo", 2, 4),
    ("Apelación caso Search (posible Chrome divestiture)", 2, 3),
]

# ── Nueve inversores ─────────────────────────────────────────────────────
INVERSORES = [
    ("Graham",       3, "PASS"),
    ("Buffett",      5, "HOLD"),
    ("Munger",       4, "HOLD"),
    ("Fisher",       6, "HOLD"),
    ("Lynch",        5, "HOLD"),
    ("Templeton",    4, "PASS"),
    ("Marks",        5, "HOLD"),
    ("Seilern",      4, "PASS"),
    ("Terry Smith",  4, "PASS"),
]

if __name__ == "__main__":
    print("GOOGL data OK ·", SCORE_QG, TIER_QG, "· val-mos", VEREDICTO,
          "· PWFV", PWFV, "· zona", ZONA_HOY)
    tot = sum(p for _, p, _ in REGLAS)
    print("check raw:", tot, "→", round(tot/125*100, 1))
