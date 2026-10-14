# -*- coding: utf-8 -*-
"""
score_v2.py — Convierte los scores de la sesion anterior (/13.5) al nuevo
sistema qg-seilern /100 con 11 reglas (R11 = criterio de impacto de Felipe).

Reglas del nuevo sistema:
- R1, R3, R4: criticas, max 15 cada una
- R2, R5, R6, R7, R8, R9, R10, R11: estandar, max 10 cada una
- Total max raw = 3*15 + 8*10 = 45 + 80 = 125
- Score final = (raw_sum / 125) * 100
- Tiers: Nucleo >=85, Alta conviccion 75-84, Calidad solida 65-74, Watchlist <65

Conversion desde sistema antiguo (/2.0 para criticas, /2.0 para estandares):
- Criticas (R1,R3,R4): new = (old/2.0)*15
- Estandares (R2,R5,R6,R7,R8,R9,R10): new = (old/2.0)*10
- R11: asignado manualmente segun criterio de impacto
"""
import os, json, glob

BASE = "/Users/felipealvarez/Library/Mobile Documents/com~apple~CloudDocs/INVESTMENTS"
DATA = BASE + "/_ACTIVE/qg_ranking/data/companies"
OUT = BASE + "/_ACTIVE/qg_ranking/data"

# ---------------------------------------------------------------------------
# R11 ASIGNACIONES — Criterio de impacto estructural (0-10)
# NIVEL 1 Knock-out (R11 = -99): daño activo, core, intencional, inseparable
# NIVEL 2 Neutral (0-3): legitimo pero sin impacto estructural
# NIVEL 3 Impacto (4-10): salud, inclusion, infraestructura, ciencia, productividad
# ---------------------------------------------------------------------------
R11_MAP = {
    # Infraestructura de pagos / inclusion financiera
    "V":        8,  # 2B+ tarjetahabientes, acceso financiero global
    "MA":       8,  # Idem Visa, inclusión en mercados emergentes
    "ADYEN.AS": 8,  # Pagos SMB, inclusion financiera digital
    "FICO":     7,  # Credit scoring -> acceso al credito para millones

    # Infraestructura de mercados de capitales
    "SPGI":     7,  # Ratings + indices -> financia la economia global
    "MCO":      7,  # Idem Moody's
    "MSCI":     7,  # Indices -> asignacion de capital global
    "CME":      7,  # Price discovery commodities -> precios de alimentos/energia
    "CBOE":     7,  # Gestion de riesgo via opciones
    "FDS":      7,  # Data para asignacion de capital
    "VRSK":     7,  # Risk analytics -> seguro -> proteccion financiera
    "IBKR":     7,  # Democratiza la inversion, acceso barato a mercados

    # Software empresarial / productividad
    "MSFT":     8,  # Enterprise + AI research, empodera millones de negocios
    "GOOGL":    6,  # Acceso a info (pero modelo publicidad complica R11)
    "ADBE":     6,  # Herramientas creativas empoderan creadores globales
    "NOW":      6,  # Eficiencia workflows empresariales
    "INTU":     7,  # Empodera pymes y declaraciones fiscales de millones
    "VEEV":     8,  # Habilita desarrollo de farmacos, ensayos clinicos
    "WKL.AS":   8,  # Infraestructura de conocimiento legal/salud/fiscal
    "IT":       5,  # Decisiones tecnologicas empresariales
    "ACN":      5,  # Consultoria de eficiencia empresarial
    "REL.L":    8,  # Publicacion cientifica + analitica juridica + riesgos
    "CDNS":     8,  # EDA: habilita el diseno de chips -> toda tecnologia digital
    "APP":      3,  # Monetizacion de apps, sin impacto estructural positivo
    "PGHN.SW":  4,  # Acceso a mercados privados, principalmente para sofisticados
    "EQT.ST":   4,  # Private equity, impacto via portfolio
    "BX":       4,  # Gestion alternativa de activos

    # Salud y ciencias de la vida
    "ISRG":    10,  # Cirugia minimo-invasiva, 20M+ pacientes, salva vidas
    "RMD":     10,  # Terapia apnea del sueno para millones, calidad de vida
    "VRTX":    10,  # Terapia genica FC, cura enfermedades raras
    "LLY":     10,  # Farmacos que salvan vidas (GLP-1, cancer, Alzheimer)
    "EW":       9,  # Valvulas cardiacas TAVR, procedimientos cardiacos que salvan vidas
    "IDXX":     9,  # Diagnostico veterinario -> seguridad alimentaria + salud animal
    "7741.T":   9,  # Lentes intraoculares (cirugia cataratas), optica ciencias de la vida
    "MTD":      8,  # Instrumentos cientificos -> I+D farmaceutico, produccion
    "WST":      8,  # Sistemas de entrega de farmacos -> seguridad de todos los injectables
    "LIN":      8,  # Oxigeno para hospitales, produccion alimentos, investigacion

    # Semiconductores / infraestructura tecnologica
    "ASML":     9,  # Habilita toda manufactura avanzada de chips -> civilizacion digital
    "TSM":      9,  # Fabrica 90%+ de chips avanzados del mundo
    "ASM.AS":   9,  # Epitaxia semiconductores -> chips avanzados
    "6920.T":   9,  # Inspeccion mascaras EUV -> manufactura critica de chips
    "NVDA":     8,  # IA + computacion cientifica + imagenes medicas
    "AVGO":     7,  # Semiconductores infraestructura para redes/AI data centers
    "TXN":      7,  # Semis embebidos para industrial/automocion/medico
    "KLAC":     8,  # Control de procesos semiconductores -> calidad de chips
    "LRCX":     8,  # Deposicion semiconductores -> avance tecnologico
    "6857.T":   8,  # Test de semiconductores -> garantia de calidad
    "VACN.SW":  8,  # Valvulas de vacio para manufactura semiconductores
    "8035.T":   8,  # Equipos semiconductores (ALD, recubridores)
    "6146.T":   8,  # Corte/molienda semiconductores
    "6861.T":   7,  # Sensores de automatizacion -> eficiencia manufacturera
    "ANET":     7,  # Redes data centers IA/cloud -> infraestructura digital
    "FTNT":     7,  # Ciberseguridad -> protege infraestructura critica
    "AAPL":     6,  # Acceso a computacion personal (precio limita alcance)
    "ATCO-B.ST": 5, # Maquinaria industrial para productividad
    "6273.T":   5,  # Automatizacion neumatica, eficiencia manufacturera
    "EPI-A.ST": 5,  # Equipos de mineria

    # Entretenimiento / lujo / consumo
    "NFLX":     3,  # Entretenimiento, algo de acceso cultural
    "7974.T":   3,  # Entretenimiento/alegria, no impacto estructural
    "BKNG":     4,  # Acceso al viaje, algo de democratizacion
    "COST":     6,  # Bienes asequibles para clase media, democratiza poder adquisitivo
    "ADP":      6,  # Garantiza pago correcto de millones de trabajadores
    "MMC":      6,  # Gestion de riesgos habilita el comercio
    "CPRT":     5,  # Mercado coches de segunda mano -> asequibilidad + reduccion residuos
    "CTAS":     5,  # Seguridad laboral, servicios de uniformes
    "GRMN":     5,  # Navegacion, seguridad aviacion, salud
    "AME":      5,  # Electronica especializada para salud/defensa/industrial
    "ODFL":     4,  # Logistica de carga, cadena de suministro
    "RMS.PA":   2,  # Lujo puro Hermes, sin impacto estructural
    "MC.PA":    2,  # Lujo puro LVMH
    "RACE":     2,  # Lujo auto Ferrari
    "CFR.SW":   2,  # Lujo puro Richemont
    "OR.PA":    4,  # Democratizando algo la cosmetica, ciencia de la belleza
    "MNST":     1,  # Bebidas energeticas, asociaciones negativas a la salud
    "VRSN":     8,  # Infraestructura internet (.com/.net), sistema de dominios
    "TPL":      2,  # Royalties energeticos, adyacente a combustibles fosiles
    "PLTR":     4,  # Analytics (defensa/inteligencia dominante, controversial)
    "VRTX":    10,  # (ya definido arriba)
}

