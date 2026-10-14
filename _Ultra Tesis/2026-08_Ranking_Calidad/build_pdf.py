# -*- coding: utf-8 -*-
import sys, json, os, html
sys.path.insert(0, "/Users/felipealvarez/Library/Mobile Documents/com~apple~CloudDocs/INVESTMENTS/Skills/economist-qg/scripts")
import motor_qg as M
from reportlab.platypus import Spacer, PageBreak, KeepTogether
from reportlab.lib.units import cm

D = json.load(open("ultratesis_material.json"))
F = {x["ticker"]: x for x in D["fichas"]}

ORD = [("RMS.PA",1,1,0.35,"ALTA"),("V",2,2,0.53,"ALTA"),("MA",3,3,0.93,"ALTA"),("MSFT",4,3,1.28,"ALTA"),
("ASML",5,3,2.25,"MEDIA"),("SPGI",6,3,1.60,"ALTA"),("CSU.TO",7,4,1.06,"ALTA"),("GOOGL",8,4,3.30,"MEDIA"),
("CME",9,5,3.27,"MEDIA"),("AAPL",10,5,1.39,"ALTA"),("VRSK",11,5,1.77,"ALTA"),("REL.L",12,5,1.28,"ALTA"),
("TYL",13,5,3.89,"MEDIA"),("AMZN",14,6,2.96,"MEDIA"),("CDNS",15,6,0.93,"ALTA"),("VEEV",16,6,6.89,"BAJA"),
("VLTO",17,6,1.85,"ALTA"),("WST",18,6,7.63,"BAJA"),("ICE",19,7,4.42,"MEDIA"),("TSM",20,7,7.40,"BAJA"),
("IDXX",21,7,4.09,"MEDIA"),("SNPS",22,7,4.73,"BAJA"),("ISRG",23,7,3.40,"ALTA"),("DSY.MI",24,8,4.23,"MEDIA"),
("SYK",25,8,4.03,"MEDIA"),("CW",26,8,4.63,"MEDIA"),("DB1.DE",27,8,6.01,"BAJA"),("4684.T",28,8,9.70,"BAJA"),
("JNJ",29,8,5.42,"MEDIA"),("BKNG",30,9,3.27,"ALTA"),("NOW",31,9,5.01,"MEDIA"),("MANH",32,9,7.63,"BAJA"),
("NVDA",33,9,4.96,"BAJA"),("MSCI",34,10,2.07,"ALTA"),("AVGO",35,10,8.40,"BAJA"),("DSG.TO",36,10,7.00,"BAJA"),
("INTU",37,10,4.10,"MEDIA"),("RHHBY",38,10,6.19,"BAJA"),("NFLX",39,10,7.50,"BAJA"),("HUBB",40,10,3.81,"MEDIA")]

NIV = {
 1:("Nadie le puede quitar el negocio","No se le encontró ni un solo enemigo posible: ni una tecnología, ni una ley, ni un cliente con poder para apretarle."),
 2:("Para irse habría que mover a dos multitudes a la vez","Su fuerza es que está en medio de dos grupos enormes que dependen el uno del otro, y nadie manda sobre los dos."),
 3:("Manda en su precio","Tiene un candado fuerte y, además, es ella quien decide lo que cobra. Nadie se lo discute desde fuera."),
 4:("Grande, y con una sola puerta abierta","Puede reinvertir mucho dinero a buen retorno, pero cada una tiene exactamente un flanco por donde le pueden entrar."),
 5:("Cobra un peaje que no baja","El cliente pasa por su caja todos los días y la tarifa lleva años plana o subiendo. Aburrido y muy difícil de romper."),
 6:("Su candado lo pone un tercero que no cambia de opinión","Lo que protege a estas empresas no lo decidieron ellas: lo decidió un regulador, una fábrica de chips o un expediente sanitario."),
 7:("Fuerte, pero con una grieta que ya se ve en las cuentas","El negocio sigue siendo bueno. Pero el deterioro ya no es una sospecha: está publicado en sus propios informes."),
 8:("Cuesta cambiarles, pero no es imposible","Salir de estas empresas es caro y molesto para el cliente. Caro y molesto no es lo mismo que impensable."),
 9:("Foso grande con alguien afilando la pala","Son negocios muy buenos con un enemigo concreto, vivo y con nombre, trabajando ahora mismo en saltárselo."),
 10:("La cola: o el precio lo fija otro, o el foso hay que recomprarlo","Aquí están las que dependen de que un cliente poderoso no apriete, o las que tienen que comprar su ventaja otra vez cada pocos años."),
}
EMO = {"ALTA":"Alto","MEDIA":"Medio","BAJA":"Bajo"}

