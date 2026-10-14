# -*- coding: utf-8 -*-
"""Genera la Ultra Tesis ADBE en HTML formato casa (Economist), autocontenido (charts base64)."""
import base64, html as H
import dcf_adbe as D

def img(name):
    b = base64.b64encode(open(f"charts/{name}.png","rb").read()).decode()
    return f'<img src="data:image/png;base64,{b}" alt="{name}">'

def flag(t, sub):
    return f'<div class="flag"></div><h2>{t}</h2><p class="sub">{sub}</p>'

def tabla(rows, head=True):
    o = ['<div class="tw"><table>']
    for i,r in enumerate(rows):
        tag = "th" if (i==0 and head) else "td"
        o.append("<tr>"+"".join(f"<{tag}>{c}</{tag}>" for c in r)+"</tr>")
    o.append("</table></div>")
    return "".join(o)

def callout(tipo, txt):
    cls = {"PAUSA REFLEXIVA":"pausa","LECCIÓN TRANSFERIBLE":"leccion","CASO HISTÓRICO":"caso"}[tipo]
    return f'<div class="callout {cls}"><div class="ct">{tipo}</div><div class="cb">{txt}</div></div>'

def dot(c):
    return f'<span class="dot {c}"></span>'

es = D.es
P = D.PRECIO; PWFV = D.PWFV
S = []  # secciones (html)

# ── PORTADA ──────────────────────────────────────────────────────────────
S.append(f'''<div class="portada">
  <div class="pnombre">ADOBE INC.</div>
  <div class="ptick">NASDAQ: ADBE · Software de creación y experiencia digital</div>
  <div class="ptag">El mercado ha decidido que la inteligencia artificial matará a Adobe. Los números
   dicen que, por ahora, Adobe está monetizando la inteligencia artificial — y cotiza como si nunca
   más fuera a crecer.</div>
  <div class="kpis">
    <div class="kpi"><div class="kv">{D.SCORE_QG:.0f}/100</div><div class="kl">CALIDAD QG</div><div class="ks">tier Sólida · raw 91/125</div></div>
    <div class="kpi"><div class="kv">US${PWFV}</div><div class="kl">VALOR (PWFV)</div><div class="ks">vs US${int(P)} hoy</div></div>
    <div class="kpi"><div class="kv">{es(D.DCTO_PWFV,0).replace("-","−")}%</div><div class="kl">ZONA: {D.ZONA_HOY}</div><div class="ks">P/FCF 8,9x · fwd P/E 8,6x</div></div>
  </div>
  <div class="meta"><b>2 de julio de 2026</b> &nbsp;·&nbsp; Precio US${int(P)} &nbsp;·&nbsp; Horizonte 5-10 años
   &nbsp;·&nbsp; Posición: candidato nuevo (sin posición)</div>
  <div class="pfoot">Documento de convicción. Eje CALIDAD (sistema QG de 11 reglas) y eje PRECIO
   (VAL-MOS: PWFV-Valor, MoS por tier, detector de trampas) calculados por separado y cruzados al
   final. Uso personal; no es asesoría de inversión.</div>
</div>''')

# ── RESUMEN ──────────────────────────────────────────────────────────────
S.append(flag("Resumen en treinta segundos","La pregunta operativa, tres números y un veredicto") +
 f'''<p><b>¿Está Adobe barata porque el mercado se equivoca, o barata porque la inteligencia artificial
 generativa está a punto de comoditizar la creación de contenido — su razón de ser?</b> Toda la tesis vive
 o muere en esa pregunta. El precio ha caído un 43% desde su máximo de US$453 (marzo 2025) hasta US${int(P)},
 un mínimo de siete años. <span class="tag">HECHO</span></p>''' +
 tabla([["El número","Qué dice"],
   ["P/FCF 8,9x · fwd P/E 8,6x","De-rating histórico: el mercado paga 8-9x lo que llegó a pagar 28-42x. <span class='tag'>HECHO</span>"],
   [f"g implícita +{es(D.G_IMPL,1)}%","El precio descuenta crecimiento casi nulo para una franquicia que aún crece a doble dígito. <span class='tag'>SUPUESTO</span>"],
   ["AI-first ARR &gt;US$500M, ×3","La monetización de IA (Firefly, GenStudio) se triplicó interanual; el P&amp;L todavía no la ve entera. <span class='tag'>HECHO</span>"]]) +
 f'''<p><b>Veredicto operativo.</b> Calidad QG {D.SCORE_QG:.0f}/100 (tier Sólida). PWFV-Valor US${PWFV} frente a
 US${int(P)}: zona <b>PRECIO JUSTO</b> ({es(D.DCTO_PWFV,0).replace("-","−")}%). El detector de trampas da <b>PASA</b>
 (0 de 6 señales estructurales): ingresos +13% récord, márgenes estables, ARR aún creciendo — no es Kodak. Pero con
 un WACC exigente ({es(D.WACC,1)}%, que castiga el riesgo de disrupción y el vacío de liderazgo) el precio de hoy no
 ofrece margen: el descuento ({D.DCTO_ABS}%) queda muy por debajo del 35% que exige un tier Sólida, y la asimetría
 ({D.ASIMETRIA:.1f}:1) es inferior al umbral 3:1. <b>Acción: VIGILAR, no comprar a US${int(P)}.</b> La compra se abre en
 OPORTUNIDAD (≤US${D.Z_OPORT}, tramo scout del 3%) y el peso pleno llega en GANGA (≤US${D.Z_GANGA}, donde la asimetría
 sube a {D.ASIM_GANGA:.1f}:1) y en el MoS pleno del 35% (US${D.MOS_PLENO}). El regalo aún no está en el precio.</p>''' +
 callout("PAUSA REFLEXIVA","Adobe es el primer caso donde tu filtro «reemplazable por IA» y tu filtro «ultra "
   "calidad a buen precio» apuntan en direcciones opuestas. Antes de leer una línea más: ¿qué dato concreto, "
   "verificable en los próximos cuatro trimestres, te haría concluir que la IA está destruyendo el negocio y no "
   "que Adobe lo está montando encima de la IA?"))

