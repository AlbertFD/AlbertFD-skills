# product-review

Research a product across **retailer reviews, expert/pro reviews, and community discussion**, then deliver a verified **buy/skip verdict** as a polished single-file interactive HTML report.

## What it produces

- A **verdict** (Buy / Buy on sale / Consider / Skip) and an overall **1–10 score**
- **Top 5 things to know** about the product, most important first
- A three-pillar assessment: **value for money**, **reliability & longevity**, and **red flags** (each scored 1–10)
- Pros & cons, and who the product is (and isn't) right for
- A **source-provenance table** color-coded by tier, so you can see exactly where every rating came from
- **The most common review per tier** (retailer / expert / community)
- A **fake-review-risk** indicator
- **2–4 real alternative products** with "choose this if…" guidance
- **Where-to-buy links** with prices

## When it triggers

"Is the Sony XM5 worth it?", "should I buy this <link>", "review this product", "what's the best budget espresso machine", "compare X vs Y" — anything where someone is deciding what to buy.

## How it works

1. Pins down the exact product, use case, budget, and region.
2. Gathers reviews across all three tiers (`references/sources.md` defines the reputable allowlist and the fake-review screen).
3. Verifies every rating, price, quote, and link against sources retrieved that session — nothing from memory.
4. Forms a defensible verdict built on value, reliability, and red flags.
5. Sources real cross-shop alternatives.
6. Renders everything into `assets/template.html`.

## Files

- `SKILL.md` — workflow and quality bar
- `references/sources.md` — source tiers, fake-review detection, what to reject
- `references/design-spec.md` — report layout and visual rules
- `assets/template.html` — the report template (data-driven; replace `__REPORT_DATA__`)
- `evals/evals.json` — test prompts

Output is saved as `product-review-<slug>-<date>.html` and opens straight from your folder.
