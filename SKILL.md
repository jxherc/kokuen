---
name: kokuen
description: >-
  Apply kokuen (黒鉛), jxherc's house web UI style, pulled from jxherc/website and alles.
  Greyscale near-black base (warm bone-white in light mode), Inter + JetBrains Mono, tiny text,
  1–4px radii, the cubic-bezier(0.2,0.7,0.2,1) easing, inverted text selection, staggered "rise"
  entrances, and hand-built (never native) controls. One optional colour sits on the grey: --accent
  for interaction, with --signal for status (right/live/updated) when it differs. Use this whenever
  building or restyling any web page, app, or component for jxherc, or when they say "my style",
  "the usual look", "kokuen", "黒鉛", or "match my site / alles".
---

# kokuen (黒鉛)

The look I put on basically everything. Near-black, greyscale, square corners, small type, quiet
until you touch it. Tokens lifted from [jxherc/website](https://github.com/jxherc/website) and `alles`
so building against them matches without redoing the CSS.

黒鉛 = graphite. Greys do the work. One optional colour, used only when it carries information.

This file is the model and the rules. `reference.md` is the full component catalog with exact values.
`kokuen.css` is the drop-in.

## the colour model

**The greys are fixed.** A four-step ramp plus a panel shade. This is the actual aesthetic:

```
--bg #0a0a0a   --text #e8e6e3   --muted #6e6e6e   --faint #2e2e2e   --panel #0e0e0e
```

paper, ink, pencil, ghost. Most of any screen is built from just these. If you can do something in
grey, do it in grey.

**One optional colour goes on top, used sparingly.** It does one of two jobs:

- interaction (`--accent`): active/selected states, focus glow, a primary button, a checked box, a
  name in a greeting, the logo.
- status (`--signal`): a live dot, the winning bar, a "done" tick, freshly-changed data.

`--signal` defaults to `--accent`, so one colour can do both. Split them when status should be a
different hue. Set `--accent: var(--text)` to drop the interaction hue and stay grey except for status.

| | accent | signal | result |
|---|---|---|---|
| **alles** | purple `#818cf8` | inherits accent | one purple does interaction + status |
| **my site** | `var(--text)` (none) | green `#00ff2a` | greys, green only marks state: live dot, winner bar, pace arrow |

## quickstart

```html
<link rel="stylesheet" href="kokuen.css">
```
```css
:root{
  --accent:#818cf8;    /* the optional colour. or var(--text) for none */
  --signal:#00ff2a;    /* status hue. drop this line and it copies the accent */
}
```
```html
<button class="btn">save</button>
<span class="live-dot"></span>
<div class="switch on" aria-checked="true"></div>
<a class="ul" href="#">a link</a>
```

No build step, no dependencies. Everything is a class you can read in `kokuen.css`.

## the rules

The stuff that actually makes it read as mine. Break these and it stops looking right.

1. **Grey first, colour only when it means something.** The default for any element is greyscale.
   Reach for accent or signal and you should have a reason (it's interactive/branded, or it's
   reporting state). A screen with no colour at all is normal and fine.

2. **Two type families.** Inter for words and UI, JetBrains Mono for anything machine-shaped: code,
   IDs, timestamps, token counts, file paths, raw numbers you want monospaced. Keep
   `font-feature-settings:'cv11','ss01','ss03'` on the root, it's part of the look.

3. **Letter-spacing splits two ways.** Prose and headings go tight (negative, −0.005 to −0.025em).
   Labels, buttons, captions, meta go wide *and* lowercase (positive, +0.04 to +0.08em,
   `text-transform:lowercase`). This split is the single biggest tell of the style. Get it right and
   half the work is done.

4. **Small.** UI text lives between 0.6 and 0.9rem. A 0.7rem label is normal. The big display header
   tops out around 1.9rem and usually drops to weight 300. If a size feels like a "normal website",
   it's too big here.

5. **Barely-rounded.** `border-radius` is 1–4px, default 2–3px. The only actual pill in the system is
   a toggle switch. No soft rounded cards, no big pill buttons.

6. **Borders are 1px `--faint`, and they wake up on hover** (to `--muted`). Surfaces are flat. The
   only shadow anywhere is the little one under a toggle knob and the focus glow. No drop shadows on
   cards.

7. **One easing.** `cubic-bezier(0.2,0.7,0.2,1)` for transforms and entrances. Plain `ease` at
   0.12–0.3s for colour/border fades. Don't introduce other curves.

8. **`tabular-nums` on numbers** that tick, rank, or line up in a column. Clocks, timers, counts, stats.

9. **Never ship a native control.** Browser checkbox, radio, select, range, scrollbar: all replaced.
   Recipes are in `reference.md`. A default widget instantly breaks it.

## tokens

```css
:root{
  --bg:#0a0a0a; --text:#e8e6e3; --muted:#6e6e6e; --faint:#2e2e2e; --panel:#0e0e0e;
  --accent:#818cf8;            /* the optional colour. var(--text) = none */
  --signal:var(--accent);      /* status hue. override for a separate one */
  --error:#f87171; --green:#4ade80;
  --ease:cubic-bezier(0.2,0.7,0.2,1);
}
[data-theme="light"]{
  --bg:#f5f4f1; --text:#111111; --muted:#888888; --faint:#d4d2ce; --panel:#efede9;
}
```

Light mode is warm paper (`#f5f4f1`), not white. Keep it warm, don't "correct" it to `#fff`.

## the accent tint scale (how interaction states are built)

When the accent tints a background (hover, active, selected) it's done with `color-mix`, low
percentages, so it stays subtle on the dark. These are the actual values from alles, use them:

- hover surface: `color-mix(in srgb, var(--accent) 6–8%, transparent)`
- active / selected row: `12–14%`
- stronger active (tabs, mode buttons): `16–18%`
- tinted border: `40–45%` mixed with transparent, or `55%` mixed with `--faint`
- focus glow: `box-shadow: 0 0 0 1px var(--accent), 0 0 16px color-mix(in srgb, var(--accent) 25%, transparent)`
- hard selection (a calendar day): solid `var(--accent)` fill, `var(--bg)` text. inverted, not tinted.

## type scale

Rough ladder in rem, smallest to biggest. You won't need them all on one screen.

`0.6` micro meta · `0.62–0.66` captions/stamps · `0.68–0.72` labels + buttons · `0.78–0.82` list rows ·
`0.875` body-small / kv / textarea · `0.95–1.06` intro/prose · `1.15` card heading · `1.9` page display.

Weights: 400 body, 500 for labels/brand/emphasis, 300 for the big thin display, 600 only for one loud
number. That's the whole range, don't add more.

## motion

- transforms + entrances: `cubic-bezier(0.2,0.7,0.2,1)`. fades: plain `ease`.
- durations: 0.12–0.18s micro (hover colour, knob slide), 0.2–0.3s standard (borders, dialogs),
  0.5–0.7s entrances + bar fills, 1s long fills.
- the vocabulary: lift `translateY(-2px)`, arrow nudge `translate(3px,-3px)`, underline `scaleX(0→1)`,
  thumbnail `scale(1.04)` + `brightness(0.7)`, slider thumb `scale(1.18)`.
- keyframes that exist: `rise` (up+in, the page entrance), `fade-in`, `live-pulse` (the dot),
  `blink` (stream cursor), `name-flash` (accent→text), `shimmer` (skeleton).
- pages arrive with `.rise` on the container: kids start at opacity 0 / translateY(6px) and come in
  staggered ~0.07s apart. always pair with the reduced-motion block (it's in the CSS).

## the controls (all hand-built)

Each replaces a native element. Markup + behaviour:

- **switch** `.switch`: 34×20 pill, 16px white knob, slides + track turns accent when on. It's a
  `<div>`, toggle `.on` / `aria-checked` in JS on click.
- **checkbox** `.chk`: 15px box, accent fill + CSS tick when checked. `role="checkbox" aria-checked`.
- **slider** `.slider`: restyled `<input type=range>`, `appearance:none`, 4px track, round accent thumb.
- **select**: don't use `<select>`. Build a `.btn`-style trigger that opens a panel of rows; rows
  hover to panel/text, selected row gets a tick or accent text. Close on outside-click / Esc.
- **scrollbar**: already global (3px). Don't override it back.

Accessibility: these are divs, so add the roles (`role="checkbox"`, `aria-checked`, `tabindex="0"`)
and handle keyboard (space/enter to toggle, arrows for sliders). Focus styling is already global
(`:focus-visible` → muted outline). Don't drop the a11y just because it's custom.

## how to actually apply it

- **New page/app:** start from `kokuen.css`, set `--accent` (or `var(--text)` for none) and `--signal`,
  build with the classes. Read `reference.md` when you need a component you don't see.
- **Restyling something:** pull the tokens block and the rules. Then go kill everything that fights
  them: rounded corners over 4px, native controls, drop shadows, big fonts, decorative colour. Move
  colour usage onto accent (interaction) vs signal (status).
- **One component on its own:** still pull the tokens so the `var(--*)` resolve, then follow the recipe.

When unsure, just open the two source files and copy how they do it:
`C:/Users/jxh/Desktop/website/style.css` and `C:/Users/jxh/alles/static/style.css`.
