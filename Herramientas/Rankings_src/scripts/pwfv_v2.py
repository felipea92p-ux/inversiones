# -*- coding: utf-8 -*-
"""
pwfv_v2.py — PWFV-Valor v2 (val-mos skill, 2-jul-2026)
Recalcula valor intrinseco para las 77 empresas bajo la nueva metodologia.

Metodo por ARQUETIPO:
A) Compounder estable: DCF 50% + FCF-yield 25% + Multiplo 25%
B) Cíclico/semi: DCF normalizado mid-cycle 50% + Multiplo 50%

WACC escalado por tier QG:
- Nucleo (>=85):     WACC = 7.5%
- Alta conviccion:   WACC = 8.5%
- Calidad solida:    WACC = 9.5%

Escalera MoS:
- Nucleo: MoS >= 15% para comprar
- Alta conviccion: MoS >= 25% para comprar
- Calidad solida: MoS >= 35% para comprar
- Watchlist: NO comprar
"""
import os, json, glob, math

BASE = "/Users/felipealvarez/Library/Mobile Documents/com~apple~CloudDocs/INVESTMENTS"
DATA = BASE + "/_ACTIVE/qg_ranking/data"
COMPANIES_DIR = DATA + "/companies"

# WACC por tier
WACC_TIER = {
    "Nucleo QG":       7.5,
    "Alta conviccion": 8.5,
    "Calidad solida":  9.5,
    "Watchlist":       11.0,  # no se valora para compra
}

# Umbral MoS minimo para comprar (%)
MOS_MIN = {
    "Nucleo QG":       15.0,
    "Alta conviccion": 25.0,
    "Calidad solida":  35.0,
    "Watchlist":       999.0,  # nunca
}

# Techo de multiplo owner earnings (P/OE)
MULT_TECHO = {
    "Nucleo QG":       35.0,
    "Alta conviccion": 30.0,
    "Calidad solida":  25.0,
    "Watchlist":       20.0,
}

# Arquetipo: semi / ciclico usan earnings normalizados
SEMIS = {"NVDA","TSM","ASML","AVGO","TXN","ASM.AS","KLAC","LRCX",
         "6920.T","6857.T","VACN.SW","8035.T","6146.T","6861.T","ATCO-B.ST"}

TERMINAL_G = 3.0  # % terminal growth (max)

def wacc_reduction_factor(old_wacc_pct, new_wacc_pct, g_pct=TERMINAL_G):
    """
    Escala el IV del DCF ante un cambio de WACC.
    Basado en: V ~ FCF / (WACC - g), por tanto V_new/V_old ~ (WACC_old - g) / (WACC_new - g)
    """
    denom_old = old_wacc_pct - g_pct
    denom_new = new_wacc_pct - g_pct
    if denom_new <= 0 or denom_old <= 0:
        return 1.0  # no escalar si denominador invalido
    factor = denom_old / denom_new
    # Cap el factor para evitar extrapolaciones salvajes
    return min(max(factor, 0.5), 3.0)


def fcf_yield_value(fcf_ps, new_wacc_pct, sustainable_growth_pct, iv_dcf_new):
    """
    Valor FCF-yield (Terry Smith / val-mos v2):
    Precio donde [FCF_yield + FCF_growth] = required_return = WACC_tier + 1.5pp
    => price = FCF / (required_return - sustainable_growth)

    Correcciones anti-blow-up:
    - gap minimo 2pp (si sustainable_growth muy cerca de required_return)
    - cap at 2.5x iv_dcf_new (evitar extrapolar en compounders de muy alto crecimiento)
    """
    required_return = new_wacc_pct + 1.5  # pp extra para calidad
    gap = required_return - sustainable_growth_pct
    # Anti-blow-up: si gap < 2pp, el metodo FCF-yield no aplica confiablemente
    if gap < 2.0:
        return None  # indica "metodo no aplica"
    raw = fcf_ps / (gap / 100.0)
    # Cap: FCF-yield no puede dar mas de 2.5x el DCF (evitar extrapolaciones)
    cap = iv_dcf_new * 2.5
    return min(raw, cap)


