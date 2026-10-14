# -*- coding: utf-8 -*-
"""FUENTE ÚNICA DE VERDAD · Tesis Ultra TSM v1.1 (corte 10-jul-2026).
Datos verificados en fuente primaria: Form 20-F FY2025 + Q1 2026 earnings release/presentación.
Ejes: qg-seilern (CALIDAD 78.4/100, Alta Convicción, verificado sin corrección) + val-mos v3
(VALORACIÓN: zona BURBUJA con prima geopolítica de riesgo país en el WACC — la variable que sola
decide la zona; veredicto VIGILAR, verificado sin corrección).
Nota de precio: el modelo de valoración se ancló al precio de referencia ~US$477 (máximo histórico
30-jun-2026); la cotización en vivo de IBKR al corte de este documento es US$442,35 — ambos
niveles sostienen la misma conclusión (Burbuja/Caro, candado duro violado, HEROICAS).

v1.1 (10-jul-2026) — verificación adversarial final del ancla, DOS hallazgos añadidos como
cross-check metodológico. NINGÚN número de valoración cambia (PWFV, WACC, zonas, veredicto
idénticos a v1.0) — el ataque no encontró base para mover el ancla; de hecho el sesgo residual
apunta a que US$236 es conservador, no agresivo. Qué se agregó, con honestidad sobre sus límites:
(1) ROIC_INCR_* — cross-check de ROIC incremental (ΔOpInc/ΔActivos, 2021-2025) que corrobora
R7/el moat de capital, MENOS comparable con el mismo cálculo hecho para AWS de lo que una lectura
superficial sugeriría (aquí son activos DE TODA LA COMPAÑÍA sobre ventanas de 1-5 años; AWS usa
activos DE SEGMENTO sobre 1 año) — ver caveat en el bloque. (2) PROB_INVASION_* — probabilidades
de horizonte largo (Metaculus/Manifold) verificadas en vivo y exactas, usadas para anclar
conceptualmente la prima permanente de WACC. Se descarta explícitamente usar Polymarket de corto
plazo (evento de 6-12 meses, no un riesgo perpetuo) y se descarta reciclar cualquier umbral de
zona ya calculado (Z_GANGA) como si fuera un escenario geopolítico modelado de forma independiente
— ambos eran los dos defectos reales que encontró la verificación adversarial, ninguno de los dos
en el propio dcf_tsm.py (vivían en un documento de "validación independiente" que nunca llegó a
publicarse en la tesis, y por eso no requiere corrección aquí — solo no se repite el error)."""

def es(x, dec=1):
    return f"{x:.{dec}f}".replace(".", ",")

def pct(x, dec=1):
    return es(x, dec) + "%"

# ── Identidad / mercado (6-jul-2026, cotización IBKR) ────────────────────
PRECIO       = 442.35
PRECIO_REF_MODELO = 477.57   # ATH 30-jun-2026, precio contra el que se ancló el DCF inverso
ACCIONES     = 5.186         # B, ADR-equivalente
MKTCAP       = 2294          # US$B (a precio IBKR)
EV           = 2261          # US$B (caja neta positiva ~-33B, i.e. resta)
CAJA_NETA    = 67.1          # US$B neta positiva (caja+valores ~100B vs deuda ~32.9B)
DEUDA_TOTAL  = 32.9          # US$B

# ── EJE CALIDAD (qg-seilern, verificado sin corrección) ──────────────────
SCORE_QG = 78.4
RAW_QG   = 98.0
TIER_QG  = "Alta Convicción"
REGLAS = [
    ("R1 · Escalabilidad",       11.0, 15),
    ("R2 · Industria",            8.0, 10),
    ("R3 · Liderazgo",           13.0, 15),
    ("R4 · Moat",                13.0, 15),
    ("R5 · Crec. orgánico",      10.0, 10),
    ("R6 · Diversificación",      2.0, 10),
    ("R7 · Capital / ROIC",       9.0, 10),
    ("R8 · Balance",             10.0, 10),
    ("R9 · Transparencia",        9.0, 10),
    ("R10 · Gestión",             7.0, 10),
    ("R11 · Impacto",             6.0, 10),
]
RADAR = [
    ("R1", 7.3), ("R2", 8.0), ("R3", 8.7), ("R4", 8.7), ("R5", 10.0),
    ("R6", 2.0), ("R7", 9.0), ("R8", 10.0), ("R9", 9.0), ("R10", 7.0), ("R11", 6.0),
]

