# quiz-maker

Builds a self-contained **interactive HTML quiz** on any topic. Every question
comes with a simplified explanation, an optional step-by-step derivation with
rendered equations (MathJax), and a real citation.

**Always asks the difficulty level first** — Foundational, Intermediate, Advanced,
Expert, or PhD/Research — because difficulty changes the whole quiz.

## What the learner gets

- Multiple-choice (auto-graded, plausible distractors), numeric (tolerance-checked),
  and open/self-graded derivation questions.
- Immediate right/wrong feedback with a plain-language explanation.
- Collapsible "show next step" derivations for quantitative questions.
- Citation links for every explanation — never fabricated.
- Progress bar, live score, and an end-of-quiz summary with retake/review.

## Files

- `SKILL.md` — the skill: workflow, difficulty-first rule, citation policy.
- `assets/quiz_template.html` — the interactive template; fill the `QUIZ` data block.
- `references/html-format.md` — build procedure and the `QUIZ` schema.
- `example_output_quiz.html` — a rendered example (Special Relativity, Advanced).

## Usage

Trigger it by asking for a quiz, test, practice problems, or "quiz me on X".
The skill confirms topic + difficulty + question count, researches and cites, then
outputs `quiz-<topic>-<difficulty>.html`.