# ── CUADRO DE MANDO ──────────────────────────────────────────────────────
S.append(flag("Cuadro de mando trimestral","Ocho indicadores, su umbral de alarma, su color hoy") +
 tabla([["Indicador","Estado hoy","Umbral de alarma","●"],
   ["Digital Media ARR (crec.)","+11,5% FY25","&lt; 8% dos trimestres",dot("v")],
   ["ARR orgánico (guía)","~8,3% FY26 (recortado)","&lt; 6%",dot("a")],
   ["Margen operativo GAAP","~36-37%, estable","−300 pb en 8 trim.",dot("v")],
   ["AI-first ARR","&gt;US$500M, ×3 YoY","estancamiento 2 trim.",dot("v")],
   ["Net revenue retention","sana (no divulga cifra)","caída sostenida",dot("a")],
   ["Liderazgo (CEO/CFO)","doble transición abierta","salida sin sucesor &gt;12m",dot("r")],
   ["Brecha GAAP vs non-GAAP","~40% (SBC alto)","ampliándose",dot("a")],
   ["Precio vs PWFV",f"{es(D.DCTO_PWFV,0).replace('-','−')}% ({D.ZONA_HOY})","&gt; +15% (CARO)",dot("a")]]) +
 "<p><b>Lectura del patrón.</b> El motor económico está en verde (ARR, márgenes, IA); todos los ámbar y el único "
 "rojo se concentran en <i>gobernanza, durabilidad y precio</i>, no en rentabilidad. Es el perfil de una franquicia "
 "sólida en prueba de moat con el asiento del piloto a medio ocupar y cotizando en precio justo — ni un negocio que "
 "se deteriora por dentro, ni una ganga. Próxima revisión: Q3 FY2026 (septiembre 2026). <span class='tag'>HECHO</span></p>")

# ── VEREDICTO CUANTIFICADO ───────────────────────────────────────────────
vd = {"R1 · Escalabilidad":"Software puro, 89% margen bruto: escala casi sin coste marginal. Casi perfecto.",
 "R2 · Industria":"Creación y experiencia digital: secular, pero ahora con disrupción entrante.",
 "R3 · Liderazgo":"Estándar de facto (PDF, Creative), pero el liderazgo entró en disputa creíble.",
 "R4 · Moat":"Ancho (integración, formatos, hábito), pero en fase de prueba por IA-nativos.",
 "R5 · Crec. orgánico":"Doble dígito histórico; guía de ARR orgánico recortada a ~8,3%.",
 "R6 · Diversificación":"Dos motores (Media, Experience) y múltiples productos; concentración en Creative.",
 "R7 · Capital / ROIC":"ROIC ~40%+, pero recompras agresivas y Semrush a vigilar en asignación.",
 "R8 · Balance":"Fortaleza: caja, deuda neta trivial, FCF ~US$10B. Casi impecable.",
 "R9 · Transparencia":"Brecha GAAP/non-GAAP ~40% por SBC: bandera roja de transparencia.",
 "R10 · Gestión":"Track record excelente, pero doble vacío CEO+CFO en el peor momento.",
 "R11 · Impacto":"Neutro; sin narrativa de impacto diferencial. Punto más bajo."}
rr = [["Regla","Puntos","Veredicto en una línea"]]
for n,pts,mx in D.REGLAS: rr.append([n,f"{pts}/{mx}",vd[n]])
rr.append([f"<b>TOTAL</b>",f"<b>{D.RAW_QG}/125</b>",f"<b>{D.SCORE_QG:.1f}/100 · tier Sólida</b>"])
S.append(flag("El veredicto cuantificado","Las once reglas Quality Growth, sin perdonar la que falla") +
 f'<div class="chart">{img("01_radar")}</div>' + tabla(rr) +
 callout("LECCIÓN TRANSFERIBLE","El score es un filtro, no un veredicto. 72,8/100 no dice «compra»; dice «negocio "
   "de calidad sólida cuya variable más importante — la durabilidad del moat — acaba de entrar en prueba». Un score "
   "que ignorara R3/R4/R10 y solo mirara el motor económico (89% margen, ROIC 40%) daría «Núcleo» y te haría pagar "
   "de más. La disciplina está en dejar que la regla que falla pese."))

