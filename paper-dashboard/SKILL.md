---
name: paper-dashboard
description: Turn a research paper into a polished, self-contained interactive HTML dashboard — tabbed sections, MathJax equations explained term-by-term, Chart.js reconstructions of the paper's figures, an expandable glossary, and annotated references. Use this whenever the user wants to "make a dashboard", "interactive explainer", "study page", or "visual breakdown" of a paper, preprint, or journal article, or hands over a PDF / arXiv link / DOI / journal URL and asks to visualize, explain, or build something interactive from it. Trigger on phrases like "build a dashboard from this paper", "make this paper into an interactive page", "turn this study into a visual explainer", or when the user references a paper alongside words like dashboard, interactive, charts, figures, glossary, or explainer. For a plain text/markdown summary with no interactive HTML, use a simpler summary approach instead — this skill is for the rich HTML deliverable.
---

# Paper Dashboard

Build a single, self-contained HTML file that turns a research paper into an interactive study dashboard: a reader can land on it and, in a few minutes of clicking, understand what the paper did, follow its key equations term-by-term, see its figures rebuilt as live charts, look up any jargon, and trace its references. The bar is "a sharp grad student in the field would trust this and a newcomer could learn from it."

`assets/example_dashboard.html` is a complete, real example (an antiprotonic-helium physics paper). Read it before building — it is the canonical reference for structure, the CSS design system, the tab/glossary/chart JavaScript, and the tone. Copy its scaffold and restyle the content; don't reinvent the layout.

## Workflow

0. **Confirm before building, then ask depth — every time.** Building a full dashboard is a substantial task, so first confirm the user actually wants this skill's interactive HTML dashboard (rather than, say, a quick text summary or just having the paper read). A single combined check-in is ideal: confirm the dashboard is what they want *and* ask how much depth, in one question. Only proceed once they've confirmed. If the user's request was already explicit ("build me a dashboard from this paper at deep depth"), treat that as confirmation + depth and skip straight to building.

   Offer these depth levels and adapt the build to their answer:
   - **Quick** — Overview + Results tabs only. Hero key-facts, headline findings as callouts, 1-2 charts of the most important numbers. A 2-minute orientation; skip deep equation breakdowns and the glossary.
   - **Standard** — the full default structure: Overview, Architecture/Methods & Equations, Experiment/Approach, Results, Glossary, References. The balanced option most papers want.
   - **Deep** — everything in Standard plus: every governing equation broken down term-by-term, more charts (ablations, secondary figures), an extensive glossary, and an annotated "what this enabled since" references section with verified citations. For papers the user wants to teach from or master.

   If the user already stated a depth in their request, honor it and skip the question. Let the depth genuinely change scope — a Quick dashboard should be visibly leaner, a Deep one visibly richer; don't just relabel the same output.

1. **Get the paper's full text** (see Getting the source). You need the real methods, numbers, equations, figures, and reference list — a dashboard built from the abstract alone will be thin and is not acceptable unless the full text is genuinely unreachable.

2. **Mine the paper for dashboard material.** As you read, collect:
   - The headline contribution and 3-5 key results (these become Overview callouts and hero key-facts).
   - The governing equations, and the meaning of *every symbol* (these become the term cards).
   - The methodology / apparatus as a sequence of stages (these become numbered steps).
   - The figures and the quantitative values behind them (these become Chart.js charts).
   - Every piece of jargon a non-specialist would trip on (these become glossary cards).
   - The reference list, verbatim.

3. **Build the HTML** following the structure below, adapting the example's scaffold.

4. **Verify before delivering** (see Verification). This is a research artifact for a researcher — fabricated numbers or mislabeled reconstructions destroy its value.

5. Save the file and present it.

## Getting the source

