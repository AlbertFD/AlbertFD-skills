---
name: weekly-news-dashboard
description: Build a verified weekly news briefing as a premium single-file interactive HTML dashboard — gathers the most important stories from the last 7 days across Science, Economics, Politics, and the user's local area, summarizes each in plain language, and cites two independent reputable sources per item. Use this whenever the user wants a news roundup, weekly briefing, "what happened this week", "catch me up on the news", a current-events digest, or a dashboard/summary of recent news in science, markets, politics, or their region — even if they don't say "dashboard". Also use it to refresh an existing briefing or to dig deeper on one category. Always verify every story against reputable sources and never invent headlines, quotes, figures, or links.
---

# Weekly News Dashboard

Turn the past week's news into a verified, scannable briefing rendered as a polished interactive HTML page. The deliverable must feel like a trustworthy morning brief, not a link dump or a wall of unsourced claims.

## Why this skill is shaped the way it is

A news briefing fails in two ways, and both destroy trust instantly: **fabrication** (a headline, quote, figure, or link that the model produced from memory and that turns out to be wrong or nonexistent) and **false confidence** (a single unverified source presented as settled fact). The user works in research and cares about provenance — every claim here is treated like a citation. Everything below exists to prevent those two failures while still producing something genuinely useful and pleasant to read.

## Workflow

### 1. Pin down scope

Resolve these before searching. Take answers already given in the conversation; only ask about what's genuinely unknown (use the question tool if available).

- **Location** (for the local-news section): this is a required input with no fixed default. Infer a candidate from the conversation, the connected folder, or the user's profile/memory, state it, and let the user correct it. If nothing suggests a location, ask. Be specific — a city/region (e.g. "Geneva & neighbouring France") gives better local results than a country.
- **Categories**: default to all four — Science, Economics, Politics, Local. Drop or add per the user's request.
- **Timeframe**: default to the last 7 days. Compute the actual window at runtime — run `date +%Y-%m-%d` (or check the env date) and state the window explicitly (e.g. "14–21 June 2026") so the page and your searches share the same boundaries.
- **Stories per category**: default 4–5. The goal is the *most important* stories, not exhaustive coverage.

### 2. Gather candidates from reputable sources only

Read `references/sources.md` before searching — it defines the reputable allowlist, what to reject, and how to pick local outlets for any region. The short version: wire services and newspapers of record (Reuters, AP, AFP, BBC, Bloomberg, FT, The Economist, WSJ, NYT, The Guardian), primary institutional sources (CERN, NASA, ESA, Nature, Science, The Lancet, NEJM, WHO, IMF, OECD, ECB, central banks, official statistics offices), and the recognized newspapers of record for the user's region. Reject tabloids, partisan blogs, content farms, press releases dressed as news, and anything sourced only to social media.

Search per category with date-bounded queries (web search tool, and fetch institutional pages directly where they exist). Collect ~2–3× more candidates than the target count so you can curate down to what actually matters. Prioritize stories by genuine significance — scale of impact, how many people it affects, whether it's a real development versus incremental noise — not by how dramatic the headline is.

### 3. Verify ruthlessly — this is non-negotiable

The user asked for **reputable + verify**: every story must be corroborated by a **second independent reputable source** before it goes in. Independent means a different organization, not the same wire copy republished — Reuters and a paper that reprinted Reuters do not count as two.

- Confirm the headline, the key facts/figures, and the date against both sources during *this* session. Use what you actually saw in search results or fetched pages.
- Every link you print must be one you retrieved this session and that resolves to the story described. Never reconstruct URLs, DOIs, or quotes from memory — model memory produces plausible-looking fake citations, and one fake link makes the whole briefing untrustworthy.
- If a story is important but you can only confirm it with one source, you may still include it **clearly flagged as single-source / developing** rather than dropping it silently — but never present it as fully verified.
- If search tools fail or you can't verify enough stories, tell the user plainly instead of filling gaps from memory.

Flag any assumption worth pressure-testing (e.g. a figure that appears only in a preprint, a claim attributed to an official but not yet on the record).

### 4. Write each story for a smart, busy reader

For every item produce:

- **Headline**: factual, your own wording — not a copied tabloid-style hook.
- **Summary**: 2–4 sentences in your own words. What happened, the key number or outcome, and enough context to understand it cold. Never copy article text verbatim.
- **Why it matters**: one sentence on significance — for Science, why the result is notable; for Economics, the market/policy implication; for Politics, the consequence; for Local, the practical effect on someone living there.
- **Date**: publication date of the development (within the window).
- **Sources**: two (or more) links, each labelled with the outlet name. Mark the primary source. If single-source, say so here.

### 5. Build the HTML dashboard

Use the bundled template — don't write the page from scratch:

1. Read `assets/template.html`.
2. Build the data object described in the comment at the top of that file (window dates, location, and an array of stories each tagged with category, summary, why-it-matters, date, verification status, and sources).
3. Set `top`: an ordered array of the **5 most important story ids overall**, chosen across all categories by genuine significance — this drives the "Top stories" band the page renders above everything else, so it's your editorial front page. Pick the five a well-informed reader most needs to know this week, ranked most-important first. Use real ids from your `stories` array; if you omit `top`, the page falls back to the first five.
4. Replace the `__DASHBOARD_DATA__` placeholder with your JSON object. Validate it: well-formed JSON, no unescaped `</script>`, every source has a real URL, and every id in `top` exists in `stories`.

The template provides the design: a numbered "Top 5 most important" band at the top (each item jumps to its full card), category-color-coded cards, sticky filter/search toolbar, a "verified / single-source" indicator per story, read-state tracking that persists in the browser via localStorage, and a print stylesheet. It's opened as a local file in the user's browser, where localStorage works. If the user wants visual changes, edit the generated file and consult `references/design-spec.md` so changes stay coherent.

### 6. Deliver

Save the HTML to the user's folder as `news-briefing-<YYYY-MM-DD>.html` and present it. In chat, give a 2–3 sentence summary: the window covered, the single most important story, and a note that read-state saves automatically in the browser. Don't re-list every story in chat — the page does that. Close with a "Sources" section only if you stated specific facts in the chat summary itself.

Offer to schedule it: a weekly briefing is the canonical recurring task, so if the user likes the result, offer to run it automatically (e.g. every Monday morning).

## Follow-up requests

- **"Go deeper on Science / Economics / …"** — re-run step 2–4 for that one category with a higher story count and tighter focus; update that section of the existing HTML, keeping other stories' ids unchanged so read-state survives.
- **"Refresh it"** — recompute the date window from today and rebuild.
- **"Is this story right?"** — re-verify against fresh independent sources and report what you find, including any correction or retraction.

## Quality bar

Before delivering, check: every story has two independent reputable sources (or is explicitly flagged single-source), every link was retrieved this session and resolves to the claimed story, no headline/quote/figure came from memory, summaries are in your own words, the date window is stated and consistent, and the stories are genuinely the week's most important — not the most clickable. A reader should trust this enough to act on it.
