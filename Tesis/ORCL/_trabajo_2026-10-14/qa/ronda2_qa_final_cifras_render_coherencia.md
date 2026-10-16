

##### AGENTE a8360da3fb20496f7
RESUMEN: QA solo lectura, scripts y capturas en /tmp/qa_final_cifras/. El artefacto publicado se reconstruye idéntico (cmp) desde template.html + motor.js + orcl_data.json. Las cifras del artefacto coinciden con la tesis y las fuentes locales, con las excepciones de abajo: 20 hallazgos (1 ALTO, 6 MEDIO, 13 BAJO), todos con defecto reproducido o verificado y corrección exacta. No hay restos activos de 71–94, 52–68, 1,77× como titular, 9,4% como suelo, «casi cero cola» ni 66% como prepagos. Aparecen solo como historia retirada o dentro de la tabla de elecciones, que es legítimo.

Reproducido y correcto:
- Simulador por defecto (WACC 10,26%, pesos 10/25/40/25): ponderado 73,68, que redondeado a 5 da 75 y coincide con el héroe. Escenarios −25,4 / −3,8 / 72,6 / 178,5, y p/v 1,77.
- Preajustes (JS en Node y Chromium contra motor_orcl.py con python3 -I, idénticos):

| Preajuste | Ponderado | Redondeo a 5 | p/v |
|---|---|---|---|
| Tasa de mercado | 73,68 | 75 | 1,77 |
| ERP 3,70% (9,7%) | 85,72 | 85 | 1,52 |
| β 36 m (13,1%) | 35,00 | 35 | 3,73 |
| Pesos de tasa base | 50,54 | 50 | 2,58 |
| 100% alcista | 178,51 | 180 | 0,73 |
| β 36 m Blume (11,63%) | 51,51 | 50 | 2,53 |

- Banda 71,0 (10,4%) a 85,7 (9,7%). P_tramo1 52–63 / 58–70 / 65–78 (MoS 27/18/9%). 97 con WACC 8,26% y 106 con 8,0%.
- P_justo requerido 114,99 / 126,4 / 140,2 / 157,5, con WACC máximo 8,73 / 8,43 / 8,11 / 7,77%.
- Candado C: 129/137/145 · 67/73/78 · 34/38/43, razón 4,3.
- DCF inverso 79,1% y ×1,289. Monte Carlo media 78,9, σ 25,5, p5 42, p95 124, P(>precio) 3,5%.
- Tabla 10.3b: g∞ 3,0% → 66,1; Enm. 29 → 63,0; capex 40% → 54,4; pesos 12/25/50/13 → 59,5; SBC 3/5/7,1% → 57,8 / 47,2 / 36,1; RONIC=WACC → 56,1; combinado → 38,4.
- Escenarios: OCI FY27–FY36, EV, CAGR 26,9% / 19,0% y FCF por año coinciden con la tesis.
- Port JS contra Python: dVPS máximo 5,8e-14.
- XBRL, IBKR archivado, FRED y Yahoo: RPO, CFO, capex, TTM (46,94 / 75,66 / −28,72), cartera, 3.031 M de acciones, 328,33 el 10-sep-2025, 313,00 el 16-oct-2025, 114,99 el 24-jul-2026, 501 cierres, volumen ≈1,8×.
- Reportes de Candado A: ángel +4 a +14 contra +84, bloqueantes B1–B5 del crítico, 39 hechos del 10c, 12 incumplimientos y 13 ambigüedades del auditor de reglas, y los conteos de V_R1 a V_R8.

No pude verificar:
- Respuestas originales del MCP de IBKR (solo la transcripción archivada) y sec.gov o Form 4 (no accesibles, como en la ronda previa).
- ERP y β de Damodaran, say-on-pay 81,9%, Kd secundario y cifras de prensa.
- Que los seis revisores no vieran los informes de los demás: solo el crítico lo declara por escrito.
- Los 125 B de déficit hasta FY29 (derivación del diablo, no reproducida).
- Maquetación, contraste y accesibilidad (fuera de mi rol).

--- 0
severidad: ALTO
donde: /home/user/inversiones/Tesis/ORCL/_trabajo_2026-10-14/artefacto/template.html l.864 (JS render(), nota wnote); se propaga a artefacto_orcl.html al reconstruir
problema: El preajuste «ERP 3,70% (≈9,7%)», que la tesis define como el suelo legítimo de la banda, muestra «WACC por debajo del suelo de mercado (9,7%): subtasa solo informativa; el candado B la prohíbe». Reproducido en Chromium: botón erp y slider a 9,70 y 9,69. Causa: st.wacc = 9.7/100 = 0.09699999999999999, que es < 0.097. El artefacto acusa de violar el candado B a su propio preajuste.
correccion: En template.html reemplazar `(st.wacc<0.097?` por `(Math.round(st.wacc*1e4)<970?`. Reconstruir con `python3 build_artifact.py` desde la carpeta artefacto/.

--- 1
severidad: MEDIO
donde: /home/user/inversiones/Tesis/ORCL/_trabajo_2026-10-14/artefacto/template.html l.846 (valsFig, gráfico «Valor por acción de cada escenario y ponderado»)
problema: El gráfico muestra enteros sin redondear a 5 (por defecto: Base 73, Alcista 179, Ponderado 74), mientras las tarjetas y el resumen muestran ≈75 / ≈180 / ≈75. Contradice la frase del propio widget («Las cifras se redondean a 5 USD») y el candado C: falsa precisión con σ≈26. Capturado en Chromium.
correccion: Reemplazar `const txt=Math.round(v)<=0?'0':fmt(v,0);` por `const txt=Math.round(v)<=0?'0':'≈'+fmt(r5(v),0);`. r5 ya está definida en el mismo scope antes de la primera llamada.

--- 2
severidad: MEDIO
donde: Tesis /home/user/inversiones/Tesis/ORCL/2026-10-14_UltraTesis_ORCL_metodo12.md l.28 (Cuadro, DCF inverso) y l.257 (§10.4); template.html l.869 y l.870 (widget 2, «¿Qué tienes que creer…?»)
problema: «Con las correcciones pro-compra del auditor de modelo, 127–132» es incorrecto: 10_auditor_modelo.md §6 da 127,3 / 131,5 / 135,6 (el techo con WACC 10,12%), es decir 127–136, y los dos últimos superan 130,55. Además el artefacto imprime esa cifra fija con cualquier WACC, cola o precio. Reproducido con el preajuste β 36 m: «máximo 62 con las elecciones de la casa; … el máximo sube a 127–132».
correccion: Tesis, ambas líneas: «con las correcciones pro-compra del auditor de modelo, 127–136 (127,3 / 131,5 / 135,6; los dos últimos superan 130,55)». Artefacto: construir `const frag=(Math.abs(st.wacc-.1026)<5e-4&&Math.abs(tail-.35)<.005)?' (a WACC 10,26% y 35% de cola, el auditor de modelo obtuvo 127–136 con correcciones pro-compra)':'';` y usarlo en lugar del texto fijo «127–132» de la tarjeta (l.869) y de res2 (l.870).