# ── EJE VALORACIÓN (val-mos v3, verificado sin corrección) ──────────────
DETECTOR = "PASA"          # limpio — márgenes/ROE/ingresos acelerando, sin señales de trampa
PWFV     = 236             # ancla primaria: CON prima geopolítica (R6=2/10 confirmado severo)
PWFV_SIN_PRIMA = 360       # referencia de sensibilidad, sin prima geopolítica
EPV      = 49.2            # US$/ADR, con prima, base OE FY25 (deprimido por pico de capex)
EPV_FY26E = 69.3           # con prima, base OE FY26E estimado
V_POND   = 236
WACC     = 12.19
WACC_SIN_PRIMA = 9.72
TERMINAL = 4.0
V_BEAR, P_BEAR = 142, 25
V_BASE, P_BASE = 232, 50
V_BULL, P_BULL = 339, 25
G_IMPL   = 36.0            # con prima (vs precio de referencia del modelo, ~US$477)
G_IMPL_SIN_PRIMA = 26.3
G_GUIA   = 25.0            # guidance de management, 5 años, elevado de ~20% a ~25%
G_CAGR   = 22.0            # CAGR histórico 5-10 años aprox.
G_CONS   = 13.0
DCF_CLASE = "HEROICAS"     # en ambos escenarios de WACC — con prima excede guidance por 11pp,
                           # sin prima lo excede por solo 1,3pp (caso límite, pero igual HEROICAS)
# Zonas (tier Alta Convicción: MoS 25% + candado de expectativas activado por HEROICAS → +10pp = 35%,
# y exige zona Ganga específicamente, no solo Oportunidad)
Z_GANGA  = round(PWFV * 0.70, 0)    # 165
Z_OPORT  = round(PWFV * 0.85, 0)    # 201
Z_JUSTO  = round(PWFV * 1.10, 0)    # 260
Z_CARO   = round(PWFV * 1.35, 0)    # 319
MOS_ACTUAL = round((PWFV - PRECIO) / PWFV * 100, 1)   # muy negativo
ZONA_HOY = "BURBUJA"        # 187% del PWFV con prima (o 123%, Caro, sin prima)
VEREDICTO = "VIGILAR"       # confirmado por verificador — el detector PASA limpio y hay gatillos
                             # cuantificados y activos, a diferencia de ESPERAR (pasivo, sin catalizador)
GATE_TIER = ("Alta Convicción exige MoS 25% + techo 30x, satélite únicamente. El candado de "
             "expectativas (activado por clasificación HEROICAS) sube el MoS a 35% y exige zona Ganga "
             "específicamente. TSM está en BURBUJA con MoS profundamente negativo — no se cumple bajo ninguna lectura.")
TECHO_MULT_TIER = 30        # x owner earnings — techo del tier Alta Convicción
MULT_NORMALIZADO = 73.8     # x owner earnings FY25 trailing (recalculado a precio IBKR 442,35)
MULT_FY26E = 52.4           # x owner earnings FY26E estimado (recalculado a precio IBKR)
MULT_PS = 18.9               # contraste diagnóstico (valoracion.md "distorsión por capex de
                              # crecimiento"): MKTCAP/REVENUE_USD[FY25] = 2294/121.42. No levanta
                              # el candado duro (ancla en owner earnings) — solo documenta que
                              # incluso en P/S el nivel es rico (no barato), consistente con VIGILAR.
PRECIO_EPV = round(PRECIO / EPV, 1)   # ~9,0x (con OE FY25); ~6,4x con OE FY26E
GATILLO_OPORT = 201
GATILLO_GANGA = 165
ASIMETRIA = None             # no aplica en el mismo sentido que MELI: aquí el detector PASA limpio;
                              # el freno es 100% de precio (candado duro + gate de expectativas)

# ── Sensibilidad WACC × g terminal (con prima geopolítica) ───────────────
WACC_GRID = [10.19, 11.19, 12.19, 13.19, 14.19]
GT_GRID   = [3.0, 3.5, 4.0, 4.5, 5.0]
SENS = [
    [285, 305, 328, 354, 384],
    [252, 268, 286, 306, 329],
    [225, 236, 249, 264, 281],   # fila WACC 12,19 · col g 4,0 = 249 ≈ base ligeramente arriba de 236
    [202, 210, 220, 232, 245],
    [183, 190, 198, 207, 217],
]
SENS_MAX = 384

# ── WACC construcción ────────────────────────────────────────────────────
RF   = 4.3
ERP  = 4.8
BETA = 1.15
COE_CAPM = round(RF + BETA * ERP, 2)   # ~9,82 (costo de equity sin prima)
PRIMA_GEOPOLITICA = 2.5      # pp, punto medio de rango defendible 150-400pb

