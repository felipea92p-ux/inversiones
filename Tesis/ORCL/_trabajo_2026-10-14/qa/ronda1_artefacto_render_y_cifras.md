

##### AGENTE a7e42362b5357d79d
RESUMEN: Revisé la página envuelta en 1280 y 400 px, tema claro y oscuro, con 17 capturas por sección y combinación (68 PNG en /tmp/qa/, todas vistas con Read). Todo salió de la versión con md5 a4f18613 (copia en /tmp/qa/snap.html), porque /tmp/shots/test.html cambió a las 04:19:52 mientras revisaba: las capturas de /tmp/shots/ ya no valen. Las fuentes de Google estaban bloqueadas, así que el render usó Inter/Georgia de reemplazo. Para los choques de etiquetas SVG escalé los anchos de texto un 12% para aproximar Poppins. Veredicto de render: ningún desbordamiento horizontal de página (scrollWidth = clientWidth a 1280 y a 400), pero hay 1 bloqueante funcional (el índice Pasos), 4 ALTO (gráficos cortados en móvil, probabilidad negativa en el widget 2, contraste de texto blanco sobre rellenos, rótulo faltante en el gráfico del CFO) y 17 hallazgos MEDIO y BAJO. No edité los archivos del artefacto. Dejé un parche que reúne las correcciones de render, JS y CSS: /tmp/qa/patch.py. Aplica limpio sobre snap.html y sobre template.html (salidas: /tmp/qa/fixed.html y /tmp/qa/fixed_template.html). Lo verifiqué así: el índice abre a top=46 px con scroll 6000; no quedan fallos de contraste HTML en ningún tema (antes 3 en claro y 1 en oscuro); no hay choques de texto SVG con factor 1,12; los saltos por ancla en móvil dejan el kicker 10 px por debajo de la barra; los widgets recorren 6 preajustes y 6 combinaciones extremas sin errores de consola. El parche NO cubre los hallazgos 14 y 16 a 25, que son copy, jerarquía y detalles sueltos; esas correcciones van escritas en cada hallazgo. La paleta y la tipografía de tokens_nvda.md no se tocan. Todo el color nuevo sale de tokens existentes o de #141413, que es --ink del tema claro.

--- 0
severidad: CRITICO
donde: Barra superior, botón 'Pasos' y <nav id=idx> (HTML líneas 151-174, JS idxBtn)
problema: El panel del índice es un bloque estático que va después de la barra sticky. Con la página desplazada, al pulsar Pasos el panel se abre arriba del documento (medido: top=-6431 px a scrollY 6000 en móvil, 479 px de alto), fuera de pantalla. El navegador compensa con el scroll anchoring y el lector ve que el botón 'no hace nada'. Solo funciona en scrollY=0. Es la única navegación de una página de 25.000 px (34.700 px en móvil). Tampoco cierra con Escape.
correccion: Meter el nav dentro del contenedor sticky. HTML: <div class="top"><div class="top-in">…</div><nav class="idx" id="idx" hidden aria-label="Índice por pasos"><ol>…</ol></nav></div>. CSS: .top .idx{max-height:calc(100dvh - 3.4rem);overflow-y:auto;overscroll-behavior:contain;border-top:1px solid var(--line)}. JS tras idxBtn.addEventListener: document.addEventListener('keydown',e=>{ if(e.key==='Escape'&&!idx.hidden){ idx.hidden=true; idxBtn.setAttribute('aria-expanded','false'); idxBtn.focus(); }});. Verificado: top=46 px con scrollY 6000 en móvil y escritorio.

--- 1
severidad: ALTO
donde: mount() y las 12 figuras SVG en móvil: figSeg, figOci, figRoic, figCash, figOwn, figCfo, figPrice, figPaths, figVals, figMC, figPort (y la tabla del Paso 4)
problema: A 400 px cada SVG mide 620 px (minWidth) dentro de un .scroll de 368 px: queda oculto el 41-47% de cada gráfico, sin ningún aviso visual y sin foco de teclado. Lo que se pierde es lo principal: el precio de hoy y las bandas en figPrice, la línea 'precio 130,55' y el valor 179 del escenario alcista en figVals, el rango TTM en figRoic, el gráfico RPO entero en figOci. El texto SVG queda a 9 px (escala 0,82). El área de scroll no es focusable por teclado en Safari ni Firefox.
correccion: 1) Sustituir mount(): function mount(id,svg,label,opt){ opt=opt||{}; const c=$(id); if(!c) return; svg.setAttribute('aria-label',label||''); if(!opt.fit) svg.style.minWidth='620px'; const w=document.createElement('div'); w.className='scroll'; if(!opt.fit){ w.classList.add('sc'); w.tabIndex=0; w.setAttribute('role','group'); w.setAttribute('aria-label','Gráfico desplazable: '+(label||'')); } w.appendChild(svg); c.replaceChildren(w); if(!opt.fit&&opt.end) requestAnimationFrame(()=>{ w.scrollLeft=w.scrollWidth; }); }. 2) CSS: @media (max-width:700px){.fig .scroll.sc::after{content:'Desliza para ver el resto →';display:block;font:500 .72rem var(--sans);color:var(--muted);text-align:right;position:sticky;left:0;padding-top:.2rem}}. 3) En figPrice cambiar el último argumento a mount('figPrice',s,'…ambos por debajo del mínimo',{end:true}) para que arranque en el precio de hoy. 4) figVals se adapta al ancho: function valsFig(res){ const cw=($('figVals').clientWidth||760); const W=Math.max(300,Math.min(760,cw)),H=250; …; const x=lin(0,mx,100,W-36); y la etiqueta de fila con x:92 en vez de 122; llamar mount('figVals',valsFig(res),'…',{fit:true}); y al final del IIFE: let _rw=0; window.addEventListener('resize',()=>{ clearTimeout(_rw); _rw=setTimeout(()=>read(),150); });. Verificado en captura a 400 px: figVals cabe entero y figPrice abre en el precio de hoy.

--- 2
severidad: ALTO
donde: Widget 2 '¿Qué tienes que creer…?', render2() (HTML líneas 905-909 del snapshot)
problema: Si el precio de entrada queda por debajo del valor del escenario base, 'need' sale negativo y el widget imprime probabilidades imposibles. Reproducido: cola 10% y precio 50 muestra 'ALCISTA REQUERIDO −15%' y 'exige una probabilidad absoluta de -15% … (y 105% para el base)'. Cola 0% y precio 40 muestra −31% y 131%. Es el widget que responde a la pregunta central de la tesis y da un número sin sentido.
correccion: En render2: const free=need<=0; En el KPI: ${imp?'Imposible':free?'0%':pct(need*rest)} y en el .d: ${imp?'incluso con todo el resto en alcista':free?'el base ya vale más que el precio':'probabilidad absoluta de la senda guiada'}. En el texto: free?`Con ${pct(tail)} de cola, ${fmt(px,0)} USD ya queda por debajo del valor del escenario base: el precio no exige ninguna probabilidad de alcista.`:`Con ${pct(tail)} de cola, ${fmt(px,0)} USD exige…` (el resto de la rama sin cambios). Verificado con cola 10/precio 50 y cola 0/precio 40.

--- 3
severidad: ALTO
donde: Texto blanco sobre rellenos: figOwn 'Ellison no pignorado 24,6%', figCfo (11.363, 3997, 7743) y botón de preajuste activo '.presets .btn[aria-pressed=true]'
problema: Se usa #fff sobre --sky, --clay y --clay-ink. Contrastes medidos: claro 2,93:1 (sobre sky) y 3,12:1 (sobre clay); oscuro 2,29, 2,61 y 1,97:1 (sobre clay-ink). Texto de 11-12 px: incumple WCAG AA 4,5:1 y en oscuro es casi ilegible (3997 sobre #efa88e). El botón de preajuste activo falla igual (3,12 claro y 2,61 oscuro).
correccion: Usar #141413 (valor de --ink claro) sobre sky y clay, y var(--paper) sobre clay-ink: 5,9-6,3 en claro, 7,1-9,4 en oscuro. CSS: .presets .btn[aria-pressed="true"]{background:var(--clay);border-color:var(--clay);color:#141413}. figOwn: style:'fill:#141413;font-weight:600'. figCfo: parts=[['Prepagos con componente financiero',11363,'var(--clay)','#141413','Prepagos financieros'],['Otros ingresos diferidos',3997,'var(--clay-ink)','var(--paper)','Otros diferidos'],['El resto del CFO (≈7.700)',7743,'var(--sky)','#141413','Resto del CFO']] y el texto del valor con style:`fill:${p[3]};font-weight:700`. Verificado: 0 fallos de contraste HTML en ambos temas.

--- 4
severidad: ALTO
donde: figCfo (Paso 6, 'De dónde sale el CFO del último trimestre')
problema: Los tres segmentos son cifras sueltas. 'parts' tiene nombre para cada uno pero no se dibuja: solo hay leyendas bajo el primero ('prepagos: cero hace un año') y el tercero. El bloque central (3997) no dice qué es. Además formatea '3997' y '7743' sin separador mientras '11.363' sí lo lleva.
correccion: Tras la línea que dibuja el valor, rotular cada segmento: s.appendChild(el('text',{x:x0+w/2,y:98,'text-anchor':'middle',style:'font-weight:600'},p[4])); (con p[4] = 'Prepagos financieros' / 'Otros diferidos' / 'Resto del CFO'). Bajar las aclaraciones a y:114 ('cero hace un año', 'operación sin diferidos'), la nota inferior a y:142 y subir H a 160. La separación de miles se corrige con el hallazgo de formato de cifras.

--- 5
severidad: MEDIO
donde: Slider WACC #s_wacc (step=0.05) frente al preajuste 'Tasa de mercado (10,26%)'
problema: min=8 y step=0.05 no admiten 10,26: el input lo redondea a 10,25. Al cargar, el botón activo dice 10,26% y el control muestra 'WACC 10,25%'. El simulador corre a 10,25% en todas partes (preajustes mercado y base-rate incluidos) mientras el texto de la tesis habla de 10,26%. Con 10,26 exacto la guía da un primer tramo de 130 en vez de 131.
correccion: <input type="range" id="s_wacc" min="8" max="13.5" step="0.01" value="10.26">. Verificado: output '10,26%' en los preajustes mercado y base-rate.

--- 6
severidad: MEDIO
donde: SVG con fuente real Poppins: figCash (etiquetas FCF), figPaths (etiqueta de guía y etiquetas finales)
problema: Con Inter no hay choques, pero Poppins Bold es ≈12% más ancha. figCash: 'FCF −23,7' y 'FCF −28,7' solapan con centros a 60 px. figPaths: 'Colapso 30' llega a x=764 sobre un viewBox de 760, queda recortada; la etiqueta 'guía de Oracle (sep-2025): 144 B en FY30' toca el '150 B' del eje.
correccion: figCash: quitar el prefijo y rotular una vez: s.appendChild(el('text',{x:cx,y:326,'text-anchor':'middle',style:'fill:var(--clay-ink);font-weight:700'},t)); y la etiqueta izquierda como 'FCF = CFO − capex (B USD):'. figPaths: const x=lin(0,10,64,640); y la guía: {x:x(4)-14,y:y(144)-16,'text-anchor':'end',…},'guía de Oracle: 144 B en FY30'. Verificado: 0 choques y 0 recortes con factor 1,12.

--- 7
severidad: MEDIO
donde: Formato de cifras: fmt() y tarjetas de escenarios (cardsInit/render)
problema: Cuatro defectos en la misma función. 1) 4 dígitos sin separador en es-ES: '5743', '4737', '3084', '3997' junto a '19.804' y '11.363' en la misma figura. 2) Menos ASCII '-43%', '-25', '-100%' frente al menos tipográfico '−58%' del resto de la página. 3) Aparece '-0 → 0 USD' en la tarjeta Bajista con el preajuste ERP (vps ≈ −0,3). 4) Las tarjetas Colapso y Bajista muestran '−25 → 0 USD' y '−4 → 0 USD': un valor negativo del modelo que el lector no sabe leer. Además usan 'equity' y 'TIR 10 a. a 130,55' (ilegible).
correccion: const fmt=(x,d=0)=>{ if(!isFinite(x)) return '—'; const r=Math.round(Math.abs(x)*Math.pow(10,d))/Math.pow(10,d); const sg=(x<0&&r!==0)?'−':''; return sg+r.toLocaleString('es-ES',{minimumFractionDigits:d,maximumFractionDigits:d,useGrouping:'always'}); };. Tarjetas: $('cv_'+n).textContent=(Math.round(o.vps)<=0?'0':fmt(o.vps,0))+' USD'; y en cd_: (Math.round(o.vps)>0?`TIR a 10 años comprando a 130,55: <b>${pct(o.tir,1)}</b>`:`Las acciones valen 0 (el modelo da ${fmt(o.vps,0)})`). figVals: const txt=Math.round(v)<=0?'0':fmt(v,0);. Verificado en los 6 preajustes.

