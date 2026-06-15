<img src="banner.svg" alt="kokuen — a black and white UI system" width="100%">

# kokuen (黒鉛)

The look I put on basically everything. Near-black, greyscale, no rounded corners, small type, quiet
until you touch it. I got tired of rebuilding the same CSS for every project so I pulled the tokens
out of [my site](https://github.com/jxherc/website) and alles and dumped them here.

*Kokuen* means graphite. It's a pencil drawing — four greys do all the work and colour only shows up
when it's actually telling you something.

## colours: there are two, and they're not the same thing

This trips people up so I'll be blunt about it.

The **base is grey**. Five shades, fixed, that's the actual aesthetic. On top of that you get two
colours, and they do different jobs:

- **accent** — the project's identity colour. Active states, focus rings, a primary button, the logo.
  Normal accent stuff. It's *optional*. alles has one (purple). My own site has none, it's straight
  black and white.
- **signal** — a status colour. Means right, live, updated, on. A pulsing dot, the winning bar, a
  "done" tick. That's it, it never decorates. On my site the green is *only* this — it shows up in
  three places and nowhere else.

They can be the same colour or different. If you only set `--accent`, the signal just copies it (that's
alles, one purple doing both). Set them apart when the status colour should be its own thing (that's my
site: no accent, green signal).

```
my site →  no accent (pure b&w) + green signal
alles   →  purple accent, signal inherits it
```

## use it

```html
<link rel="stylesheet" href="kokuen.css">
```
```css
:root{
  --accent:#818cf8;   /* your identity colour. or var(--text) if you want none, like my site */
  --signal:#00ff2a;   /* status. delete this and it copies the accent */
}
```

Then it's just classes:

```html
<button class="btn">save</button>
<span class="live-dot"></span>             <!-- signal, pulsing -->
<div class="switch on" aria-checked="true"></div>
<a class="ul" href="#">a link</a>
```

No build, no dependencies. Every class is readable in [`kokuen.css`](kokuen.css).

## the rules

The stuff that makes it look right. Skip these and it falls apart.

1. Grey first. Colour needs a reason — it's either interactive (accent) or it's reporting state
   (signal). A screen with zero colour is fine.
2. Inter for words, JetBrains Mono for anything machine-shaped (code, IDs, timestamps, raw numbers).
3. Letter-spacing goes two ways: prose tight (negative), labels and buttons wide + lowercase. This
   one does most of the heavy lifting.
4. Small. UI text is 0.6–0.9rem. If it looks like a normal website font size it's too big.
5. Barely-rounded. 1–4px. The only pill is a toggle switch.
6. 1px faint borders that go to muted on hover. Flat surfaces. No drop shadows.
7. One easing for everything that moves: `cubic-bezier(0.2,0.7,0.2,1)`.
8. `tabular-nums` on numbers that tick or line up.
9. No native controls, ever. Build the checkbox, toggle, slider, select, scrollbar yourself.

## tokens

```css
:root{
  --bg:#0a0a0a; --text:#e8e6e3; --muted:#6e6e6e; --faint:#2e2e2e; --panel:#0e0e0e;
  --accent:#818cf8;          /* var(--text) for none */
  --signal:var(--accent);    /* override for a separate hue */
  --error:#f87171; --green:#4ade80;
}
[data-theme="light"]{
  --bg:#f5f4f1; --text:#111111; --muted:#888888; --faint:#d4d2ce; --panel:#efede9;
}
```

paper, ink, pencil, ghost. Light mode is warm paper, not white — leave it warm.

## what's in here

| file | what |
|------|------|
| [`kokuen.css`](kokuen.css) | the drop-in. tokens, reset, type, scrollbars, every component and custom control, the keyframes. |
| [`reference.md`](reference.md) | the long version. every component with real numbers, the accent tint scale, light-mode notes, a ship checklist, worked examples. |
| [`SKILL.md`](SKILL.md) | same thing as a [Claude Code](https://claude.com/claude-code) skill. drop the folder in `~/.claude/skills/kokuen/` and it'll style stuff for you. |

---

<sub>MIT. built by <a href="https://github.com/jxherc">jxherc</a>. 黒鉛</sub>
