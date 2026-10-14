# -*- coding: utf-8 -*-
"""FUENTE ÚNICA DE VERDAD · Tesis Ultra MELI v1.0 (corte 6-jul-2026).
Datos verificados en fuente primaria: 10-K FY2025 + 10-Q Q1 2026 + shareholder letters
(SEC EDGAR CIK 0001099590). Ejes: qg-seilern (CALIDAD, corregido por verificador
adversarial: 64.8→72.0, tier Calidad sólida — el primer pase fue demasiado duro,
invirtió la mecánica de R9/R10) + val-mos v3 (VALORACIÓN: zona BURBUJA, veredicto
ESPERAR — corregido de "VIGILAR" por el verificador, asimetría 0.56:1 activa la
regla textual de mos_sizing.md)."""

def es(x, dec=1):
    return f"{x:.{dec}f}".replace(".", ",")

def pct(x, dec=1):
    return es(x, dec) + "%"

# ── Identidad / mercado (6-jul-2026) ─────────────────────────────────────
PRECIO       = 1805.68
ACCIONES     = 50.7        # M, verificado SEC 10-K/10-Q (no 47-48M como en un primer supuesto)
MKTCAP       = 91.5        # US$B
EV           = 97.2        # US$B (deuda neta +5.7B)
CAJA_NETA    = -5.748      # US$B (neto DEUDOR, no neto caja — deuda neta positiva)
DEUDA_TOTAL  = 12.345      # US$B (Q1'26)

# ── EJE CALIDAD (qg-seilern, corregido por verificador adversarial) ──────
SCORE_QG = 72.0
RAW_QG   = 90.0
TIER_QG  = "Calidad sólida"
REGLAS = [
    ("R1 · Escalabilidad",        11.0, 15),
    ("R2 · Industria",             9.0, 10),
    ("R3 · Liderazgo",            10.0, 15),
    ("R4 · Moat",                 11.0, 15),
    ("R5 · Crec. orgánico",        7.0, 10),
    ("R6 · Diversificación",       7.0, 10),
    ("R7 · Capital / ROIC",        6.0, 10),
    ("R8 · Balance",               6.0, 10),
    ("R9 · Transparencia",         7.0, 10),
    ("R10 · Gestión",              6.0, 10),
    ("R11 · Impacto",             10.0, 10),
]
RADAR = [
    ("R1", 7.3), ("R2", 9.0), ("R3", 6.7), ("R4", 7.3), ("R5", 7.0),
    ("R6", 7.0), ("R7", 6.0), ("R8", 6.0), ("R9", 7.0), ("R10", 6.0), ("R11", 10.0),
]

# ── EJE VALORACIÓN (val-mos v3, corregido por verificador adversarial) ──
DETECTOR = "GRIS"          # PASA CON VIGILANCIA — 1 señal corroborada (compresión de
                           # margen, ~390pb de origen crediticio), decisión DELIBERADA
                           # de management (no drift pasivo) — CFO lo confirmó en vivo.
PWFV     = 1101
EPV      = 347.7           # corregido: ACCIONES=50.7M (no 47-48M), OE/WACC=2.38/0.135
V_POND   = 1101
WACC     = 13.5
TERMINAL = 3.5
V_BEAR, P_BEAR = 508, 30
V_BASE, P_BASE = 1083, 50
V_BULL, P_BULL = 2036, 20
G_IMPL   = 38.1
G_CONS   = 19.8
G_OPT    = 39.0
DCF_CLASE = "HEROICAS"     # simplificado por el verificador: 38,1 cae técnicamente
                           # bajo 39,0 (RAZONABLES por la letra) pero al 95% de la
                           # banda — más honesto llamarlo HEROICAS sin ambigüedad.
# Zonas (tier Calidad sólida: GATE binario, solo elegible en Ganga/Oportunidad)
Z_GANGA  = round(PWFV * 0.70, 0)    # 771
Z_OPORT  = round(PWFV * 0.85, 0)    # 936
Z_JUSTO  = round(PWFV * 1.10, 0)    # 1211
Z_CARO   = round(PWFV * 1.35, 0)    # 1486
MOS_ACTUAL = -64.0          # negativo: precio ya está muy por encima del PWFV
ZONA_HOY = "BURBUJA"        # 164% del PWFV — muy por encima del umbral >135%
VEREDICTO = "ESPERAR"       # corregido de "VIGILAR": asimetría 0,56:1 < 2:1 activa
                             # la regla textual de mos_sizing.md ("ESPERAR sin
                             # importar cuán bueno sea el patrón")
GATE_TIER = ("El tier 'Calidad sólida' (65-74) NO se compra fuera de zonas Ganga/Oportunidad: "
             "es un GATE binario, no un umbral de MoS más exigente. MELI está en BURBUJA — excluida por regla.")
