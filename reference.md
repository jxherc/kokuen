# kokuen reference

Everything with real numbers. Class names match `kokuen.css`. When this disagrees with the source,
the source wins: `C:/Users/jxh/Desktop/website/style.css` and `C:/Users/jxh/alles/static/style.css`.

---

## palette

| token | dark | light | what it does |
|-------|------|-------|--------------|
| `--bg` | `#0a0a0a` | `#f5f4f1` | the paper. near-black, or warm bone in light. never pure `#000`/`#fff` |
| `--text` | `#e8e6e3` | `#111111` | ink. body, values, the thing you read |
| `--muted` | `#6e6e6e` | `#888888` | pencil. labels, keys, secondary text, the hover target colour |
| `--faint` | `#2e2e2e` | `#d4d2ce` | ghost. borders, dividers, bar tracks, disabled |
| `--panel` | `#0e0e0e` | `#efede9` | raised/hover surface. one notch off bg |
| `--accent` | per project | per project | the optional colour. interaction (button, focus, active) or status. `var(--text)` for none |
| `--signal` | per project | per project | separate status hue, when status should differ from accent. defaults to accent |
| `--error` | `#f87171` | same | destructive, validation, recording |
| `--green` | `#4ade80` | same | success / positive delta (toasts, diff-add) |

The grey ramp `bg → text → muted → faint` is the spine. `--panel` is for the slightly-raised stuff.
Light mode is warm paper on purpose, keep it warm.

### the optional colour

Greys carry the UI. One colour goes on top, used sparingly, for one of two jobs:

- interaction: active nav, focus ring, primary button, checked box, a name in a greeting.
- status: a live dot, the winning bar, a done tick.

`--accent` is the interaction hue, `--signal` is the status hue, and `--signal` falls back to
`--accent` if unset. Use one colour for both (alles uses purple) or split them. Set
`--accent: var(--text)` to drop the interaction hue and keep status only. That's what my site does:
one green, in `.live-dot`, `.year-card.winner .year-bar`, and `.pace-arrow`.

---

## typography

- **families:** Inter (`'Inter',-apple-system,BlinkMacSystemFont,sans-serif`) for everything readable.
  JetBrains Mono (`'JetBrains Mono',ui-monospace,SFMono-Regular,Menlo,Consolas,monospace`) for code,
  IDs, timestamps, counts, paths.
- **features:** `font-feature-settings:'cv11','ss01','ss03'` on the root. antialiased +
  `-moz-osx-font-smoothing:grayscale`. subtle but it's part of the fingerprint.
- **weights:** 400 body · 500 labels/brand/emphasis · 300 big thin display · 600 one loud number. done.
- **the two-mode letter-spacing** (most important rule):
  - prose, headings, values → tight, negative, −0.005 to −0.025em
  - labels, buttons, captions, meta, stamps → wide + lowercase, +0.04 to +0.08em, `text-transform:lowercase`
- **size ladder (rem):** `0.6` micro · `0.62–0.66` caption/stamp · `0.68–0.72` label/button ·
  `0.78–0.82` list row · `0.875` body-small / kv / textarea · `0.95–1.06` prose/intro · `1.15` card head ·
  `1.9` page display.
- **line-heights:** 1.5 base, 1.55–1.7 for prose, 1 for tight stacked numbers, 1.6 for textareas.
- **numbers:** `font-variant-numeric:tabular-nums` (`.tnum`) on anything ticking or aligned.

---

## spacing & layout

No rigid scale, but the rhythm in both files: section gaps `2.5–3rem`, control padding `0.3–0.45rem`
vertical / `0.5–0.9rem` horizontal, list row padding `0.4rem 0.9–1.1rem`, card padding `1–1.25rem`.

- reading column: `max-width: 560px`, centered, `body` padding `6rem 2rem 5rem` (the site).
- app shell: fixed `100vh`, flex, `.sidebar` is `248px` fixed width with a `1px var(--faint)` right border.
- grids: `repeat(4,1fr)` album-style with `1rem` gaps; drop to 3 cols under 600px.
- dividers: `1px var(--faint)`, or a dashed `stroke-dasharray:2 4` feel for a softer split.

---

## components

Exact values. All of these are in `kokuen.css`.

### buttons
- **`.btn`** (default, ghost): no fill, `1px var(--faint)`, radius 2px, `0.68rem`, lowercase,
  `letter-spacing:0.05em`, padding `0.35rem 0.75rem`, colour `--muted`. Hover → text colour, `--muted`
  border, `--panel` bg. `.active` looks the same as hover (sticky).
