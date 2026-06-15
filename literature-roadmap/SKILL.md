---
name: literature-roadmap
description: Build a structured, prioritized literature review reading guide as a premium single-file HTML "research roadmap" — searches arXiv, journals, and books for the most relevant work (default: last decade), verifies every citation, tiers papers by reading priority, color-codes by study type, synthesizes cross-corpus patterns/conflicts/gaps, and includes per-paper note-taking with persistence. Use this whenever the user starts a literature review, asks "what should I read on X", wants a reading list/guide/plan for a research topic, asks to survey a field, prepare for quals/thesis background, or wants papers organized into a roadmap — even if they don't say "roadmap" or "HTML". Also use it for follow-ups on an existing roadmap: checking whether a noticed trend really holds across the literature, resolving conflicting sources, or filling knowledge gaps with new searches. Infer the subject from conversation, project files, or the user's profile when not stated explicitly.
---

# Literature Roadmap

Turn a research subject into a verified, prioritized reading guide rendered as a polished interactive HTML page the user works through over weeks. The deliverable must feel like a premium research tool, not a list dump.

## Why this skill is shaped the way it is

A literature review fails in two ways: fake or wrong citations (instantly destroys trust with a researcher), and no prioritization (30 papers with no entry point is paralysis). Everything below exists to prevent those two failures.

## Workflow

### 1. Pin down the subject and scope

The subject may be explicit ("literature review on antiprotonic helium") or implicit. If implicit, infer from — in priority order — the current conversation, files in the connected folder, and the user's profile/memory. State the inferred subject and let the user correct it.

Then ask (use the question tool if available, otherwise ask in chat) about whatever is still unknown:

- **Focus**: theoretical foundations, experimental methods, state of the art, open problems — or some subset
- **Depth**: ~10 must-reads / ~15–20 curated (good default) / ~30–40 comprehensive
- **Timeframe**: last decade is the default, but foundational older papers are allowed in a "Foundations" tier if they're essential
- **Reader level**: PhD student in the field vs. newcomer — changes whether you include textbook chapters and pedagogical reviews

Don't re-ask anything already answered in the conversation.

### 2. Search broadly, then verify ruthlessly

Search in parallel across source types:

- **arXiv**: query the API via the web fetch tool, e.g. `http://export.arxiv.org/api/query?search_query=all:"antiprotonic helium"&sortBy=submittedDate&max_results=40`. Returns Atom XML with real IDs, titles, authors, dates, abstracts.
- **Journals & reviews**: web-search for review articles (Rev. Mod. Phys., Nature Reviews, Annual Reviews, Physics Reports and field equivalents), landmark results in Nature/Science/PRL-tier venues, and highly cited papers ("review of X", "X progress report", "X 2015..2025").
- **Books & theses**: search for monographs, graduate texts, and well-regarded PhD theses (often the best methods documentation).

**Verification is non-negotiable.** Every entry in the roadmap must have a real arXiv ID, DOI, or ISBN that you saw in a search result or fetched page during this session. For critical citations — everything in Tier 1, plus any paper a synthesis claim rests on — additionally fetch the landing page (DOI resolver or arXiv abs page) and confirm title, authors, and year match what you'll print. If you cannot confirm a paper exists, it does not go in. Never reconstruct citations from memory — model memory produces plausible-looking fake references, and one fake reference makes the whole roadmap untrustworthy. When search tools fail entirely, tell the user instead of filling gaps from memory.

Collect ~2–3× more candidates than the target count, then curate down to the papers that best serve the user's stated focus.

### 3. Curate into a prioritized structure

Assign each paper:

- **Tier** (reading order): `Tier 1 — Start here` (reviews and orientation papers that map the field, 3–5 items), `Tier 2 — Core literature` (the essential results and methods), `Tier 3 — Deep dives & frontier` (specialist papers, latest preprints, open problems). Add `Foundations` before Tier 1 only if pre-decade classics are truly required.
- **Study type** (drives color-coding): `review`, `theory`, `experiment`, `methods` (instrumentation/techniques/analysis), `book` (incl. theses).
- **Why read this**: 2–3 sentences in your own words from the abstract — what it contributes and why it's at this position in the roadmap. Never copy abstracts verbatim.
- **Effort**: rough reading time (e.g. "~2 h", "weekend", "reference — skim").
- **Prerequisites**: titles of roadmap entries to read first, when a real dependency exists.

