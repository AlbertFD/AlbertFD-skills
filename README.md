# AlbertFD-skills

A collection of [Claude](https://claude.com) skills, ready to install or share.

Repo: https://github.com/AlbertFD/AlbertFD-skills

## Skills

- **[paper-dashboard](paper-dashboard/)** — Turns a research paper (PDF, arXiv, DOI, or URL) into an interactive HTML dashboard: explained equations, rebuilt figures, glossary, and a source-provenance table.
- **[learning-map](learning-map/)** — Finds the root of what a learner misunderstands, then builds an interactive HTML lesson around that exact gap.
- **[living-sketch](living-sketch/)** — Turns a concept, sketch, or diagram into one offline interactive HTML visual, co-built in stages and calibrated to your audience and key takeaway.
- **[literature-roadmap](literature-roadmap/)** — Turns a research subject into a verified, tiered reading guide as an interactive HTML roadmap: prioritized papers, color-coded study types, cross-corpus synthesis, and persistent per-paper notes.
- **[weekly-news-dashboard](weekly-news-dashboard/)** — Turns the past week's news into a verified interactive HTML briefing across Science, Economics, Politics, and your local area: plain-language summaries, two independent reputable sources per story, and persistent read-state.
- **[product-review](product-review/)** — Researches a product across retailer, expert, and community reviews and delivers a verified buy/skip verdict as an interactive HTML report: value/reliability/red-flag assessment, fake-review screening, a source-provenance table, and ranked alternatives.
- **[language-translator](language-translator/)** — Detects the source language and translates text with fidelity over fluency: side-by-side original/translation, technical-mode terminology citations, and a key-vocabulary table for learning as you go.
- **[quiz-maker](quiz-maker/)** — Builds a self-contained interactive HTML quiz on any topic. Asks your difficulty level first (Foundational → PhD/Research), then generates MCQ, numeric, and open questions with rendered equations, step-by-step derivations, plain-language explanations, and a real citation on every answer.
- **[code-converter](code-converter/)** — Ports source code between any two languages while preserving behavior exactly: same inputs, same outputs, same edge cases. Verifies equivalence by running both versions where possible (or a rigorous static audit where not) and delivers an equivalence report with every judgment call flagged.

See each skill's own README for full details.

## Adding a skill

Create a folder named after the skill with a `SKILL.md` inside (YAML frontmatter:
`name`, `description`), plus `scripts/` and `assets/` as needed. Add a one-line summary to
the list above.

## Building installable packages

Run `./build.sh` to package every skill folder into an installable `.skill` file under
`build/`. Pass a name to build just one (e.g. `./build.sh paper-dashboard`). A `.skill`
file is a zip of the skill folder that renders with a one-click "Save skill" install
button. The `build/` folder is a build artifact and is gitignored — regenerate it with
`build.sh` rather than committing it.
