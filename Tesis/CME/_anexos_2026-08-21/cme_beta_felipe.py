# -*- coding: utf-8 -*-
"""La beta correcta para una cartera de 14 nombres, no para el indice.
Damodaran: beta_total = beta / R(activo,mercado)  -> limite de NO diversificacion.
Para un inversor PARCIALMENTE diversificado: beta_ajustada = beta / R(cartera,mercado).
Con R_cartera = 1 se recupera el CAPM clasico; con R_cartera = R_activo, la beta total."""
P, RF, ERP, DIV = 275.03, 0.0474, 0.0423, 11.25

print("Cartera viva (IBKR, 21-ago-2026): 14 posiciones, NAV 145.336 USD.")
print("MELI 19,9% · DUOL 15,1% · TSM 7,8% · GOOGL 7,8% · AMZN 6,4% · BRK.B 6,2% · INTU 6,0% ...")
print("Correlacion estimada de esa cartera con el S&P 500: 0,85-0,92 (SUPUESTO declarado,")
print("no medido: es una cartera de megacaps de EEUU + MELI + TSM, sin cobertura ni bonos).")
print()
print("="*94)
print("BETA AJUSTADA POR CONCENTRACION = beta de mercado / R(cartera, mercado)")
print("="*94)
print(f"{'beta mercado':>13} {'origen':<24} | " + " ".join(f"{'R='+str(r):>9}" for r in [1.00,0.92,0.85,0.19]))
print("-"*94)
for b, src in [(0.578,"diaria 10a, R2=0,18"),(0.630,"implicita en el precio"),(0.715,"Blume"),(0.850,"tres motores")]:
    print(f"{b:13.3f} {src:<24} | " + " ".join(f"{b/r:9.2f}" for r in [1.00,0.92,0.85,0.19]))
print()
print("  R=1,00 -> CAPM puro (inversor perfectamente diversificado: no es el caso de Felipe)")
print("  R=0,19 -> beta TOTAL de Damodaran (inversor con UNA sola posicion: tampoco es el caso)")
print("  R=0,85-0,92 -> el rango realista para 14 nombres. Es el que uso.")
print()
BU_DCF, BU_RT = 0.651, 0.674   # betas umbral calculadas antes (gT 2,5% / g 3,5%)
print("="*94)
print("VEREDICTO DEL AJUSTE")
print("="*94)
lo, hi = 0.578/0.92, 0.715/0.85
print(f"  Banda de beta ajustada para ESTA cartera: {lo:.2f} - {hi:.2f}   (centro {(lo+hi)/2:.2f})")
print(f"  Beta umbral de indiferencia (DCF gT 2,5% / retorno total g 3,5%): {BU_DCF:.2f} - {BU_RT:.2f}")
print()
for b,lab in [(lo,"suelo"),((lo+hi)/2,"centro"),(hi,"techo")]:
    ke = RF + b*ERP
    pj = DIV/(ke-0.035)
    print(f"  beta {b:.2f} ({lab:6}) -> Ke {100*ke:5.2f}%  ->  precio justo con g=3,5%: {pj:6.0f} USD  ({100*(pj/P-1):+5.1f}% vs 275,03)")
print()
print("  Es decir: para una cartera de catorce nombres, la beta relevante de CME cae")
print("  ENCIMA de la beta umbral, no debajo. El margen de seguridad no es positivo:")
print("  es CERO en el centro y ligeramente negativo en el techo.")
