# -*- coding: utf-8 -*-
"""Secciones 8-11 + Anexo de trazabilidad."""
import motor_qg as M
from reportlab.platypus import Spacer, PageBreak
from reportlab.lib.units import cm


def seccion_8():
    out = M.flag_titulo("8 &middot; Los seis campos del anti-limbo",
                        "Un veredicto sin estos seis campos no existe — es la regla que mata el "
                        "“todavia” sin fecha")
    filas = [
        ["#", "Campo", "Valor"],
        ["1", "P_justo", "304 USD CON la correccion del 23-ago (g&#8734; = 3,58%) &middot; 261 USD "
         "SIN ella (g&#8734; = 2,34%) &middot; 338 USD con g&#8734; al techo de 4,30% &middot; "
         "209 USD con g&#8734; = 0 y techo 10,32&times;. Base OE 3.982 M, g&#8320; 9%, r 9,69%. "
         "Peso del terminal 43,1%-62,0% (nunca &gt;75%)"],
        ["2", "P_tramo1 / P_pleno", "N2, MoS 25-35%. CON la correccion: P_tramo1 228 USD &middot; "
         "P_pleno 198 USD. SIN: 196 / 170 USD"],
        ["3", "Tamano en % del NAV", "4,02% (16 acc.) en el escenario central; 3,02% (12 acc.) si "
         "2+ piernas fallan; 4,52% (18) si ninguna falla. Techo absoluto 6,03% — no se anade ni "
         "una accion por encima de 228 USD. Tope de ruina 15%: no vinculante aqui"],
        ["4", "Alternativa real", "Efectivo al 4,69% (Tesoro 10a, H.15 del 21-ago). INTU rinde "
         "8,71% de TIR a diez anos en el central (+402 pb) y 4,690% en la celda mas dura de toda la "
         "matriz (empate exacto). El rendimiento estatico de owner earnings sobre EV es 3,94% — por "
         "debajo del efectivo, y es la unidad equivocada para una comparacion a diez anos, pero se "
         "publica"],
        ["5", "Test de alcanzabilidad", "FALLA. El minimo de cierre de los ultimos 12 meses es "
         "255,07 USD (semana del 22-jun-2026) y el minimo de cierre semanal de 24 meses es 267,00 "
         "USD. P_tramo1 = 228 USD nunca fue precio de cierre en la ventana. Falla por 27 USD "
         "(10,6%). Consecuencia mecanica: el caso de COMPRA queda ARCHIVADO 12 MESES"],
        ["6", "Caducidad", "[CADUCA: 2026-09-21] — fin de la cuarentena de la correccion de g&#8734;. "
         "La valoracion se rehace ese dia. Controles intermedios: 25-ago (reporte), ~3-sep (10-K "
         "FY2026), 17-sep (Investor Day)"],
    ]
    out.append(M.tabla(filas, [0.7 * cm, 3.4 * cm, 12.9 * cm], font_sz=7.9))
    out.append(Spacer(1, 8))
    out.append(M.p(
        "<i>Matiz sobre el campo 5, para que nadie lo lea como “inalcanzable”: el precio cerro a "
        "255,07 hace nueve semanas, no hace 42 meses como el MSFT-227 que origino la regla.</i>",
        "nota"))
    out.append(M.callout("PAUSA REFLEXIVA",
        "<b>Veredicto formal del expediente de compra: NO, ARCHIVADO 12 MESES.</b> Y el archivo "
        "archiva el caso de compra, no la posicion: no suspende el gate, ni el test del hoy del ADN, "
        "ni el trigger de drawdown, ni la revision de sizing — asi lo resolvio el Acta de B4 el "
        "23-ago y vale para las cinco empresas."))
    out.append(M.p(
        "<b>Fila para libro-omisiones.md:</b><br/>"
        "<font face=\"Sans\" size=\"7.6\">2026-08-24 &middot; INTU &middot; NO archivado 12 m &middot; "
        "precio 364,53 &middot; P_tramo1 228 &middot; P_justo 304 (con correccion) / 261 (sin) "
        "&middot; caso alcista maximo registrado 533 (camara del angel: OE 5.100, g&#8320; 13,95%, "
        "g&#8734; 4,30%) &middot; caso bajista maximo registrado 171 (camara del diablo: OE 3.982, "
        "g&#8320; 3,95%, g&#8734; 0) &middot; alternativa: efectivo 4,69% &middot; falsador del "
        "angel: 10-K FY2026 ~3-sep, ingresos de QBO Advanced + IES &lt;+25% &rarr; su caso muere "
        "&middot; falsador del diablo: ROIIC 4a sobre ventana mandada &le; r &rarr; su caso vive"
        "</font>", "cuerpo"))
    out.append(PageBreak())
    return out


