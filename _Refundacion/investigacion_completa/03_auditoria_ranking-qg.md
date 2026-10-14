# AUDITORÍA — ranking-qg

## Resumen
La skill `ranking-qg` está bien escrita y mal fundada: su ingeniería (regla de autoridad, diff tipado, disciplina del Tramo 3) es correcta y determinista —reproduje el output del 07-11 byte a byte— pero opera sobre una base que no controla y produce una decisión que no soporta. El libro mayor NO es la fuente única de verdad: PG, CL y CLX tienen Tesis Ultra en disco y están ausentes del ledger; las 9 tesis de `tesis-forja` (oro por su propia especificación) jamás se ingirieron; SPOT se editó a mano el 07-19 sin pasar por el sync, así que el changelog —la promesa central de la skill— nunca vio la corrección más grande de su historia. Y la única salida decisoria, el Tramo 3, entregó 2 de 12 nombres, uno de los cuales (CSU.TO, +19% MoS en el ledger) está contradicho por su propia tesis-forja del 07-14 (−41,6%). Los 24 puestos restantes son ordenación por debajo del ruido del instrumento: inyectando σ=2.45 en los scores del ledger actual, el Tramo 2 conserva 6,8 de 12 miembros.

## Hallazgos
### [HECHO] El Tramo 1 vs Tramo 2 es 43% ruido — el corte en el puesto 12 no existe

**Detalle:** Monte Carlo propio (N=2000) sobre el ledger real, inyectando el σ=2.45 del propio instrumento en cada calidad.score y re-corriendo el comparador exacto de `clave_orden` (build_ranking.py:66-78): el Tramo 1 conserva en media 10,04/12 miembros (mín 7) y el Tramo 2 solo 6,82/12 (mín 3). El conjunto top-24 sí es robusto (20,5/24), pero la PARTICIÓN en dos tramos —que es el producto editorial— no lo es. Desplazamientos máximos de posición: NEM.DE 30 puestos, TYL 33, MANH 36. En el top-30 actual, 12 de 29 gaps entre vecinos son exactamente 0,0 y el gap medio es 0,55 pts, contra σ=2.45.

**Fuente:** Computado por mí sobre /Users/felipealvarez/Library/Mobile Documents/com~apple~CloudDocs/INVESTMENTS/Rankings/_ledger.json (85 tickers, meta.actualizado 2026-07-19), con el comparador de build_ranking.py:66-78

**Implicación para el método nuevo:** La estructura de 'tramos' hay que eliminarla, no recalibrarla. Cualquier método nuevo que ordene por un escalar y luego corte en un puesto fijo reproduce este artefacto. Si algo se conserva, que sea una lista sin orden interno declarado (un conjunto 'estudiadas y aprobadas') o un orden por una magnitud con dispersión real (el MoS lo tiene: va de +35,8% a −283%).

### [HECHO] El 'libro mayor, fuente única de verdad' no contiene lo que hay en disco

**Detalle:** Comparé las 59 carpetas de `Tesis/` contra el ledger: CL, CLX y PG tienen carpeta de Tesis Ultra y están AUSENTES del ledger; EFX, SOON.SW, TOI.V y WISE.L tienen tesis en disco pero figuran como `plata` (no oro). Además hay 9 tesis de `tesis-forja` sueltas (tesis-ALC-2026-07-14.md, tesis-CSU.TO-2026-07-14.md, tesis-FDS, tesis-INTU-2026-07-13, tesis-LMN.TO, tesis-MA-2026-07-11, tesis-MSFT-2026-07-11, tesis-SGSN.SW, tesis-WISE.L), todas posteriores al último sync (07-11 14:06) y ninguna ingerida — pese a que ledger.md:56 las declara ORO. El sync solo informa de los records que alguien le da: no existe ningún chequeo de cobertura tesis-en-disco vs ledger, ni bandera de omisión.

