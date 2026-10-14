# CAMBIOS vs `Skills/metodologia-qg` v1 — auditoría de la fusión

**Para que Felipe pueda auditar la fusión sin releerlo todo.** Original respaldado íntegro en
`Metodo_Nuevo/_taller/backup/metodologia-qg-original-20260719-2202`.

---

## 1. Lo que se CONSERVA de v1 (el suelo, intacto)

| Pieza | Estado |
|---|---|
| **Regla de oro** — nunca un score ni un ranking | intacta, reforzada con las tres frases de control |
| **Candado A** — veto de `abogado-diablo` antes de toda COMPRA | conservado + 3 reparaciones (ver §2) |
| **Candado B** — WACC siempre bottom-up de mercado | **intacto y sin matices**. Es la única frase del corpus que cierra una vía de contaminación por construcción y no por disciplina |
| **Candado C** — piso de resolución | conservado + auditoría de ruido ejecutable |
| Hallazgos empíricos (σ=2,45 · ρ_LOO=0,938 · ×1,889 · 26 de 38 cruzando la frontera) | conservados como fundamento |
| Resultado del piloto del Candado A (2 de 4 veredictos cambiados) | conservado |
| Taxonomía HECHO / INFERENCIA / SUPUESTO y jerarquía de fuentes | conservada |
| DCF inverso como motor de precio · owner earnings = FCF − SBC | conservado |
| Knock-outs binarios decididos sólo con filing primario | conservados como **única** excepción al Candado D |
| `NO DECIDIBLE` como cuarta salida | conservada, ahora con fecha y acción por defecto obligatorias |
| `references/frontera-dato-juicio.md` · `por-que-fallo-el-sistema-viejo.md` | copiados sin cambios |

---

## 2. Lo que se AÑADE (lo que v1 no tenía)

**El ciclo de capital completo.** v1 cubría de "generar idea" hasta "decidir" y estaba **vacío de
"decidir" en adelante**. Todo lo siguiente es nuevo:

- **Capa de cartera y tamaño** — `PESO = min(T_A, T_T)`, los cinco topes discretos, la única función
  continua `w_max = 12% + (MoS−18%)/0,8`, y el **tope desdoblado 25% mercado / 12% a coste**.
- **La caja como dial principal** — Monte Carlo 200k y Kelly de cartera convergiendo: P(caída >50%) =
  35,8% sin caja vs 4,8% a tamaño de entrada con 26% de caja. Suelo 15%, techo 25%.
- **Universo pre-aprobado** — con su lista negativa, `P*`/`E*`/`M*`, tramo 1 automático, tope de fuego
  del 6% en 30 días, caducidad silenciosa a 36 meses y el tripwire anti-ranking.
- **Definición operacional de ULTRA CALIDAD** — seis puertas binarias con orden anti-halo, la
  distinción **ULTRA-R vs ULTRA-C**, la matriz de cuatro etiquetas y cinco contraejemplos verificados.
- **Protocolo de venta** — lista cerrada de 4 knock-outs, las 6 series con exigencia de 2 en rojo
  simultáneas, y la separación estricta recorte-por-sobrevaloración / salida-por-deterioro.
- **Protección de CAYLA** — ≤8 consultas de precio al año, regla de las 12 horas, canario semanal de
  contaminación, ficha de caída en papel. Ninguna de estas piezas existe en ningún método estándar.
- **Banco de preguntas forzantes de 12 maestros** — con la acción cableada a cada respuesta mala.
- **Presupuestos de tiempo en cada decisión** — v1 no tenía ni uno. El proceso viejo costaba 27-48 h
  por empresa (7-12 semanas al ritmo de Felipe) y por eso nunca se ejecutó.

**Candados nuevos:**

- **B′ (calidad congelada antes del precio).** La contradicción madre entraba por el WACC; B cerró esa
  puerta, pero podía volver a entrar **por el MoS**, porque aquí el MoS es función de la calidad. B′
  congela y fecha la clasificación antes del bloque de precio: ningún DCF puede reclasificar hacia
  arriba.
- **D (válvula de tamaño).** La reparación central. Ninguna respuesta mala puede producir un bloqueo de
  veredicto; produce techo de tamaño más bajo, prohibición de núcleo, o muerte sólo desde la lista
  cerrada de knock-outs.

---

## 3. Lo que se CORRIGE de v1

| # | Qué | Por qué |
|---|---|---|
| 1 | **Candado A ahora es bidireccional** | v1 lo exigía sólo para COMPRAR y era opcional para NO COMPRAR — protegía sólo contra la comisión, en alguien cuyo error demostrado es de **omisión**. Ahora, si una empresa pasa las seis puertas y el veredicto propuesto es NO COMPRAR, el agente recibe el encargo invertido de **defender la compra** |
| 2 | **Input del Candado A especificado** | el propio piloto admitió que el extractor de hechos "pudo heredar el entusiasmo original". Ahora sólo recibe campos estructurados; un adjetivo valorativo y el paquete se devuelve |
| 3 | **Gate de verificación de archivo, recuperado** | estaba en el piloto y **se perdió al transcribirlo a la skill**. Es exactamente lo que falló en WKL.AS: el ledger apuntaba al borrador pre-adversarial y existía una versión 12 minutos posterior con veredicto opuesto |
| 4 | **Sanción del Candado A acotada** | una objeción viva re-corre **el bloque afectado, no el expediente entero**. Re-correr desde cero convertía cualquier objeción en un no-comprar por agotamiento |
| 5 | **Candado C.2 estrechado** | prohibía por escrito el comparador que una cartera de plazas finitas exige: con máximo 18, cuando llega la candidata 19 algo tiene que morir. Ahora se prohíbe el ordenamiento **cardinal**; se permiten dos comparaciones **binarias** (índice y peor posición viva) |
| 6 | **Candado C.3 — excepción escrita para el MoS** | aplicado con rigor, C dice que el 18% cabe entero dentro de la barra de error del valor sobre el que se aplica. Se resuelve moviendo el MoS de "medición" a "regla de decisión sobre `M*`". **Ninguno de los dos lados vio esto** |
| 7 | **Cláusula "sin válvula de escape por tamaño" DEROGADA** | la Frontera F-1.0 §3 la prohibía y el Candado D la exige. Los dos documentos se anulaban. Sin válvula no hay método: hay otra máquina de vetos. *Pendiente de ratificación formal — la Frontera está sellada y su candado C5 exige cuarentena de 30 días* |
| 8 | **WACC del 8% "por convención" rechazado** | un 8% universal es literalmente un WACC heredado. Gana el Candado B sin matices |

