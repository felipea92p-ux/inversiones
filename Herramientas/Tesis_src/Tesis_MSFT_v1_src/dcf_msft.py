# -*- coding: utf-8 -*-
"""FUENTE ÚNICA DE VERDAD · Tesis Ultra MSFT v1.0 (corte 6-jul-2026).
Datos verificados en fuente primaria: 10-K FY2025 + 10-Q Q3 FY2026 + DEF 14A 2025
(SEC EDGAR CIK 0000789019). Ejes: qg-seilern (CALIDAD) + val-mos (VALORACIÓN).
Nota: el score QG se corrigió a 86.0 (el agente puntuó R3/R4 fuera del rango 0-10)."""

def es(x, dec=1):
    return f"{x:.{dec}f}".replace(".", ",")

def pct(x, dec=1):
    return es(x, dec) + "%"

# ── Identidad / mercado (6-jul-2026) ─────────────────────────────────────
PRECIO       = 384.34
ACCIONES     = 7428          # M (una sola clase, un voto)
MKTCAP       = 2.86          # US$T
CAJA_NETA    = 38.0          # US$B (caja+STI $78.3B − deuda bonos $40.3B); +$8.8B si se cuentan finance leases
EV           = 2.82          # US$T
ATH          = 555.45        # máximo 52 semanas
LOW_52       = 349.20
HIGH_52      = 555.45
CAIDA_MAX    = -31           # % desde máximo 52s
CAIDA_12M    = -20
BETA         = 1.13

# ── EJE CALIDAD (qg-seilern) · corregido a 86.0 ──────────────────────────
SCORE_QG = 86.0
RAW_QG   = 107.5
TIER_QG  = "Núcleo"
# (nombre, puntos ponderados, máximo)
REGLAS = [
    ("R1 · Escalabilidad",       13.5, 15),
    ("R2 · Industria",            8.5, 10),
    ("R3 · Liderazgo",          14.25, 15),
    ("R4 · Moat",               14.25, 15),
    ("R5 · Crec. orgánico",       8.0, 10),
    ("R6 · Diversificación",      9.0, 10),
    ("R7 · Capital / ROIC",       7.5, 10),
    ("R8 · Balance",              8.5, 10),
    ("R9 · Transparencia",        8.0, 10),
    ("R10 · Gestión",             8.0, 10),
    ("R11 · Impacto",             8.0, 10),
]
# radar 0-10 por regla
RADAR = [
    ("R1", 9.0), ("R2", 8.5), ("R3", 9.5), ("R4", 9.5), ("R5", 8.0),
    ("R6", 9.0), ("R7", 7.5), ("R8", 8.5), ("R9", 8.0), ("R10", 8.0), ("R11", 8.0),
]

# ── EJE VALORACIÓN (val-mos) ─────────────────────────────────────────────
DETECTOR = "PASA"            # 0 señales estructurales plenas · 2 alertas de vigilancia
PWFV     = 520              # US$/acción — ancla
EPV      = 210             # suelo sin crecimiento
V_POND   = 520             # valor ponderado por escenarios
OE_TTM   = 115             # owner earnings normalizado, US$B (rango 107-122)
OE_XACC  = 15.5            # owner earnings por acción
FCF_REP  = 72.9            # FCF reportado TTM (deprimido por capex de crecimiento)
WACC     = 8.0
TERMINAL = 3.0
# escenarios (nombre, prob %, valor US$/acción)
V_BEAR, P_BEAR = 395, 25
V_BASE, P_BASE = 520, 50
V_BULL, P_BULL = 640, 25
# DCF inverso
G_IMPL   = 7.7             # g implícita en el precio
G_GUIA   = 14.0           # crecimiento guiado (Azure/IA implícito)
G_CAGR   = 13.0           # CAGR revenue TTM
G_CONS   = 8.0            # crecimiento del escenario conservador propio
# zonas ancladas al PWFV (val-mos, tier Núcleo)
Z_GANGA  = round(PWFV * 0.75, 0)   # ≥25% dcto  → 390
Z_OPORT  = round(PWFV * 0.85, 0)   # 15–25% dcto → 442
Z_JUSTO  = round(PWFV * 1.15, 0)   # ±15%        → 598
Z_CARO   = round(PWFV * 1.35, 0)   # 15–35% prima → 702
MOS_EXIG = 15             # % exigido por tier Núcleo
MOS_HOY  = 26             # % actual (precio vs PWFV)
DCTO_HOY = round((PRECIO/PWFV - 1) * 100, 1)   # −26.1
ZONA_HOY = "OPORTUNIDAD / GANGA"
VEREDICTO = "COMPRAR TRAMO"
TRAMO_INI = "3–4%"        # NAV inicial
TECHO_POS = "5–6%"        # NAV tras descompresión de FCF
ASIMETRIA = 3.0