def label_mos(mos_pct, tier):
    if tier == "Watchlist":
        return "NO COMPRABLE"
    min_mos = MOS_MIN[tier]
    if mos_pct >= 25:
        return "GANGA FUERTE"
    elif mos_pct >= 15:
        return "OPORTUNIDAD"
    elif mos_pct >= -15:
        return "PRECIO JUSTO"
    elif mos_pct >= -35:
        return "CARO"
    else:
        return "BURBUJA"


def run():
    # Cargar scores v2
    with open(DATA + "/new_quality_v2.json") as f:
        quality_data = json.load(f)
    quality_map = {c["ticker"]: c for c in quality_data["companies"]}

    # Cargar merged (todos los datos financieros y IVs previos)
    with open(DATA + "/fase4v2_merged.json") as f:
        merged_data = json.load(f)
    merged_map = {c["ticker"]: c for c in merged_data["companies"]}

    results = []

    for ticker, m in merged_map.items():
        q = quality_map.get(ticker)
        if q is None:
            print(f"  SKIP {ticker}: no hay score v2")
            continue

        tier = q["tier"]
        score_100 = q["score_100"]
        new_wacc = WACC_TIER[tier]
        old_wacc = m.get("wacc", new_wacc)  # WACC del sistema anterior

        price = m.get("price", 0)
        iv_dcf_old = m.get("iv_dcf", 0)
        iv_mult_old = m.get("iv_mult", 0)

        # --- PASO 1: Escalar iv_dcf con nuevo WACC ---
        wacc_factor = wacc_reduction_factor(old_wacc, new_wacc, TERMINAL_G)
        iv_dcf_new = iv_dcf_old * wacc_factor

        # Para semis/ciclicos: adicionalmente aplicar normalizacion mid-cycle
        # El rango de expansion actual de los semis infla el DCF en pico
        # Si el P/E forward excede el percentil 75 historico -> PICO -> descontar 25%
        archetype = "compounder"
        if ticker in SEMIS:
            archetype = "ciclico"
            fwd_pe = m.get("fwd_pe", 0)
            fwd_pe_5y = m.get("fwd_pe_5y", fwd_pe)
            if fwd_pe_5y and fwd_pe > 0 and fwd_pe / fwd_pe_5y > 1.5:
                # P/E actual > 1.5x media historica = presumiblemente pico
                iv_dcf_new *= 0.7  # normalizacion mid-cycle (conservadora)
                archetype = "ciclico_pico"

        # --- PASO 2: FCF-yield value (solo compounders) ---
        # Intentar leer val.json para FCF/share y growth estimate
        val_path = COMPANIES_DIR + f"/{ticker}_val.json"
        iv_fcf_yield = None
        fcf_ps = 0
        sustainable_growth = 5.0  # default conservador

        if os.path.exists(val_path):
            try:
                with open(val_path) as f:
                    v = json.load(f)
                # Extraer FCF/share y growth del escenario base
                scenarios = v.get("dcf_scenarios", {})
                base = scenarios.get("base", {})
                iv_base_ps = base.get("iv_per_share", 0)
                # FCF/share aproximado: inferir del owner_fcf_base string
                # O usar: FCF_owner_total / shares
                # Simplificacion: usar iv_dcf_weighted / (1/(wacc-g)) como proxy
                old_wacc_v = v.get("wacc_pct", old_wacc)
                # FCF primer año estimado = iv_dcf_old * (old_wacc - g) / 100
                gap_old = (old_wacc_v - TERMINAL_G) / 100
                if gap_old > 0:
                    fcf_ps = iv_dcf_old * gap_old

                # Sustainable growth: tomar el 60% del growth del escenario base
                # (conservatismo de largo plazo vs. crecimiento actual)
                base_note = base.get("note", "")
                # Extraer el CAGR del escenario base (buscar el primer numero %)
                import re
                cagr_match = re.search(r"(\d+)% CAGR", base_note)
                if cagr_match:
                    phase1_cagr = float(cagr_match.group(1))
                    sustainable_growth = phase1_cagr * 0.5  # 50% del phase1 CAGR
                    sustainable_growth = min(sustainable_growth, 12.0)  # cap 12%

                if archetype == "compounder" and fcf_ps > 0:
                    iv_fcf_yield = fcf_yield_value(fcf_ps, new_wacc, sustainable_growth, iv_dcf_new)

            except Exception as e:
                pass

        # --- PASO 3: Multiplo (sin cambios del sistema anterior) ---
        # El multiplo justificado por calidad no cambia con WACC
        # Pero aplicar techo de multiplo por tier
        # Si el multiplo objetivo en el DCF inverso era "heroico", penalizar
        iv_mult_new = iv_mult_old  # sin cambio en el multiplo por ahora

        # --- PASO 4: PWFV-Valor (ponderado por arquetipo) ---
        if archetype in ("ciclico", "ciclico_pico"):
            # Para semis: 50% DCF normalizado + 50% multiplo
            pwfv = 0.50 * iv_dcf_new + 0.50 * iv_mult_new
        else:
            # Compounder estable: 50% DCF + 25% FCF-yield + 25% multiplo
            if iv_fcf_yield is not None and iv_fcf_yield > 0:
                pwfv = 0.50 * iv_dcf_new + 0.25 * iv_fcf_yield + 0.25 * iv_mult_new
            else:
                # FCF-yield no disponible o growth > required: sesgo al DCF
                pwfv = 0.55 * iv_dcf_new + 0.00 * 0 + 0.45 * iv_mult_new

        # --- PASO 5: MoS ---
        if price > 0:
            mos_pct = round((pwfv - price) / pwfv * 100, 1)
        else:
            mos_pct = 0.0

        # Cap display a -60% (evitar distorsion visual por precios de pico extremo)
        mos_disp = max(mos_pct, -60.0)

        # Determinar zona de oportunidad
        lbl = label_mos(mos_pct, tier)

        # Verificar si cumple MoS minimo para comprar
        min_mos = MOS_MIN[tier]
        comprable = mos_pct >= min_mos and tier != "Watchlist"

        results.append({
            "ticker": ticker,
            "name": m.get("name", ticker),
            "tier": tier,
            "score_100": score_100,
            "archetype": archetype,
            "price": price,
            "currency": m.get("currency", "USD"),
            "old_wacc": old_wacc,
            "new_wacc": new_wacc,
            "wacc_factor": round(wacc_factor, 3),
            "iv_dcf_old": round(iv_dcf_old, 2),
            "iv_dcf_new": round(iv_dcf_new, 2),
            "iv_mult": round(iv_mult_new, 2),
            "iv_fcf_yield": round(iv_fcf_yield, 2) if iv_fcf_yield else None,
            "pwfv": round(pwfv, 2),
            "mos_pct": mos_pct,
            "mos_disp": mos_disp,
            "min_mos_required": min_mos,
            "comprable": comprable,
            "label": lbl,
            "ethical_flag": m.get("ethical_flag", "none"),
            "sbc_flag": m.get("sbc_flag", "ok"),
        })

    # Ordenar por MoS descendente
    results.sort(key=lambda x: x["mos_pct"], reverse=True)

    out_path = DATA + "/new_mos_v2.json"
    with open(out_path, "w") as f:
        json.dump({"method": "PWFV-Valor v2 / val-mos skill", "date": "2026-07-04",
                   "companies": results}, f, ensure_ascii=False, indent=1)

    print(f"\nPWFV-VALOR v2 ({len(results)} empresas) — Ordenadas por MoS:")
    print(f"{'#':<4} {'Ticker':<12} {'Tier':<20} {'Score':>6} {'OldWACC':>8} {'NewWACC':>8} {'PWFV':>10} {'MoS%':>7} {'Comprable':>10}")
    print("-" * 100)
    for i, c in enumerate(results, 1):
        mark = "‡" if c.get("ethical_flag") == "dagger" else " "
        comp = "SI" if c["comprable"] else "-"
        pwfv_str = f"{c['pwfv']:>10,.1f}"
        print(f"{i:<4} {c['ticker']:<12} {c['tier']:<20} {c['score_100']:>6.1f} "
              f"{c['old_wacc']:>8.1f}% {c['new_wacc']:>7.1f}% {pwfv_str} "
              f"{c['mos_pct']:>+7.1f}% {comp:>10}{mark}")

    print(f"\nOutput: {out_path}")

    # Resumen de comprables
    comprables = [c for c in results if c["comprable"]]
    print(f"\nEmpresas COMPRABLES ({len(comprables)}):")
    for c in comprables:
        print(f"  {c['ticker']:<12} {c['tier']:<20} MoS {c['mos_pct']:+.1f}%  {c['label']}")

    return results


if __name__ == "__main__":
    run()
