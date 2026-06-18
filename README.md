<img src="banner.svg" alt="kokuen" width="100%">

# kokuen (黒鉛)

Near-black greyscale UI. Square corners, small type, 1px borders. Tokens pulled out of
[my site](https://github.com/jxherc/website) and alles so I stop rewriting the same CSS.

黒鉛 = graphite. Greys do the work. One optional colour, used sparingly.

## use it

```html
<link rel="stylesheet" href="kokuen.css">
```
```css
:root{
  --accent:#818cf8;   /* the optional colour. var(--text) to drop it */
  --signal:#00ff2a;   /* status hue, if it differs from accent. else delete this line */
}
```
```html
<button class="btn">save</button>
<span class="live-dot"></span>
<div class="switch on" aria-checked="true"></div>
<a class="ul" href="#">link</a>
```

No build, no deps. Every class is readable in [`kokuen.css`](kokuen.css).

## tokens

```css
:root{
  --bg:#0a0a0a; --text:#e8e6e3; --muted:#6e6e6e; --faint:#2e2e2e; --panel:#0e0e0e;
  --accent:#818cf8;          /* var(--text) for none */
  --signal:var(--accent);    /* override for a separate status hue */
  --error:#f87171; --green:#4ade80;
}
[data-theme="light"]{
  --bg:#f5f4f1; --text:#111111; --muted:#888888; --faint:#d4d2ce; --panel:#efede9;
}
```

paper, ink, pencil, ghost. Light mode is warm paper, not white.

## colour

Base is greyscale: `bg`, `text`, `muted`, `faint`, plus a `panel` shade. Fixed.

One optional colour (`--accent`) on top, used sparingly: interaction (button, focus ring, active row)
or status (live dot, a done tick). Set `--accent: var(--text)` to drop it and stay grey. `--signal` is
there if the status hue should differ from the interaction hue; it defaults to `--accent`.

alles uses purple for both. My site uses one green, in three places, all status.

## the rest

Rules and every component value are in [`reference.md`](reference.md). [`SKILL.md`](SKILL.md) is the
same thing as a Claude Code skill: drop the folder in `~/.claude/skills/kokuen/`.

MIT.
