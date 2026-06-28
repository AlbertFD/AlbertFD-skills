# Design spec

The template is a single self-contained HTML file (no external assets, no network calls) so it opens straight from the user's folder. Keep it that way when editing.

## Layout order
1. **Verdict hero** — product name, current price + region, the verdict pill (Buy / Buy on sale / Consider / Skip), the 1–10 score as a ring/dial, and the one-line reason.
2. **Top 5 things to know** — numbered list of the five most decision-relevant facts, most important first.
3. **Who it's for / not for** — two short columns.
4. **Three-pillar assessment** — Value for money, Reliability & longevity, Red flags. Each pillar shows a 1–10 score badge, a short rating label, and 2–4 supporting bullets.
5. **Pros & cons** — two-column split, each point traceable to the evidence.
6. **Source provenance table** — every source as a row: outlet, tier (retailer/expert/community, color-coded), rating/verdict, date, link. This is the trust centerpiece — it must make "where did this come from" obvious at a glance, including a fake-review-risk badge.
7. **What reviewers most commonly say** — three tier-colored cards, one representative/common review per tier (retailer, expert, community) with attribution and link.
8. **Alternatives** — cards/rows: name, price, "choose this if…", key tradeoff, link.
9. **Where to buy** — seller buttons with price and link.

## Visual language
- Tier colors: retailer = amber, expert = blue, community = green. Use consistently in the source table and any source badges.
- Verdict colors: Buy = green, Buy on sale = teal, Consider = amber, Skip = red.
- Clean, calm, document-like. One accent per verdict state; generous whitespace; readable at a glance and in print.
- Score ring uses conic-gradient or an SVG arc; color it by verdict band.
- Mobile-friendly: columns collapse to a single column under ~700px.

## Hard rules
- No fabricated links — every `url` in the data must be real.
- Escape any `</script>` in data; the data object is injected into a `<script>` block.
- Include a `print` stylesheet so the report exports cleanly to PDF.
- Degrade gracefully if an optional field (e.g. an alternative's price) is missing.
