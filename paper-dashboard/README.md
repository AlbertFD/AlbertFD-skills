# paper-dashboard

A Claude skill that turns a research paper into a polished, self-contained **interactive
HTML dashboard** — tabbed sections, MathJax equations explained term-by-term, Chart.js
reconstructions of the paper's figures, an expandable glossary, and annotated references.

## What it does

Hand it a paper as a **PDF, arXiv link/ID, DOI, or journal URL** and it produces a single
HTML file you can open in any browser. The dashboard typically has six tabs: Overview,
Architecture/Physics & Equations, Experiment/Approach, Results & Data, Glossary, and
References.

## How it works

1. **Confirms & asks depth.** Before building, it checks that you want a dashboard and asks how deep to go:
   - **Quick** — Overview + Results only, a couple of key charts (a 2-minute orientation).
   - **Standard** — the full six-tab build (most papers want this).
   - **Deep** — every equation broken down, extra charts, an extensive glossary, and an annotated "what this enabled since" references section with verified citations.
2. **Fetches the paper.** Uses web tools for remote papers; `scripts/fetch_paper.py` extracts text from a local PDF.
3. **Builds the dashboard** from the example template, generating a fresh color palette via `scripts/palette.py`.
4. **Verifies** the generated JavaScript with `node --check` before delivering, so tabs and charts work.

## Design principles

- **Faithfulness over polish** — every number, symbol, and reference traces to the paper.
- **Labels reconstructions** — charts rebuilt from reported values are marked schematic; values quoted in the text are plotted exactly.
- **No fabricated citations** — any "further reading" entries are real papers, verified.
- **Self-contained** — one HTML file, only MathJax and Chart.js loaded from CDN.

## Files

```
paper-dashboard/
├── SKILL.md                      # the skill instructions Claude follows
├── README.md                     # this file
├── assets/
│   └── example_dashboard.html    # reference template (antiprotonic-helium paper)
├── scripts/
│   ├── fetch_paper.py            # local-PDF text extraction (+ arXiv/DOI fallback)
│   └── palette.py                # randomized color-palette generator
├── evals.json                    # test cases used while developing the skill
├── example_output_attention.html # worked example: "Attention Is All You Need"
└── example_output_ion_paper.html # worked example: Hori et al., PRL 94, 063401 (2005)
```

## Usage

Once the skill is installed in the Claude desktop app, just ask:

> "Build a dashboard from this paper: https://arxiv.org/abs/1706.03762"

or point it at a local PDF or a DOI. Claude will confirm depth and produce the HTML file.

### Generate a palette directly

```bash
python3 scripts/palette.py        # random palette
python3 scripts/palette.py 42     # reproducible palette from a seed
```

### Extract text from a local PDF

```bash
python3 scripts/fetch_paper.py /path/to/paper.pdf
```

## Installing

Package the folder into an installable `.skill` file and open it in the Claude desktop app:

```bash
cd .. && zip -r paper-dashboard.skill paper-dashboard
```
