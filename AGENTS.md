# AGENTS.md — NODESWIS Viral Finder

## Jules Role
Search for viral AI/Tech topics with a financial/power angle for long-format documentary video production.
Jules executes the search autonomously. Do not ask repeated clarifying questions — apply the rules in this file exactly as written.

## Search Language — MANDATORY, ALL IN ENGLISH
- All YouTube Data API queries (search.list) must be built EXCLUSIVELY in English
- Base keywords in English: AI, artificial intelligence, Anthropic, OpenAI, Nvidia, AGI, tech billionaires, AI bubble, AI collapse, AI power
- Do NOT use keywords in Spanish, French, Korean, Russian, Portuguese, or any other language in the searches
- The pool of relevant AI/Tech-financial power content is published mostly in English — searching in other languages dilutes quality and returns irrelevant results
- Candidate titles in the final output must remain in their original language (English) — do not translate
- Reasoning and the output table may be presented in Spanish, but the search itself (search.list) must be 100% in English

## Duration Filter — mandatory, applied first
- Minimum duration: 3 minutes (180 seconds)
- DISCARD ALL Shorts or short clips without exception, regardless of views or breakout ratio
- A video under 3 minutes is never a valid source for documentary content — it is YouTube Shorts algorithmic noise, not a real topic signal
- Check duration BEFORE any other filter

## View Count Filter (OR, not AND)
- Minimum 300,000 views if the video is 90 days old or less, OR
- Minimum 1,000,000 views if the video is 180 days old or less
- Discard any video that does not meet either condition

## Channel Filter — small channels with real breakout
- Calculate ratio: video views / channel subscribers
- Minimum acceptable ratio: 5x
- Discard large/established channels even if they have millions of views
- Goal: detect the anomalous spike of a small channel, not the expected performance of a large channel or the algorithmic farming of shorts/meme channels

## Format Exclusion
Exclude if title or description contains: podcast, interview, fireside chat, full episode, conversation with

## Topic Exclusion
Exclude if title or description contains topics of:
- Politics (elections, government, congress, public policy)
- Theft / scams / fraud (scam, fraud, ponzi, heist, robbery)
- Violence (murder, shooting, attack, assault, war crime)

## Exclusion of Content Unrelated to the Niche
Exclude outright — even if the title contains niche keywords ("AI", "tech", "nvidia", etc.) — if the actual content is:
- Hardware/gaming memes (parts reviews, "GPU caught fire", "my parts arrived", personal benchmarks)
- Video game clips or gameplay (streamers, highlights, matches)
- Corporate/tutorial product content (feature demos, "how to use X product") without a power/money/collapse angle
- Any title where the financial/power angle is not explicit and verifiable

## Exclusion of Fiction/Entertainment Content
Exclude outright: movies, films, series, trailers, dramatizations, or any fictional/scripted content — regardless of topic or title match. Only real news/analysis/documentary-style content about actual events qualifies. Red flags: "Full Movie," "Trailer," "Thriller," "Disaster," "Epic Films," or any title signaling fictional/cinematic content.

## Channel Diversity Rule
Maximum 2 candidates from the same channel per run. If a channel produces more valid candidates than this limit, keep only the top 2 by breakout ratio and discard the rest to preserve topic diversity.

## Winning Pattern — mandatory rejection filter
A candidate is valid if it combines AT LEAST 2 of these 3 signals, and each signal used must be SPECIFIC — not generic or vague:

1. Financial figure — must be a real, stated number (e.g., "$1 billion," "$965B") — NOT vague terms like "huge," "massive," or unstated amounts
2. Proper noun — must be a company or executive with real financial/power stakes (e.g., Nvidia, Anthropic, Musk, Huang, Amodei) — NOT YouTubers, streamers, or public figures unrelated to corporate/financial power
3. Threat or opportunity — must name a specific, concrete consequence (e.g., "biggest failure," "collapse," "$1B bet," "bankruptcy to resurrection") — NOT vague phrases like "experts warned" or "does exactly what you'd expect" with no named stakes

If a candidate meets fewer than 2 SPECIFIC signals, discard it completely — vague or generic matches do not count toward the 2-of-3 requirement.
Prioritize candidates with all 3 signals when available, but do not require all 3 as a hard gate.
Avoid abstract corporate topics without a strong proper noun (e.g., "pricing power," generic "semiconductors") — confirmed as low-performing in retention and views.

## YouTube Data API v3 Usage — quota control
- Use exclusively the YouTube Data API v3 — never estimate or invent data
- HARD LIMIT: maximum 2-3 API calls per full search run
- Efficiency order:
  1. One search.list call with the most specific parameters possible (keywords + date + long duration)
  2. One videos.list call in batch (up to 50 IDs) for statistics
  3. One channels.list call in batch (up to 50 IDs) for subscriber count
- NEVER make individual calls in a loop — always use the batch parameter with comma-separated IDs
- If 2-3 calls do not reach the minimum of 10 valid candidates, deliver what was found and explain why the minimum was not reached — never fill in with candidates that don't meet all filters

## Filter Application Order
1. Duration (discard Shorts, <3 min)
2. Topic exclusion (politics/scam/violence)
3. Format exclusion (podcast/interview)
4. Exclusion of content unrelated to the niche (memes/gaming/corporate tutorial)
5. Exclusion of fiction/entertainment content
6. View count filter (300K/90d OR 1M/180d)
7. Winning pattern (at least 2 of 3 SPECIFIC signals) — mandatory, discards if not met
8. Channel diversity rule (max 2 per channel)
9. Breakout filter (views/subscribers ratio ≥ 5x) — most quota-costly, applied last

## Expected Output
Table with: Title, Channel, Views, Channel Subscribers, Breakout Ratio, Duration, Publish Date, URL
Sorted by breakout ratio, highest to lowest
Minimum 10 candidates per run when possible, without sacrificing filter quality to reach the minimum

## Verification Rule
No self-reported data accepted without verification. All view/subscriber data must come directly from the YouTube Data API v3 — never estimated or invented.
