# AlbertFD-skills

A collection of [Claude](https://claude.com) skills, ready to install or share.

Repo: https://github.com/AlbertFD/AlbertFD-skills

## Skills

- **[paper-dashboard](paper-dashboard/)** — Turns a research paper (PDF, arXiv, DOI, or journal URL) into a self-contained interactive HTML dashboard: tabbed sections, MathJax equations explained term-by-term, Chart.js figure reconstructions, a glossary, annotated references, and a ⚠ Source Check transparency table (✅ full text / 📄 cited paper / ⚠ secondary source / 🔍 inferred). Asks for depth (Quick / Standard / Deep) before building.
- **[learning-map](learning-map/)** — Diagnoses what a learner *actually* misunderstands and teaches from there. Maps existing understanding, traces confusion to its root (the specific misconception or missing prerequisite under the symptom), then produces two artifacts: a Markdown **understanding map** of the diagnosis and a self-contained **interactive HTML lesson** built around that exact gap — with a working manipulative, predict-then-check steps, and graded practice whose wrong answers are the learner's own misconception. Subject chosen at runtime; uses surrounding project/chat/file context.
- **[living-sketch](living-sketch/)** — Brings a concept, sketch, diagram, or written explanation to life as a single self-contained **interactive HTML visual** that sharpens how the idea is articulated. Takes a PDF, a photo of a whiteboard, a rough sketch, a paragraph, or just the chat context; calibrates audience knowledge level, purpose/medium, and the one key takeaway first; then **co-builds the visual in checkpointed stages** (structure → core elements → labels → interactivity), pausing at each so you can steer. SVG-first diagrams with hover-reveal, staged build-up, step-through, and figure↔step cue syncing; **offline-first** (equations rendered in HTML/CSS, no CDN to fail), sized to fit its medium, with a source-fidelity check before delivery.

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
