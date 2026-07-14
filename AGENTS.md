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
DIRECTOR — Production Script Rules (Google Flow Omni Flash)
Source: DIRECTOR_SECRETS_v3 — NODESWIS — L99. Global source of truth: /Users/alejan/REGLAS_GLOBALES_NODESWIS.txt (applies to all skills, no exceptions).
Pipeline: Google Flow Omni Flash — text-to-video, 10s, one prompt per scene. Google AI Ultra — Flow Agent + Flow Tools + SceneBuilder active.

Critical Google Flow rule — zero tolerance
FORBIDDEN in every Omni Flash prompt: the line [IMAGE: still Nano Banana + @Character character ingredient].
This line causes an immediate Google Flow policy rejection. The image is dropped directly into Flow as an ingredient — never declare it as text in the prompt.

Full pipeline — mandatory order
Flow Characters — create @CharacterName once per series.
Agent Instructions — load the full episode briefing before any generation (see template below).
Nano Banana Pro — generate a 9:16 still, drop it directly as an ingredient into Omni Flash.
Omni Flash — a single prompt block — ingredient + text — animate + @Voice — 10s.
SceneBuilder — assemble the 60 clips into the timeline.
Flow Agent — batch-edit if a narration correction is needed.
Flow Tools — apply colorimetry + 115% watermark automatically.
Agent Instructions template — load before every episode
SERIES: [series name]
EPISODE: [number and title]
CHANNEL: [ES / FR / DE / EN]
VOICE: @Voice: [NarradorES / NarradorFR / NarradorDE / NarradorEN]
COLORIMETRY: [channel palette]
CHARACTER: @[CharacterName]
FINANCIAL ANGLE: [episode angle]
NARRATION: EXACTLY 28-30 words FR — 26-28 words ES — 32-35 words EN/DE — count before writing
SCENE 0: brutal scroll-stopper hook — ultra-fast summary of the full series — face fully visible from the first two seconds — lips moving
Fixed structure — absolute standard
STRUCTURE: 60 scenes total — Scene 0 to Scene 59.
DURATION: 600 seconds = exactly 10 minutes — 60 scenes of 10 seconds each, Scene 0 included.
EACH SCENE: exactly 10 seconds.
Brutal hooks — six total, every 100 seconds exactly
Hook	Scenes
Hook 1	0, 1, 2
Hook 2	10, 11, 12
Hook 3	20, 21, 22
Hook 4	30, 31, 32
Hook 5	40, 41, 42
Hook 6	50, 51, 52
Each hook carries a different brutal idea — never repeat the same angle twice. Scene 0 is an integral part of Hook 1 — it is not a separate hook outside the act structure.

Rehooks — three total
Rehook	Scenes
Rehook 1	16, 17, 18
Rehook 2	33, 34, 35
Rehook 3	53, 54, 55
CTAs — three total: Scenes 23 / 43 / 59
⚠️ Discrepancy to confirm with Ha: the source document (DIRECTOR_SECRETS_v3) places the three CTAs at scenes 23 / 43 / 59. A separate conversation referenced scenes 20 / 40 / 59 instead. These are not reconcilable as written — scene 20 is inside Hook 3 and scene 40 is inside Hook 5, so a CTA there would overlap the hook itself. Do not resolve this silently; confirm which set is current before wiring it into AGENTS.md.

Scene 5 — fixed exception
Scene 5 always remains the colorimetry crisis scene (deep red collapse accent, see Colorimetry below) — unchanged regardless of episode content.

Three-act narrative structure
Scene 0 is included in Act 1, integrated into Hook 1 as the scroll-stopper opening.

ACT 1 — Scenes 0-23: Hook 1 (0-1-2) + Hook 2 (10-11-12) + Rehook 1 (16-17-18) + Hook 3 (20-21-22) + CTA (23)
ACT 2 — Scenes 24-43: Hook 4 (30-31-32) + Rehook 2 (33-34-35) + Hook 5 (40-41-42) + CTA (43)
ACT 3 — Scenes 44-59: Hook 6 (50-51-52) + Rehook 3 (53-54-55) + CTA (59)
Note: Hook 3 closes Act 1 and Hook 5 closes Act 2 — each is the last hook of its act and serves as the narrative bridge into the next act, immediately before the CTA.