def seccion_9():
    out = M.flag_titulo("9 &middot; El falsable",
                        "Cuatro, cada uno con metrica, umbral y fecha. Aqui se califica el pronostico")

    bloques = [
        ("F1 &middot; El falsable de la TESIS DE COSECHA", "~3-sep-2026 (10-K FY2026), con lectura "
         "previa el 25-ago",
         "<b>Metrica:</b> clientes de pago del ecosistema online FY2026 y “US QBO customers "
         "excluding self-employed” FY2026 y crecimiento del gasto de marketing del ano completo.<br/>"
         "<b>Umbral que FALSA esta tesis:</b> si los clientes de pago del ecosistema online salen "
         "&ge;+8% y el marketing crece por encima de los ingresos, entonces el mecanismo que se "
         "afirma —recortar adquisicion y tomar precio sobre una base cautiva— no esta ocurriendo, y "
         "la tesis de cosecha de este documento queda falsada. En ese caso el recorte se queda en la "
         "cifra minima de la rejilla y el expediente se reabre.<br/>"
         "<b>Umbral que la CONFIRMA en su forma dura:</b> clientes &le;+5% con ARPC &ge;+12% y QBO "
         "EE.UU. ex-autonomos &le;+6% y el marketing creciendo por debajo de los ingresos. Eso es la "
         "firma contable de la cosecha y sube el recorte de 8 a 12 sin discusion adicional.<br/>"
         "<b>Prediccion sellada:</b> clientes +4% (rango +3/+5%, 80% de confianza de que sea &le;5%); "
         "ARPC +14% (90% de que sea &ge;12%); QBO ex-autonomos +7% (rango +5/+8%)."),
        ("F2 &middot; El falsable del ANGEL, escrito por el y que se adopta", "25-ago / ~3-sep-2026",
         "<b>Metrica:</b> ingresos de QBO Advanced + Intuit Enterprise Suite, FY2026.<br/>"
         "<b>Umbral:</b> &lt;+25% &rarr; su Cargo 2 cae entero, el gate de gates.md si media el "
         "mecanismo que nombra, y la critica al instrumento se retira. &ge;+35% &rarr; el gate esta "
         "mal apuntado y hay que reescribirlo antes de volver a invocarlo."),
        ("F3 &middot; El falsable de la CANTERA, el unico riesgo estructural vivo",
         "17-sep-2026 (Investor Day)",
         "<b>Metrica:</b> declarantes originados desde Credit Karma y su tasa de conversion a "
         "cliente de pago de TurboTax, con cifra.<br/>"
         "<b>Umbral:</b> si el Investor Day no publica esa cifra, el riesgo de que Intuit este "
         "cobrando hoy el inventario de manana queda sin resolver por cuarta vez, y se registra fila "
         "de omision con esa fecha. Si la publica y la conversion es &ge; la de la cantera gratuita "
         "historica, la vida util del moat de TurboTax sube del rango 5-8 anos al de QuickBooks."),
        ("F4 &middot; El falsable del CANDADO DE RECOMPRA", "25-ago-2026",
         "<b>Metrica:</b> precio medio de la recompra del Q4 FY2026.<br/>"
         "<b>Umbral:</b> &gt;304 USD (P_justo central) &rarr; confirmacion de que la direccion sigue "
         "destruyendo valor tapando dilucion, y el candado queda activo en la revision del 21-sep. "
         "&le;304 USD &rarr; primera ejecucion por debajo del valor intrinseco desde FY2023.<br/>"
         "<b>Prediccion sellada:</b> &ge;1.200 M ejecutados a un precio medio &le;450 USD (en el Q3 "
         "compraron 3,749 M de acciones a 416,38)."),
    ]
    for tit, fecha, cuerpo in bloques:
        out.append(M.p(f"<b>{tit}</b> &mdash; <i>{fecha}</i>", "h3"))
        out.append(M.p(cuerpo, "cuerpo"))
    out.append(PageBreak())
    return out