--- 3
severidad: MEDIO
donde: template.html l.877 (render3, «Lupa del precio»)
problema: Paréntesis fijo «con desplazamiento paralelo … baja a ≈70–73% a 130,55 USD» calibrado a WACC 10,26%, pero se imprime con cualquier tasa o precio. Con el preajuste erp el texto dice «margen terminal de 71% … el umbral baja a ≈70–73%», lo que es incoherente porque 71% ya está dentro de ese rango.
correccion: Mostrar el paréntesis solo si `Math.abs(st.wacc-.1026)<5e-4&&Math.abs(px-130.55)<1`; en otro caso omitirlo.

--- 4
severidad: MEDIO
donde: template.html l.859 (render(), texto de «pasa»)
problema: El texto fijo «con la tasa de mercado solo se logra con ≥80% de peso alcista» solo vale para el WACC central. Reproducido: con 9,70%, colapso 0, bajista 0 y alcista 70%, el simulador marca «Pasa» (≈170) y repite la frase. Con el resto en base, el mínimo es ≈60% a 9,7% y ≈85% a 10,4%.
correccion: Reemplazar «con la tasa de mercado solo se logra con ≥80% de peso alcista o con una tasa ≤7,8%» por «con la tasa central (10,26%) solo se logra con ≥80% de peso alcista, con el resto en base (≈60% con 9,7%, ≈85% con 10,4%), o con una tasa ≤7,8%».

--- 5
severidad: MEDIO
donde: Tesis l.425 (P6), template.html l.576 y l.586 (P6 y factor D), propuestas/PREREGISTRO_2T_FY27_ORCL.md (P6), ADENDA (factor D) y DIARIO_borrador (falsable)
problema: Se presenta «1T FY27: 54,5%; 1T FY26: 59,6%» como valores de la «tabla MD&A». El 10-Q 1T FY27 imprime «Total Margin % 55% | 60%» (enteros). 54,5% y 59,6% son cálculo propio: 9.358/17.157 y 7.691/12.907. Un lector del 2T FY27 comparará enteros con un umbral de 52,5%, y el falsable duro queda ambiguo.
correccion: Sustituir por: ««Total Margin %» del segmento (la tabla del 10-Q imprime enteros: 1T FY27 55%, 1T FY26 60%; calculado como Total Margin $ ÷ (Total Margin $ + Total expenses): 54,5% y 59,6%). Umbral ≤52,5% calculado, equivalente a ≤52% impreso; ≥54,5% calculado, equivalente a ≥55% impreso». Aplicar en los cinco documentos.

--- 6
severidad: BAJO
donde: template.html l.441 (slider s_px de widget 2) y l.866/870/871 (fmt(px,0))
problema: El precio de entrada por defecto es 130 (paso 1), no 130,55. Con cola 0%, el widget muestra «54%» mientras el héroe y la tesis dicen ≥55% (54,7% a 130,55). Reproducido: 130 → 54%, 131 → 55%.
correccion: En el input cambiar `step="1" value="130"` por `step="0.05" value="130.55"` y sustituir `fmt(px,0)` por `fmt(px,2)` en l.866, 870, 871.

--- 7
severidad: BAJO
donde: template.html l.489 (Paso 10)
problema: «los cinco leen las reglas como «mantener sin añadir» … (con tu firma y un falsador escrito antes del dato)» atribuye a los cinco jueces una condición que, según la tesis §11, añade solo el juez de posición.
correccion: Reemplazar el paréntesis por: «(el juez de posición añade que solo es defendible con tu firma y un falsador de puerta 1 escrito antes del dato)».

--- 8
severidad: BAJO
donde: template.html l.198 (KPI «Cierre 14-oct»)
problema: «−58% desde el máximo de cierre (313,00)». El artefacto dice en el Paso 4 que el máximo de cierre en 24 meses es 328,33 (10-sep-2025); 313,00 (16-oct-2025) es el de 52 semanas. Dos «máximos de cierre» distintos sin rotular.
correccion: «−58% desde el máximo de cierre de 52 semanas (313,00); −60% desde el de 24 meses (328,33)».

--- 9
severidad: BAJO
donde: template.html l.190 (párrafo lead del héroe)
problema: «alquilar capacidad de IA … y rinde como mucho su coste de capital» atribuye a OCI un retorno que no está medido: la tesis (§4) dice que el margen real de OCI «Oracle no lo desglosa». El ≤10,5% es el ROIC incremental del grupo FY23→FY26.
correccion: Reemplazar «y rinde como mucho su coste de capital» por «y el capital nuevo del grupo ha rendido como mucho su coste (ROIC incremental ≤10,5% frente a un WACC de 10,26%)».

--- 10
severidad: BAJO
donde: template.html l.367 (M4)
problema: «4→5 años en FY23 y 5→6 en FY25, +573 M de beneficio neto» sugiere +573 M para ambos cambios. Según V_R1 R1-23 y el pre-mortem sellado, 573 M es solo el efecto de FY25; el cambio de FY23 redujo el gasto en 434 M.
correccion: «(4→5 años en FY23: −434 M de gasto; 5→6 años en FY25: −733 M de gasto y +573 M de beneficio neto; 10-K FY25, Nota 1)».

--- 11
severidad: BAJO
donde: template.html l.372 (falsador «Sellado»); propuestas/ADENDA_gates_ORCL_2026-10-15.md l.12 (F3); propuestas/DIARIO_borrador_ORCL_2026-10-15.md l.7
problema: Los tres omiten «o al alza por las tres agencias» del punto 3 sellado (paso8_premortem.md; tesis l.182 «rating estable o al alza»). El addendum y la tesis sí lo llevan.
correccion: Artefacto: «rating estable o al alza y emisión a 10 años ≤UST + 150 pb». ADENDA: «F3 rating estable o al alza por las tres agencias y emisión a 10 años ≤UST + 150 pb». DIARIO: «rating estable o al alza por las tres agencias y emisión ≤UST+150 pb».

--- 12
severidad: BAJO
donde: propuestas/ADENDA_gates_ORCL_2026-10-15.md l.14, l.20 y l.32
problema: (a) «16 en §13 de la tesis» pero la tesis lista 17 decisiones. (b) «+38% frente a 130,55» cuando la tesis dice +37% (178,5; el 180 es redondeo a 5). (c) MELI «~31-ago (51 d)»: 51 d son días desde la orden del 24-ago; desde la caducidad ~31-ago son 44 d, y las otras filas cuentan desde el vencimiento.
correccion: (a) «17 en §13». (b) «≈180 USD/acc. (178,5 sin redondear; +37% frente a 130,55 …)». (c) «~31-ago (44 d; la orden lleva 51 d sin ejecutar)».

--- 13
severidad: BAJO
donde: Tesis l.45 (§0)
problema: «44 palabras; `wc -w` sobre el archivo sellado». `wc -w paso0_inclinacion_monologo.txt` da 82 por los encabezados; 44 es solo el cuerpo del monólogo.
correccion: «(sin editar, 44 palabras contadas sobre el texto del monólogo; `wc -w` sobre el archivo sellado completo, con encabezados, da 82):»

--- 14
severidad: BAJO
donde: Tesis l.113 (§4, SAP HANA 2015)
problema: Cita el soporte FY17 como 19.230 M; el XBRL y V_R5 corrigen a 19.229, que es la cifra que usa la propia tesis dos párrafos después (l.119, «19.229 M (FY17)»).
correccion: «(18.847 → 18.861 → 19.229 M FY15-FY17)».

