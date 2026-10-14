# Propuesta de método — Ángulo: Calibración y Ruido

## 1. Principio organizador

**El sistema es un instrumento de medición, y todo instrumento reporta su propio error o no es instrumento: es teatro.** Se descarta cualquier salida que sea un punto sin banda (un score, un PWFV único, un tier), cualquier ranking más fino que la dispersión medida permita, y la pretensión de que "comprensión del negocio" y "número final" sean la misma cosa. Se descarta también la opción de siempre-dar-veredicto: el sistema tiene autorización explícita para responder "no resuelto" y esa respuesta cuenta como éxito, no como fallo.

## 2. Proceso paso a paso

**Paso 0 — Clasificación de la pregunta** (hereda la Frontera F-1.0, Paso 0): frecuencia → §1 evidencia; mecanismo → §2 juicio. Se ejecuta antes de tocar la empresa.

**Paso 1 — Descomposición a preguntas ortogonales, no a reglas correlacionadas.** Dado que un solo factor explica 74.8% de la varianza de las 11 reglas viejas (PC1), el método nuevo usa como máximo 3-4 preguntas genuinamente independientes por eje: (a) mecanismo del moat [J1], (b) persistencia de ROIC incremental [E1/E4], (c) reinversión y runway [g=RR×ROIC], (d) integridad de gestión [J3]. Cada respuesta se registra como **intervalo o distribución**, nunca como punto: "durabilidad del moat: mediana 12 años, IC80% [6,20]", no "8/10".

**Paso 2 — Doble pase ciego, obligatorio y estructural, no accesorio.** Cada pregunta se responde DOS veces: una primera pasada, y una segunda tras un enfriamiento (mínimo 5 días o cambio de framing), ciega a la primera respuesta. La diferencia entre pasadas ES el σ de ESTA empresa, medido en el momento, no heredado de una auditoría de 2026. Si σ de la empresa > σ histórico del proceso (2.45 en la línea base), se marca el caso como "juicio inestable" y se agrega una tercera pasada o se declara no resuelto.

**Paso 3 — Agregación por intervalos, no por suma de puntos.** Las 3-4 distribuciones se combinan por Monte Carlo (no por promedio ponderado): 10.000 draws sobre cada input, propagando incertidumbre en vez de colapsarla. El output es una distribución de valor intrínseco, no un PWFV.

**Paso 4 — Piso de resolución.** Ninguna cifra se reporta con más precisión que 1 unidad de la σ medida en el Paso 2. Si σ=2.45, no existe "86.4 vs 91.2": existe "84-89" y "89-94", que se solapan y por tanto son EL MISMO CUBO.

**Paso 5 — Gate de "no sé".** Si el IC de la decisión (comprar/no comprar) cruza el umbral de decisión, el output obligatorio es "NO RESUELTO" + el dato exacto y verificable que lo resolvería + fecha de revisión. Prohibido forzar veredicto (mecaniza el "test del hoy" de ADN-QG12 y el Paso 4 de la Frontera).

**Paso 6 — Test de dispersión antes de cualquier comparación entre empresas.** Antes de rankear u ordenar N candidatos, se inyecta el σ medido en Monte Carlo sobre el conjunto: si el orden no sobrevive (como ya se demostró: 71.3% de pares indistinguibles), NO se rankea — se reporta el clúster de indistinguibles como conjunto, sin orden interno.

**Paso 7 — Auditoría de proceso, desacoplada del resultado.** Checklist fijo (¿pre-mortem antes que valoración? ¿segunda pasada realmente ciega? ¿se buscó evidencia que refutara?) puntuado y archivado por tesis, revisado trimestralmente SIN mirar el P&L — exactamente lo que el ADN-QG12 exige para el diario de decisiones.

**Paso 8 — Registro de calibración personal.** Toda afirmación probabilística de Felipe ("70% de que el moat aguanta 10 años") se loguea con fecha de resolución futura. Anualmente se construye curva de calibración (Brier score, reliability diagram, estilo GJP/Tetlock) — esto entrena el INSTRUMENTO (el juicio de Felipe), separado de cualquier decisión de capital.

## 3. Artefactos

