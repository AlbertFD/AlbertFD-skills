---
name: code-converter
description: Translates source code from one programming language to another while preserving behavior exactly — same inputs produce the same outputs, same logic, structure, and edge-case handling. Works between any pair of languages (Python, JavaScript/TypeScript, Java, C#, C++, C, Go, Rust, Ruby, PHP, Kotlin, Swift, R, MATLAB, SQL, Bash, and more), then verifies equivalence by running tests on both versions where possible, or a rigorous line-by-line audit where not. Use whenever the user wants to port, convert, translate, rewrite, or migrate code between languages, or says things like "turn this Python into Go", "what does this Rust look like in TypeScript", "port my script to C++", "rewrite this function in Java", "convert this file to Kotlin", or pastes code in one language and asks for it in another — even without the word "convert". Also for migrating a whole file or module, matching a codebase's language, or checking that two versions behave identically.
---

# Code Converter

## What this skill does

Ports code from a **source language** to a **target language** so that the translation is a faithful, behavior-preserving equivalent of the original — not a reimagining. The guiding standard is: *if you fed both versions the same inputs, you'd get the same outputs, including the same errors, edge-case behavior, and side effects.* Getting this right is what makes a port trustworthy; a version that "looks right" but diverges on an edge case is worse than useless, because the divergence hides until production.

This skill assumes the user wants **fidelity first**. It is not a refactoring or "make it more idiomatic at the cost of matching" tool. It does write natural, idiomatic target-language code — but idiom is in service of preserving behavior, never a reason to change it.

## Core principle: preserve behavior exactly

Everything below flows from one idea — the translated program must do what the original did. Concretely:

- **Same logic and control flow.** Loops, branches, recursion, short-circuit evaluation, and the order operations happen in should map across. If the source iterates in a specific order, so does the target.
- **Same numeric behavior.** Watch integer vs. float division, integer width and overflow, rounding, and operator precedence. `7 / 2` is `3` in C/Java/Go integer context but `3.5` in Python 3 — the translation must reproduce the original's result, not the target language's default.
- **Same edge cases and errors.** Empty inputs, nulls/None, off-by-one boundaries, division by zero, and out-of-range access should behave as they did. If the original throws on bad input, the port should too (with the target's equivalent exception).
- **Same string and collection semantics.** 0-based vs. 1-based indexing, string immutability, encoding, mutable-default-argument quirks, and how the language handles missing dictionary keys all differ — translate the *behavior*, not the syntax.
- **Same structure, where it doesn't fight the target.** Keep the same functions/methods, names, and decomposition so a reader can diff the two side by side. Preserve comments (translated if needed) and docstrings.
- **Same public interface.** Function signatures, argument order, return shapes, and names carry over unless the target language forces a change (which you then flag).

When a language feature has no direct equivalent, reproduce its *effect* using the target's idioms, and flag it (see below). Do not silently drop or approximate behavior.

## Workflow

1. **Identify source and target languages.** If the source is obvious from the code and the target is stated, proceed. If the target language is missing or ambiguous, ask before translating — don't guess. If a target framework/runtime matters (e.g. Python 2 vs 3, .NET vs Mono, ES modules vs CommonJS, a specific SQL dialect), confirm it.

2. **Read the source carefully and note behavioral hotspots** before writing anything: integer division, overflow, mutable state, concurrency, exception paths, external I/O, library calls, and anything language-specific that won't translate literally. These are where ports break.

3. **Translate**, preserving logic, structure, names, and comments. Write idiomatic target code, but never let idiom change results.

4. **Handle library/stdlib calls deliberately.** Map to the target's standard library where a clear equivalent exists (e.g. Python `json` → Go `encoding/json`). Where there's no equivalent, either implement the needed behavior inline or flag that an external dependency is required — and name it. Never invent a library function that doesn't exist.

5. **Verify equivalence** (see next section). This is not optional — it's what separates a real port from a plausible-looking one.

6. **Deliver** the translated code plus a short equivalence report: how it was verified, and every judgment call or behavioral risk the user should pressure-test.

## Verification

The user asked for behavior to match, so prove it rather than asserting it.

**Preferred — run both versions.** When both languages are runnable in this environment:

- Derive test inputs from the code: normal cases, boundaries (empty, zero, negative, max), and any branch you can reach. If the original ships with examples or tests, reuse them.
- Run the **original** on those inputs to capture ground-truth outputs (don't assume what it produces — execute it). Run the **translation** on the same inputs. Compare.
- For anything numeric, compare exactly where the original is exact, and within a stated tolerance only where the original itself is floating-point. Note the tolerance.
- If outputs differ, fix the translation and re-run. Report what the discrepancy was — it's often the most instructive part.
- Show the user the inputs tested and the matching outputs so the check is transparent, not a "trust me."

**Fallback — static equivalence audit.** When a language can't be run here (or needs libraries/hardware that aren't available), do a disciplined line-by-line comparison instead of executing:

- Walk the two versions in parallel and confirm each construct maps faithfully, paying special attention to the behavioral hotspots from step 2.
- Hand-trace a few representative inputs (including edge cases) through both versions and confirm they'd produce the same result.
- State clearly that verification was by static analysis, not execution, and list the specific spots where you'd most want the user to run their own test — this is exactly the kind of assumption worth pressure-testing before relying on the port.

Never claim the versions are equivalent without saying *how* you checked. "Verified by running 6 inputs including empty and negative cases" and "Verified by static trace; not executed" are both fine — silently asserting equivalence is not.

## Things that commonly break a port

Keep these in view; they're the usual culprits:

- **Integer vs. float division** and integer overflow/wraparound (fixed-width ints in C/Go/Rust/Java vs. arbitrary precision in Python/Ruby).
- **Indexing and slicing** — 0- vs 1-based (R, MATLAB, Lua, SQL are 1-based), inclusive vs exclusive ranges, negative indices.
- **Truthiness** — what counts as false (`0`, `""`, `[]`, `None` vs only `false`/`null`) differs and changes which branch runs.
- **Null handling** — `None`/`nil`/`null`/`undefined` and how missing map keys behave (return default, throw, or return a zero value).
- **Mutable default arguments** (Python), pass-by-value vs pass-by-reference, and shared-reference aliasing.
- **String encoding and immutability**, character vs byte, and how `==` compares (value vs reference).
- **Map/dict iteration order** — insertion-ordered in modern Python/JS, unordered/ randomized in Go.
- **Exception vs error-return** conventions (Go/Rust return errors; Python/Java/JS throw) — preserve which conditions fail and how.
- **Concurrency and floating-point formatting** (default precision when printing) — easy to overlook, easy to diverge on.

## Output format

Structure the response like this:

1. **Header line** naming the conversion, e.g. `Python → Go`. Note the target runtime/version if it mattered.
2. **The translated code**, in a single code block, ready to drop in. If the source was multiple files, mirror that structure and label each file.
3. **Equivalence report** — one short section covering:
   - How it was verified (ran N inputs / static trace), with the inputs and matching outputs if run.
   - Any behavioral judgment calls (a construct with no direct equivalent, a library mapping, a numeric-precision choice).
   - Assumptions to pressure-test before relying on it — especially anything verified only statically, or any external dependency the port now needs.

Keep the prose tight. The user wants working, matching code and an honest account of how faithful it is — not an essay.

## When the request is bigger than a snippet

For a whole file or module: translate it in full, keep the file/function structure so the two can be diffed, and if it's large, verify the trickiest functions by running them rather than every line. For a multi-file project or build-system migration, say what's in scope, translate module by module, and be explicit about what still needs the user's environment to fully verify (external services, platform APIs, dependencies). Don't pretend a static check covers what only their environment can confirm.
