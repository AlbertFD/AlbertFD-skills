---
name: language-translator
description: Detects the source language of any text and translates it to a target language while staying faithful to the original meaning, tone, and register. Automatically switches into a technical/academic precision mode for scientific, academic, or jargon-heavy text (research abstracts, papers, technical documentation), preserving specialized terminology and flagging translation choices with citations to the terminology source used. Outputs original and translated text side-by-side so fidelity can be checked at a glance. Use this skill whenever the user asks to translate text, convert something to another language, wants a "language converter," pastes foreign-language text and asks what it says, needs a translation of a paper abstract or technical passage, or references translating a document, email, or quote into another language — even if they don't use the word "translate" explicitly (e.g. "what does this German paragraph mean in English", "convert this to Japanese", "put this abstract into French for a submission").
---

# Language Translator

## What this skill does

Translates text between languages while treating fidelity to the source as the top priority — the goal is a translation the original author would recognize as accurate, not a paraphrase or a summary. It detects the source language automatically, confirms the target language, and adapts its approach depending on whether the text is everyday language or technical/academic writing.

## Workflow

1. **Detect the source language.** State it explicitly (e.g., "Source: German").
2. **Confirm the target language.** If the user names it, use it. If it's ambiguous or missing (they just paste text with no instructions), ask before translating rather than guessing.
3. **Assess the register.** Decide whether the text is general/conversational or technical/academic (scientific terminology, equations, citations, discipline-specific jargon, formal academic prose). This determines which mode below applies. When in doubt, default to technical mode — it's the more conservative choice, and a general reader loses nothing from precise terminology.
4. **Translate.**
5. **Output** in the parallel format below.
6. **Flag anything that needed a judgment call** — ambiguous phrases, idioms without a direct equivalent, terms with more than one accepted translation, or source text that's unclear or garbled.

## Principle: faithfulness over fluency

A translation that reads beautifully but drifts from the original's meaning, hedging, or ambiguity is a failure, not a success. Concretely:

- Preserve the original's level of certainty or hedging. If the source says "possibly" or "preliminary," don't upgrade it to a confident claim in translation.
- Don't resolve ambiguity that exists in the source. If a phrase is genuinely ambiguous in the original language, say so rather than silently picking one reading.
- Don't summarize, trim, or "clean up" the original — translate what's there, including awkward phrasing, repetition, or informality if that's how the source reads.
- Idioms and culturally specific expressions rarely have exact equivalents. Translate the meaning and flag it as an idiom rather than silently substituting a same-vibe idiom in the target language — the reader should know a substitution happened.
- If part of the source text is illegible, garbled (e.g., bad OCR), or you're not confident in a phrase, say so explicitly rather than guessing and presenting it as certain.

## Technical / academic mode

Triggered by: scientific or field-specific terminology, equations/formulas, citations, research-paper structure (abstract, methods, results), or formal academic register.

- Keep terminology consistent throughout — don't translate the same term two different ways in one passage.
- For terms with a standard translation in the field, use it. Where the choice isn't obvious or the term has more than one accepted rendering, add a short note citing the source you used to decide (a bilingual glossary, a standard textbook translation, a field convention) — see Citation format below.
- Don't invent a translation for a term of art. If you're not confident a standard target-language term exists, say so and offer the closest gloss with a note that it may not be the field's established usage.
- Preserve equations, units, and symbols unchanged — these aren't language-dependent.

## Output format

Always use this structure for the reply (adapt lightly for very short texts like a single sentence — the segment-by-segment breakdown can collapse to one pair):

```
**Source language:** [detected language]
**Target language:** [target]

[If technical/academic content detected: **Mode: technical** — one-line note on why]

---

**Original:** [segment 1 of source text]
**Translation:** [segment 1 translated]

**Original:** [segment 2 of source text]
**Translation:** [segment 2 translated]

[... continue in logical segments — sentence-by-sentence for short text, paragraph-by-paragraph for longer text]

---

**Notes:**
- [Any flagged idioms, ambiguous phrases, terminology choices with citation, or uncertain/illegible source text — omit this section only if there's genuinely nothing to flag]

**Key vocabulary:**
| Original | Translation | Notes |
|---|---|---|
| [word/phrase] | [word/phrase] | [optional: part of speech, register, or usage note] |
```

