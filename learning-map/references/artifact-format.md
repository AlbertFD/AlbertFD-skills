# Artifact format

A session produces two files: the **understanding map** (the diagnosis, in
Markdown) and the **interactive lesson** (the treatment, a self-contained HTML
page the learner practises against). The map records *what* was wrong; the lesson
lets them *fix* it by doing. Build both, and keep them specific to this learner —
a generic explainer they could have googled defeats the purpose.

---

## Part 1 — The understanding map (Markdown)

A durable record the learner can revisit when the chat is gone. Use this skeleton;
adapt headings to the subject but keep the spine (map → gap → lesson → check → next).

```markdown
# Understanding Map: [Topic]

*[Learner's name or "you"] · [date] · subject: [field]*

## What you already understand
An honest inventory of the correct, load-bearing pieces of their model — the
scaffolding the lesson was built on. Naming these reassures the learner they
weren't starting from zero.

## The gap we found
The single root misconception or missing prerequisite, stated precisely, plus its
*type* (misconception / missing prerequisite / conflation / brittle procedure).
One or two sentences linking the root cause to the symptom they came in with.

## The lesson
The surgical explanation that closes the gap, anchored to what they already knew,
with the worked example/equation/snippet that made it land. Self-contained enough
to re-read cold.

## Check yourself
1–3 transfer questions (same idea, new surface) with answers in a
collapsed/footnote section so they can try first.

## Where to go next
The natural next concept, or a prerequisite still worth firming up. One or two
sentences.
```

---

## Part 2 — The interactive lesson (self-contained HTML)

This is the headline deliverable. One `.html` file, no external dependencies except
CDN scripts, that the learner can open offline and practise against. It is built
around the *diagnosed gap* — not a survey of the whole topic.

### Required sections (in order)

1. **The diagnosis** — a short banner/intro: "Here's what was tripping you up,"
   naming the specific gap. This gives the page a point of view about *their*
   confusion instead of being a generic lesson.

2. **Make the misconception fail** — present the case their old model can't
   explain, interactively where possible (e.g. let them predict the result, then
   reveal it). The friction is what makes the fix land. Don't skip to the answer.

3. **The fix, with a manipulative** — teach the correct model, and give them
   something to *move*:
   - a **slider** that recomputes a value/curve (Chart.js or inline JS)
   - a **draggable** element or clickable diagram (inline SVG + JS)
   - an **editable input** that re-evaluates a formula or runs a snippet
   - a **toggle** that switches between the wrong and right mental model
   Pick the one that makes *this* concept tangible. Where a concept has no natural
   manipulative, predict-then-reveal steps keep it active.

4. **Graded practice that targets the gap** — 2–4 questions where the *distractor*
   options are the learner's actual misconception. Feedback must explain *why* the
   tempting wrong answer is wrong (it's the most teachable moment), not just mark
   it incorrect. Use buttons/inputs with immediate, specific feedback.

5. **Transfer challenge** — one final problem putting the same idea on an
   unfamiliar surface. Passing it is the evidence the gap is closed. Reveal a
   worked solution after they attempt it.

### Build checklist

- **Single file.** Inline all CSS and JS. CDN allowed only for MathJax, Chart.js,
  or Plotly. No `localStorage`/`sessionStorage` — keep state in JS variables.
- **Interactive, not a slideshow.** If the learner can finish the page without
  clicking, typing, or dragging anything, it isn't done. Every section after the
  diagnosis should ask them to *do* something.
- **Feedback teaches.** Right/wrong responses reference the specific misconception
  by name. "Not quite — that's the 'dividing always shrinks' instinct again;
  remember we're asking how many quarters fit." beats "Incorrect."
- **Match the subject's tools.** MathJax for equations, a coordinate plane for
  geometry/linear algebra, a Chart.js plot for anything with data or a curve, a
  runnable/editable snippet for code.
- **Calibrate to the learner.** Vocabulary and difficulty should match the level
  you diagnosed — an expert lesson uses proper notation and skips basics; a
  beginner lesson leans on concrete manipulatives.
- **Readable.** Max content width ~720px, generous spacing, light/neutral theme,
  works offline.
- **Math must fit the screen.** Rendered equations (especially matrices, large
  fractions, and display math) overflow narrow viewports and look oversized by
  default. Configure MathJax to render slightly smaller and make every equation
  responsive so it scales down or scrolls instead of spilling off-screen. Use this
  exact setup:

  ```html
  <script>
    window.MathJax = {
      tex: { inlineMath: [['\\(','\\)']], displayMath: [['$$','$$']] },
      svg: { scale: 0.9 }      /* shrink symbols ~10% from default */
    };
  </script>
  <script async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.2/es5/tex-svg.min.js"></script>
  ```

  ```css
  mjx-container{max-width:100%;}
  mjx-container[display="true"]{overflow-x:auto;overflow-y:hidden;}
  mjx-container[display="true"] svg{max-width:100%;height:auto;}
  ```

  Prefer inline math (`\(...\)`) for short expressions inside sentences; reserve
  display math (`$$...$$`) for the one or two equations that truly deserve a line of
  their own. Don't put a full matrix in running text — it balloons the line height.

### Manipulative ideas by domain (illustrative, not exhaustive)

- **Linear algebra** — a 2×2 matrix whose entries are sliders, with a live grid /
  unit circle showing the transformation and the eigenvectors highlighted.
- **Calculus** — a draggable point on a curve showing the tangent slope; a
  Riemann-sum slider for `n`.
- **Statistics** — a slider on assumed σ that recomputes reduced χ² live so the
  learner sees the 1/σ² relationship move.
- **Fractions / arithmetic** — a number line or bar the learner partitions to
  count "how many fit."
- **Programming** — an editable code box that runs and prints, with a
  predict-the-output gate before the run.

Name the file for the topic, e.g. `lesson-eigenvectors.html`, and save it beside
the understanding map.
