# -*- coding: utf-8 -*-
"""Validador de consistencia para dcf_<tick>.py — correr ANTES de dar por cerrada
cualquier Tesis Ultra (nueva o refresh trimestral). No recalcula la tesis: solo
verifica que la aritmética interna del archivo fuente sea consistente consigo misma.

Uso:
    python3 validador_tesis.py /ruta/a/dcf_tick.py [/ruta/a/otro/dcf_tick2.py ...]

Historial: nace 8-jul-2026 tras encontrar en auditoría (a) un bug de escala R1/R3/R4
recurrente (SPOT/VEEV/ORCL) que ya se corrigió a mano 3 veces sin un chequeo
automático, y (b) un campo ASIMETRIA con signo invertido en MELI y ausente en
6/17 tesis pese a ser "filtro final" obligatorio de val-mos. Ver memoria
`feedback-loop-valoraciones.md`.
"""
import re
import sys

def grab_scalar(src, name):
    m = re.search(rf'^{name}\s*=\s*([\-\d.]+)\s*(#.*)?$', src, re.M)
    if m:
        return float(m.group(1))
    m = re.search(rf'^{name}\s*,\s*\w+\s*=\s*([\-\d.]+)\s*,', src, re.M)
    if m:
        return float(m.group(1))
    return None

def grab_reglas(src):
    m = re.search(r'REGLAS\s*=\s*\[(.*?)\n\]', src, re.S)
    if not m:
        return None
    tuples = re.findall(r'\("([^"]+)"\s*,\s*([\d.]+)\s*,\s*([\d.]+)\)', m.group(1))
    return [(n, float(p), float(w)) for n, p, w in tuples]

