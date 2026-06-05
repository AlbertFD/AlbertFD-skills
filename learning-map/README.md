# learning-map

**Diagnose what a learner actually misunderstands, then teach from there.**

Most teaching answers the question that was asked instead of the confusion
underneath it. `learning-map` does the opposite: it maps what the learner already
understands, traces their confusion to its *root* (the specific misconception or
missing prerequisite under the surface symptom), and builds a lesson around exactly
that gap — anchored to the correct ideas they already hold.

Subject is chosen at runtime, so it works for anything — math, physics, code,
languages, music, electronics. It also reads the surrounding context (the current
project, the ongoing chat, uploaded files, memory) so the diagnosis fits what the
learner is really working on instead of starting cold.

## What it produces

Every session ends with two files the learner keeps:

1. **Understanding map** (`understanding-map-<topic>.md`) — the diagnosis: what you
   already understood, the gap that was found (named and *typed*), the lesson, a
   self-check, and where to go next.
2. **Interactive lesson** (`lesson-<topic>.html`) — a self-contained, offline HTML
   page built around the gap, with a working **manipulative** (slider, draggable,
   toggle, or editable input), predict-then-check steps, and graded practice whose
   wrong answers *are* the learner's actual misconception, with feedback that
   explains why each trap is tempting.

## How it works

A six-to-seven step loop:

1. **Frame the target** — the concrete symptom (the wrong answer, the step that
   won't click).
2. **Map the current understanding** — 2–4 sharp questions that probe the
   *prerequisites*, not the surface topic, to find the boundary of solid knowledge.
3. **Locate the root gap** — the single most upstream broken piece, typed as a
   misconception, missing prerequisite, conflation, or brittle procedure.
4. **Confirm** the gap with the learner before teaching.
5. **Teach surgically** — only the gap, built on what they already got right.
6. **Check it closed** — a transfer question, not just a nod.
7. **Build the deliverables** — the understanding map and the interactive lesson.

## When it triggers

Phrases like "I don't understand X," "I keep getting this wrong," "explain X
again," "help me actually get Y," "tutor me on Z," or any request to build a lesson
or study page around a specific point of confusion. It deliberately *skips* the full
workflow when someone just wants a quick fact — no manufacturing a gap to justify
the process.

## Files

```
learning-map/
├── SKILL.md                                  # the skill
├── references/
│   └── artifact-format.md                    # understanding-map + interactive-lesson spec
├── example_output_lesson_eigenvectors.html   # a real interactive lesson
└── example_output_map_eigenvectors.md        # the matching understanding map
```

## Example

Open `example_output_lesson_eigenvectors.html` to see the interactive lesson the
skill builds — drag the 2×2 matrix sliders to watch the plane transform, see the
eigenlines appear and vanish, and work the misconception-targeted practice.
