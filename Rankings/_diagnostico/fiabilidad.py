#!/usr/bin/env python3
"""
fiabilidad.py — el termómetro permanente de Rabitt UQG.

Mide si una rúbrica de puntuación se pone de acuerdo CONSIGO MISMA. Es la primera pregunta que
hay que hacerle a cualquier sistema de scoring, antes de analizar pesos, colinealidad o validez:
la fiabilidad pone techo a la validez (techo = raíz cuadrada de la fiabilidad).

Uso:
    python3 fiabilidad.py                      # todos los registros de _score_records/
    python3 fiabilidad.py --dir _score_records
    python3 fiabilidad.py --a screening --b retest-ciego    # comparar dos procedencias

Línea base medida el 2026-07-19 sobre qg-seilern (65 tickers, screening vs re-verificado):
    rho test-retest = 0.51 · fiabilidad implícita ~0.19 · halo 43.7% · ablación >= 0.979
Objetivo de Rabitt UQG: rho >= 0.85 y correlación de errores entre reglas <= 0.30.
"""

import json, glob, argparse, math, os
from collections import defaultdict

try:
    import numpy as np
except ImportError:
    raise SystemExit("Hace falta numpy:  pip3 install numpy")

REGLAS = [f"R{i}" for i in range(1, 12)]
PESO = {"R1": 15, "R3": 15, "R4": 15}          # el resto vale 10
MAXTOT = sum(PESO.get(r, 10) for r in REGLAS)  # 115


def cargar(directorio):
    """Devuelve {ticker: [registros ordenados por fecha]}."""
    reg = defaultdict(list)
    for f in glob.glob(os.path.join(directorio, "*.json")):
        try:
            d = json.load(open(f))
        except Exception:
            continue
        if not isinstance(d, list):
            continue
        for r in d:
            if not isinstance(r, dict) or "sub_scores" not in r:
                continue
            if not all(k in r["sub_scores"] for k in REGLAS):
                continue
            reg[r["ticker"]].append(r)
    for t in reg:
        reg[t].sort(key=lambda x: x.get("fecha", ""))
    return reg


def total(r):
    return sum(float(r["sub_scores"][k]) for k in REGLAS)


def pares(reg, proc_a=None, proc_b=None):
    """Pares (pase1, pase2) del mismo ticker. Si se dan procedencias, exige que coincidan."""
    out = []
    for t, v in reg.items():
        if proc_a and proc_b:
            a = next((x for x in v if x.get("procedencia") == proc_a), None)
            b = next((x for x in reversed(v) if x.get("procedencia") == proc_b), None)
            if a and b and a is not b:
                out.append((t, a, b))
        else:
            if len(v) >= 2 and v[0].get("fecha") != v[-1].get("fecha"):
                out.append((t, v[0], v[-1]))
    return out


def rango(x):
    return np.argsort(np.argsort(-np.asarray(x, float))).astype(float) + 1


def spearman(a, b):
    ra, rb = rango(a), rango(b)
    return float(np.corrcoef(ra, rb)[0, 1])


def pearson(a, b):
    a, b = np.asarray(a, float), np.asarray(b, float)
    if a.std() == 0 or b.std() == 0:
        return float("nan")
    return float(np.corrcoef(a, b)[0, 1])


