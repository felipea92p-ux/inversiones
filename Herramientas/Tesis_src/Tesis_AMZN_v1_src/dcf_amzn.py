# -*- coding: utf-8 -*-
"""FUENTE ÚNICA DE VERDAD · Tesis Ultra AMZN v2.0 (corte 9-jul-2026, corrección val-mos).
Datos verificados en fuente primaria: 10-K FY2025 + 10-Q Q1 2026 + DEF 14A 2026
(SEC EDGAR CIK 0001018724). Eje CALIDAD (qg-seilern) SIN TOCAR: 80.2, Alta
convicción — esta corrida es 100% del eje VALORACIÓN (val-mos).

QUÉ CAMBIÓ v1→v2 y por qué (verificación adversarial 9-jul-2026, ver
`valmos-verificacion-amzn-9jul2026`): el WACC=9,0% de v1 era una "beta regalada"
(8,5% escalón tier + 0,5pp recargo) que ignoraba el CAPM propio. Reconstruido con
datos de hoy — beta 1,47 (GuruFocus), Rf 4,55% (10Y UST 7/8-jul-2026), ERP 4,23%
(Damodaran, implícito real, NO el rango genérico 4,5-5,0% que usaba v1) — el WACC
bottom-up cae en 10,0-10,5%; el punto usado es 10,4%, sostenido por una emisión
sorpresa de bonos AMZN de US$25.000M el 8-jul-2026 (Treasury+100pb, spreads
hyperscaler ensanchándose) que confirma que el mercado de crédito ya empieza a
cobrar precio por el súper-capex. Segundo hallazgo central: el ROIC incremental
de AWS medido en 10-K (op.income/activos promedio, FY25 vs FY24) da ~8,0% — por
DEBAJO del WACC, y casi exacto al supuesto del escenario BEAR (8%), no al BASE
(16%). Jassy confirmó en la call Q1'26 el mecanismo de lag capex→facturación
("6 a 24 meses"), lo que sesga ese 8,0% a la baja — pero la trayectoria real de
márgenes AWS (39,5%→32,9%→35,4% FY→37,7% Q1'26) muestra una recuperación PARCIAL,
no completa, un año después. Con esa evidencia se repesan los tres escenarios
hacia el bear (25/45/30 → 35/40/25) y se escalan los tres valores por el WACC más
bajo — los dos efectos casi se cancelan: PWFV pasa de $161 (v1, WACC regalado) a
$108 (v2, WACC honesto + pesos corregidos), con banda defendible $92-121. El
detector pasa de PASA a GRIS: se suma la concentración OpenAI (hasta $138.000M en
compromisos) a la ya conocida circularidad Anthropic como segundo vector de
calidad-de-ingresos. VEREDICTO SOBREVIVE: ESPERAR, y no al filo — resiste incluso
en el extremo más favorable a AMZN ($121 PWFV, -50% MoS) que la verificación pudo
construir razonablemente."""

def es(x, dec=1):
    return f"{x:.{dec}f}".replace(".", ",")

def pct(x, dec=1):
    return es(x, dec) + "%"

# ── Identidad / mercado (6-jul-2026) ─────────────────────────────────────
PRECIO       = 244.59
ACCIONES     = 10757        # M
MKTCAP       = 2.63         # US$T
EV           = 2.70         # US$T (incl. leases LP)
ATH          = 278.56       # máximo 52 semanas
LOW_52       = 196.00
CAIDA_MAX    = -12.2        # % desde máximo — clave: apenas ha caído
BETA         = 1.47         # v2: GuruFocus "as of jun-2026" (v1 usaba 1.46)

