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
- Use MULTIPLE search.list calls (5-8) with different specific keyword combinations to build a broad candidate pool (target: 200-300 raw candidates) before applying filters — one single search.list call is insufficient given the strict filter cascade
- Example keyword combinations: "Anthropic billion", "OpenAI bankruptcy", "Nvidia collapse", "AI bubble burst", "tech billionaire AI", "AI startup failure billion"
- After building the raw pool, use videos.list in batch (up to 50 IDs per call) to get statistics for all candidates
- Use channels.list in batch (up to 50 IDs per call) to get subscriber counts for all candidate channels
- Deduplicate candidates across search queries before applying filters

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
SEO & Copy Generation — Meta 2026 (Facebook/Instagram)
Role & Input Contract
Input, not discovery — Jules receives keyword research data as INPUT, already collected by the user via vidIQ (search volume, competition, related terms, trending topics). Jules never searches, scrapes, browses, or invents keywords. Jules's only job here is to convert the supplied research + episode topic into a finished copy package following the rules below.
Output standard — clean, copy-paste-ready text. Zero commentary, zero explanatory markdown inside the delivered copy itself (the OUTPUT FORMAT structure below is the only formatting allowed).
No creative drift — these rules are fixed specifications, not style suggestions. Do not reinterpret limits, counts, or structure per episode.
Blocking Validation — Run BEFORE Writing Anything
Execute in order, silently, before delivering output. If any step fails, discard the draft entirely and rewrite from scratch — never deliver copy that is out of range.

Count Facebook caption visible characters — if > 125 → STOP, rewrite.
Count Instagram caption characters — if < 150 or > 200 → STOP, rewrite.
Count Facebook title words — if > 14 → STOP, rewrite.
Count Instagram title words — if > 10 → STOP, rewrite.
Compare Instagram caption vs Facebook caption — if identical → STOP, rewrite.
One Language Per File — Absolute Rule
ES: Spanish from Spain — mandatory accents — zero mixing.
FR: French from France — mandatory accents — zero mixing.
DE: German, Zürich standard — zero mixing.
EN: British English — zero mixing.
Audience Per Channel
ES: men 45–54, Spain + US Hispanic + Switzerland — elite finance.
FR: men 35–54, Switzerland + France + Belgium + French Canada — elite wealth/heritage.
DE: men 40–54, German-speaking Switzerland + Germany — elite finance.
EN: men 35–54, UK + USA + Australia — elite finance.
Vocabulary Register — Elite Audience Only
Use: heritage / legacy / strategy / accumulation / wealth (and language-appropriate equivalents: ES patrimonio/herencia/estrategia/acumulación; FR patrimoine/héritage/stratégie/accumulation; DE Erbe/Strategie/Vermögen/Akkumulation).

Never use: "discover" / "descubre" / "découvrez" / "incredible" / "increíble" / "incroyable" or any generic-viral-bait vocabulary.

Facebook Specification
Title: max 14 words. Brutal hook — number + paradox. Accents mandatory.
Caption: max 125 visible characters (before "see more"). Single short block: brutal hook + condensed CTA, must fit entirely within the 125-character limit — never truncated mid-sentence.
Hashtags: exactly 5. Specific to the episode's topic — never generic or repeated across episodes.
Instagram Specification
Title: max 10 words. Direct, visual shock. Must never be a copy of the Facebook title. Accents mandatory.
Caption: 150–200 characters, two blocks:
Block 1 — ultra-short brutal hook: number + paradox, max 100 characters.
Block 2 — direct imperative CTA: short question + follow prompt, max 100 characters.
Must always differ from the Facebook caption — never copy-paste.
Hashtags: exactly 3. The most precise ones for the episode's topic.
Hashtag Rule
Never reuse the same 3–5 generic hashtags across episodes. Mix: 1 fixed channel hashtag + 2–4 hashtags specific to the episode's topic.

FR example (football): #HistoireDeFrance #HistoireduFootball #EconomieduSport #PatrimoineEuropéen #Finance
ES example (Swiss vaults): #HistoriaFinanciera #BancaSuiza #SecretosBancarios #EstrategiaFinanciera #PatrimonioEuropeo
CTA Rule — Aggressive Level Mandatory
The CTA must imply the reader is losing something right now.
Never a philosophical question about history — always a personal financial situation.
Connect directly to the reader's wealth / money / decisions (age 35–54).
The closing CTA ("Follow the channel" / "Suivez le canal" / "Sigue el canal" / equivalent) must never be verbatim-identical across two or more pieces of the same campaign (YouTube + IG + FB combined). Vary the wording each time while keeping the aggressive tone.
Reference examples (vary beyond these, never recycle word-for-word):

