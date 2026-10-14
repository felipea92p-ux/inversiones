# INVESTIGACIÓN HISTÓRICA — El precio de la calidad (Nifty Fifty y calidad cara)

## Resumen
No existe un múltiplo-acantilado, pero sí un colapso medible de la tasa base alrededor de P/E 50: en el único experimento natural limpio a 29 años (Nifty Fifty 1972-2001), de las que cotizaban a P/E≥50 solo el 18.8% batió al índice (retorno medio 4.33%/año vs 12.01% del S&P), frente al 70% de las que cotizaban por debajo de 30. Cada +10 puntos de P/E de entrada costaron −1.95 pp de retorno ANUAL sostenido durante 29 años. El mecanismo está verificado aritméticamente en las tres épocas: la calidad protege el BENEFICIO, no el PRECIO — Cisco multiplicó su BPA por 7.08 y su accionista ganó 0.0% durante 25.7 años; Adobe subió el BPA 67% en cuatro años y su accionista perdió 66%. Y el caso alcista de Siegel, mal citado, no dice lo que se le atribuye: en su propio estudio los Nifty Fifty PERDIERON contra el índice (12.5% vs 12.7%).

## Hallazgos
### [HECHO] El colapso de la tasa base está en P/E ~50, y tiene pendiente cuantificada: −1.95 pp anuales por cada 10 puntos de múltiplo

**Detalle:** Transcribí la Tabla 1 de Fesenmaier & Smith (48 de las 50 acciones Morgan Guaranty; P/E dic-1972 y retorno anualizado 12/1972-12/2001, con dividendos reinvertidos, base CRSP) y computé los tramos yo mismo:

  P/E >= 50 (n=16): baten al índice 3/16 = 18.8% | retorno medio 4.33%/año | mediana 6.04% | 5 con retorno NEGATIVO a 29 años | peor Polaroid −14.68%
  P/E 40-50 (n=10): 3/10 = 30.0% | medio 8.45%
  P/E 30-40 (n=12): 3/12 = 25.0% | medio 9.31%
  P/E <  30 (n=10): baten 7/10 = 70.0% | retorno medio 13.12% | mediana 14.12% | CERO negativos | peor +4.91%
  S&P 500: P/E 19.2 en 1972, retorno 12.01%/año.

Regresión sobre las 48: Pearson −0.535, t=−4.29 (gl=46), R²=0.286. Pendiente: cada +10 puntos de P/E en 1972 = −1.95 pp de retorno ANUAL durante 29 años. P/E medio de las que batieron al índice: 37.0. De las que no: 50.2.

Efecto compuesto sobre 1 USD a 29 años: Polaroid (P/E 90.7) → 0.01 USD. Digital Equipment (P/E 60.0) → 1.31 USD. Coca-Cola (P/E 47.6) → 39.85 USD. Philip Morris (P/E 25.9) → 111.75 USD. Índice → 26.82 USD.

No es un acantilado: Coca-Cola a 47.6x, Merck a 45.9x y Eli Lilly a 46.0x batieron al índice. Es un derrumbe de probabilidad, no una frontera.

**Fuente:** Fesenmaier, Jeff & Gary Smith, "The Nifty-Fifty Re-Revisited", Pomona College, Dept. of Economics (publicado en The Journal of Investing, 2002), Tabla 1. PDF descargado y leído 19-jul-2026. Tramos, correlación y pendiente COMPUTADOS POR MÍ sobre esa tabla.

**Implicación para el método nuevo:** Da a Felipe el único número duro que puede pre-comprometerse ANTES de ver la empresa, que es justo lo que exige su regla de precedencia explícita: por encima de ~50x, la tasa base histórica de batir al índice a 29 años es 1 de 5, y el precio de entrada explica el 29% de la varianza del retorno a tres décadas. Operativamente: en la tesis, el múltiplo de entrada deja de ser un dato del apartado de valoración y pasa a ser una PROBABILIDAD PREVIA que hay que declarar antes de escribir una sola línea del caso alcista. Y sustituye la pregunta inútil '¿está cara?' por una respondible: '¿qué tasa base me asigna el múltiplo que estoy pagando?'