# ── EJE CALIDAD (qg-seilern, corregido) ──────────────────────────────────
SCORE_QG = 80.2
RAW_QG   = 100.25
TIER_QG  = "Alta convicción"
# (nombre, puntos ponderados, máximo) — R3/R4 capados a 10 por el verificador
REGLAS = [
    ("R1 · Escalabilidad",       11.25, 15),
    ("R2 · Industria",            9.0, 10),
    ("R3 · Liderazgo",           15.0, 15),
    ("R4 · Moat",                15.0, 15),
    ("R5 · Crec. orgánico",       7.5, 10),
    ("R6 · Diversificación",      8.5, 10),
    ("R7 · Capital / ROIC",       6.0, 10),
    ("R8 · Balance",              7.5, 10),
    ("R9 · Transparencia",        6.0, 10),
    ("R10 · Gestión",             7.5, 10),
    ("R11 · Impacto",             7.0, 10),
]
RADAR = [
    ("R1", 7.5), ("R2", 9.0), ("R3", 10.0), ("R4", 10.0), ("R5", 7.5),
    ("R6", 8.5), ("R7", 6.0), ("R8", 7.5), ("R9", 6.0), ("R10", 7.5), ("R11", 7.0),
]

# ── EJE VALORACIÓN (val-mos, corregido por verificación adversarial 9-jul-2026) ─
DETECTOR = "GRIS"        # no PASA limpio: apalancamiento acelerado (bono $25.000M
                          # 8-jul-2026) + circularidad Anthropic+OpenAI (hasta $138.000M)
PWFV     = 108            # US$/acción — ancla tri-método, banda defendible $92-121
EPV      = 62             # suelo sin crecimiento — ajuste menor proporcional al WACC (v1: 71)
V_POND   = 108            # ponderado por escenarios (misma fórmula que PWFV)
OE_TTM   = 58             # owner earnings normalizado US$B (rango honesto 55-75; bajista 42)
WACC     = 10.4           # CAPM bottom-up (beta 1.47, ERP Damodaran real 4.23%) ponderado
                           # con deuda a valor de mercado; defendible 10.0-10.5% (v1: 9.0% "regalado")
TERMINAL = 3.0
V_BEAR, P_BEAR = 26, 35    # ROIC=8% (el dato MEDIDO en 10-K); prob. sube 25→35 tras verificación
V_BASE, P_BASE = 133, 40   # ROIC=16%; prob. baja 45→40 — sigue siendo el escenario dominante
V_BULL, P_BULL = 182, 25   # ROIC=27% (precedente AWS 2014-16, a 1/25-1/50 de la escala actual)
# DCF inverso — candado HEROICO activo
G_IMPL   = 20.0           # g implícita en el precio (owner earnings, década)
G_GUIA   = 23.1          # CAGR EPS normalizado del consenso FY26-28 (ya asume éxito pleno)
G_CAGR   = 11.1          # CAGR revenue histórico
G_CONS   = 12.0          # escenario conservador propio
# zonas ancladas al PWFV
Z_GANGA  = 81            # ≤75% del PWFV
Z_OPORT  = 92            # 75-85%
Z_JUSTO  = 124           # ±15%
Z_CARO   = 146           # +15% a +35%
MOS_EXIG = 35            # % — 25% tier Alta + 10pp candado HEROICO (sin cambio)
MOS_HOY  = -55.8         # % — PWFV/precio − 1 (v1: -34.2%; banda verificación -50% a -62%)
PRIMA    = 126.5         # % — precio/PWFV − 1 (v1: 51.9%)
ASIMETRIA = -0.51        # (V_BASE-PRECIO)/(PRECIO-V_BEAR) — v1 no la declaraba; verificación estima ~-0.54
ZONA_HOY = "BURBUJA"      # ratio precio/PWFV ~2.26x (verificación: banda 2.2-2.4x, "sobrevive intacta")
VEREDICTO = "ESPERAR"
GATILLO_T1 = 81          # tramo 1 (3% NAV): zona GANGA
GATILLO_PLENO = 70       # posición plena: MoS 35% (candado HEROICO), = 0.65×PWFV
CAIDA_A_GANGA = -71      # % desde máximo para llegar a GANGA

