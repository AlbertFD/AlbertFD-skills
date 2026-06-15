# literature-roadmap

A Claude skill that turns a research subject into a verified, prioritized **reading guide**
rendered as a polished, self-contained **interactive HTML roadmap** — tiered by reading
order, color-coded by study type, with a cross-corpus synthesis section and per-paper
note-taking that persists in the browser.

## What it does

Tell it a topic (or let it infer one from the conversation, your files, or your profile)
and it produces a single HTML file you open in any browser and work through over weeks. It
searches arXiv, journals, and books for the most relevant work, **verifies every citation**,
curates the results into reading-order tiers, and synthesizes what the literature
*collectively* says — patterns, conflicts, and gaps — not just a list of papers.

## How it works

1. **Pins down subject and scope.** Confirms the topic, then asks (only what's still
   unknown) about focus, depth (~10 / ~15–20 / ~30–40 papers), timeframe (default: last
   decade), and reader level.
2. **Searches broadly, verifies ruthlessly.** Queries the arXiv API and web-searches for
   reviews, landmark results, and key books/theses, collecting ~2–3× the target before
   curating down. Every entry must have a real arXiv ID, DOI, or ISBN seen this session;
   Tier 1 and any paper a synthesis claim rests on get their landing page fetched and
   checked. No citation is ever reconstructed from memory.
3. **Curates into a prioritized structure.** Assigns each paper a tier (reading order), a
   study type (color), a "why read this" rationale, an effort estimate, and prerequisites.
4. **Synthesizes across the corpus.** Builds patterns (tested against the full candidate
   set, with exceptions reported), conflicts (both sides stated and linked), and gaps —
   each citing the specific roadmap papers that support it.
5. **Builds the HTML** from the bundled template (no page written from scratch) and
   delivers a single file with progress tracking and notes export.

## Design principles

- **Trust through verification** — one fake reference makes the whole roadmap useless, so
  every citation is confirmed against a real source before it goes in.
- **Prioritization over volume** — 30 papers with no entry point is paralysis; tiers tell a
  coherent story from orientation → core → frontier, and you always know what to read first.
- **Synthesis, not just a list** — the most valuable thing a reviewer offers is what the
  literature collectively says; patterns are pressure-tested for exceptions, not cherry-picked.
- **A working document** — handles follow-ups (does this trend hold? fill this gap? these
  papers disagree) and updates the roadmap in place, preserving paper `id`s so your saved
  notes and progress survive.
- **Self-contained** — one offline HTML file; notes and reading progress persist via
  browser localStorage, exportable to Markdown.

## Files

```
literature-roadmap/
├── SKILL.md                       # the skill instructions Claude follows
├── README.md                      # this file
├── assets/
│   └── template.html              # premium roadmap template (data placeholder)
├── references/
│   ├── data-format.md             # shape of the roadmap data object
│   └── design-spec.md             # design system (palette, type scale, spacing)
└── evals/
    ├── evals.json                 # test cases + expectations used while developing
    └── fixtures/
        └── antihydrogen-roadmap.html  # input fixture for the follow-up eval
```

## Usage

Once the skill is installed in the Claude desktop app, just ask:

> "I'm starting my thesis literature review on antiprotonic helium spectroscopy — find me
> the ~15–20 key papers from the last decade and tell me what to read first."

or more casually:

> "new group does laser cooling of molecules and I know nothing — give me ~10 must-reads
> for the next month."

You can also come back to an existing roadmap: *"Does this precision trend actually hold?"*,
*"Find me 2–3 sources on X and slot them in,"* or *"these two papers disagree — what gives?"*

## Installing

Package the folder into an installable `.skill` file and open it in the Claude desktop app:

```bash
cd .. && ./build.sh literature-roadmap
```