### [HECHO] Siegel no dice lo que todo el mundo cita: en su PROPIO estudio los Nifty Fifty perdieron contra el índice, y midió hasta dentro de otra burbuja de calidad

**Detalle:** El estudio de Siegel (ventana dic-1972 a 31-ago-1998) reporta: P/E medio Nifty Fifty 1972 = 41.9x vs S&P 500 = 18.9x; retorno anualizado Nifty Fifty rebalanceado = 12.5% vs S&P 500 = 12.7%; aproximadamente 25 de las 50 batieron al mercado. Es decir: el estudio que se cita como 'la calidad justificó el precio' documenta UNDERPERFORMANCE de 0.2 pp anuales y una tasa de acierto de moneda al aire.

Su conclusión real es más estrecha: en AGREGADO estaban sobrevaloradas solo un 3.2%, porque el 'P/E garantizado' (el que se habría debido pagar con bola de cristal) compensaba entre nombres. Ejemplos que él mismo da: Philip Morris pagado a 24.0x, garantizado 68.5x; Coca-Cola pagado 46.4x, garantizado 82.3x; IBM pagado 35.5x, garantizado 17.1x. Nótese la dirección: las infravaloradas eran las BARATAS del grupo; la cara (IBM) valía la mitad de lo que costó.

Dos problemas de endpoint y de muestra:
(a) Siegel corta en agosto de 1998, con el mercado dentro de la mayor burbuja de acciones de calidad de la historia. Fesenmaier & Smith extienden a dic-2001 y el veredicto se invierte: los 24 nombres que aparecen en AMBAS listas canónicas (Morgan Guaranty y Kidder Peabody) —los 'Terrific 24', lo más incuestionablemente 'Nifty Fifty' que existe— rindieron 9.69% (congelado) y 9.58% (rebalanceado) contra 12.01% del S&P 500. Ratio de riqueza a 29 años: 0.54 congelado, 0.53 rebalanceado. El inversor terminó con la MITAD de la riqueza del indexado.
(b) Nunca existió una lista oficial de los Nifty Fifty. Las dos listas usadas dan respuestas opuestas. Elegir la lista es elegir la conclusión.

**Fuente:** Siegel, Jeremy, "Valuing Growth Stocks: Revisiting the Nifty Fifty" (AAII Journal; versión Journal of Portfolio Management, verano 1995; y Stocks for the Long Run, 2ª ed. 1998, cap. 7), ventana dic-1972 a 31-ago-1998 — cifras verificadas 19-jul-2026. Contraste: Fesenmaier & Smith (2002), Tablas 3 y 4.

**Implicación para el método nuevo:** Mata la coartada intelectual que sostiene pagar múltiplos altos ('los Nifty Fifty al final tuvieron razón'). Felipe debe borrarla de la capa de mentalidad: no es cierta ni siquiera en la fuente que la origina. Segundo, y más importante para el método: le da la regla de higiene de fecha de corte. Toda tasa base histórica que use para valorar debe reportarse con AL MENOS dos fechas finales, una de ellas fuera de un pico de mercado; si la conclusión cambia con el endpoint —como aquí, 12.5% se convierte en 9.69%— la conclusión no es un hecho, es una elección. Esto aplica directo a su criterio de éxito nº2 (tasas base 1990-2020) y a su desconfianza declarada hacia el nº4.

### [HECHO] Todo el resultado 'favorable' de comprar calidad cara depende de UNA acción entre cincuenta

**Detalle:** Fesenmaier & Smith, Tablas 3 y 4, ventana 31-dic-1972 a 31-dic-2001 (29 años), retornos anualizados y ratio de riqueza frente al S&P 500:

  Kidder Peabody 50 (empalmado, congelado): 13.11% anual → ratio de riqueza 1.32 (BATE al índice un 32%)
  Kidder Peabody 50 SIN Wal-Mart:            9.93% anual → ratio de riqueza 0.58
  Morgan Guaranty 50:                       11.64% anual → ratio 0.91
  Terrific 24 (en ambas listas):             9.69% anual → ratio 0.54