def seccion_10():
    out = M.flag_titulo("10 &middot; Sesgos declarados, incluidos los del redactor",
                        "Cazar el sesgo en el instante en que aparece, no al cierre del documento")

    out.append(M.p("<b>De Felipe, ya escritos en el pre-compromiso:</b>", "h3"))
    fp = [
        "<b>Sunk cost disfrazado de “todavia”</b> — diagnosticado en el diario del 26-jul y nunca "
        "corregido. La posicion lleva +39% y eso hace que mantener se sienta gratis.",
        "<b>Compromiso y consistencia</b> — quinto documento consecutivo sobre INTU y ninguno ha "
        "vendido una accion todavia. Verbalizar endurece la posicion (Li Lu / Pabrai). Este "
        "documento es el quinto y sale con un numero distinto de cero. Esa es toda la correccion que "
        "se puede aportar desde dentro.",
        "<b>Efecto disposicion, medido:</b> 14:1 en esta misma cartera el 21-ago. Se vende lo que "
        "gana poco y se guarda lo que gana mucho. INTU lleva +39%.",
    ]
    for f in fp:
        out.append(M.p(f"&#9642; {f}", "cuerpo"))

    out.append(M.p("<b>El trigger de drawdown y la pregunta de Li Lu, que el archivo nunca activo y "
                   "que aqui se responde:</b>", "h3"))
    out.append(M.p(
        "INTU esta &minus;48,1% desde su maximo de cierre de 52 semanas (702,09 el 22-sep-2025). El "
        "trigger permanente del ADN se dispara a &minus;25% y gates.md no lo registraba para INTU. La "
        "pregunta obligada es: &ldquo;¿esta caida pone a prueba la autenticidad del circulo de "
        "competencia?&rdquo;", "cuerpo"))
    out.append(M.callout("PAUSA REFLEXIVA",
        "<b>Respuesta: SI, y la prueba la pasa a medias.</b> La caida no fue una sorpresa sobre el "
        "negocio &mdash;el negocio hizo exactamente lo que este documento describe&mdash; sino sobre "
        "el multiplo: de 48,6&times; owner earnings a 17,9&times; en nueve meses. Quien creia tener "
        "una tesis sobre el negocio tenia en realidad una posicion apalancada al multiplo. <b>Eso es "
        "un fallo de circulo de competencia sobre el PRECIO, no sobre la EMPRESA.</b> Y la parte que "
        "la pasa: Felipe compro a 262,23, es decir cerca del suelo, no en el panico ni en la euforia. "
        "La caida no le pillo dentro con tamano; le pillo fuera y entro. Eso hay que anotarlo a favor "
        "y no dejar que la narrativa del sesgo se lo coma."))

    out.append(M.p("<b>Los del redactor, que hay que vigilar mas porque nadie mas los va a "
                   "nombrar:</b>", "h3"))
    propios = [
        "<b>Sesgo de integrador.</b> Este documento arbitra entre dos camaras y las dos han hecho "
        "trabajo mejor documentado que el propio en sus respectivos frentes. La posicion del arbitro "
        "premia el punto medio, y el resultado (8) esta literalmente entre 0 y 20. Puede que sea la "
        "respuesta correcta y puede que sea la respuesta comoda. El control aplicado: se adopto la "
        "base de owner earnings mas baja, el g&#8734; mas bajo de la correccion, el nivel de MoS mas "
        "exigente admisible, y se declaro el fallo del test de alcanzabilidad que archiva la compra. "
        "Con esos cuatro frenos puestos, sigue sin salir “vender mas de 12”.",
        "<b>Sesgo de sesion no limpia.</b> Se leyeron las dos camaras antes de calcular. El motor "
        "reproduce las dos matrices, lo cual es tranquilizador sobre la aritmetica y no lo es en "
        "absoluto sobre la eleccion de insumos: se sabia que numeros producirian que conclusion "
        "mientras se elegian.",
        "<b>Sesgo de novedad del dato de precio.</b> Se encontro el historico de precios que ninguna "
        "camara uso y eso ha dado una pieza fuerte. La tentacion de sobrevalorar el propio hallazgo "
        "es real. Se acota: el historico cambia el encuadre y no cambia ni una celda de la "
        "valoracion, que se calcula sobre filings, no sobre cotizaciones.",
        "<b>Sesgo de deferencia a la regla sellada.</b> Cumplir C3 es comodo: exime de defender un "
        "numero propio. Se ha compensado escribiendo en §7.7 la discrepancia con su cifra exacta "
        "(0 contra 8) en lugar de esconderla detras del cumplimiento.",
        "<b>Y el que no se puede compensar:</b> se lleva el marco de “cosecha” heredado de la "
        "sintesis de trayectoria. Es una hipotesis potente y por eso mismo organiza la evidencia a su "
        "favor. El falsable F1 esta escrito precisamente para que pueda perder.",
    ]
    for p in propios:
        out.append(M.p(f"&#9642; {p}", "cuerpo"))
    out.append(PageBreak())
    return out