- **Local PDF** → `python scripts/fetch_paper.py "/path/to/paper.pdf"` (extracts text; falls back to `pdftotext`; for scanned PDFs use the `pdf` skill for OCR).
- **arXiv ID / link** → use your web-fetch tool on `https://arxiv.org/abs/<id>` for metadata, and `https://arxiv.org/html/<id>` for full text when available; otherwise fetch the PDF.
- **DOI / journal URL** → use your web-fetch tool. If the full text is paywalled and only the abstract is reachable, tell the user plainly and build what you honestly can rather than inventing the body.

Prefer your built-in web tools for remote papers — they handle JavaScript and redirects better than a raw script.

## Source provenance: the core discipline

Before writing a single sentence of dashboard content, mentally tag every claim with one of four provenance levels:

- **✅ Paper** — stated in the paper you are summarising (abstract or full text). This is the only tier that can be stated as fact without qualification.
- **📄 Cited paper** — stated in a different verified publication (a follow-up, a review, a cited reference). Accurate but not *this* paper.
- **⚠ Secondary source** — came from a search-engine snippet, abstract database, Wikipedia, or any summary you cannot trace back to primary text. Treat as unverified.
- **🔍 Inferred** — derived by calculation, physical argument, or domain knowledge from confirmed numbers. May be very likely correct but is not stated anywhere.

**This tagging must appear in two places:**

### 1. Inline, at the point of use

Whenever a ⚠ or 🔍 claim appears in the dashboard prose — in any tab, in any callout, in any term card, in any glossary definition, in any chart caption — add a short parenthetical flag immediately after it. Do not let a secondary-source or inferred claim stand bare as if it came from the paper.

Use consistent inline markers:
- `(reported in secondary sources — see ⚠ Source Check)` for ⚠ claims
- `(inferred — see ⚠ Source Check)` for 🔍 claims
- `(from [Author Year], not this paper)` for 📄 claims

The goal is that a researcher skimming any tab can immediately see which claims need verification, without having to cross-reference the Source Check tab. The Source Check tab provides the detail; the inline flag provides the warning.

### 2. Comprehensively, in the ⚠ Source Check tab

Every claim — including ✅ ones — is catalogued in the Source Check table. See the tab description below.

**Common traps to avoid:**
- Inferring the EOM crystal type (e.g. "Pockels cell", "KD*P") from domain knowledge when the paper says only "electro-optic modulator" — that is a 🔍 inference, flag it.
- Inferring the pulse duration from the Fourier limit — 🔍 inference, flag it.
- Citing a wavelength range from a follow-up paper as if it came from this one — 📄, flag it.
- Calling a technique by its common name when the paper uses a more general term — check whether the specific name is in the paper before using it bare.

The discipline is simple: if you did not read it in this paper, it does not get to masquerade as if you did.

## Dashboard structure

Mirror the example. A complete dashboard has:

**`<head>`** — load MathJax (`tex-svg.js`) configured for `\( \)` and `\[ \]`, and Chart.js UMD. Inline all CSS using the example's `:root` custom-property design system (panels, cards, callouts, pills, sticky tabs); keep the structure.

**Pick a fresh, randomized palette for every dashboard** so two dashboards never look identical. Run `python scripts/palette.py` (optionally with a seed) — it prints CSS-ready accent variables, a hero gradient, and the matching Chart.js `COL` object. Paste those into the `:root` block, the `header.hero` gradient, and the JS `COL`. Drive *all* colors (including per-bar `backgroundColor` arrays in charts) from the `--proton`/`--anti`/`--he` variables and `COL`, so swapping the palette restyles the whole page consistently. Re-run the script to reroll if a palette clashes with the paper's subject, but don't hand-pick the same indigo/teal every time — variety is the point.

**Hero header** — gradient banner with: category pills (venue, group/lab, topic), the paper title, the author list, the full citation with DOI, and a 4-cell "key facts" grid of the most striking numbers. Optionally a small thematic SVG. Only put ✅ Paper values in the hero key-facts; flag any 📄/⚠/🔍 values with a small superscript or note.

**Sticky tab nav + tab panes.** Default tabs, adapt to the paper:

