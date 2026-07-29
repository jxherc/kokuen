<p align="center">
  <img src="banner.svg" alt="KOKUEN design operating system" width="100%">
</p>

<h1 align="center">KOKUEN</h1>

<p align="center">
  A design operating system for the parts of product UI that must stay coherent.<br>
  Product-owned character, shared interaction discipline, and rendered proof.
</p>

<p align="center">
  <a href="SKILL.md">Use the skill</a> ·
  <a href="designs/kokuen-visual-template/Universal%20UI%20Template.html">Open the visual reference</a> ·
  <a href="reference.md">Read the contracts</a> ·
  <a href="docs/RESEARCH.md">Review the research</a>
</p>

## What it is

KOKUEN gives designers and coding agents an exact contract for spacing, controls, fields,
navigation, command search, overlays, feedback, AI surfaces, accessibility, Figma parity, and
verification.

It is not a grayscale theme, a component screenshot catalog, an Alles template, or a reusable page
skeleton.

> KOKUEN owns recurring behavior. The product owns character.

That means unrelated products can have different palettes, type, imagery, density, composition, and
signature while their controls remain predictable and complete.

## Use it

Clone the repository into the Codex skills directory:

```bash
git clone https://github.com/jxherc/kokuen.git ~/.codex/skills/kokuen
```

Then invoke it directly:

```text
Use $kokuen to design and verify this product surface.
```

For a new theme or substantial redesign, start with
[`docs/CUSTOM_THEME.md`](docs/CUSTOM_THEME.md). For one reusable component, start with
[`docs/COMPONENT_CONTRACT_TEMPLATE.md`](docs/COMPONENT_CONTRACT_TEMPLATE.md).

## What KOKUEN guarantees

- A deliberate product brief comes before visual styling.
- Layout uses the `0, 4, 8, 12, 16, 24, 32, 48, 64` spacing scale.
- Interactive targets default to at least 44 by 44 CSS pixels.
- One control has one perceived resting boundary and one focus geometry.
- A visible boundary must provide input affordance, state, containment, clipping, or separation.
- Field actions remain attached to the field they change.
- Common controls implement complete pointer, keyboard, focus, disabled, busy, error, and recovery behavior.
- Content remains visible before motion runs, and controls do not jump on hover.
- Theme, contrast, and density are independent axes.
- Figma, screenshots, and source inspection support review, but the current rendered surface is the proof.

The exact rules live in [`references/`](references/). `SKILL.md` is intentionally a concise router so
an agent loads only the material relevant to the task.

## From brief to proof

```text
product brief
    ↓
visual grammar and semantic tokens
    ↓
component anatomy, states, boundaries, keyboard, and content contract
    ↓
Figma and code mapping
    ↓
real interaction, reflow, accessibility, and visual verification
```

The [universal UI reference](designs/kokuen-visual-template/Universal%20UI%20Template.html) is a
functional stress surface for common controls. It deliberately avoids a product hero, dashboard
shell, and modular card layout. It is a reference document, not a product template.

## System inventory

KOKUEN v5 defines 23 candidate contracts across:

- buttons and icon actions;
- text fields, textarea, checkbox, radio group, switch, slider, and select/listbox;
- tabs, menu, row/list, table, and pagination;
- tooltip, popover, dialog, confirmation, toast, and reusable data states;
- universal command/search;
- AI composer, generation, streaming, Stop, sources, permissions, failure, and recovery.

The machine-readable registry is
[`contracts/kokuen.components.json`](contracts/kokuen.components.json). A candidate becomes stable
only after code, Figma, and rendered fixture proof agree.

## Verify it

Run the deterministic checks:

```bash
python3 scripts/validate_theme.py tokens/kokuen.tokens.json
python3 scripts/validate_contracts.py contracts
python3 scripts/validate_figma_manifest.py
python3 scripts/lint_ui_rules.py kokuen.css preview.html \
  "designs/kokuen-visual-template/Universal UI Template.html" \
  tests/forward-fixtures --forbid-native-controls --warnings-as-errors
```

Run the browser interaction suites:

```bash
python3 /Users/jxh/.codex/skills/webapp-testing/scripts/with_server.py \
  --server "python3 -m http.server 4312 --bind 127.0.0.1" \
  --port 4312 -- python3 tests/test_visual_template.py

python3 /Users/jxh/.codex/skills/webapp-testing/scripts/with_server.py \
  --server "python3 -m http.server 4312 --bind 127.0.0.1" \
  --port 4312 -- python3 tests/test_forward_fixtures.py
```

The main suite covers component states, keyboard models, focus containment and return, command
search, async repeat rejection, AI Stop, narrow reflow, a 200-percent equivalent viewport, forced
colors, reduced motion, target measurement, console errors, and screenshots.

The [three forward tests](docs/FORWARD_TESTS.md) prove the same contracts can produce a manuscript
workspace, an operational ledger, and a media browser without converging on one KOKUEN look.

## Repository map

| Path | Purpose |
| --- | --- |
| [`SKILL.md`](SKILL.md) | Entry point and task router |
| [`references/`](references/) | Detailed foundation, component, Figma, AI, and QA rules |
| [`tokens/kokuen.tokens.json`](tokens/kokuen.tokens.json) | Typed primitive, semantic, mode, and component tokens |
| [`contracts/kokuen.components.json`](contracts/kokuen.components.json) | Machine-readable component contracts and fixture IDs |
| [`kokuen.css`](kokuen.css) | No-build reference primitives, not a mandatory visual skin |
| [Universal UI reference](designs/kokuen-visual-template/Universal%20UI%20Template.html) | Functional visual and interaction specimen |
| [`docs/KOKUEN_V5_MASTER_PLAN.md`](docs/KOKUEN_V5_MASTER_PLAN.md) | Architecture, rules, implementation sequence, and acceptance gates |
| [`docs/RESEARCH.md`](docs/RESEARCH.md) | Primary standards and professional design-system sources |
| [`docs/FORWARD_TESTS.md`](docs/FORWARD_TESTS.md) | Product-neutrality proof across three unrelated briefs |
| [`docs/ANTI_SLOP_AUDIT.md`](docs/ANTI_SLOP_AUDIT.md) | Point-by-point visual anti-pattern and craft audit |
| [`figma/kokuen.library.json`](figma/kokuen.library.json) | Validated remote library synchronization manifest |

## Figma

The [KOKUEN Figma file](https://www.figma.com/design/dMpK3ZOhraefh9L6m4BgBi) is the inspectable
design companion. It is not currently synchronized with v5: the installed, authenticated Figma MCP
connector is blocked by the account's Starter-plan tool-call limit. No remote IDs or component keys
are fabricated.

The exact evidence, remaining work, and resume sequence are recorded in
[`docs/FIGMA_SYNC.md`](docs/FIGMA_SYNC.md).

## License

[MIT](LICENSE)