# ── Sensibilidad WACC × g terminal (valor base US$/acción) ───────────────
WACC_GRID = [9.4, 9.9, 10.4, 10.9, 11.4]
GT_GRID   = [2.0, 2.5, 3.0, 3.5, 4.0]
SENS = [
    [140, 146, 153, 160, 169],
    [132, 137, 142, 149, 156],
    [125, 129, 133, 139, 145],   # fila WACC 10,4 · col g 3,0 = 133 (base)
    [118, 121, 125, 130, 135],
    [112, 115, 117, 121, 126],
]
SENS_MAX = 169             # ni la mejor celda alcanza el precio de 244,59

# ── WACC construcción ────────────────────────────────────────────────────
RF   = 4.55
ERP  = 4.23                # Damodaran, ERP implícito real (v1 usaba rango genérico 4.5-5.0%)
COE_CAPM = round(RF + BETA * ERP, 1)   # ~10,77 → 10,8% (Ke sin ajuste de beta)

# ── Serie financiera anual (US$B) · FY cierra 31-dic ─────────────────────
YRS_FIN = ["2021", "2022", "2023", "2024", "2025", "TTM"]
REVENUE = [469.8, 514.0, 574.8, 638.0, 716.9, 742.8]
OP_INC  = [24.9, 12.2, 36.9, 68.6, 80.0, 85.4]
OP_MGN  = [5.3, 2.4, 6.4, 10.8, 11.2, 11.5]
NET_INC = [33.4, -2.7, 30.4, 59.2, 77.7, 90.8]
CFO     = [46.3, 46.8, 84.9, 115.9, 139.5, 148.5]
CAPEX   = [61.1, 63.6, 52.7, 83.0, 131.8, 151.0]
FCF     = [None, None, None, 38.2, 11.2, -2.5]   # definición Amazon (2024/2025 reportado)
SBC     = [12.8, 19.6, 24.0, 22.0, 19.5, 19.8]
DYA_TTM = 70.4
CAPEX_2026E = 200

# ── Segmentos (Q1'26; rev US$B, margen OI % Q1'25 → Q1'26) ──────────────
SEG = [
    ("North America", 104.1, 6.3, 7.9),
    ("International", 39.8, 3.0, 3.6),
    ("AWS", 37.6, 39.5, 37.7),
]
AWS_YOY_SERIE = [17, 17, 20, 24, 28]     # aceleración 5 trimestres
AWS_Q = ["Q1'25", "Q2'25", "Q3'25", "Q4'25", "Q1'26"]
AWS_MGN_TTM = [37.0, 35.2]               # margen TTM a/a (comprime por depreciación)
ADS_TTM = 72                             # US$B publicidad TTM (+22-24%)
UNITS_YOY = 15                           # unit growth WW — máximo post-covid
MIX_3P = 60                              # % unidades 3P
AWS_BACKLOG = 364                        # US$B (+93%), sin incluir Anthropic >$100B
NI_Q1 = 30.3; ANTHROPIC_Q1 = 16.8       # US$B; NI normalizado Q1 ~$17.5B, EPS ~$1.60 plano
EPS_Q1_REP = 2.78; EPS_Q1_NORM = 1.60

# ── Balance / deuda (el giro) ────────────────────────────────────────────
DEUDA_LP = [65.6, 119.1]                 # dic-25 → mar-26 (+$53.4B en un trimestre)
CAJA_NETA = [54.7, 21.2]                 # posición neta dic-25 → mar-26
LEASES_LP = 90.8

# ── Múltiplos: las tres lentes en desacuerdo ─────────────────────────────
# (lente, actual, mediana histórica, lectura)
LENTES = [
    ("EV/EBITDA", 16.8, 27.6, "barato vs historia"),
    ("P/OCF", 17.7, 22.5, "razonable"),
    ("P/Owner Earnings", 45.0, None, "caro: paga crecimiento perfecto"),
]
PE_GAAP = 23.7           # espejismo (inflado por Anthropic)
PE_LIMPIO = 45           # ~43-48x sobre NI ex-Anthropic
CONSENSO_PT = 313        # Strong Buy, upside +28% — el sistema discrepa de la calle

