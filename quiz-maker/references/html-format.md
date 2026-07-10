# Building the quiz HTML

The template `assets/quiz_template.html` is a complete, self-contained interactive
quiz. It already implements MathJax rendering, multiple-choice checking, numeric
and open (self-graded) questions, collapsible explanations and step-by-step
derivations, citation links, a progress bar, live scoring, and an end summary. You
supply only the content.

## How to build

1. Copy `assets/quiz_template.html` to your output path.
2. Replace the single placeholder `/*__QUIZ_DATA__*/` with a JavaScript object
   literal assigned to `QUIZ` (see schema below). That is the only edit required.
3. Do not touch the CSS or the logic unless the user asks for a visual change.
   Everything the learner needs is driven by the `QUIZ` object.

You can build the file however is convenient — Python string replace, a heredoc,
or the Edit tool. Just make sure the final file is valid HTML with the data block
filled in. Open it once (or read it back) to sanity-check there are no unescaped
characters breaking the script.

## The `QUIZ` schema

```js
const QUIZ = {
  topic: "Special Relativity — Time Dilation & Length Contraction",
  difficulty: "Advanced",          // exact label from the five levels
  intro: "Optional one-line framing shown under the title.",
  questions: [
    {
      type: "mcq",                 // "mcq" | "numeric" | "open"
      prompt: "A muon travels at \\(0.99c\\). By what factor is its lifetime dilated in the lab frame?",
      options: [                   // mcq only
        "\\(\\gamma \\approx 1.4\\)",
        "\\(\\gamma \\approx 7.1\\)",
        "\\(\\gamma \\approx 0.14\\)",
        "No dilation — lifetime is invariant"
      ],
      answer: 1,                   // mcq: 0-based index of correct option
      explanation: "The Lorentz factor \\(\\gamma = 1/\\sqrt{1-\\beta^2}\\). With \\(\\beta = 0.99\\), \\(\\gamma \\approx 7.1\\), so the lab sees the muon live ~7x longer. Option C inverts the factor — a common slip; \\(\\gamma\\) is always \\(\\ge 1\\).",
      derivation: [                // optional; omit or [] if not quantitative
        "Start from the Lorentz factor: \\(\\gamma = \\dfrac{1}{\\sqrt{1-\\beta^2}}\\).",
        "Insert \\(\\beta = v/c = 0.99\\): \\(\\gamma = \\dfrac{1}{\\sqrt{1-0.9801}}\\).",
        "\\(\\sqrt{0.0199} \\approx 0.141\\), so \\(\\gamma \\approx 7.09\\)."
      ],
      citations: [
        { label: "Griffiths, Introduction to Electrodynamics, 4th ed., §12.1", url: "" },
        { label: "Particle Data Group, Kinematics review", url: "https://pdg.lbl.gov/" }
      ]
    },

    {
      type: "numeric",
      prompt: "Compute \\(\\gamma\\) for \\(\\beta = 0.6\\). Give it to two decimal places.",
      answer: 1.25,                // numeric: the accepted value
      tolerance: 0.02,             // optional; absolute tolerance, default 0.01
      explanation: "\\(\\gamma = 1/\\sqrt{1-0.36} = 1/\\sqrt{0.64} = 1/0.8 = 1.25\\).",
      derivation: [
        "\\(\\beta^2 = 0.36\\), so \\(1-\\beta^2 = 0.64\\).",
        "\\(\\sqrt{0.64} = 0.8\\); invert to get \\(\\gamma = 1.25\\)."
      ],
      citations: [ { label: "Standard result — any SR text", url: "" } ]
    },

    {
      type: "open",
      prompt: "Explain why length contraction and time dilation are consistent for the muon — i.e. why both frames agree the muon reaches the ground.",
      modelAnswer: "In the muon's frame its lifetime is normal but the atmosphere is length-contracted, so the distance is short enough to cross. In the lab frame the distance is full but the muon's clock runs slow, so it survives long enough. Same outcome, different bookkeeping.",
      citations: [ { label: "Taylor & Wheeler, Spacetime Physics, 2nd ed., Ch. 4", url: "" } ]
    }
  ]
};
```

### Field notes

- **type** decides the interaction. `mcq` needs `options` + `answer` (index).
  `numeric` needs `answer` (number) and optional `tolerance`. `open` needs
  `modelAnswer` (a string revealed for self-assessment; there is no auto-grade —
  the learner marks themselves correct/incorrect).
- **prompt / options / explanation / derivation / modelAnswer** may all contain
  LaTeX. Use `\\( ... \\)` for inline and `\\[ ... \\]` for display math — note
  the doubled backslashes because it's inside a JS string. MathJax renders them.
- **derivation** is an array of strings, each a reasoning step with its equation.
  The template reveals them progressively ("Show next step"). Omit for
  non-quantitative questions.
- **citations** is an array of `{ label, url }`. `url` may be empty for a pure
  textbook reference; if present the label becomes a link. Always give a specific,
  real label — never invent page numbers or DOIs.

## Escaping gotchas

Because the data lives inside a `<script>` in an HTML file:

- Write LaTeX backslashes as `\\` (e.g. `\\gamma`, `\\sqrt`, `\\dfrac`).
- Avoid a literal `</script>` inside any string.
- Keep strings quoted consistently; if a string contains a quote, escape it or use
  the other quote style.

After writing, verify the page renders (equations typeset, buttons work) before
handing it over.