--- 8
severidad: MEDIO
donde: figRoic (Paso 2)
problema: El trazo llega hasta TTM=13,5 (techo del rango 10,8–13,5) con un punto en 13,5. La línea sube de 13,0 a 13,5 y sugiere una mejora que no existe. El texto dice que el TTM es un rango. La etiqueta '19,0' de FY22 queda cruzada por el trazo.
correccion: Cortar la línea en FY26 y dejar el TTM solo como barra de rango: s.appendChild(el('path',{d:path(v.slice(0,10).map((d,i)=>[x(i),y(d)])),…})); y en el forEach: if(i<10) s.appendChild(el('circle',{cx:x(i),cy:y(d),r:3.6,style:'fill:var(--ink)'}));. Para '19,0': en i===5 usar x:x(i)+16,'text-anchor':'start',y:y(d)-4.

--- 9
severidad: MEDIO
donde: .verdict .vt del héroe (#vtext) y KPI 'Asimetría'
problema: El párrafo del veredicto hereda .wide (56 rem): líneas de ≈140 caracteres en 1280 px y un muro de 8 oraciones. El 'primer tramo' se explica con tres cláusulas encadenadas. 'entre 1,4× y 3,8× por debajo del precio' se lee al revés: el precio es 1,4 a 3,8 veces el valor. El KPI '+37% / −100%' se parte en dos líneas en las cinco tarjetas.
correccion: CSS: .verdict .vt{max-width:42rem}. KPI: <div class="v" style="font-size:1.2rem">+37% / −100%</div>. Copy de #vtext: «El valor es ≈75 USD, con banda de 71 a 86 y ruido de ±26. El precio es entre 1,4 y 3,8 veces ese valor, según la elección documentada que se use. El primer tramo (52–63 USD) nunca fue precio de cierre en 24 meses, cuyo mínimo es 114,99, y ningún margen de seguridad entre 0% y 35% lo cambia. El caso de compra queda archivado 12 meses y la compra nueva es 0% del NAV. Mi recomendación para tus 9 acciones (0,86%) es salir del lote. El método no permite vender por precio, así que la decisión es tuya y está en el Paso 11.»

--- 10
severidad: MEDIO
donde: Widget 1 en móvil (#w1): sliders a 1.400 px de los resultados
problema: Siete sliders apilados en una columna; los KPI, el texto de resultado y los gráficos quedan 1.100 a 1.500 px más abajo. Quien mueve un control en el teléfono no ve el efecto. Es el widget central de la tesis.
correccion: Barra de resultado pegajosa. HTML justo antes de .presets: <div class="mini" id="mini" aria-hidden="true"></div>. CSS: .mini{position:sticky;top:calc(3rem + env(safe-area-inset-top,0px));z-index:5;display:flex;flex-wrap:wrap;gap:.2rem 1rem;font:500 .8rem var(--sans);background:var(--card);border:1px solid var(--line2);border-radius:10px;padding:.45rem .7rem;margin:0 0 .8rem;box-shadow:0 2px 8px color-mix(in srgb,var(--ink) 8%,transparent)} .mini b{font-variant-numeric:tabular-nums}. JS en render(), antes de const r=$('res'): $('mini').innerHTML=`<span>Valor ponderado <b>${fmt(res.pond,0)} USD</b></span><span>Precio / valor <b>${isFinite(pv)?fmt(pv,2)+'×':'—'}</b></span><span>Alcanzabilidad <b>${pass?'Pasa':'Falla'}</b></span>`;. Verificado en captura a 400 px.

--- 11
severidad: MEDIO
donde: .state (pastilla 'Candado A cerrado · v2 · falta tu confirmación') y .heat .d
problema: La pastilla usa line-height:1 y radio 99px: en móvil el texto ocupa dos líneas que se pisan dentro de una forma redondeada. Contraste clay-ink sobre clay-bg = 4,28:1 en claro (por debajo de 4,5). El mismo par falla en las celdas rojas del heatmap (4,28:1 a 13,8 px).
correccion: .state{line-height:1.3;border-radius:12px;padding:.32rem .65rem;background:color-mix(in srgb,var(--clay-bg) 55%,var(--paper))} y .heat .d{background:color-mix(in srgb,var(--clay-bg) 55%,var(--paper));color:var(--clay-ink)}. Verificado: sin fallos de contraste en claro y oscuro.

--- 12
severidad: MEDIO
donde: Saltos por ancla en móvil: @media (max-width:560px) .sec{padding-top:2.6rem}
problema: Tras pulsar un paso del índice, la sección arranca en y=0 y el kicker (.sn) queda en y=42-43 px, bajo los 47 px de la barra sticky: el tercio superior del kicker queda tapado en las 7 secciones probadas. En escritorio sí hay holgura (55 frente a 47).
correccion: En el media query de 560 px: .sec{padding-top:3.5rem}.sec.first{padding-top:1.6rem}. Verificado: kicker en y=57 px.

--- 13
severidad: MEDIO
donde: Tablas: Paso 4, Paso 10, 'Coste de equivocarse' (Paso 11), 'Elecciones documentadas' y 'Candado C'
problema: 1) Ninguna tabla tiene separación con el .small que la sigue: el texto pega con el borde inferior. 2) Las celdas con dos cifras ('59,5 · 50,5', '2,19× · 2,58×') se parten en dos líneas. 3) En móvil la tabla 'Coste de equivocarse' comprime la tercera columna a una o dos palabras por línea ('pierdes / +454 / USD si / ocurre el / alcista'). tokens_nvda.md fija table{min-width:34rem} y aquí se omitió. 4) Candado C: la cabecera 'g años 3–5 −2 pp | 0 | +2 pp' mezcla etiqueta y valor en una sola columna.
correccion: CSS: td.n,th.n{white-space:nowrap} .scroll+.small,.scroll+p{margin-top:.8rem} .scroll>table:not(.heat){min-width:30rem}. Cabecera del Candado C: <th>WACC</th><th class="n">g −2 pp</th><th class="n">g base</th><th class="n">g +2 pp</th> y mover «g de los años 3–5» al texto de debajo.

--- 14
severidad: MEDIO
donde: Copy: antítesis y dos puntos que revelan
problema: No hay guiones largos ni 'sino' literal, pero sí cuatro 'No es X: es Y' y varias variantes en el cuerpo, más dos puntos que anticipan la conclusión en el veredicto, el Paso 0 y titulares. Hay jerga anglicista en texto de usuario ('widget', 'equity', 'port').
correccion: Reemplazos exactos. Paso 1: «Ahí el «tentáculo» no es la integración, es un contrato.» → «Ahí el «tentáculo» es un contrato.» Paso 6: «No es fraude ni opacidad: es la estructura de un constructor que cobra por construir.» → «Su estructura es la de un constructor al que se le paga por construir, sin señales de fraude ni opacidad.» Escenarios (final): «No es un ranking: es la anchura de la incertidumbre del instrumento, y por eso…» → «La anchura de este rango mide la incertidumbre del instrumento. Por eso el valor se publica como banda y la puerta 2 queda indeterminada.» Pie: «No es asesoría de inversión ni una orden: es la salida del método…» → «Esta página aplica el método y las reglas de Felipe a los datos del 14 y 15 de octubre de 2026. No constituye asesoría ni orden de inversión. La decisión y la ejecución son suyas.» Paso 4: «…dice a qué precio absorbió el mercado esa oferta, no que 141 sea valor.» → «…indica a qué precio absorbió el mercado esa oferta. No dice que 141 sea el valor.» Paso 6 viñeta 4: «…sin valor hoy: hay exposición al precio, pero no al retorno del capital.» → «…sin valor hoy. Dan exposición al precio de la acción y ninguna al retorno del capital.» Paso 0: «…un acto ejecutado: sesgo de compromiso en estado puro.» → «…un acto ejecutado, un sesgo de compromiso en estado puro.» Paso 9: «La casa no tiene ERP única: se declaran ambas.» → «La casa no tiene una ERP única y declara ambas.» H3: «Si firmas «mantener»: un factor basta» → «Si firmas «mantener», un factor basta». Anglicismos: «el widget de escenarios» y «El widget de abajo usa un port a JavaScript» → «el simulador de escenarios» y «El simulador de abajo usa una versión en JavaScript»; «Pérdida del equity» y «donde el equity vale cero» → «Las acciones valen 0».