# ── Sensibilidad WACC × g terminal (valor base por acción, US$) ──────────
WACC_GRID = [7.0, 7.5, 8.0, 8.5, 9.0]
GT_GRID   = [2.0, 2.5, 3.0, 3.5, 4.0]
SENS = [
    [560, 578, 600, 625, 655],
    [525, 540, 558, 578, 600],
    [495, 507, 520, 535, 552],   # fila WACC 8,0 · col g 3,0 = 520 (base)
    [468, 478, 490, 503, 518],
    [444, 453, 463, 474, 487],
]
SENS_MIN = 444

# ── WACC construcción ────────────────────────────────────────────────────
RF   = 4.49
ERP  = 5.0
COE_CAPM = round(RF + BETA * ERP, 1)   # ~10,1% CAPM

# ── Serie financiera anual (US$B) · FY cierra 30-jun ─────────────────────
YRS_FIN = ["FY21", "FY22", "FY23", "FY24", "FY25", "TTM"]
REVENUE = [168.1, 198.3, 211.9, 245.1, 281.7, 318.3]
REV_YOY = [None, 18.0, 6.9, 15.7, 14.9, 13.0]
OP_INC  = [69.9, 83.4, 88.5, 109.4, 128.5, 149.0]
OP_MGN  = [41.6, 42.1, 41.8, 44.6, 45.6, 46.8]
NET_INC = [61.3, 72.7, 72.4, 88.1, 101.8, 125.2]
GM      = [68.9, 68.4, 68.9, 69.8, 68.8, 68.3]
CFO     = [76.7, 89.0, 87.6, 118.5, 136.2, 170.1]
CAPEX   = [20.6, 23.9, 28.1, 44.5, 64.6, 97.2]
FCF     = [56.1, 65.1, 59.5, 74.1, 71.6, 72.9]
FCF_MGN = [33.4, 32.9, 28.1, 30.2, 25.4, 22.9]
CAPEX_REV = [12.3, 12.0, 13.3, 18.1, 22.9, 30.5]
SBC     = [6.1, 8.0, 9.6, 10.7, 12.0, 12.4]
CAPEX_FY26E = 190          # US$B ampliado (incl. leases); ~$107B "puro" anualizado
CAPEX_PURO_FY26 = 107
# ROIC (%)
ROIC_YRS = ["FY23", "FY24", "FY25"]
ROIC_GW  = [43.6, 33.2, 30.6]     # con goodwill
ROIC_EXGW = [74.2, 59.5, 46.8]    # ex-goodwill
# balance / leases
PPE_NET_25 = 205.0
PPE_NET_Q3 = 283.2
FINLEASE_23 = 17.0
FINLEASE_Q3 = 63.0
LEASES_NOINIC = 196.6      # US$B leases de datacenter no iniciados (off-balance)
GOODWILL = 119.7
NET_CASH_SERIE = [56.8, 18.1, 20.6, 8.8]  # FY23, FY24, FY25, Q3FY26

# ── Segmentos (FY2025, US$B) ─────────────────────────────────────────────
SEG = [
    ("Productivity &amp;\nBusiness Processes", 120.8, 57.8, 59.9),   # rev, OI margin FY25, OI margin Q3
    ("Intelligent\nCloud (Azure)", 106.3, 42.0, 39.7),
    ("More Personal\nComputing", 54.6, 25.9, 27.8),
]
SEG_TOTAL_MGN_Q3 = 46.3