---

## 4. Lo que MUERE

- **El esqueleto de 12 pasos numerados** → sustituido por seis decisiones. Razón: cinco de las seis
  decisiones reales son post-compra, y un esqueleto por pasos es estructuralmente un pipeline de
  compra. No se pierde contenido: los 12 pasos viven dentro de D1 y D2.
- **La exigencia dura de PERCEPCIÓN VARIANTE como condición de tesis.** v1 decía *"sin variante
  articulable no hay tesis, hay consenso con pasos extra"*. Eso **prohíbe estructuralmente comprar un
  negocio extraordinario a precio justo** — que es la estrategia declarada de Felipe y la frase de
  Buffett con la que justificó el MoS del 18%. Sobrevive como **pregunta que degrada el tamaño**, no
  como condición de existencia de la tesis (Candado D).
- **Los veredictos-por-paso con candados de degradación.** La auditoría demostró que un sistema de
  veredictos por paso con candados que degradan **es el score /100 disfrazado**: un continuo siempre
  permite un "casi", y un "casi" siempre produce ESPERAR.
- **`rabitt-uqg`** — se añade a la lista de retiradas.

---

## 5. Estado de entrega (actualizado 2026-07-20, tras los 6 simulacros)

**Skill APARTE, no reemplaza nada.** `Skills/metodologia-qg/` (v1) sigue activa y sin tocar. Esta es
`Skills/qg-nucleo/`, una skill distinta e instalable por su cuenta, que **no se dispara sola**
con una mención de ticker — sólo bajo invocación explícita ("usa la v2", "el método fusionado").

**El ciclo adversarial sí se completó**, en dos tandas (la primera murió por el límite de gasto
mensual de la cuenta; se retomó y se amplió). Resultado: **8 enmiendas**, cada una nacida de un
simulacro histórico real, cada una con prueba de equilibrio explícita contra los casos anteriores:

| # | Caso | Debía | Veredicto | Enmienda que produjo |
|---|---|---|---|---|
| 1 | Amazon ene-2005 | COMPRAR | 4%, núcleo prohibido | 1-3 (0/6 → 6/6 tras corregir las puertas) |
| 2 | Nokia dic-2007 | RECHAZAR | 0% | confirmó 1-3; produjo la 4 (C4-ter) |
| 3 | Coca-Cola dic-1998 | RECHAZAR | 0% | 3 (repara C5, el único agujero de la 1) |
| 4 | Microsoft feb-2014 | COMPRAR | 8% | 4 (C4-bis producía omisión; sustituida por C4-ter) |
| 5 | Groupon dic-2011 (gemelo adversarial de Amazon) | RECHAZAR | 0%, 1/6 | 5 (contra prospecto real de EDGAR) |
| 6 | GoPro jun-2014 (caso intermedio) | RECHAZAR | 0%, ≤2/6 | 8 (G2 mal especificada con <5 años de historia) |

**Los 6 veredictos son correctos.** Además, **4 de los 5 juegos de cifras que sostenían los simulacros
ya están verificados contra fuente primaria de SEC EDGAR** (10-K de Amazon, 20-F de Nokia, 10-K de
Coca-Cola, 10-K/10-Q de Microsoft; Groupon se corrió directamente contra su 424B4 real) — ninguna
corrección cambió un veredicto; dos lo endurecieron.

**Lo que sigue pendiente, y es gobernanza, no investigación:** las 8 enmiendas se escribieron
motivadas por casos concretos, en la misma sesión, con aplicación retroactiva — lo que la propia
Frontera F-1.0 del método prohíbe hacer sin trámite. Están en **cuarentena hasta el 2026-08-19**
(exige C2 + C3 + revisión adversarial real de `abogado-diablo` defendiendo el texto original). Hasta
entonces, **para una decisión de capital real manda el texto pre-enmienda** — el candidato sólo vale
para simulacros. El re-test contra 9 casos cerrados ya está documentado en la Enmienda 1 §C0 de
`references/ultra-calidad.md`, pero falta la revisión adversarial real, que necesita un candidato vivo
(no se puede simular retroactivamente sobre un caso con desenlace ya conocido).

**Dos cifras siguen sin verificar**, de fuente secundaria: la rotación de Fundsmith (51,8% en H1 2026,
prensa) y las tasas base de Mauboussin (algunos PDF devolvieron 403 o son imágenes). Ninguna sostiene
hoy un knock-out por sí sola.

**Documentación completa del proceso** —el dossier de 12 maestros, los criterios endurecidos, las 3
arquitecturas en competencia, los simulacros íntegros, y el material recuperado de las corridas que
fallaron— vive en `../../Metodo_Nuevo/Documentacion/`. Ver el `README.md` de `Metodo_Nuevo/` como
índice de todo el proceso.
cuando el límite se renueve.
