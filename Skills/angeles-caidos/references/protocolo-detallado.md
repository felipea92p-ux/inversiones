# Protocolo detallado — criterios y errores a evitar

## Criterio de selección de pares

**El gemelo fallido tiene que ser un caso genuinamente confundible en su momento**, no un fracaso
obvio con ventaja retrospectiva. Si en la fecha de corte cualquier analista serio ya veía las
señales de alarma, no es un buen par — no enseña nada, porque el patrón nunca fue realmente
convincente. El par vale cuando, leído a ciegas, el caso fallido y el caso exitoso son
indistinguibles con la información disponible en ese momento.

**Test rápido:** si tu resumen del gemelo fallido en la fecha de corte podría pegarse, palabra por
palabra, en la descripción del ganador — es un buen par. Si ya suena distinto, busca otro.

## Cuántos pares hacen falta para dar un patrón por sostenido

- **1 par:** es una anécdota. Sirve para generar la hipótesis, no para confiar en ella.
- **2-3 pares** con la misma diferencia observable: la hipótesis empieza a ser interesante, se
  puede usar como "primer aviso" pero se declara explícitamente como preliminar.
- **4+ pares** con la misma diferencia, en sectores o épocas distintas: el patrón se puede tratar
  como razonablemente sostenido — sigue sin ser una ley, pero ya no es una anécdota.

Nunca se declara un patrón como "confirmado" sin más — siempre se declara junto al número de pares
que lo sostienen, para que quien lo lea después sepa cuánto peso ponerle.

## Errores ya conocidos que este protocolo existe para evitar

**Muestreo sobre el resultado.** Elegir los gemelos fallidos porque ya se sabe que fallaron, sin
haber comprobado antes que en su momento eran genuinamente convincentes, es la misma trampa
estadística que ya se identificó y se descartó como camino de validación en esta casa (equivalente
a elegir alumnos por lo mucho que cambió su nota entre dos exámenes: siempre parecerá que "mejoran"
la segunda vez, sea cierto o no). La forma de evitarlo: el gemelo fallido se selecciona por **cómo
se veía en la fecha de corte**, no por cómo terminó — el desenlace solo se mira después de haber
fijado por escrito por qué en su momento parecía un ganador.

**Sesgo de retrospectiva (hindsight bias).** Es el error central que el candado de "disciplina de
fecha" del `SKILL.md` existe para cerrar. Un investigador que ya sabe que Intel perdió la década no
puede evitar, sin querer, dar más peso a las señales de alarma que existían en 2014 y menos peso a
las señales de fortaleza — aunque en 2014 las señales de alarma fueran minoritarias y poco
convincentes. La disciplina de fecha no es un formalismo: es la única defensa real contra esto.

**Convertir el patrón en score.** Ya sucedió una vez en esta casa con un sistema de 11 reglas
puntuadas: cada regla individual parecía razonable, y la suma terminó siendo un instrumento que no
se repetía a sí mismo (dos puntuaciones de la misma empresa, en momentos distintos, casi no
coincidían). La forma de evitarlo aquí es estructural: este método no tiene ningún campo numérico
en su salida. Si en algún momento alguien —Felipe, un agente, una versión futura de este documento—
propone "démosle un número a cada patrón para poder compararlos", eso es la señal de alarma exacta
para detenerse.

**El corpus solo con casos famosos.** Los ejemplos de la tabla semilla son casos conocidos porque
son casos conocidos — es fácil investigarlos, pero también es fácil que el corpus entero termine
siendo solo "grandes fracasos célebres" en vez de una muestra representativa. Cuando el corpus
crezca, vale la pena añadir deliberadamente casos menos famosos (empresas medianas, no solo
gigantes caídos) para que el patrón no esté sesgado hacia lo espectacular.

## Cuándo un caso se descarta, no se fuerza

Si al investigar un par no aparece ninguna diferencia clara y observable en la fecha de corte —los
dos casos son honestamente indistinguibles incluso después de investigar a fondo—, eso también es
información real: significa que el patrón que se buscaba no era detectable con la información
disponible en ese momento, y no vale forzar una diferencia artificial para que el caso "funcione".
Se registra como caso sin diferencia observable y se pasa al siguiente par.
