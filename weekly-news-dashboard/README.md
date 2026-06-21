# weekly-news-dashboard

Turns the past week's news into a verified, scannable briefing rendered as one
self-contained interactive HTML page — the most important stories across Science,
Economics, Politics, and your local area, each summarized in plain language and
backed by two independent reputable sources.

## What it does

- Gathers candidates from a curated allowlist of reputable outlets (wire services,
  newspapers of record, and primary institutional sources), then curates down to the
  ~4–5 most consequential stories per category.
- Verifies every story against a second independent source; single-source stories are
  included only when flagged as such. Nothing is reconstructed from memory.
- Builds a premium HTML dashboard: category-color-coded cards, verification badges,
  filter/search toolbar, and read-state that persists in the browser.

## Inputs

- **Location** (required, no default) — your area for the Local section, e.g.
  "Geneva & neighbouring France".
- **Categories** — defaults to all four; drop or add as you like.
- **Timeframe** — defaults to the last 7 days.

## Output

`news-briefing-<date>.html`, saved to your folder and ready to open in any browser.

## Files

- `SKILL.md` — workflow and the verification standard.
- `references/sources.md` — the reputable allowlist, what to reject, regional outlets.
- `references/design-spec.md` — design system for editing the generated page.
- `assets/template.html` — the dashboard template (data goes in `__DASHBOARD_DATA__`).

## Tip

A weekly briefing is a natural recurring task — ask to have it run automatically every
Monday morning.
