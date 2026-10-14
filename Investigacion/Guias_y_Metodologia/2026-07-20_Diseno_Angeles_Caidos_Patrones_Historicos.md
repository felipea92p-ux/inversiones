# Diseño: estudio de patrones históricos por comparación (ángeles caídos)

> Rescatado el 20 de julio de 2026, de la idea original con la que Felipe abrió la sesión de esa
> noche: *"estudiar la historia empresarial y todos los casos documentados, leyendo cientos o
> miles de informes, para entender los 12 o 21 patrones de estrategias corporativas o cualidades
> que denotan las empresas ultra fuertes que se multiplican con el tiempo y componen capital y
> siguen innovando."*
>
> **Estado: diseñado, NUNCA ejecutado.** Se propuso al principio de esa sesión y la conversación
> se desvió hacia reparar un sistema de puntuación viejo — ver `Rankings/_diagnostico/` para ese
> historial, que no hace falta leer para entender ni ejecutar este documento.

---

## 1 · La idea en una frase

No basta con leer sobre empresas que triunfaron y sacar patrones de ahí. Hay que comparar cada
patrón contra empresas que en su momento **se parecían** a las triunfadoras y **no lo consiguieron**.
Solo esa comparación dice si el patrón es real o es una historia bonita contada al revés.

## 2 · Por qué hace falta la comparación (explicado sin tecnicismos)

**La metáfora que lo explica mejor — los aviones que no volvieron.**

En la Segunda Guerra Mundial, la marina estudiaba los aviones que volvían de sus misiones,
marcaba dónde tenían los agujeros de bala, y quería blindar esas zonas. Un matemático dijo: no —
blinden las zonas SIN agujeros. Los aviones con agujeros en esas zonas nunca volvieron para que
nadie los contara. Contar solo los que volvieron da la respuesta exactamente al revés.

Leer solo sobre Hermès, Constellation Software o ASML es lo mismo: contar solo los aviones que
volvieron. Los patrones que se sacan así describen igual de bien a empresas que después
fracasaron — simplemente nunca se comprobó eso, porque nadie las miró.

**El caso real que ya se conoce:** el libro *Good to Great* estudió 11 empresas excelentes y sacó
patrones de liderazgo y disciplina. Dos de esas 11 —Circuit City y Fannie Mae— quebraron o
tuvieron que ser rescatadas después. Los patrones no eran falsos: eran igual de aplicables a
empresas que fracasaron, y el libro nunca lo comprobó.

**La prueba que un patrón de verdad tiene que pasar:** si describes por qué Intel era una empresa
excepcional en 2014 —líder indiscutido, alto retorno sobre el capital, ventaja de tres décadas sin
competencia real, viento de cola estructural— esa descripción es exacta. Y Intel perdió la década
siguiente. Un patrón que no distingue esa Intel de una ASML de la misma época no es un patrón: es
prominencia disfrazada de causa.

## 3 · Qué produce este estudio (y qué NO produce)

**Produce:** una biblioteca de patrones, cada uno con su "gemelo fallido" — el caso que se parecía
y no lo consiguió — y con una idea aproximada de qué tan seguido funciona ese patrón.

**NO produce:** ningún número, ninguna nota, ningún orden de empresas de mejor a peor. Esa fue la
lección cara de esta sesión: en el momento en que este estudio empiece a generar un score
comparable entre empresas, ha dejado de ser un estudio de patrones y se ha convertido en el mismo
examen viejo que ya se demostró que no funciona. Si eso empieza a pasar, se para y se corrige.

## 4 · Cómo se construye, paso a paso

### Paso 1 — Elegir los pares
Para cada patrón candidato (ejemplo: "adquirente en serie disciplinado"), buscar:
- **El caso que lo confirma** — una empresa real que exhibía ese patrón y compuso capital durante
  décadas.
- **El gemelo fallido** — una empresa que en su momento se describía casi igual, con el mismo
  patrón visible, y que después se rompió.