--- 15
severidad: BAJO
donde: Tesis l.327 (tabla Candado A, fila 10c)
problema: «11 cifras del texto contradicen un filing o su aritmética». El 10c (§0) cuenta 10 (E1–E10); E11 es una inferencia degradada, no una contradicción.
correccion: «… 3 degradados; 10 cifras del texto contradicen un filing o su aritmética (E1–E10) y una inferencia presentada junto a un HECHO queda degradada (E11)».

--- 16
severidad: BAJO
donde: Tesis l.431 (§13)
problema: «lo aprueba Felipe antes del 20-nov-2026, 10 sesiones antes del reporte». Del 20-nov al 10-dic hay 13 sesiones (el festivo del 26-nov no cuenta); 10 sesiones atrás es el 25-nov, como dicen PREREGISTRO y ADENDA («≈23/25-nov»).
correccion: «antes del 20-nov-2026 (≈13 sesiones antes del reporte; la ventana de la fila 22 empieza ≈25-nov)».

--- 17
severidad: BAJO
donde: Tesis l.220 (§10.2) y §10.10 punto 5 («≈2,34%») frente a la tabla 10.3b y template.html (2,35%)
problema: El tope de la Enmienda 29 aparece como 2,34% y como 2,35%. FRED T10YIE del 14-oct es 2,35%, y la tesis usa 2,35% para el software. Con 2,34% el ponderado es 62,9 y con 2,35% 63,0.
correccion: Unificar a «≈2,35%» (T10YIE 14-oct) en l.220 y en §10.10 punto 5.

--- 18
severidad: BAJO
donde: /home/user/inversiones/Tesis/ORCL/_trabajo_2026-10-14/mercado/ibkr_2026-10-15.md l.41
problema: «501 barras diarias del 2024-10-16 al 2026-10-14». Entre esas fechas hay 500 sesiones NYSE (calendario con festivos, incluido el 9-ene-2025). La serie Yahoo archivada tiene 501 sesiones completas del 2024-10-15 al 2026-10-14 sin huecos. Un dato del archivo está mal: la fecha inicial o el conteo.
correccion: Verificar contra la respuesta de IBKR. Si la serie es la misma, escribir «501 barras diarias del 2024-10-15 al 2026-10-14»; si empieza el 16-oct, «500 barras».

--- 19
severidad: BAJO
donde: template.html (figura ROIC, serie v, FY22 = 19,0) y Tesis §3
problema: El punto FY22 (19,0%) incluye el cargo de litigio de 4.700 M; R1 §d.2 da ≈27,2% sin él (NOPAT 12.501/45.916). El gráfico y la narrativa de caída desde 28,7% no lo señalan.
correccion: Añadir al pie de la figura: «FY22 incluye un cargo de litigio de 4.700 M; sin él ≈27,2% (R1 §d.2, INFERENCIA)».


##### AGENTE ac41a1f21083e8575
RESUMEN: QA de render y funcionalidad de artefacto_orcl.html, hecho con Playwright/Chromium 1194, red bloqueada salvo file:/data:, HTML envuelto en doctype+charset+viewport. Probé 1280 y 400 px en claro y oscuro, más 320, 360, 375, 390, 414, 600, 768 y 1024 px. Verifiqué que el artefacto es idéntico a template.html + motor.js + orcl_data.json reconstruido (byte a byte). El repo queda intacto (git status limpio); mis scripts y capturas están en el directorio de scratchpad .../scratchpad/qa_final_render/.

Resultado de los 9 puntos.
(1) PASA. Cero errores de consola en las 4 combinaciones; solo falla la carga de Google Fonts, bloqueada a propósito.
(2) PASA. scrollWidth = clientWidth en los 8 anchos, también tras 192 combinaciones extremas del simulador.
(3) PASA. «Pasos» abre el índice visible con la página desplazada a 0, 5.000 y 15.000 px; el panel recibe los clics. El índice cubre las 17 secciones, ninguna sin enlace. Cada enlace aterriza con el título bajo la barra sticky. Escape lo cierra.
(4) PASA, con una salvedad (hallazgo 4). Los 6 preajustes funcionan, incluido «Beta de 36 m con Blume» (WACC 11,63%, ponderado ≈50, coherente con el 51,5 de la tabla). Probé 192 esquinas más 400 combinaciones aleatorias, sin NaN, undefined, Infinity ni «−0», sin probabilidades negativas o >100%, sin TIR en los bordes del bracket y sin texto desbordado. Las probabilidades de peso, cola y «alcista requerido» están bien acotadas.
(5) PASA para el texto HTML: 0 fallos AA en 4 combinaciones, incluidas las del índice abierto y los .tg. Una etiqueta SVG falla (hallazgo 5).
(6) PASA salvo lo de los hallazgos 2 y 3: 0 choques o recortes de etiquetas en las 11 figuras. Lo comprobé con bbox y también con DejaVu Sans como proxy de la Poppins ancha (Poppins no está instalada, se usó la de respaldo Inter). La fila «Cadena de IA» y la línea de tope de 20% se ven bien.
(7) PASA. Bandas «71–86» y «52–63» (consistentes con 71×0,73 y 86×0,73); ROIC TTM como barra 10,8–13,5; los datos de pico, máximo de 52 s y mínimo coinciden con orcl_data.json.
(8) PASA con una salvedad: las figuras avisan con «Desliza…» y la barra de resumen sticky existe y no choca con la barra superior. La dirección de la flecha en figPrice es incorrecta (hallazgo 6).
(9) FALLA (hallazgo 1).

Hallazgos, de mayor a menor: 1 tablas ilegibles (ALTO), 2 etiqueta recortada en figVals (MEDIO), 3 cifras sin redondear (MEDIO), 4 a 9 son BAJOS. Todos los parches los probé en una copia parcheada de template.html en scratchpad (build en wrapped_patched.html) y funcionan. Los números de línea son de template.html; artefacto_orcl.html se regenera con build_artifact.py.

No pude verificar: (a) Safari/WebKit, solo hay Chromium. Al abrir «Pasos» el panel crece 157 px en flujo y Chromium lo compensa con scroll anchoring (scrollY pasó de 5000 a 5157); en un navegador sin scroll anchoring el contenido saltaría. Mitigación: position:absolute en .top .idx. (b) La tipografía real Lora/Poppins (bloqueada). (c) Contraste sobre el desenfoque del fondo de la barra .top (backdrop-filter). (d) El `<html lang>` que pone el publicador, el artefacto no lo trae. (e) Gestos táctiles reales; usé viewport emulado, no un dispositivo.