- **`.btn-bare`**: text only, no border, `0.7rem`, muted → text on hover.
- **`.btn-primary`**: accent text + `45%` accent border; hover adds `12%` accent bg. The rare loud one.
- **`.btn-danger`**: same shape in `--error`.
- **`.seg`**: a row of `.btn`; the `.active` one gets `12%` accent bg + `40%` accent border + accent text.

### inputs
- **`.field`**: underline only. transparent bg, `border-bottom:1px var(--faint)`, `0.72rem`, placeholder
  in `--faint`, focus → `--muted` underline. This is the default input.
- **`.field-box`**: boxed, sits on `--panel`, radius 3px, focus → muted border.
- **`.field-glow`**: the important one (main composer). focus → accent border + the glow:
  `box-shadow:0 0 0 1px var(--accent), 0 0 16px color-mix(in srgb,var(--accent) 25%,transparent)`.
- textareas: `resize:none`, `line-height:1.6`.

### custom controls
- **`.switch`** (replaces a checkbox used as on/off): 34×20 pill, `--faint` track, 16px white knob at
  `top/left:2px` with `box-shadow:0 1px 3px rgba(0,0,0,.35)` (one of the only shadows in the system).
  `.on` / `aria-checked="true"` → track `--accent`, knob slides to `left:16px`. It's a div, wire the
  click in JS.
- **`.chk`** (checkbox): 15px, `1.5px var(--muted)` border, radius 3px. checked → accent fill + a CSS
  `::after` tick (rotated bottom-right border, white). `role="checkbox" aria-checked`.
- **`.slider`** (range): `appearance:none`, 4px `--faint` track, 15px round accent thumb ringed with
  `box-shadow:0 0 0 1px var(--accent)` and a `2px var(--bg)` border so it floats. thumb `scale(1.18)`
  on hover. style both `::-webkit-slider-thumb` and `::-moz-range-thumb`.
- **select**: build it. a `.btn`-style trigger (`min-height:31px`, a chevron, faint underline/border)
  that opens an absolutely-positioned `--panel` list; rows hover to `--panel`/`--text`, the selected
  row gets a tick or accent text. close on outside-click and Esc. never `<select>`.

### status marks (these are `--signal`)
- **`.live-dot`**: 5px circle, `live-pulse` 2s (opacity 0.3↔1). means live/now.
- **`.dot`** / **`.dot.on`**: 5px, faint by default, turns signal when the row is active/live.
- **`.ok`**: signal-coloured text or tick. "right / correct / done."
- **`.badge-new`**: a `.badge` with signal border. "updated / new."
- **`.bar`** + **`.bar.win`**: 3px track (`--faint`), fill `--muted`, animates by adding `.fill`
  (`scaleX 0→1`). the winning/best bar swaps fill to `--signal`.

### badges / tags
- **`.badge`**: greyscale by default. `0.62rem`, lowercase, `1px faint` border, radius 2px,
  padding `0.05rem 0.35rem`. add a semantic colour class to tint it.

### key/value rows
- **`.kv`**: muted key (`min-width:84px`, `0.72rem`, wide) + text value. as a link it dims to `0.7`
  opacity and the trailing `.arrow` (faint `↗`) nudges `translate(3px,-3px)` on hover.

### links
- **`.ul`**: hover-underline that sweeps in from the left (`::after` 1px bar, `scaleX 0→1`, 0.25s).
  cleaner than `text-decoration`. use for inline nav.

### list rows
- **`.row`**: flex, `0.8rem`, muted, padding `0.4rem 0.9rem`. hover → text + `--panel`.
- **`.row.active`**: `12%` accent bg + text colour (the soft selected state).
- **`.row.sel`**: solid `--accent` bg, `--bg` text. inverted. for hard selection (a picked day).

### cards
- **`.card`**: `1px faint`, radius 3px, padding `1rem 1.25rem`, flat. hover → muted border + panel bg.
- **`.card.lift`**: adds `translateY(-2px)` on hover.
- image cards: wrap the `<img>`, start it `opacity:0`, add `.loaded` (→ opacity 1) once it loads;
  hover the wrapper does the lift, the img does `scale(1.04)` + `brightness(0.7)`.

