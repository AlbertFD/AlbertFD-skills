---
name: living-sketch
description: Bring a concept, sketch, diagram, or written explanation to life as a single self-contained interactive HTML visual that sharpens how the idea is articulated. Use when the user wants to visualize, diagram, illustrate, sketch out, or "bring to life" a mechanism, process, system, or argument, or hands over a PDF, image, hand-drawn sketch, whiteboard photo, or paragraph to turn into a clear visual explanation — e.g. "help me explain X visually", "turn this sketch into a real diagram", "make an interactive figure of how X works", "I need a visual for my talk/paper". Calibrates to the audience's knowledge level and asks the purpose and one key takeaway first, then co-builds in checkpointed stages. For turning a research paper into a multi-tab study dashboard use paper-dashboard; for diagnosing a learner's misconception use learning-map.
---

# Living Sketch

Turn a concept, rough sketch, diagram, or written explanation into a single self-contained interactive HTML visual whose job is to make the idea *click* — and, in doing so, to sharpen how the user themselves articulates it. The deliverable is not decoration; it is an argument made visible. The bar is: "someone in the target audience looks at this and the concept lands, faster and more precisely than words alone would have managed."

The two things that make this skill different from just drawing a picture:

1. **It is co-created in stages, with the user in the loop.** You don't disappear and return with a finished artifact. You build the visual up in checkpointed stages and pause at each one so the user can steer. The act of building it together is itself the act of sharpening the explanation — the user discovers what they actually mean as the picture forces precision.
2. **It is calibrated before a single shape is drawn.** Depth (how much the audience already knows), purpose (where it will live), and the one key takeaway are settled up front, because each of those changes the whole composition, not just the labels.

`references/html-patterns.md` is the toolbox — a self-contained CSS design system plus working interactive patterns (SVG diagrams, hover-reveal labels, staged build-up animation, step-through narration, pan/zoom, MathJax, Chart.js). Read it before you build so you assemble from tested parts instead of reinventing them.

## Workflow at a glance

Intake (calibrate) → read the context → agree the plan → **build in checkpointed stages, pausing at each** → verify → save and present.

The checkpointed build is the heart of it. Do not skip the pauses to "save time" — the pauses are where the explanation gets sharp.

---

## Step 1 — Intake: calibrate before you draw

Before drawing anything, settle four things. If the user's opening message already answers some of these, don't re-ask — reflect back what you inferred and ask only about the gaps. Keep it to one compact round of questions; this is a warm-up, not an interrogation.

1. **Depth / knowledge level — always ask this.** This is the single most important calibration: how much does the intended viewer already know? It decides the vocabulary, how much gets explained vs. assumed, and how abstract the visual can be. Offer concrete anchors rather than vague labels, e.g.:
   - **Newcomer** — assume no background. Everyday analogies, define every term, no unexplained notation. The visual carries most of the load.
   - **Informed** — knows the field's basics. Use standard terminology, explain the non-obvious moves, skip the 101.
   - **Expert / peer** — fluent in the domain. Be precise and dense, use real notation, focus on the subtle or novel part; don't waste their time re-deriving fundamentals.

   Let depth genuinely change the artifact — a Newcomer visual should look visibly gentler (fewer symbols, more analogy, slower reveal) and an Expert one visibly denser (real equations, tighter labels, the interesting edge case foregrounded). Don't just swap word choice.

2. **Purpose / medium.** Where will this live and what is it for? A live talk slide (big, legible from the back, one idea per view, projector-safe contrast), a paper/report figure (print-friendly, captioned, static-export-able), a teaching aid (interactive, explore-at-your-own-pace), or the user's own private understanding (anything goes, optimize for insight). This shapes size, density, interactivity, and color.

3. **The one key takeaway.** Ask the user to name the single thing the viewer must walk away understanding. This becomes the spine of the composition — every element either serves it or gets cut. If the user can't name one, that's a useful signal: help them find it before drawing, because a visual without a thesis is just a busy picture. Often this question alone sharpens their articulation more than the finished file does.

4. **The source material.** Establish what you're working from (see *Reading the context* below) — a PDF, an image or photo of a sketch, a written paragraph, or just the surrounding conversation.

A good single intake message looks like: *"Before I sketch this — three quick calibrations: (a) who's the audience and how much do they already know — newcomer, informed, or expert? (b) where will this live — a talk slide, a paper figure, a teaching aid, or just for you? (c) if a viewer remembers only one thing, what should it be? And point me at whatever you've got — a sketch, a PDF, a paragraph, or just describe it."*

## Reading the context

The visual should fit *this* user's actual situation, not a generic version of the topic. Before building, pull in what's around you:

- **A handed-over artifact** — read it directly. A PDF (use the `pdf` skill or extract text), an image/photo of a hand sketch or whiteboard (read the image; transcribe the boxes, arrows, and labels the user drew — honor their structure, you are bringing *their* sketch to life, not replacing it), or a pasted written explanation.
- **The conversation so far** — the user may have explained the concept earlier in the chat. Mine it.
- **The project / folder context** — files, README, and project instructions in the working folder, and any user/project memory. If the surrounding context tells you the user's domain (e.g. their field, their tools, their prior work), match the visual's examples, notation, and rigor to it rather than defaulting to textbook generic.

When the user gives you a sketch, treat their layout as the source of truth for *what connects to what*; your job is to make it legible, correct, and alive — not to impose a different mental model unless theirs is actually wrong (in which case say so plainly and propose the fix).

## Step 2 — Agree the plan (one short checkpoint)

Before building, write a 3-6 line plan and get a quick yes. State: the key takeaway (one line), the central visual metaphor or layout you'll use (e.g. "a labelled cross-section", "a left-to-right pipeline", "an energy-level ladder", "nested boxes", "a state machine"), the 3-6 elements it will contain, and the one or two interactions that will carry the explanation (e.g. "hover each stage to reveal what it does", "a play button that builds the process up step by step"). 

This plan is cheap to change and expensive to ignore — a wrong metaphor discovered now costs a sentence; discovered after building costs the whole file. If the user already gave a very explicit brief, compress this to a single confirming line and move on.

Pick the visual metaphor deliberately — it is the most important design decision. Match it to the *shape* of the idea: sequential → pipeline/timeline/numbered steps; structural/spatial → cross-section/map/exploded view; relational → graph/network/nested sets; quantitative → chart; state-and-transition → state diagram; comparative → side-by-side. The right metaphor makes the takeaway feel obvious; the wrong one makes a simple idea look complicated.

## Step 3 — Build in checkpointed stages

Build the visual up in passes, and **pause after each pass to show the user where it stands and ask if it's tracking.** Each pause is a chance for the user to redirect before you've over-invested — and, more importantly, the conversation at each pause is where the explanation gets refined. Narrate briefly what you did and what's next; keep the file openable at every checkpoint so they can actually look.

The four stages:

1. **Structure** — lay out the skeleton: the canvas, the central metaphor's frame, and placeholder positions for the main elements. No detail yet, just the bones and the overall composition. *Checkpoint: "Here's the layout — does this arrangement match how you picture it?"* This is the cheapest moment to change the whole approach, so genuinely invite redirection here.

2. **Core elements** — draw the real elements in their right relationships: the boxes, bodies, nodes, arrows, levels, or curves that carry the actual content, correctly connected. Still minimal labelling. *Checkpoint: "The pieces and their connections are in — is anything mislabelled, missing, or connected wrong?"* Correctness of relationships matters most here; catch structural errors before they're buried under polish.

3. **Labels & annotations** — add the text that does the explaining: titles, labels, the key callout that states the takeaway, units, and short annotations calibrated to the depth level chosen in intake. *Checkpoint: "Read it as your audience would — does the wording land at the right level? Too much, too little?"*

4. **Interactivity & polish** — wire in the interaction that carries the explanation (hover reveals, staged build-up, step-through, pan/zoom), apply the color system, ensure legibility and responsive sizing, and add a static-friendly fallback if the medium needs print/export. *Checkpoint: final review.*

You can compress stages if the visual is simple or the user says "just build it" — but default to pausing, because the pauses are the feature. If the user is clearly engaged and steering, lean into more frequent check-ins; if they say "stop asking, just go", honor that and build straight through.

### How to build it well

- **Self-contained and offline-first.** One HTML file with all CSS and JS inlined, so it opens by double-clicking. Don't assume a CDN is reachable — many environments (offline, locked-down networks, restricted desktop sandboxes) block it, and a failed CDN fetch breaks the visual silently. Render **equations with plain HTML/CSS** rather than CDN-loaded MathJax (see `references/html-patterns.md` §7); reserve MathJax/Chart.js for cases that truly need them, and only after confirming the CDN works in the target environment — otherwise inline a pre-rendered fallback. No `localStorage`/`sessionStorage`.
- **Prefer SVG for diagrams.** Hand-authored inline SVG gives you crisp, labelable, animatable shapes with full control — far better than canvas for explanatory diagrams, and it needs no external library. Use Chart.js only when the point is quantitative data and the CDN is available.
- **Drive all color from CSS custom properties** (see the design system in `references/html-patterns.md`) so the palette is consistent and easy to reroll. Don't hand-pick clashing colors per element.
- **Let the interaction teach.** The best interactions externalize the explanation: a staged build-up shows causality in order; hover-reveal lets the viewer ask "what's this?" exactly when they wonder; a step-through narrates the logic one move at a time. Avoid interactivity that's just motion — every interaction should answer a question the viewer would actually have.
- **Legibility is non-negotiable**, especially for the "talk slide" medium: large type, high contrast, generous spacing, nothing that vanishes against the background on a projector.

