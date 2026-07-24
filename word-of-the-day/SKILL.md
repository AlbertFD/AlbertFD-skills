---
name: word-of-the-day
description: Deliver one new vocabulary word per day with its definition, how it is used, a natural example sentence, and a cited source. Rotates the theme by weekday across sophisticated English, physics/science terms, Italian, French, and GRE/academic words, and keeps a history log so a word is never repeated. Use whenever the user asks for a "word of the day", "today's word", "teach me a word", a daily vocabulary word, or wants to build vocabulary one word at a time — and pair it with a scheduled task for automatic daily delivery. Also use to catch up on a missed day or to generate a batch of words. Every definition must carry a real, verifiable citation to a reputable dictionary or authoritative source; never invent the word, its meaning, or the source.
---

# Word of the Day

## What this skill does

Delivers exactly **one** new word each time it runs, presented as a compact, readable snippet: the word, what it means, how it is actually used, a natural example, and a real citation for the definition. The point is durable vocabulary growth — one word learned properly beats ten skimmed — so each entry is small enough to absorb in under a minute but complete enough to actually use the word afterward.

It is designed to run daily (typically as a scheduled task), but works just as well on demand ("give me today's word") or in a small batch ("give me this week's words").

## Two things that make this trustworthy

**Never repeat a word.** Learning stalls if the same words keep coming back. Before choosing, read the history log and exclude everything already delivered. After choosing, append the new word to the log. Default history path:

```
/Users/albertforsyth/Documents/Claude/Projects/Skill Maker/word-of-the-day-history.md
```

Create it if it does not exist. Each appended line: `- YYYY-MM-DD (theme): WORD`. If the user runs this in a different folder, use a `word-of-the-day-history.md` in the working directory instead.

**Always cite the definition.** A vocabulary tool is only as good as its accuracy, and a confidently wrong definition teaches the wrong thing. Every entry must link the definition to a reputable source the user can check — a major dictionary (Merriam-Webster, Oxford/Lexico, Cambridge, Collins, Treccani for Italian, Larousse for French, Wiktionary as a fallback) or, for technical terms, an authoritative reference (a textbook, standards body, or peer-reviewed source). Search the web to confirm the word exists and means what you say before presenting it. Never fabricate a word, a meaning, or a citation. If you cannot verify a candidate, pick a different word.

## Theme rotation

Vary the theme by weekday so vocabulary stays broad. Get the weekday with `date +%A` and pick:

- **Monday** — sophisticated / advanced English
- **Tuesday** — physics or science term (atomic, particle, antimatter — tuned to a CERN physicist)
- **Wednesday** — Italian (a useful everyday word; handy near Geneva/CERN)
- **Thursday** — GRE / academic word common in papers
- **Friday** — sophisticated / advanced English
- **Saturday** — French (a useful everyday word)
- **Sunday** — physics or science term

For non-English words, give the English meaning and, where it helps, the gender/article. If the user asks for a specific theme, honor that over the rotation.

## Output format

Keep it tight — no preamble, no filler, just the word and its breakdown. Use this structure:

**[WORD]** /pronunciation/ · *part of speech* — (for non-English words, add the English gloss)

- **Definition:** one clear sentence.
- **How it's used:** one sentence on register, nuance, or when to reach for it — the thing a dictionary alone won't tell you.
- **Example:** one natural sentence showing the word in use.
- **More:** optional — a short etymology note or an easily-confused relative.
- **Source:** [Dictionary/reference name](URL)

**Example (English):**

**Perspicacious** /ˌpɜːspɪˈkeɪʃəs/ · *adjective*

- **Definition:** Having a keen understanding and quick, accurate judgment.
- **How it's used:** A formal compliment for sharp insight — natural in writing about someone's judgment, stilted in casual speech.
- **Example:** "Her perspicacious reading of the data caught the systematic error everyone else missed."
- **More:** From Latin *perspicax* (sharp-sighted). Don't confuse it with *perspicuous*, which means clear or easy to understand.
- **Source:** [Merriam-Webster](https://www.merriam-webster.com/dictionary/perspicacious)

**Example (physics):**

**Adiabatic** /ˌædiəˈbætɪk/ · *adjective*

- **Definition:** Describing a process in which no heat is exchanged with the surroundings.
- **How it's used:** Central in thermodynamics and quantum mechanics — an "adiabatic" change is slow enough that a system stays in its instantaneous eigenstate (the adiabatic theorem), distinct from "isothermal".
- **Example:** "The gas cooled on adiabatic expansion because it did work without drawing in heat."
- **More:** From Greek *adiábatos*, "not passable" (to heat).
- **Source:** [Britannica](https://www.britannica.com/science/adiabatic-process)

## Running it daily

If the user wants this automatically, set up a scheduled task that runs this skill's logic each morning. A cron of `0 8 * * *` delivers it at 8 AM local time. The scheduled prompt should be self-contained: restate the rotation, the no-repeat history rule, the citation requirement, and the output format above, since each scheduled run starts fresh with no memory of prior conversations.

## Batch mode

If asked for several words at once (e.g. "this week's words"), produce one entry per requested day following the rotation, each with its own citation, and log all of them to the history file. Keep each entry in the same compact format.