**Fuente:** Rankings/_ledger.json vs ls Tesis/ (59 carpetas + 9 .md de forja); Skills/ranking-qg/references/ledger.md:56 y :140-149; ledger_sync.py:343-402 (no hay opción de verificación de cobertura)

**Implicación para el método nuevo:** El fallo dominante de un libro mayor no es el dato erróneo, es la omisión silenciosa — y esta arquitectura es ciega a ella por construcción. Cualquier registro que se conserve necesita invertir la dirección: partir del corpus de documentos en disco y reportar qué falta, no partir de records entregados a mano y suponer que están todos.

### [HECHO] La única recomendación real del ranking está contradicha por su propia tesis

**Detalle:** El Tramo 3 —'las infravaloradas', la única salida que produce una decisión— entregó 2 de 12: WKL.AS y CSU.TO. El ledger da CSU.TO precio zona OPORTUNIDAD, MoS +19%, autoridad plata, fecha 2026-07-10. Cuatro días después, `Tesis/tesis-CSU.TO-2026-07-14.md` (tesis-forja = ORO por ledger.md:56) concluye ESTADO VIGILAR con MoS −41,6%. Mismo caso en MA: ledger JUSTO +6,3%; tesis-MA-2026-07-11.md dice MoS −9,7%. Ninguna de las dos correcciones entró al ledger, y el changelog no las menciona porque nunca existieron como score record.

**Fuente:** Rankings/_ledger.json (CSU.TO.precio, MA.precio); Tesis/tesis-CSU.TO-2026-07-14.md; Tesis/tesis-MA-2026-07-11.md; salida de build_ranking.py sobre el ledger actual: 'Tramo 3 (2/12): WKL.AS, CSU.TO'

**Implicación para el método nuevo:** La regla de autoridad es correcta en el papel y falsa en los hechos: en el caso más importante del tablero, el screening plata le ganó a la tesis oro porque la tesis nunca se ingirió. La precedencia explícita que Felipe quiere para el método nuevo debe ir acompañada de un mecanismo que DETECTE la evidencia de mayor autoridad, no de uno que la espere.

### [HECHO] tesis-forja como fuente oro es inimplementable tal como está especificada

**Detalle:** ledger.md:56 y :145 declaran las tesis forjadas fuente ORO. Pero el formato de score record que el sync entiende (ledger.md:151-160) está construido enteramente sobre la portada de una Tesis Ultra: exige `score /100` y `tier`. Los diarios de tesis-forja no producen ninguno: grep de '/100' en tesis-ALC, tesis-MA y tesis-CSU.TO devuelve 0 ocurrencias en los tres. Producen ESTADO (VIGILAR/PASO), MoS, asimetría y gatillo falsable — otro vocabulario. El ledger no tiene campo para nada de eso. Por eso ninguna forja se ingirió: no es descuido, es incompatibilidad estructural.

**Fuente:** grep -c '/ ?100' en Tesis/tesis-{ALC,MA,CSU.TO}-*.md → 0,0,0; Skills/ranking-qg/references/ledger.md:56, :145, :151-160

**Implicación para el método nuevo:** El sistema tiene dos gramáticas de conclusión incompatibles: 'score/tier/zona' (Seilern) y 'estado/asimetría/gatillo' (forja). El método nuevo tiene que elegir UNA. Dado el propósito declarado —entender, valorar, escribir tesis— la gramática de forja (asimetría, gatillo falsable, owner earnings) es la que sirve; la de score/tier es la que ya sabemos que es ruido.

### [HECHO] La compuerta anti-sesgo nunca ha degradado nada: 58 de 59 banderas son una constante

**Detalle:** Recorrí todos los flags_ingesta del ledger: 59 banderas en total, de las cuales 58 son `anti-sesgo-divulgacion-no-auditada` y 1 es `mos-dudoso`. Cero degradaciones. La bandera dominante se añade incondicionalmente a TODO record no-oro (ledger_sync.py:153, sin ninguna condición previa) — es decir, no aporta información: repite lo que ya dice la insignia PLATA/PROVISIONAL, y el propio build lo admite y la oculta (build_ranking.py:230-236, comentario: 'no se pinta (es ruido)'). De los tres chequeos declarados en ledger.md:113-136, el nº2 está explícitamente NO automatizado (ledger.md:129), el nº3 es esa constante, y el nº1 (aritmética) jamás disparó — coherente con el hallazgo de la auditoría de que la aritmética está limpia (error máx 0,02 en 191 filas).