--- 0
severidad: ALTO
donde: template.html líneas 96 y 98 (CSS de tablas) y 284 (tabla Paso 4); afecta también a las tablas de los Pasos 10, 11, 12 y a «Elecciones documentadas»
problema: td.n tiene white-space:nowrap y varias celdas .n llevan frases largas, así que el Paso 4 mide 883 px y el Paso 11 («Coste de equivocarse») 788 px frente a un contenedor de 672 px, ya en 1280 px: las columnas Microsoft, Alphabet y Amazon, y «Si vendes», quedan fuera sin aviso (ej. «dejas de ganar 454 USD si ocurre…» cortado). Además la primera columna se aprieta en 5 líneas de ~70 px. En 400 px el Paso 4 solo muestra «Métrica» y un trozo de «RPO sin desglose…»: la columna ORCL no se ve. Por min-width:30rem, las tablas de los Pasos 10 y 12 y la de elecciones miden 480 px frente a 368 px útiles, con frases truncadas a media palabra y sin ninguna señal de desplazamiento (el aviso «Desliza…» solo existe para .fig .scroll.sc; getComputedStyle(::after).content = none en esos .scroll).
correccion: 1) Línea 98: sustituir `.scroll>table:not(.heat){min-width:30rem}` por `.scroll>table.wide{min-width:30rem}\n.scroll>table:not(.heat) td.n{white-space:normal}`. 2) Línea 284: `<table class="tight">` por `<table class="tight wide">` (solo la tabla del Paso 4). 3) Línea 92: añadir el aviso a las tablas anchas: `.fig .scroll.sc::after,.scroll:has(>table.wide)::after{...misma regla...}`. Probado: a 1280 las 5 tablas no desbordan; a 400 las tablas de los Pasos 10, 11, 12 y la de elecciones caben en 368 px con el texto envuelto; el Paso 4 desplaza con aviso y muestra la columna ORCL.

--- 1
severidad: MEDIO
donde: template.html línea 841-846, función valsFig (etiqueta «precio 130,55» y eje); aparece con los preajustes «Beta de 36 m (13,1%)» y «Beta de 36 m con Blume (11,6%)»
problema: La etiqueta `text x=x(PRECIO)+5` no cabe y se recorta: a 400 px ocupa x=265..338 sobre un viewBox de 329 (se ve «precio 130,5»). Reproducido a 320, 360, 375, 390, 400 y 414 px; con los dos preajustes beta (incluido el nuevo de Blume) y con combinaciones extremas. Además, con valores altos (mx>440, p. ej. WACC 8, k 1,3, margen +10, capex −8) las etiquetas del eje 50/100/150/200/250/300/350 se solapan a 400 px (192 solapes en la barrida) y el eje se detiene en 350 aunque las barras lleguen a 800.
correccion: Reemplazar la línea `s.appendChild(el('text',{x:x(PRECIO)+5,y:12,style:'fill:var(--clay-ink);font-weight:700'},'precio 130,55'));` por `{ const lx=x(PRECIO), fl=lx+5+90>W; s.appendChild(el('text',{x:fl?lx-5:lx+5,y:12,'text-anchor':fl?'end':'start',style:'fill:var(--clay-ink);font-weight:700'},'precio 130,55')); }`. Y la línea `const ticks=[0,50,100,150,200,250,300,350].filter(t=>t<=mx);` por `const step=mx>400?100:50, ticks=[]; for(let t=0;t<=mx;t+=step) ticks.push(t);`. Verificado a 320, 400 y 414 px con los 6 preajustes y con el extremo: 0 recortes y 0 solapes.

--- 2
severidad: MEDIO
donde: template.html línea 846 (valsFig, etiquetas de barra) frente a línea 410 (texto «Las cifras se redondean a 5 USD…») y a r5() usado en tarjetas, barra de resumen y KPIs
problema: El gráfico de valores muestra 73 (base), 179 (alcista) y 74 (ponderado) mientras que las tarjetas, el KPI y la barra mini muestran ≈75, ≈180 y ≈75. Contradice la promesa de redondeo a 5 del propio widget y el piso de resolución (σ≈26): falsa precisión en la misma pantalla, con cifras distintas para la misma cantidad. Preajuste beta: figura 28/95/35 frente a ≈30/≈95/≈35.
correccion: Línea 846: `const txt=Math.round(v)<=0?'0':fmt(v,0);` por `const txt=Math.round(v)<=0?'0':'≈'+fmt(r5(v),0);` (r5 está definida antes de la primera llamada a render). Verificado: la figura pasa a «≈75 | ≈180 | ≈75».

--- 3
severidad: BAJO
donde: template.html línea 866 (render2) y línea 876 (render3)
problema: Estos widgets usan el valor crudo del motor, mientras compute() y las tarjetas lo recortan a 0 (equity ≥ 0). Con WACC 13,5, crecimiento ×0,6, margen −10 pp y capex +8 pp el widget 2 muestra «MÁXIMO ALCANZABLE −18 USD» (−27 con cola 0%, −11 con cola 60%) y el widget 3 «VALOR AL MARGEN DEL MODELO −43 USD», pero la tarjeta dice «valen 0 (el modelo da −43)». Con base<0<alcista (65 combinaciones en la rejilla) la fórmula de «alcista requerido» mezcla un base negativo que el ponderado no usa.
correccion: Línea 866: `const va=res.sc.alcista.vps, vb=res.sc.base.vps;` por `const va=Math.max(res.sc.alcista.vps,0), vb=Math.max(res.sc.base.vps,0);`. Línea 876: `<div class="v">${fmt(vps(base),0)}</div>` por `<div class="v">${fmt(Math.max(vps(base),0),0)}</div>`. Verificado: esos casos pasan a mostrar 0 y «No alcanza».

--- 4
severidad: BAJO
donde: template.html línea 763 (figPrice, etiqueta «Primer tramo 52–63»)
problema: Contraste medido en píxeles, tema claro: 4,16:1 (texto 11 px semibold, mínimo AA 4,5:1). Es clay-ink sobre clay-bg (4,28:1 sin más), oscurecido por el área de precio al 5% que se pinta encima de las bandas. «Valor ponderado 71–86» queda en 4,53:1, al límite. Tema oscuro: bien. El texto HTML no tiene ningún fallo.
correccion: En la línea 763 cambiar `style:'fill:var(--clay-ink);font-weight:600'` por `style:'fill:var(--ink);font-weight:600'` (medido tras el parche: 13,7:1). Opcional: dibujar el path de área (opacity .05) antes de las bandas.

--- 5
severidad: BAJO
donde: template.html línea 648 (mount, opt.end) y línea 92 (CSS del aviso)
problema: figPrice se abre desplazada al final (scrollLeft=252 de 252 a 400 px), pero el aviso dice «Desliza para ver el resto →». Lo que queda por ver está a la izquierda (mínimo de 24 m, «Pico…»), y la etiqueta «Mínimo de cierre 24 m: 114,99 · 24-jul-2026» no se ve hasta desplazar.
correccion: En mount: `if(!opt.fit){ w.classList.add('sc'); if(opt.end) w.classList.add('en'); ...`. En la línea 92 añadir dentro del @media: `.fig .scroll.sc.en::after{content:'← Desliza para ver el resto';text-align:left}` antes de la regla general. Verificado: figPrice muestra «← Desliza para ver el resto».