CRITICAL = {"R1", "R3", "R4"}

def tier(score):
    if score >= 85:
        return "Nucleo QG"
    elif score >= 75:
        return "Alta conviccion"
    elif score >= 65:
        return "Calidad solida"
    else:
        return "Watchlist"

def convert_company(score_file):
    with open(score_file) as f:
        d = json.load(f)

    ticker = d.get("ticker", "")
    rules = d.get("rules", {})
    new_scores = {}
    raw_sum = 0.0

    for rule_key, rule_data in rules.items():
        old_score = rule_data.get("score", 0)
        if rule_key in CRITICAL:
            max_old = 2.0
            max_new = 15.0
        else:
            max_old = 2.0  # en el sistema antiguo todas podian llegar a 2.0
            max_new = 10.0

        # Conversion lineal desde escala 0-2 a escala 0-max_new
        new_s = round((old_score / max_old) * max_new, 1)
        new_s = min(new_s, max_new)  # cap
        new_scores[rule_key] = {
            "old": old_score,
            "new": new_s,
            "max": max_new,
            "just": rule_data.get("just", "")
        }
        raw_sum += new_s

    # R11
    r11 = R11_MAP.get(ticker, 3)  # default 3 si no esta en el mapa
    new_scores["R11"] = {
        "old": None,
        "new": r11,
        "max": 10,
        "just": "Criterio de impacto estructural (Felipe, jul-2026)"
    }
    raw_sum += r11

    score_100 = round((raw_sum / 125.0) * 100, 1)

    return {
        "ticker": ticker,
        "name": d.get("name", ticker),
        "scores": new_scores,
        "raw_sum_new": round(raw_sum, 1),
        "score_100": score_100,
        "tier": tier(score_100),
        "amplification": d.get("amplification", False),
        "moat_type": d.get("moat_type", ""),
        "moat_one_line": d.get("moat_one_line", ""),
        "thesis_3lines": d.get("thesis_3lines", []),
        "bear_case": d.get("bear_case_strongest", ""),
        "sbc_flag": d.get("sbc_flag", "ok"),
        "ethical_flag": d.get("ethical_flag", "none"),
        "r11": r11
    }