CTA copy — scenes 23 / 43 / 59 — mandatory
ES: [Pregunta que desestabiliza patrimonio personal — español de España] + "Sigue el canal para la próxima revelación."
FR: [Question déstabilisante patrimoine personnel — français de France formel] + "Suivez le canal pour la prochaine révélation."
DE: [Frage Zürich formal — Vermögen persönlich] + "Folgen Sie dem Kanal für die nächste Enthüllung."
EN: [BBC-formal question — personal wealth] + "Follow the channel for the next revelation."
Narration — absolute rule — exact limits per channel
FR: EXACTLY 28-30 words per scene
ES: EXACTLY 26-28 words per scene
EN: EXACTLY 32-35 words per scene
DE: EXACTLY 32-35 words per scene
Count word by word before writing — display the real count next to the line: "text" (29 ✅). If out of range: STOP — REWRITE — never proceed with a false count. Numbers are ALWAYS written in words — never as digits. Lips synced, elegant natural gesture. @Voice only — zero music — zero sound effects.

Actor motion rule — mandatory
The three actors (lead + two secondary) must be in continuous physical motion for the full ten seconds of every scene. The camera must be in continuous motion for the full ten seconds. Each secondary actor performs one continuous, specific physical action — turning pages, adjusting an object, walking, pouring, manipulating an instrument.

Forbidden to write: stationary, immobile, motionless, never moving, fixed, never crossing frame.

Aesthetic — absolute standard
Reference: Ritz Carlton / Rolex / Patek Philippe / Ferrari / Porsche.
Materials: leather, marble, gold, crystal, lacquered wood — never plastic.
Light: ARRI Alexa LF 8K — never flat light.
Settings: historically specific — never generic. Never write "Victorian office" / "grand salon" without precision — always a real, dated location.
14 camera movements — one distinct per scene 1-13 — never repeat
Crane shot, brutal descent
Steadicam push-in, extreme
Dutch angle, aggressive
Pull back, total reveal
Fast lateral tracking shot
Low angle, power rise
Overhead, plunging
Dolly zoom (Hitchcock)
Orbital arc around the subject
Handheld, intimate close
Oner, continuous tracking
Push-out, final reveal
Extreme macro, financial close-up
Tilt up, monumental final
Colorimetry — exact per channel — mandatory in every block
ES — dramatic gold: Deep, cinematic black shadows. Warm, dramatic gold light. Soft ivory highlights. Deep red collapse accent — scene 5 only.
FR — ARTE golden sepia: Deep, cinematic black shadows. Warm, golden sepia light. Soft ivory highlights. Desaturated ARTE documentary grade. Deep red collapse accent replacing the gold — scene 5 only.
DE — precise cold Zürich: Deep black shadows. Precise, cold gold light. Metallic silver accent. Soft ivory highlights.
EN — BBC high contrast: Deep black shadows. Warm gold light. Cold white, high-definition highlights. BBC high-contrast documentary grade.
Language and voice per channel — absolute rule
ES: Spain Spanish — formal, high-register castellano — @Voice: NarradorES
FR: France French — formal Parisian, ARTE accent — @Voice: NarradorFR
DE: Zürichdeutsch — formal, elite Zürich accent — @Voice: NarradorDE
EN: British English — BBC formal — @Voice: NarradorEN
Scene 0 format — brutal intro hook — scroll stopper
SCENE 0 — SCROLL STOPPER — 10 SECONDS
OMNI FLASH — Text-to-video 10s — 9:16
[LOCATION] [most epic location of the series] — [year in words] — [channel colorimetry]
[SUBJECT] @[CharacterName] facing camera, human face fully visible from the first two seconds, lips moving.
[ACTION] ULTRA-FAST COLLAGE — 5 FLASH CUTS IN 10 SECONDS:
0.0-2.0s: EXTREME STEADICAM PUSH-IN on @[CharacterName]'s face, lips already moving, gaze rising toward the lens.
2.0-4.0s: FLASH CUT — iconic physical detail — hands / object / money — brutal close-up — short orbital arc around the detail
4.0-6.0s: FLASH CUT — most dramatic moment of the series — aggressive dutch angle — maximum contrast
6.0-8.0s: FLASH CUT — @[CharacterName] facing camera in front of the monumental set — human scale vs. monumental scale — low angle power shot
8.0-10.0s: total ORBITAL PULL BACK — reveals the full extent — final frame total black
Hard brutal cut between each flash — zero fade — pure cinema
[CAMERA] steadicam push-in / short orbital arc / dutch angle / low angle / total orbital pull back — five distinct movements, hard cuts between each flash
[AUDIO] @Voice: [NarradorFR/ES/DE/EN]. Zero music.
[CHANNEL COLORIMETRY]
ARRI Alexa LF. 8K. Motion blur on secondary actors.
Narrator: "[BRUTAL FIGURE IN WORDS — first word is the shock word — channel word limit]" ([N] ✅)
Zero text. Zero music. Zero watermarks.
NEGATIVE: no static freeze-frame, no motionless actors, no locked camera, no still image, no photo-like render, no on-screen text, no code, no programming code, no code snippets, no text, no letters, no symbols, no wall carvings, no murals, no wigs, no children, no four actors, no modern elements, no music, no watermarks, no logos
Scenes 1-59 format — single Omni Flash block
SCENE [N] — [PRECISE HISTORICAL LOCATION — YEAR IN WORDS]
OMNI FLASH — Text-to-video 10s — 9:16
[LOCATION] [precise, dated historical location, year in words] — [channel colorimetry]
[SUBJECT] @[CharacterName] [precise period costume — material/color detail]
[ACTION] @[CharacterName] lips moving clearly, gesturing continuously over [precise luxury object — material] the full ten seconds.
Second actor in continuous physical motion — turning pages of an open leather dossier [precise detail] — hands moving throughout the ten seconds.
Third actor in continuous physical motion — handling [iconic object] — adjusting, pouring or manipulating throughout the ten seconds.
All three actors in continuous physical motion the full ten seconds — camera in continuous motion the full ten seconds.
[CAMERA] [Movement N from the list — different from previous scenes]. 10 seconds continuous.
[AUDIO] @Voice: [NarradorFR/ES/DE/EN]. Zero music. Zero effects.
[CHANNEL COLORIMETRY]
ARRI Alexa LF. 8K.
Narrator: "[NARRATION — channel word limit — numbers in words]" ([N] ✅)
Zero text. Zero music. Zero watermarks.
NEGATIVE: no static freeze-frame, no motionless actors, no locked camera, no still image, no photo-like render, no on-screen text, no code, no programming code, no code snippets, no text, no letters, no symbols, no wall carvings, no murals, no wigs, no children, no four actors, no modern elements, no music, no watermarks, no logos
Historical proper-noun replacements — zero tolerance
The source document (DIRECTOR_SECRETS_v3) marks this table ZÉRO TOLÉRANCE with no stated exception — every entry below must always be replaced:

Never write	Always write
Rockefeller	an American industrialist
Wall Street	an American financial hub
Rothschild	a European banking family
JP Morgan	a New York banker
Google / Apple / IBM	a technology empire
FIFA / UEFA	an international sports organization
Nike / Adidas	a global sports brand
⚠️ Discrepancy to confirm with Ha: the SEO/copy section of AGENTS.md carries an exception where current-affairs entities central to an episode's angle (Nvidia, Nokia, etc.) stay named. Applying that same exception here would conflict with this table, since Google / Apple / IBM, FIFA / UEFA, and Nike / Adidas are all current, real, named brands that this table orders replaced with zero tolerance and no carve-out. Two rules cannot both hold as written: either (a) this table is a fixed, closed list of brand references to anonymize in narration regardless of the current-affairs exception, or (b) the current-affairs exception overrides this table when the episode's angle is specifically about one of these brands. Confirm which interpretation applies before this ships.

SEO title rule — absolute
Before writing any title:

Run nodeswis-title-generator — search YouTube + Google Trends.
FB Title A and B: ALWAYS open with a figure written in words — never any other opening.
IG Title: figure + brutal consequence — never "secret / guerre / incroyable" (or their translations).
Mandatory formula: CHIFFRE IMPOSSIBLE + GÉOGRAPHIE PRÉCISE + CONSÉQUENCE BRUTALE.
If a title doesn't comply → fix it automatically → re-validate.
NEVER deliver a title without a figure as the first word.
Output format — clean text only
Zero markdown in the delivered script — no ##, no **, no comments.
Zero visible validation — zero checklist in the output.
Zero [IMAGE: still...] line.
Text ready to paste directly into Google Flow.
Output ends with: ===FIN===
Internal validation checklist — never show in output, run silently before delivering
non terminé
Narration word count verified — exact limit per channel — if out of range, STOP and REWRITE.
non terminé
Camera movement varied across scenes 1-59 — from the 14-movement list — never repeated within the same 3-scene sequence.
non terminé
Correct channel colorimetry present in every block.
non terminé
Correct @Voice for the channel.
non terminé
@CharacterName present in every Omni block.
non terminé
Zero historical proper noun in any narration.
non terminé
CTA only at scenes 23 / 43 / 59 — personal-wealth question — never elsewhere. (pending confirmation — see discrepancy note above)
non terminé
Numbers in words everywhere.
non terminé
Single language — zero mixing.
non terminé
Zero [IMAGE: still...] line.
non terminé
60 scenes produced — Scene 0 to Scene 59 — never fewer, never more.
non terminé
Three actors and camera in continuous physical motion throughout every scene.
