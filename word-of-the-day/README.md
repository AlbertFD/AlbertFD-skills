# word-of-the-day

Delivers one new vocabulary word per day — definition, how it's used, a natural example, and a **cited source** — with the theme rotating by weekday and a history log so words never repeat.

## What you get

Each run produces one compact entry:

- The word, with pronunciation and part of speech (English gloss for foreign words)
- A one-sentence definition
- A note on how it's actually used (register / nuance)
- A natural example sentence
- Optional etymology or an easily-confused relative
- A real citation to a reputable dictionary or authoritative reference

## Theme rotation

| Day | Theme |
|-----|-------|
| Mon | Sophisticated / advanced English |
| Tue | Physics / science term |
| Wed | Italian (everyday) |
| Thu | GRE / academic |
| Fri | Sophisticated / advanced English |
| Sat | French (everyday) |
| Sun | Physics / science term |

Ask for a specific theme any time to override the rotation.

## No repeats + citations

- **No repeats:** words are logged to `word-of-the-day-history.md`; already-seen words are excluded.
- **Citations:** every definition is verified against and linked to a reputable source (Merriam-Webster, Oxford, Cambridge, Treccani, Larousse, Britannica, etc.). No invented words or sources.

## Automating it

Pair with a scheduled task (e.g. cron `0 8 * * *`) to receive a word every morning. Also works on demand ("today's word") or in batch ("give me this week's words").