--- 6
severidad: BAJO
donde: template.html línea 894 (handler de resize) y línea 648 (mount, replaceChildren)
problema: El handler de resize vuelve a renderizar todo aunque solo cambie el alto (en móvil la barra de URL dispara resize al desplazar), y mount() recrea el scroller en cada render, incluido cada movimiento de slider. Reproducido a 400 px: scrollLeft de figPaths 150 pasa a 0 tras un resize solo de alto (400×800 a 400×860) y también tras mover cualquier slider; el usuario pierde su posición de lectura.
correccion: Línea 894: `let _rw=0; window.addEventListener('resize',()=>{ clearTimeout(_rw); _rw=setTimeout(()=>read(),150); });` por `let _rw=0,_lw=window.innerWidth; window.addEventListener('resize',()=>{ clearTimeout(_rw); _rw=setTimeout(()=>{ if(window.innerWidth!==_lw){ _lw=window.innerWidth; read(); } },150); });`. En mount: `w.appendChild(svg); c.replaceChildren(w);` por `w.appendChild(svg); const sl=(c.querySelector('.scroll')||{}).scrollLeft||0; c.replaceChildren(w); w.scrollLeft=sl;`. Verificado: scrollLeft se conserva (150) en ambos casos.

--- 7
severidad: BAJO
donde: template.html línea 648: `svg.style.minWidth='620px'` (viewBox de 760)
problema: En móvil las figuras desplazables se escalan a 0,816: las etiquetas de 11 px se ven a 9,0 px y las de 10,5 px (ejes) a 8,6 px, medido con getBoundingClientRect/viewBox en las 10 figuras con scroll; a 1280 son 13 px. Es poco legible en pantallas de 400 px (figVals, que no tiene minWidth, se ve a 11 px).
correccion: Cambiar `svg.style.minWidth='620px'` por `svg.style.minWidth=svg.viewBox.baseVal.width+'px'` (escala 1,0, etiquetas a 11 px; hay que deslizar algo más, con el aviso ya existente). Verificado: scrollWidth del documento sigue en 400 y las 10 figuras pasan a 11 px efectivos.

--- 8
severidad: BAJO
donde: template.html línea 117 (.ctrl label output) y línea 423 (slider «Margen EBITDA de OCI (pp sobre cada escenario)»)
problema: El valor «+0,0 pp» se parte en dos líneas («+0,0» / «pp») porque el label largo comprime el output flex. Reproducido a 1280, 400 y 360 px (Range.getClientRects: 2 filas); el resto de los outputs queda en una línea.
correccion: Línea 117: `.ctrl label output{font-weight:600;` por `.ctrl label output{white-space:nowrap;font-weight:600;`. Verificado: 1 fila en los tres anchos.


##### AGENTE a31442904fd6255fb
RESUMEN: Auditoría de solo lectura, sin ningún defecto CRÍTICO. La dirección del veredicto (NO por precio, compra nueva 0%) no depende de ninguno de los defectos listados. Verifiqué lo siguiente.
- Los 4 sha256 de SELLOS.md coinciden con los archivos, y esos archivos no cambian en git desde 82ff5a1.
- gates.md, diario-decisiones.md, CLAUDE.md y ADN-QG12.md no cambian entre 5058604 y HEAD, y no hay cambios fuera de Tesis/ORCL.
- Las tablas markdown (5 archivos) tienen columnas consistentes y no hay `**` impares.
- Reproduje con una copia del motor, en /tmp/qa_final_coherencia/: 73,7 / 72,6 / 178,5, la matriz 129/137/145…, los umbrales de WACC 8,73/8,43/8,11/7,77, el ponderado 85,7 a WACC 9,7%, los pesos 59,5 y 50,5, y los P_tramo1 por bloque de MoS. El cruce exacto del ponderado con 130,55 está en WACC ≈8,33%. También cuadran las 18 filas de §10.3b (12 por encima de 2×) y la aritmética de caja, ROIC, posición y cartera.
- Cotejé ≈25 filas de la tabla del §11 con los informes originales. Son fieles, salvo los puntos indicados abajo. Las horas y los hashes de §11 coinciden con el mtime y el sha256 de los archivos.
- La caducidad 2027-10-14 es coherente en todos los archivos.

Los defectos están sobre todo en los satélites (adenda, addendum del sello, preregistro, diario), en rótulos heredados de la v1 y en incumplimientos de reglas de la casa (filtro Munger, etiquetas, puerta 1).

No pude verificar:
- el contenido de la URL del artefacto;
- sec.gov y los Form 4;
- el Treasury del 14-oct y Damodaran;
- IBKR en vivo (solo el archivo archivado);
- la historia de 10 años de ORCL, que no está en el repo;
- las salidas de los 5 jueces, que no están archivadas;
- el contenido del artefacto HTML, que quedó fuera de este rol. Solo comprobé que su lista de decisiones tiene 17 puntos.

--- 0
severidad: ALTO
donde: Tesis/ORCL/sellos_2026-10-14/paso8_addendum_falsador_2026-10-15.md l.5, l.9 y l.22; Tesis l.182
problema: El addendum atribuye al sello cosas que el sello no contiene. `paso8_premortem.md` (sha256 394a30fe…) no tiene ninguna «revisión anticipada» ni «cierre ≤68»: grep «68» y «anticipada» sobre el sello da 0 coincidencias relevantes. El punto 3 («revisión anticipada (a)… imposible por fechas») y la frase de l.22 «La versión sellada decía «cierre ≤ 68»» describen la v1 de la tesis §12 (`candadoA/entrada_v1_2c00625e.md` l.283), que no estaba sellada. La tesis l.182 repite el encuadre. Como el addendum se sella como archivo nuevo (C1), el error quedaría congelado.
correccion: En el addendum: l.5 «Qué estaba mal en el falsador sellado y en la revisión anticipada de la v1 de la tesis»; l.9 «3. La «revisión anticipada (a)» de la v1 de la tesis (§12; NO está en `paso8_premortem.md`) era mecánicamente imposible por fechas…»; l.22 sustituir «La versión sellada decía «cierre ≤ 68»» por «La v1 de la tesis (§12, no el sello) decía «cierre ≤ 68»». En la tesis l.182 sustituir «y la «revisión anticipada» por el 8-K del 2T FY27 era imposible por fechas» por «y la «revisión anticipada (a)» de la v1 de la tesis (no del sello) era imposible por fechas». Corregir ANTES de sellar el addendum.

--- 1
severidad: MEDIO
donde: Addendum del sello l.26 («Qué NO cambia») y tesis l.179 (fila M5 de la tabla §9)
problema: Citan el umbral sellado de M5 como «soporte ≤−3% cc dos trimestres, o ≤−1% tres trimestres sin cifra de migración; SaaS <+7%». El sello dice «SaaS <+7% cc dos trimestres» y «tres trimestres consecutivos». Al omitir «dos trimestres» en SaaS, el addendum subestima cuánto relaja el factor B, que justamente pretende declarar la relajación del M5 sellado.
correccion: En el addendum l.26 y en la tesis l.179 escribir: «soporte ≤−3% cc dos trimestres consecutivos; o ≤−1% cc tres trimestres consecutivos sin cifra de migración en dólares; SaaS <+7% cc dos trimestres». Y en el factor B: «relaja AMBAS patas del M5 sellado (soporte −3% y SaaS <+7%) de dos trimestres a uno».