def esc(t):
    return html.escape(str(t or "")).replace("&#x27;","'")

M.configurar(titulo="LAS CUARENTA EMPRESAS MÁS DURADERAS",
             badge="RANKING DE CALIDAD",
             pie="Ranking de calidad · agosto de 2026",
             cabecera="RANKING DE CALIDAD · AGOSTO 2026")
doc = M.Doc("/tmp/RANKING_CALIDAD_2026-08.pdf")
fl = []

# ── PORTADA ──
fl += M.flag_titulo("Las cuarenta empresas más duraderas del mundo",
    "Cuáles seguirán ganando dinero de verdad dentro de diez años, por qué, y qué podría estropearlo")
fl.append(M.p("<b>Este documento no dice qué comprar.</b> Dice qué empresas tienen más probabilidades de "
  "seguir siendo excelentes en 2036, que es una pregunta distinta y anterior. Una empresa magnífica puede "
  "estar carísima hoy; este trabajo no mira el precio ni una sola vez. Eso se hace aparte y después."))
fl.append(Spacer(1,8))
fl.append(M.kpi_panel([("40","EMPRESAS ANALIZADAS","de un universo inicial de 60"),
  ("8","JUECES INDEPENDIENTES","cada uno a ciegas, sin ver a los demás"),
  ("10","NIVELES DE CALIDAD","dentro de cada nivel no hay orden")]))
fl.append(Spacer(1,12))
fl.append(M.callout("PAUSA REFLEXIVA",
  "La pregunta que se hicieron los ocho jueces, una y otra vez, fue siempre la misma: "
  "<b>si tuviera que elegir entre estas dos empresas para que siguiera existiendo y ganando dinero dentro "
  "de diez años, ¿cuál elijo?</b> Nada más. Ni el precio, ni las modas, ni lo que ha subido este año."))

fl.append(PageBreak())

# ── CÓMO SE HIZO ──
fl.append(M.p("Cómo se ha hecho esto, y por qué puede fiarse", "h_seccion"))
fl.append(M.p("Un método antiguo se tiró a la basura. Éste se puso a prueba antes de usarlo.", "h_sub"))
fl.append(M.p("Durante meses, este ranking se hacía sumando once reglas: se le daba una nota a cada empresa "
  "en cada regla, se sumaba todo y salía un número. En julio se auditó ese método con sus propios datos y "
  "el resultado fue demoledor: <b>de cada diez parejas de empresas, en siete el método decía «ésta es mejor "
  "que aquélla» sin poder demostrarlo</b>. Las once reglas resultaron ser, en la práctica, una sola regla "
  "disfrazada. Se retiró."))
fl.append(M.p("Lo que se usa ahora es más simple y funciona mucho mejor: <b>en vez de puntuar, se compara</b>. "
  "Ocho jueces independientes, cada uno trabajando a ciegas y sin ver el trabajo de los otros, van "
  "resolviendo parejas: ¿ésta o aquélla? Como quien ordena una estantería de libros cogiéndolos de dos en "
  "dos, en lugar de darle una nota del uno al diez a cada uno."))
fl.append(M.chart("charts/g2_instrumento.png", 15.6))
fl.append(M.p("Y para saber si el resultado era fiable, se hizo la prueba que de verdad importa: <b>se repitió "
  "el ejercicio entero con cuatro jueces distintos que no habían visto nada del primer grupo</b>. Si las dos "
  "listas hubieran salido diferentes, este documento no existiría. Salieron prácticamente idénticas: la "
  "coincidencia entre ambas fue del 0,97 sobre 1 <i>(donde 1 sería que las dos listas son exactamente "
  "iguales y 0 que no tienen nada que ver)</i>."))
fl.append(M.callout("LECCIÓN TRANSFERIBLE",
  "<b>Un juez suelto se equivoca; ocho jueces promediados, mucho menos.</b> Cada juez por separado "
  "coincidía con los demás sólo un 0,87 sobre 1. Pero al promediar los cuatro de cada grupo, la coincidencia "
  "entre grupos subió a 0,97. Es la misma razón por la que se pide opinión a varios médicos y no a uno."))
fl.append(M.p("<b>Lo que este método sigue sin poder hacer.</b> No hay ni un solo dato de rentabilidad futura "
  "aquí dentro: esto mide <i>en qué están de acuerdo ocho jueces sobre la durabilidad de un negocio</i>, no "
  "la verdad. Un grupo puede equivocarse entero y a la vez. Un ranking hecho en 2016 habría puesto a Intel "
  "en lo más alto por unanimidad."))

