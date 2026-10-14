# -*- coding: utf-8 -*-
"""Motor de precio: diagnostico del fallo + aritmetica Terry Smith + DCF inverso."""

def techo_perpetuidad(wacc, g):
    return 1.0/(wacc-g)

print("="*72)
print("A) DIAGNOSTICO: el techo de multiplo que impone la perpetuidad")
print("="*72)
print(f"{'WACC':>6} {'g_term':>7} {'multiplo maximo terminal':>26}")
for wacc in (0.08,0.09,0.10):
    for g in (0.025,0.03):
        print(f"{wacc:>6.1%} {g:>7.1%} {techo_perpetuidad(wacc,g):>24.1f}x")

def dcf_2etapas(oe0, g1, n, wacc, g_term, roic_term=None, roic1=None):
    """DCF con reinversion explicita. Si roic1 dado, FCF=NOPAT*(1-g1/roic1)."""
    vp=0.0; oe=oe0
    for t in range(1,n+1):
        oe*= (1+g1)
        fcf = oe*(1-g1/roic1) if roic1 else oe
        vp += fcf/(1+wacc)**t
    oe_t = oe*(1+g_term)
    rr_t = g_term/roic_term if roic_term else 0.0
    tv = oe_t*(1-rr_t)/(wacc-g_term)
    vp += tv/(1+wacc)**n
    return vp, (tv/(1+wacc)**n)/vp

print()
print("="*72)
print("B) REPLICA DEL BUG: 5 anios explicitos, sin creditar reinversion")
print("="*72)
print("Se descuenta el FCF actual (ya neto de todo el capex de crecimiento),")
print("se crece 5 anios y se cierra con perpetuidad g=2.5%, WACC=9%.")
print()
print(f"{'g 1-5a':>7} {'multiplo justo /OE':>20} {'precio real':>12} {'MoS resultante':>16}")
for g1 in (0.05,0.10,0.15,0.20,0.25):
    v,_ = dcf_2etapas(1.0, g1, 5, 0.09, 0.025)
    for px in (45,):
        mos = 1 - px/v
        print(f"{g1:>7.0%} {v:>19.1f}x {px:>11}x {mos:>15.0%}")