--- 2
severidad: MEDIO
donde: ADENDA_gates_ORCL_2026-10-15.md l.13; tesis l.6; addendum l.3
problema: La adenda dice «el pre-registro sellado», pero SELLOS.md solo tiene 4 filas: ni PREREGISTRO_2T_FY27_ORCL.md ni la tesis v2 ni el addendum (que vive dentro de sellos_2026-10-14/) figuran sellados. El propio PREREGISTRO y la tesis §13 dicen que se sella «antes del reporte». La tesis l.6 («Esta versión se sella como archivo nuevo») y el addendum («se sella con sellar.sh») están en presente aunque no está hecho. Además, P6 se llama «pre-registrada» en un archivo sin hash.
correccion: ADENDA l.13: «…y en el pre-registro (`propuestas/PREREGISTRO_2T_FY27_ORCL.md`, aún sin sellar; se sella con `sellar.sh` antes de ≈23-nov)». Tesis l.6: «Esta versión se sellará como archivo nuevo…». Ejecutar, desde sellos_2026-10-14/, `./sellar.sh paso8_addendum_falsador_2026-10-15.md "Addendum Paso 8: falsador observable + P6"` y los equivalentes para la tesis v2 y el PREREGISTRO, una vez corregidos los demás hallazgos (sellar congela los errores).

--- 3
severidad: MEDIO
donde: ADENDA l.11 (frase «recomendación del método = salir del lote») y PREREGISTRO_2T_FY27_ORCL.md (última línea: «Recomendación del método: salir del lote»)
problema: Contradice la tesis. Allí las reglas literales solo autorizan «mantener sin añadir» (5 de 5 jueces; default del 20-nov) y «salir» es la recomendación del asistente, vía test del hoy del ADN («mi recomendación es salir… El método no me deja ejecutarla», l.10). La adenda es el texto que iría a gates.md y diría que el método recomienda salir mientras en la misma línea dice que B4 impide vender.
correccion: ADENDA l.11: «**Posición de 9 acc.: recomendación del asistente (test del hoy, ADN) = salir del lote; las reglas literales solo autorizan mantener sin añadir** (puerta 2 indeterminada y bloqueada por B4; puerta 1 en el umbral…)». PREREGISTRO: «Recomendación del asistente (test del hoy): salir del lote; las reglas literales autorizan mantener sin añadir; decisión de Felipe.»

--- 4
severidad: MEDIO
donde: ADENDA l.14
problema: «Decisiones de Felipe pendientes (16 en §13 de la tesis…)». §13 numera 17 decisiones (la última, «Regla contra las compras sin tesis»), y el artefacto también lista 17.
correccion: Sustituir «16 en §13» por «17 en §13».

--- 5
severidad: MEDIO
donde: Tesis l.420 (P1) y PREREGISTRO_2T_FY27_ORCL.md (P1): «<8,0 B = M2 activo (bajista/colapso)»
problema: M2 sellado exige «OCI FY27 <30.000 M» o «dos trimestres con crecimiento interanual <60%» (o margen <50%, CIP). Con la propia tabla de la tesis (l.208) el bajista da 31,7 B y el colapso 30,8 B en FY27, ambos ≥30.000: ni el bajista dispara M2. Un 2T FY27 de 7,9 B es +93% sobre los 4,1 B del 2T FY26, lejos del <60% (6,5 B). Rotular «<8,0 B» como «M2 activo» es incorrecto.
correccion: Reemplazar por: «<8,0 B = señal de bajista/colapso según la senda de esta tesis (umbral propio de P1; NO es el umbral sellado de M2, que en el 2T equivaldría a <6,5 B por crecimiento interanual <60%, o a OCI FY27 <30.000 M)». Aplicar igual en el PREREGISTRO y revisar el artefacto.

--- 6
severidad: MEDIO
donde: ADENDA l.11 (factor A) frente a tesis l.429 y PREREGISTRO (factor A)
problema: La adenda define el factor A como «OCI 2T FY27 <8,0 B o RPO a la baja». La tesis y el PREREGISTRO dicen «RPO a la baja secuencial sin atribución». La versión de la adenda, que es la que se aprobaría en gates.md, dispara con cualquier baja del RPO, incluso atribuida a reconocimiento ordinario (que M1 sellado excluye).
correccion: ADENDA l.11: «A: OCI 2T FY27 <8,0 B o RPO a la baja secuencial sin atribución».

--- 7
severidad: MEDIO
donde: Tesis (todo el documento): falta el «Filtro Munger»; ADN-QG12.md (sección «Cuando la conversación pasa a decisión de capital»)
problema: El ADN exige «Filtro Munger antes de todo veredicto nuevo: incentivos, invertir el problema, redundancia, punto de no retorno». grep «Filtro» en la tesis da 0 resultados; Munger aparece solo en una cita en §7. Las demás tesis método-12 (DUOL 13-oct, CME, CLX, CPRT, DSG…) llevan sección «Filtro Munger (antes del veredicto)». Redundancia y punto de no retorno no están tratados como tales.
correccion: Insertar antes de §12 (o al inicio de §12): «**Filtro de Munger (ADN).** *Incentivos:* PSO pagan por ingresos non-GAAP FY2028, cero métricas de ROIC/FCF/deuda/dilución (§7; HECHO, DEF 14A 2026). *Invertir:* el equity se pierde por contraparte que no convierte el contrato en caja (M1) o por cierre del acceso a financiación (M3), no por covenant (§9, §10.10). *Redundancia:* ninguna en FCF (−28,7 B TTM); caja+inversiones 37,1 B; el legado cubre las cargas fijas ≈1,4× (INFERENCIA, §8). *Punto de no retorno:* 288 B de arrendamientos firmados no iniciados de 15–19 años y 34,2 B de compras incondicionales (HECHO, 10-Q Nota 6) más ≈20 B de captación FY27 sin tipo definir: compromisos que Oracle no puede deshacer si el cliente incumple.»

--- 8
severidad: MEDIO
donde: Tesis l.10, l.397, l.403 y ADENDA l.11 (puerta 1) frente a gates.md l.447–449
problema: La tesis presenta la puerta 1 como la «vía formal» para vender el lote si J5 = NO. Pero gates.md define puerta 1 como «knock-out disparado, o motor apagado» y añade (l.449): «Si la calidad sigue intacta, se recorta a tamaño de vigilancia en vez de liquidar». La tesis no menciona esa cláusula (grep «vigilancia» = 0 en ese sentido), aunque el crítico la planteó (informe, sección d, pregunta 10) y la tabla del §11 no tiene fila de disposición. Que J5 = NO equivalga a «tesis rota» no figura en el texto de la regla. A 0,86% la posición ya está por debajo de cualquier tamaño de vigilancia.
correccion: En l.10 sustituir «la puerta 1 abre solo si Felipe responde NO a la pregunta J5 sobre OCI» por «la puerta 1 solo abriría si Felipe decide que J5 = NO equivale a «tesis rota» (el texto de la puerta no lo prevé: knock-out o motor apagado)». En §12 (tras «Puerta 3…») añadir: «Nota: gates.md l.449 prescribe, si la calidad sigue intacta, «recortar a tamaño de vigilancia en vez de liquidar»; a 0,86% del NAV la puerta 1 no ordena liquidar el lote.» Añadir fila al §11: «Puerta 1 sin cláusula de tamaño de vigilancia (crítico d.10) | D3 | Aceptada; §12».