Wal-Mart rindió 26.96% anualizado en esos 29 años: el TERCER mejor retorno de toda la base de datos CRSP (solo por detrás de Southwest Airlines 28.94% y Boothe Computer/Robert Half 29.65%). Los propios autores lo describen sin adorno: comprar una acción de P/E alto se parece a comprar un billete de lotería — la esperanza matemática es mala pero existe una posibilidad de premio enorme. El 40% de las Kidder Peabody quedó por debajo del mercado y una sola, con P/E por encima de 50, se llevó el bote.

**Fuente:** Fesenmaier & Smith (2002), Tablas 3 y 4 y sección "Wal-Mart". Leído 19-jul-2026.

**Implicación para el método nuevo:** Es el argumento decisivo contra construir una cartera concentrada de compounders caros, y encaja con lo que Felipe ya rechazó (ranking/sizing): el retorno de esa estrategia no viene de acertar el ranking, viene de tener dentro un outlier de una-entre-mil. Un inversor individual con 10-20 posiciones NO tiene el número de intentos que hace falta para capturarlo. Operativamente, en la tesis obliga a un apartado explícito: 'esta tesis, ¿necesita que la empresa sea un outlier del percentil 99.9 para funcionar al múltiplo que pago?'. Si la respuesta es sí, la tesis no es de calidad, es un billete de lotería con prosa mejor escrita — y hay que decirlo así en el documento.

### [HECHO] El mecanismo, verificado con identidad aritmética exacta: la calidad protege el beneficio, no el precio. Cisco multiplicó su BPA por 7 y su accionista ganó cero durante 25.7 años

**Detalle:** Fuentes primarias: 10-K de Cisco FY2000 (ejercicio cerrado 29-jul-2000, accession 0001095811-00-003692): ventas 18,928 M USD, beneficio neto 2,668 M USD, BPA diluido 0.36 USD. SEC XBRL FY2025 (cerrado 26-jul-2025): BPA diluido 2.55 USD.

  BPA: 0.36 → 2.55 = x7.08 (+608%), CAGR 8.1% durante 25 años. El negocio hizo exactamente lo que un caso alcista de calidad prometería.
  Precio: cierre máximo 80.06 USD el 27-mar-2000; superado por primera vez el 10-dic-2025. 25.7 años. Retorno de precio: 0.0% anual.
  P/E pagado: 222x. P/E al recuperar: 31.4x.
  Identidad: 7.083 (crecimiento de BPA) × 0.1412 (contracción de múltiplo) = 1.000. El 100% de 25 años de compounding se lo comió el múltiplo.

El mismo patrón, mismas fechas, otros nombres: Intel alcanzó su máximo en 2000 y sus accionistas de entonces necesitaron MÁS DE 26 AÑOS para volver a estar en positivo (artículo del 13-jul-2026). En el episodio anterior, 1973-74: Polaroid cayó ~91% desde máximos, Avon ~86%, Xerox ~71%, mientras el S&P 500 caía ~45%; entre 1973 y 1977 los Nifty Fifty rindieron −4.4% anual frente a +2.5% del mercado.

**Fuente:** SEC EDGAR, 10-K Cisco FY2000 (accession 0001095811-00-003692) y SEC XBRL companyconcept API, ambos consultados 19-jul-2026. Precio y fecha de recuperación: Sherwood News, 11-dic-2025, y CNBC 10-dic-2025. Intel: Yahoo Finance/Motley Fool, 13-jul-2026. Descomposición aritmética computada por mí. Caídas 1973-74: fuentes secundarias (ver límites).