- **Overview** — what the paper achieved (a `lead` paragraph), a two-card "what it is / why it matters", and the headline results as colored callout boxes. This is the part everyone reads, so make it genuinely informative. Apply inline provenance flags to any non-paper claim.
- **The Physics / Methods & Equations** — each governing equation in an `.eq` block (MathJax), followed by a row of `.term` cards defining every symbol, plus callouts explaining *why* the equation matters. Use step blocks or a small energy-level/diagram layout where the paper's logic is sequential or structural. Flag any term value or equation parameter that comes from domain knowledge rather than the paper.
- **The Experiment / Approach** — the apparatus or methodology as numbered `.step` stages, with callouts for the central difficulty and the clever trick that beats it. Flag any apparatus detail (crystal type, geometry, dimensions) that is inferred or from secondary sources.
- **Results & Data** — rebuild the paper's figures as Chart.js canvases. Each chart sits in a `.chartbox` with a caption and a `.note`. **Crucial honesty rule:** plot quantitative values quoted in the text *exactly*, and where you can only approximate a published curve, label it "schematic reconstruction" in the caption. Never present an invented curve as the real data. Flag data points from secondary sources in the caption. **Before coding each canvas, open the corresponding figure and match its axes — see "Reconstructing figures faithfully" below. This is mandatory, not optional.**
- **Glossary** — define every term in the `glossary` JS array; cards are injected and expand on click. Write real, substantive definitions (2-4 sentences) at the paper's technical level, not dictionary one-liners. If a definition includes details not in the paper (crystal properties, typical values, physical reasoning), say so within the definition.
- **References** — the paper's own reference list, each with a one-line note on what it contributes. Optionally a curated "what this enabled since" section — but only with citations you have actually verified (see Verification).

- **⚠ Source Check** *(always include, regardless of depth level)* — a transparency table that catalogs every factual claim in the dashboard by provenance. This tab is the backstop: it provides full detail on every claim that was flagged inline, and also documents the ✅ claims so a reader can see the complete picture.

  Use the same four status levels as above, each rendered with a distinct coloured badge:
  - `✅ Paper` — from the paper itself (abstract or full text)
  - `📄 Cited paper` — from a different verified publication
  - `⚠ Secondary source` — from an unverified summary or snippet
  - `🔍 Inferred` — derived by calculation or physical argument

  Build this as an HTML table with columns: **Claim | Status | Detail**. The Detail column must say exactly where the claim came from and what a reader would need to check to confirm it. Populate it with *every* claim: hero key-facts, equation symbol values, experimental parameters, chart data points, glossary details, and any technique name that goes beyond what the paper states.

  Add a callout at the bottom with a direct link to the full text (DOI URL) and, if the paper is paywalled, a note about how the reader might access it.

  Wire this tab into the tab-switching JS (re-run `MathJax.typesetPromise()` on tab open). Give the nav button a warning prefix — e.g. "⚠ Source Check" — so it is visually distinct from content tabs.

**Footer** — one line crediting the source paper and noting that charts reconstruct published figures and equations render with MathJax.

**`<script>`** — tab switching (build charts lazily when the Results tab first opens; re-run `MathJax.typesetPromise()` on tab change), the glossary array + injection loop, and the `buildCharts()` function. The example's JS is a working starting point — adapt the data, keep the mechanics.

## Reconstructing figures faithfully

A reconstructed chart is only useful if it can be laid **side-by-side with the original figure** and read on the same terms. A chart that shows roughly the right trend but on invented axes is misleading — it looks authoritative while quietly disagreeing with the paper. So for **every** chart, before you write any Chart.js code:

1. **Open the actual figure.** Locate the specific figure in the paper that the chart reconstructs — the PDF page, the arXiv HTML `<img>`, or the rendered image. Look at it directly (read the image; on a client-rendered page use the browser tools to view it). Do not reconstruct a figure you have not actually looked at.