# ── §1..§11 (prosa condensada fiel) ─────────────────────────────────────
S.append(flag("§1 · La historia detrás del veredicto","De la caja de software a la nube de la creación") +
 "<p>Adobe nació en 1982 vendiendo PostScript. De ahí salieron Photoshop, Illustrator y el PDF: no un producto, "
 "un <i>estándar</i>. En 2013 hizo la apuesta que define su calidad de hoy: mató la caja y forzó la suscripción de "
 "Creative Cloud. La acción se hundió, los usuarios protestaron — y luego el negocio se convirtió en la máquina de "
 "flujo de caja recurrente que es hoy. <span class='tag'>HECHO</span></p>"
 "<p>Esa historia ya ocurrió una vez: en 2013 el mercado creyó que Adobe destruía su negocio; en realidad lo "
 "blindaba. El paralelo con 2026 es exacto en la forma (transición dolorosa, escepticismo máximo) pero <b>no</b> en "
 "el fondo: en 2013 el enemigo era la fricción del propio modelo; en 2026 es externo — la IA generativa que fabrica "
 "imágenes, texto y vídeo sin abrir Photoshop. La pregunta no es si Adobe sabe reinventarse (lo demostró); es si esta "
 "vez la ola es más rápida que su capacidad de subirse encima. <span class='tag'>INFERENCIA</span></p>")

S.append(flag("§2 · Historia de mi posición","El espejo antes que el análisis") +
 "<p><b>Posición actual: ninguna.</b> Adobe entra como candidato nuevo del ranking QG (#16, tier Sólida). No hay "
 "coste hundido que defender ni P&amp;L que sesgue: la situación más limpia para decidir. <span class='tag'>HECHO</span> "
 "(verificación en IBKR pendiente; esta sesión no tiene acceso en vivo al bróker.)</p>"
 "<p>El riesgo aquí no es el sesgo de propiedad, es el <b>sesgo de gorra de superinversor</b>: media comunidad de "
 "calidad compra Adobe «porque está barata y es Adobe». Ese es el coattailing que tu propio sistema prohíbe. Si la "
 "compras, que sea por el dato verificable, no porque otros la compren. Y el tamaño lo manda el tier Sólida (techo "
 "~4-5% del patrimonio, en tramos), no la convicción emocional. <span class='tag'>INFERENCIA</span></p>")

S.append(flag("§3 · El modelo de negocio en dos minutos","La prueba de Lynch: ¿lo entiende un niño?") +
 "<p>Adobe cobra un peaje mensual por las herramientas con las que el mundo fabrica y gestiona contenido digital. "
 "Dos motores. <b>Digital Media</b> (US$17,7B, el 75%): Creative Cloud (Photoshop, Illustrator, Premiere) y Document "
 "Cloud (Acrobat, el PDF). <b>Digital Experience</b> (US$5,9B): software para que las grandes marcas midan y "
 "personalicen la experiencia de sus clientes. El volante: cuanto más contenido se crea en Adobe, más hay que "
 "gestionar, medir y volver a editar en Adobe. <span class='tag'>HECHO</span></p>" +
 f'<div class="chart">{img("02_segmentos")}</div>' +
 "<p>La economía es de las mejores del planeta: 89% de margen bruto, ~36% operativo GAAP (~46% non-GAAP) y un FCF de "
 "US$9,9B sobre US$23,5B — 42 centavos de cada dólar se vuelven caja. No hay compresión estructural de márgenes: la "
 "supuesta muerte por IA todavía no aparece en la cuenta de resultados. <span class='tag'>HECHO</span></p>" +
 f'<div class="chart">{img("07_margenes")}</div>')

S.append(flag("§4 · Las reglas aplicadas con bisturí","Dónde brilla, dónde sangra") +
 "<p><b>Bloque económico (R1, R2, R7, R8): sobresaliente.</b> Escalabilidad de software puro, ROIC ~40%+, balance "
 "de fortaleza (caja US$5,6B, deuda neta trivial). Si Adobe se puntuara solo por su motor, sería Núcleo. "
 "<span class='tag'>HECHO</span></p>"
 "<p><b>Bloque de durabilidad (R3, R4): en prueba.</b> Aquí está la tesis. Liderazgo (9/15) y moat (11/15) enfrentan "
 "por primera vez retadores creíbles: Figma, Canva (US$4B ARR, +35%) y los modelos generativos. El sistema no "
 "perdona: estas dos reglas cargan la mayor parte de la distancia entre el 72,8 real y el 85+ de una franquicia "
 "intacta. <span class='tag'>INFERENCIA</span></p>"
 "<p><b>Bloque de gobernanza (R5, R9, R10): las banderas.</b> R5 por el recorte de guía de ARR orgánico a ~8,3% y el "
 "giro a freemium; R9 por la brecha GAAP/non-GAAP de ~40% (SBC); R10 por la doble transición CEO+CFO. Ninguna es "
 "knock-out; juntas explican por qué esto es Sólida y no Alta convicción. <span class='tag'>HECHO</span></p>" +
 callout("LECCIÓN TRANSFERIBLE","La regla que falla es la que hay que mirar, no la que brilla. El instinto dice «89% "
   "de margen, cómprala». La disciplina dice «el moat entró en prueba y el piloto se está bajando: paga menos y trae "
   "menos». El precio de una franquicia en prueba de moat tiene que incorporar esa prueba."))