--- 15
severidad: MEDIO
donde: Copy: frases de más de 38 palabras (11 detectadas)
problema: Las más largas, de 54, 53, 48, 46 y 44 palabras, mezclan varias ideas con paréntesis y dos puntos. Son las que más cuesta leer en móvil.
correccion: Partir así. Paso 11: «La primera versión defendía mantener con dos argumentos («no hay puerta» y «sumaría turnover»). Ninguno resiste. Vender 1.153 USD suma ≈0,9 puntos de rotación frente a un ≈55% anualizado. La regla de venta protege posiciones nacidas del proceso. Esta compra se hizo sin tesis, con B4 cerrado y antes del Paso 0.» Paso 10 'Pendiente de red': pasar a <ul class="clean"> con una viñeta por pendiente (USD de Cerner, bonos del 13 y 14 de octubre, garantía de 3,3 B, clase de referencia con ≥30 casos, calendario de los 288 B). Paso 5 'Qué limita el crecimiento': tres viñetas (Financiación, Energía y sitios, Demanda concentrada) y 'Pista' aparte. Escenarios: «Si OCI valiera cero, el software solo valdría ≈30 USD por acción. Eso tampoco es un suelo. En el colapso OCI vale −99 B y los 209 B del software dependen de un margen de 42% sin ancla y de SBC = 0.» Paso 8 falsador: una viñeta por condición en lugar de cuatro separadas con «·».

--- 16
severidad: BAJO
donde: Foco visible de los sliders (input:focus-visible)
problema: El anillo rodea todo el input de 30 px y pisa la etiqueta y el valor de arriba ('WACC' / '10,25%'). El pulgar no marca cuál control tiene el foco. La pista (--line2 sobre --paper2) tiene 1,34:1 y el pulgar clay 2,76:1.
correccion: input[type=range]:focus-visible{outline:none} input[type=range]:focus-visible::-webkit-slider-thumb{box-shadow:0 0 0 2px var(--paper2),0 0 0 4px var(--sky)} input[type=range]:focus-visible::-moz-range-thumb{box-shadow:0 0 0 2px var(--paper2),0 0 0 4px var(--sky)}. Opcional: subir el pulgar a ≥3:1 con box-shadow:0 0 0 1.5px var(--ink2).