**Fuente:** Conteo propio sobre Rankings/_ledger.json; ledger_sync.py:123-154 y :153; build_ranking.py:230-236; references/ledger.md:113-136

**Implicación para el método nuevo:** Es el equivalente exacto de una regla con ρ leave-one-out = 0,99: 24 líneas de código, 24 líneas de documentación y un nombre imponente ('compuerta') para un paso que no ha cambiado ni una conclusión. Se tira entero. La lección que sí transfiere: los tres bugs que la motivaron (doble conteo, tope disparejo, deterioro de divulgación) son cualitativos y solo los caza una lectura dedicada — que es precisamente lo que Felipe dice querer hacer.

### [HECHO] La política de frescura nunca ha disparado, y su gatillo de drawdown contradice Calidad≠Precio

**Detalle:** Los snapshots de las dos únicas corridas reales (2026-07-10 y 2026-07-11) tienen `"refrescar": {}` — vacío. No existe ningún fichero de feed de precios en todo el árbol de Rankings/, así que el gatillo de drawdown ha estado inactivo el 100% del tiempo (build_ranking.py:169 `drawdown_activo: bool(precios)`). Y el gatillo de antigüedad no puede disparar: las fechas del ledger van de 2026-07-02 a 2026-07-19 y el umbral es 90 días. Peor: el fallback implementado en build_ranking.py:57 y frescura_eje(..., precio_ref) hace que la caída del PRECIO marque como stale el score de CALIDAD — reconocido en ledger.md:105-107 como 'cobertura parcial'. Eso contradice de frente la doctrina propia (tramos.md:69-73 y CLAUDE.md: 'Calidad y precio son dos preguntas separadas').

**Fuente:** Rankings/2026-07-10/snapshot_2026-07-10.json y 2026-07-11/snapshot_2026-07-11.json ('refrescar': {}); build_ranking.py:42-63, :169; references/ledger.md:92-111

**Implicación para el método nuevo:** Toda la sección de frescura —umbral de 90 días, gatillo de 25%, insignias REFRESCAR, parámetro --stale-dias, la discusión de divisa nativa— es maquinaria que jamás se ejecutó. Se tira. Si el método nuevo quiere caducidad, el gatillo útil no es el calendario sino el evento: se relee una tesis cuando se rompe el supuesto que la sostenía (que es lo que forja llama gatillo falsable), no cuando pasan 90 días.

### [HECHO] El changelog: la mitad es cosmética y el evento más informativo va marcado como aviso

**Detalle:** changelog_2026-07-11.md tiene 30 líneas; 15 son reescrituras cosméticas del campo `sector` (p.ej. '...Ciberseguridad'→'Ciberseguridad (Palo Alto Networks)'), que `CAMBIO_TIPOS` (ledger_sync.py:340) cuenta como CAMBIO REAL y el HTML pinta arriba del ranking. El debut del mecanismo, changelog_2026-07-10.md, son 376 líneas de siembra fundacional (149 'NUEVO', 131 reemplazos de autoridad, 72 líneas de sector). En cambio, `actualizacion-fecha` —una re-puntuación que devuelve exactamente el mismo contenido, o sea el único dato de acuerdo test-retest que el sistema genera— está clasificada como AVISO (ledger_sync.py:373) y se escribe precedida de 'AVISO ·'.

**Fuente:** Rankings/2026-07-11/changelog_2026-07-11.md (30 líneas, 15 de sector); Rankings/2026-07-10/changelog_2026-07-10.md (376 líneas); ledger_sync.py:340 y :373