def barra(v, ancho=24):
    return "█" * max(0, int(max(0.0, v) * ancho))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default="_score_records")
    ap.add_argument("--a", default=None, help="procedencia del pase 1")
    ap.add_argument("--b", default=None, help="procedencia del pase 2")
    args = ap.parse_args()

    reg = cargar(args.dir)
    pr = pares(reg, args.a, args.b)
    if not pr:
        raise SystemExit(f"Sin pares comparables en {args.dir}")

    A = np.array([total(a) for _, a, _ in pr])
    B = np.array([total(b) for _, _, b in pr])
    n = len(pr)

    print("=" * 74)
    print(f"FIABILIDAD DEL INSTRUMENTO   (n = {n} tickers puntuados dos veces)")
    if args.a:
        print(f"comparando procedencia '{args.a}'  vs  '{args.b}'")
    print("=" * 74)

    # ---------- 1. test-retest global ----------
    rho = spearman(A, B)
    ra, rb = rango(A), rango(B)
    mov = np.abs(ra - rb)
    desp = float((B - A).mean())
    resid = (B - A) - desp
    fiab = max(0.0, 1 - resid.var() / B.var()) if B.var() > 0 else 0.0

    print(f"\n1) ORDEN — ¿el ranking se repite?")
    print(f"   Spearman rho .................. {rho:6.3f}   {barra(rho)}")
    print(f"   Movimiento medio de puesto .... {mov.mean():6.1f} de {n}")
    print(f"   Desplazamiento de nivel común . {desp:+6.2f} pts  (inofensivo: se corrige con una constante)")
    print(f"   Reordenación residual (sigma) . {resid.std():6.2f} pts  (esto SÍ es ruido)")
    print(f"   Señal entre empresas (sigma) .. {B.std():6.2f} pts")
    print(f"   FIABILIDAD IMPLÍCITA .......... {fiab:6.2f}   (>=0.85 objetivo · <0.70 inservible)")
    print(f"   Techo de validez alcanzable ... {math.sqrt(max(fiab,0)):6.2f}   (raíz de la fiabilidad)")

    for k in (10, 15):
        if n >= k:
            ta = {pr[i][0] for i in np.argsort(-A)[:k]}
            tb = {pr[i][0] for i in np.argsort(-B)[:k]}
            print(f"   TOP-{k}: coinciden {len(ta & tb)}/{k}")

    # ---------- 2. fiabilidad por regla ----------
    print(f"\n2) FIABILIDAD POR REGLA")
    print(f"   {'regla':6} {'peso':>4} {'fiab':>7}  veredicto")
    fila = []
    for r in REGLAS:
        x = [float(a["sub_scores"][r]) for _, a, _ in pr]
        y = [float(b["sub_scores"][r]) for _, _, b in pr]
        fila.append((pearson(x, y), r))
    for v, r in sorted(fila):
        et = "INSERVIBLE" if v < 0.45 else "mala" if v < 0.65 else "aceptable" if v < 0.85 else "BUENA"
        print(f"   {r:6} {PESO.get(r,10):>4} {v:7.3f}  {et:11}{barra(v)}")

    # ---------- 3. halo ----------
    E = np.array([[float(b["sub_scores"][r]) - float(a["sub_scores"][r]) for _, a, b in pr] for r in REGLAS])
    if all(E[i].std() > 0 for i in range(len(REGLAS))):
        C = np.corrcoef(E)
        w = np.sort(np.linalg.eigvalsh(C))[::-1]
        f1 = w[0] / w.sum()
        print(f"\n3) EFECTO HALO — ¿los errores de las reglas se mueven juntos?")
        print(f"   Primer factor de la matriz de ERRORES . {f1*100:5.1f}%")
        print(f"   Si el ruido fuera independiente ....... {100/len(REGLAS):5.1f}%")
        print(f"   Exceso sobre el azar .................. {f1/(1/len(REGLAS)):5.1f}x")
        print(f"   -> ~{f1*100:.0f}% del ruido se elimina puntuando A CIEGAS, una regla a la vez.")

        print(f"\n   Pares de reglas cuyos ERRORES más se mueven juntos (frontera difusa >0.30):")
        pares_e = []
        for i in range(len(REGLAS)):
            for j in range(i + 1, len(REGLAS)):
                pares_e.append((C[i, j], REGLAS[i], REGLAS[j]))
        for c, x, y in sorted(pares_e, reverse=True)[:6]:
            flag = "  <-- comparten evidencia" if c > 0.30 else ""
            print(f"     {x}-{y}: {c:+.2f}{flag}")

    # ---------- 4. ortogonalidad (ítem-resto) ----------
    M = np.array([[float(b["sub_scores"][r]) for r in REGLAS] for _, _, b in pr])
    print(f"\n4) ORTOGONALIDAD — ítem-RESTO (no ítem-total: el total contiene la propia regla)")
    for i, r in enumerate(REGLAS):
        resto = M.sum(1) - M[:, i]
        v = pearson(M[:, i], resto)
        et = "ORTOGONAL (info independiente)" if v < 0.15 else "débil" if v < 0.35 else "redundante"
        print(f"   {r:6} {v:+7.3f}  {et}")

    # ---------- 5. ablación ----------
    print(f"\n5) ABLACIÓN — quitar cada regla, ¿cuánto se mueve el ranking?")
    full = M.sum(1)
    for i, r in enumerate(REGLAS):
        red = np.delete(M, i, axis=1).sum(1)
        print(f"   sin {r:4} rho = {spearman(full, red):.4f}")
    eq = (M / np.array([PESO.get(r, 10) for r in REGLAS])).sum(1)
    print(f"   equiponderando (tirando los pesos 15/15/15): rho = {spearman(full, eq):.4f}")
    print("\n   Si todas las ablaciones dan >0.97, ninguna regla sostiene el ranking:")
    print("   el instrumento discrepa consigo mismo más que con una versión amputada de sí mismo.")
    print()


if __name__ == "__main__":
    main()
