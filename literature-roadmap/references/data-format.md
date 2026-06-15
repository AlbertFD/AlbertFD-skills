# Roadmap data format

`assets/template.html` contains the line:

```js
const ROADMAP_DATA = __ROADMAP_DATA__;
```

Replace `__ROADMAP_DATA__` with a JSON object of this shape:

```json
{
  "subject": "Antiprotonic Helium Spectroscopy",
  "subtitle": "Precision tests of CPT symmetry with exotic atoms",
  "generated": "2026-06-12",
  "scope": "≈18 papers · 2015–2026 · focus: theory, methods, state of the art, open problems",
  "intro": "2–4 sentences: how to use this roadmap, what story the tiers tell, where to start.",
  "synthesis": [
    {
      "kind": "pattern",
      "title": "Short claim, e.g. 'Precision improved ~10× per five years'",
      "text": "The claim, how many corpus papers support it, and any exceptions or contradictions found when testing it against the full set.",
      "papers": ["hori2016-rmp", "other-id"]
    },
    {
      "kind": "conflict",
      "title": "What disagrees with what",
      "text": "Both positions stated fairly, plus any later work that resolves the tension.",
      "papers": ["id-a", "id-b"]
    },
    {
      "kind": "gap",
      "title": "What the corpus doesn't answer",
      "text": "Why it's a gap and what a search to fill it would look for.",
      "papers": []
    }
  ],
  "tiers": [
    {
      "id": "tier1",
      "name": "Tier 1 — Start here",
      "blurb": "One sentence on what this tier accomplishes for the reader.",
      "papers": [
        {
          "id": "hori2016-rmp",
          "title": "Exact title as published",
          "authors": "M. Hori, J. Walz",
          "year": 2016,
          "venue": "Rev. Mod. Phys. 88, 035001",
          "type": "review",
          "link": "https://doi.org/10.1103/RevModPhys.88.035001",
          "linkLabel": "DOI",
          "why": "2–3 sentences: contribution + why it sits at this point in the reading order.",
          "effort": "~4 h",
          "prereqs": []
        }
      ]
    }
  ]
}
```

Field notes:

- `type` must be one of `review`, `theory`, `experiment`, `methods`, `book` — these map to the color-coding and filters.
- `id` must be unique and stable (slug of first author + year); localStorage notes are keyed on it, so don't change ids if regenerating the page for the same user.
- `link`: prefer DOI; arXiv abs page otherwise; publisher/WorldCat for books. `linkLabel` examples: `DOI`, `arXiv:2403.01234`, `ISBN 978-...`.
- `prereqs`: array of other paper `id`s in the roadmap (rendered as "Read first" chips linking to those cards). Use sparingly — only real dependencies.
- Tier `id`s: `foundations` (optional), `tier1`, `tier2`, `tier3`.
- `synthesis` is optional but strongly encouraged; `kind` must be `pattern`, `conflict`, or `gap`. `papers` ids render as links to the cited cards — a synthesis entry with no cited papers should be rare (gaps only).
- When **updating** an existing roadmap, never change existing paper `id`s — notes and progress are keyed on them.
- Escape any `</script>` or `</` sequences inside strings (use `<\/`) so the inline JSON can't terminate the script tag.
