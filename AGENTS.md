# AGENTS.md — NODESWIS Viral Finder

## Rol de Jules
Buscar temas virales de IA/Tech con ángulo financiero/de poder para producción de video documental largo formato.
Jules ejecuta la búsqueda de forma autónoma. No pedir aclaraciones repetidas — aplicar las reglas de este archivo tal cual.

## Filtro de duración — obligatorio, se aplica primero
- Duración mínima: 3 minutos (180 segundos)
- DESCARTAR TODO Short o clip corto sin excepción, sin importar vistas o ratio de breakout
- Un video de menos de 3 minutos nunca es fuente válida de contenido documental — es ruido algorítmico de YouTube Shorts, no señal de tema real
- Verificar duración ANTES de cualquier otro filtro

## Filtro de vistas (OR, no AND)
- 300,000 vistas mínimo si el video tiene 90 días o menos desde publicación, O
- 1,000,000 vistas mínimo si el video tiene 180 días o menos desde publicación
- Descartar cualquier video que no cumpla ninguna de las dos condiciones

## Filtro de canal — solo canales pequeños con breakout real
- Calcular ratio: vistas del video / subscribers del canal
- Ratio mínimo aceptable: 10x
- Descartar canales grandes/establecidos aunque tengan millones de vistas
- Objetivo: detectar el salto anómalo de un canal chico, no el rendimiento esperado de un canal grande ni el farming algorítmico de canales de shorts/memes

## Exclusión de formato
Excluir si título o descripción contiene: podcast, interview, fireside chat, full episode, conversation with

## Exclusión de temas
Excluir si título o descripción contiene temas de:
- Política (elecciones, gobierno, congreso, políticas públicas)
- Robos / estafas / fraude (scam, fraud, ponzi, heist, robbery)
- Violencia (murder, shooting, attack, assault, war crime)

## Exclusión de contenido no relacionado al nicho
Excluir de raíz aunque el título contenga keywords del nicho ("AI", "tech", "nvidia", etc.) si el contenido real es:
- Memes de hardware/gaming (reviews de piezas, "se incendió la GPU", "llegaron mis piezas", benchmarks personales)
- Clips de videojuegos o gameplay (streamers, highlights, partidas)
- Contenido tutorial/corporativo de producto (demos de features, "cómo usar X producto") sin ángulo de poder/dinero/colapso
- Cualquier título donde el ángulo financiero/de poder no sea explícito y verificable

## Patrón ganador — filtro obligatorio de descarte, no criterio de orden
Un candidato solo es válido si combina las 3 señales de forma clara y verificable en el título:
1. Cifra financiera "bestia" — miles de millones de dólares, no cifras chicas o vagas
2. Nombre propio reconocible — empresa (Anthropic, OpenAI, Nvidia) o persona (Musk, Huang, Amodei)
3. Amenaza u oportunidad sistémica — colapso, riesgo existencial, quiebre de statu quo

Si un candidato no cumple las 3 señales, se descarta completamente — no se incluye en la tabla final para completar el mínimo de 10.
Evitar temas corporativos abstractos sin nombre propio fuerte (ej: "pricing power", "semiconductores" genérico) — confirmado como bajo rendimiento en retención y vistas.

## Uso de YouTube Data API v3 — control de quota
- Usar exclusivamente la YouTube Data API v3 — nunca estimar ni inventar datos
- LÍMITE DURO: máximo 2-3 llamadas a la API por corrida completa
- Orden de eficiencia:
  1. Una llamada de search.list con los parámetros más específicos posibles (keywords + fecha + duración larga)
  2. Una llamada de videos.list en batch (hasta 50 IDs) para estadísticas
  3. Una llamada de channels.list en batch (hasta 50 IDs) para subscriber count
- NUNCA hacer llamadas individuales en loop — siempre batch de IDs separados por coma
- Si con 2-3 llamadas no se alcanza el mínimo de 10 candidatos válidos, entregar los que se hayan encontrado y explicar por qué no se alcanzó el mínimo — nunca rellenar con candidatos que no cumplan todos los filtros

## Orden de aplicación de filtros
1. Duración (descartar Shorts, <3 min)
2. Exclusión de temas (política/estafa/violencia)
3. Exclusión de formato (podcast/entrevista)
4. Exclusión de contenido no relacionado al nicho (memes/gaming/tutorial corporativo)
5. Filtro de vistas (300K/90d OR 1M/180d)
6. Patrón ganador (cifra + nombre propio + amenaza) — obligatorio, descarta si no cumple
7. Filtro de breakout (ratio vistas/subscribers ≥ 10x) — más costoso en quota, va último

## Output esperado
Tabla con: Título, Canal, Vistas, Subscribers del canal, Ratio breakout, Duración, Fecha de publicación, URL
Ordenado por ratio breakout, de mayor a menor
Mínimo 10 candidatos por corrida cuando sea posible, sin sacrificar calidad de filtro para llegar al mínimo

## Regla de verificación
No aceptar autoreporte sin datos verificables. Todo dato de vistas/subscribers debe venir de la YouTube Data API v3 directamente, no estimado ni inventado.