**Implicación para el método nuevo:** La taxonomía de cambios está invertida respecto a lo que importa: eleva metadatos a cambio y degrada la reproducibilidad a ruido de fondo. Si algo del diff se conserva, hay que reclasificar: 'el número no se movió al re-verificar' es la señal más valiosa que este sistema ha producido nunca y ahora está enterrada.

### [HECHO] Colisión de enrutamiento: dos skills reclaman 'SIEMPRE' el mismo disparador, y ya ocurrió

**Detalle:** La descripción de ranking-qg (SKILL.md:3) dice: 'Úsala SIEMPRE que Felipe pida el ranking, rankear el universo, las mejores empresas QG'. La de qg-seilern dice: 'Úsalo SIEMPRE que Felipe pida rankear empresas por calidad... armar un ranking QG o las mejores empresas del mundo'. Evidencia de que la colisión se materializó: Rankings/2026-07-08/ contiene un `Ranking_QG_3Tramos_2026-07-08.{csv,html,pdf}` con un esquema CSV completamente distinto (tramo,orden,ticker,sector,score_100,score_R1..score_R11) y un CSS con modo oscuro — no lo produjo build_ranking.py (cuyo CSV es tramo,orden,ticker,nombre,sector,calidad,tier,calidad_proc,...). Dos tuberías distintas escribieron el mismo nombre de archivo. Resultado: MA aparece #1 con 86,4 el 07-08 y #12 con 74,8 el 07-11.

**Fuente:** Skills/ranking-qg/SKILL.md:3; Skills/qg-seilern/SKILL.md:3-9; head de Rankings/2026-07-08/Ranking_QG_3Tramos_2026-07-08.{csv,html} vs Rankings/2026-07-11/Ranking_QG_3Tramos_2026-07-11.csv

**Implicación para el método nuevo:** La separación 'esta skill ordena, aquella puntúa' es una convención declarada que el enrutador no puede hacer cumplir. En una refundación con menos piezas el problema desaparece solo; si se mantiene más de un artefacto, la frontera tiene que ser de datos (quién escribe qué fichero), no de descripción.

### [HECHO] El artefacto que Felipe tocó por último contradice el ledger y usa una rúbrica prohibida

**Detalle:** Ranking_Cruzado_QGxMoS_v4_2026-07-10.md (modificado 07-13 19:47, exportado a PDF el 07-14 11:45 — DESPUÉS del último build del 07-13 14:07) contradice el ledger en: V (Caro, MoS −34,0, nota 'CORREGIDO: peaje inflado→Caro (forja $280)') vs ledger OPORTUNIDAD +16,7 oro; MSCI (68,0 / BURBUJA / −99,3) vs ledger (76,8 / CARO / −18,8); DUOL 78,2 vs 80,8; ADBE 72,8 vs 73,0. Además incluye PG con 92,0 'Núcleo' y CLX con 72,0, ambas AUSENTES del ledger, ambas anotadas 'rúbrica Quality-Value (maduras)' — una rúbrica alternativa que tramos.md:62 prohíbe explícitamente ('Tiers de referencia heredados de qg-seilern, sin excepción').

**Fuente:** Rankings/2026-07-10/Ranking_Cruzado_QGxMoS_v4_2026-07-10.md (mtime 07-13 19:47; PDF 07-14 11:45) vs Rankings/_ledger.json; Skills/ranking-qg/references/tramos.md:62

**Implicación para el método nuevo:** El tablero 'estable y auditable' no es lo que Felipe usa: cuando quiso decidir, hizo a mano un cruce que discrepa del ledger hasta 8,8 pts en calidad (MSCI, 3,6× el σ del instrumento) y hasta 50 pts de MoS (V), e inventó una rúbrica paralela para las maduras. Esa desviación es el dato de uso real más informativo de toda la auditoría: el output automático no le servía para decidir.

### [HECHO] El desempate lo decide un artefacto de maquetación de PDF, y luego el alfabeto

