# -*- coding: utf-8 -*-
"""ÚNICA FUENTE DE VERDAD NUMÉRICA · Ultra Tesis ADBE (2026-07-06, refresh ligero de precio).
Prosa y gráficos importan de aquí. Cero divergencia. Todo dato etiquetado en su fuente.
Fuentes primarias: Adobe 10-K FY2025 (fin 28-nov-2025), release Q2 FY2026 (11-jun-2026),
stockanalysis.com (deriva de filings), Adobe IR. Fundamentales verificados 2026-07-02;
precio refrescado 2026-07-06 (IBKR, $219.37 vs $220.00 el 2-jul — variación trivial de
-0,3%, no ameritó ningún cambio de fundamentales, WACC o escenarios)."""

TICKER = "ADBE"
FECHA = "6 de julio de 2026"

# ── Precio y mercado [HECHO · IBKR 6-jul-2026] ──────────────────
PRECIO = 219.37            # USD, cierre/intradía reciente (rango 52s $190–$387)
MKT_CAP = 87.2           # USD B
ACCIONES = 397.5         # M (411M cierre FY25; recompras la reducen)
P52_HI, P52_LO = 386.88, 190.12
PICO_2025 = 453.0        # pico mar-2025 antes de la caída
PE_TTM = 12.1
PE_FWD = 8.6             # sobre EPS non-GAAP guía FY26 ~$24.4

# ── Fundamentales FY2025 y TTM [HECHO · 10-K FY25 / release Q2FY26] ───────
REV_FY23, REV_FY24, REV_FY25 = 19.41, 21.51, 23.51   # USD B
REV_TTM = 25.20
DM_FY25, DX_FY25 = 17.65, 5.86      # Digital Media / Digital Experience, USD B
DM_ARR = 19.20                       # Digital Media ARR salida FY25 (+11.5% YoY)
ARR_TOTAL = 27.10                    # ARR total Q2FY26
AI_ARR = 0.50                        # "AI-first ARR" >$500M, triplicó YoY
FIREFLY_ARR = 0.25                   # Firefly ARR >$250M Q1FY26
RPO = 22.27                          # remaining performance obligations Q2FY26
MARGEN_BRUTO = 0.89
MARGEN_OP_GAAP = 0.36
MARGEN_OP_NONGAAP = 0.46
FCF_FY25 = 9.85                      # USD B
FCF_TTM = 10.5                       # aprox TTM a Q2FY26
SBC = 1.95                           # USD B/año
BUYBACK_FY25 = 11.3                  # USD B recomprados FY25
BUYBACK_AUTOR = 25.0                 # autorización recompra vigente
CAJA_STI = 5.63                      # caja + inversiones corto plazo (may-2026)
DEUDA_TOTAL = 7.07
DEUDA_NETA = DEUDA_TOTAL - CAJA_STI  # +1.44 (deuda neta leve)
NOPAT = 7.2                          # NOPAT normalizado aprox [INFERENCIA]
EPS_TTM = 17.48
MAU = 850                            # usuarios activos mensuales, M

# Owner earnings = FCF − 100% SBC (Damodaran puro)
OWNER_EARN = FCF_FY25 - SBC          # 7.90 USD B [ancla conservadora FY25]
OWNER_EARN_TTM = FCF_TTM - SBC       # 8.55 USD B
OE_PS = OWNER_EARN * 1000 / ACCIONES # ~19.9 USD/acción

# ── Guía FY2026 [HECHO · release Q2FY26 11-jun-2026] ─────────────────────
GUIA_REV = (26.50, 26.60)
GUIA_EPS_NONGAAP = (24.35, 24.45)
ARR_CREC_GUIA = 0.102                # crecimiento ARR total (incl. Semrush)
ARR_ORG_GUIA = 0.083                 # ARR ORGÁNICO tras recorte de ~$480M
ARR_RECORTE = 0.480                  # USD B recorte guía ARR (freemium + precios)

# ── QG · 11 reglas (sistema Felipe; ranking QG v1 2026-07-01) ────────────
SCORE_QG = 72.8
RAW_QG = 91          # /125
TIER_QG = "Calidad Sólida"
# (nombre, puntos, máximo)
REGLAS = [
    ("R1 · Escalabilidad",       13, 15),
    ("R2 · Industria",            8, 10),
    ("R3 · Liderazgo",            9, 15),
    ("R4 · Moat",                11, 15),
    ("R5 · Crec. orgánico",       8, 10),
    ("R6 · Diversificación",      7, 10),
    ("R7 · Capital / ROIC",       7, 10),
    ("R8 · Balance",              9, 10),
    ("R9 · Transparencia",        7, 10),
    ("R10 · Gestión",             7, 10),
    ("R11 · Impacto",             5, 10),
]
# radar en escala 0-10
RADAR = [(n, round(p/m*10, 1)) for n, p, m in REGLAS]

