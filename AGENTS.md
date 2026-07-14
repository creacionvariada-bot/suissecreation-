# AGENTS.md — NODESWIS Viral Finder

## Rol de Jules
Buscar temas virales de IA/Tech con ángulo financiero/poder para producción de video documental.
Jules ejecuta la búsqueda de forma autónoma. No pedir aclaraciones repetidas — aplicar las reglas de este archivo tal cual.

## Filtro de vistas (OR, no AND)
- 300,000 vistas mínimo si el video tiene 90 días o menos desde publicación, O
- 1,000,000 vistas mínimo si el video tiene 180 días o menos desde publicación
- Descartar cualquier video que no cumpla ninguna de las dos condiciones

## Filtro de canal — SOLO canales pequeños con breakout
- Calcular ratio: vistas del video / subscribers del canal
- Ratio mínimo aceptable: 10x
- Descartar canales grandes/establecidos aunque tengan millones de vistas (señal de audiencia normal, no de tema viral)
- Objetivo: detectar el salto anómalo de un canal chico, no el rendimiento esperado de un canal grande

## Exclusión de formato (descartar de raíz, no marcar para revisión)
Excluir si título o descripción contiene: podcast, interview, fireside chat, full episode, conversation with

## Exclusión de temas (descartar de raíz)
Excluir si título o descripción contiene temas de:
- Política (elecciones, gobierno, congreso, políticas públicas)
- Robos / estafas / fraude (scam, fraud, ponzi, heist, robbery)
- Violencia (murder, shooting, attack, assault, war crime)

## Patrón ganador confirmado (priorizar estos temas, datos reales verificados)
Un tema tiene alta probabilidad de viralidad si combina las 3 señales:
1. Cifra financiera "bestia" — miles de millones de dólares, no cifras chicas o vagas
2. Nombre propio reconocible — empresa (Anthropic, OpenAI, Nvidia) o persona (Musk, Huang, Amodei)
3. Amenaza sistémica — colapso, riesgo existencial, quiebre de statu quo

Evitar temas corporativos abstractos sin nombre propio fuerte (ej: "pricing power", "semiconductores" genérico) — confirmado como bajo rendimiento en retención y vistas.

## Uso de YouTube Data API v3 — control de quota
- Usar exclusivamente la YouTube Data API v3 para obtener vistas, subscribers, y metadata — nunca estimar ni inventar datos
- LÍMITE DURO: máximo 2-3 llamadas a la API por corrida de búsqueda completa
- Priorizar eficiencia de quota en este orden:
  1. Una sola llamada de search.list con los parámetros más específicos posibles (keywords + fecha + duración) para traer el máximo de candidatos relevantes de una vez
  2. Una llamada de videos.list en batch (hasta 50 IDs por llamada) para traer estadísticas de todos los candidatos juntos, no uno por uno
  3. Una llamada de channels.list en batch (hasta 50 IDs por llamada) para traer subscriber count de todos los canales candidatos juntos, no uno por uno
- NUNCA hacer llamadas individuales por video o por canal en loop — siempre usar el parámetro batch de IDs separados por coma
- Si con 2-3 llamadas no se alcanza el mínimo de 10 candidatos, entregar los que se hayan encontrado y reportarlo, no hacer llamadas adicionales sin autorización

## Orden de aplicación de filtros (para eficiencia de quota API)
1. Exclusión de temas (política/estafa/violencia)
2. Exclusión de formato (podcast/entrevista)
3. Filtro de vistas (300K/90d OR 1M/180d)
4. Filtro de breakout (ratio vistas/subscribers ≥ 10x) — este es el más costoso en quota, va último

## Output esperado
Entregar tabla con: Título, Canal, Vistas, Subscribers del canal, Ratio breakout, Duración, Fecha de publicación, URL
Ordenado por ratio breakout, de mayor a menor
Mínimo 10 candidatos por corrida cuando sea posible

## Regla de verificación
No aceptar autoreporte sin datos verificables. Todo dato de vistas/subscribers debe venir de la YouTube Data API v3 directamente, no estimado ni inventado.