**Implicación para el método nuevo:** Es el hallazgo que reescribe la ESTRUCTURA de la tesis. Hoy el método de Felipe (y cualquier tesis QG) sostiene la conclusión sobre la calidad del negocio y trata el precio como un chequeo posterior. La identidad Precio = ΔBPA × ΔMúltiplo demuestra que son dos apuestas independientes y que la segunda puede anular por completo a la primera durante horizontes más largos que la vida inversora útil de una tesis. Cambio concreto: toda tesis debe llevar, obligatoriamente, la descomposición explícita del retorno esperado en (a) crecimiento del BPA que espero y (b) múltiplo terminal que asumo — con el múltiplo terminal declarado como NÚMERO, no como supuesto implícito del DCF. Una tesis que no declara su múltiplo de salida no es falsable, y es precisamente ahí donde se esconde el error de 25 años.

### [HECHO] La cohorte 2021-22, medida hoy: los negocios que CUMPLIERON el guion de calidad fueron los que más dinero perdieron, porque eran los más caros

**Detalle:** Precios: barras mensuales IBKR, consultadas 19-jul-2026. BPA: SEC XBRL 10-K diluido GAAP, FY2021 → último FY. Descomposición mía. Sin dividendos.

  ADBE  pico 699.54 (nov-2021)  jul-2026: 237.25  →  −66.1%. BPA 10.02→16.70 = +66.7%. P/E 69.8x → 14.2x (múltiplo −79.7%). EL BENEFICIO CUMPLIÓ; EL 100% DEL DAÑO ES MÚLTIPLO.
  ZTS   pico 249.27 (dic-2021)  may-2026: 114.97  →  −53.9%. BPA 4.27→6.02 = +41.0%. P/E 58.4x → 19.1x (múltiplo −67%). EL BENEFICIO CUMPLIÓ. (En jun-2026 cayó a ~77 por un deterioro real del negocio — separo las dos causas a propósito.)
  IDXX  pico 706.95 (jul-2021). BPA 8.60→13.08 = +52.1%. Recuperó máximos en nov-2025 (769.98): 52 meses, 4.3 años. Hoy 567.44. Recuperó porque su múltiplo NO revirtió (82.2x → 43.4x, sigue caro).
  TMO   pico 672.34 (dic-2021)  jul-2026: 532.48  →  −20.8%. BPA 19.46→17.74 = −8.8%. P/E 34.5x → 30.0x.
  NKE   pico 179.10 (nov-2021)  jul-2026:  43.76  →  −75.6%. BPA 3.56→2.10 = −41.0%. P/E 50.3x → 20.8x. Fallaron AMBOS.
  EL    pico 374.20 (ene-2022)  jul-2026:  82.13  →  −78.1%. BPA 7.79→ −3.15. El negocio se rompió.

El resultado contraintuitivo: TMO fue el ÚNICO del grupo cuyo BPA CAYÓ y aun así tuvo la menor caída (−20.8%), porque era el más barato al pico (34.5x). ADBE y ZTS hicieron todo bien operativamente y perdieron dos tercios y la mitad. A 56 meses del pico, 5 de los 6 siguen por debajo.

**Fuente:** Precios: Interactive Brokers get_price_history, barras mensuales, consultado 19-jul-2026. BPA: SEC XBRL companyconcept (EarningsPerShareDiluted, formularios 10-K), consultado 19-jul-2026. Descomposición computada por mí. Advertencia de muestra en "limites".

**Implicación para el método nuevo:** Rompe el reflejo central del sistema viejo de Felipe: que entender bien el negocio basta para acertar. ADBE y ZTS son el escenario en el que el analista TIENE RAZÓN sobre el negocio y aun así pierde dinero — y no hay ninguna rúbrica de calidad, con 11 reglas o con 40, que hubiera avisado, porque el defecto no estaba en el negocio. Cambio concreto: la tesis necesita un pre-mortem específico de múltiplo, distinto del pre-mortem de negocio, con esta pregunta literal: 'si acierto en TODO lo operativo y el múltiplo revierte a la media del sector, ¿cuánto pierdo y en cuántos años recupero?'. Si esa cifra es inaceptable, la tesis se rechaza aunque el negocio sea extraordinario — que es exactamente la doctrina Calidad≠Precio que su CLAUDE.md ya declara pero que el método no ejecutaba con números.