Central: **Ficha de Incertidumbre** por empresa — no un score, una distribución con (a) intervalo de valor, (b) el driver que más ancha la banda, (c) el dato exacto que la estrecharía, (d) veredicto o "no resuelto" explícito. Secundarios: registro de calibración (para Brier futuro), log de auditoría de proceso (desacoplado de resultado), reporte de dispersión pre-ranking (clusters, no orden).

## 4. Valoración y comprensión del negocio

El valor intrínseco es una distribución de Monte Carlo sobre 2-3 palancas reales (g=reinversión×ROIC incremental con IC, duración del moat con IC, WACC con β citada y fecha — nunca heredado del tier de calidad). El MoS deja de ser "25%": es "el precio cae en el percentil 15 de mi distribución de valor". La anchura del IC **es** la medida de cuánto entiende Felipe el negocio: un IC angosto no es logro estadístico, es la única prueba operativa de comprensión profunda; un IC ancho no se estrecha con más supuestos, se estrecha con más investigación del driver específico que lo ensancha — eso es "entender el negocio" hecho medible.

## 5. Frontera dato/juicio

No se toca. E4 (calibración del propio instrumento) es exactamente mi dominio y ahí el juicio de Felipe tiene voto cero — coherente: mi Paso 2 mide σ empírico, no lo asume. D1 (superinversores) entra solo como generador de hipótesis: nunca estrecha un IC, solo sugiere dónde buscar evidencia primaria (Paso 3 de la Frontera se aplica igual). J9 (no invertir por incomprensión) es el resultado natural de mi Paso 5 cuando el IC es demasiado ancho — mi "no sé" es la instrumentación de J9, no una invención paralela.

## 6. Los 4 criterios

**(1) Backtest 69 tesis**: honestamente, mi diseño no puede "validarse" contra ellas sin outcomes reales (E6 vacío) — solo puede medir si mis IC nuevos coinciden o divergen de los veredictos viejos, lo cual el Caso 3 de la Frontera prohíbe usar como prueba de acierto. Este criterio queda parcialmente irresoluble para CUALQUIER método, y lo digo así.
**(2) Tasas base 1990-2020**: encaje fuerte — las tasas base ENTRAN directamente como prior de la distribución, no como adorno.
**(3) Dispersión > ruido**: es mi criterio nativo; el Paso 6 lo aplica en cada uso.
**(4) Superinversores fuera de muestra**: tratado como D1, nunca cierra nada — coherente pero no aporta ventaja especial aquí.

## 7. Se salva / se tira

Se salva: knock-outs binarios verificables (VIE, SBC>50%, ROIC<WACC estructural — bajo ruido, mecánicos); taxonomía HECHO/INFERENCIA/SUPUESTO mecanizada con campo {doc,página,fecha} obligatorio; pre-mortem-primero de tesis-forja; owner earnings=FCF−SBC; DCF inverso como pregunta falsable (un input del IC, no un punto final); semáforo contable R9 (discreto, bajo ruido).
Se tira: el /100 y los tiers de qg-seilern completos (PC1=74.8%); pesos 15/10; empresas-ancla; consejo-maestros entero (aritmética rota, nunca ejecutado); la escalera de MoS por tier de val-mos (probadamente arbitraria); tramos/desempates de ranking-qg (fabrican orden donde no lo hay); el panel de 9 inversores como votación BUY/HOLD/PASS (nunca diverge — pasa a D1, sin voto).

## 8. Coste

Es caro: doblar cada evaluación (Paso 2) duplica el trabajo por empresa — cubrir 69 tesis así es insostenible sin recortar cobertura o rigor. Y es un instrumento que **dice "no sé" con frecuencia**, lo cual puede sesgar el sistema hacia nunca comprar nada — invirtiendo el defecto viejo (todo score alto) por su espejo (parálisis por incertidumbre irreducible), especialmente en moat/gestión donde el ruido humano nunca baja de cierto piso. Un método que nunca falsamente afirma certeza también nunca ofrece el confort de una conclusión limpia — y eso, para un inversor que quiere "creer" en una tesis, es un costo psicológico real, no solo metodológico.