Ejemplo ya identificado: Constellation Software (adquirente en serie que funcionó) frente a
Valeant Pharmaceuticals (adquirente en serie con el mismo discurso de "asignadores de capital
superiores", que se desintegró). Vistas ambas desde 2014, con solo la descripción del patrón, eran
indistinguibles. Lo que las separaba no era el patrón — era si el retorno venía de operar mejor lo
comprado o de subir precios apalancando el balance.

### Paso 2 — Disciplina de fecha (lo más importante de todo el diseño)
Toda lectura se hace **solo con lo que se sabía en el momento**, nunca con lo que se sabe hoy.
Si lees el informe de Intel de 2014 sabiendo cómo terminó, tu cerebro ya vio el final de la
película y no puede evitar puntuar mejor de lo justo. Por eso cada caso lleva una fecha de corte
fija, y solo se usan documentos publicados antes de esa fecha.

### Paso 3 — Candidatos ya identificados para empezar
No hace falta inventar la lista desde cero. Candidatos de "gemelo fallido" ya señalados durante
esta sesión, listos para investigar con la disciplina del Paso 2:

| Caso | Año de corte | Qué patrón parecía tener |
|---|---|---|
| Intel | 2014 | Liderazgo indiscutido, escala de fabricación, foso de décadas |
| Cisco | 2000 | Dominio de infraestructura de red, crecimiento imparable |
| Nokia | 2007 | Escala + marca + ecosistema |
| GE | 2000 | Gestión legendaria, diversificación disciplinada |
| IBM | 2011 | Recompras agresivas, "asignación de capital superior" |
| Gilead | 2015 | Alto ROIC, dominio terapéutico |
| Kraft Heinz | 2017 | Disciplina de costes, marca fuerte |
| Estée Lauder | 2021 | Marca de lujo con pricing power |
| BlackBerry | 2009 | Coste de cambio real en el cliente corporativo |
| Zoom | 2021 | Efecto de red aparente |
| Valeant | 2014 | Adquirente en serie disciplinado |

Cada uno se empareja con su contraparte que sí funcionó en la misma época y el mismo sector.

### Paso 4 — Extraer el patrón, no la anécdota
Por cada par, la pregunta no es "¿qué tenían en común?" (eso ya se sabe, es lo que los hacía
parecer iguales). La pregunta es: **¿qué los separaba, que ya era visible en el momento, antes de
saber quién ganaría?** Esa diferencia —y solo esa— es el patrón real.

### Paso 5 — Registrar con tasa base, no como certeza
Cada patrón se anota con una idea aproximada de cuántas veces funciona frente a cuántas veces
falla, según los pares reunidos. Nunca se presenta un patrón como garantía — se presenta como
"esto suele funcionar cuando X está presente y suele fallar cuando falta Y".

## 5 · Cómo se conecta con el método nuevo de Felipe (`metodologia-qg`)

Esto no es un sistema que compite con el método nuevo — es una pieza que al método nuevo **le
falta**, y que su propio documento (`_Refundacion/2026-07-19_Refundacion_Metodologia_v1.md`,
sección de la Frontera de Precedencia) ya declara vacía:

- **Persistencia de métricas excepcionales a 5 y 10 años** — el estudio de patrones da la tasa
  base real: ¿cuántas empresas con ROIC altísimo lo mantienen una década, y cuáles no?
- **Frecuencia de eventos que rompen un negocio, por sector** — los gemelos fallidos son
  exactamente esos eventos, documentados con fecha y mecanismo.
- **Tasa base del propio analista** — hoy está vacía porque nadie ha comparado nunca una
  predicción con el resultado real. Este estudio no la llena directamente, pero sí construye la
  disciplina (comparar predicción contra desenlace real) que hace falta para empezar a llenarla.

En el método nuevo, este trabajo alimentaría el **Paso 3** (mecanismo del moat: "¿qué lo mató en
el pasado y por qué no volvería a pasar?") y el **Paso 8** (pre-mortem: mecanismos concretos de
este arquetipo de negocio, no genéricos) con casos reales en vez de intuición.

## 6 · Cómo se ejecutaría (cuando se retome)

No hace falta decidirlo ahora. Cuando se retome, la forma más eficiente es repartir el trabajo:
varios pares investigados en paralelo, cada uno con su disciplina de fecha de corte, y una síntesis
final que agrupe los patrones que se repiten en más de un par. No es una tarea de una sola sesión
corta — es un proyecto de investigación real, y merece tiempo y atención frescos, no el final de
una noche de veinte horas.