--- 17
severidad: BAJO
donde: figPaths: líneas Colapso y Bajista
problema: En oscuro, --clay-ink (#efa88e) y --clay (#e18a6b) son casi el mismo salmón: ambas líneas y los bordes de tarjeta Colapso/Bajista se confunden. En claro se distinguen por poco. Solo las etiquetas finales las separan.
correccion: En el path de cada escenario: style:`stroke:${COL[n]};stroke-width:2.6;${n==='colapso'?'stroke-dasharray:7 4':''}`. Verificado en captura.

--- 18
severidad: BAJO
donde: Leyendas .lg i y tipografía pequeña
problema: Los cuadros de leyenda del heatmap (--moss-bg, --sky-bg, --clay-bg) casi no se ven sobre --paper (≈1,15:1). Tamaños de HTML bajo 12 px: .tg 10,6 px, .kpi .k 11,2, .src 11,5, th 11,5, .sn 11,8; el texto SVG baja a 9 px en móvil.
correccion: .lg i{box-shadow:inset 0 0 0 1px var(--line2)} .tg{font-size:.7rem} .fig .src{font-size:.76rem} .kpi .k{font-size:.74rem} th{font-size:.76rem}.

--- 19
severidad: BAJO
donde: Histograma figMC, ejes y nombres
problema: Los ticks del eje Y salen de redondear a 100 conteos: 16,5%, 8,5%, 0,0%. Son valores raros sin motivo. En el subtítulo se usa jerga sin glosa ('g∞', 'σ').
correccion: yGrid(s,y,[0,1000,2000,3000],50,745,t=>fmt(t/200,0)+'%'); Subtítulo: «Tasa ±1 pp, margen terminal ±5 pp, crecimiento ×0,8–1,2, crecimiento a perpetuidad ±0,5 pp, margen del software ±2 pp. Media 79 y desviación típica ≈26 (≈37 si los escenarios comparten el ruido).»

--- 20
severidad: BAJO
donde: Etiquetas con guion cortable y KPI de 2 líneas
problema: Las etiquetas en mayúsculas parten 'DISPARARÍA CON EL 10-/K FY27' porque el guion de '10-K' permite el salto. En Paso 5 la cuarta tarjeta ('TASA BASE (≥50 B DE INGRESOS)') ocupa dos líneas y desalinea su valor respecto a las vecinas.
correccion: Usar el guion no separable U+2011 en '10‑K' y '10‑Q' dentro de .ko .r y .kpi .k. CSS: .kpis .kpi .k{min-height:2.6em}.

--- 21
severidad: BAJO
donde: Widgets: aria-live, jerarquía de encabezados
problema: #res, #res2 y #res3 tienen aria-live=polite y los <output> de los sliders anuncian cada paso: un lector de pantalla recibe decenas de avisos al arrastrar. Los <h4> de .callout y .fig saltan de h2 a h4 sin h3.
correccion: Cambiar aria-live="polite" por aria-live="off" en los tres .res, o actualizar su texto con debounce de 400 ms. Cambiar .callout h4 y .fig h4 por <p class="h4"> con el mismo estilo (h4{…} → h4,.h4{…}) o por h3 con el estilo actual.

--- 22
severidad: BAJO
donde: Coherencia de cifras visibles y una afirmación sin fuente en render3()
problema: El héroe dice '≈75', el simulador por defecto '74' y la tabla de elecciones 'Casa … 73,7'. El KPI 'banda 71–86 (WACC 10,4–9,7%)' ordena el WACC de mayor a menor. El texto del simulador dice 'más que cualquier operador de infraestructura' sin cita en la página.
correccion: Unificar con el mismo redondeo y explicar la diferencia en una frase (≈75 es con anulación, 73,7 es la casa). Cambiar «(WACC 10,4–9,7%)» por «(WACC 9,7–10,4%)». En render3: «…en OCI: por encima del 55% que publica el segmento combinado de Oracle.»

--- 23
severidad: BAJO
donde: figPort (cartera, Paso 11) y pie de la figura
problema: El pie y el titular hablan de una cadena de IA de 26,9% frente a un tope de 20%, pero el gráfico solo muestra el tope de 15% de ruina. La barra de la cadena y su límite no existen en la figura. Esa es la cifra de la que depende la regla.
correccion: Añadir fila 'Cadena IA ancha' con 26,9% (TSM+GOOGL+AMZN+MSFT+ORCL) y una segunda línea punteada en 20% rotulada 'tope cadena de IA 20%'. El dominio X debe pasar de 24 a 30 (lin(0,30,110,700)) y los ticks a [0,5,10,15,20,25,30].


##### AGENTE ab6dcd882f917aafc
RESUMEN: REVISION DE CONSISTENCIA NUMERICA, SESION LIMPIA, SIN EDITAR ARCHIVOS. Versiones revisadas: tesis /home/user/inversiones/Tesis/ORCL/2026-10-14_UltraTesis_ORCL_metodo12.md (sha256 162a6170c8b9..., mtime 04:14:42Z, 480 lineas); artefacto /home/user/inversiones/Tesis/ORCL/_trabajo_2026-10-14/artefacto/template.html (sha256 873fcddaa814..., mtime 04:19:52Z, 874 lineas; artefacto_orcl.html construido con la misma parte estatica; ambos scripts pasan node --check); orcl_data.json (sha256 7ceca410eb03...). Aviso: ambos archivos cambiaron mientras revisaba (la primera lectura del template era la v1: 71-94, 52-68, 1,77x, Provisional, monologo propuesto, etc.); todos los hallazgos de abajo se contrastan con la version de las 04:19:52Z y las lineas L### son de ella. Tras corregir hay que reconstruir con build_artifact.py y republicar la URL claude.ai/artifact/HG6cFnED67diq7bXBAZKds (la que cita la cabecera de la tesis).

LO QUE ESTA BIEN (no tocar): ya estan integradas la reescritura del veredicto (NO por precio, salir del lote como recomendacion, puerta 2 indeterminada, B4), 71-86 / 52-63 / 1,5-1,8x / 1,4-3,8x, DCF inverso (>=55% / <=27% de cola), 49% (no 66%) de prepagos, recompras a 57,5, 24,9 B = 19,9 B + 5,0 B, CIP 38-40% neto, SBC por duracion con disparo en el 10-K FY27, ROIC TTM 10,8-13,5%, J5/Li Lu, P1-P6, factores 'basta uno', 16 decisiones, tabla de elecciones documentadas, +37% con la salvedad de +5%, 'no es un suelo', MC con ruido comun. Reproduje con el motor JS: 72,6 / 178,5 / ponderado 73,7 / P/V 1,77 / TIR 7,18% y 15,55% / candado C 129-137-145 · 67-73-78 · 34-38-43 / DCF inverso 79,1% y 54,7%-73,2%-27% / pesos de tasa base 50,5 / ERP 85,7 / beta cruda 35,0 / necesidad de P_justo 157,5; todo coincide con la tesis. Los cuadros V_R1, V_R2, V_R3, V_R4, V_R5, V_R6, V_R7, V_R8 del Paso 10 suman bien (22+4+4=30, 29+4+8=41, 21+1+3=25, 22+1+13=36, 25+1+4=30, 27+1+2=30). La fila del angel (+4 a +14) y las 3 refutaciones del 10c coinciden con sus informes.

CONTEO: 0 criticos, 5 altos, 26 medios, 22 bajos. PRINCIPALES: (1) rotulo 'Candado A cerrado' contradice los pendientes del propio artefacto y no dice que sin la excepcion de la fila 23 es borrador sin veredicto; (2) el lead conserva el marco retirado 'paga la guia entera'; (3) el preset 'Lo mas generoso' (WACC 8,0%, ponderado 297, 'Pasa') no existe en la tesis, viola el espiritu del candado B y usa el mensaje retirado 'casi sin cola'; (4) la lista de sesgos del modelo del 10.10 sigue incompleta (valor terminal 74% del EV, financiacion/dilucion, capex post-pico, circulante, WACC unico, margen incremental 39,2%, sesgos al alza cuantificados); (5) falta el suelo HECHO de concentracion (contrato >30 B/anio = >=41% del OCI guiado de FY28; 4 contratos con 3 clientes). Correcciones de verificadores aun sin integrar: V_R2/V_R8 balloon 4.504 M (artefacto: 4,6 B), V_R1 R1-13 y R1-14 (VIE 27 docs ok; restatement FY17-FY24 DEGRADADO sin rotular), V_R1 R1-15 (margen no es de OCI; ya no figura en Sleep), V_R8 V8-14b (hito judicial condicional), V_R8 V8-25 (margen incremental 39,2%), V_R5 R5-05 (licencias: dos definiciones). Incoherencias de la propia tesis detectadas que condicionan el texto del artefacto: 'max. 78' para MoS 0-35% (con MoS 0% el tramo es 71-86); redondeo mixto (base 72,6 -> 'aprox. 70' a la decena, ponderado 73,7 -> 'aprox. 75' a la 5; el simulador muestra 73/179/74); 'Fuentes: 10-K FY17-FY26' frente a un corpus local que solo tiene FY25 y FY26.

--- 0
severidad: ALTO
donde: template.html L182 (#vstate) y L507 (#vstate2); condicion ausente en L185 y L508
problema: El rotulo dice 'Candado A cerrado · v2 · falta tu confirmacion'. (a) Contradice el propio artefacto (L499 y L579 punto 3: el cruce 10c y los desempates D1-D3 siguen pendientes) y la tesis (LAGUNAS: 'el cruce 10c (Felipe) y los desempates finales estan pendientes'). (b) 'falta tu confirmacion' no dice de que: la nota de gobernanza de la tesis fija que sin 'excepcion: si' explicita de Felipe (decision n.2) el documento es BORRADOR SIN VEREDICTO y 'nada de lo anterior cuenta como veredicto emitido'; el hero muestra 'NO, por precio' en grande sin esa condicion (solo aparece en L577 y L579).
correccion: En L182 y L507 sustituir el texto del span por: Candado A ejecutado · v2 · pendientes tu cruce 10c y tu confirmacion de la excepcion (fila 23). Anadir al final de L185 y de L508: ' Condicion: si no confirmas la excepcion a la fila 23 con tus palabras, este documento es un borrador sin veredicto.'

--- 1
severidad: ALTO
donde: template.html L180 (lead del hero)
problema: 'A 130 USD el precio paga la guia entera' reintroduce el marco retirado en la v2 ('el mercado paga la senda alcista completa con casi cero probabilidad de cola'; critico B2/C1; cabecera de la tesis: 'no sobrevivio'). Lo verificado (tesis cuadro, 10.4, 8): 130,55 es el 73% del valor alcista, exige P(alcista)>=55% si el resto es base (>=73% si vale cero) y admite como maximo 27% de cola frente al 35% de la tesis. Ademas 'rinde apenas su coste de capital' toma el ROIC incremental mas generoso (10,5%; 9,0% sin rezago, 8,1-8,5% con prepagos, 7,9% sin Cerner) y 'crece mas del 100%' es solo el ultimo trimestre (FY26: +77%).
correccion: Sustituir L180 por: Un negocio cautivo y rentable que paga los intereses, y otro, alquilar capacidad de IA, que crecio un 121% en el ultimo trimestre (77% en FY26), se financia con deuda, acciones y los prepagos de pocos clientes y rinde, como mucho, su coste de capital. A 130 USD el precio es el 73% del valor de la guia cumplida: exige que el escenario alcista pese al menos 55%, y la tesis deja 35% a la cola.

--- 2
severidad: ALTO
donde: template.html L406 (boton 'Lo mas generoso'), L864 (PRE.generoso) y L838 (mensaje de 'Pasa')
problema: El preset 'Lo mas generoso' (WACC 8,0%, crecimiento x1,15, +3 pp de margen, -3 pp de capex, pesos 5/15/40) no existe en la tesis y con el motor da base 232, alcista 495, ponderado 297 (P/V 0,44x) y 'Alcanzabilidad: Pasa'. WACC 8,0% es una subtasa de mercado que el candado B prohibe (tesis 10.9: 'solo informativas') y B4 impide que la valoracion autorice compra. El mensaje de 'Pasa' dice 'hace falta creer casi sin cola en la guia completa': frase retirada y falsa para ese preset (cola 20%). La tesis: pasar exige P_justo>=157,5 (WACC<=7,8% o >=80% de peso alcista).
correccion: (1) Borrar el boton de L406 y la linea 'generoso:{...}' de PRE (L864). (2) En L838 sustituir ' Para llegar aqui hace falta creer casi sin cola en la guia completa.' por: ` Para pasar hace falta un valor ponderado >= ${fmt(MIN24/0.73,1)} USD (= ${fmt(MIN24,2)} / 0,73): con la tasa de mercado solo se logra con >=80% de peso alcista o con un WACC <=7,8%, que el candado B prohibe. La valoracion es informativa: no autoriza compra (B4).` (3) En render(), tras definir wnote, anadir: if(st.wacc<0.097){ $('wnote').innerHTML+=' <b style="color:var(--clay-ink)">WACC por debajo del suelo de mercado (9,7%): subtasa solo informativa; el candado B la prohibe.</b>'; }

--- 3
severidad: ALTO
donde: template.html L394, L399, L455, L469 y L595 (lista de sesgos del modelo; tesis 10.10 y 10.2)
problema: El artefacto resume 'sesgo neto mixto' pero omite casi todo el contenido de 10.10 que cambia la lectura: valor terminal = 74% del EV y 113% del patrimonio en el base; financiacion (~125 B de deficit hasta FY29 con 3.050 M de acciones fijas; plan de 40 B de FY27 con 20,1 B sin tipo; dilucion no modelada); capex de los anios 6-10 por debajo de la depreciacion del propio motor (-7 a -21 USD); retorno marginal terminal implicito 55,6%; capital circulante de OCI omitido (-4 a -5); WACC unico para dos segmentos (~-4); margen incremental interanual del segmento 39,2% (1T FY27) frente al 50-58% supuesto; y los sesgos al alza cuantificados (fin de periodo +5,0; deuda a par +4,8; anio 1 x0,75 +1,7; caja restringida 2,6 B e inversiones 2,4 B +0,8 c/u; acciones +0,6 a +1,5; financiacion de clientes 0 a +10). Tampoco dice que la base esta +13% sobre la guia en FY27 y -21/-31/-35% en FY28-FY30.
correccion: Sustituir el <li> de L595 por: <li><strong>El sesgo neto del modelo es mixto.</strong> Empujan a la baja y siguen abiertos: margen EBITDA de OCI 50-58% sin derivacion (el margen incremental interanual del segmento fue 39,2% en el 1T FY27; +-5 pp mueven el ponderado -+16-17 USD); SBC = 0 (indeterminado: 0 a -38); renta de los 288 B (cada 5 B/anio resta ~11); capex de los anios 6-10 por debajo de la depreciacion del motor (-7 a -21); retorno marginal terminal de OCI implicito de 55,6% y g_inf de 4,2% frente al tope de 2,35% de la Enmienda 29 (ponderado 56 y 63); circulante de OCI omitido (-4 a -5); un solo WACC para dos segmentos (~-4); candados TAM y de reinversion sin ejecutar; ~125 B de deficit hasta FY29 financiados a WACC con 3.050 M de acciones fijas (la dilucion del plan de 40 B de FY27, 20,1 B sin tipo, no esta modelada). El valor terminal pesa el 74% del EV y el 113% del patrimonio en el base. Empujan al alza: descuento a fin de periodo (+5,0), deuda a par frente a valor razonable (+4,8), anio 1 prorrateado x0,75 (+1,7), prepagos a nominal, caja restringida de 2,6 B e inversiones no negociables de 2,4 B fuera del puente (~+0,8 cada una), acciones 3.050 frente a 3.024 (+0,6 a +1,5) y financiacion de clientes no modelada (0 a +10). Con ambas listas el ponderado queda en 69-74: el ~75 no es ni un techo ni un centro demostrable.</li>. En L394 anadir tras 'FY28-FY30': ' (y un 13% por encima en FY27)'.

--- 4
severidad: ALTO
donde: template.html L240 (tarjeta Concentracion), L215, L280 (celda 'RPO sin desglose') y L354 (M1); tesis 10.10 ultimo parrafo
problema: El artefacto solo dice 'ningun cliente >=10%... CxC y RPO sin desglose', lo que invita a leer 'sin concentracion', cuando M1 es el mecanismo mas grave. La tesis (con V_R8 V8-08/V8-09) aporta el suelo con base HECHO: un contrato 'de mas de 30 B de ingresos anuales desde FY28' (8-K del 30-jun-2025) seria >=41% del OCI guiado de FY28 (30/73), y el salto de +317,5 B de RPO del 1T FY26 vino de cuatro contratos con tres clientes (8-K del 9-sep-2025). La cifra de OpenAI (~300 B, ~45%) es DEGRADADA.
correccion: Sustituir el <p> de L240 por: <p>Ningun cliente >=10% de ingresos en FY24-FY26, pero el RPO no se desglosa y el suelo con base HECHO es alto: un contrato 'de mas de 30 B de ingresos anuales desde FY28' (8-K del 30-jun-2025) seria >=41% del OCI guiado de FY28 (30 de 73 B), y el salto de +317,5 B de RPO del 1T FY26 vino de cuatro contratos con tres clientes (8-K del 9-sep-2025). Los contratos de IA tienen menos de 18 meses. El riesgo vive en el RPO y va al Paso 8 (M1), no a este gate.</p>. En L280 cambiar 'RPO sin desglose' por 'RPO sin desglose; suelo HECHO: un contrato >30 B/anio desde FY28'.

--- 5
severidad: MEDIO
donde: template.html L361 (callout 'Falsador del caso bajista')
problema: Muestra como principal el falsador sellado, cuyo texto la tesis declara inalcanzable, y solo describe la correccion de forma resumida e inexacta ('dos de los cuatro puntos eran inalcanzables o inobservables en diciembre'). Segun tesis 9 y el addendum: el punto 2 (FCF>0 en un trimestre de FY28) no lo cumple ni el alcista (FCF -40,1 B en FY28); el punto 4 es inobservable (Oracle no revela RPO por cliente); y la 'revision anticipada' por el 8-K de diciembre era imposible porque los puntos 1 y 3 necesitan el cierre de FY27 o una emision de 2027. Las condiciones vigentes F1-F4 no se listan.
correccion: Sustituir el segundo <p class='small'> de L361 por: <p class='small'>Falsador revisado (addendum del 15-oct; el sello no se toca), tres de cuatro: F1 OCI de FY27 >=36 B con margen del segmento Cloud & Software >=55% sostenido (8-K/10-K del 4T FY27); F2 FCF positivo en un trimestre de FY29 o FY30 sin prepagos con componente financiero; F3 rating estable o al alza por las tres agencias y emision a 10 anios <= UST + 150 pb (primera emision de 2027); F4 RPO >=700 B con la nota de modificaciones sin cancelaciones, o un segundo cliente nombrado con >=10% del RPO. Por que se corrigio: el punto 2 sellado no lo cumple ni el escenario alcista (FCF -40 B en FY28), el punto 4 sellado es inobservable y la revision anticipada por el 8-K de diciembre era imposible. Revision anticipada: el 10-K FY27 cumple F1, F3 y F4 (F2 aun no es evaluable) o un cierre <=63 USD sin que el alcista se haya materializado.</p>. Rotular el <p> principal de L361 con 'Sellado:' al inicio.

--- 6
severidad: MEDIO
donde: template.html L446 (fuente de los mapas de calor) y orcl_data.json 'rejilla'
problema: La fuente dice 'motor de la tesis (resultados_paso9.txt)', pero las celdas vienen de build_data.py (margen limitado desde el anio 6), no de resultados_paso9.txt (desde el anio 4). Verifique: 10 celdas de la rejilla base difieren hasta 4,4 USD (fila 45%: 60,3/47,7/40,2/22,5/9,9 frente a 56,0/43,4/35,8/18,2/5,6) y 15 de la alcista hasta 7,0 USD. La tesis (10.10, LAGUNAS) y el auditor de modelo (#15) lo declaran; el artefacto lo oculta y cita la fuente equivocada.
correccion: Opcion A (recomendada): regenerar orcl_data.json con la misma convencion que resultados_paso9.txt (i>=3) o reescribir resultados_paso9.txt con i>=5, y dejar L446 como esta. Opcion B: sustituir L446 por: 'Fuente: motor de la tesis con el margen limitado desde el anio 6 (build_data.py). resultados_paso9.txt lo limita desde el anio 4 y difiere hasta 4,4 USD (senda base) y 7,0 (alcista) en las celdas con margen <55-58%; el DCF inverso no se ve afectado.'

--- 7
severidad: MEDIO
donde: template.html L485 (fila 'Critico de completitud' del Paso 10)
problema: Lista como cinco bloqueantes 'frase del DCF inverso, puertas de venta, formato de bandas, circulo de competencia y falsables' y dice 'todos reescritos'. El informe del critico: B1 Candado A sin ejecutar, B2 DCF inverso, B3 puertas, B4 formato del candado C y B5 J5 sin respuesta de Felipe; los falsables son B6 (bloqueante del cierre, no del veredicto). J5 no puede estar 'reescrito': sigue abierto (decision n.1).
correccion: Sustituir la celda por: Direccion intacta. Cinco bloqueantes del veredicto: Candado A sin ejecutar (ya ejecutado), frase del DCF inverso (reescrita), puertas de venta (reescritas), formato de bandas del candado C (reescrito) y J5 sobre OCI sin respuesta tuya (sigue abierto). Y uno del cierre: los falsables mal formados (corregidos en el addendum).

--- 8
severidad: MEDIO
donde: template.html L484 (fila 'Auditor de reglas')
problema: 'casi todos de forma y de rotulo' es una glosa del artefacto que no esta en el informe ni en la tesis. El informe cuenta incumplimientos de fondo: puerta 2 desmentida por las propias cifras, valor central apoyado en una anulacion optimista sin pagar el peaje, y decisiones de Felipe resueltas por el redactor (convencion SBC/FCF, circulo de competencia).
correccion: Sustituir por: 12 incumplimientos y 13 ambiguedades; entre ellos, el peaje de la anulacion optimista sin pagar, la puerta 2 desmentida por las propias cifras y decisiones tuyas resueltas por el redactor (convencion SBC/FCF, circulo de competencia). El sentido del veredicto no se tambalea.

--- 9
severidad: MEDIO
donde: template.html L241 (tarjeta 'Solvencia inminente')
problema: 'con colchon de 7-11x' presenta como hecho una INFERENCIA (proxy propio) y la llama colchon. Tesis 3: proxy ~9-11x en FY26 y ~7-9x LTM, 'no hay declaracion a 31-ago-26' (V_R2 R2-13/14: el cumplimiento a esa fecha es inferencia). Falta la lectura clave de 10.10/V_R8: el EBITDA tendria que caer ~70% para romperlo, los bonos no tienen covenants financieros y las facilidades bancarias tienen cross-default a 500 M; el riesgo es el acceso a financiacion.
correccion: Sustituir el <p> por: <p>Sin going concern. Unico covenant (cobertura neta de intereses >=3,0x) declarado cumplido a 31-may-26; no hay declaracion a 31-ago-26. Proxy propio (INFERENCIA): ~9-11x en FY26 y ~7-9x LTM; el EBITDA tendria que caer ~70% para romperlo. Los bonos no tienen covenants financieros; las facilidades bancarias, cross-default a 500 M. El riesgo es el acceso a la financiacion, no el covenant.</p>

--- 10
severidad: MEDIO
donde: template.html L238 (Restatement) y L239 (VIE)
problema: Restatement afirma 'Cero reexpresiones por error FY17-FY26' sin rotulo; la tesis (tabla del Paso 2) lo marca HECHO solo para FY25-FY26 y DEGRADADO el resto (V_R1 R1-14: 10-K FY17-FY24 fuera del corpus). VIE (V_R1 R1-13: DEGRADADO fuera de 27 documentos; ausencia en filings no prueba inexistencia) no dice 'por ausencia'.
correccion: L238: <p>Ninguna reexpresion por error en FY25-FY26 (casilla de la portada del 10-K FY26 sin marcar; opinion limpia; cero debilidades materiales): HECHO. FY17-FY24: DEGRADADO, 10-K fuera del corpus local.</p>. L239: <p>Cero menciones de 'variable interest entity' en los 27 documentos EDGAR del corpus local (HECHO por ausencia: prueba que Oracle no las revela, no que no existan). TikTok USDS JV (15%) por el metodo de la participacion.</p>

--- 11
severidad: MEDIO
donde: template.html L234 (introduccion del Paso 2)
problema: 'Pero uno esta en el umbral y otro depende de una convencion' quedo obsoleto: la tarjeta SBC (L237) ya dice que la convencion de capex de mantenimiento no se adopta y que el knock-out dispararia con el 10-K FY27. Contradiccion interna.
correccion: Sustituir la frase por: 'Pero uno esta en el umbral (ROIC) y otro dispararia con el 10-K FY27 si el FCF sigue <=0 (SBC).'

--- 12
severidad: MEDIO
donde: template.html L245-246 (titulo y fuente de la figura ROIC), L305 (fuente de la figura de caja), L600 (Fuentes primarias); tesis L477
problema: El titulo ('cayo a menos de la mitad en cinco anios') descansa en FY21 = 28,7%, que la tesis declara DEGRADADO junto con toda la serie FY17-FY23 (filings ausentes del corpus), pero la fuente solo lleva INFERENCIA. Las fuentes dicen '10-K FY17-FY26'; el corpus local solo tiene 10-K FY25 y FY26 y el resto sale de companyfacts.json, de procedencia no re-verificable (V_R1: DEGRADADO).
correccion: L245 h4: 'El retorno sobre el capital cayo de 28,7% (FY21, serie degradada) a 13,0% (FY26), y esta entre 10,8% y 13,5% en el ultimo anio'. L246 src: 'Fuente: calculo propio sobre 10-K FY25 y FY26 y 10-Q 1T FY27 (corpus local); FY17-FY24 solo via XBRL consolidado, de procedencia no re-verificable. Serie FY17-FY23: DEGRADADA. <span class='tg i'>INFERENCIA</span> <span class='tg x'>DEGRADADO</span>'. L305 y L600: sustituir '10-K FY17-FY26' por '10-K FY25 y FY26 (FY17-FY24 solo via XBRL)'. Corregir lo mismo en la tesis L477.

--- 13
severidad: MEDIO
donde: template.html L253 (h2 del Paso 3) frente a L266
problema: El h2 dice 'Un foso real'; L266 dice que el del legado 'lo afirma la empresa y no esta medido'. La tesis v2 (Paso 3): 'que sea real lo afirma la empresa, no esta medido'. Contradiccion interna.
correccion: L253: <h2>Un foso declarado por la empresa y no medido</h2>

--- 14
severidad: MEDIO
donde: template.html L255 (Test de Sleep)
problema: Afirma 'En cloud no... El ahorro va al cliente o a construir capacidad' sin las salvedades de la tesis 4: el 59%/55% es el margen del segmento COMBINADO (incluye soporte de alto margen, excluye I+D, G&A y SBC), el margen real de OCI es menor y no se desglosa (V_R1 R1-15), la caida 64%->55% se debe en parte a la mezcla (soporte plano, OCI +121%) y la inferencia es debil; los gastos del segmento subieron +50% (linea 'Cloud and software' +82%) frente a ingresos +33%.
correccion: Sustituir la segunda frase por: 'En cloud, la lectura mas probable, no medida, es que no: el margen del segmento cloud & software cayo de 64% (FY24) a 59% (FY26) y 55% en el ultimo trimestre, con gastos del segmento +50% frente a ingresos +33%. Ojo: es el margen del segmento combinado (incluye el soporte de alto margen y excluye I+D, G&A y SBC), el margen real de OCI es menor y no se desglosa, y la caida se debe en parte a la mezcla, asi que la inferencia es debil. El ahorro iria al cliente o a construir capacidad.'

--- 15
severidad: MEDIO
donde: template.html L273 (introduccion del Paso 4)
problema: 'mas cerca de CoreWeave por la concentracion y la financiacion' va mas alla de la tesis 5 ('ORCL se situa entre los hiperescaladores y CoreWeave en capex, FCF y apalancamiento'). La concentracion de Oracle no esta cuantificada (RPO sin desglose; el ~45% en un cliente es DEGRADADO).
correccion: Sustituir por: 'Oracle esta entre los hiperescaladores y CoreWeave en capex, FCF y apalancamiento. Su concentracion de clientes no esta cuantificada: el RPO no se desglosa y el ~45% atribuido a un cliente es prensa (DEGRADADO).'

--- 16
severidad: MEDIO
donde: template.html L339 (Paso 7, triangulacion)
problema: Solo muestra la lectura favorable: 'P/E non-GAAP 16,1x (yield 6,2% frente a 5,21%)'. La tesis 8 y 10.6 anaden que la guia EPS excluye ~1,6 USD/acc. de SBC y que el P/E GAAP LTM es 20,5x (yield 4,9%, POR DEBAJO del Tesoro); el EV/EBITDA 16,7x es de FY26 (LTM 14,8x) con EV 501 B (deuda a par, sin prepagos), no el EV implicito de 517 B del Paso 9.
correccion: Sustituir la frase de triangulacion por: 'Triangulacion: EV/EBITDA FY26 16,7x (LTM 14,8x; EV 501 B con deuda a par y sin prepagos, no los 517 B del Paso 9); P/E non-GAAP de FY27 16,1x (yield 6,2% frente a 5,21% del Tesoro, pero la guia excluye ~1,6 USD/acc. de SBC); P/E GAAP LTM 20,5x (yield 4,9%, por debajo del Tesoro); EV sobre owner earnings, no definido (negativo).'

--- 17
severidad: MEDIO
donde: template.html L833 (tarjetas de escenario) y L399
problema: Las tarjetas muestran 'TIR 10 a. a 130,55: 7,2%' y '15,6%' con un decimal. La tesis (cuadro, v2 fila 10) declara que la prueba de coherencia FALLA (comprando a valor justo el motor devuelve 13,5% en lugar de 10,26%): no es una TIR de accionista comparable con Ke 11,55% y se publica como orden de magnitud (base ~6-7%, alcista ~13-16%; con coste financiero neto 6,0-6,8% y 14,6-15,2%).
correccion: En L833 sustituir `TIR 10 a. a 130,55: <b>${pct(o.tir,1)}</b>` por `TIR 10 a. a 130,55 (orden de magnitud): <b>~${pct(o.tir,0)}</b>`. Anadir al final del sub de L399: ' La TIR es un orden de magnitud, no una TIR de accionista: comprando a valor justo el motor devuelve 13,5% en lugar de 10,26%; con coste financiero neto de 2-6 B/anio la base es 6,0-6,8% y la alcista 14,6-15,2%, frente a Ke 11,55%.'

--- 18
severidad: MEDIO
donde: template.html L856 (res3, texto para m>0,7)
problema: 'Hace falta un margen EBITDA de X% en OCI: mas que cualquier operador de infraestructura' no tiene soporte en la tesis ni en el corpus (no hay margenes comparables) y el 79% es el desplazamiento solo del terminal; con desplazamiento paralelo de todos los anios la tesis (cuadro, 8, 10.4) da ~70-73% a 130,55.
correccion: Sustituir por: `Hace falta un margen EBITDA terminal de <b class="bad">${pct(m,0)}</b> en OCI (desplazando solo el terminal; con desplazamiento paralelo de todos los anios el umbral baja a ~70-73% a 130,55 USD). Oracle no publica el margen de OCI y el corpus no trae comparables.`

--- 19
severidad: MEDIO
donde: template.html L368 (calendario, balloon del term loan)
problema: 'balloon del term loan (~4,6 B)' usa la cifra del sello (4.644 M) que V_R2 R2-04 y V_R8 V8-34 corrigieron y la tesis (11 y tabla de disposicion) ya integro: el balloon puro del 16-ago-2027 es 4.504 M (la cuota de 140,75 M del 30-jun-27 va aparte).
correccion: <li><b>ago-2027 · balloon del term loan (~4,5 B)</b>4.504 M segun el calendario del 10-K (el pre-mortem sellado decia 4.644 M por una cuota de mas). Extensible.</li>

--- 20
severidad: MEDIO
donde: template.html L370 (calendario, ultima linea)
problema: 'FY28: meta de las PSO (100 B)': 100 B es el UMBRAL (paga 80%); el objetivo es 125 B y el maximo 250 B (tesis 7; el artefacto lo dice bien en L323). Ademas junta en una fecha 15-ene-2029 dos eventos distintos: el cierre de FY28 es el 31-may-2028.
correccion: Sustituir el <li> por dos: <li><b>may-2028 · cierre de FY28</b>Umbral de las PSO: 100 B de ingresos non-GAAP (paga 80%); objetivo 125 B.</li><li><b>15-ene-2029 · conversion obligatoria de las preferentes</b></li>

--- 21
severidad: MEDIO
donde: template.html L711 (grafico CFO 1T FY27) y L325
problema: 'Otros ingresos diferidos 3.997' se pinta con clay-ink (color de alerta) como si fuera anomalo; V_R1 R1-05 y la tesis (cuadro, 8) dicen que son diferidos normales de estacionalidad (en 1T FY26 hubo 2.550, 31% del CFO de entonces) y que 'quitarlos como si fueran anomalos sobrestima el ajuste'. La alerta es solo el 49% (11.363 M).
correccion: En la lista 'parts' de L711: ['Otros diferidos (estacionalidad normal)',3997,'var(--stone)']. Anadir al src de L331: ' Los 3.997 M de otros diferidos son estacionalidad normal (2.550 M en el 1T FY26); lo anomalo es el 49% de prepagos con componente financiero.'

--- 22
severidad: MEDIO
donde: template.html L299 (KPI ROIC incremental) y L342
problema: No traslada la lectura hacia delante de la tesis 6: g derivado 29,6% frente a un NOPAT real +16,6% (FY26) y +15,1% (FY25), y, con el capital del 31-ago-26 y la inversion de la senda base, ROIC del grupo 9,6% en FY27, ~5-7% en FY28-FY31 y ~10% solo hacia FY33 (INFERENCIA del diablo, cota alta). Hace que 'el coste del capital' parezca un suelo.
correccion: Anadir al <div class='d'> de L299: '. Hacia delante, con la inversion de la propia senda base, el ROIC del grupo cae a 9,6% en FY27 y a ~5-7% en FY28-FY31 (INFERENCIA del diablo, cota alta).'

--- 23
severidad: MEDIO
donde: template.html L185 y L189 (valor ponderado) y L511
problema: La tesis exige rotular toda cifra de valor: 'Etiqueta obligatoria: valor SIN SBC, sin renta de los arrendamientos no iniciados, con g_inf de OCI 4,2%'; el ponderado ~75 se publica como 'con anulacion' (con pesos de tasa base ~51-60). El hero y el KPI no lo dicen (solo L399 y L595 lo dicen).
correccion: L189 d: 'banda 71-86 (WACC 10,4-9,7%) · sigma ~26 · sin SBC, con anulacion optimista (~51-60 con pesos de tasa base) · precio / valor ~1,8x'. L185: tras 'USD' anadir ' (sin SBC, con anulacion optimista)'.

--- 24
severidad: MEDIO
donde: template.html L191 y L515; tesis 10.9 (L288) y 12 campo 5 (L388)
problema: 'primer tramo <=78 con cualquier margen de seguridad' es falso para MoS entre 0% y 9%: P_tramo1 = P_justo x (1 - MoS), asi que con MoS 0% es 71-86 y solo desde 9% es 65-78. La conclusion (falla) no cambia porque 86 < 114,99. La tesis repite '(max. 78)' con 'cualquier MoS entre 0 y 35%'.
correccion: L191 d: 'primer tramo <=86 con MoS entre 0% y 35% (52-63 con 27%) frente a minimo 114,99'. L515: 'FALLA de forma invariante: <=86 con cualquier margen de seguridad entre 0% y 35% (<=78 desde 9%) frente a minimo 114,99 (24-jul-2026)'. En la tesis L288 y L388 sustituir '(max. 78)' / '<=78' por '(max. 86 con MoS 0%; 78 desde MoS 9%)'.

--- 25
severidad: MEDIO
donde: template.html L185/L189/L458 y JS L833/L836; tesis L24 y L213
problema: Redondeos incoherentes: el hero dice ~75, el simulador muestra 74 (fmt(73,68,0)), la tabla 73,7; escenarios 73/179 en el simulador frente a la tesis 'base ~70 / alcista ~180' (72,6 -> 70 es redondeo a la decena; 73,7 -> 75 a la 5). P/V se muestra 1,77x con dos decimales cuando sigma del ponderado es ~26 (tesis: ~1,8x). El candado C exige no publicar mas resolucion que el ruido del instrumento.
correccion: JS: anadir const r5=(x)=>Math.round(x/5)*5; y mostrar ponderado y escenarios con '~'+fmt(r5(valor),0) (73,7 -> 75; 72,6 -> 75; 178,5 -> 180), y P/V con fmt(pv,1). Anadir al sub de L399: ' Las cifras se redondean a 5 USD (sigma del ponderado ~26; ~41 el base y ~78 el alcista); la tabla de elecciones conserva decimales solo por trazabilidad.' En la tesis (L24 y L213) cambiar 'Base ~70' por 'Base ~75' para usar una sola convencion.

--- 26
severidad: MEDIO
donde: template.html L386 (callout 'Por que NO por precio')
problema: 'Incluso con la tasa mas generosa (8,0%) el primer tramo seria 106 USD' no aclara que 8,0% es una subtasa de mercado (solo informativa, prohibida por el candado B) ni que 106 depende de MoS 27% (SUPUESTO); la tesis 10.9 admite que con MoS 18% y WACC 8,0% saldria 119 y con MoS 9% y 8,26% 121, es decir alcanzable.
correccion: Sustituir la frase por: 'Incluso con una subtasa de 8,0% (solo informativa: el candado B la prohibe) y un margen de seguridad de 27% (supuesto) el primer tramo seria 106 USD, por debajo del minimo de cierre de 24 meses (114,99, el 24-jul-2026); solo combinando subtasas con margenes de seguridad de 9-18% se llegaria a 119-121.'

--- 27
severidad: MEDIO
donde: template.html L383 (fuente del grafico de precio) y L755
problema: La serie dibujada es la de Yahoo (501 cierres del 15-oct-2024 al 14-oct-2026, identica fecha a fecha a orcl_yh_d2y.json), no la de IBKR (el archivo mercado/ibkr_2026-10-15.md da las barras desde 2024-10-16). 'contrastado con Yahoo en tres puntos de control' no esta documentado: el archivo registra cuatro (cierre 130,55; minimo 114,99; 313,00 del 16-oct-2025; pico 328,33 del 10-sep-2025).
correccion: Sustituir por: 'Fuente: serie de 501 cierres diarios de Yahoo Finance (15-oct-2024 a 14-oct-2026), contrastada con IBKR get_price_history en el cierre (130,55), el minimo (114,99), el 16-oct-2025 (313,00) y el pico (328,33); respuesta de IBKR archivada en mercado/ibkr_2026-10-15.md.'

--- 28
severidad: MEDIO
donde: template.html L354-L358 (M1-M5) y L361
problema: Faltan los amplificadores de gobierno y legales del pre-mortem (tesis 9): G1 pignoracion de Ellison >=450 M o venta >=10 M de acciones; G2 cambio de metricas en la DEF 14A 2027 o say-on-pay <75%; G3 denegacion de la mocion de desestimacion o provision >=500 M. M4 omite el HECHO (sello, V_R8 V8-27) de que Oracle ya alargo la vida util dos veces (4->5 anios en FY23, -434 M de gasto; 5->6 en FY25, -733 M y +573 M de beneficio neto); M3 no dice que el valor razonable de la deuda ya esta en 84,6% del importe en libros (84,2% del nominal), a 4-5 puntos del umbral.
correccion: Anadir tras L358 un bloque: <div class='m'><div class='t'>Gobierno y legal (amplifican, no bastan solos)</div><p>G1 pignoracion de Ellison >=450 M de acciones o venta >=10 M; G2 cambio de metricas de retribucion en la DEF 14A 2027 o say-on-pay <75%; G3 denegacion de la mocion de desestimacion o provision >=500 M.</p></div>. En M4 anadir: ' Oracle ya alargo la vida util dos veces (4->5 anios en FY23 y 5->6 en FY25, +573 M de beneficio neto).' En M3 anadir: ' (hoy 84,6% del importe en libros, 84,2% del nominal).'

--- 29
severidad: MEDIO
donde: template.html L585-L599 (Lagunas)
problema: Faltan lagunas de la tesis: estado de la garantia de 3,3 B (vencia en sep-2026; ya no figura en el 10-Q; solo estaba en los 260 B del 10-K); la ventana de 90 dias de IBKR no muestra operaciones de ORCL entre el 17-jul y el 13-oct (el round-trip del verano no esta verificado ni fechado); las dos rejillas distintas.
correccion: Anadir tres <li>: 'La garantia de hasta 3,3 B a un arrendador (solo en los 260 B del 10-K; vencia en sep-2026) ya no figura en el 10-Q: estado desconocido hasta el 10-Q del 2T FY27.' / 'IBKR (90 dias) no muestra operaciones de ORCL entre el 17-jul y el 13-oct: el round-trip del verano que pediste omitir no esta verificado ni fechado.' / 'Hay dos rejillas margen x intensidad publicadas (resultados_paso9.txt y build_data.py) que difieren hasta 4,4 y 7,0 USD.'

--- 30
severidad: MEDIO
donde: template.html L848 (KPI 'Alcista requerido': 'Imposible')
problema: El KPI dice 'Imposible' mientras res2 (L849) explica que con las correcciones pro-compra el maximo sube a 127-132 y la frontera es 'fragil'. La tesis (10.4): la frase es exacta pero fragil; con 35% de cola el 100% del resto en alcista da 116. 'Imposible' contradice 'fragil'.
correccion: En L848 sustituir 'Imposible' por 'No alcanza' y 'incluso con todo el resto en alcista' por 'con todo el resto en alcista (frontera fragil: 127-132 con las correcciones pro-compra)'.

--- 31
severidad: BAJO
donde: template.html L179 (h1)
problema: 'Oracle dejo de vender software' es falso: el 73% de los ingresos de FY26 (49.256 de 67.357 M) sigue siendo el negocio historico; la tesis lo titula 'el monopolio de software que se convirtio en constructor apalancado'.
correccion: <h1>Oracle sigue vendiendo software, pero lo que justifica su capex y su deuda es otro negocio: construir capacidad de IA. Con deuda.</h1>

--- 32
severidad: BAJO
donde: template.html L201
problema: 'El monologo tiene 44 palabras, no 60.' es una correccion de un borrador anterior que el lector no vio: carece de sentido en la pagina.
correccion: Sustituir por: 'El monologo tiene 44 palabras.'

--- 33
severidad: BAJO
donde: template.html L198 y L200
problema: L198 da '23:21 UTC' como hecho; la tesis 0 dice que las filas 1-2 de SELLOS.md llevan hora redonda puesta a mano y que la cronologia es 'declarada, no atestiguada' (L204 lo reconoce, L198 no). L200 reproduce con tildes y punto final una cita que la tesis llama literal ('suscripcion', 'sin editar').
correccion: L198: 'Paso 0 · sellado el 14-oct (23:21 UTC, hora declarada)'. L200: o bien citar sin tildes ni punto final como en la tesis, o anadir '(ortografia corregida)' tras la cita.

--- 34
severidad: BAJO
donde: template.html L215
problema: 'No explica el negocio que justifica el capex de 55,7 B' presenta como hecho una INFERENCIA: la tesis 1 dice que el 10-K no da capex por segmento ('primarily due to the expansion of our data centers') y que 'OCI' es INFERENCIA.
correccion: Sustituir por: 'No explica el negocio que, por inferencia, justifica el capex de 55,7 B (el 10-K no lo reparte por segmento: dice "primarily due to the expansion of our data centers") ni la ampliacion de capital:'

--- 35
severidad: BAJO
donde: template.html L243
problema: Omite el umbral de vigilancia de la casa (2,5-3,0x) del que habla la tesis 3: la deuda neta/EBITDA LTM de 2,60x ya esta dentro de esa banda.
correccion: Anadir tras '3,54x.': ' El LTM (2,60x) ya esta dentro del umbral de vigilancia de la casa (2,5-3,0x).'

--- 36
severidad: BAJO
donde: template.html L264 y L254
problema: El callout del foso solo recoge el matiz que agrava (Cerner) y omite el que atenua (tesis 4): los 5,4 B miden ingreso cloud ganado, no soporte perdido (el 8-K atribuye la caida a 'migracion continua a la nube'); el '-1% dos trimestres' 'ya se cumple tecnicamente' pero dentro del redondeo. V_R5 R5-05 pide leer -49,7% de licencias como '~-50% entre dos definiciones proximas' (FY14 'new software licenses' frente a FY26 'Software license').
correccion: Anadir al <p> de L264: ' Dos matices en sentidos opuestos: agrava que el soporte orgánico sin Cerner podria caer mas que -1%; atenua que los 5,4 B de cloud migrado son ingreso ganado, no soporte perdido, y que el -1% esta dentro del redondeo. El -49,7% compara dos definiciones proximas de licencia, no una serie homogenea.'

--- 37
severidad: BAJO
donde: template.html L277-L283 (tabla del Paso 4)
problema: La fila FCF mezcla periodos sin rotular (ORCL FY26; Alphabet y Amazon TTM; CoreWeave 6M); 'Deuda/EBITDA' es bruta mientras L243 usa neta; 'Vida util de GPU' es la politica contable de servidores y red; toda la tabla lleva solo HECHO aunque los ratios son INFERENCIA con insumos verificados (V_R6 R6-29); la capex de CoreWeave en efectivo subestima la inversion (11.151 M de pasivos OEM en FY25).
correccion: Etiquetas: 'FCF (ORCL FY26; Alphabet y Amazon TTM; CoreWeave 6M)', 'Deuda bruta / EBITDA', 'Vida util contable de servidores y red'. L283: '<span class='tg h'>HECHO</span> <span class='tg i'>INFERENCIA</span> (ratios)'. Anadir: 'La capex de CoreWeave en efectivo subestima su inversion real en 11.151 M de pasivos de financiacion OEM (FY25).'

--- 38
severidad: BAJO
donde: template.html L286-L288
problema: La lista muestra solo el lado alcista del comportamiento de insiders: omite las ventas discrecionales de la tesis 7 (Magouyrk 60.000; Henley 400.000 a 156-166; ~642.000 acciones entre NEO y consejeros; Ellison y Catz, cero ventas) y que Rusckowski/Henley son DEGRADADOS (Form 4 fuera del corpus; 'unica compra' vale para 14-oct-2025 -> 1-oct-2026).
correccion: Anadir al <li> de L288: ' Ventas de los otros ejecutivos en 12 meses: ~642.000 acciones entre NEO y consejeros, entre ellas 400.000 de Henley a 156-166 (Form 4 fuera del corpus: degradado). "Unica compra" vale para 14-oct-2025 a 1-oct-2026.'

--- 39
severidad: BAJO
donde: template.html L298
problema: 'Con capex devengado: 325%': el 325% suma capex devengado Y activos obtenidos en arrendamientos financieros (solo devengado = 295%; neto de financiacion de proveedores y prepagos = 233%; V_R1 R1-06 y tesis 6).
correccion: Sustituir por: 'Con capex devengado y arrendamientos financieros: 325% (233% neto de financiacion de proveedores y prepagos)'.

--- 40
severidad: BAJO
donde: template.html L343
problema: 'Dos de cada tres dolares... son aumento de diferidos: la mitad, prepagos' es ambiguo: los prepagos son el 49% del CFO (74% del aumento de diferidos), no la mitad del aumento.
correccion: Sustituir por: 'El 66% del CFO del ultimo trimestre es aumento de diferidos: el 49% del CFO son prepagos con componente financiero y el 17% otros diferidos de estacionalidad normal.'

--- 41
severidad: BAJO
donde: template.html L351
problema: 'sellado el 15-oct, 00:02 UTC, antes de calcular ningun valor': la hora (00:02:16Z) es mecanica, pero que el Paso 8 precedio al Paso 9 es 'declarado, no atestiguado' (tesis 0 y 10; la unica cota externa es el commit de las 00:08:32Z, que ya contenia resultados_paso9.txt).
correccion: 'Paso 8 · sellado el 15-oct, 00:02 UTC; que precede a cualquier calculo de valor es declarado, no atestiguado'.

--- 42
severidad: BAJO
donde: template.html L365
problema: Presenta 'mocion de desestimacion totalmente alegada' como evento fechado; V_R8 V8-14b: el texto dice 'if the defendants move to dismiss... fully briefed by December 18, 2026' y el estado tras el 16-sep es DEGRADADO (el 10-Q se firmo el 11-sep). 'El descubrimiento seria la primera fuente externa sobre los contratos de IA' no esta en la tesis (viene del lector R8) y va sin rotular.
correccion: '18-dic-2026 · fin del briefing de desestimacion, si los demandados presentaron la mocion (estado desconocido tras el 16-sep: degradado)'. Demanda colectiva de valores sobre OCI. Anadir <span class='tg i'>INFERENCIA</span> a la frase del descubrimiento o borrarla.

--- 43
severidad: BAJO
donde: template.html L453 y L469
problema: L453 no publica la regla que resuelve el candado C: razon max/min de la matriz 3x3 = 145,3/33,7 = 4,3 > 2,0 (v2 fila 9) -> NO DECIDIBLE, resuelto por la doctrina del Acta B4. L469 dice '12 de 18 elecciones' pero la tabla muestra 10 filas (14 cifras), asi que el lector no puede contarlas.
correccion: L453: anadir ' La razon maxima/minima de la matriz (145/34) es 4,3, por encima de 2,0: no decidible como punto (v2 fila 9); se resuelve con la doctrina del Acta B4, porque la prueba de alcanzabilidad falla igual en todos los puntos.' L469: 'En la tesis (10.3b), 12 de las 18 elecciones documentadas quedan por encima de 2x; aqui se muestran las principales.'

--- 44
severidad: BAJO
donde: template.html L514
problema: 'Efectivo 7.718 USD (5,76%) al 5,21%': 5,21% es el Tesoro a 10 anos (tesis 12 campo 4), no el rendimiento del efectivo; falta el comparador de TIR (base ~6-7%, alcista ~13-16% frente a Ke 11,55%).
correccion: 'Efectivo 7.718 USD (5,76%) frente al 5,21% del Tesoro a 10 anos; TIR de ORCL a 130,55: ~6-7% (base) y ~13-16% (alcista), orden de magnitud, frente a Ke 11,55%; o recortar MELI (20,5% frente al tope de 15%) y DUOL (15,4%)'.

--- 45
severidad: BAJO
donde: template.html L526 y L530
problema: '~55% anualizado' es la cifra de gates.md a 21-ago, no verificable sin IBKR (tesis 12; critico N16); L530 'pierdes +454 USD si ocurre el alcista' es confuso: son 454 USD de ganancia que se dejan de obtener.
correccion: L526: 'frente a ~55% anualizado (cifra de gates.md a 21-ago, no verificada)'. L530: 'dejas de ganar 454 USD si ocurre el alcista (25%)'.

--- 46
severidad: BAJO
donde: template.html L537, L192
problema: 'el tope de 20% que la v2 fijo' es ambiguo porque 'v2' es ahora tambien la version de la tesis (aqui es la Recalibracion v2, fila 16); falta que DUOL (15,4%) tiene un recorte a ~4% sin ejecutar. L192 mezcla 'decide Felipe' con el tuteo del resto de la pagina.
correccion: L537: 'el tope de 20% que la Recalibracion v2 (fila 16) fijo... MELI y DUOL tienen recortes pendientes sin ejecutar (MELI: vender 4 acciones del 24-ago; DUOL: recorte a ~4%)'. L192: 'recomendacion: salir (decides tu)'. Igual 'la regla v2 (C-11)' de L386 -> 'la Recalibracion v2 (C-11)'.

--- 47
severidad: BAJO
donde: template.html L588 y L378
problema: 'con Kd de filing el WACC es 10,12%': el Baa de 6,67% es un indice de FRED (DBAA), no un filing (tesis: 'Kd HECHO (Baa 6,67%)'). L378 omite la estimacion de R7 de que la beta de 60 m sube a ~1,95 en doce meses si nada cambia (la ventana contiene 24 meses 'pre-ciclo'), lo que mueve el WACC central.
correccion: L588: 'con Kd HECHO (indice Baa de FRED, 6,67%) el WACC es 10,12%'. L378: anadir ' R7 estima que la beta de 60 m sube a ~1,95 en doce meses si nada cambia.' y rotular '(rf y ERP HECHO; beta y Kd INFERENCIA)'.

--- 48
severidad: BAJO
donde: template.html L425 y L429
problema: El titulo del widget habla de 130,55 pero el slider de precio arranca en 130 (paso 1): los resultados por defecto (54,2%/78,2%/73,2%) son para 130, no 130,55 (tesis: >=55% y 27% a 130,55).
correccion: Cambiar el titulo a '¿Que tienes que creer para que 130 sea justo?' o inicializar con JS $('s_px').value=130.55 y step='0.05'.

--- 49
severidad: BAJO
donde: template.html L286, L755 y L758 (maximos)
problema: Hay tres 'maximos' sin conciliar: 345 (maximo intradia mensual de sep-2025, L286), 328,33 (maximo de cierre de la serie, 10-sep-2025, L755) y 313,00 (maximo de cierre de 52 semanas, usado para el -58%).
correccion: En L286: '(el maximo intradia fue 345; el maximo de cierre en 24 meses, 328,33; el de 52 semanas, 313,00)'.

--- 50
severidad: BAJO
donde: template.html L499
problema: 'ambos se instanciaron ad hoc' es inexacto: la tesis 11 dice que el angel fue ad hoc (no existe abogado-angel.md) pero el diablo si existe como agente y no declara tools, por lo que heredo todas las herramientas.
correccion: 'el abogado angel no existe como agente en .claude/agents/ (se instancio ad hoc) y el del diablo no declara tools: heredo todas las herramientas.'

--- 51
severidad: BAJO
donde: template.html L190
problema: El KPI 'Asimetria' omite el escenario base (-44%, peso 40%) y el ponderado (-44%) que la tesis publica junto al alcista +37% y bajista/colapso -100%.
correccion: '+37% / -44% / -100%' con d: 'alcista (+5% si el retorno marginal terminal = WACC) / base / bajista y colapso; ponderado -44%'.

--- 52
severidad: BAJO
donde: template.html L331
problema: El src del grafico CFO lleva solo HECHO, pero 'los prepagos no se convierten en ingreso a 12 meses' es una inferencia por clasificacion del balance (tesis 8: no se sostiene por los ~4,0 B reconocidos por trimestre).
correccion: Anadir <span class='tg i'>INFERENCIA</span> al final del src y escribir 'lo indica' como 'se infiere de'.

--- 53
severidad: BAJO
donde: template.html L243 / L455 / L704 (acciones y capitalizacion)
problema: Tres recuentos de acciones sin explicar: 3.031 M (DEF 14A, L704), 398 B de capitalizacion con 3.050 M (motor, L455) y 395 B/3.024 M (10-Q, cabecera de la tesis).
correccion: L455: 'Capitalizacion 398 B (3.050 M acciones del motor; 395 B con las 3.024 M del 10-Q)'. L704: 'Propiedad de Oracle (3.031 M de acciones con voto, DEF 14A a 21-sep)'.

--- 54
severidad: BAJO
donde: template.html L864 (preset 'beta') y L403
problema: El preset 'Beta de 36 m (13,1%)' reproduce solo el extremo crudo (ponderado 35,0, P/V 3,7x); la tesis publica 11,6-13,1% (Blume 51,5 / cruda 34,7).
correccion: Anadir un preset 'beta-blume': {wacc:11.63,k:1,dm:0,di:0,w:[10,25,25]} con el rotulo 'Beta de 36 m con Blume (11,6%)'.

--- 55
severidad: BAJO
donde: template.html L396-L399 (simulador, cola)
problema: Los presets 'base-rate' y 'guia' son legitimos, pero el simulador no avisa de que la tesis fija el 35% de cola como SUPUESTO sin base en la clase de referencia (V8-38).
correccion: Anadir al sub de L399: ' La cola de 35% (colapso + bajista) es un supuesto: la tasa de mortalidad de la clase de referencia no es usable como porcentaje.'

--- 56
severidad: BAJO
donde: template.html L204
problema: Menor: dice 'un commit de las 00:08 UTC que ya contenia los resultados del Paso 9' sin la fecha ni el hash (la tesis cita 82ff5a1, 2026-10-15T00:08:32Z).
correccion: '... un commit del 15-oct a las 00:08:32 UTC (82ff5a1) que ya contenia los resultados del Paso 9.'
