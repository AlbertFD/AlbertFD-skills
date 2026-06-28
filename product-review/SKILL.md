---
name: product-review
description: Research a product across retailer reviews, expert/pro reviews, and community discussion, then deliver a verified buy/skip verdict as a premium single-file interactive HTML report — with a value-for-money and reliability assessment, red-flag warnings (including fake-review risk), a transparent source-provenance breakdown, and ranked alternative products. Use this whenever the user wants to know if a product is "worth it", "any good", "worth buying", asks you to "review", "compare", or "research" a specific product, is deciding between options, links a product page, or asks "should I buy X" / "what's the best X" — even if they don't say "report" or "dashboard". Always cite where every rating and claim comes from and never invent ratings, quotes, prices, or links.
---

# Product Review

Turn a single product (or "what's the best X") into a trustworthy buy/skip decision, rendered as a polished interactive HTML report. The deliverable should feel like advice from a sharp friend who actually read every review — not a regurgitated marketing page or an unsourced star rating.

## Why this skill is shaped the way it is

Product research fails in three ways, and each one wastes the user's money or trust. **Fabrication**: a rating, price, quote, or link the model produced from memory that turns out to be wrong or nonexistent — fatal, because a purchase decision rides on it. **Marketing capture**: parroting the manufacturer's claims or a single glowing source as if it were an independent verdict. **Fake-review blindness**: treating a 4.8-star average as truth when the reviews are incentivized, AI-generated, or astroturfed. Everything below exists to defeat those three failures while still producing something genuinely decisive — the user wants an answer, not a shrug.

The user values provenance: every rating and claim in the report is treated like a citation, traceable to where it came from.

## Workflow

### 1. Pin down what's being reviewed and what matters

Resolve these before searching. Take answers already in the conversation; only ask about what's genuinely unknown (use the question tool if available).

- **The product**: the exact model/version. "AirPods" is ambiguous; "AirPods Pro 3" is reviewable. If the user gave a URL, fetch it to confirm the exact item, current price, and seller. If they asked "what's the best X", treat it as a category review — shortlist 3–5 leading contenders, then review the top pick in depth with the others as alternatives.
- **Use case & priorities**: who's buying and for what. A blender for daily smoothies vs. occasional use changes the verdict. If the user signalled priorities (budget, durability, a specific feature), weight the assessment toward them and say so.
- **Budget / price context**: note the current price and whether the user has a ceiling. "Worth it" is always relative to price.
- **Region**: affects price, availability, and which retailers/outlets are relevant. Infer from profile/folder/conversation; state your assumption.

### 2. Gather reviews across all three source types

Read `references/sources.md` before searching — it defines what counts as reputable in each tier, how to spot fake/incentivized reviews, and what to reject. Gather from all three tiers so the verdict triangulates rather than leaning on one voice:

- **Retailer reviews** — aggregate star ratings and verified-buyer reviews (Amazon, Best Buy, manufacturer store, major regional retailers). Capture the rating, the review count, and the *distribution* (a 4.3 from 12,000 reviews means something different from a 4.3 from 8). Read the critical reviews (1–3 star), not just the praise — that's where real defects surface.
- **Expert / pro reviews** — independent testing and editorial outlets (Wirecutter, RTINGS, TechRadar, CNET, DPReview, Consumer Reports, specialist press for the category). These do controlled testing and comparisons the crowd can't.
- **Community / forums** — real-owner sentiment from Reddit, category forums, and YouTube reviews. This is where long-term ownership problems, "I returned it because…", and honest comparisons live.

Use date-bounded web search and fetch product/review pages directly. For each source, record: the outlet, what kind of source it is (retailer/expert/community), its rating or verdict, the date, and the URL you actually retrieved. Collect more than you'll show so you can weigh consensus vs. outliers. Favor reviews from roughly the **current product generation** — a glowing review of last year's model can be misleading.

### 3. Verify before trusting — this is non-negotiable

A purchase decision is only as good as the evidence under it.

