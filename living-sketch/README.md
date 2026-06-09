# living-sketch

Bring a concept, sketch, diagram, or written explanation to life as a single
self-contained **interactive HTML visual** — and, in the process, sharpen how you
articulate the idea itself.

Hand it a PDF, a photo of a whiteboard, a rough sketch, a paragraph, or just the
conversation so far. It calibrates first (audience knowledge level, where the visual
will live, and the one key takeaway), then **co-builds the visual with you in
checkpointed stages** — structure → core elements → labels → interactivity — pausing
at each so you can steer. The pauses are the point: a diagram forces precision a
paragraph can hide, so building it together is where the explanation gets sharp.

Output is one **offline-first** HTML file — all CSS and JS inlined, equations rendered
in plain HTML/CSS (no MathJax/CDN to fail in locked-down or offline environments),
sized for its medium: a talk slide, a paper figure, a teaching aid, or your own
understanding. Before delivering, it runs a **source-fidelity check** — comparing the
finished visual against your original element by element and flagging any deliberate
departures.

## When it triggers

"Help me explain X visually", "turn this sketch into a real diagram", "make an
interactive figure of how X works", "I need a visual for my talk/paper", or whenever a
picture would do the explaining better than words.

Related skills: use **paper-dashboard** to turn a whole research paper into a multi-tab
study dashboard; use **learning-map** to diagnose and teach around a learner's specific
misconception. `living-sketch` is for a focused, articulate visual of one concept.

## Contents

- `SKILL.md` — the workflow (intake → context → plan → staged build → verify → present).
- `references/html-patterns.md` — toolbox: CSS design system, SVG diagram primitives,
  dependency-free HTML/CSS equations (with sizing + alignment rules), hover-reveal,
  staged build-up, step-through, figure↔step cue syncing, pan/zoom, fit-the-viewport,
  print/export.