Keep the reply in the chat — don't create a file unless the user explicitly asks for one.

## Key vocabulary

Beyond the raw translation, the person on the other end is often trying to build up their own working vocabulary in the source language — not just get an answer. Treat every translation as a small language lesson: pull out a short list of words or phrases worth remembering, paired 1:1 with their translation (a clean word-to-word or phrase-to-phrase map, not a paragraph of explanation).

Pick words for:
- **Reusability** — words that will come up again in other contexts, not one-off proper nouns or place names.
- **Non-obviousness** — skip near-identical cognates that need no explanation (e.g. "información" → "information"); favor words a learner wouldn't guess correctly.
- **Idioms and set phrases** — these are usually the highest-value entries, since they can't be worked out word-by-word.
- **Field-specific terms** — in technical mode, this list can double up with the terminology citations above, but keep the vocabulary table focused on the word itself (citations stay in Notes).

Aim for roughly 5-15 entries depending on text length — a single sentence might only yield 1-3 genuinely useful words; don't pad the list with filler just to hit a number. Skip this section entirely only for trivial inputs (e.g. translating a single common word) where there's nothing worth teaching.

## Handling long documents

For a full paper, long email thread, or multi-page document, don't try to translate everything into one giant reply. Translate the first logical chunk (e.g., the abstract, or the first section), then ask whether the user wants you to continue with the rest. This keeps quality high and avoids losing terminology consistency partway through a huge block.

## Citation format for terminology

When a technical term's translation isn't a straightforward 1:1 mapping, cite where the choice came from:

`**[term]** → **[translation]** — per [source: e.g., "IUPAC nomenclature," "standard German physics usage (field convention)," "CERN glossary," a named bilingual dictionary]`

Never invent a citation. If the choice is based on general knowledge of the field rather than a specific reference, say that plainly ("standard usage in the field, no single canonical source") rather than fabricating a source name.

## What not to do

- Don't fabricate a translation for text you can't actually read (bad handwriting, corrupted file, unsupported script) — say so instead.
- Don't silently drop footnotes, citations, or references embedded in the source text — translate them, or note they were left as-is if untranslatable (e.g., a citation key).
- Don't add commentary, opinions, or corrections into the translation itself. If the source contains an apparent error, translate it faithfully and flag the error separately in Notes — don't silently fix it.

## Example

Input: "Translate to English: 'Der Wirkungsquerschnitt wurde bei einer Schwerpunktsenergie von 13 TeV gemessen, was auf eine mögliche Resonanz hindeuten könnte.'"

Output:

```
**Source language:** German
**Target language:** English
**Mode: technical** — contains particle-physics terminology (Wirkungsquerschnitt, Schwerpunktsenergie)

---

**Original:** Der Wirkungsquerschnitt wurde bei einer Schwerpunktsenergie von 13 TeV gemessen, was auf eine mögliche Resonanz hindeuten könnte.
**Translation:** The cross section was measured at a center-of-mass energy of 13 TeV, which could point to a possible resonance.

**Notes:**
- "hindeuten könnte" (could point to / might suggest) is hedged in the original — kept as "could point to" rather than upgraded to a firm claim.
- **Wirkungsquerschnitt** → **cross section** — standard particle-physics term (CERN/HEP field convention).
- **Schwerpunktsenergie** → **center-of-mass energy** — standard particle-physics term (CERN/HEP field convention).

**Key vocabulary:**
| Original | Translation | Notes |
|---|---|---|
| der Wirkungsquerschnitt | the cross section | noun, physics term |
| die Schwerpunktsenergie | the center-of-mass energy | noun, compound word (Schwerpunkt = center of mass + Energie) |
| hindeuten auf | to point to / suggest | hedging phrase, common in scientific writing |
| die Resonanz | the resonance | noun, near-cognate but worth noting for physics contexts |
```
