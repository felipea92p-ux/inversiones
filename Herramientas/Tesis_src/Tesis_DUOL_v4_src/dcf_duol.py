# -*- coding: utf-8 -*-
"""FUENTE ÚNICA DE VERDAD · Tesis Ultra DUOL v4.0 (corte 4-jul-2026).
Todos los números viven aquí; make_charts_duol y contenido_duol los importan.
Datos verificados en fuente primaria: 10-K FY2025 + 10-Q Q1'26 + DEF 14A 2026
(SEC EDGAR CIK 0001562088) y cartas a accionistas. Ejes: qg-seilern + val-mos."""

# ── Helpers de formato (coma decimal española) ───────────────────────────
def es(x, dec=1):
    s = f"{x:.{dec}f}"
    return s.replace(".", ",")

def pct(x, dec=1):
    return es(x, dec) + "%"

# ── Identidad / mercado (2-jul-2026) ─────────────────────────────────────
PRECIO       = 125.76
ACCIONES     = 46.59          # M (Clase A 40.49 + Clase B 6.36)
MKTCAP       = 5.86           # US$B
CAJA_NETA    = 1.39           # US$B (caja+STI+LTI, cero deuda)
EV           = 4.55           # US$B (mcap − caja neta, punto medio)
ATH          = 540.68         # máximo 14-may-2025
LOW_52       = 87.89
HIGH_52      = 468.00
CAIDA_MAX    = -77            # % desde máximo
CAJA_X_ACC   = 29.6           # US$/acción de caja neta
BETA         = 0.89           # 5Y publicado (se ajusta a ~1,2)

# ── EJE CALIDAD (qg-seilern) ─────────────────────────────────────────────
SCORE_QG = 78.2
RAW_QG   = 97.75
TIER_QG  = "Alta convicción"
# (nombre, puntos, máximo)
REGLAS = [
    ("R1 · Escalabilidad",       13.5, 15),
    ("R2 · Industria",            7.5, 10),
    ("R3 · Liderazgo",           12.75, 15),
    ("R4 · Moat",                10.5, 15),
    ("R5 · Crec. orgánico",       7.0, 10),
    ("R6 · Diversificación",      7.5, 10),
    ("R7 · Capital / ROIC",       8.5, 10),
    ("R8 · Balance",              9.5, 10),
    ("R9 · Transparencia",        6.0, 10),
    ("R10 · Gestión",             7.5, 10),
    ("R11 · Impacto",             7.5, 10),
]
# radar: score 0-10 por regla (para el polar)
RADAR = [
    ("R1", 9.0), ("R2", 7.5), ("R3", 8.5), ("R4", 7.0), ("R5", 7.0),
    ("R6", 7.5), ("R7", 8.5), ("R8", 9.5), ("R9", 6.0), ("R10", 7.5), ("R11", 7.5),
]

# ── EJE VALORACIÓN (val-mos) ─────────────────────────────────────────────
DETECTOR = "PASA"             # 0 de 6 señales estructurales
PWFV     = 160               # US$/acción — ancla
EPV      = 55.5              # suelo sin crecimiento
V_POND   = 163.75           # valor ponderado por escenarios
OE_2025  = 223              # owner earnings 2025 (FCF−SBC), US$M
OE_SS    = 190              # owner earnings estado estable (conservador)
WACC     = 8.5
TERMINAL = 3.0
# escenarios (nombre corto, prob %, valor US$/acción)
V_BEAR, P_BEAR = 118, 25
V_BASE, P_BASE = 167, 45
V_BULL, P_BULL = 197, 30
# DCF inverso
G_IMPL   = 4.3              # g implícita en el precio
G_GUIA   = 16.0            # guidance revenue FY26
G_CAGR3  = 40.0           # CAGR revenue 3 años
G_CONS   = 8.5            # crecimiento del escenario conservador propio
# zonas ancladas al PWFV (val-mos: escalera por tier)
Z_GANGA  = round(PWFV * 0.75, 0)   # ≥25% dcto  → 120
Z_OPORT  = round(PWFV * 0.85, 0)   # 15–25% dcto → 136
Z_JUSTO  = round(PWFV * 1.15, 0)   # ±15%        → 184
Z_CARO   = round(PWFV * 1.35, 0)   # 15–35% prima → 216
MOS_EXIG = 25              # % exigido por tier Alta convicción
MOS_HOY  = 21.4            # % actual (precio vs PWFV)
DCTO_HOY = round((PRECIO/PWFV - 1) * 100, 1)   # −21.4
ZONA_HOY = "OPORTUNIDAD"
VEREDICTO = "VIGILAR"
TRIGGER  = 120            # gatillo de compra (25% MoS)
ASIMETRIA = 4.9
TECHO_POS = 5            # % NAV techo de posición

# ── Sensibilidad WACC × g terminal (valor base por acción, US$) ──────────
WACC_GRID = [7.5, 8.0, 8.5, 9.0, 9.5]
GT_GRID   = [2.0, 2.5, 3.0, 3.5, 4.0]
SENS = [
    [172, 180, 190, 202, 217],
    [160, 167, 175, 184, 196],
    [149, 154, 160, 168, 178],   # fila WACC 8,5 · col g 3,0 = 160 (base)
    [139, 143, 149, 156, 165],
    [130, 134, 139, 145, 152],
]
SENS_MIN = 130

# ── WACC construcción ────────────────────────────────────────────────────
RF   = 4.49
ERP  = 5.0
BETA_AJ = 1.2             # beta ajustado (el 0,89 subestima el riesgo IA)
COE_CAPM = round(RF + BETA_AJ * ERP, 1)   # ~10,5% CAPM
# anclado al escalón de tier (Alta ~8,5%)