- **Every rating, price, quote, and link must be one you actually saw this session.** Never reconstruct a star rating, a price, a URL, or a reviewer quote from memory — model memory produces plausible fakes, and one fake number poisons the whole verdict.
- **Triangulate the verdict across independent sources.** A strength or flaw you want to assert should show up in more than one place, ideally across tiers (e.g. retailer reviewers *and* an expert teardown both flag the hinge). A claim that appears in only one source gets reported as such, not as settled fact.
- **Screen for fake / incentivized reviews** using the signals in `references/sources.md` (sudden rating spikes, repetitive phrasing, "received free in exchange for review", review count wildly out of line with the product's age/popularity, Fakespot/ReviewMeta-style red flags). If the retailer rating looks gamed, say so and lean harder on expert and community sources.
- **Prices change** — state the price you found, its source, and the date; never present a stale price as current.

Flag any assumption worth pressure-testing (e.g. a reliability concern that rests on a handful of forum posts, or a rating that may be inflated).

### 4. Form the verdict

The point of the report is a clear, defensible call. Build it on three pillars the user asked for:

- **Value for money** — is the price justified by the quality and the alternatives? This drives the headline buy/skip. Be willing to say "good product, wrong price — wait for a sale" or "cheaper alternative does 90% for 60% of the cost".
- **Reliability / longevity** — what does the evidence say about defects, durability, and how it holds up over months/years? Weight critical retailer reviews and long-term community reports heavily here.
- **Red flags** — dealbreakers, common complaints, and trust issues (fake-review suspicion, discontinued support, recurring defect, hidden costs like subscriptions or proprietary refills). If there are none, say so explicitly rather than omitting the section.

Translate this into a **verdict** (one of: *Buy* / *Buy on sale* / *Consider* / *Skip*), a short reason, and an overall **score from 1 to 10** that reflects your confidence-weighted assessment — not just an average of star ratings (one decimal place is fine, e.g. 8.6). Score each of the three pillars on the same **1–10 scale** too: for the red-flags pillar, treat it as a *trust* score where 10 means no red flags and a low number means serious dealbreakers. Also name **who it's right for** and **who should look elsewhere**.

Also distil two things the user explicitly wants front and centre:

- **Top 5 things to know** — the five most decision-relevant facts about the product, ordered most-important first. These are the things you'd tell a friend in 30 seconds: the standout strength, the price reality, the one big caveat, etc. Keep each to a single line.
- **The most common review per tier** — for each of the three tiers (retailer, expert, community), capture the *representative* sentiment: what most reviewers in that group actually say, as a short quote or paraphrase with attribution and a link. This shows the user the consensus in each camp at a glance, not just cherry-picked extremes.

### 5. Find alternatives

Give the user real options, not just a single verdict. Identify **2–4 alternative products** that a reviewer would genuinely cross-shop against: a cheaper "good enough" pick, a premium step-up, and a close direct rival are all useful archetypes. For each, give a one-line "choose this if…" and its key tradeoff vs. the main product, with at least one source. Don't invent alternatives — they must be real products you can source.

Also collect **where to buy it**: 2–4 real seller links (retailers / official store) with the price each one shows, so the user can act on the verdict immediately. Use only seller pages you actually retrieved this session — never reconstruct a store URL or price from memory.

### 6. Build the HTML report

Use the bundled template — don't write the page from scratch:

1. Read `assets/template.html`.
2. Build the data object described in the comment at the top of that file: product name/price/region, the verdict + score, the **top-5 things to know**, the three-pillar assessment, pros/cons, red flags, a sources array (each tagged retailer/expert/community with outlet, rating, date, URL), the **most-common-review-per-tier** `voices` object, the alternatives array, and the **buyLinks** array.
3. Replace the `__REPORT_DATA__` placeholder with your JSON object. Validate it: well-formed JSON, no unescaped `</script>`, every source and alternative has a real URL you retrieved this session.

The template provides the design: a verdict hero band with the score and buy/skip call, a three-pillar assessment (value / reliability / red flags), a pros-and-cons split, a **source-provenance table** color-coded by tier so the user can see exactly where each rating came from and how many sources back the verdict, an alternatives comparison, and a fake-review-risk indicator. It's opened as a local file in the user's browser, where any localStorage-based state works. For visual changes, edit the generated file and consult `references/design-spec.md` so changes stay coherent.

### 7. Deliver

Save the HTML to the user's folder as `product-review-<slug>-<YYYY-MM-DD>.html` and present it. In chat, give a 2–3 sentence summary: the verdict, the score, the single biggest reason, and the top alternative. Don't re-list everything — the report does that. Close with a "Sources" section listing the key links if you stated specific facts (ratings, prices) in the chat summary.

## Follow-up requests

- **"Compare it to <other product>"** — review the named rival to the same depth and render a side-by-side, promoting it from the alternatives list.
- **"Is the price good?"** — re-check current price across sellers and recent price history; update the value pillar and verdict.
- **"Are these reviews real?"** — re-run the fake-review screen in `references/sources.md` and report what you find, including the signals that drove the call.
- **"Refresh it"** — re-search from today; ratings, prices, and the current generation may have changed.

## Quality bar

Before delivering, check: the verdict is clear and defensible, every rating/price/quote/link was retrieved this session and resolves to the claimed source, the report draws on all three source tiers (or explains why one is missing), fake-review risk was actively screened, alternatives are real cross-shop options, and the source-provenance table makes it obvious where every claim came from. The user should be able to act on this and feel they made an informed decision — not just trust a number.
