# -*- coding: utf-8 -*-
"""DCF INVERSO con fade explicito. Despeja el g implicito del precio de hoy."""

def valor(oe0, g1, n_explicito, n_fade, wacc, g_term, roic, roic_term=None):
    """
    Fase 1: n_explicito anios creciendo g1, reinvirtiendo g1/roic.
    Fase 2: n_fade anios, g decae linealmente de g1 a g_term, roic decae a roic_term.
    Fase 3: perpetuidad g_term con roic_term.
    Devuelve valor por unidad de NOPAT_0.
    """
    if roic_term is None: roic_term = wacc + 0.02
    vp=0.0; nopat=1.0
    for t in range(1, n_explicito+1):
        nopat *= (1+g1)
        vp += nopat*(1-min(g1/roic,0.95))/(1+wacc)**t
    for j in range(1, n_fade+1):
        f=j/n_fade
        g = g1 + (g_term-g1)*f
        r = roic + (roic_term-roic)*f
        nopat *= (1+g)
        t = n_explicito+j
        vp += nopat*(1-min(g/r,0.95))/(1+wacc)**t
    N=n_explicito+n_fade
    nt = nopat*(1+g_term)
    tv = nt*(1-g_term/roic_term)/(wacc-g_term)
    vp += tv/(1+wacc)**N
    return vp

def g_implicito(multiplo_precio, n_explicito, n_fade, wacc, g_term, roic, roic_term=None, tol=1e-6):
    """Biseccion sobre g1 para que valor() == multiplo_precio."""
    lo, hi = -0.20, 1.20
    for _ in range(200):
        mid=(lo+hi)/2
        v=valor(1.0, mid, n_explicito, n_fade, wacc, g_term, roic, roic_term)
        if v < multiplo_precio: lo=mid
        else: hi=mid
        if hi-lo < tol: break
    return (lo+hi)/2

print("="*80)
print("DCF INVERSO — g implicito 1-10a segun el multiplo que pagas")
print("Estructura: 10a explicitos + 10a de fade + perpetuidad 2.5%")
print("WACC 8%  ·  ROIC fase 1 = 30%  ·  ROIC terminal = 10%")
print("="*80)
print(f"{'Precio/OE':>10} {'g implicito':>13} {'veredicto vs tasa base'}")
BASE_10Y_REAL_GE10 = 0.197   # % de empresas que logran >=10% CAGR real de ventas 10a
for px in (15,20,25,30,35,40,45,50,60,70,80):
    g = g_implicito(px, 10, 10, 0.08, 0.025, 0.30, 0.10)
    # traducir nominal->real asumiendo 2.5% inflacion para comparar con Mauboussin
    g_real = (1+g)/1.025 - 1
    print(f"{px:>9}x {g:>12.1%}   (real {g_real:>5.1%})")

print()
print("="*80)
print("SENSIBILIDAD DEL g IMPLICITO AL WACC — a precio fijo de 40x")
print("="*80)
for w in (0.07,0.08,0.09,0.10):
    g=g_implicito(40,10,10,w,0.025,0.30,0.10)
    print(f"  WACC {w:>4.0%}  ->  g implicito {g:>6.1%}")

print()
print("="*80)
print("SENSIBILIDAD AL ROIC ASUMIDO — a precio fijo de 40x, WACC 8%")
print("="*80)
for r in (0.60,0.40,0.30,0.20,0.15):
    g=g_implicito(40,10,10,0.08,0.025,r,0.10)
    print(f"  ROIC {r:>4.0%}  ->  g implicito {g:>6.1%}   (reinv. necesaria {g/r:>5.0%} del NOPAT)")

print()
print("="*80)
print("COSTE DEL HORIZONTE CORTO — el mismo negocio, distinto n explicito")
print("g1=15%, ROIC 30%, WACC 8%, fade 10a, g_term 2.5%")
print("="*80)
for n in (0,3,5,10,15):
    v=valor(1.0,0.15,n,10,0.08,0.025,0.30,0.10)
    print(f"  {n:>2} anios explicitos  ->  valor justo {v:>6.1f}x OE")