# ── Serie financiera anual (US$M) ────────────────────────────────────────
YRS_FIN = ["2021", "2022", "2023", "2024", "2025"]
REVENUE = [250.8, 369.5, 531.1, 748.0, 1037.6]
REV_YOY = [None, 47.3, 43.8, 40.8, 38.7]
OP_INC  = [-60.0, -65.2, -13.3, 62.6, 135.6]
FCF     = [5.6, 48.1, 150.0, 264.4, 360.4]
SBC     = [40.8, 73.8, 95.2, 110.5, 137.4]
SBC_PCT = [16.3, 20.0, 17.9, 14.8, 13.2]
GM      = [72.4, 73.1, 73.2, 72.8, 72.2]     # margen bruto
BOOKINGS = [None, None, 622.2, 870.6, 1158.4]
REV_2026E = 1205.0
ADJEBITDA_25 = 305.9
ADJEBITDA_26E = 310.0
ADJEBITDA_M25 = 29.5
ADJEBITDA_M26 = 25.7
NI_2025 = 414.1
NI_NORM = 139           # neto normalizado (quita el one-off fiscal)
EPS_GAAP = 8.57
EPS_NORM = 3.0
TAX_ONEOFF = 257        # US$M liberación valuation allowance

# ── KPIs operativos (serie trimestral) ───────────────────────────────────
KPI_Q   = ["Q1'24", "Q2'24", "Q3'24", "Q4'24", "Q1'25", "Q2'25", "Q3'25", "Q4'25", "Q1'26"]
DAU     = [31.4, 34.1, 37.2, 40.5, 46.6, 47.7, 50.5, 52.7, 56.5]
DAU_YOY = [54, 59, 54, 51, 49, 40, 36, 30, 21]
MAU     = [97.6, 103.6, 113.1, 116.7, 130.2, 128.3, 135.3, 133.1, 137.8]
SUBS    = [7.4, 8.0, 8.6, 9.5, 10.3, 10.9, 11.5, 12.2, 12.5]
SUBS_YOY = [54, 52, 47, 43, 40, 37, 34, 28, 21]
DAU_MAU = [32.2, 32.9, 32.9, 34.7, 35.8, 37.2, 37.3, 39.6, 41.0]
BOOK_YOY = [41, 38, 38, 42, 38, 41, 33, 24, 14]   # bookings totales YoY
# streaks (moat conductual)
STREAK_365_PCT = 28      # % de DAU con racha ≥365 días (dic-25); era ~20% en 2024
STREAK_7_PCT = 82        # % de DAU con racha ≥7 días
STREAK_365_M = 15        # M usuarios con racha ≥365 días

# ── Múltiplos vs historia (EV/Sales trailing) ────────────────────────────
MULT_YRS = ["2021", "2022", "2023", "2024", "pico\nmay-25", "2025", "HOY"]
MULT_EVS = [15.9, 7.7, 17.9, 19.1, 29.0, 7.8, 4.3]
MULT_MEDIANA = 13.7      # mediana EV/Sales 10 años (GuruFocus)
PE_GAAP = 14.4
PE_NORM = 42
PFCF = 15
POE = 28                 # P/owner-earnings punto medio (~25-33x)
EVS_FWD = 3.8

# ── Porter 5 fuerzas (1 favorable → 5 adversa) ───────────────────────────
PORTER = [
    ("Rivalidad", 2),
    ("Nuevos entrantes\n(IA baja barreras)", 4),
    ("Sustitutos\n(IA gratis)", 4),
    ("Poder proveedores\n(stores + cómputo)", 4),
    ("Poder compradores\n(lock-in conductual)", 2),
]
PORTER_TOTAL = 16        # /25

# ── TAM / SAM / SOM (US$B) ───────────────────────────────────────────────
TAM = 85                 # aprendizaje de idiomas 2025 (top-down)
TAM_2030 = 190
TAM_MONET = 25           # monetizable por el modelo freemium de DUOL (~20-30B)
SAM = 27                 # online idiomas + testing + verticales
SOM_HOY = 1.04           # ingresos DUOL 2025
SOM_2030 = 4.4           # base 2030 (~8% del SAM)

# ── Management (6 dimensiones, /5) ────────────────────────────────────────
MGMT = [
    ("ROIC vs WACC", 5.0),
    ("Track record M&A", 4.0),
    ("Insiders + recompra", 4.5),
    ("Guidance vs resultados", 3.5),
    ("Ownership / skin", 5.0),
    ("Capital allocation lifecycle", 4.0),
]
MGMT_TOTAL = 26          # /30

# ── Riesgos (nombre, prob 1-5, impacto 1-5) ──────────────────────────────
RIESGOS = [
    ("Sustitución por IA (erosión de pricing)", 3, 5),
    ("Desaceleración / meta 100M DAU 2028", 3, 3),
    ("Pivote de monetización no rinde", 3, 3),
    ("Múltiplo sigue comprimido", 3, 3),
    ("Gobernanza / hombre clave (dual-class)", 2, 4),
    ("Dependencia de app stores", 2, 3),
]

# ── Nueve inversores (orden fijo; convicción /10; navy=comprar, ocre=mantener) ──
INVERSORES = [
    ("Graham",       4, "PASS"),
    ("Buffett",      6, "HOLD"),
    ("Munger",       6, "HOLD"),
    ("Fisher",       7, "HOLD"),
    ("Lynch",        6, "HOLD"),
    ("Templeton",    7, "BUY"),
    ("Marks",        6, "HOLD"),
    ("Seilern",      6, "HOLD"),
    ("Terry Smith",  6, "HOLD"),
]

if __name__ == "__main__":
    print("DUOL data module OK · QG", SCORE_QG, TIER_QG, "· val-mos", VEREDICTO,
          "· PWFV", PWFV, "· zona", ZONA_HOY, es(DCTO_HOY))
