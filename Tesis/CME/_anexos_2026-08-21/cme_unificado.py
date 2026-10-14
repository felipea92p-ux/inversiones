# -*- coding: utf-8 -*-
"""CME — valoracion unificada. Corrige la inconsistencia entre los cuatro motores:
   rf unico (4,74%, Tesoro del 21-ago-2026, el dia del precio ancla)
   ERP unico (4,23%, Damodaran titular, fila 1-ago-2026)
   gT declarado como BANDA y aplicado igual en todos los motores
   beta barrida, nunca elegida"""

P      = 275.03      # precio ancla vivo
ACC    = 361.282     # acciones diluidas medias 2T-26 (M) — la base conservadora
RF     = 0.0474      # Tesoro 10a, 21-ago-2026
ERP    = 0.0423      # Damodaran implicito titular, 1-ago-2026
KD     = 0.0535      # kd marginal de mercado pretax
TAX    = 0.236
WE, WD = 0.9664, 0.0336
DEUDA_NETA = 1148.6  # M USD
FCFF0  = 4344.0      # FCFF FY2026E consensuado entre motores (banda 4.215-4.462)
DIV_TTM= 11.25       # regular 5,20 anualizado + variable 6,15 (mar-2026)

def ke(b):   return RF + b*ERP
def wacc(b): return WE*ke(b) + WD*KD*(1-TAX)

def dcf(b, g1, gT, n=10):
    """DCF de dos etapas con fade lineal de g1 a gT."""
    w, vp, f = wacc(b), 0.0, FCFF0
    for t in range(1, n+1):
        g = g1 + (gT-g1)*(t-1)/(n-1)
        f *= (1+g)
        vp += f/(1+w)**t
    vt = f*(1+gT)/(w-gT)
    return (vp + vt/(1+w)**n - DEUDA_NETA)/ACC

BETAS = [(0.275,"mensual 60m, R2=0,04"),(0.397,"Dimson +-2, diaria"),(0.490,"sectorial 5a"),
         (0.550,"central del motor WACC"),(0.578,"diaria 10a, R2=0,18"),(0.630,"implicita en el precio"),
         (0.715,"Blume / sectorial 60m"),(0.850,"central de tres motores"),(1.022,"anual 2009-2025, R2=0,33")]

print("="*104)
print("A · DCF UNIFICADO — valor por accion. g1=4,75% (tasa base verificada: ADV +5,75% x RPC -0,99%)")
print("="*104)
print(f"{'beta':>6} {'origen':<26} {'Ke':>7} {'WACC':>7} | {'gT=2,5%':>9} {'gT=3,0%':>9} {'gT=3,5%':>9} | {'vs P (gT=3%)':>13}")
print("-"*104)
for b,src in BETAS:
    v25, v30, v35 = dcf(b,0.0475,0.025), dcf(b,0.0475,0.030), dcf(b,0.0475,0.035)
    print(f"{b:6.3f} {src:<26} {100*ke(b):6.2f}% {100*wacc(b):6.2f}% | {v25:9.0f} {v30:9.0f} {v35:9.0f} | {100*(v30/P-1):+12.1f}%")

print()
print("="*104)
print("B · EL TEST QUE MANDA PARA UN ACTIVO QUE REPARTE EL 100%: retorno total esperado vs Ke")
print("    (con payout ~100% el DCF y este test son la misma pregunta; este no necesita gT)")
print("="*104)
print(f"   Dividendo TTM real {DIV_TTM:.2f} USD (regular 5,20 + variable 6,15) -> rendimiento {100*DIV_TTM/P:.2f}%")
print()
print(f"{'beta':>6} {'Ke':>7} | " + " ".join(f"{'g='+str(g)+'%':>9}" for g in [3.0,3.5,4.0,4.75]) + "  <- retorno total - Ke, en pb")
print("-"*104)
for b,_ in BETAS:
    k = ke(b)
    row = " ".join(f"{10000*((DIV_TTM/P + g/100) - k):+9.0f}" for g in [3.0,3.5,4.0,4.75])
    print(f"{b:6.3f} {100*k:6.2f}% | {row}")
print()
print("   Positivo = el activo bate a su propio coste de capital al precio de hoy. Negativo = no lo bate.")

print()
print("="*104)
print("C · PRECIO AL QUE EL RETORNO TOTAL IGUALA AL Ke  (= 'precio justo', el umbral de Felipe)")
print("="*104)
print(f"{'beta':>6} {'Ke':>7} | " + " ".join(f"{'g='+str(g)+'%':>10}" for g in [3.0,3.5,4.0,4.75]))
print("-"*104)
for b,_ in BETAS:
    k = ke(b)
    row = ""
    for g in [3.0,3.5,4.0,4.75]:
        d = k - g/100
        row += f"{DIV_TTM/d:10.0f}" if d > 0.001 else f"{'sin tope':>10}"
    print(f"{b:6.3f} {100*k:6.2f}% | {row}")

print()
print("="*104)
print("D · LA BETA UMBRAL: por encima de ella CME esta cara; por debajo, barata")
print("="*104)
for g1,gT,lab in [(0.0475,0.025,"g1 4,75% / gT 2,5%"),(0.0475,0.030,"g1 4,75% / gT 3,0%"),(0.0400,0.025,"g1 4,00% / gT 2,5%")]:
    lo, hi = 0.0, 2.0
    for _ in range(80):
        mid = (lo+hi)/2
        if dcf(mid,g1,gT) > P: lo = mid
        else: hi = mid
    print(f"   DCF, {lab:<22} -> beta umbral {lo:.3f}  (Ke {100*ke(lo):.2f}%)")
for g in [0.030,0.035,0.040]:
    bu = (DIV_TTM/P + g - RF)/ERP
    print(f"   Retorno total, g={100*g:.1f}%          -> beta umbral {bu:.3f}  (Ke {100*ke(bu):.2f}%)")
