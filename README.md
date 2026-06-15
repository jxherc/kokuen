# 黒鉛 kokuen

A near-black web design system. Four shades of grey on near-black paper (warm bone-white in light
mode), and exactly **one** color allowed to show through — the accent, like the single bright mark
a pencil can't make. *Kokuen* (黒鉛) means graphite.

It's the house style behind [jxherc/website](https://github.com/jxherc/website) (accent green) and
`alles` (accent purple) — same bones, different nameplate. This repo is that style pulled out so any
new thing can speak it.

```
--bg #0a0a0a   --text #e8e6e3   --muted #6e6e6e   --faint #2e2e2e   + one --accent
```

## Use it

Link the stylesheet, set your one accent, build against the documented class names:

```html
<link rel="stylesheet" href="kokuen.css">
```
```css
:root{ --accent:#818cf8; }   /* the only thing you change per project */
```

- **[`kokuen.css`](kokuen.css)** — drop-in: tokens, reset, base typography, thin scrollbars, inverted
  selection, focus rings, the `rise` / `live-pulse` / `fade-in` keyframes, and every custom control
  (ghost button, toggle, checkbox, slider, ghost input).
- **[`reference.md`](reference.md)** — the full component catalog & recipes: the palette explained,
  typography rules, every component, the custom-control recipes (so you never ship native chrome),
  a motion cheatsheet, a light-mode checklist, and a 10-point ship smell-test.
- **[`SKILL.md`](SKILL.md)** — the same system packaged as a [Claude Code](https://claude.com/claude-code)
  skill. Drop the folder into `~/.claude/skills/kokuen/` and Claude applies the style on request.

## The 9 laws

1. **Four greys, near-black paper, one accent.** The accent is the only saturated hue and it stays rare.
2. **Inter for words, JetBrains Mono for data.** `font-feature-settings:'cv11','ss01','ss03'`, antialiased.
3. **Letter-spacing has two modes.** Prose/headings tight (negative); labels/buttons wide + lowercase (positive).
4. **Everything is small.** UI text lives at 0.6–0.9rem.
5. **Micro-radii only.** `border-radius` 1–4px. The only pill is a real toggle switch.
6. **1px faint borders that wake up on hover** (`--faint` → `--muted`). Flat surfaces, no shadows.
7. **One easing for everything that moves:** `cubic-bezier(0.2,0.7,0.2,1)`.
8. **Numbers are `tabular-nums`.**
9. **No native chrome — ever.** Build the checkbox, toggle, slider, select, scrollbar yourself.

## Tokens

```css
:root{
  --bg:#0a0a0a; --text:#e8e6e3; --muted:#6e6e6e; --faint:#2e2e2e;
  --panel:#0e0e0e;
  --accent:#818cf8;              /* swap per project */
  --error:#f87171; --green:#4ade80;
}
[data-theme="light"]{
  --bg:#f5f4f1; --text:#111111; --muted:#888888; --faint:#d4d2ce; --panel:#efede9;
}
```

`--bg → --faint` is the graphite ramp: paper, ink, pencil-grey, ghost-grey. Light mode is warm
paper, not white — keep the warmth.

---

MIT. Build something that looks like it's mine.