def run():
    score_files = sorted(glob.glob(DATA + "/*_score.json"))
    results = []
    for sf in score_files:
        try:
            c = convert_company(sf)
            results.append(c)
        except Exception as e:
            print(f"  ERROR {sf}: {e}")

    # Sort by score_100 descending
    results.sort(key=lambda x: x["score_100"], reverse=True)

    out_path = OUT + "/new_quality_v2.json"
    with open(out_path, "w") as f:
        json.dump({"system": "qg-seilern v2 /100", "date": "2026-07-04", "companies": results}, f,
                  ensure_ascii=False, indent=1)

    print(f"\nNEW QUALITY SCORES v2 ({len(results)} empresas):")
    print(f"{'#':<4} {'Ticker':<12} {'Score':>6} {'Tier':<20}")
    print("-" * 46)
    for i, c in enumerate(results, 1):
        mark = ""
        if c.get("ethical_flag") == "dagger":
            mark = " ‡"
        print(f"{i:<4} {c['ticker']:<12} {c['score_100']:>6.1f} {c['tier']:<20}{mark}")

    print(f"\nOutput: {out_path}")

    # Tier summary
    from collections import Counter
    tier_counts = Counter(c["tier"] for c in results)
    print("\nTier breakdown:")
    for t in ["Nucleo QG", "Alta conviccion", "Calidad solida", "Watchlist"]:
        print(f"  {t}: {tier_counts.get(t, 0)}")

    return results

if __name__ == "__main__":
    run()