S.append(flag("§5 · El moat","Capas de defensa, de la piel al hueso") +
 tabla([["Capa de foso","Qué la sostiene","Años"],
   ["Formatos estándar (PDF, PSD)","El mundo guarda archivos en ellos; coste de cambio brutal","10-15+"],
   ["Hábito y currículo profesional","Se enseña Adobe; el CV pide Photoshop","8-12"],
   ["Integración de suite","El flujo Creative↔Document↔Experience no se replica por partes","6-10"],
   ["Datos y distribución empresarial","Contratos, GenStudio, relaciones con grandes marcas","5-8"],
   ["Marca en creación","Sinónimo de profesionalidad; opción por defecto","5-8, erosionable"]]) +
 "<p>Las capas profundas (formatos, hábito) son las que más aguantan y las que la IA no toca directamente. Las "
 "superficiales (marca, primera opción) son las que la IA-nativa erosiona primero: un adolescente que empieza en "
 "Canva puede no llegar nunca a Photoshop. El moat no se rompe de golpe; se pela por fuera. <span class='tag'>INFERENCIA</span></p>" +
 callout("PAUSA REFLEXIVA","¿Qué capa se erosiona primero y qué señal la delata? La «marca / primera opción», y la "
   "señal es la retención neta de ingresos en la cohorte de clientes nuevos — no el ARR agregado, que va con retraso. "
   "Si la cohorte joven deja de convertir a pago, el foso se está pelando aunque el ARR total suba un año más."))

S.append(flag("§6 · El campo de batalla competitivo","El frente que decide la década") +
 f'<div class="chart">{img("04_competencia")}</div>' +
 "<p><b>Frente 1 — masas (Canva).</b> US$4B de ARR creciendo 35%; se comió el segmento no profesional. Respuesta: "
 "Express + freemium para 850M de usuarios. <b>Frente 2 — generación (Firefly vs Midjourney/Sora/Google).</b> El "
 "decisivo: cada mejora de Sora es una razón menos para pagar Creative Cloud, pero Firefly es la propia arma de Adobe "
 "(AI-first ARR &gt;US$500M, ×3). <b>Frente 3 — profesional (Figma, GenStudio).</b> Adobe intentó comprar Figma por "
 "US$20B; los reguladores lo bloquearon (2023) y pagó US$1B de ruptura. <span class='tag'>HECHO</span></p>"
 "<p><b>La síntesis que importa:</b> el frente que decide la década es el 2. Si Firefly monetiza la IA más rápido de "
 "lo que Sora/Google comoditizan la creación, la valoración de hoy es un regalo; si es al revés, es una trampa lenta "
 "tipo Kodak. Y ese frente <b>no</b> se lee en el ARR agregado; se lee en la economía del contrato marginal. <span class='tag'>INFERENCIA</span></p>" +
 callout("CASO HISTÓRICO","Kodak inventó la cámara digital y murió: no por falta de tecnología, sino porque su "
   "economía (rollo de película) era incompatible con el nuevo mundo. Adobe tiene la ventaja opuesta: su economía "
   "(suscripción a herramientas) es <i>compatible</i> con la IA — Firefly es una función más de la suscripción, no un "
   "producto que canibaliza un margen físico. La analogía correcta no es Kodak; es Microsoft metiendo Copilot dentro "
   "de Office. Pero hay que ganársela con datos de monetización, no asumirla."))

S.append(flag("§7 · TAM, runway y catalizadores","Cuánto mercado queda y qué lo enciende") +
 tabla([["Vector","Hoy","2030E","Nota"],
   ["TAM total (Adobe)","~US$205B","~US$290B+","Creatividad + documentos + experiencia + IA"],
   ["ARR total Adobe","US$27,1B","US$45-55B","Penetración de un solo dígito sobre el TAM"],
   ["Usuarios monetizables","~40M pagados","de 850M MAU","El runway del giro freemium"],
   ["AI-first ARR","&gt;US$0,5B","US$5B+ posible","La opción gratis en el precio de hoy"]]) +
 f'<div class="chart">{img("20_runway")}</div>' +
 "<p>El giro a freemium recorta el ARR de corto plazo para meter en el embudo a cientos de millones de usuarios que "
 "la IA hace posible servir barato: sembrar hoy para monetizar mañana — o una concesión defensiva ante Canva. La "
 "diferencia la dará la conversión de esa base, no el titular del ARR. <b>Catalizadores por materialidad:</b> (1) "
 "nombramiento de CEO; (2) AI-first ARR cruzando US$1B; (3) reaceleración del ARR orgánico &gt;10%; (4) monetización "
 "de Firefly en empresa vía GenStudio. <span class='tag'>INFERENCIA</span></p>" +
 f'<div class="chart">{img("15_demanda")}</div>')