# ── WACC construido input a input [INFERENCIA] ───────────────────────────
# Beta elevada a 1.45 (vs ~1.25 histórico) para exigir explícitamente por el
# riesgo de ejecución/disrupción IA y el vacío de liderazgo CEO+CFO. WACC más
# exigente = valoración más conservadora (decisión de Felipe, 2-jul-2026).
RF = 4.5             # 10Y Treasury
BETA = 1.45
ERP = 4.2            # ERP implícito Damodaran
COE = RF + BETA*ERP  # 10.59 coste de equity
KD_AT = 3.0          # coste deuda after-tax
W_E, W_D = 0.98, 0.02
WACC = round(W_E*COE + W_D*KD_AT, 1)   # ~10.4
WACC_PARTES = [("Tasa libre riesgo (10Y)", RF),
               ("Prima riesgo × beta 1.25", round(BETA*ERP, 2)),
               ("Coste de equity", round(COE, 2)),
               ("Ajuste peso deuda", round(WACC-COE, 2)),
               ("WACC", WACC)]

# ── DCF sobre owner earnings, 10 años, 3 escenarios ──────────────────────
def dcf(oe0, g_early, g_mid, g_late, g_term, wacc):
    """oe0 en USD B; devuelve valor patrimonial por acción."""
    r = wacc/100.0
    val = 0.0; oe = oe0
    for t in range(1, 11):
        g = g_early if t <= 3 else (g_mid if t <= 6 else g_late)
        oe *= (1+g)
        val += oe / (1+r)**t
    oe_term = oe*(1+g_term)
    tv = oe_term / (r - g_term)
    val += tv / (1+r)**10
    equity = val - DEUDA_NETA          # restar deuda neta
    return equity*1000/ACCIONES        # USD/acción

# escenarios (g early/mid/late/terminal)  [SUPUESTO probabilístico]
# Oso genuino = disrupción IA que erosiona la franquicia (declive real de owner earnings).
# Probabilidad del oso deliberadamente alta (35%): moat "en fase de prueba" + recorte de guía ARR.
OSO  = dict(g_early=-0.01, g_mid=-0.03, g_late=-0.04, g_term=-0.020, p=0.35)
BASE = dict(g_early=0.07,  g_mid=0.05,  g_late=0.035, g_term=0.025, p=0.45)
TORO = dict(g_early=0.12,  g_mid=0.09,  g_late=0.05,  g_term=0.030, p=0.20)

V_OSO  = round(dcf(OWNER_EARN, OSO['g_early'],  OSO['g_mid'],  OSO['g_late'],  OSO['g_term'],  WACC))
V_BASE = round(dcf(OWNER_EARN, BASE['g_early'], BASE['g_mid'], BASE['g_late'], BASE['g_term'], WACC))
V_TORO = round(dcf(OWNER_EARN, TORO['g_early'], TORO['g_mid'], TORO['g_late'], TORO['g_term'], WACC))
DCF_POND = round(OSO['p']*V_OSO + BASE['p']*V_BASE + TORO['p']*V_TORO)

# ── EPV Greenwald (suelo sin crecimiento) = NOPAT / WACC ─────────────────
EPV = round((NOPAT/(WACC/100.0) - DEUDA_NETA)*1000/ACCIONES)   # USD/acción
PESO_CREC = round((1 - EPV/PRECIO)*100, 1)                     # % del precio en crecimiento

# ── PWFV-Valor VAL-MOS = (2·DCF_ponderado + 1·EPV) / 3 ───────────────────
PWFV = round((2*DCF_POND + EPV)/3)
DCTO_PWFV = round((PRECIO/PWFV - 1)*100, 1)   # negativo = descuento

# ── Zonas VAL-MOS (ancladas al PWFV-Valor) ───────────────────────────────
Z_GANGA = round(PWFV*0.75)      # ≥25% dcto
Z_OPORT = round(PWFV*0.85)      # 15-25% dcto (frontera superior de compra)
Z_JUSTO_SUP = round(PWFV*1.15)  # ±15%
Z_CARO_SUP  = round(PWFV*1.35)  # 15-35% premium
def zona(p):
    if p <= Z_GANGA: return "GANGA FUERTE"
    if p <= Z_OPORT: return "OPORTUNIDAD"
    if p <= Z_JUSTO_SUP: return "PRECIO JUSTO"
    if p <= Z_CARO_SUP: return "CARO"
    return "BURBUJA"
ZONA_HOY = zona(PRECIO)

# ── DCF inverso: g de owner earnings implícito en el precio de hoy ────────
def dcf_inverso(precio):
    from math import isnan
    lo, hi = -0.10, 0.30
    target = (precio*ACCIONES/1000.0) + DEUDA_NETA
    for _ in range(80):
        mid = (lo+hi)/2
        v = 0.0; oe = OWNER_EARN
        for t in range(1, 11):
            oe *= (1+mid); v += oe/(1+WACC/100.0)**t
        tv = oe*(1+0.025)/(WACC/100.0-0.025); v += tv/(1+WACC/100.0)**10
        if v > target: hi = mid
        else: lo = mid
    return round(mid*100, 1)
