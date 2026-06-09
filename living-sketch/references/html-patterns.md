# Living Sketch — HTML patterns toolbox

Assemble the visual from these tested parts instead of reinventing them. Everything here is self-contained: inline CSS + inline JS, CDN only for MathJax / Chart.js. Copy a pattern, then adapt the content. Keep the file openable at every checkpoint.

## Table of contents

1. Page scaffold + CSS design system
2. SVG diagram primitives (boxes, arrows, levels, cross-sections)
3. Hover-reveal labels
4. Staged build-up (play / step controls)
5. Step-through narration
6. Pan & zoom
7. MathJax equations
8. Chart.js (only when the point is data)
9. Print / static-export friendliness
10. Picking a palette

---

## 1. Page scaffold + CSS design system

Drive every color from the `:root` variables so the palette is consistent and easy to reroll. Swap the four accent hues to restyle the whole page.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>__TITLE__</title>
<style>
  :root{
    --bg:#0f1117; --panel:#171a23; --ink:#e8eaf0; --muted:#9aa3b2;
    --line:#2a2f3a;
    --a1:#5b8cff;   /* primary accent */
    --a2:#37d4a7;   /* secondary     */
    --a3:#ffb454;   /* highlight     */
    --a4:#ff6b8a;   /* alert / focus */
    --radius:14px; --gap:18px;
    --maxw:980px;
    font-synthesis:none;
  }
  /* Light medium (paper figure / projector): override these on <body class="light"> */
  body.light{--bg:#ffffff;--panel:#f5f7fa;--ink:#10131a;--muted:#5a6473;--line:#dfe4ec;}
  *{box-sizing:border-box}
  body{margin:0;background:var(--bg);color:var(--ink);
    font:16px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;}
  .wrap{max-width:var(--maxw);margin:0 auto;padding:28px 20px 60px;}
  h1{font-size:clamp(22px,3.4vw,34px);margin:0 0 4px;letter-spacing:-.01em}
  .sub{color:var(--muted);margin:0 0 22px}
  .stage{background:var(--panel);border:1px solid var(--line);border-radius:var(--radius);
    padding:18px;position:relative;overflow:hidden}
  .takeaway{border-left:4px solid var(--a3);background:color-mix(in srgb,var(--a3) 12%,transparent);
    padding:12px 16px;border-radius:8px;margin:18px 0;font-weight:600}
  .controls{display:flex;gap:10px;flex-wrap:wrap;align-items:center;margin:16px 0}
  button{background:var(--a1);color:#fff;border:0;border-radius:10px;padding:9px 16px;
    font:inherit;font-weight:600;cursor:pointer}
  button.ghost{background:transparent;color:var(--ink);border:1px solid var(--line)}
  button:disabled{opacity:.45;cursor:default}
  .legend{display:flex;gap:16px;flex-wrap:wrap;color:var(--muted);font-size:14px;margin-top:14px}
  .legend span{display:inline-flex;align-items:center;gap:6px}
  .dot{width:12px;height:12px;border-radius:50%}
  svg{width:100%;height:auto;display:block}
  .note{color:var(--muted);font-size:13px;margin-top:10px}
  @media (max-width:600px){.wrap{padding:18px 12px 48px}}
</style>
</head>
<body>
  <div class="wrap">
    <h1>__TITLE__</h1>
    <p class="sub">__ONE_LINE_FRAMING__</p>
    <div class="takeaway">__KEY_TAKEAWAY__</div>
    <div class="stage" id="stage"><!-- SVG / chart goes here --></div>
    <div class="controls"><!-- play / step buttons --></div>
    <p class="note">__SOURCE_OR_ASSUMPTIONS_NOTE__</p>
  </div>
<script>
/* interaction logic here */
</script>
</body>
</html>
```

Note: one stray non-ASCII character can silently break CSS or JS — type variable names cleanly and `node --check` the script block before delivering.

## 2. SVG diagram primitives

Author diagrams as inline SVG — crisp, labelable, animatable. Define reusable markers once.

```html
<svg viewBox="0 0 800 420" role="img" aria-label="__DESCRIPTION__">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-end">
      <path d="M0 0 L10 5 L0 10 z" fill="currentColor"/>
    </marker>
  </defs>

  <!-- a labelled box -->
  <g class="node" style="color:var(--a1)">
    <rect x="40" y="60" width="170" height="80" rx="12" fill="color-mix(in srgb,var(--a1) 18%,transparent)" stroke="currentColor" stroke-width="2"/>
    <text x="125" y="105" text-anchor="middle" fill="var(--ink)" font-size="16" font-weight="600">Stage A</text>
  </g>

  <!-- a connecting arrow -->
  <line x1="210" y1="100" x2="330" y2="100" stroke="var(--muted)" stroke-width="2.5" marker-end="url(#arrow)"/>

  <!-- an energy level / horizontal rule with label -->
  <line x1="500" y1="140" x2="740" y2="140" stroke="var(--a2)" stroke-width="3"/>
  <text x="500" y="132" fill="var(--muted)" font-size="13">n = 2</text>
</svg>
```

Useful layouts: left→right pipeline (boxes + arrows), top-down tree, energy-level ladder (stacked horizontal lines), cross-section (nested shapes with leader lines to side labels), state machine (circles + curved arrows with `marker-end`), network (nodes + lines). Use leader lines (`<line>` + `<text>`) to label without crowding the figure.

## 3. Hover-reveal labels

Let the viewer ask "what's this?" exactly when they wonder. Pure CSS for hover; add focus for keyboard/touch.

```html
<g class="hot" tabindex="0">
  <rect .../>
  <text ...>Stage A</text>
  <g class="pop"><rect x="40" y="150" width="220" height="56" rx="8" fill="var(--panel)" stroke="var(--line)"/>
    <text x="52" y="172" fill="var(--ink)" font-size="13">What it does, in one line.</text></g>
</g>
<style>
  .pop{opacity:0;transform:translateY(4px);transition:.18s;pointer-events:none}
  .hot:hover .pop,.hot:focus .pop{opacity:1;transform:none}
  .hot{cursor:help}
</style>
```

## 4. Staged build-up (play / step controls)

Reveal elements in causal order so the viewer sees *why* before *what's next*. Give each element a `data-step`, then show them in sequence.

```html
<div class="controls">
  <button id="play">▶ Build it up</button>
  <button class="ghost" id="reset">Reset</button>
  <span class="note" id="caption"></span>
</div>
<script>
  const steps = [...document.querySelectorAll('[data-step]')]
    .sort((a,b)=>a.dataset.step-b.dataset.step);
  const captions = ["First, the input arrives.","It's transformed here.","And out comes the result."];
  steps.forEach(el=>{el.style.opacity=0;el.style.transition='opacity .4s';});
  let i=0, timer=null;
  function show(n){steps.forEach((el,k)=>el.style.opacity = k<=n?1:0);
    document.getElementById('caption').textContent = captions[n]||'';}
  function reset(){i=0;steps.forEach(el=>el.style.opacity=0);document.getElementById('caption').textContent='';}
  document.getElementById('play').onclick=()=>{clearInterval(timer);reset();
    timer=setInterval(()=>{show(i);if(i++>=steps.length-1)clearInterval(timer);},900);};
  document.getElementById('reset').onclick=()=>{clearInterval(timer);reset();};
</script>
```

For a more controlled feel, replace auto-play with Prev/Next buttons driving the same `show(n)`.

## 5. Step-through narration

When the logic is a sequence of moves, pair each step with a sentence so the diagram and the words advance together. Same mechanism as §4 but user-driven, with a step counter ("Step 2 of 5") and the caption doing the teaching. This is the best pattern for "explain how X works one move at a time."

## 6. Pan & zoom

For dense or large diagrams (especially cross-sections / maps). Lightweight, no library:

```js
const svg = document.querySelector('svg');
let vb = svg.viewBox.baseVal, scale=1, ox=0, oy=0, drag=null;
svg.addEventListener('wheel', e=>{e.preventDefault();
  const f = e.deltaY<0?0.9:1.1; vb.width*=f; vb.height*=f;}, {passive:false});
svg.addEventListener('pointerdown', e=>drag={x:e.clientX,y:e.clientY});
addEventListener('pointerup',()=>drag=null);
addEventListener('pointermove', e=>{if(!drag)return;
  const k=vb.width/svg.clientWidth;
  vb.x-=(e.clientX-drag.x)*k; vb.y-=(e.clientY-drag.y)*k; drag={x:e.clientX,y:e.clientY};});
```

Only add pan/zoom when the figure genuinely needs it; for a slide it's usually clutter.

## 7. MathJax equations

Use when real notation carries meaning (calibrate to depth — newcomers rarely need it).

```html
<script>MathJax={tex:{inlineMath:[['\\(','\\)']],displayMath:[['\\[','\\]']]}};</script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.2/es5/tex-svg.js" id="MathJax-script" async></script>
```

Write `\( E_n = -\tfrac{R}{n^2} \)` inline. After dynamically revealing any element containing math, call `MathJax.typesetPromise()`. For an expert audience, break a key equation down term-by-term with small labelled cards.

## 8. Chart.js (only when the point is data)

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.min.js"></script>
<canvas id="c" height="120"></canvas>
<script>
  new Chart(document.getElementById('c'), {type:'line',
    data:{labels:[...], datasets:[{label:'…',data:[...],
      borderColor:getComputedStyle(document.documentElement).getPropertyValue('--a1')}]},
    options:{scales:{y:{title:{display:true,text:'units'}},x:{title:{display:true,text:'units'}}}}});
</script>
```

Honesty rule: plot real quoted values exactly; if you're sketching the shape of a curve between known points, label it "schematic" in the caption. Never present invented data as real. Match axis ranges/units to any source figure.

## 9. Print / static-export friendliness

For the "paper figure" medium, the visual must survive being static. SVG already exports cleanly. Add:

```css
@media print{ .controls{display:none} body{background:#fff;color:#000} }
```

Default any animated/staged elements to their *fully revealed* state on load (then let the play button re-run), so a screenshot or print captures the complete figure, not a blank first frame. Offer a `<body class="light">` toggle for projector/print contrast.

## 10. Picking a palette

Choose a palette that fits the subject and the medium, and keep two diagrams from looking identical. Set the four `--a1..--a4` accents in `:root`; everything inherits. Dark canvas (`--bg:#0f1117`) reads well on screen and projectors; light (`body.light`) for print. Keep accents distinct in hue and high-contrast against the chosen background; avoid red/green as the *only* distinction (color-blind safety). A quick recipe: pick one anchor hue, then take accents at roughly +150°, +40°, and +320° around the wheel for a balanced, legible set.