S.append(flag("§8 · Valoración","Cinco supuestos desnudos y un valor con banda honesta") +
 f"<p><b>Supuesto #1 (el más interrogado): owner earnings.</b> Parto del FCF de US$9,85B (FY2025) y resto el 100% "
 f"del SBC (US$1,95B), estilo Damodaran. Resultado: US$7,9B, US${D.OE_PS:.1f} por acción. A US${int(P)}, eso es 11,1x — "
 f"muy por debajo del techo de 25x del tier Sólida. <span class='tag'>HECHO</span></p>" +
 f'<div class="chart">{img("05_cascada")}</div>' +
 f"<p><b>Supuesto #2: WACC.</b> Tasa libre {es(D.RF,1)}% + beta {es(D.BETA,2)} × prima {es(D.ERP,1)}% = {es(D.COE,2)}% "
 f"de coste de equity, ~{es(D.WACC,1)}% de WACC. Beta elevada a {es(D.BETA,2)} (vs ~1,25 histórico) para exigir de "
 f"forma explícita por el riesgo de disrupción y el vacío de liderazgo. <b>#3</b> crecimiento por escenario; <b>#4</b> "
 f"terminal ≤ min(3%, tasa libre); <b>#5</b> margen año 10 ≤ máximo histórico. <span class='tag'>SUPUESTO</span></p>" +
 f'<div class="chart">{img("17_wacc")}</div>' +
 f"<p>Tres escenarios: <b>Oso (35%)</b> la IA comoditiza; owner earnings <i>declinan</i> → US${D.V_OSO}. <b>Base "
 f"(45%)</b> compounder que decelera al ~7% → US${D.V_BASE}. <b>Toro (20%)</b> Firefly/GenStudio inflexionan → "
 f"US${D.V_TORO}. Probabilidad del oso deliberadamente alta: el moat está en prueba. <span class='tag'>SUPUESTO</span></p>" +
 f'<div class="chart">{img("08_dcf")}</div>' +
 f"<p><b>El ancla: PWFV-Valor = US${PWFV}.</b> Dos tercios de DCF ponderado (US${D.DCF_POND}) y un tercio de EPV "
 f"(US${D.EPV}, el valor sin crecimiento). El hallazgo: el EPV ya vale US${D.EPV}, solo un {es(D.PESO_CREC,0)}% por "
 f"debajo del precio. <b>El mercado paga apenas ~{es(D.PESO_CREC,0)}% del precio por todo el crecimiento futuro de "
 f"Adobe.</b> El resto lo justifica la franquicia congelada. <span class='tag'>INFERENCIA</span></p>" +
 f'<div class="chart">{img("18_sensibilidad")}</div>' +
 f"<p>Incluso en el cuadrante más severo (WACC {es(D.WACC_GRID[-1],1)}%, terminal 1,5%) el valor DCF base es "
 f"US${D.SENS_MIN} — por encima del precio. US${int(P)} solo se justifica si los owner earnings apenas crecen; el DCF "
 f"inverso lo cuantifica en <b>+{es(D.G_IMPL,1)}%/año a perpetuidad</b>. Para una franquicia con 89% de margen bruto, "
 f"US$27B de ARR contratado y monetización de IA triplicándose, un crecimiento casi nulo es extraordinario. <span class='tag'>INFERENCIA</span></p>" +
 f'<div class="chart">{img("10_multiplos")}</div>' +
 f"<p><b>Banda honesta.</b> El valor va de US${D.EPV} (EPV) a US${D.V_BASE} (DCF base) y US${D.V_TORO} (toro); el "
 f"PWFV de US${PWFV} es el punto ponderado. PEG &lt; 1 a fwd P/E 8,6x — barato en cualquier lectura, con la "
 f"advertencia de que el PEG sesga a favor de la calidad. <span class='tag'>INFERENCIA</span></p>" +
 f'<div class="chart">{img("09_zonas")}</div>' +
 f"<p><b>Zona hoy: PRECIO JUSTO ({es(D.DCTO_PWFV,0).replace('-','−')}% vs PWFV).</b> El MoS del 35% de un tier Sólida "
 f"es US${D.MOS_PLENO}. Y la asimetría con el oso honesto ({D.ASIMETRIA:.1f}:1) no llega al 3:1 hasta GANGA "
 f"(~US${D.Z_GANGA}, donde sube a {D.ASIM_GANGA:.1f}:1). Buen negocio, pero a US${int(P)} el precio de convicción está "
 f"más abajo. <span class='tag'>INFERENCIA</span></p>" +
 callout("LECCIÓN TRANSFERIBLE",f"Una banda de US${D.EPV} a US${D.V_TORO} no es imprecisión; es la forma correcta de "
   "decir «el desenlace depende de una variable binaria aún sin resolver». Cuando la banda es tan ancha, la respuesta "
   "no es un precio objetivo falso; es tamaño pequeño y compra en tramos que respeten la incertidumbre."))