### [INFERENCIA] La herramienta operativa: cuántos años de compounding le regalas al múltiplo solo para EMPATAR

**Detalle:** Aritmética elemental pero no explicitada en ninguna de las 6 skills actuales. Años necesarios de crecimiento del BPA para que el precio vuelva al punto de entrada, si el múltiplo revierte al de salida indicado:

  → múltiplo de salida 20x        (crecimiento anual del BPA:)   8%     10%     12%     15%     20%
     P/E entrada 25x  (BPA x1.25)                              2.9a    2.3a    2.0a    1.6a    1.2a
     P/E entrada 30x  (x1.50)                                  5.3a    4.3a    3.6a    2.9a    2.2a
     P/E entrada 35x  (x1.75)                                  7.3a    5.9a    4.9a    4.0a    3.1a
     P/E entrada 40x  (x2.00)                                  9.0a    7.3a    6.1a    5.0a    3.8a
     P/E entrada 50x  (x2.50)                                 11.9a    9.6a    8.1a    6.6a    5.0a
     P/E entrada 60x  (x3.00)                                 14.3a   11.5a    9.7a    7.9a    6.0a
     P/E entrada 70x  (x3.50)                                 16.3a   13.1a   11.1a    9.0a    6.9a
     P/E entrada 80x  (x4.00)                                 18.0a   14.5a   12.2a    9.9a    7.6a

  Con múltiplo de salida más benévolo (25x): entrada 50x → 6.1 años al 12%; entrada 70x → 9.1 años al 12%; entrada 30x → 1.6 años.

Estos son años para llegar a CERO por ciento de rentabilidad, no para ganar. Contraste con la realidad verificada: Cisco necesitó x7.08 de BPA y 25.7 años para empatar desde 222x; Adobe lleva 4.7 años, +66.7% de BPA, y sigue a −66%.

**Fuente:** Computado por mí (identidad Precio = ΔBPA × ΔMúltiplo). Calibrado contra los casos verificados de los hallazgos 4 y 5.

**Implicación para el método nuevo:** Es el entregable directamente instalable, y responde a la regla de autoridad híbrida que Felipe eligió: el dominio 'precio de entrada' queda gobernado por evidencia empírica (esta tabla + la tasa base del hallazgo 1), y el dominio 'múltiplo terminal justificado' queda gobernado por juicio cualitativo — pero el juicio tiene que producir un NÚMERO declarado por anticipado, y el desempate se escribe antes: si el múltiplo pagado exige más de ~7-8 años de compounding solo para empatar, manda la evidencia empírica y la idea se descarta, por muy convincente que sea la narrativa del negocio. Esto sustituye con ventaja al score /100: no puntúa nada, obliga a entender el negocio (hay que estimar crecimiento de BPA y múltiplo terminal, que es entender el negocio) y produce una decisión falsable.

## Límites de este hallazgo
Sé implacable conmigo mismo, así que aquí va lo que NO sostiene mi evidencia.

1) MI TRANSCRIPCIÓN, NO EL PAPER. El PDF de Fesenmaier & Smith se me renderizó como imagen. Transcribí 48 de las 50 filas de la Tabla 1 — dos (una es General Electric) no pude leerlas con fiabilidad y las omití. Por tanto la correlación −0.535, el t=−4.29, la pendiente de −1.95 pp/año y TODOS los porcentajes por tramo son míos sobre una transcripción visual, no cifras publicadas. El propio paper reporta una correlación de −0.41 sobre la lista combinada de 76 nombres. Mismo signo y misma significación, magnitud distinta. Si Felipe va a pre-comprometer una regla con estos números, hay que re-transcribir la tabla del paper original con OCR verificado antes.

2) EL UMBRAL DE 50 NO ES UN UMBRAL. Es donde parten mis cubos, y los elegí YO después de mirar los datos — esto es exactamente el pecado que Felipe quiere evitar (elegir el corte tras ver el resultado). Los tramos 40-50 y 30-40 son casi idénticos entre sí (30.0% vs 25.0% de aciertos), o sea la relación no es monótona; solo los dos extremos están claramente separados. Coca-Cola a 47.6x, Merck a 45.9x y Eli Lilly a 46.0x batieron al índice cómodamente. Con n=16 en el tramo caro, el intervalo de confianza de ese 18.8% es enorme (aproximadamente 4%-46%). Lo honesto es decir "por encima de ~50x la tasa base se derrumba", no "50x es la línea".