# ── Porter por segmento (/25, menor = mejor foso) ────────────────────────
PORTER_SEG = [
    ("Logística (#1 carrier US)", 10),
    ("Publicidad (datos de intención)", 11),
    ("AWS (switching costs + silicio)", 12),
    ("E-commerce (vs Walmart)", 14),
]
PORTER_POND = 11.75

# ── TAM (US$B, 2026) ─────────────────────────────────────────────────────
MERCADOS = [
    ("E-commerce global", 4500, 420, "penetración ~9% del retail"),
    ("Cloud IaaS/PaaS", 389, 129, "#1 con ~30% de cuota"),
    ("Publicidad digital", 662, 72, "#3, el que más rápido gana"),
    ("Logística 3P (opción)", 450, 0, "de coste a negocio"),
]

# ── Management (6 dimensiones, /5) → 23/30 ───────────────────────────────
MGMT = [
    ("ROIC vs WACC", 3.5),
    ("Track record M&A", 3.5),
    ("Insiders + recompra", 4.0),
    ("Guidance vs resultados", 4.0),
    ("Ownership / skin (Bezos 8,8%)", 4.5),
    ("Capital allocation lifecycle", 3.5),
]
MGMT_TOTAL = 23.0

# ── Riesgos (nombre, prob 1-5, impacto 1-5) ──────────────────────────────
RIESGOS = [
    ("Capex $200B sin ROIC probado (deuda + FCF cero)", 3, 5),
    ("Reversión de Anthropic (down-round revierte $16,8B)", 3, 4),
    ("De-rating: el mercado normaliza los earnings", 3, 4),
    ("Antitrust FTC (juicio feb-2027, corazón del flywheel)", 2, 4),
    ("AWS pierde cuota relativa (Azure +40% / GCP +63%)", 3, 3),
    ("Laboral / sindical en la red logística", 2, 3),
]

# ── Nueve inversores ─────────────────────────────────────────────────────
INVERSORES = [
    ("Graham",       3, "PASS"),
    ("Buffett",      6, "HOLD"),
    ("Munger",       6, "HOLD"),
    ("Fisher",       7, "HOLD"),
    ("Lynch",        5, "HOLD"),
    ("Templeton",    3, "PASS"),
    ("Marks",        4, "PASS"),
    ("Seilern",      6, "HOLD"),
    ("Terry Smith",  5, "HOLD"),
]

if __name__ == "__main__":
    print("AMZN data OK · QG", SCORE_QG, TIER_QG, "· val-mos", VEREDICTO,
          "· WACC", pct(WACC), "· PWFV", PWFV, "· zona", ZONA_HOY, "· prima", pct(PRIMA))
    tot = sum(p for _, p, _ in REGLAS)
    print("check raw:", tot, "→", round(tot/125*100, 1))
    assert abs(tot - RAW_QG) < 0.05, f"suma REGLAS ({tot}) != RAW_QG ({RAW_QG})"
    assert abs(round(RAW_QG/125*100, 1) - SCORE_QG) < 0.15, "SCORE_QG no cuadra con RAW_QG/125*100"
    pond = V_BEAR*P_BEAR/100 + V_BASE*P_BASE/100 + V_BULL*P_BULL/100
    print("check PWFV ponderado:", round(pond, 1), "vs declarado", PWFV)
    assert abs(pond - PWFV) < 2.0, f"PWFV ponderado ({pond:.1f}) se aleja del declarado ({PWFV})"
    asim_recomp = (V_BASE - PRECIO) / (PRECIO - V_BEAR)
    print("check ASIMETRIA recomputada:", round(asim_recomp, 2), "vs declarada", ASIMETRIA)
    assert abs(asim_recomp - ASIMETRIA) / abs(asim_recomp) < 0.15, "ASIMETRIA declarada se aleja de la recomputada"
    mos_recomp = (PWFV / PRECIO - 1) * 100
    print("check MOS_HOY recomputado:", round(mos_recomp, 1), "vs declarado", MOS_HOY)
    print("AUTO-CHEQUEO OK")
