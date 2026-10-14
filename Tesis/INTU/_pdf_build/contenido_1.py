# -*- coding: utf-8 -*-
"""Portada, nota de encuadre, veredicto (§1)."""
import motor_qg as M
from reportlab.platypus import Spacer, PageBreak, Table, TableStyle, KeepTogether, NextPageTemplate, Paragraph
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import ParagraphStyle
from paleta_qg import PALETA as PP
from reportlab.lib.colors import HexColor
C = {k: HexColor(v) for k, v in PP.items()}


def portada():
    out = []
    out.append(Spacer(1, 2.0 * cm))
    out.append(M.p('<font size="9.5" color="#666054"><b>DOCUMENTO DE CONVICCION · TESIS DEFINITIVA</b></font>',
                    "nota"))
    out.append(Spacer(1, 6))
    tstyle = ParagraphStyle("portada_t", fontName="Serif-B", fontSize=33, leading=38,
                            textColor=C["tinta"])
    out.append(Paragraph("INTUIT, INC.", tstyle))
    out.append(M.p('<font size="16" color="#666054"><i>NASDAQ: INTU</i></font>', "nota"))
    out.append(Spacer(1, 4))
    sub = ParagraphStyle("portada_sub", fontName="Serif-I", fontSize=15, leading=20,
                         textColor=C["azul_noche"])
    out.append(Paragraph("Doce trimestres de trayectoria, dos camaras adversariales "
                         "y una decision de tamano de posicion", sub))
    out.append(Spacer(1, 0.9 * cm))
    out.append(M.hr())
    out.append(Spacer(1, 0.5 * cm))
    out.append(M.p("Lunes 24 de agosto de 2026 &nbsp;&middot;&nbsp; escrita ANTES del reporte del "
                   "martes 25-ago (Q4 y ejercicio fiscal 2026, tras el cierre; llamada 13:30 PT)",
                   "cuerpo"))
    out.append(Spacer(1, 0.6 * cm))

    kpis = M.kpi_panel([
        ("VENDER 8", "DE 24 ACCIONES", "Escenario central &middot; ~52% de probabilidad"),
        ("US$ 304", "VALOR JUSTO CENTRAL", "Con la correccion del 23-ago &middot; precio hoy 364,53"),
        ("&minus;48,1%", "DRAWDOWN DE 52 SEMANAS", "Desde el maximo de cierre (702,09, 22-sep-2025)"),
    ])
    out.append(kpis)
    out.append(Spacer(1, 0.55 * cm))

    nota = ('<b>NOTA DE ENCUADRE, antes de nada.</b> Este es un documento de metodo dentro del marco '
            'propio de Felipe. <b>No soy asesor registrado, esto no es asesoramiento de inversion '
            'personalizado, y no ejecuto ni puedo ejecutar ninguna orden</b>: toda decision de capital '
            'es de Felipe y se toma fuera de este documento. La cifra de acciones no es una '
            'recomendacion: es la salida mecanica de la regla que Felipe sello el 22 de agosto, '
            'aplicada sin moverla, mas la declaracion explicita de donde el analisis discrepa de ella. '
            'Todo dato lleva etiqueta HECHO / INFERENCIA / SUPUESTO. Jerarquia de fuentes: EDGAR '
            '(CIK 0000896878) &gt; guiones propios de Intuit &gt; transcripcion de tercero &gt; prensa. '
            'Ni score ni ranking.')
    out.append(M.callout("PAUSA REFLEXIVA", nota))

    caduca = ('<b>Que caduca y que no.</b> Las trayectorias, los mecanismos y las promesas fechadas '
              '(secciones 2, 3 y 4) siguen siendo validas el miercoles: son calculos sobre filings '
              'cerrados, no sobre el precio de hoy. La valoracion (seccion 5) esta fechada al cierre '
              'del 21-ago-2026 y <b>caduca el 21-sep-2026</b>. La decision de tamano (seccion 7) se '
              'resuelve manana por la noche, con el reporte ya publicado.')
    out.append(M.callout("LECCIÓN TRANSFERIBLE", caduca))

    out.append(NextPageTemplate("Normal"))
    out.append(PageBreak())
    return out


def indice_lectura():
    out = M.flag_titulo("Como leer este documento",
                        "Once secciones, en el orden en que se construyo el juicio")
    filas = [
        ["§", "Contenido", "Por que importa"],
        ["1", "Veredicto y la rejilla completa de escenarios", "La respuesta, antes que el argumento"],
        ["2", "El negocio: de donde sale cada dolar", "Precio contra unidades, motor por motor"],
        ["3", "Doce trimestres: promesas contra entregas", "El corazon del documento — no caduca"],
        ["4", "El mecanismo del moat", "Cuanto dura la ventaja y por que"],
        ["5", "La valoracion", "Motor, insumos en disputa, matriz de sensibilidad"],
        ["6", "El cruce: abogado del diablo contra abogado angel", "Donde gana cada uno y por que"],
        ["7", "La decision de tamano de posicion", "Que hacer con las 24 acciones, escenario por escenario"],
        ["8", "Los seis campos del anti-limbo", "Ficha completa: precio, tamano, caducidad"],
        ["9", "Cuatro falsables", "Que dato, en que fecha, mataria esta tesis"],
        ["10", "Sesgos declarados", "Los de Felipe y los del redactor"],
        ["11", "Lo que esta tesis no puede resolver", "Sin fingir que se cierra"],
    ]
    out.append(M.tabla(filas, [1.1 * cm, 6.9 * cm, 9.0 * cm]))
    out.append(Spacer(1, 10))
    return out