# ── Cross-check ROIC incremental (verificación adversarial, 10-jul-2026) ────
# Método: ΔOpInc / ΔBase de capital sobre varias ventanas 2021-2025. Fuente:
# stockanalysis.com (balance sheet + income statement TSM, FY2021-FY2025),
# verificado dato-a-dato en vivo — coincide al millón de NT$ con el Form 20-F.
# No mueve PWFV ni ninguna otra cifra de valoración; es un cross-check de
# apoyo a R7 (Capital/ROIC) y a la lectura cualitativa "capex de IA con
# historial probado" citada en §9.
# CAVEAT 1 (comparabilidad con AWS): el mismo ejercicio hecho para AWS usa
# activos DEL SEGMENTO (Amazon reporta por segmento) sobre una ventana de 1
# año (FY25 vs FY24). TSM no reporta segmentos — aquí se usan activos DE TODA
# LA COMPAÑÍA (mezcla nodos de punta con nodos maduros) sobre ventanas de
# 1-5 años. Misma FORMA (ΔOpInc/ΔCapital), base de comparación distinta.
# CAVEAT 2 (sesgo no declarado en versiones previas): el método de dos puntos
# asume que el retorno de la base de capital VIEJA se mantuvo constante y
# atribuye TODO el aumento de utilidad operativa al capital NUEVO — puede
# inflar la cifra si parte de la expansión de margen (42,6%→58,1% op. margin,
# 2023→Q1'26) viene de poder de fijación de precios sobre fabs ya existentes
# antes de 2021, no solo de capex marginal reciente. Dirección ambigua.
ROIC_INCR_CENTRAL     = 30.6   # ventana 2021→2025 (caso central, "ciclo completo") — ΔOpInc/ΔActivos
ROIC_INCR_RECIENTE    = 42.3   # ventana 2023→2025 (más favorable de las 5 ventanas probadas)
ROIC_INCR_MINIMO      = 15.0   # ventana 2021→2023 (la más débil probada) — aun así > WACC (9,72-12,19%)
ROIC_INCR_AWS_EQUIV   = 49.5   # ventana 2024→2025 (único año), réplica exacta del método usado en AWS
ROIC_INCR_AWS_EQUIV_PPE = 133.3  # misma ventana 2024→2025, pero ΔOpInc/ΔPP&E neto (aún más favorable)
ROIC_INCR_NEG_2022_23 = -54.0  # único año negativo de la serie 2021-2025, reportado sin ocultarlo
ROIC_INCR_FUENTE = ("stockanalysis.com, balance sheet + income statement TSM FY2021-FY2025, "
                     "verificado en vivo 10-jul-2026 — coincide exacto con Form 20-F")

# ── Probabilidades geopolíticas — horizonte largo, verificadas en vivo ──────
# Uso: ancla conceptual de la prima PERMANENTE de WACC (compensa un riesgo a
# perpetuidad, no un evento de 6-12 meses). Se elige deliberadamente NO usar
# el spot de corto plazo de mercados de eventos (Polymarket) como insumo de
# este ajuste estructural — más ruidoso y de horizonte equivocado para lo que
# el WACC está modelando.
PROB_INVASION_2027 = 22.0   # % acumulado a 2027 (Metaculus/Manifold, verificado en vivo 10-jul-2026)
PROB_INVASION_2030 = 37.0   # % acumulado a 2030 (Metaculus/Manifold, verificado en vivo 10-jul-2026)
PROB_FUENTE = "Metaculus/Manifold, verificado en vivo 10-jul-2026"

# ── Serie financiera anual (NT$M salvo indicado) · FY cierra 31-dic ──────
YRS_FIN = ["2023", "2024", "2025", "Q1'26"]
REVENUE_NTD = [2161736, 2894308, 3809054, 1134103]
REVENUE_USD = [79.85, 90.03, 121.42, 35.90]   # US$B aprox.
GROSS_MGN = [54.4, 56.1, 59.9, 66.2]
OP_MGN  = [42.6, 45.7, 50.8, 58.1]
NET_MGN = [39.4, 40.0, 44.6, 50.5]
ROE_MGMT = [None, None, 32.7, 40.5]   # % anualizado, Q1'25 y Q1'26
CFO_NTD   = [1241967, 1826177, 2274976, None]
CAPEX_NTD = [949817, 956007, 1272411, None]
CAPEX_SALES = [43.9, 33.0, 33.4, None]
FCF_NTD   = [292150, 870171, 1002565, None]
CAPEX_2026E_USD = 54   # midpoint 52-56B guidance

# ── Revenue por nodo tecnológico (% de ingreso de obleas) ────────────────
NODO_YRS = ["2023", "2024", "2025", "Q1'26"]
NODO_3NM = [6, 18, 24, 25]
NODO_5NM = [33, 34, 36, 36]
NODO_7NM = [19, 17, 14, 13]
AVANZADO_7NM_MENOS = [58, 69, 74, None]

# ── Revenue por plataforma (%) ────────────────────────────────────────────
PLAT_YRS = ["2023", "2024", "2025", "Q1'26"]
PLAT_HPC = [43, 51, 58, 61]
PLAT_SMARTPHONE = [38, 35, 29, 26]