fl.append(PageBreak())

# ── EL CUADRO ──
fl.append(M.p("El cuadro completo", "h_seccion"))
fl.append(M.p("Las cuarenta, de la más duradera a la menos. El número de la izquierda ordena; el que manda es el nivel.", "h_sub"))
fl.append(M.callout("PAUSA REFLEXIVA",
  "<b>Dentro de cada nivel, el orden no significa nada.</b> Que una empresa aparezca dos puestos por encima "
  "de otra no quiere decir que sea mejor: quiere decir que el método no las sabe separar. Sólo son "
  "diferentes de verdad las que están en niveles distintos. Y la última columna avisa de cuánto se fiaron "
  "los jueces de cada puesto."))
rows = [["#","Niv.","Empresa","Qué es, en una línea","Acuer&shy;do"]]
for t,p_,n,s,c in ORD:
    f = F.get(t, {})
    rows.append([str(p_), str(n), f"<b>{esc(f.get('nombre_llano',t))}</b><br/><font size='6.8' color='#7A7A72'>{esc(t)}</font>",
                 esc(f.get("en_una_frase","")), EMO[c]])
fl.append(M.tabla(rows, [0.85*cm, 1.0*cm, 3.45*cm, 9.15*cm, 1.95*cm], font_sz=7.4))

fl.append(PageBreak())
fl.append(M.p("Cuánto se fían los jueces de cada puesto", "h_seccion"))
fl.append(M.p("Cuanto más larga es la barra, menos se pusieron de acuerdo entre ellos.", "h_sub"))
fl.append(M.chart("charts/g1_escalera.png", 15.2))

fl.append(PageBreak())
fl.append(M.p("Qué cambió en cuatro semanas", "h_seccion"))
fl.append(M.p("Y por qué los cambios son señal y no ruido.", "h_sub"))
fl.append(M.p("Entre el ranking de julio y éste de agosto, algunas empresas se movieron mucho. Eso podría ser "
  "simple capricho, así que se comprobó: <b>la lista cambió más en cuatro semanas de lo que cambia cuando "
  "se vuelve a medir el mismo día</b>. Es decir, los movimientos son reales. Y cada uno tiene detrás un dato "
  "que la propia empresa publicó, no una impresión."))
fl.append(M.chart("charts/g3_movimientos.png", 15.6))
fl.append(M.callout("CASO HISTÓRICO",
  "<b>MSCI cayó veintiún puestos, y es el ejemplo más limpio.</b> En enero firmó con su mayor cliente "
  "—BlackRock, el gestor de fondos más grande del mundo— un contrato nuevo en el que <b>lo que MSCI cobra "
  "queda atado a lo que BlackRock decida cobrarle a sus propios clientes</b>. Cada vez que BlackRock baje "
  "sus comisiones para competir, la tarifa de MSCI baja con ella, automáticamente, hasta 2035. Dejó de "
  "decidir su propio precio sin dejar de ser un gran negocio."))

fl.append(PageBreak())

# ── LAS FICHAS ──
fl.append(M.p("Las cuarenta, una por una", "h_seccion"))
fl.append(M.p("Qué hace cada empresa, por qué sus clientes no se van, y quién podría arruinarle la fiesta.", "h_sub"))

last = None
for t,p_,n,s,c in ORD:
    f = F.get(t)
    if not f: continue
    blk = []
    if n != last:
        tit, sub = NIV[n]
        blk.append(Spacer(1,6))
        blk.append(M.p(f"NIVEL {n} · {esc(tit)}", "h2"))
        blk.append(M.p(f"<i>{esc(sub)}</i>", "nota"))
        blk.append(M.hr())
        last = n
    blk.append(M.p(f"{p_}. {esc(f.get('nombre_llano',t))} <font size='8' color='#7A7A72'>· {esc(t)} · acuerdo entre jueces: {EMO[c].lower()}</font>", "h3"))
    blk.append(M.p(f"<b>A qué se dedica.</b> {esc(f.get('que_hace'))}"))
    blk.append(M.p(f"<b>La imagen que lo explica.</b> <i>{esc(f.get('metafora'))}</i>"))
    blk.append(M.p(f"<b>Por qué sus clientes no se van.</b> {esc(f.get('por_que_dura'))}"))
    blk.append(M.p(f"<b>El número que lo demuestra.</b> {esc(f.get('el_dato'))}"))
    blk.append(M.p(f"<b>Quién podría quitárselo.</b> {esc(f.get('quien_puede_quitarselo'))}"))
    blk.append(M.p(f"<b>El pero.</b> {esc(f.get('el_pero'))}"))
    blk.append(M.p(f"<i>En una frase: {esc(f.get('en_una_frase'))}</i>", "nota"))
    blk.append(Spacer(1,4))
    fl.append(KeepTogether(blk) if len(blk) < 10 else blk[0])
    if len(blk) >= 10:
        for x in blk[1:]: fl.append(x)

