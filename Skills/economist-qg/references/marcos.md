# §VI · Marcos analíticos obligatorios

> El scoring de las 11 reglas (VI.1) lo produce **`qg-seilern`** — NO se reimplementa aquí. Esta
> referencia cubre los marcos que rodean al scoring y alimentan el documento. El §4 de la tesis presenta
> el output de qg-seilern (knock-outs, score/100, radar, tier, verificación adversarial, calibración vs
> anclas, protocolo de earnings en R9, nota de ROIC incremental en R7) + el disclaimer literal.

## VI.2 · Porter dual + tabla cruzada al Seilern + protocolo de contradicción `ESTÁTICA`

- **Diamante de Porter** (ventaja competitiva nacional): **obligatorio** para arquetipos con ventaja de
  origen real (redes de pago, semis); **condicional** para SaaS/plataformas/consumo (si se omite, una
  línea de justificación).
- **Cinco Fuerzas** *(obligatorias siempre)*, puntuadas **numéricamente (1–5 por fuerza, score /25)** con
  narrativa que justifica cada puntuación.
- **Tabla cruzada Porter–Seilern** (obligatoria): ata cada fuerza a la regla Seilern que ilumina.
- **Protocolo de contradicción Porter↔Seilern:** cuando una fuerza puntúa 4–5 (adversa) pero la regla
  Seilern correlacionada puntúa 8–10 (favorable), los marcos contradicen. No se ignora ni se promedia →
  **PAUSA REFLEXIVA obligatoria**: (a) ¿qué mecanismo concreto vuelve a la empresa inmune a esa fuerza
  pese a la presión sectorial? (b) ¿es estructural y duradero o situacional y frágil? (c) si el mecanismo
  desaparece, ¿cuánto cae el score Seilern? Las empresas monstruosas suelen exhibir esta contradicción —
  son inmunes a fuerzas que destrozan a sus competidores. Si no puedes articular el mecanismo, el score
  alto es sospechoso.

## VI.3 · TAM / SAM / SOM con doble método y verificación de consistencia `ESTÁTICA`

- Embudo TAM → SAM → SOM con la participación de competidores marcada.
- **Doble construcción reconciliada en tabla:** bottom-up (unidades × precio × penetración) Y top-down
  (report citado). Fuentes **primarias con URL**; estimaciones propias solo como respaldo, etiquetadas
  `ESTIMADO`.
- **SOM derivado de forma INDEPENDIENTE:** SOM = SAM × trayectoria defendible de cuota. NO se define como
  el revenue del DCF. El "puente SOM↔DCF" es una **verificación de consistencia entre dos estimaciones
  independientes**: si el revenue del DCF base implica un SOM que exige 40% de cuota en 5 años, la brecha
  se hace visible y debe defenderse o corregirse.

## VI.4 · Matriz de posicionamiento competitivo `MIXTA`

Cuadrícula propia: 5–7 competidores × 5–7 dimensiones clave del arquetipo. Para plataformas, además,
**diagrama de flywheel obligatorio.**

## VI.5 · Score de management de 6 dimensiones `MIXTA`

Rating cuantitativo del equipo directivo. **El SBC NO se evalúa aquí** —ya se penaliza en R9 (qg-seilern):

| # | Dimensión | Qué mide | Escala |
|---|---|---|---|
| 1 | ROIC vs WACC histórico | Creación real de valor sobre el coste de capital | 1–5 |
| 2 | Track record de M&A | Disciplina; destrucción vs creación de valor | 1–5 |
| 3 | Insiders + disciplina de recompras | Patrón Form 4 y si las recompras se hacen a valoración barata | 1–5 |
| 4 | Coherencia guidance vs resultados | Últimos 8 trimestres guiado vs entregado | 1–5 |
| 5 | Ownership / skin in the game | Alineación con el minoritario | 1–5 |
| **6** | **Capital allocation lifecycle** | ¿reinversión orgánica intensiva, expansión por M&A, o madurez con buybacks/dividendos? ¿Coherente con el ROIC incremental disponible? Distribuir con ROIC incremental 35% destruye valor; reinvertir con 8% también | 1–5 |

Score /30 + radar de 6 dimensiones. Deméritos de gobernanza sin maquillar. La fase de capital allocation
se proyecta (transición) y alimenta el supuesto #9 del DCF.

## VI.6 · Riesgos: matriz cuantitativa + pre-mortem narrativo `MIXTA`

- **Matriz heatmap probabilidad × impacto** (cada eje 1–5, score 1–25) para los 5–7 riesgos principales.
- **Pre-mortem narrativo:** la historia del fracaso a 5 años contada en pasado —"es 20XX y esta inversión
  salió mal; ¿qué pasó?"

## VI.7 · Early Warning System de erosión del moat `DINÁMICA`

Convierte las capas del moat (§5) en señales cuantificables que se monitorizan **antes** de que el
deterioro aparezca en el P&L. **Vinculado al Cuadro de Mando:** cualquier señal roja obliga a revisar §5 y
actualizar R4 en el Seilern de ese trimestre, aunque no haya earnings que lo justifiquen todavía.

**Señales universales:**
- Gross margin: caída >150bps en dos trimestres consecutivos sin causa de costes externa → roja.
- Pricing test: el management deja de subir precios anualmente o los baja para retener → roja.
- Menciones en earnings calls: competidores/alternativas citados en llamadas de clientes → ámbar.
- Customer concentration: el top-3 sube como % de revenue → dependencia creciente.

**Señales por arquetipo** (definir umbrales al escribir la tesis):

| Arquetipo | KPI primario de alerta | Umbral rojo | Frecuencia |
|---|---|---|---|
| Software / SaaS | NRR por cohorte (últimas 4 vintages) | NRR vintage reciente <100% cuando histórico >115% | Trimestral |
| Software / SaaS | DSO trend | +10 días vs año anterior sin cambio de mix | Trimestral |
| Plataforma | Take rate | Caída >50bps sin causa estructural | Trimestral |
| Plataforma | Frequency (transac/usuario/año) | −5% interanual 2 trimestres seguidos | Trimestral |
| Red de pagos | Cross-border growth vs domestic mix | Cross-border cae como % de payment volume | Trimestral |
| Media / suscripción | Churn por vintage reciente | Churn vintage <12m >15% cuando histórico <8% | Trimestral |
| Media / suscripción | ARPU cohortes nuevas vs antiguas | ARPU nuevas <80% de maduras | Anual |
| Semiconductor | Utilización de capacidad | <75% sostenido >2 trimestres sin recesión macro | Trimestral |
| Datos / índices | Retención neta por segmento | Pérdida de >2 clientes systemically important en 12m | Continuo |

**Pre-mortem del moat:** documentar **la secuencia concreta de eventos que destruirían este moat en 36
meses** como historia causal ("X ocurre primero, luego Y, lo que hace que Z se vuelva viable para los
competidores"), no como lista de riesgos abstractos. Si no puedes escribir esa historia, el moat está
insuficientemente analizado.

**Nota DUOL:** el KPI de alerta primario es el par **churn/engagement por vintage** + **conversión
free→paid**; la historia causal del pre-mortem del moat gira sobre la disrupción por IA generativa (tutor
IA gratuito y personalizado que erosiona la propuesta de valor pagada antes que la gamificación conductual).