**Detalle:** Con 12 de 29 gaps del top-30 exactamente en 0,0, la cadena de desempate de tramos.md:50-60 / build_ranking.py:66-78 es load-bearing. Su segundo escalón son R4,R3,R7,R1 con 'ausentes = −1', y solo 15 de las 30 primeras empresas tienen sub_scores en el ledger. Consecuencia comprobada: 4684.T (OBIC) supera a ISRG —ambas 79,2 oro— exclusivamente porque su portada imprimió las 11 notas y la de ISRG no. Y DUOL supera a V —ambas 80,8 oro, ninguna con sub_scores— por orden alfabético. Puestos 2, 3, 5 y 6 del Tramo 1 los decide el layout del PDF de origen y la letra inicial del ticker.

**Fuente:** Cálculo propio sobre Rankings/_ledger.json (15/30 con sub_scores); build_ranking.py:66-78; references/tramos.md:50-60; orden confirmado en Rankings/2026-07-11/snapshot_2026-07-11.json

**Implicación para el método nuevo:** Reconoce el problema real —el orden es indeterminado— y lo resuelve con un procedimiento determinista, que es distinto de resolverlo con información. Determinismo sin señal es reproducir el mismo ruido dos veces. El método nuevo no debe fabricar orden donde no hay diferencia: debe declarar el empate.

### [HECHO] Campos que se escriben, se protegen con reglas propias y nadie lee nunca

**Detalle:** `pwfv`, `dcf_inverso`, `max_52s` y `ccy` aparecen 0 veces en build_ranking.py (ccy solo en un comentario). `max_52s` tiene además una regla anti-corrupción dedicada (ledger.md:46-48: 'un record perdedor jamás pisa metadatos'), aparece en el esquema (ledger.md:28), en la ingesta desde portada (ledger.md:153) y en la discusión de frescura (ledger.md:101) — para un campo que no alimenta ninguna salida. `dcf_inverso` ni siquiera lo toca el sync. También `necesita_tesis` (build_ranking.py:150-151) cuenta solo los 5 `provisional` y reporta 4, cuando 29 empresas son `plata` — y el propio changelog del 07-11 muestra que pasar de screening a plata movió scores hasta −12,0 pts (EFX 67,2→55,2, ENX.PA 71,2→60,8, LMN.TO 68→60). La lista de trabajo pendiente se sub-reporta 7×.

**Fuente:** grep de pwfv/dcf_inverso/max_52s/ccy en Skills/ranking-qg/scripts/build_ranking.py → 0,0,0,1(comentario); build_ranking.py:150-151; Rankings/2026-07-11/changelog_2026-07-11.md

**Implicación para el método nuevo:** Hay más especificación defendiendo datos muertos que produciendo conclusiones. Y el hueco que sí importa —29 empresas cuyo número solo ha sobrevivido a una verificación de lote— no se le presenta a Felipe como trabajo pendiente.

### [INFERENCIA] Supuestos heredados que nunca se sometieron a prueba

**Detalle:** (a) Los tiers de Seilern se declaran intocables (tramos.md:62, 'sin excepción'), pero sobre las 85 empresas del ledger reparten 1 en Núcleo (≥85, solo MSFT), 11 en Alta, 35 en Sólida y 38 en Watchlist: el escalón superior no discrimina nada. (b) La forma '3 tramos de 12' no está justificada en ningún archivo de la skill — 36 casillas de las que la última corrida llenó 26. (c) El corte de calidad ≥65 para el Tramo 3 (tramos.md:12) hereda el umbral de tier sin justificación propia. (d) La escalera oro>plata>provisional está validada solo en su tramo inferior: el 07-11 demuestra provisional<plata (correcciones de hasta −12 pts), pero NO existe ni un dato que demuestre plata<oro. (e) Los umbrales 90 días y 25% no tienen derivación en ningún sitio; ledger.md:96 justifica los 90 días por analogía con el cuadro de mando trimestral, que es coherencia interna, no evidencia.

