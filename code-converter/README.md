# code-converter

Ports source code from one programming language to another so the translation
**behaves exactly like the original** — same inputs produce the same outputs,
same logic, structure, edge cases, and errors. Fidelity first: it writes
idiomatic target-language code, but never lets idiom change results.

Works between any pair of languages (Python, JavaScript/TypeScript, Java, C#,
C++, C, Go, Rust, Ruby, PHP, Kotlin, Swift, R, MATLAB, SQL, Bash, and more).

## What you get

- A faithful translation that keeps the same functions, names, and comments so
  the two versions can be diffed side by side.
- Deliberate handling of the usual port-breakers: integer vs. float division,
  overflow, indexing base, truthiness, null/error conventions, and library
  mappings.
- An **equivalence report** on every port: how it was verified, any judgment
  calls, and the assumptions worth pressure-testing.

## Verification

Every conversion ends with a proof, not an assertion:

- **Runnable languages** — both versions are executed on inputs derived from the
  code (normal, boundary, and edge cases) and their outputs compared. The tested
  inputs and matching outputs are shown.
- **Non-runnable here** — a disciplined line-by-line static audit plus a
  hand-trace of representative inputs, clearly labelled as not executed, with the
  spots most worth testing in your own environment called out.

## Files

- `SKILL.md` — the skill: core principle, workflow, port-breaker checklist, and
  the verification policy.
- `evals/evals.json` — test prompts (Python→Go, JS→Python, Java→C++).

## Usage

Trigger it by asking to port, convert, translate, rewrite, or migrate code
between languages — e.g. "turn this Python into Go", "port my script to C++", or
just by pasting code and asking for it in another language. The skill confirms
the target language (and runtime, if it matters), translates, verifies, and
returns the code plus an equivalence report.