## Step 4 — Verify before delivering

- **Re-compare against the source — the fidelity check.** This is the step that closes the loop, so do it deliberately, not by memory. Put the finished visual next to what you started from and confirm they actually coincide:
  - **If the source was an image or sketch** (a PDF figure, a photo of a whiteboard, a hand drawing), you cannot judge fidelity from the code — you must *see* the rendered output. Open the HTML and screenshot it (or render it) and view that screenshot beside the original image. Walk the original element by element: every box/body/node, every arrow and its **direction**, every label and axis the user drew — is each one present, correctly placed, correctly connected, and correctly named in your version? Then walk your version back the other way: did you *add* anything the source didn't have, or silently drop or rename anything it did? Pay special attention to arrow/flow direction and to axis orientation, which are the easiest things to flip.
  - **If the source was a written explanation** (a paragraph, the chat, a description), re-read it line by line and check that each claim, relationship, and step it states is represented in the visual, and that the visual doesn't assert anything the text didn't.
  - Where the visual deliberately departs from the source (you fixed an error, simplified, or inferred a missing link), that's fine — but it must be a *flagged* choice you tell the user about, not a silent drift. List those departures in the delivery message so the user can confirm them.

  The goal is that the user can hold the original and the result side by side and agree they're the same idea, only sharper.
- **Syntax-check the JavaScript** — extract the main `<script>` and run `node --check`. A stray character silently disables every interaction. Watch for apostrophes inside single-quoted strings; prefer template literals or double quotes for text.
- **Check correctness of the content**, not just that it renders. The whole value is a *correct* explanation — a beautiful diagram of a wrong mechanism is worse than no diagram. Verify the relationships, the direction of every arrow/flow, the labels, units, and any numbers against the source. **Flag any claim you inferred or assumed rather than took from the source, so the user can pressure-test it** — an honest "I assumed the second stage feeds the third; confirm?" is far more valuable than a confident guess.
- **Read it back at the chosen depth level.** Put yourself in the audience's shoes: would a newcomer actually follow this, or did jargon creep in? Would an expert find it patronizing or imprecise?
- **Confirm it serves the one takeaway.** If an element doesn't help the viewer reach the key takeaway, cut it. Busy is the enemy of clear.
- **Confirm equations actually render in the browser, not as raw LaTeX.** If you used MathJax, check it didn't silently fall back to showing `\( ... \)` because the CDN was blocked — if there's any doubt, switch to the dependency-free HTML/CSS math. Any chart's axes must be honest (label reconstructions as such; never present invented data as real).

## Step 5 — Save and present

Save the HTML file to the working folder and present it. In the message, restate the one key takeaway the visual is built around and explicitly list any assumptions you made that the user should pressure-test. Offer the obvious next moves: adjust the depth, change the medium (e.g. "want a print-friendly static version for the paper?"), or push deeper on any element.

## Principles that make these good

**The picture forces precision.** A paragraph can hide vagueness; a diagram cannot — every arrow has to point somewhere, every box has to be a real thing. Use that. When the visual won't come together, it's usually because the underlying idea isn't yet sharp; surface that to the user rather than papering over it with decoration. Sharpening the articulation *is* the job.

**One idea, well.** Resist the urge to explain everything. A visual that nails one takeaway beats one that gestures at five. Things that don't serve the spine get cut, not shrunk.

**Honor the user's sketch.** When they hand you a drawing, you're amplifying their thinking, not overwriting it. Keep their structure and vocabulary unless it's actually wrong, and if it is, say why and propose the fix rather than silently changing it.

**Calibrate, don't dumb down.** Newcomer ≠ childish; expert ≠ cluttered. Each depth level is a different *correct* artifact, not the same one with more or fewer words.

**Flag your assumptions.** You will often have to infer a connection the source left implicit. That's fine — but mark it, so the user can confirm or correct. A flagged assumption invites the conversation that sharpens the explanation; a hidden one quietly ships an error.

**Self-contained and openable — assume no network.** One file, double-click to open, everything inlined. Don't depend on a CDN you haven't verified reaches the user's environment; render math as HTML/CSS so it can't break offline. The user should be able to drop it into a talk, a folder, or an email and have it just work.