--- 9
severidad: MEDIO
donde: Tesis l.83 (§2, fila «$66B en SPVs») y l.100 (§3, fila VIE); FUENTES l.480
problema: Inconsistencia entre secciones sobre la cobertura de VIE. §2 dice «No hay VIE… en 35 documentos EDGAR FY17-1T FY27 (…HECHO por ausencia)» sin reserva. §3 dice «35 declarados; 27 verificables» pero conserva «documentos EDGAR locales FY17–1T FY27». V_R1 (R1-13) confirma solo 27 documentos locales (FY25–1T FY27) y el veredicto es DEGRADADO fuera de ellos. FUENTES ya dice que FY17–FY24 son «solo vía XBRL». El crítico (N9) pidió la reserva en §2 y §3.
correccion: l.83: «…en los 27 documentos locales FY25–1T FY27 (35 declarados por el lector, no reconciliados; V_R1 R1-13: DEGRADADO fuera de esos 27); HECHO por ausencia solo con esa cobertura». l.100: sustituir «locales FY17–1T FY27» por «locales FY25–1T FY27».

--- 10
severidad: MEDIO
donde: Tesis l.290 (§10.9, «Sesgo de fecha declarado»)
problema: «en una ventana de 10 años ORCL cerró en ≈61 (sep-2022) y P_tramo1 pasaría a «alcanzable»». La serie mensual archivada (mercado/orcl_yh_m.json) cubre solo 6 años (nov-2020→oct-2026); su mínimo mensual es 57,72 (nov-2020), no 61,07 (sep-2022). La ventana de 10 años no está en el repo, así que la cifra no es reproducible. Además «alcanzable» no vale para todo P_tramo1: con mín. 61,07 solo lo sería la parte alta del bloque 27% (52–63), y sí el 18% (58–70) y el 9% (65–78).
correccion: «Sesgo de fecha declarado (C6, fuera de alcance): la serie mensual archivada (nov-2020→oct-2026, 6 años) tiene cierre mensual mínimo 57,72 (nov-2020) y 61,07 (sep-2022); con esa ventana `P_tramo1` sería alcanzable con MoS 9% y 18% (58–78) y solo en el tramo alto con 27% (52–63). La ventana de 10 años no está archivada (NO VERIFICADO). La etiqueta «por precio»…»

--- 11
severidad: MEDIO
donde: Tesis l.373 (panel de 5 jueces)
problema: El resultado «5 de 5 emiten NO por precio… 5 de 5 leen las reglas como mantener sin añadir» no tiene ningún archivo en el repo: candadoA/ solo contiene los 6 informes. Los jueces y su código constan solo en el scratchpad y workflow de la sesión, fuera del repo. §11 documenta con hash los 6 revisores, pero no el panel que sustenta la precedencia «reglas = mantener».
correccion: Añadir al final de l.373: «Los informes de los 5 jueces no están archivados en el repo (constan en el workflow de la sesión, sin hash): su resultado 5/5 es declarado, no verificable desde el repo». Mejor aún, archivar sus salidas en `candadoA/panel_jueces/` con sha256 antes de sellar.

--- 12
severidad: MEDIO
donde: Tesis, párrafos sin ninguna etiqueta HECHO/INFERENCIA/SUPUESTO/SECUNDARIO/DEGRADADO (p. ej. l.113 «57 B de fondo de comercio», l.115 «5,4 B de ingreso cloud», l.142, l.148, l.160, l.164, l.263, l.274, l.405)
problema: CLAUDE.md: «Todo dato lleva etiqueta». Un awk sobre l.41–450 encuentra 46 párrafos de más de 400 caracteres sin ninguna etiqueta. Entre ellos hay cifras densas: §7 propiedad/pignoración (l.148), §8 múltiplos y yields (l.160), caja prestada (l.164), §10.5 EV implícito (l.263), §10.7 (l.274), cartera IBKR (l.405). La auditoría de reglas (4.2) ya señaló EV/EBITDA 16,7×, 5,4 B y 57 B; siguen sin etiqueta.
correccion: Añadir cola de etiqueta a cada bloque. Ejemplos exactos: l.148 «…(HECHO: DEF 14A 2026 accn 0001193125-26-402816 y DEF 14A 2025 accn 0001193125-25-220801)»; l.160 «(HECHO: precio y guía de la empresa; INFERENCIA: EV con 3.050 M acc., múltiplos y yields)»; l.163/164 «(HECHO: 10-Q 1T FY27; INFERENCIA: lectura de «caja prestada»)»; l.263 «(INFERENCIA sobre HECHO: EV con 3.050 M acc. y reclamaciones del puente)»; l.405 «(HECHO: IBKR 15-oct, archivo mercado/ibkr_2026-10-15.md)»; l.113 «57 B de fondo de comercio (HECHO, 10-K FY26 Nota)»; l.115 «5,4 B (SECUNDARIO: pre-mortem sellado, sin cita de filing)».

--- 13
severidad: MEDIO
donde: Tesis l.425 (P6), DIARIO_borrador l.7, addendum del sello l.30
problema: Residuo de la v1. P6 dice «salir del lote sin exigir un segundo factor» (diario: «sin segundo factor»; addendum: «sin exigir un segundo factor»). En v2 basta UN factor para todos (A–D), así que la frase sugiere que A–C sí exigen un segundo y contradice «Basta uno» de l.429 y «salida con un factor» de l.10.
correccion: Sustituir en los tres sitios por «salir del lote (basta este factor, como con A–C)». Diario: «⇒ salir del lote (factor D; basta uno)».

--- 14
severidad: BAJO
donde: ADENDA l.31, l.33 (filas de tabla) y tesis l.393
problema: La propia adenda (l.3) y la fila 23 exigen un token `[CADUCA: AAAA-MM-DD]` por línea viva y al final de la línea. En l.31 (DUOL, `[CADUCA: 2026-11-04]`) y l.33 (MSFT, `[CADUCA: 2026-10-29]`) el token queda en mitad de la celda y la línea termina en «| Felipe |». En la tesis l.393 el token va envuelto en `**…**`. Un `grep -E '\[CADUCA: [0-9-]+\]`?$'` no los encuentra (solo 6 líneas de la adenda cumplen: 9, 11, 12, 17, 20, 23).
correccion: Mover los tokens de DUOL y MSFT a líneas propias de lista al final del texto (p. ej. «- DUOL: renovación 2/2 propuesta. `[CADUCA: 2026-11-04]`») y dejar la tabla sin token. Tesis l.393: «Campo 6, token canónico: [CADUCA: 2027-10-14]» sin negritas, o dejar solo el token en su línea.

--- 15
severidad: BAJO
donde: ADENDA l.32
problema: «~31-ago (51 d)» mezcla dos conteos. 31-ago→14-oct son 44 días; 51 días son desde la orden del 24-ago (el vigía lo cuenta así). Las otras filas cuentan desde el vencimiento (DUOL 47, MSFT 77, FDS 14, verificados).
correccion: «~31-ago (44 d vencida; 51 d sin ejecutar desde la orden del 24-ago)».