G_IMPL = dcf_inverso(PRECIO)   # crecimiento implícito %

# ── Asimetría Pabrai (base vs oso desde el precio) ───────────────────────
UPSIDE = round((V_BASE/PRECIO - 1)*100, 1)
DOWNSIDE = round((1 - V_OSO/PRECIO)*100, 1)
ASIMETRIA = round(UPSIDE/abs(DOWNSIDE), 1) if DOWNSIDE > 0 else 99.0

# ── Sensibilidad: PWFV(DCF base) según WACC × g terminal ─────────────────
WACC_GRID = [9.4, 9.9, 10.4, 10.9, 11.4]
GT_GRID = [1.5, 2.0, 2.5, 3.0, 3.5]
def sens(wacc, gt):
    return round(dcf(OWNER_EARN, BASE['g_early'], BASE['g_mid'], BASE['g_late'], gt/100.0, wacc))
SENS = [[sens(w, gt) for gt in GT_GRID] for w in WACC_GRID]

# ── MoS por tier y veredicto ─────────────────────────────────────────────
MOS_REQ = 35        # Sólida
MOS_ACTUAL = round((1 - PRECIO/PWFV)*100, 1)
TECHO_MULT = 25     # Sólida
MULT_OE = round(PRECIO/OE_PS, 1)
GATILLO_OPORT = Z_OPORT
GATILLO_GANGA = Z_GANGA

# ── Multiplos vs historia [HECHO/INFERENCIA] ─────────────────────────────
PE_HIST_3A = 42     # PER medio 3-5 años atrás (época $500-600)
PFCF_HOY = round(MKT_CAP/FCF_FY25, 1)
PFCF_HIST = 32

# ── Proyección posición 5 años (por escenario, desde precio hoy) ─────────
def proyeccion(vfin):
    cagr = (vfin/PRECIO)**(1/5)-1
    return [round(PRECIO*(1+cagr)**t) for t in range(0, 6)]
PROY_OSO  = proyeccion(V_OSO)
PROY_BASE = proyeccion(V_BASE)
PROY_TORO = proyeccion(V_TORO)

# ── Derivados para prosa/gráficos (que el cambio de WACC propague) ───────
MOS_PLENO = round(PWFV*0.65)                       # gatillo MoS 35% (Sólida)
SENS_MIN = min(min(r) for r in SENS)               # peor celda de sensibilidad
SENS_MAX = max(max(r) for r in SENS)
ASIM_GANGA = round((V_BASE/Z_GANGA - 1)/(1 - V_OSO/Z_GANGA), 1)   # asimetría en GANGA
DCTO_ABS = round(abs(DCTO_PWFV))
G_IMPL_TXT = ("declive perpetuo" if G_IMPL < 0 else
              ("crecimiento casi nulo" if G_IMPL < 3 else "crecimiento moderado"))
PROY_POND = round(OSO['p']*PROY_OSO[-1] + BASE['p']*PROY_BASE[-1] + TORO['p']*PROY_TORO[-1])
RET_POND = round((PROY_POND/PRECIO - 1)*100)       # retorno esperado 5 años, %
def es(x, dec=0):   # formato español con coma
    return f"{x:.{dec}f}".replace(".", ",")

if __name__ == "__main__":
    print(f"ADBE {FECHA} · precio ${PRECIO}")
    print(f"Owner earnings ${OWNER_EARN}B  (${OE_PS:.1f}/acc)  ·  P/OE {MULT_OE}x (techo {TECHO_MULT}x)")
    print(f"WACC {WACC}%  ·  EPV ${EPV}  (peso crecimiento {PESO_CREC}%)")
    print(f"DCF  oso ${V_OSO} / base ${V_BASE} / toro ${V_TORO}  ponderado ${DCF_POND}")
    print(f"PWFV-Valor (2·DCF+EPV)/3 = ${PWFV}  ·  descuento hoy {DCTO_PWFV}%  ·  zona {ZONA_HOY}")
    print(f"DCF inverso: g implícito {G_IMPL}%  ·  base rate: {'declive/estancamiento' if G_IMPL<3 else 'moderado'}")
    print(f"Asimetría {ASIMETRIA}:1  (up {UPSIDE}% / down {DOWNSIDE}%)")
    print(f"MoS actual {MOS_ACTUAL}% vs req {MOS_REQ}%  ·  gatillos: OPORT ${GATILLO_OPORT} / GANGA ${GATILLO_GANGA}")
    print(f"Zonas: GANGA≤{Z_GANGA} · OPORT≤{Z_OPORT} · JUSTO≤{Z_JUSTO_SUP} · CARO≤{Z_CARO_SUP} · BURBUJA>")
