# -*- coding: utf-8 -*-
"""Aritmetica de Terry Smith: que multiplo justifica el ROCE x pista de reinversion."""

def multiplo_justificado(roce, rr, anios_pista, wacc=0.08, g_term=0.025, roic_term=None):
    """
    NOPAT_0 = 1. Reinvierte 'rr' del NOPAT a 'roce' durante 'anios_pista'.
    => g = roce * rr ; FCF = NOPAT * (1-rr)
    Despues: crecimiento terminal g_term a roic_term (por defecto = wacc, sin creacion de valor).
    Devuelve el multiplo justificado sobre NOPAT_0.
    """
    if roic_term is None: roic_term = wacc
    g = roce*rr
    vp=0.0; nopat=1.0
    for t in range(1, anios_pista+1):
        nopat *= (1+g)
        vp += (nopat*(1-rr))/(1+wacc)**t
    nopat_t = nopat*(1+g_term)
    rr_t = g_term/roic_term
    tv = nopat_t*(1-rr_t)/(wacc-g_term)
    vp += tv/(1+wacc)**anios_pista
    return vp, g

print("="*78)
print("ARITMETICA TERRY SMITH — multiplo justificado sobre NOPAT (WACC 8%, g_term 2.5%)")
print("="*78)
print()
print("Caso central pedido: ROCE 30% vs ROCE 10%, 15 anios de pista, reinvierte 50%")
print("-"*78)
for roce in (0.30, 0.10):
    m,g = multiplo_justificado(roce, 0.50, 15)
    print(f"  ROCE {roce:>4.0%} · reinvierte 50% · g={g:>5.1%} · 15 anios  ->  multiplo justo {m:>6.1f}x")
print()
print("El mismo negocio si REINVIERTE TODO lo que puede (rr=100%):")
print("-"*78)
for roce in (0.30, 0.10):
    m,g = multiplo_justificado(roce, 1.00, 15)
    print(f"  ROCE {roce:>4.0%} · reinvierte 100% · g={g:>5.1%} · 15 anios ->  multiplo justo {m:>6.1f}x")
print()
print("SENSIBILIDAD A LA PISTA (rr=50%) — el multiplo justo por anios de reinversion")
print("-"*78)
print(f"{'ROCE':>6} | " + " ".join(f"{n:>7}a" for n in (5,10,15,20,25)))
for roce in (0.40,0.30,0.20,0.15,0.10,0.08):
    fila=[]
    for n in (5,10,15,20,25):
        m,_=multiplo_justificado(roce,0.50,n)
        fila.append(f"{m:>7.1f}x")
    print(f"{roce:>6.0%} | " + " ".join(fila))
print()
print("MISMO CRECIMIENTO (10%), DISTINTO ROCE — el coste del capital que se traga")
print("-"*78)
print(f"{'ROCE':>6} {'rr necesaria':>13} {'FCF/NOPAT':>10} {'multiplo justo (15a)':>22}")
for roce in (0.50,0.30,0.20,0.15,0.125,0.11):
    rr = 0.10/roce
    if rr>1: continue
    m,_ = multiplo_justificado(roce, rr, 15)
    print(f"{roce:>6.0%} {rr:>12.0%} {1-rr:>10.0%} {m:>21.1f}x")