### overlay + dialog
- **`.overlay`**: fixed, `rgba(0,0,0,.6)`, fades in via `.show`.
- **`.dialog`**: a `--panel` card, `min 260 / max 380px`, slides up 8px on entrance. same recipe for
  confirms, modals, settings popovers.

### toast
- **`.toasts`** container fixed bottom-right, `gap 0.4rem`. **`.toast`**: panel bg, faint border,
  `0.78rem`, `rise` in. `.success` → green border+text, `.error` → error border+text.

### context menu
- **`.ctx`**: fixed, panel bg, faint border, `min-width:140px`, `fade-in`. **`.ctx-item`**: `0.78rem`
  muted, hover → text + `--bg`. **`.ctx-item.danger`** in `--error`.

### tooltip
- **`.tip`**: panel bg, faint border, `0.66rem`, `white-space:nowrap`, `pointer-events:none`, `fade-in`.

### code / kbd
- **`.code`**: `#111` bg (light: `#ebe9e5`), faint border, mono `0.75rem`, `line-height:1.55`.
- **`kbd`**: faint border, radius 3px, `0.7rem`, muted.

### empty / loading
- **`.empty`**: faint, `0.78rem`, italic. for "nothing here yet."
- **`.skel`**: panel bg, `shimmer` (opacity 0.35↔0.7). skeleton row while loading.

### momentary accent bits
- **`.stream-cursor`**: 2px×0.9em accent bar, `blink` 0.9s step-end. for streaming text.
- **`.flash`**: `name-flash` 1.5s, accent → text. flash a value that just changed.

### entrance
- **`.rise`**: put it on a container. direct kids start hidden + 6px down and animate up on
  `nth-child` delays ~0.07s apart, 0.7s, house easing. `kokuen.css` ships 10 delays, extend the list
  if a container has more kids.

---

## motion cheatsheet

- ease: `cubic-bezier(0.2,0.7,0.2,1)` for transform/entrance, plain `ease` for colour fades.
- durations: `0.12–0.18s` micro · `0.2–0.3s` standard · `0.5–0.7s` entrance + bar · `1s` long fill.
- hover moves: lift `-2px`, arrow `+3/-3`, underline `scaleX`, img `scale 1.04 + brightness .7`,
  thumb `scale 1.18`.
- keyframes: `rise`, `fade-in`, `live-pulse`, `blink`, `name-flash`, `shimmer`.

---

## light mode

The five tokens flip via `[data-theme="light"]`. What you hand-fix:

1. hardcoded dark hexes you used for image/placeholder bg (`#161616`, `#1a1a1a`, `#111`) → light
   equivalents (`#e8e6e2`, `#e2e0dc`, `#ebe9e5`).
2. any `:hover` bg that pointed at a literal dark panel → repoint to `--panel`.
3. re-check **both** accent and signal contrast on `#f5f4f1`. a neon that pops on black can vanish on
   paper (my green `#00ff2a` is borderline in light, bump it if needed).
4. never introduce pure `#fff`/`#000`. stay warm.

Ship a `.theme-toggle` (fixed top-right, faint → muted on hover) that flips `data-theme` on `<html>`
and saves to `localStorage`.

---

## smell test before shipping

- [ ] base is greyscale; colour only shows up to be interactive (accent) or report state (signal)?
- [ ] you know which of your colours is accent and which is signal, and they're used for the right jobs?
- [ ] every radius ≤ 4px except the toggle?
- [ ] no native checkbox / radio / select / range / scrollbar visible?
- [ ] labels lowercase + wide; prose tight?
- [ ] UI text mostly 0.6–0.9rem?
- [ ] borders 1px faint, waking to muted on hover?
- [ ] moving things use the one easing?
- [ ] numbers tabular?
- [ ] no shadows except the toggle knob + focus glow?
- [ ] stuff `rise`s in on load, and reduced-motion is handled?

---

## worked examples

**a "now playing" row, my-site style (greys + green status, no interaction hue):**
```css
:root{ --accent:var(--text); --signal:#00ff2a; }
```
```html
<div class="row">
  <span class="live-dot"></span>            <!-- green, pulsing -->
  <span class="ul">song title</span>
  <span class="muted">artist</span>
  <span class="cap" style="margin-left:auto">2m ago</span>
</div>
```

**a sidebar session item, alles style (one purple doing both):**
```css
:root{ --accent:#818cf8; }   /* signal inherits */
```
```html
<div class="row active">                    <!-- 12% purple tint bg -->
  <span class="dot on"></span>              <!-- purple -->
  <span>session name</span>
</div>
```
