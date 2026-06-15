---
name: kokuen
description: >-
  Apply 黒鉛 kokuen — jxherc's signature near-black "graphite" web design language,
  reverse-engineered from jxherc/website and jxherc/alles. A four-step gray ramp on
  near-black (or bone-white in light mode), Inter + JetBrains Mono, micro border-radii,
  one swappable accent color, the cubic-bezier(0.2,0.7,0.2,1) easing, the "rise" stagger,
  inverted text selection, and fully custom (never-native) controls. Use whenever building
  or restyling ANY web page / app UI / component for this user, or when they say "my style",
  "the usual look", "kokuen", "黒鉛", or "match my site / alles".
---

# 黒鉛 kokuen

The house style. *Kokuen* = graphite, pencil lead. The whole UI is drawn in four shades of
grey on near-black paper, and exactly **one** color is allowed to show through — the accent,
like the single bright mark a pencil can't make. Get the greys and the motion right and it
reads as "mine" instantly; the accent is just the nameplate.

Two real codebases already speak it: `jxherc/website` (accent = green `#00ff2a`) and
`jxherc/alles` (accent = purple `#818cf8`). Same bones, different nameplate. When you build
something new, you're adding a third.

## The 9 laws (don't break these — everything else is taste)

1. **Four greys, near-black paper, one accent.** Background, text, muted, faint — that's the
   whole palette. The accent is the *only* saturated hue and it stays rare: live dots, the
   active state, a winner bar, a focused thumb. If two accent things are adjacent, one of them
   is wrong.
2. **Inter for words, JetBrains Mono for data.** `font-feature-settings:'cv11','ss01','ss03'`,
   always antialiased. Mono is for code, IDs, timestamps, raw values — anything machine-ish.
3. **Letter-spacing has two modes.** Prose & headings go *tight* (negative, −0.005 to −0.025em).
   Labels, buttons, meta go *wide + lowercase* (positive, +0.04 to +0.08em, `text-transform:lowercase`).
   This contrast is the single most recognizable tell of the style.
4. **Everything is small.** UI text lives at 0.6–0.9rem. A 0.7rem label is normal. Display
   headers cap around 1.9rem and often drop to `font-weight:300`. If it looks like a "normal
   website" font size, it's too big.
5. **Micro-radii only.** `border-radius` is 1–4px (default 2–3px). The *only* pill in the system
   is a real toggle switch. No big soft rounded cards, ever.
6. **1px faint borders that wake up on hover.** Dividers and outlines are `1px solid var(--faint)`.
   On hover they go to `var(--muted)`. Surfaces are flat — lift with the `--panel` shade or a 2px
   translateY, not with shadows (shadows only exist under a moving knob).
7. **One easing for everything that moves:** `cubic-bezier(0.2,0.7,0.2,1)`. Fast out, soft landing.
   Plain `ease` at 0.12–0.3s is fine for color/border fades; the bezier is for transforms and entrances.
8. **Numbers are `tabular-nums`.** Any number that ticks, ranks, aligns in a column, or sits next
   to another number gets `font-variant-numeric:tabular-nums`.
9. **No native chrome — ever.** Build the checkbox, the toggle, the slider, the select, the
   scrollbar yourself (recipes in `reference.md`). A default browser widget breaks the spell.

## Tokens (copy verbatim — these are identical across both sites)

```css
:root{
  --bg:#0a0a0a; --text:#e8e6e3; --muted:#6e6e6e; --faint:#2e2e2e;
  --panel:#0e0e0e;                /* raised / hover surface */
  --accent:#818cf8;              /* THE one color — swap per project */
  --error:#f87171; --green:#4ade80;
}
[data-theme="light"]{
  --bg:#f5f4f1; --text:#111111; --muted:#888888; --faint:#d4d2ce; --panel:#efede9;
}
```

`--bg → --faint` is the graphite ramp: paper, ink, pencil-grey, ghost-grey. Memorize the order.
Light mode is warm paper (`#f5f4f1`), not white — keep the warmth.

**Picking an accent for a new project:** one saturated color, readable on both `#0a0a0a` and
`#f5f4f1`. Greens/indigos/violets fit the family. Run it through the same `var(--accent)` slot —
never hardcode it, so a future re-theme is one line.

## How to apply

- **New page/app:** start from `kokuen.css` (drop-in: tokens + reset + base + all the primitives
  and custom controls). Set `--accent`, write your markup against the documented class names.
- **Restyle / matching an existing thing:** lift the tokens block and the 9 laws; translate their
  components onto the grey ramp. Kill every `border-radius > 4px`, every native control, every
  shadow that isn't under a knob.
- **A single component in isolation:** still pull the tokens so `var(--*)` resolves, then follow
  the relevant recipe in `reference.md`.

Honor the user's standing rule: **no default browser widgets** — if you're about to emit a bare
`<input type=checkbox/range/...>` or a native `<select>`, stop and use the kokuen control instead.

## Files in this skill

- **`kokuen.css`** — the drop-in stylesheet. Tokens, reset, base typography, scrollbars, selection,
  focus, the `rise`/`live-pulse`/`fade-in` keyframes, and every custom control (button, toggle,
  checkbox, slider, ghost input). Link it, set `--accent`, go.
- **`reference.md`** — the full component catalog & recipes: ghost button, live dot, key/value rows,
  scaleX bars, hover-underline links, lift-on-hover cards, the stagger-entrance pattern, dialog/overlay,
  toggle/checkbox/slider/select internals, and the light-mode checklist. Read it when you need a
  specific pattern or want the "why" behind a law.

When in doubt, open the two source files and match them:
`C:/Users/jxh/Desktop/website/style.css` and `C:/Users/jxh/alles/static/style.css`.