Order within tiers by reading sequence, not by date or citation count.

### 3b. Synthesize across the corpus — patterns, conflicts, gaps

A roadmap that just lists papers misses the most valuable thing a reviewer can offer: what the literature *collectively* says. Build a `synthesis` section (rendered prominently in the HTML) with three kinds of entries:

- **Patterns** — trends you notice across the papers (e.g. "precision improved ~10× per 5 years", "the field shifted from single-photon to two-photon techniques"). Before stating a pattern, test it against the *full* candidate set, not just the papers that suggested it. Count how many papers support it, actively look for exceptions and contradictions, and report them: a pattern with stated exceptions is credible; a cherry-picked one is misinformation. If a trend doesn't survive the check, either drop it or report it as "apparent but not robust — holds in X of Y papers".
- **Conflicts** — places where sources disagree: discrepant measured values, incompatible theoretical predictions, or contradictory conclusions. Don't smooth these over or silently pick a side. State both positions, link the conflicting papers, and note any later work that resolves the tension. Conflicts are often exactly where the user's own research opportunity lies.
- **Gaps** — questions the corpus doesn't answer: unmeasured regimes, untested predictions, methods nobody has applied. Each gap is a flag for follow-up searching (see "Living with the roadmap" below).

Every synthesis claim must cite the specific roadmap papers (by id) that support or contradict it — the template renders these as links to the cards.

### 4. Build the HTML roadmap

Use the bundled template — don't write the page from scratch:

1. Read `assets/template.html`.
2. Build the data object described in `references/data-format.md` from your curated papers.
3. Replace the `__ROADMAP_DATA__` placeholder with the JSON object, and review the result for correctness (valid JSON, no unescaped `</script>`).

The template already provides the premium design: tiered layout with visual hierarchy, study-type color-coding and filters, progress tracking, per-paper notes that persist in the browser via localStorage, and notes export to Markdown. This page is opened as a local file in the user's own browser, where localStorage works fine.

If the user asks for design changes, edit the generated file directly; consult `references/design-spec.md` for the design system (palette, type scale, spacing) so changes stay coherent.

### 5. Deliver

Save the HTML to the user's folder named like `<subject-slug>-roadmap.html` and present it. In chat, summarize in 2–3 sentences: tier counts, the single paper to start with today, and a note that their notes/progress save automatically in the browser. Do not enumerate every paper in chat — the page does that.

## Living with the roadmap (follow-up requests)

The roadmap is a working document the user returns to mid-review. Handle these follow-ups with the same rigor as the initial build:

- **"Does this pattern actually hold?"** — The user noticed a trend while reading. Re-examine it against every relevant paper already in the roadmap, search for counterexamples outside it, and answer with counts, exceptions, and contradictions — not just confirmation. Distinguish "real trend" from "coincidence of the papers selected so far".
- **"I found a gap / I don't understand X"** — Search for sources that fill it. For each new paper found, verify it (same standard as step 2) and say exactly where it fits: which tier, which existing papers it should follow, and which synthesis entry it affects.
- **"These two papers disagree"** — Trace the conflict: check whether it's a real disagreement or different conditions/conventions, and search for later work that adjudicates it. Add it to the synthesis section.

When updating the HTML, edit the existing file's `ROADMAP_DATA` in place and **keep existing paper `id`s unchanged** — the user's notes and reading progress are keyed on them in localStorage and will be lost otherwise.

## Quality bar

Before delivering, check: every link resolves to the claimed paper (spot-check at least Tier 1), every paper has a non-generic "why read this", tiers tell a coherent story from orientation → core → frontier, and the counts match what the user asked for. A researcher should be able to open the page and know exactly what to read first and why.