def seccion_11():
    out = M.flag_titulo("11 &middot; Lo que esta tesis no puede resolver",
                        "Sin fingir que se cierra. Seis puntos, ordenados por lo que costaria "
                        "equivocarse")

    puntos = [
        ("1 &middot; Si Credit Karma cambio la cantera de sitio o si la cantera se esta vaciando.",
         "Es la unica pregunta que puede convertir a Intuit en otra empresa, tiene una firma temporal "
         "de tres a cinco anos, es invisible en cualquier trimestre, y no hay serie publica que la "
         "responda. La cantera gratuita cayo de 13 M a ~7 M en cuatro anos y el propio 10-K la "
         "declara la fuente de los clientes de pago futuros. NO DECIDIBLE hoy. Fecha de la unica "
         "oportunidad de resolverla: 17-sep-2026."),
        ("2 &middot; Cual es la tasa de reinversion real de un negocio que reinvierte por la cuenta "
         "de resultados.",
         "Intuit gasto en FY2025 5.035 M en marketing (26,7% de ingresos) y 2.928 M en I+D (15,5%) "
         "&mdash;juntos, 2,02 veces su NOPAT. Si un cuarto de eso es inversion de crecimiento, la tasa "
         "de reinversion real supera el 50% y la g coherente sube a ~9%. g = reinversion &times; ROIC "
         "con la reinversion medida en el balance subestima estructuralmente a un negocio sin "
         "capital, y el metodo no tiene regla para eso. Es la mayor palanca abierta: mueve el tope de "
         "g&#8320; de 3,95% a 13,95%, un factor de 3,5&times;. Se entrega sin resolver, como manda "
         "C6."),
        ("3 &middot; Cual es la convencion correcta de capital invertido, y si el umbral de "
         "dispersion de C-4(i) aplica.",
         "Con los datos del diablo la dispersion entre ventanas de ROIIC es 10,31 pp, por encima del "
         "umbral de 10 pp que declara ciclica a una empresa. Intuit no es ciclica; la dispersion es "
         "calendario de M&amp;A. La regla no distingue y no se puede escribir hoy sin caer en C2/C3."),
        ("4 &middot; Si la IA es palanca de precio o compresor de precio, en neto.",
         "Hay evidencia primaria en las dos direcciones (agentes con &gt;85% de recurrencia y la "
         "aritmetica de los 900 USD de valor contra el ARPU de TT Live en &minus;1,4%), tres nombres "
         "de marca en cinco trimestres y cero metricas de ingresos asociadas en ningun trimestre. No "
         "es resoluble con filings hoy."),
        ("5 &middot; El reparto exacto precio/volumen de QuickBooks Online Accounting.",
         "En los tres trimestres de FY2026 la formula es cualitativa y en el mismo orden. La unica "
         "cuantificacion que la direccion ha dado en dos anos es “Pricing contribution is relatively "
         "consistent throughout the four quarters” &mdash;no dice cuanta. Sin ella, todo lo que este "
         "documento afirma sobre el reparto es inferencia sobre el orden de las palabras del filing, "
         "no medicion."),
    ]
    for tit, cuerpo in puntos:
        out.append(M.p(f"<b>{tit}</b> {cuerpo}", "cuerpo"))

    out.append(M.p("<b>6 &middot; Lo que no se pudo ver, declarado sin adorno.</b>", "cuerpo"))
    huecos = [
        "Quartr: sin acceso (subscription_required, plan “none”). Bigdata.com: sin creditos. Cero "
        "llamadas utiles por ambas vias, en cuatro mesas distintas. Recomendacion operativa: resolver "
        "Quartr antes del Investor Day del 17-sep, o el bloque de transcripciones de septiembre "
        "volvera a construirse con transcripcion de tercero.",
        "investors.intuit.com devuelve 403 para las hojas de datos de FY2025-FY2026.",
        "El Q&amp;A de FY2025 no existe verbatim en el expediente; todo lo citado de ese ano es 8-K "
        "o guion propio.",
        "El fondo de comercio asignado especificamente a Mailchimp (~8.167 M) es INFERENCIA por "
        "diferencia, no HECHO: el 10-K no lo desglosa.",
        "No se ha podido cerrar la discrepancia de 2,47 USD entre el cierre del 21-ago que fija el "
        "encargo (364,53) y el que devuelve IBKR (367,00).",
    ]
    for h in huecos:
        out.append(M.p(f"&#9642; {h}", "cuerpo"))
    out.append(PageBreak())
    return out