S.append(flag("§9 · Gestión, cultura y gobernanza","El demérito sin maquillaje") +
 "<p>Shantanu Narayen dirigió Adobe 18 años: de menos de US$1B a más de US$25B de ingresos y el giro a la nube de "
 "2013. En marzo de 2026 anunció que se retira en cuanto haya sucesor (se queda de presidente). En junio, el CFO "
 "Daniel Durn dimitió con efecto inmediato. <b>Doble vacío de liderazgo en plena prueba de moat: la mayor bandera de "
 "esta tesis, sin maquillar.</b> <span class='tag'>HECHO</span></p>"
 "<p>Asignación de capital: recompras muy agresivas (US$11,3B en FY25, autorización de US$25B) que redujeron las "
 "acciones ~5,7% en un año — acumulativas con la acción barata. A vigilar: la compra de Semrush y el apetito de M&amp;A "
 "tras el veto a Figma; adquirir crecimiento inorgánico para tapar el orgánico sería la señal equivocada. <span class='tag'>HECHO</span></p>" +
 f'<div class="chart">{img("11_balance")}</div>' +
 callout("PAUSA REFLEXIVA","¿Cuánto del descuento de hoy es «IA» y cuánto es «no sé quién dirige esto en 2027»? Si "
   "una parte material del −43% es el vacío de liderazgo, el nombramiento de un CEO creíble es un catalizador de "
   "re-rating que no depende de ganar la guerra de la IA — solo de despejar la incertidumbre. Ese es el tipo de miedo "
   "con nombre y fecha de caducidad que el sistema premia."))

inv = [["Inversor","Veredicto (convicción /10)"],
 ["Graham","Precio bajo el valor de la franquicia sin crecer; margen existe pero exigiría más. (6)"],
 ["Buffett","Negocio maravilloso a precio razonable, pero «¿está el foso intacto?» sin respuesta aún. (7)"],
 ["Munger","Gran empresa a precio justo &gt; mediocre barata; el moat en prueba le baja la mano. (7)"],
 ["Fisher","Scuttlebutt: ¿los profesionales siguen abriendo Photoshop? Sí, por ahora. (6)"],
 ["Lynch","PEG &lt; 1 con marca conocida; «compra lo que usas». Pero vigilaría la desaceleración. (7)"],
 ["Templeton","Máximo pesimismo = mejor momento; el titular «la IA mata a Adobe» es su señal. (8)"],
 ["Marks","El precio es el control de riesgo; a 8x FCF el error está barato, no gratis. (6)"],
 ["Seilern","Calidad sólida, no núcleo; la durabilidad del moat — su variable clave — en duda. (6)"],
 ["Terry Smith","Buena compañía, no pagar de más: a 8-9x FCF no paga de más; el «no hacer nada» viene después. (7)"]]
S.append(flag("§10 · Nueve inversores legendarios opinan","La divergencia es la señal") +
 f'<div class="chart">{img("13_inversores")}</div>' + tabla(inv) +
 "<p>La divergencia es estrecha y reveladora: nadie dice «pasa» (todos ven la calidad y el precio) pero nadie dice "
 "«apuesta la casa» (todos ven el moat en prueba). El consenso implícito es el veredicto del sistema: comprar sí, en "
 "tamaño Sólida, con paciencia — y hoy, esperar a mejor precio. <span class='tag'>INFERENCIA</span></p>")

