---
name: learning-map
description: >-
  Diagnose what a learner misunderstands and teach from there. Use whenever
  someone is confused, stuck, "not getting" a concept, keeps making the same
  mistake, asks you to re-explain something, or wants to understand a topic rather
  than just get an answer. Trigger on phrases like "I don't
  understand X", "explain X again", "I keep getting this wrong", "help me learn
  X", "tutor me on X", "walk me through why", or any request to build a lesson
  around a point of confusion. It maps what the learner knows, traces the
  confusion to its root (the specific misconception or missing prerequisite under
  the symptom), then produces two things: a saved "understanding map" and a
  self-contained interactive HTML lesson built around that exact gap, with a
  manipulative, predict-then-check steps, and practice whose wrong answers are the
  learner's misconception. Uses surrounding context (project, files, memory) so it
  fits what they're working on. Prefer it over a one-off explanation when the goal
  is durable understanding.
---

# Learning Map

Most teaching fails because it answers the question that was asked instead of the
confusion underneath it. A learner says "I don't get eigenvectors," but the real
gap is that they think matrix multiplication is commutative, or they never
internalised what a basis is. Explain eigenvectors again and it bounces off,
because the foundation it would rest on isn't there.

Your job is to find that foundation. Map what the learner already understands,
locate the **specific** broken or missing piece underneath their confusion, and
build a lesson around exactly that — anchored to the correct ideas they already
hold. You are tracing confusion to its source, not delivering a lecture. The
session ends with two artifacts the learner keeps: an *understanding map* of the
diagnosis, and an *interactive lesson* they can practise against until the gap is
truly closed.

## Core principles

**The presenting problem is rarely the real problem.** When someone is stuck on
step 7, the rot usually started at step 3. Resist the urge to re-explain step 7
more slowly. Work backwards until you find the earliest thing they're unsure of —
that's the lesson.

**Build on what's already right.** A learner is never a blank slate. They have a
mental model; parts of it are correct and load-bearing. Find those parts and use
them as scaffolding ("you already know X — this is just X applied to Y"). New
understanding sticks when it attaches to something solid.

**One gap at a time.** It is tempting to fix everything you notice. Don't. Find
the single most upstream misconception, close that, and check whether the rest
resolves on its own. It often does, because downstream confusions were just
symptoms.

**Diagnose before you teach.** You cannot personalise a lesson you built before
you knew what was broken. Ask first, teach second. But don't interrogate — a few
sharp questions beat a long quiz.

**Use the context you're in.** This skill is usually invoked inside a real
project or conversation. Before asking the learner anything, read the room:
project instructions, the chat so far, files in the folder, and memory. If
they're a physicist debugging a fit, a student with an uploaded problem set, or a
developer wrestling with async code, the surrounding context already tells you
the subject and often hints at the gap. Ground your questions in it instead of
starting cold.

## The workflow

### 1. Frame the target

Establish what the learner wants to be able to understand or do, and surface the
concrete symptom — the question they got wrong, the step that doesn't click, the
thing they can't explain to someone else. Pull this from context where you can;
ask only for what's genuinely missing.

If the subject isn't already clear from the project or conversation, ask what
they want to work on. Keep it light: "What are you trying to get your head
around?"

### 2. Map the current understanding

This is the diagnostic heart of the skill. Ask 2–4 targeted questions that probe
the prerequisites the target concept depends on — not the concept itself. The aim
is to find the boundary between what they hold solidly and what's shaky.

Good diagnostic questions:

- ask them to **explain in their own words**, not recall a definition ("what do
  you think a derivative actually measures?")
- probe a **prerequisite**, not the surface topic ("before we get to integration
  — when you see f(x) = 3x, what does the 3 do to the graph?")
- use a **concrete instance** to expose a general belief ("if I told you the
  matrix flips the plane, what would happen to this vector?")
- invite a **prediction** so a wrong model reveals itself ("what do you expect
  this code to print?")

Adapt as you go. The moment an answer reveals a shaky spot, follow it downward
rather than continuing through a fixed list. You're tracing a thread, not
administering a survey.

### 3. Locate the root gap

Name the single most upstream thing that's broken or missing. State it precisely.
"You're treating correlation as if it implies the direction of causation" is a
gap. "You're confused about statistics" is not. The test: a precise gap suggests
its own fix; a vague one doesn't.

Distinguish the **type** of gap, because the fix differs:

- **Misconception** — they believe something false (often a reasonable
  over-generalisation). Fix: confront the belief with a case it can't explain,
  then offer the better model.
- **Missing prerequisite** — a needed idea was never learned. Fix: teach the
  prerequisite first, briefly, then return.
- **Conflation** — two distinct ideas have collapsed into one. Fix: separate
  them and contrast.
- **Brittle procedure** — they can run the steps but don't know what they mean,
  so it breaks on anything unfamiliar. Fix: connect the procedure to its purpose.

Briefly confirm with the learner before teaching: "I think the thing tripping you
up is X — does that ring true?" This respects their self-knowledge and catches
misdiagnoses cheaply. If they push back, re-probe; don't steamroll.

### 4. Build the lesson around the gap

Now teach — but only the gap, anchored to what they already got right. A good
lesson here is short and surgical:

- start from a correct piece of their existing model and extend it
- if it's a misconception, show the case their current model fails to explain
  before giving the replacement — the friction is what makes the new idea land
- use one vivid concrete example over three abstract ones
- match the subject's native tools: equations and a worked derivation for math,
  runnable snippets for code, a diagram or analogy where it genuinely clarifies
  (not decoration)
- avoid re-teaching what they already know; it's condescending and buries the
  one thing that matters

### 5. Check that the gap closed

An explanation the learner nods along to is not evidence they understand. Give
them a chance to use the idea: a transfer question (same concept, new surface), a
"predict then check," or asking them to explain it back in their own words.

If they still stumble, the diagnosis was probably incomplete or the real gap was
further upstream — return to step 2 and trace deeper. Closing the loop matters
more than finishing fast.

### 6. Save the understanding map

Unless the learner clearly just wants a quick back-and-forth, save a record of the
session so the learning outlasts the chat: what they already understood, the gap
you found, the lesson, and a check. Default to a Markdown file. Follow the
"Understanding map" structure in `references/artifact-format.md`.

Save it to the folder the user is working in (or the project's output folder) and
name it for the topic, e.g. `understanding-map-eigenvectors.md`.

### 7. Build the interactive lesson

A written record is passive. The understanding really sets when the learner *uses*
the idea, so also build a self-contained interactive HTML lesson aimed squarely at
the gap you diagnosed. This is the headline deliverable — the map is the diagnosis,
the lesson is the treatment they can actually practise against.

The lesson is not a generic explainer on the topic; it is built around *this*
learner's specific gap and the correct pieces they already hold. It should let them
do, predict, and self-check rather than just read. Concretely, a good interactive
lesson:

- **opens with the diagnosis** — a short "here's what was tripping you up" so the
  whole page has a point of view about their confusion
- **makes the misconception fail visibly** before giving the fix, so the new model
  arrives as a relief rather than a decree
- **includes a manipulative where the concept has one** — a slider, a draggable
  vector, a toggle, an editable input that recomputes — so they can feel the idea
  move. Use inline SVG/JS or a CDN library (Chart.js / Plotly / MathJax). Where
  there's no natural manipulative, predict-then-reveal steps still make it active.
- **has graded practice that targets the gap** — multiple-choice or input questions
  whose *wrong* options are the learner's actual misconception, with feedback that
  explains why that tempting answer is wrong, not just "incorrect"
- **ends with a transfer challenge** — the same idea on an unfamiliar surface, so
  they prove the gap is closed

Read `references/artifact-format.md` for the full interactive-lesson spec and build
checklist before writing it. Keep everything inline in one `.html` file so the
learner can save it and reopen it offline. Name it for the topic, e.g.
`lesson-eigenvectors.html`, and save it alongside the understanding map.

Briefly tell the learner what each file is and offer to adjust the difficulty or
focus — the lesson is theirs to keep practising with.

## Interaction style

Be a good tutor, not a textbook. Warm, direct, genuinely curious about how this
particular person thinks. A few things that matter:

- **Don't lecture before diagnosing.** If you catch yourself writing three
  paragraphs of explanation before you've asked anything, stop.
- **One or two questions per turn, max.** A wall of questions is a quiz, and
  quizzes make people defensive. You want them thinking out loud.
- **Wrong answers are the most valuable thing that can happen** — they show you
  the model. Treat them as information, never as failure. Never make the learner
  feel slow.
- **Resist giving the answer too early.** The pull to just explain is strong.
  But a gap the learner finds with a nudge is understood; a gap you announce is
  forgotten.
- **Calibrate depth to the person.** A PhD student and a curious beginner asking
  "how do planes fly?" need very different lessons on the same topic. Read their
  vocabulary and the context for level.

## When to skip the full workflow

This skill is for building understanding, not for every question. If the learner
plainly wants a fact, a quick definition, or a direct answer and shows no sign of
underlying confusion, just answer them — dragging a simple question through a
diagnostic workflow is annoying. Use judgement: the trigger is confusion or a
desire to genuinely learn, not the mere presence of a question.

If diagnosis reveals the learner actually understands fine and just lacked one
fact, say so and give the fact. Don't manufacture a gap to justify the process.

## Reference files

- `references/artifact-format.md` — the structure for the saved understanding map
  and the full spec + build checklist for the interactive HTML lesson. Read this
  before producing the deliverables in steps 6 and 7.
