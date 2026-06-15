# 黒鉛 kokuen — component catalog & recipes

The "why" behind the laws, plus copy-paste patterns. Class names match `kokuen.css`. Source of
truth: `C:/Users/jxh/Desktop/website/style.css` (green) and `C:/Users/jxh/alles/static/style.css`
(purple). When this doc and those files disagree, the files win.

---

## The palette, explained

| token | dark | light | what it's for |
|-------|------|-------|---------------|
| `--bg` | `#0a0a0a` | `#f5f4f1` | the paper. near-black / warm bone — never pure #000 or #fff |
| `--text` | `#e8e6e3` | `#111111` | ink. body copy, values, the thing you actually read |
| `--muted` | `#6e6e6e` | `#888888` | pencil-grey. labels, keys, secondary text, hover targets |
| `--faint` | `#2e2e2e` | `#d4d2ce` | ghost-grey. borders, dividers, bar tracks, disabled |
| `--panel` | `#0e0e0e` | `#efede9` | raised/hover surface — one notch off `--bg` |
| `--signal` | per project | per project | the ONE non-grey. a status sign — right / live / updated / on. never decoration |
| `--error` | `#f87171` | — | destructive / mic recording / validation |
| `--green` | `#4ade80` | — | success / positive delta (when the signal isn't already green) |

The whole base is **black & white** — the grey ramp `bg → text → muted → faint` is the spine,
and most of the UI is built out of just those four. `--signal` is *not* part of the aesthetic;
it's information. It appears only to say "this is right / live / updated / on", and it should
feel like spending something. A screen with zero signal on it is completely normal.

**Why warm light mode:** `#f5f4f1` paper + `#111` ink reads like newsprint, not a glaring white
SaaS dashboard. Keep the warmth; don't "fix" it to `#fff`.

---

## Typography in detail

- **Families:** `Inter` (UI/prose) with the system fallback stack; `JetBrains Mono` for code, IDs,
  timestamps, token counts, file paths — anything that came from a machine.
- **Feature settings:** `'cv11','ss01','ss03'` on the root (single-story a, stylistic alts). It's
  subtle but it's part of the fingerprint — keep it.
- **Weights:** `400` body · `500` labels/brand/emphasis · `300` for large thin display headers ·
  `600` only for a loud number (countdown, big stat). That's the whole scale.
- **The two-mode letter-spacing rule** (most important type tell):
  - prose / headings / values → **tight**: `-0.005em` to `-0.025em`
  - labels / buttons / meta / stamps → **wide + lowercase**: `+0.04em` to `+0.08em`, `text-transform:lowercase`
- **Size ladder** (rem): `0.6` micro-meta · `0.62–0.66` stamps/cat-labels · `0.68–0.72` buttons/labels ·
  `0.78–0.82` list rows · `0.875` kv/body-small · `0.95–1.06` intro/prose · `1.15` card heading ·
  `1.9` page display. Living above ~1.1rem for UI text is a smell.
- **Numbers:** `font-variant-numeric:tabular-nums` on anything that ticks (clock, age, timer),
  ranks, or column-aligns. Use the `.tnum` helper.

---

## Components

### Ghost button (`.btn`)
The default button. No fill, 1px `--faint` border, lowercase + tracked. Hover wakes text to
`--text`, border to `--muted`, background to `--panel`. `.active` = same as hover (sticky).
Variants seen in the wild: bordered (`.btn`), bare text (`.btn-bare`), and pill-of-buttons
toggle groups (`.toggle-row` of `.btn`, one `.active`).

### Live dot (`.live-dot`)
5px signal circle, `live-pulse` 2s (opacity 0.3↔1). Means "this is live / now / happening". The
static cousin `.dot` is faint and only turns signal (`.dot.on`) when its row is active/selected.

### Key/value row (`.kv`)
`min-width` key in muted + wide-tracking, value in text. As a link it dims to 0.7 opacity and its
trailing `.arrow` (a faint `↗`) kicks `translate(3px,-3px)`. The backbone of "about/contact/specs"
lists.

### Bar (`.bar-wrap` + `.bar`)
3px track in `--faint`, fill in `--muted` (or `--signal` via `.win`, i.e. the bar that's "winning"). Animate by adding `.fill` →
`scaleX(0→1)` over the house easing. Used for top-songs, genres, year-vs-year. Width-animation
(`transition:width`) is an acceptable alt for variable-length fills.

### Hover-underline link (`.ul`)
Underline is a `::after` 1px bar that `scaleX`-sweeps from the left on hover. Cleaner than
`text-decoration`. Use for inline nav and lists.

### Card (`.card`)
Flat: 1px faint border, micro-radius, optional `--panel` hover. Add `.lift` for the `translateY(-2px)`
raise. Image cards (covers/portraits) do the same lift on a wrapping element and fade the `<img>`
in via an `.loaded` class (opacity 0→1) once it loads. No drop shadows.

### Dialog / overlay (`.overlay` + `.dialog`)
Overlay `rgba(0,0,0,0.6)`, fades in via `.show`. Dialog is a `--panel` card that slides up 8px on
entrance. Min 260 / max 380px. Same recipe powers confirm dialogs, meme modals, settings popovers.

### Stagger entrance (`.rise`)
Direct children start at `opacity:0; translateY(6px)` and animate up on `nth-child` delays ~0.07s
apart (house easing, 0.7s). This is how every page "arrives". `kokuen.css` ships delays for 10
children; extend the list if a container has more. Pair with `prefers-reduced-motion` (already in
the base).

---

## Custom controls — the recipes (NEVER ship native)

Standing user rule: no default browser widgets. Each of these replaces one.

### Toggle switch (`.switch`) — replaces `<input type=checkbox>` as an on/off
34×20 pill, 16px white knob with a soft shadow (the *only* sanctioned shadow), `top/left:2px`,
slides to `left:16px` and track→signal when on (on = a state, so the signal color is correct here).
Drive with `aria-checked="true"` or `.on`. Wire a
click handler in JS; it's a `<div>`, not an input.

### Checkbox (`.chk`) — replaces `<input type=checkbox>` as a tick
15px box, 1.5px `--muted` border, 3px radius. Checked → signal fill + a CSS `::after` tick (rotated
border trick, white). `role="checkbox" aria-checked`.

### Slider (`.slider`) — restyled `<input type=range>`
The one native element we keep, but `appearance:none` strips all chrome: 4px faint track, 15px round
signal thumb ringed by `box-shadow:0 0 0 1px var(--signal)` and a 2px `--bg` border so it floats off
the track. Thumb scales 1.18 on hover. Style both `::-webkit-slider-thumb` and `::-moz-range-thumb`.

### Select — replaces native `<select>`
Don't use `<select>`. Build a `.btn`-styled trigger (`.custom-select`: faint underline/border,
chevron, `min-height:31px`) that opens an absolutely-positioned `--panel` menu of rows; rows hover
to `--panel`/`--text`, selected row gets a check or signal text. Close on outside-click / Esc.

### Color picker — replaces `<input type=color>`
If you need one: saturation box + hue slider built from divs, same as alles' `accent-custom`. Native
color input only as a last-resort hidden fallback.

### Scrollbars
Already global in `kokuen.css`: 3px, `--faint` thumb → `--muted` on hover, transparent track,
`scrollbar-width:thin`. Don't override back to native.

---

## Motion cheatsheet

- **Easing:** `var(--ease)` = `cubic-bezier(0.2,0.7,0.2,1)` for transforms & entrances. Plain `ease`
  for color/border/background fades.
- **Durations:** `0.12–0.18s` micro (hover color, knob slide) · `0.2–0.3s` standard (borders,
  dialogs) · `0.5–0.7s` entrances & bar fills · `1s` long bar/genre fills.
- **Hover vocabulary:** lift `translateY(-2px)` · arrow kick `translate(3px,-3px)` · underline
  `scaleX(0→1)` · img `scale(1.04)` + `brightness(0.7)` · thumb `scale(1.18)`.
- **Keyframes:** `rise` (up+in), `fade-in`, `live-pulse` (dot), `mic-pulse`/`think-shimmer` for
  busy/recording states.

---

## Light-mode checklist (when adding `[data-theme="light"]`)

The four tokens + `--panel` flip automatically. What you must hand-fix:
1. Any hardcoded dark hex you used for image/placeholder backgrounds (`#161616`, `#1a1a1a`, `#0e0e0e`)
   → light equivalents (`#e8e6e2`, `#e2e0dc`, `--panel`).
2. `:hover` backgrounds that referenced a literal dark panel → repoint to `--panel` or a light hex.
3. Re-check signal contrast on `#f5f4f1` — a neon that pops on black can vanish on paper.
4. Never introduce pure `#fff`/`#000`; stay on the warm ramp.

Provide a `.theme-toggle` (fixed, top-right, faint→muted on hover) that flips `data-theme` on
`<html>` and persists to `localStorage`.

---

## Quick smell-test before shipping

- [ ] Base is pure black & white, and the only non-grey is `var(--signal)` *reporting state* (right/live/updated/on), not decorating?
- [ ] Every `border-radius` ≤ 4px (except the toggle)?
- [ ] No native checkbox / select / scrollbar / range chrome visible?
- [ ] Labels lowercase + wide-tracked; prose tight-tracked?
- [ ] UI text mostly 0.6–0.9rem?
- [ ] Borders 1px `--faint`, waking to `--muted` on hover?
- [ ] Moving things use `cubic-bezier(0.2,0.7,0.2,1)`?
- [ ] Numbers `tabular-nums`?
- [ ] No shadows except under the toggle knob?
- [ ] Page elements `rise` in on load?

If all ten are yes, it's kokuen.