def anexo():
    out = M.flag_titulo("Anexo &middot; Trazabilidad",
                        "")
    out.append(M.p(
        "<b>Ficheros del repositorio consultados:</b> /CLAUDE.md &middot; /ADN-QG12.md &middot; "
        "/gates.md (§C INTU, §Regla de venta de tres puertas, §Triggers permanentes, §Decisiones "
        "abiertas) &middot; /Tesis/INTU/2026-08-22_PreCompromiso_INTU_25ago.md &middot; "
        "/_Refundacion/2026-08-21_Recalibracion_Metodologia_v2.md (§4.2, §4.3, §4.4, C-4, C-5, C-7, "
        "C-9, C-11, Anexo &middot; Enmienda 29 y 29-bis) &middot; "
        "/_Refundacion/2026-08-22_Acta_Activacion_B4.md (§0 condicion iii, §1 conteo B3, §2 Regla de "
        "eje, §3 los cuatro cruces 10c) &middot; /_Refundacion/2026-08-23_Prueba_Infalibilidad.md.",
        "cuerpo"))
    out.append(M.p(
        "<b>Datos vivos:</b> IBKR MCP, contrato 270662 (INTUIT INC, NASDAQ), barras diarias de 12 "
        "meses y semanales de 24 meses, extraidas el 24-ago-2026. Maximo de cierre 52s 702,09 "
        "(22-sep-2025); minimo de cierre 12m 255,07 (semana del 22-jun-2026); cierre 21-ago 367,00; "
        "ultimo precio 24-ago 369,49 (barra parcial).", "cuerpo"))
    out.append(M.p(
        "<b>Motor de valoracion:</b> script propio, DCF convencional a 10 anos con senda lineal "
        "decreciente, terminal Gordon, r = 9,69%, deuda neta 1.327 M, 273,537 M acciones. Prueba de "
        "coherencia MoS = 0 &rarr; TIR = 9,690% (cumple). Reproduce la matriz del diablo al dolar y "
        "las salidas del angel dentro del 1%.", "cuerpo"))
    out.append(M.p(
        "<b>Accesiones EDGAR citadas:</b> 0000896878-24-000009 &middot; -24-000024 &middot; "
        "-24-000030 &middot; -24-000035 &middot; -24-000045 &middot; -25-000009 &middot; -25-000020 "
        "&middot; -25-000031 &middot; -25-000035 (10-K FY2025) &middot; -26-000024 (8-K Q3 FY2026) "
        "&middot; -26-000025 (10-Q Q3 FY2026).", "cuerpo"))
    out.append(Spacer(1, 8))
    out.append(M.p("<b>Pendientes que este documento genera y que alguien tiene que cerrar:</b>",
                   "h3"))
    pend = [
        "Cinco tareas para el verificador (§6, D1.1 a D1.5). La tarea 3 se usa manana.",
        "Corregir gates.md: encender el trigger de drawdown de INTU (&minus;48,1%) y reescribir el "
        "umbral del gate de INTU, que mide un agregado contaminado (§6, cargo decisivo del angel).",
        "Reescribir la Pierna 5 del pre-compromiso apuntando a Credit Karma &mdash; despues del "
        "25-ago, nunca antes.",
        "Re-correr la ficha de seis puertas de INTU (C-9, pendiente desde el 21-ago) antes del "
        "21-sep, con la consecuencia de nivel ya pre-comprometida en §6.",
        "Registrar en diario-decisiones.md, el mismo dia de la ejecucion, la venta y la nota de que "
        "la razon escrita del aplazamiento del 22-ago no era la correcta.",
        "Sembrar la fila de libro-omisiones.md de §8.",
    ]
    for i, p in enumerate(pend, 1):
        out.append(M.p(f"{i}. {p}", "cuerpo"))

    out.append(Spacer(1, 14))
    out.append(M.hr())
    out.append(M.p('<font size="10" color="#C60C2A"><b>[CADUCA: 2026-09-21]</b></font>', "cuerpo"))
    return out
