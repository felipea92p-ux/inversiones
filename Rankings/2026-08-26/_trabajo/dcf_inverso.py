#!/usr/bin/env python3
"""DCF INVERSO — la metrica primaria de infravaloracion.
No calcula un valor justo y resta: DESPEJA que crecimiento de owner earnings hay que
creerse para justificar el precio de HOY, y lo compara contra el crecimiento MEDIDO en filing.
Asi la constante rota del motor (13,924x) no decide nada: decide la brecha.

Motor V3 del archivo: fade multietapa, N1<=12 (C1), terminal NOPAT/r (a ROIC=r el
crecimiento no crea valor y g_terminal desaparece del modelo).
CANDADO B: r identica para toda empresa. R6 (riesgo de jurisdiccion) va al VALOR, nunca a la tasa.
"""
import json, math

R=0.0970

def valor(oe0, g0, N1, ginf, r=R, phi=0.87):
    """VP de owner earnings con fade geometrico de g0 a ginf en N1 anios + terminal."""
    if oe0 is None or oe0<=0: return None
    vp=0.0; oe=oe0; g=g0
    for t in range(1,N1+1):
        g = ginf + (g-ginf)*phi
        oe = oe*(1+g)
        vp += oe/((1+r)**t)
    # terminal: perpetuidad Gordon sobre el flujo del anio N1
    term = oe*(1+ginf)/(r-ginf)
    vp += term/((1+r)**N1)
    return vp

def g_implicita(ev, oe0, N1, ginf, r=R, phi=0.87):
    """Despeja g0 tal que valor(g0) == EV. Biseccion."""
    if not ev or not oe0 or oe0<=0: return None
    lo,hi=-0.50,1.00
    vlo,vhi=valor(oe0,lo,N1,ginf,r,phi),valor(oe0,hi,N1,ginf,r,phi)
    if vlo is None or vhi is None: return None
    if ev<vlo: return lo
    if ev>vhi: return hi
    for _ in range(80):
        mid=(lo+hi)/2
        if valor(oe0,mid,N1,ginf,r,phi)<ev: lo=mid
        else: hi=mid
    return (lo+hi)/2

def caja_sensibilidad(oe0,g0,N1,ginf):
    """C-3: matriz 3x3 (N1 -5/base/+5) x (prima -2/base/+2). ratio>2,0 -> NO DECIDIBLE."""
    vals=[]
    for dn in (-5,0,5):
        n=max(1,min(12,N1+dn))
        for dp in (-0.02,0.0,0.02):
            v=valor(oe0,g0,n,ginf,R+dp)
            if v and v>0: vals.append(v)
    if len(vals)<4: return None,None
    return max(vals)/min(vals), (min(vals),max(vals))

def pct_valor_tras_12(oe0,g0,N1,ginf,r=R,phi=0.87):
    """C-2: % del valor que vive mas alla del anio 12. Si >70% -> veredicto con phi=0,45."""
    tot=valor(oe0,g0,N1,ginf,r,phi)
    if not tot: return None
    vp=0.0; oe=oe0; g=g0
    for t in range(1,13):
        g=ginf+(g-ginf)*phi; oe=oe*(1+g)
        if t<=N1: vp+=oe/((1+r)**t)
    return 1-vp/tot

# N1 por defecto segun mecanismo (C-4 ii: la clasificacion sale del SIC, no del juicio)
N1_POR_SIC={
 '7372':8,'7370':8,'7371':8,'7389':8,   # software y servicios de datos
 '6199':9,'6200':9,'6211':9,'6231':9,   # infraestructura financiera / bolsas
 '3841':7,'3845':7,'2834':6,'8731':6,   # equipo medico / farma
 '3674':6,'3559':6,                     # semis y equipo semis (ciclico)
 '5961':7,'7389':8,'2844':6,'3021':6,
}
N1_DEFECTO=6
