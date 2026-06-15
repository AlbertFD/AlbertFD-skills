# Design system (for modifying the generated roadmap)

Read this only when the user asks for visual changes; the template already implements all of it.

## Feel
Premium academic tool: warm paper background, serif display type, generous whitespace, restrained color used only for meaning (study type, status, synthesis kind). Avoid decorative gradients, shadows heavier than `0 4px 18px rgba(28,33,48,.07)`, or more than one accent per element.

## Tokens (CSS variables in `:root`)
- Surfaces: `--paper #faf8f3` (page), `--card #ffffff`, `--line #e8e4da` (borders)
- Text: `--ink #1c2130`, `--ink-soft #5b6172`, `--ink-faint #9aa0b0`
- Accent: `--accent #3d5af1` (links, progress, kicker)
- Study-type colors (each has a `-bg` tint for badges): review `#3d5af1`, theory `#8b5cf6`, experiment `#0e9f6e`, methods `#d97706`, book `#db2777`
- Type: `--serif` (Iowan/Palatino/Georgia) for headings and paper titles; `--sans` system stack for body/UI; `--mono` for metadata, counts, badges

## Hierarchy rules
- One `h1` (subject, serif, clamp 30–44px). Tier headers `h2` serif 24px with a 2px ink underline. Paper titles `h3` serif 18.5px.
- Color-coding by study type appears in exactly three places: card left border (4px), badge, legend/filter chips. Don't add it elsewhere.
- Metadata (authors, venue, effort, ids) is always mono or small sans in `--ink-soft`/`--ink-faint` — content reads first, chrome recedes.

## Interactive elements
- Sticky toolbar: progress bar + label, type filter chips, search, export button. Backdrop blur over `--paper`.
- Paper card: status select (To read/Reading/Done — Done dims card to 62% opacity), collapsible notes textarea with 400ms-debounced localStorage autosave and "saved hh:mm:ss" feedback.
- Synthesis cards: kind badge (pattern=accent, conflict=pink, gap=amber), linked paper refs.
- Print stylesheet hides toolbar/buttons; cards avoid page breaks.

## When editing
Change tokens, not scattered hex values. Keep all data in `ROADMAP_DATA` — never hardcode paper content into markup. Preserve localStorage key (`lit-roadmap:<subject-slug>`) and paper `id`s or the user loses notes.