# ── Concentración de clientes ─────────────────────────────────────────────
TOP10_PCT = [70, 76, 78]      # FY23,24,25
TOP10_YRS = ["2023", "2024", "2025"]
CLIENTE1_PCT = [25, 22, 19]   # mayor cliente, declinante (Apple, no confirmado por nombre en 20-F)
CLIENTE2_PCT = [11, 12, 17]   # segundo cliente, creciendo (Nvidia, no confirmado por nombre en 20-F)

# ── CoWoS / capacidad avanzada (estimados externos, no divulgados en 20-F) ─
COWOS_2024 = 35    # k wafers/mes
COWOS_2026E = 130
COWOS_2027E = 170

# ── Múltiplos ─────────────────────────────────────────────────────────────
PE_TRAILING = 30.5
PE_FORWARD = 23.5
EV_EBITDA = 22.0
EV_EBITDA_MEDIANA_10A = 10.05
CONSENSO_PT = 490
CONSENSO_RATING = "Strong Buy (con dispersión, ver notas)"

# ── Porter (score 1-5, menor = mejor foso) ────────────────────────────────
PORTER_FUERZAS = [
    ("Amenaza de nuevos entrantes", 1),
    ("Sustitutos (ASICs vs GPU — neutro/positivo para TSM)", 2),
    ("Rivalidad (Samsung, Intel Foundry)", 2),
    ("Poder de clientes (concentrado pero cautivo)", 2),
    ("Poder de proveedores (ASML, monopolio EUV)", 4),
]
PORTER_POND = 2.2

# ── TAM (US$B, 2026) ──────────────────────────────────────────────────────
MERCADOS = [
    ("Foundry global", 190, 121, "~72% cuota"),
    ("Foundry de punta (&lt;5nm)", 90, 85, "&gt;92% cuota proy."),
    ("Empaquetado avanzado (CoWoS)", 40, 20, "cuello de botella IA"),
]

# ── Management (6 dimensiones, /5) → total /30 ───────────────────────────
MGMT = [
    ("Track record de ejecución (C.C. Wei)", 4.5),
    ("Independencia (Presidente+CEO combinado)", 2.5),
    ("Compensación ejecutiva", 3.5),
    ("Instrumentalidad geopolítica (Taiwán/EEUU)", 2.0),
    ("Disciplina de capital (capex guiado, no especulativo)", 4.0),
    ("Transparencia / respuesta accionista", 3.5),
]
MGMT_TOTAL = 20.0

TAIWAN_GOB_STAKE = 6.38   # % del Fondo Nacional de Desarrollo de Taiwán
INST_EXTRANJERA_PCT = 74

# ── Riesgos (nombre, prob 1-5, impacto 1-5) ──────────────────────────────
RIESGOS = [
    ("Bloqueo/cuarentena de Taiwán (no invasión)", 2, 5),
    ("Confiabilidad del respaldo militar de EEUU en duda", 2, 4),
    ("Concentración de clientes (2 clientes &gt;15%, convergiendo)", 4, 3),
    ("Dependencia de proveedor único (ASML, monopolio EUV)", 2, 3),
    ("Valoración estirada (EV/EBITDA 124% sobre mediana 10a)", 4, 4),
    ("Samsung/Intel cerrando brecha de proceso (Tesla AI6)", 2, 2),
]

# ── Nueve inversores ─────────────────────────────────────────────────────
INVERSORES = [
    ("Graham",       3, "PASS"),
    ("Buffett",      4, "PASS"),
    ("Munger",       5, "HOLD"),
    ("Fisher",       6, "HOLD"),
    ("Lynch",        5, "PASS"),
    ("Templeton",    3, "PASS"),
    ("Marks",        4, "HOLD"),
    ("Seilern",      6, "HOLD"),
    ("Terry Smith",  5, "HOLD"),
]

if __name__ == "__main__":
    print("TSM data OK ·", SCORE_QG, TIER_QG, "· val-mos", VEREDICTO,
          "· PWFV", PWFV, "· zona", ZONA_HOY)
    tot = sum(p for _, p, _ in REGLAS)
    print("check raw:", tot, "→", round(tot/125*100, 1))
    print("check mult FY25:", round(MKTCAP/31.1, 1), "check mult FY26E:", round(MKTCAP/43.8, 1))
    print("check ROIC incremental: central", ROIC_INCR_CENTRAL, "· reciente", ROIC_INCR_RECIENTE,
          "· mínimo", ROIC_INCR_MINIMO, "· equiv-AWS(activos)", ROIC_INCR_AWS_EQUIV,
          "· todas > WACC", WACC_SIN_PRIMA, "/", WACC)
    print("check prob. geopolítica (horizonte largo):", PROB_INVASION_2027, "% a 2027 ·",
          PROB_INVASION_2030, "% a 2030")
