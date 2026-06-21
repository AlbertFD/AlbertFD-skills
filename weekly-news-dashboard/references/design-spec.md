# Design system (for modifying the generated dashboard)

Read this only when the user asks for visual changes; the template already implements all of it. Keep the look consistent with the rest of the AlbertFD skills: premium, restrained, color used only for meaning.

## Feel
A trustworthy morning brief. Warm paper background, serif display headings, generous whitespace, color reserved for category meaning and verification status. No decorative gradients, no shadows heavier than `0 4px 18px rgba(28,33,48,.07)`, one accent per element.

## Tokens (CSS variables in `:root`)
- Surfaces: `--paper #faf8f3` (page), `--card #ffffff`, `--line #e8e4da` (borders)
- Text: `--ink #1c2130`, `--ink-soft #5b6172`, `--ink-faint #9aa0b0`
- Accent: `--accent #3d5af1` (links, progress, kicker)
- Category colors (each has a `-bg` tint for badges/borders): science `#0e9f6e`, economics `#d97706`, politics `#8b5cf6`, local `#3d5af1`
- Status: verified `#0e9f6e`, single-source `#d97706`
- Type: `--serif` (Iowan/Palatino/Georgia) for headings and story titles; `--sans` system stack for body/UI; `--mono` for dates, badges, source labels

## Hierarchy rules
- One `h1` (the briefing title + date window, serif). Category headers `h2` serif with a 2px ink underline. Story titles `h3` serif ~18px.
- Category color appears in exactly three places: card left border (4px), category badge, and the filter chips. Don't add it elsewhere.
- Verification status is its own small badge (verified = green check, single-source = amber). Keep it distinct from category color.
- Metadata (date, outlet names, source labels) is mono or small sans in `--ink-soft`/`--ink-faint`; the summary reads first.

## Interactive elements
- Sticky toolbar: read-progress label, category filter chips, search box. Backdrop blur over `--paper`.
- Story card: "Mark read" toggle (read dims the card to ~62% opacity), category badge, verification badge, source links opening in new tabs.
- Read-state persists in localStorage under key `news-briefing:<window-start>`. Preserve this key and story `id`s when editing so the user's read-state survives a refresh.
- Print stylesheet hides the toolbar and toggles; cards avoid page breaks.

## When editing
Change tokens, not scattered hex values. Keep all content in the `DASHBOARD_DATA` object — never hardcode story text into markup. Preserve the localStorage key and story `id`s.