fl.append(PageBreak())
fl.append(M.p("Lo que se corrigió al revisar", "h_seccion"))
fl.append(M.p("Cuatro auditores volvieron a los documentos originales y encontraron errores. Aquí están.", "h_sub"))
fl.append(M.p("Antes de escribir este documento se hizo una segunda pasada: cuatro revisores independientes "
  "descargaron los informes originales de las empresas y comprobaron una por una las cifras, las fechas y "
  "las citas. <b>Encontraron quince errores.</b> Los más importantes:"))
for tit, txt in [
 ("Microsoft — la cifra estaba desfasada por su propia fuente",
  "Se decía que su asistente de inteligencia artificial tenía 20 millones de usuarios de pago. El mismo día "
  "del informe que se citaba, la empresa anunció que había superado <b>los 30 millones</b>. El argumento de "
  "«adopción floja» se debilita bastante: pasar de 20 a 30 millones en un trimestre es su mayor salto."),
 ("Apple — el pleito ya se falló, y en sentido contrario",
  "Se daba por pendiente el recurso del caso Epic. Se resolvió el <b>11 de diciembre de 2025</b>, y el "
  "tribunal <b>anuló en parte</b> justo la orden en la que se apoyaba el argumento."),
 ("Visa — se comparaban dos cosas distintas",
  "Se afirmaba que su margen había subido del 64,3% al 66,4%. Medido igual en los dos años, <b>bajó ocho "
  "décimas</b>. El argumento de fondo se sostiene, pero la comparación estaba mal hecha."),
 ("Alphabet — el porcentaje era menor",
  "Se decía que el 78% de su beneficio venía de revalorizaciones de inversiones no vendidas. La cifra "
  "correcta es <b>el 65%</b>."),
 ("CME — una inferencia presentada como hecho",
  "Se afirmaba que los dueños de un competidor tienen derecho de veto en el consejo de CME. El documento "
  "citado <b>no dice eso en ningún punto</b>: era una deducción, no un dato."),
]:
    fl.append(M.p(f"<b>{tit}.</b> {txt}"))
fl.append(M.callout("LECCIÓN TRANSFERIBLE",
  "Que una revisión encuentre quince errores no significa que el trabajo fuera malo: significa que la "
  "revisión funciona. <b>El problema no son los documentos que tienen erratas corregidas; son los que nunca "
  "se han vuelto a mirar.</b>"))

fl.append(PageBreak())
fl.append(M.p("Las tres advertencias", "h_seccion"))
fl.append(M.p("Lo que este documento no puede hacer, dicho antes de que nadie lo use para decidir.", "h_sub"))
for tit, txt in [
 ("Mide acuerdo, no verdad",
  "No hay aquí ni un solo dato de rentabilidad futura. Ocho jueces coinciden en que estas empresas son "
  "duraderas; eso no las hace duraderas. Un ranking hecho en 2016 habría puesto a Intel arriba por "
  "unanimidad, y con los mismos argumentos de calidad que hoy parecen impecables."),
 ("Los ocho jueces se parecen entre sí",
  "Comparten forma de razonar, así que coinciden más de lo que coincidirían ocho personas distintas. Y hay "
  "un detalle incómodo: <b>las empresas donde más coincidieron son justamente donde un error compartido "
  "sería invisible</b>. El acuerdo alto tranquiliza, y no debería del todo."),
 ("No dice absolutamente nada del precio",
  "La número uno puede estar impagable y la número cuarenta puede estar regalada. Este documento responde a "
  "«¿cuál durará?», no a «¿cuál comprar?». Son dos preguntas distintas y mezclarlas es el error más caro "
  "que se puede cometer con una lista como ésta."),
]:
    fl.append(M.p(f"<b>{tit}.</b> {txt}"))

doc.build(fl)
print("PDF OK:", os.path.getsize("/tmp/RANKING_CALIDAD_2026-08.pdf"), "bytes")
