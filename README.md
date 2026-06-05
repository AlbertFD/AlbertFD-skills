# AlbertFD-skills

A collection of [Claude](https://claude.com) skills, ready to install or share.

Repo: https://github.com/AlbertFD/AlbertFD-skills

## Skills

- **[paper-dashboard](paper-dashboard/)** — Turns a research paper (PDF, arXiv, DOI, or journal URL) into a self-contained interactive HTML dashboard: tabbed sections, MathJax equations explained term-by-term, Chart.js figure reconstructions, a glossary, annotated references, and a ⚠ Source Check transparency table (✅ full text / 📄 cited paper / ⚠ secondary source / 🔍 inferred). Asks for depth (Quick / Standard / Deep) before building.

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