TECHO_MULT_TIER = 25        # x owner earnings — el techo del tier
MULT_NORMALIZADO = 38.5     # x owner earnings (ingreso neto normalizado; corregido de 44-47x)
MULT_FCF_REAL = 8.7         # x CFO simple (ilusorio, distorsionado por crecimiento del libro de crédito)
MULT_PS = 3.2                # contraste diagnóstico (valoracion.md): MKTCAP/REVENUE[TTM] = 91.5/28.89.
                              # Distorsión de MELI es de working capital (libro de crédito), no de
                              # capex —capex/revenue ~4,6%, no cruza el umbral de 20%— pero el P/S
                              # bajo por sí solo tampoco rescata el veredicto: zona BURBUJA y candado
                              # duro violado son gates independientes del múltiplo elegido.
PRECIO_EPV = 5.2            # x EPV (corregido de 7,95x)
GATILLO_OPORT = 936
GATILLO_GANGA = 771
ASIMETRIA = -0.56           # (V_BASE-PRECIO)/(PRECIO-V_BEAR) — signo corregido 8-jul-2026:
                             # el precio YA SUPERA el propio escenario base (no hay "upside a
                             # base", solo downside a bear); el +0,56 original invertía el signo
                             # por error aritmético. La magnitud y el veredicto no cambian.

# ── Sensibilidad WACC × g terminal ───────────────────────────────────────
WACC_GRID = [11.5, 12.5, 13.5, 14.5, 15.5]
GT_GRID   = [2.5, 3.0, 3.5, 4.0, 4.5]
SENS = [
    [1340, 1390, 1445, 1505, 1570],
    [1180, 1220, 1265, 1315, 1370],
    [1050, 1080, 1101, 1140, 1180],   # fila WACC 13,5 · col g 3,5 = 1101 = base
    [945, 970, 1000, 1030, 1065],
    [860, 880, 905, 930, 960],
]
SENS_MAX = 1570

# ── WACC construcción (blend de riesgo-país ponderado por ingresos) ─────
RF   = 4.5
ERP  = 4.5
BETA = 1.34
COE_CAPM = round(RF + BETA * ERP, 1)
PRIMA_PAIS_BLEND = 8.68     # Brasil 54%×7,6 + México 22%×6,7 + Argentina 19%×14,5 + Otros 5%×7
LAMBDA_EXPOSICION = 0.55

# ── Serie financiera anual (US$M) · FY cierra 31-dic ─────────────────────
YRS_FIN = ["2021", "2022", "2023", "2024", "2025", "Q1'26"]
REVENUE = [7069, 10537, 15107, 20777, 28893, 8845]
OP_INC  = [441, 1034, 2207, 2631, 3201, 611]
OP_MGN  = [6.2, 9.8, 14.6, 12.7, 11.1, 6.9]
NET_INC = [83, 482, 987, 1911, 1997, 417]
NET_MGN = [1.2, 4.6, 6.5, 9.2, 6.9, 4.7]
CFO     = [965, 2940, 5140, 7918, 12116, None]
CAPEX   = [None, None, 509, 860, 1327, None]
FCF_SIMPLE = [None, None, None, 7058, 10789, None]
FCF_AJUSTADO = [None, None, 1439, 1215, 1481, -56]

# ── Balance / deuda / crédito ─────────────────────────────────────────────
NET_DEBT_SERIE = [1505, 2247, 2768, 3830, 4605, 4682, 5748]   # US$M, dic23→mar26
NET_DEBT_YRS = ["Dic'23", "Dic'24", "Mar'25", "Jun'25", "Sep'25", "Dic'25", "Mar'26"]
CREDITO_GROSS = [6573, 12508, 14555]     # FY24, FY25, Q1'26 US$M
CREDITO_YRS = ["FY24", "FY25", "Q1'26"]
ALLOWANCE = [1678, 3143, 3820]
CREDITO_PCT_ASSETS_GROSS = [26.1, 29.3, 31.0]
WRITEOFF_RATE = [32.3, 17.1, 18.8, 19.4]   # FY23,FY24,FY25,Q1'26 anualizado
WRITEOFF_YRS = ["FY23", "FY24", "FY25", "Q1'26 anual."]

# ── NIMAL (net interest margin after losses) — serie completa ────────────
NIMAL_SERIE = [36.5, 32.0, 36.2, 28.2, 22.4, 17.8]
NIMAL_YRS = ["2021", "2022", "2023", "2024", "2025", "Q1'26"]
PROVISION_PCT_REV = [7.0, 8.9, 10.7, 14.1]   # FY23,FY24,FY25,Q1'26
PROVISION_YRS = ["FY23", "FY24", "FY25", "Q1'26"]