3) LA COHORTE 2021-22 NO ES UNA TASA BASE, Y ESTÁ CONTAMINADA POR MÍ. Son 6 nombres que elegí de memoria por ser "compounders de calidad reconocidos". Eso es selección retrospectiva pura: no construí el universo en nov-2021 con un criterio pre-registrado, lo construí en jul-2026 sabiendo cómo acabó. No permite concluir NADA sobre frecuencias — solo ilustra un mecanismo que es aritméticamente cierto para cualquier acción. Además solo han pasado 4.7 años: es perfectamente posible que ADBE recupere y el episodio acabe pareciéndose más a Microsoft (17 años) que a Polaroid. Los porcentajes de ese hallazgo son de PRECIO, sin dividendos, lo que perjudica a NKE y EL en varios puntos acumulados sin cambiar el sentido.

4) MEZCLO DOS COSAS EN P/E GAAP. Usé BPA GAAP de XBRL por trazabilidad, pero para ADBE el consenso trabaja con BPA normalizado (12.48 en 2021 → 20.94 en 2025), lo que sitúa el P/E de pico en ~56x en vez de 69.8x. La conclusión no cambia; la cifra exacta sí. Y el P/E de pico que calculo usa el BPA del ejercicio que se estaba cerrando, no el forward que miraba el mercado — los múltiplos forward eran menores en todos los casos.

5) SESGO DE SUPERVIVENCIA QUE NO PUDE CORREGIR. El más grave está en el episodio de 2000: cito Cisco, Intel, Microsoft y Qualcomm porque SOBREVIVIERON para tener una fecha de recuperación. Las que no volvieron nunca —o quebraron— no aparecen en ningún titular de "tardó X años en recuperar", y por construcción mis tiempos de recuperación están sesgados a la baja. El verdadero número de "cuánto tarda en recuperar la tecnología de calidad de 2000" es peor que cualquiera que yo he dado, y no sé cuánto peor. Fesenmaier & Smith sí corrigen esto en el episodio de 1972 mediante el empalme de fusiones y compras (columnas "spliced" vs "not reinvested"), y ahí la diferencia resulta modesta (Morgan Guaranty 11.64% vs 11.19%) — pero eso es tranquilizador solo para 1972, no para 2000.

6) NO VERIFIQUÉ CON FUENTE PRIMARIA: las caídas de 1973-74 de Polaroid (~91%), Avon (~86%) y Xerox (~71%) y el −4.4% anual de los Nifty Fifty en 1973-77 salen de fuentes secundarias, no de datos de precio que yo haya visto. Trátalas como pista, no como prueba. Tampoco pude verificar el caso Coca-Cola 1998 (pico ~88 USD, ~45-50x, y su fecha real de recuperación): la fuente estaba tras muro de pago y SEC me devolvió 403 en ese documento, así que lo he dejado FUERA de los hallazgos en vez de citarlo a medias. El dato de Intel (">26 años") viene de un artículo del 13-jul-2026 que no da ni el precio de pico ni la fecha exacta de break-even; lo doy con esa imprecisión declarada.

7) LO QUE NADA DE ESTO DEMUESTRA. No demuestra que exista un múltiplo por debajo del cual se esté seguro: Nike a 50.3x y Estée Lauder a 48.0x perdieron 75% y 78%, pero por deterioro del NEGOCIO, no del múltiplo — un múltiplo bajo no habría salvado esas dos tesis. Y no demuestra causalidad: que el P/E alto de 1972 predijera mal el retorno de 1972-2001 es compatible con que el mercado de 1972 simplemente se equivocara sobre qué negocios eran de calidad, que es un problema distinto —y probablemente peor— que el de pagar de más por identificarlos bien.