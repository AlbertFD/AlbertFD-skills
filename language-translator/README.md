# language-translator

Detects the source language of any text and translates it to a target language, treating **fidelity to the original over fluency** as the top priority.

## What it produces

- Source and target language stated up front, plus a **technical/academic mode** flag when the text is scientific, academic, or jargon-heavy
- Original and translation shown **side-by-side, segment by segment** — so you can check fidelity at a glance rather than trusting a black-box output
- **Notes** flagging anything that needed a judgment call: idioms, ambiguous phrases, hedged claims that shouldn't be upgraded to confident ones, or uncertain/illegible source text
- **Terminology citations** for technical terms whose translation isn't a straightforward 1:1 mapping (e.g. "per CERN/HEP field convention") — never a fabricated source
- A **key vocabulary** table pulling out 5–15 reusable, non-obvious words or phrases from the text, paired 1:1 with their translation, so you pick up vocabulary rather than just getting an answer

## When it triggers

"Translate this to Spanish", "what does this German paragraph say in English", "convert this to Japanese", "put this abstract into French for a submission" — anything asking to translate, convert between languages, or explain what foreign-language text says, even without the word "translate."

## Core principle

A translation that reads beautifully but drifts from the original's meaning, hedging, or ambiguity is a failure. The skill doesn't summarize, resolve ambiguity that exists in the source, or silently swap in a same-vibe idiom without flagging that a substitution happened.

## Files

- `SKILL.md` — workflow, output format, and the faithfulness/technical-mode/vocabulary rules
- `evals/evals.json` — test prompts (casual text, a technical/academic passage, an idiom)

Output stays in the chat — no file is created unless you ask for one.