def validate(path):
    with open(path, encoding="utf-8") as f:
        src = f.read()
    problems, warnings = [], []

    # 1 — cada regla no puede superar su propio peso (bug de escala R1/R3/R4)
    reglas = grab_reglas(src)
    raw_qg = grab_scalar(src, "RAW_QG")
    score_qg = grab_scalar(src, "SCORE_QG")
    if reglas:
        suma = 0.0
        for nombre, pts, peso in reglas:
            suma += pts
            if pts > peso + 1e-6:
                problems.append(f"{nombre}: puntos {pts} > peso {peso} (bug de escala)")
        if raw_qg is not None and abs(suma - raw_qg) > 0.05:
            problems.append(f"suma de REGLAS ({suma}) != RAW_QG declarado ({raw_qg})")
        if raw_qg is not None and score_qg is not None:
            esperado = round(raw_qg / 125 * 100, 1)
            if abs(esperado - score_qg) > 0.15:
                problems.append(f"SCORE_QG={score_qg} pero RAW_QG/125*100={esperado}")
    else:
        warnings.append("no se encontró REGLAS — revisar a mano el eje CALIDAD")

    # 2 — asimetría: recomputar con la fórmula canónica val-mos
    #     Asimetría = (V_BASE−PRECIO)/PRECIO ÷ (PRECIO−V_BEAR)/PRECIO
    #     (mos_sizing.md §"Filtro final")
    precio = grab_scalar(src, "PRECIO")
    v_base = grab_scalar(src, "V_BASE")
    v_bear = grab_scalar(src, "V_BEAR")
    asim = grab_scalar(src, "ASIMETRIA")
    if precio is not None and v_base is not None and v_bear is not None and precio != v_bear:
        recomputada = (v_base - precio) / (precio - v_bear)
        if asim is None:
            warnings.append(
                f"ASIMETRIA no está poblada; con V_BASE/V_BEAR propios sería {recomputada:.2f}:1 "
                f"— campo obligatorio de val-mos ('filtro final'), completar aunque el verdicto no cambie"
            )
        elif abs(recomputada) > 1e-6 and abs((asim - recomputada) / recomputada) > 0.15:
            problems.append(
                f"ASIMETRIA declarada={asim} pero (V_BASE,V_BEAR,PRECIO) propios dan {recomputada:.2f} "
                f"(revisar signo/fórmula)"
            )
    elif asim is None:
        warnings.append("ASIMETRIA no está poblada y no hay V_BASE/V_BEAR para recomputarla")

    # 2b — casos degenerados de asimetría (val-mos v4, mos_sizing.md §"Filtro final")
    if precio is not None and v_base is not None and precio > v_base + 1e-6 and asim is not None and asim > 0:
        problems.append(
            f"ASIMETRIA declarada positiva ({asim}) pero PRECIO ({precio}) > V_BASE ({v_base}): "
            f"no hay upside al base, la asimetría debe ser <=0 (revisar signo — bug tipo MELI)"
        )
    if precio is not None and v_bear is not None and precio < v_bear - 1e-6:
        warnings.append(
            f"PRECIO ({precio}) < V_BEAR ({v_bear}): la fórmula de asimetría DEGENERA — no reportar el "
            f"ratio crudo, re-correr detector de trampas (bug tipo WKL). Marcar ASIMETRIA no-aplicable con nota."
        )

    # 2c — el PWFV no puede implicar un múltiplo > techo del tier (val-mos v4, "bug de Visa")
    #   PWFV_implícito_múltiplo = MULT_NORMALIZADO (múltiplo del precio) × (PWFV / PRECIO)
    #   Si el propio valor justo asume pagar por encima del techo, el mapa de zonas queda corrido.
    mult_norm = grab_scalar(src, "MULT_NORMALIZADO")
    techo = grab_scalar(src, "TECHO_MULT_TIER")
    pwfv = grab_scalar(src, "PWFV")
    #   OJO (v4, corregido tras el falso positivo de GOOGL): esto es un WARNING, no un FAIL.
    #   Un múltiplo de PWFV alto tiene DOS causas posibles y la regla ciega no las distingue:
    #     (a) PWFV genuinamente inflado sobre owner earnings LIMPIO (Visa/MA — peaje sin capex) → error real;
    #     (b) owner earnings DEPRIMIDO por capex de crecimiento (GOOGL/TSM — capex-intensivo) → artefacto, NO
    #         sobrevaloración; el múltiplo alto es del denominador chico, no del precio.
    #   Solo el router de arquetipo (arquetipos.md) decide cuál es. Aquí se marca para investigar, no se condena.
    if (mult_norm is not None and techo is not None and techo > 0
            and pwfv is not None and precio is not None and precio > 0):
        mult_pwfv = mult_norm * (pwfv / precio)
        if mult_pwfv > techo * 1.05:
            warnings.append(
                f"PWFV implica múltiplo {mult_pwfv:.1f}x > techo del tier {techo:.0f}x "
                f"(MULT_NORMALIZADO {mult_norm:.1f}x × PWFV/PRECIO {pwfv/precio:.2f}). INVESTIGAR el arquetipo: "
                f"si es peaje/asset-light con owner earnings limpio → PWFV inflado real (tipo Visa); si es "
                f"capex-intensivo con owner earnings deprimido → probable ARTEFACTO de capex, NO burbuja (tipo GOOGL/TSM)."
            )

    # 3 — vocabulario canónico cerrado (val-mos v4, output.md §enums)
    ENUMS = {
        "DETECTOR": {"PASA", "GRIS", "TRAMPA"},
        "ZONA_HOY": {"Ganga", "Oportunidad", "Justo", "Caro", "Burbuja"},
        "VEREDICTO": {"COMPRAR TRAMO", "ACUMULAR EN ZONA", "VIGILAR", "ESPERAR", "VETO-TRAMPA"},
    }
    for campo, permitidos in ENUMS.items():
        m = re.search(rf'^{campo}\s*=\s*"([^"]+)"', src, re.M)
        if m:
            val = m.group(1).strip().upper()
            # pasa si es exactamente un token canónico, o empieza con uno seguido de
            # separador (permite sufijos enfáticos legítimos: "ESPERAR — NO COMPRAR")
            ok = any(
                val == p.upper() or val.startswith(p.upper() + " ")
                for p in permitidos
            )
            if not ok:
                problems.append(
                    f"{campo}=\"{m.group(1).strip()}\" fuera del enum canónico de val-mos v4 "
                    f"(permitidos: {', '.join(sorted(permitidos))})"
                )

    return problems, warnings

def main(paths):
    any_problem = False
    for path in paths:
        problems, warnings = validate(path)
        tick = path.split("/")[-1]
        if not problems and not warnings:
            print(f"OK   {tick}")
            continue
        for p in problems:
            any_problem = True
            print(f"FAIL {tick}: {p}")
        for w in warnings:
            print(f"WARN {tick}: {w}")
    sys.exit(1 if any_problem else 0)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    main(sys.argv[1:])