--- 16
severidad: BAJO
donde: ADENDA l.20 (libro de omisiones)
problema: «≈180 USD/acc. (+38% frente a 130,55…)». La tesis usa 178,5 → +37% (cuadro de mando y §10.8). Además la fila lleva fecha 2026-10-15 con precio 130,55, que es el cierre del 14-oct, y caducidad 2027-10-14.
correccion: «caso alcista máximo registrado: ≈178,5 USD/acc. (+37% frente a 130,55; TIR ≈13–16%)» y «2026-10-15 (marca; precio = cierre 14-oct 130,55)».

--- 17
severidad: BAJO
donde: ADENDA l.2
problema: «como las adendas del 6-sep y 14-sep, que siguen pendientes». gates.md l.2 y l.60 listan tres adendas pendientes: 6-sep, 14-sep y 13-oct.
correccion: «como las adendas del 6-sep, 14-sep y 13-oct, que siguen pendientes».

--- 18
severidad: BAJO
donde: ADENDA l.38
problema: «El calendario de lecturas, la fila 22 (…) y el pre-registro de P1–P6 están en la tesis §9 y §13». La tesis no contiene «fila 22» ni «calendario de lecturas» (grep = 0). La ventana de la fila 22 está en PREREGISTRO l.2 y en el calendario del pre-mortem sellado.
correccion: «…están en el pre-registro (`propuestas/PREREGISTRO_2T_FY27_ORCL.md`) y en el calendario de `sellos_2026-10-14/paso8_premortem.md`; la tesis §9 y §13 solo da las ventanas por mecanismo y P1–P6.»

--- 19
severidad: BAJO
donde: ADENDA l.11
problema: Formato roto: se abre «{A: …» y se cierra con «)» tras «2T FY27»; la línea tiene 2 «(» y 3 «)», y ninguna «}».
correccion: Sustituir «…≤52,5% en el 10-Q del 2T FY27); extensión propuesta» por «…≤52,5% en el 10-Q del 2T FY27}; extensión propuesta».

--- 20
severidad: BAJO
donde: Tesis l.25 (cuadro de mando, «Banda y ruido»)
problema: «el precio solo cruza el valor con WACC ≈8,26% (1,1 pp bajo el piso de cualquier tasa admisible)». El 1,1 pp venía del piso 9,4% de la v1; con el piso v2 de 9,7% son 1,4 pp (9,7−8,26; el cruce exacto del ponderado con 130,55 está en 8,33%, reproducido con el motor).
correccion: «(≈1,4 pp bajo el piso de 9,7%; el cruce exacto del ponderado está en WACC ≈8,33%)».

--- 21
severidad: BAJO
donde: Tesis l.45
problema: «44 palabras; `wc -w` sobre el archivo sellado». `wc -w paso0_inclinacion_monologo.txt` da 82 (incluye la cabecera). 44 es el recuento de la línea del monólogo.
correccion: «44 palabras; `wc -w` sobre la línea del monólogo (el archivo completo con cabecera da 82)».

--- 22
severidad: BAJO
donde: DIARIO_borrador_ORCL_2026-10-15.md l.12
problema: «≈12,77 USD de P&L según `gates.md`». gates.md no contiene 12,77: su l.514 solo agrega «ORCL el mismo día» dentro de ~$42 netos. La cifra viene de la Recalibración v2 (L24 y L282) y del vigía.
correccion: «(≈12,77 USD de P&L según la Recalibración v2, L24/L282; `gates.md` l.514 solo lo agrega dentro de ~$42 netos)».

--- 23
severidad: BAJO
donde: Tesis l.388 (§12 campo 3)
problema: «Acta 22-ago». El Acta declara que su fecha es el 23-ago (nombre de archivo 22-ago). La tesis usa «Acta 23-ago» en l.10, l.339 y l.397.
correccion: «Acta 23-ago (archivo `_Refundacion/2026-08-22_Acta_Activacion_B4.md`)».

--- 24
severidad: BAJO
donde: Tesis l.431 (§13, «antes del 20-nov-2026, 10 sesiones antes del reporte»)
problema: 20-nov no está a 10 sesiones del reporte. Con reporte el 10-dic y cierre el 26-nov y 25-dic, la ventana de 10 sesiones abre el 25-nov y el 20-nov queda 13 sesiones antes. El PREREGISTRO y la adenda dicen «≈23/25-nov»; el 20-nov es el límite conservador del vigía.
correccion: «antes del 20-nov-2026 (límite conservador del vigía; la ventana de la fila 22 abre ≈23/25-nov)».

--- 25
severidad: BAJO
donde: Tesis l.56
problema: La secuencia «si tengo 9 acciones que compre en 130» → «Solo hazlo!» → «omite eso» invierte el orden del archivo sellado `declaraciones_felipe_2026-10-14.txt`, que numera 1) Solo hazlo!, 2) 9 acciones, 3) omite eso. El diablo usó el mismo orden alterado; el archivo no prueba cuál fue el cronológico.
correccion: Escribir la secuencia en el orden numerado del archivo sellado («Solo hazlo!» → «si tengo 9 acciones que compre en 130» → «omite eso»), o añadir «(orden de la numeración del archivo sellado; la cronología exacta no está atestiguada)».

--- 26
severidad: BAJO
donde: Tesis l.327 y l.329 (tabla de §11, fila 10c)
problema: Dos errores en esa fila. Primero, «11 cifras del texto contradicen un filing o su aritmética»: 10c dice 10 cifras (E1–E10) y E11 va aparte como DEGRADADO. Segundo, la etiqueta «10c» designa a la vez al verificador de hechos nuevos y, en l.6 y l.329, al «cruce 10c» de Felipe, que en la Recalibración v2 fila 17 es el cruce de la bicameral.
correccion: «10 cifras del texto contradicen un filing o su aritmética (+1 degradada: E11)». Renombrar el agente: «Verificador de hechos nuevos (D1; archivo `10c_…`, no es el cruce 10c de la fila 17)».

--- 27
severidad: BAJO
donde: Tesis l.224 y l.401
problema: Dos redondeos. (1) «0,25 × 0,77 + 0,40 × 0,11 ≈ 23%» da 23,65%; con los valores de §10.2 (76,8% y 10,6%) da 23,4%. (2) «Mantener solo se justifica con P(alcista) ≥55%» se compara con vender a 128,11; con ese precio el umbral es 52,4% (54,7% es el de 130,55 del DCF inverso).
correccion: (1) «0,25 × 0,768 + 0,40 × 0,106 ≈ 23,4%». (2) «Mantener solo se justifica con P(alcista) ≥52% frente a vender a 128,11 (≥55% frente a 130,55)».

--- 28
severidad: BAJO
donde: Tesis l.318 y l.201
problema: l.318: «cada uno escribió únicamente su informe». El auditor de modelo dejó además ≈20 scripts y salidas en `candadoA/auditor_modelo/` (su informe lo dice). l.201: cita el script `wacc.py` del lector, que no está en el repo (vive en el scratchpad de R7).
correccion: l.318: «cada uno escribió su informe (el auditor de modelo además dejó sus scripts y salidas en `candadoA/auditor_modelo/`)». l.201: «el script `wacc.py` del lector (no archivado en el repo)».
