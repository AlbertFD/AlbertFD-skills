---
name: quiz-maker
description: >-
  Build a self-contained interactive HTML quiz on any topic, with simplified,
  clearly-explained answers that can include rendered equations and full
  derivations, plus real citations for every explanation. ALWAYS ask the user
  which difficulty level they want (Foundational, Intermediate, Advanced, Expert,
  or PhD/Research) BEFORE generating anything. Use this skill whenever the user
  wants a quiz, test, practice questions, flashcards, a self-check, exam prep,
  "quiz me on X", "test my knowledge of X", "make me some practice problems", or
  wants to study or revise a subject through questions — even if they don't say
  the word "quiz". Prefer it over a plain list of Q&A whenever the user wants to
  actually practice, self-grade, or study interactively. For diagnosing a single
  stubborn misconception use learning-map instead; for turning one paper into a
  study page use paper-dashboard. This skill is for practice-by-questions across a
  topic.
---

# Quiz Maker

A good quiz does two jobs at once: it tests what someone knows, and it teaches
them the moment they get something wrong. Most auto-generated quizzes do only the
first — a bare question, a right answer, nothing that helps the learner
understand *why*. This skill exists to do the second job well. Every question
comes with a simplified explanation the learner can actually follow, the equation
or derivation behind it when the topic is quantitative, and a real citation so
they can go deeper and trust the answer.

The output is a single interactive HTML file the user can open in a browser,
answer at their own pace, check themselves, reveal worked derivations, and score.
It should feel like a well-made study tool, not a printout.

## The one rule that comes first: ask difficulty before you build

Difficulty changes *everything* about the quiz — the vocabulary, whether you show
a derivation or just state a result, how many steps a problem has, how much you
assume the reader already knows. So you cannot write a single good question until
you know the level. **Ask the user which level they want before generating the
quiz**, using the AskUserQuestion tool with these five options:

- **Foundational** — first exposure. Plain language, concrete examples, minimal
  jargon, results stated without derivation. Think curious beginner or early
  high-school.
- **Intermediate** — comfortable with the basics. Introduces the standard
  terminology and simple one- or two-step reasoning. Think strong high-school or
  early undergraduate.
- **Advanced** — solid working knowledge. Multi-step problems, expects fluency
  with the core formalism, short derivations shown. Think upper undergraduate.
- **Expert** — deep command. Non-obvious edge cases, connections between ideas,
  full derivations expected. Think graduate coursework.
- **PhD / Research** — frontier. Subtle assumptions, current debates, rigorous
  derivations, primary-literature citations. Think qualifying exam or research
  seminar.

If the user already stated a level in their message ("give me a hard PhD-level
quiz on..."), map it to the nearest option and confirm rather than re-asking.
While you're asking difficulty, it's efficient to also confirm the **topic** (if
at all fuzzy) and **how many questions** they want (default 8) in the same
AskUserQuestion call — but difficulty is the one you must never skip.

## Get the topic right

Read the room before you ask. The topic may already be obvious from the user's
message, the project instructions, files in the folder, or the conversation so
far. If the user works in a specialised field (their profile or CLAUDE.md often
says so), pitch examples in their world rather than generic ones — a physicist
gets antimatter and cross-sections, not "a ball rolling down a hill", unless they
asked for the ball. Only ask for clarification when the topic is genuinely
ambiguous or too broad to make a coherent quiz ("science" is too broad; "special
relativity — time dilation and length contraction" is a quiz).

## Research and cite — never fabricate

Every explanation carries a citation, and the citation has to be real. This is
the difference between a study tool someone can trust and a plausible-sounding
hallucination.

**For technical, scientific, medical, historical, or fast-moving topics, search
the web** to ground the explanation and pull a verifiable source — a textbook
with edition and chapter, a review article with DOI, a standards body, a
reputable reference site. Prefer primary and authoritative sources over blogs.
Capture a real URL or DOI so the citation links out.

**For stable, general-knowledge topics** where you have high confidence (basic
arithmetic, well-established definitions), it's fine to cite a standard reference
from knowledge without a live search — but name a *specific, checkable* source
(e.g. "Griffiths, *Introduction to Electrodynamics*, 4th ed., §2.3"), never a
vague "textbooks" or an invented page number.

If you cannot find a real source for a claim, that's a signal the claim may be
shaky — reword the question around something you *can* source, rather than
inventing a citation. Faking a citation is worse than having none.

## Write the questions

Aim for a mix that actually exercises understanding, not just recall. Good quizzes
lean on questions that make the learner *apply* an idea. Vary the format:

- **Multiple choice** is the backbone — auto-gradable, and the wrong options are a
  teaching opportunity. Make distractors *plausible*: each wrong answer should
  correspond to a specific, common mistake or misconception, so that picking it
  tells the learner something. Avoid throwaway joke options and obvious
  give-aways.
- **Numeric / short-answer** questions suit quantitative topics — the learner
  works it out and checks against the answer with its worked solution.
- **Open / derivation** questions ask the learner to reason or derive, then reveal
  a model answer they self-assess against. Use these at higher difficulties.

For each question write:

1. A clear **prompt**. Use LaTeX for any math (see the format section) — inline
   `\( ... \)` or display `\[ ... \]`.
2. A **simplified explanation** of the correct answer — the heart of the skill.
   Explain it the way a good tutor would to someone at the chosen level: plain,
   direct, building on what they know. Simplify the language, not the correctness.
3. When quantitative, a **derivation**: an ordered list of steps from first
   principles to the result, each step a short line of reasoning plus its
   equation. The HTML reveals these one block at a time so the learner can try
   before peeking.
4. One or more **citations**, each with a label and (ideally) a URL/DOI.

Calibrate depth to difficulty: at Foundational you might skip the derivation and
give an intuitive analogy; at PhD level the derivation is rigorous and the
citation is a primary source.

## Build the interactive HTML

Use the bundled template rather than hand-rolling a page each time — it already
handles MathJax rendering, answer-checking, score-keeping, progress, collapsible
derivations, and citation links, and it looks clean. **Read
`references/html-format.md` for the full build procedure and the exact `QUIZ`
data schema**, then fill the template's data block with your questions. Do not
rewrite the template's CSS/JS from scratch; you only supply the content.

The finished page should let the learner: read a question with properly rendered
equations, choose or reveal an answer, get immediate right/wrong feedback, expand
the explanation and step-through derivation, follow citation links, and see a
running score with a summary at the end. A difficulty badge sits at the top so
they know what they're taking.

## Deliver

Save the finished quiz as a single `.html` file to the skills output folder the
user prefers (per project/memory conventions), name it descriptively
(`quiz-<topic>-<difficulty>.html`), and present it to the user so they can open
it directly. Keep your closing message short — the quiz speaks for itself. Offer
to adjust difficulty, add questions, or narrow the topic as a natural follow-up.

## Flagging assumptions

If you had to make a judgement call that affects correctness — you assumed a
convention (sign, units, notation), picked one side of a genuinely debated point,
or couldn't fully verify a source — say so briefly when you hand over the quiz, so
the user can pressure-test it. Silent assumptions in a study tool propagate into
what someone learns.