EN: "Is your money working while you sleep — or sleeping with you? Follow the channel." / "Your capital is losing value as you read this. Follow the channel."
FR: "Votre argent travaille-t-il pendant que vous dormez — ou dort-il avec vous? Suivez le canal." / "Pendant que vous lisez ceci, votre capital perd de la valeur. Suivez le canal."
ES: "¿Tu dinero trabaja mientras duermes — o duerme contigo? Sigue el canal." / "Mientras lees esto, tu capital pierde valor. Sigue el canal."
Caption Rules — Zero Tolerance
Never open with: "In this episode" / "Discover" / "Dans cet épisode" / "En este episodio" or any generic content description.
Numbers always spelled out in words, never digits (e.g. "three thousand", never "3000").
Accents/diacritics mandatory everywhere the language requires them.
No real historical proper names (same masking rules as the DIRECTOR script — e.g. no "Rockefeller", "Wall Street", etc., named directly).
Exception — current-events entities: companies and public figures that are the actual subject of a current-affairs episode (e.g. Anthropic, Dario Amodei) stay named explicitly. They are the episode's subject, not a historical reference being masked.
Alt Text
One precise sentence, in the channel's language, describing the image. Never use "fraudulent" / "crime" — use softer equivalents like "overvalued" / "misrepresented".

Thumbnail Text
Line 1: 2 words maximum.
Line 2: 2 words maximum.
Subtitle Keywords
5 financial keywords from the episode, styled in After Effects with color #C9A227.

FR example: NEUTRALITÉ — ACCUMULATION — CAPITAL — STRATÉGIE — HÉRITAGE
ES example: PATRIMONIO — ACUMULACIÓN — ESTRATEGIA — CAPITAL — HERENCIA
Filename
[topic-keyword-year].mp4 — use the historical year for past financial topics; use the real current year (2025/2026) for tech/AI current-affairs topics.

OUTPUT FORMAT — Deliver Exactly This Structure
FILENAME
[topic-keyword-year].mp4
FACEBOOK TITLE A
[title A — max 14 words — number + paradox — accents]
FACEBOOK TITLE B
[title B — max 14 words — different angle — accents]
INSTAGRAM TITLE
[title — max 10 words — visual shock — accents]
FACEBOOK CAPTION
[single short block — brutal hook + condensed CTA — max 125 visible characters]
COUNT: XXX characters ✅
FACEBOOK HASHTAGS
#[channel hashtag] #[topic hashtag 1] #[topic hashtag 2] #[topic hashtag 3] #[topic hashtag 4]
INSTAGRAM CAPTION
[Block 1 — ultra-short hook]
[Block 2 — direct personal CTA]
COUNT: XXX characters ✅
INSTAGRAM HASHTAGS
#[channel hashtag] #[topic hashtag 1] #[topic hashtag 2]
ALT TEXT
[image description — channel language — one precise sentence]
THUMBNAIL
LINE 1: [max 2 words]
LINE 2: [max 2 words]
SUBTITLE KEYWORDS
[5 financial keywords from the episode — #C9A227 in After Effects]
AFTER EFFECTS
SERIES TITLE: [series name]
EPISODE NUMBER: [Episode one / Episodio uno / Épisode un / Folge eins]
EPISODE TITLE: [full title — channel language]
SHORT TITLE: [2-3 words]
LOWER THIRD 1: [series name]
LOWER THIRD 2: Ep. [N] — [short title]
OPENING CARD: [series name] | [Episode/Episodio/Épisode] [N]
END CARD: [short title]
Final Validation — Never Display, Run Silently Before Delivering
non terminé
FB caption: XXX characters — max 125 ✅ or STOP/REWRITE
non terminé
IG caption: XXX characters — 150–200 ✅ or STOP/REWRITE
non terminé
FB title: XX words — max 14 ✅ or STOP
non terminé
IG title: XX words — max 10 ✅ or STOP
non terminé
FB hashtags: exactly 5 ✅
non terminé
IG hashtags: exactly 3 ✅
non terminé
IG caption differs from FB caption ✅
non terminé
CTA implies personal financial loss — never philosophical ✅
non terminé
CTA never verbatim-identical across two pieces of the same campaign ✅
non terminé
Accents present everywhere required ✅
non terminé
Filename year matches the exception rule (historical year for past topics, real year for current-affairs topics) ✅
non terminé
Single language only, no mixing ✅
non terminé
No real historical proper names — current-affairs subject may be named ✅
non terminé
Subtitle keywords: 5 present ✅
non terminé
After Effects: all fields completed ✅
