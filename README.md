# AlbertFD-skills

A collection of [Claude](https://claude.com) skills, ready to install or share.

Repo: https://github.com/AlbertFD/AlbertFD-skills

## What's a skill?

A skill is a folder containing a `SKILL.md` file — Markdown instructions with YAML
frontmatter (`name`, `description`) that tell Claude how to perform a specialized task —
plus any supporting scripts, assets, or reference files. Claude loads a skill when a
request matches its description.

## Skills in this repo

### paper-dashboard

Turns a research paper (PDF, arXiv link, DOI, or journal URL) into a polished,
self-contained interactive HTML dashboard: tabbed sections, MathJax equations explained
term-by-term, Chart.js reconstructions of the paper's figures, an expandable glossary, and
annotated references.

Highlights:

- **Asks first.** Confirms you want a dashboard and which depth — Quick, Standard, or Deep — before building.
- **Fresh look every time.** `scripts/palette.py` generates a new harmonious color palette per dashboard.
- **Faithful by design.** Plots values quoted in the paper exactly, labels schematic figure reconstructions as such, and verifies any added citations — no fabricated numbers.
- **Self-checks.** Runs `node --check` on the generated JavaScript before delivering so tabs and charts actually work.

```
paper-dashboard/
├── SKILL.md                      # the skill instructions
├── assets/
│   └── example_dashboard.html    # reference template (antiprotonic-helium paper)
├── scripts/
│   ├── fetch_paper.py            # local-PDF text extraction (+ arXiv/DOI fallback)
│   └── palette.py                # randomized color-palette generator
├── example_output_attention.html # worked example: "Attention Is All You Need" (Standard)
└── example_output_ion_paper.html # worked example: Hori et al. PRL 94, 063401 (Standard)
```

## Repo layout

```
AlbertFD-skills/
├── README.md
├── .gitignore
└── <skill-name>/
    └── SKILL.md   (+ scripts/, assets/, references/ as needed)
```

## Adding a new skill

Create a folder named after the skill and add a `SKILL.md` inside it (with `name` and
`description` frontmatter). Supporting scripts and assets go in `scripts/` and `assets/`
subfolders.

## Installing a skill

Package any skill folder into an installable `.skill` file (a zip archive) and open it in
the Claude desktop app:

```bash
cd <skill-name> && zip -r ../<skill-name>.skill .
```

## Updating the repo

```bash
git add -A
git commit -m "Describe your change"
git push
```