**Fuente:** Distribución de tiers computada por mí sobre Rankings/_ledger.json; references/tramos.md:12, :62-67; references/ledger.md:50-58, :92-111; ausencia de justificación en los 6 archivos de la skill

**Implicación para el método nuevo:** La regla de autoridad de la refundación (híbrido con precedencia explícita) debería heredar exactamente UNA cosa de aquí: la distinción provisional vs. verificado, que es lo único con evidencia interna a favor. Los tres niveles, los tiers, los tramos y los umbrales van al montón de lo no probado.

### [INFERENCIA] El 20% que se salva: el registro estructurado de procedencia y el filtro de margen real

**Detalle:** Lo que sirve al propósito de entender/valorar/escribir: (1) `Rankings/_score_records/*.json` como FORMATO de captura —cada conclusión se guarda con ticker, eje, procedencia, fecha y fuente con ruta al documento— y el diff tipado que registra toda mutación (ledger_sync.py:186-338). No como ranking: como índice bibliográfico de qué se ha estudiado, cuándo, con qué profundidad y dónde está el documento. Es la única pieza que sobrevive a eliminar el score. (2) `margen_real()` (build_ranking.py:81-88) más la lista 'verificadas sin margen hoy': es la única lógica de toda la skill que produce una decisión con contenido —exige que el MoS supere el exigido o que la zona sea de compra con MoS positivo— y nació de un fracaso concreto y documentado (tramos.md:27: el 08-jul, 11 de 15 supuestas gangas del 20-40% se desinflaron al 1-9% al verificar). (3) La honestidad estructural del Tramo 3 incompleto (build_ranking.py:292-294): decir '2 de 12' en vez de rellenar.

**Fuente:** Skills/ranking-qg/scripts/ledger_sync.py:186-338; build_ranking.py:81-88, :119-136, :292-294; references/tramos.md:25-44; Rankings/_score_records/

**Implicación para el método nuevo:** El método nuevo puede quedarse con un registro de procedencia (qué documento, qué fecha, qué profundidad, qué concluyó) y con el gate de margen real. Del 80% restante se tira sin pérdida: build_ranking.py entero (tramos, desempates, insignias, HTML/PDF), la política de frescura completa, la compuerta anti-sesgo completa, los snapshots y movimientos de tramo, los campos muertos, y la maquinaria de empates intra-corrida (ledger_sync.py:289-321) — 33 líneas para resolver de forma determinista una colisión que ocurrió 0 veces en 191 registros.

## Límites de este hallazgo
No tengo NINGÚN dato de rentabilidad posterior, así que no puedo decir si la escalera oro>plata>provisional predice algo: solo demuestro que provisional y plata discrepan (hasta −12 pts), no cuál de los dos acierta. No leí los 69 PDFs de tesis: verifiqué la presencia/ausencia de carpetas y los valores de 6 diarios de forja, no la calidad del análisis dentro de ellos. El σ=2.45 que uso en el Monte Carlo lo tomo del encargo, no lo recomputé de forma independiente, y la propia auditoría advierte que es un suelo (72,3% de arrastre entre corridas) — con el ruido real, la supervivencia del Tramo 2 sería peor que 6,82/12, nunca mejor. Solo existen dos corridas reales de esta skill (07-10 y 07-11), ambas del mismo fin de semana: no puedo distinguir defectos de diseño de una muestra insuficiente en lo que respecta a la frecuencia con que la maquinaria de frescura o de empates DEBERÍA haber disparado — solo constato que con estos datos no podía. No sé por qué PG, CL y CLX quedaron fuera del ledger (¿decisión deliberada de excluir maduras, o simple omisión?); el ledger no lo registra y esa ambigüedad es en sí misma el hallazgo. Y no tengo evidencia directa de cómo usa Felipe estos outputs para decidir: infiero de las fechas de modificación (el Cruzado hecho a mano es posterior al último build) que el output automático no le bastó, pero es inferencia sobre mtimes, no un hecho sobre su proceso.