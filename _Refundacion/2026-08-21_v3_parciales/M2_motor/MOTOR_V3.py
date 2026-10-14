# -*- coding: utf-8 -*-
"""MOTOR DE VALORACION V3.1 — DCF multietapa con FADE DE ROIC (dos fades separados).
EV en multiplos de NOPAT_0. Sin beta, sin dial de g terminal.
  r      = T10Y nominal + prima fija            (candado B)
  g_inf  = breakeven de inflacion = T10Y - TIPS10Y   (candado B extendido: sale del mercado, no del analista)
  phi    = 0,87 constante de la casa (medida sobre EDGAR 2009-2025)
  N1     = UNICO input de juicio: años de meseta del exceso de ROIC. Con techo por tipo de moat.
"""
PHI_CASA=0.87; CORTE=0.0025; NMAX=45

def dcf(nopat0, roiic0, g0, r, N1, g_inf, phi=PHI_CASA, Ng=None, detalle=False):
    """Ng = años de meseta de crecimiento (por defecto = N1: el crecimiento no dura mas que el foso)."""
    if Ng is None: Ng=N1
    Ng=min(Ng,N1)
    exc0=max(roiic0-r,0.0); vp=0.0; nopat=float(nopat0); filas=[]; t=0
    roiic=roiic0; g=g0
    while t<NMAX:
        t+=1
        # --- fade del RETORNO ---
        if t<=N1: roiic=roiic0
        else:
            exc=exc0*phi**(t-N1)
            roiic=r+exc if exc>CORTE else r
        # --- fade del CRECIMIENTO ---
        if t<=Ng: g=g0
        else:     g=g_inf+(g0-g_inf)*phi**(t-Ng)
        nopat*=(1+g)
        b=min(max(g/roiic,0.0),1.0) if roiic>0 else 1.0   # reinversion REQUERIDA, no elegida
        fcf=nopat*(1-b)
        vp+=fcf/(1+r)**t
        filas.append((t,roiic,g,b,nopat,fcf))
        if t>=N1 and roiic<=r+CORTE and abs(g-g_inf)<0.0015: break
    vt=nopat*(1+g_inf)/r          # ROIIC=r => el crecimiento es valor-neutral => VT=NOPAT_T(1+g_inf)/r
    vp+=vt/(1+r)**t
    return (vp,t,filas,vt/(1+r)**t/vp) if detalle else vp

def mult(roiic0,g0,r,N1,g_inf,phi=PHI_CASA,Ng=None): return dcf(1.0,roiic0,g0,r,N1,g_inf,phi,Ng)

def n1_implicito(m_obs,roiic0,g0,r,g_inf,phi=PHI_CASA,hi=40):
    if m_obs<mult(roiic0,g0,r,0,g_inf,phi): return None
    for n in range(hi):
        a=mult(roiic0,g0,r,n,g_inf,phi); b=mult(roiic0,g0,r,n+1,g_inf,phi)
        if a<=m_obs<=b: return n+(m_obs-a)/(b-a)
    return float('inf')

def tir(m_obs,roiic0,g0,N1,g_inf,phi=PHI_CASA,lo=0.005,hi=0.60):
    for _ in range(120):
        mid=(lo+hi)/2
        if mult(roiic0,g0,mid,N1,g_inf,phi)>m_obs: lo=mid
        else: hi=mid
    return (lo+hi)/2

def valor_destruccion(roiic0,b0,r,g_inf,años):
    """Caso ROIIC<r con reinversion mantenida 'años' y luego parada. Devuelve EV/NOPAT_0."""
    g=b0*roiic0; vp=0.0; nopat=1.0
    for t in range(1,años+1):
        nopat*=(1+g); vp+=nopat*(1-b0)/(1+r)**t
    vp+=(nopat*(1+g_inf)/r)/(1+r)**años
    return vp