2. **Copy the axes verbatim onto the Chart.js `scales`:**
   - **Ranges** — read the min and max of each axis off the figure and set `scales.x.min/max` and `scales.y.min/max` to those exact bounds (use `suggestedMin/Max` only if the paper's bounds are genuinely open-ended). Do not let Chart.js auto-scale to your data — that produces different bounds than the paper and breaks side-by-side comparison.
   - **Units and axis titles** — copy the axis labels and units exactly as printed (e.g. "Target density ρ (×10¹⁷ cm⁻³)", "BLEU", "Top-5 error (%)"). Match the multiplier/exponent convention the paper uses on the axis.
   - **Scale type** — if the figure axis is logarithmic, set `type:'logarithmic'`; if linear, linear. Match it.
   - **Tick labels** — reproduce the paper's tick positions/labels where it matters for reading the plot (e.g. the same x categories, the same gridline values).

3. **Place your data points on those axes.** The exact values quoted in the text are plotted at their true coordinates within the paper's ranges. If you are filling in the shape of a curve between quoted points, that interpolation is the *only* schematic part — say so in the caption, but the axes themselves are never schematic.

4. **Sanity-check the result against the figure.** Glance from your chart to the original: do the points sit at the same place relative to the axes? Does a value the paper calls "an order of magnitude lower" actually render an order of magnitude lower? Does the trend go the same direction? If the reconstruction and the figure disagree, the reconstruction is wrong — fix the data or the scales, don't ship it.

If a figure's underlying numbers genuinely cannot be read (no quoted values, unreadable image), it is better to omit that chart, or render only the axes with a clear "values not recoverable from the source" note, than to fabricate points.

## Principles that make these good

**Faithfulness over polish.** The whole value is that a researcher can rely on it. Every number, symbol definition, and reference must trace to the paper. If you don't know something, say "not stated by the authors" rather than guessing — an honest gap is fine, a confident fabrication is not.

**Flag at the point of use, not just in a separate tab.** The Source Check tab is comprehensive, but a researcher skimming the Physics tab should not have to navigate away to discover that a key parameter is inferred rather than measured. Put the flag where the claim is.

**Label reconstructions.** Charts are almost always rebuilt from reported values, not the original data files. Say so in the caption. Distinguish "values quoted exactly in the text" from "schematic of the trend" so the reader knows what to trust.

**Explain the why.** The term cards and callouts should explain *why* an equation or design choice matters, not just restate it. That is what turns a summary into an explainer.

**Verify added citations.** If you include a "current literature / what this enabled" section, every entry must be a real paper you have confirmed exists (correct title, venue, year, DOI) via web search — do not generate plausible-looking citations. A single hallucinated reference undermines the whole artifact. Note in the footer when/how citations were verified.

**Self-contained.** One HTML file, CDN scripts only (MathJax, Chart.js). It must open and work by double-clicking, offline-friendly except for the two CDN libs.

## Verification

Before delivering, check:
- **Syntax-check the JavaScript** — extract the main `<script>` block and run `node --check` on it. A single stray character breaks the whole script, silently disabling tab switching and charts. The most common culprit is an apostrophe inside a single-quoted string in the `glossary` array (e.g. `'the ion's lifetime'`): use a typographic apostrophe (') or escape with `\'`, and prefer template literals or double quotes for text containing apostrophes. Always verify before delivering.
- Scan every tab for bare ⚠/🔍 claims — any claim not from the paper that lacks an inline flag should be flagged or removed.
- Spot-check that every number in the hero key-facts and charts appears in the source text (or is explicitly flagged if it does not).
- **Check each chart against its figure.** For every canvas, confirm you opened the real figure and that the Chart.js `scales` carry the paper's exact axis ranges, units, scale type (lin/log), and tick labels — so the reconstruction could be laid directly over the original. Verify the plotted points land where the figure puts them and the trend direction matches. A chart on auto-scaled or invented axes is a defect.
- Confirm equations render (valid MathJax/LaTeX) and every symbol in each equation has a term card.
- If you added outside citations, confirm each one resolves to a real paper.

For a high-stakes dashboard, consider a verification subagent that re-checks the numbers and citations against the source.