S.append(flag("§11 · Veredicto final, triggers y proyección","Qué hacer, a qué precio y qué lo rompería") +
 f"<p><b>VEREDICTO: VIGILAR — hoy en PRECIO JUSTO (US${int(P)}, {es(D.DCTO_PWFV,0).replace('-','−')}% vs PWFV US${PWFV}). "
 f"COMPRAR EN TRAMOS solo desde OPORTUNIDAD (≤US${D.Z_OPORT}).</b> Doble candado: <i>precio</i> (peso pleno solo en "
 f"GANGA) y <i>tamaño</i> (tier Sólida = techo ~4-5% del patrimonio). La tesis en una frase: <b>el mercado teme que la "
 f"IA comoditice la creación de contenido; ese miedo está mal dimensionado porque Adobe ya monetiza la IA (AI-first "
 f"ARR &gt;US$500M, ×3) mientras cotiza a 11x owner earnings con el mercado pagando casi cero por su crecimiento — pero "
 f"con un WACC exigente el descuento aún no basta para un tier Sólida.</b></p>" +
 tabla([["Zona","Precio","Acción"],
   ["PRECIO JUSTO (hoy)",f"US${D.Z_OPORT}-{D.Z_JUSTO_SUP}","No comprar. Vigilar con las órdenes de abajo ya escritas."],
   ["OPORTUNIDAD",f"US${D.Z_GANGA}-{D.Z_OPORT}","Tramo 1 scout, 3%. Convicción baja: asimetría aún &lt; 3:1."],
   ["GANGA",f"≤ US${D.Z_GANGA}",f"Tramo 2. Asimetría {D.ASIM_GANGA:.1f}:1 y MoS ~25%."],
   ["MoS pleno (35%)",f"≤ US${D.MOS_PLENO}","Tramo 3, peso pleno del tier. Regalo si la franquicia aguanta."]]) +
 "<p><b>Triggers de venta falsables</b> (regla Seilern: se vende por deterioro de negocio, nunca por múltiplo):</p>" +
 tabla([["#","Trigger","Umbral","Respuesta"],
   ["1","ARR orgánico se desploma","&lt; 6% dos trimestres","Re-correr tesis; reducir"],
   ["2","Retención de cohorte nueva cae","net revenue retention &lt; 100%","Salida ordenada (moat pelándose)"],
   ["3","Margen bruto se comprime","−300 pb en 8 trim.","Señal de comoditización; reducir"],
   ["4","Firefly/AI-first ARR se estanca","sin crecimiento 2 trim.","La IA es amenaza, no ingreso; salir"],
   ["5","M&amp;A para tapar el orgánico","compra grande de crecimiento","Revisar asignación de capital"]]) +
 callout("CASO HISTÓRICO","Teleperformance, 2024: ingresos aún creciendo, múltiplo por los suelos, «la IA nos mata». "
   "El sistema la marcó como posible mispricing por sus fundamentales trailing — y resultó TRAMPA: cayó otro 42% "
   "mientras el crecimiento orgánico real (no el ajustado) se hundía. Lección que Adobe hereda: «los ingresos aún "
   "crecen» es condición necesaria, jamás suficiente. Por eso los triggers 2 y 4 miran indicadores <i>adelantados</i> "
   "(retención de cohorte, ARR de IA), no el ARR agregado que va con retraso.") +
 f"<p><b>Pre-mortem (a 5 años, desde 2031).</b> «Adobe cotiza a US$120. La generación de contenido se volvió gratis y "
 f"buena; los profesionales siguieron pagando, pero la cohorte joven nunca convirtió. El ARR aguantó dos años por los "
 f"contratos legacy y luego rodó cuesta abajo. La señal temprana, ignorada, fue la retención de la cohorte nueva en "
 f"2026-27.» Probabilidad ~35% (mi escenario oso). El antídoto está en el trigger 2. <span class='tag'>SUPUESTO</span></p>" +
 f'<div class="chart">{img("19_eps")}</div>' +
 f"<p><b>Proyección (5 años, desde US${int(P)}).</b> Oso → US${D.V_OSO}. Base → US${D.V_BASE}. Toro → US${D.V_TORO}. "
 f"Valor esperado ponderado ≈ US${D.PROY_POND}, un +{D.RET_POND}% a cinco años antes de dividendos/recompras. La "
 f"asimetría del <i>setup</i> es real, pero a US${int(P)} la asimetría del <i>precio</i> ({D.ASIMETRIA:.1f}:1) aún no "
 f"compensa; por eso se vigila y el peso llega en GANGA. <span class='tag'>SUPUESTO</span></p>" +
 callout("PAUSA REFLEXIVA","El proceso por encima de la convicción: si dentro de un año Adobe está a US$150 y todos "
   "los triggers siguen verdes, ¿comprarás el tramo pleno con la misma calma con la que hoy lo escribes — o dejarás "
   "que el precio cayendo te convenza de que el mercado sabe algo que tú no? La regla anti-sesgo existe para ese día: "
   "no promediar a la baja sin re-verificar la tesis por escrito."))

# ── CIERRE ───────────────────────────────────────────────────────────────
S.append(flag("Glosario y advertencias","Términos y la letra pequeña") +
 tabla([["Término","Definición"],
   ["ARR","Ingreso recurrente anualizado; la suscripción convertida a base anual."],
   ["AI-first ARR","ARR de productos nativos de IA (Firefly, GenStudio, Acrobat AI Assistant)."],
   ["DCF inverso",f"Qué crecimiento implica el precio de hoy; aquí +{es(D.G_IMPL,1)}%/año (casi nulo)."],
   ["EPV","Earnings Power Value (Greenwald): valor de la franquicia SIN crecimiento = NOPAT / WACC."],
   ["MoS","Margen de seguridad; descuento del precio frente al valor intrínseco (PWFV)."],
   ["Owner earnings","FCF menos el 100% del SBC; la caja que de verdad queda para el dueño."],
   ["PWFV-Valor","Valor ponderado: dos tercios DCF + un tercio EPV. El ancla de zonas y MoS."],
   ["RPO","Obligaciones de desempeño pendientes; el backlog contratado no reconocido aún."]]) +
 "<p><b>Etiquetado.</b> HECHO = filing primario (10-K FY2025, release Q2 FY2026). INFERENCIA = derivado o de terceros. "
 "SUPUESTO = asunción del modelo (escenarios, probabilidades, WACC). Los tres escenarios del DCF y sus probabilidades "
 "son SUPUESTOS; el PWFV es tan bueno como ellos. <b>WACC 10,4%</b> (beta 1,45) elevado a propósito para exigir por el "
 "riesgo de disrupción/liderazgo. <b>Precio</b> US$220 (stockanalysis.com, 2-jul-2026; rango 52s US$190-387). "
 "<b>Posición</b> tratada como cero; verificación IBKR pendiente. <b>Naturaleza:</b> uso personal; no es asesoría; "
 "analiza, no ejecuta. <b>Actualización:</b> Q3 FY2026 (sep-2026) o si se dispara un trigger o cae &gt;20%.</p>")