# ── KPIs Q3 FY26 ─────────────────────────────────────────────────────────
AZURE_YOY = 40            # %
AI_RUNRATE = 37          # US$B
AI_YOY = 123
MSCLOUD = 54.5           # US$B
MSCLOUD_YOY = 29
MSCLOUD_GM = [69, 67, 66]   # Q3'25, Q2'26, Q3'26
COPILOT_SEATS = 20       # M asientos pagados M365 Copilot
COPILOT_ADDS = 250       # % YoY seat adds
RPO = 633                # US$B backlog comercial
RPO_YOY = 99
OPENAI_RPO = 45          # % del RPO ligado a OpenAI
M365_SEATS = 446         # M asientos comerciales

# ── Múltiplos vs historia (P/E) ──────────────────────────────────────────
MULT_YRS = ["FY21", "FY22", "FY23", "FY24", "FY25", "HOY"]
MULT_PE  = [35.0, 26.0, 30.0, 35.0, 32.0, 22.9]
PE_MEDIANA = 31.2       # mediana 10 años
PE_FWD_26 = 22.9
PE_FWD_27 = 19.4
EV_EBITDA = 16.0
EV_EBITDA_MED = 19.5
PFCF_REP = 39           # P/FCF reportado (artefacto)
PFCF_OE = 23            # P/owner-earnings normalizado
OWNER_YIELD = 4.0       # %

# ── Porter 5 fuerzas por segmento (/25, menor = mejor foso) ──────────────
PORTER_SEG = [
    ("LinkedIn", 8),
    ("Productividad (M365)", 9),
    ("Cloud (Azure)", 14),
    ("IA", 14),
    ("Gaming", 15),
]
PORTER_POND = 11.5      # /25 ponderado

# ── TAM / SAM / SOM por mercado (US$B, SOM 2030-31) ──────────────────────
MERCADOS = [
    ("IA empresarial", 255, 37, "$120–140B"),
    ("Cloud IaaS/PaaS", 389, 78, "$200–220B"),
    ("Productividad SaaS", 390, 95, "$130–150B"),
    ("Ciberseguridad", 280, 37, "$50–60B"),
    ("Publicidad", 662, 26, "$40–50B"),
    ("Gaming", 386, 23, "$28–32B"),
]
TAM_TOTAL = 2400        # US$B agregado que toca MSFT (2026)
TAM_2030 = 3750

# ── Management (6 dimensiones, /5) ────────────────────────────────────────
MGMT = [
    ("ROIC vs WACC", 5.0),
    ("Track record M&A", 4.0),
    ("Insiders + recompra", 3.0),
    ("Guidance vs resultados", 4.5),
    ("Ownership / gobernanza", 3.5),
    ("Capital allocation lifecycle", 3.5),
]
MGMT_TOTAL = 23.5      # /30

# ── Riesgos (nombre, prob 1-5, impacto 1-5) ──────────────────────────────
RIESGOS = [
    ("Sobre-inversión de capex IA (ROIC incremental < WACC)", 3, 5),
    ("Solvencia de OpenAI (45% del RPO)", 3, 4),
    ("Antitrust fuerza desagrupar (FTC/UE/CMA)", 2, 4),
    ("Azure desacelera con depreciación escalando", 2, 4),
    ("El múltiplo sigue de-rated (FCF no descomprime)", 2, 3),
    ("Depreciación acelerada de GPUs (contable)", 2, 3),
]

# ── Nueve inversores (orden fijo; convicción /10) ────────────────────────
INVERSORES = [
    ("Graham",       5, "HOLD"),
    ("Buffett",      8, "BUY"),
    ("Munger",       8, "BUY"),
    ("Fisher",       8, "BUY"),
    ("Lynch",        7, "BUY"),
    ("Templeton",    7, "BUY"),
    ("Marks",        7, "BUY"),
    ("Seilern",      8, "BUY"),
    ("Terry Smith",  8, "BUY"),
]

if __name__ == "__main__":
    print("MSFT data OK · QG", SCORE_QG, TIER_QG, "· val-mos", VEREDICTO,
          "· PWFV", PWFV, "· zona", ZONA_HOY, es(DCTO_HOY))
    tot = sum(p for _, p, _ in REGLAS)
    print("check raw:", tot, "→", round(tot/125*100, 1))