# ── Segmentos geográficos (direct contribution margin, %) ────────────────
SEG_MARGEN = [
    ("Brasil",     23.79, 20.04, 13.65, 17.6, 8.2),
    ("México",     22.79, 18.31, 18.08, 17.7, 17.4),
    ("Argentina",  47.32, 43.87, 41.61, 46.9, 35.7),
]
# columnas: nombre, FY23, FY24, FY25, Q1'25, Q1'26

# ── KPIs operativos ───────────────────────────────────────────────────────
GMV_GROWTH_BRASIL = [30, 29, 34, 35, 38]      # Q1'25→Q1'26 FX-neutral
GMV_GROWTH_MEXICO = [23, 32, 34, 35, 28]
GMV_GROWTH_ARG    = [126, 75, 44, 42, 41]
KPI_QTRS = ["Q1'25", "Q2'25", "Q3'25", "Q4'25", "Q1'26"]
FINTECH_MAU = 83     # M, Q1'26, +29% YoY
TPV_Q1_26 = 87.2     # US$B, +50% YoY
REV_MIX = [("Brasil", 54), ("México", 22), ("Argentina", 19), ("Otros", 5)]

# ── Múltiplos ─────────────────────────────────────────────────────────────
PE_TRAILING = 44.1
PE_FORWARD = 39.5
PE_MEDIANA_3A = 64.3
EV_EBITDA = 24.5
CONSENSO_PT = 2217          # previo a downgrades UBS/Citi
CONSENSO_RATING = "Buy (pre-downgrade)"
UBS_PT = 2050
CITI_DOWNGRADE = True

# ── Porter (promedio, /5, menor = mejor foso) ────────────────────────────
PORTER_SEG = [
    ("Logística (Mercado Envíos)", 2.2),
    ("Fintech (Mercado Pago)",     3.0),
    ("Marketplace e-commerce",     3.4),
]
PORTER_POND = 3.0

# ── TAM (US$B, 2026) ──────────────────────────────────────────────────────
MERCADOS = [
    ("E-commerce LatAm", 215, 29, "~40% Brasil"),
    ("Pagos digitales LatAm", 788, 20, "TPV +50% YoY"),
    ("Crédito al consumo LatAm", 400, 15, "México/Arg. sub-penetrados"),
]

# ── Management (6 dimensiones, /5) → total /30 ───────────────────────────
MGMT = [
    ("Transición CEO (Galperin→Szarfsztejn, ene-2026)", 3.0),
    ("Independencia del consejo (7/9)", 3.0),
    ("Compensación ejecutiva", 3.0),
    ("Partes relacionadas (2 Galperin en directorio)", 2.0),
    ("Disciplina de capital (buyback 2025 = US$4,05M)", 2.0),
    ("Transparencia (Adjusted FCF divulgado voluntariamente)", 4.0),
]
MGMT_TOTAL = 17.0

ISS_BOARD_SCORE = 10    # peor decil (probable, no verificado en fuente primaria — Yahoo/ISS licencia)
BUYBACK_2025 = 4.05      # US$M — no cientos de millones; destinado a compensar dilución de plan de directores
GALPERIN_OWNERSHIP = 6.7

# ── Riesgos (nombre, prob 1-5, impacto 1-5) ──────────────────────────────
RIESGOS = [
    ("Deterioro de calidad crediticia (NIMAL, write-offs)", 3, 4),
    ("Competencia Shopee (Brasil, EBITDA-positivo, +53% YoY)", 3, 3),
    ("Gobernanza (ISS Board=10, familia Galperin en directorio)", 4, 3),
    ("Fragilidad macro Argentina (inflación reacelerando, peg con soporte FMI)", 3, 3),
    ("Múltiplo caro vs. pares mejor suscritos (Nu Holdings 14-15x)", 4, 3),
    ("Nubank gana en calidad de suscripción de crédito", 3, 3),
]

# ── Nueve inversores ─────────────────────────────────────────────────────
INVERSORES = [
    ("Graham",       3, "PASS"),
    ("Buffett",      4, "HOLD"),
    ("Munger",       4, "HOLD"),
    ("Fisher",       5, "HOLD"),
    ("Lynch",        4, "PASS"),
    ("Templeton",    3, "PASS"),
    ("Marks",        5, "HOLD"),
    ("Seilern",      4, "PASS"),
    ("Terry Smith",  3, "PASS"),
]

if __name__ == "__main__":
    print("MELI data OK ·", SCORE_QG, TIER_QG, "· val-mos", VEREDICTO,
          "· PWFV", PWFV, "· zona", ZONA_HOY)
    tot = sum(p for _, p, _ in REGLAS)
    print("check raw:", tot, "→", round(tot/125*100, 1))
    print("check EPV total:", round(2.38e3/0.135, 1), "/", ACCIONES, "=", round(2.38e3/0.135/ACCIONES, 1))