# ── ENSAMBLADO HTML ──────────────────────────────────────────────────────
CSS = """
:root{--fondo:#FAF5E9;--panel:#F2ECDC;--rojo:#C60C2A;--rojosc:#8C1410;--navy:#1F3A52;
--azul:#2A5A7E;--verde:#6C7E48;--ocre:#B8860B;--tinta:#2A2A2A;--gris:#666054;--linea:#D2CCC0;}
*{box-sizing:border-box}
body{margin:0;background:var(--fondo);color:var(--tinta);font-family:Georgia,'Times New Roman',serif;line-height:1.62}
.wrap{max-width:860px;margin:0 auto;padding:26px 30px 90px}
.topbar{background:var(--rojo);height:9px;margin:-26px -30px 0}
h2{font-size:25px;font-weight:700;margin:6px 0 2px;letter-spacing:-.3px}
.sub{font-style:italic;color:var(--gris);margin:0 0 14px;font-size:15px}
.flag{width:46px;height:11px;background:var(--rojo);margin-top:34px}
section{border-top:1px solid var(--linea)}
section:first-of-type{border-top:none}
p{font-size:15px;margin:0 0 12px}
b{color:var(--tinta)}
.tag{font-family:Arial,sans-serif;font-size:9.5px;font-weight:700;color:#fff;background:var(--gris);
padding:1px 5px;border-radius:3px;vertical-align:middle;letter-spacing:.03em}
.tw{overflow-x:auto;margin:6px 0 16px}
table{width:100%;border-collapse:collapse;font-size:13.4px}
th{background:var(--navy);color:#fff;text-align:left;padding:7px 9px;font-family:Arial,sans-serif;
font-size:11px;text-transform:uppercase;letter-spacing:.04em;font-weight:700}
td{padding:6px 9px;border-bottom:1px solid var(--linea);vertical-align:top}
tr:nth-child(even) td{background:var(--panel)}
.chart{margin:14px 0 18px;text-align:center}
.chart img{max-width:100%;height:auto;border:1px solid var(--linea);border-radius:3px}
.callout{display:flex;margin:14px 0;border-radius:0 4px 4px 0;overflow:hidden}
.callout .cb{background:var(--panel);padding:11px 14px;font-style:italic;font-size:14px;flex:1}
.callout .ct{writing-mode:vertical-rl;transform:rotate(180deg);color:#fff;font-family:Arial,sans-serif;
font-weight:700;font-size:10px;padding:9px 6px;letter-spacing:.05em;text-align:center}
.pausa .ct{background:var(--rojo)} .leccion .ct{background:var(--verde)} .caso .ct{background:var(--navy)}
.pausa .cb{border-left:3px solid var(--rojo)} .leccion .cb{border-left:3px solid var(--verde)}
.caso .cb{border-left:3px solid var(--navy)}
.dot{display:inline-block;width:11px;height:11px;border-radius:50%}
.dot.v{background:var(--verde)} .dot.a{background:var(--ocre)} .dot.r{background:var(--rojosc)}
/* portada */
.portada{padding:40px 0 26px;border-bottom:2px solid var(--tinta)}
.pnombre{font-size:44px;font-weight:700;letter-spacing:-1px}
.ptick{color:var(--rojo);font-family:Arial,sans-serif;font-weight:700;font-size:14px;margin:2px 0 16px}
.ptag{font-style:italic;color:var(--gris);font-size:16px;max-width:640px;margin-bottom:22px}
.kpis{display:flex;gap:14px;flex-wrap:wrap;margin-bottom:18px}
.kpi{flex:1;min-width:180px;background:var(--panel);border:1px solid var(--linea);border-radius:5px;padding:15px;text-align:center}
.kv{font-size:26px;font-weight:700;color:var(--rojo)}
.kl{font-family:Arial,sans-serif;font-weight:700;font-size:11px;color:var(--navy);margin-top:3px}
.ks{font-style:italic;color:var(--gris);font-size:11.5px}
.meta{font-size:14px;border-top:1px solid var(--linea);border-bottom:1px solid var(--linea);padding:10px 0;margin:6px 0}
.pfoot{font-style:italic;color:var(--gris);font-size:11.5px}
.docfoot{margin-top:40px;border-top:1px solid var(--linea);padding-top:12px;color:var(--gris);
font-style:italic;font-size:12px;display:flex;justify-content:space-between}
"""
body = '<div class="topbar"></div><div class="wrap">'
for i,sec in enumerate(S):
    if i==0: body += sec  # portada
    else: body += f'<section>{sec}</section>'
body += ('<div class="docfoot"><span>Tesis Ultra · Quality Growth · uso personal · v2.0</span>'
         '<span>Adobe Inc. (NASDAQ: ADBE) · 2 de julio de 2026</span></div></div>')

doc = f'''<!doctype html><html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Ultra Tesis · Adobe (ADBE) · v2</title><style>{CSS}</style></head>
<body>{body}</body></html>'''

OUT = ("/Users/felipealvarez/Library/Mobile Documents/com~apple~CloudDocs/"
       "INVESTMENTS/_ACTIVE/Tesis_Ultra_ADBE_v2.html")
open(OUT,"w").write(doc)
print("HTML:", OUT, f"({len(doc)//1024} KB)")
