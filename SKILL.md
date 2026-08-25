---
name: kokuen
description: Design skill for professional product UI. Use when designing, building, redesigning, or auditing interfaces: design systems, themes and tokens, typography, color, spacing, buttons, forms, navigation, data views, overlays, command search, AI surfaces, accessibility, and rendered verification. Establishes product-specific art direction, enforces complete component states and interaction contracts, and requires proof on the real rendered surface.
---

# KOKUEN

KOKUEN is a design skill for professional product UI. It covers the whole craft: art direction,
foundations, component design, accessibility, and proof on the real rendered surface.

One boundary governs everything:

> KOKUEN owns recurring behavior. The product owns character.

Two products can share the same button contract and look nothing alike. KOKUEN must never make
unrelated products converge, and a finished screen must never read as if it could belong to anyone.

## Authority

When guidance conflicts, apply this order:

1. explicit user direction;
2. the product's own rules and its real users;
3. rendered behavior on the current surface;
4. KOKUEN rules and component contracts;
5. references, libraries, and examples.

A mockup, screenshot, test, or diff never outranks the real delivery surface.

## 1. Build the brief

No visual work before this exists:

```text
Primary user and highest-frequency job:
Moment of greatest risk or cognitive load:
Three qualities that must feel true / three that must never:
Hardest real content case:
Signature artifact or interaction:
References to borrow principles from, and anti-references to avoid:
Viewport, zoom, localization, and input constraints:
```

Infer what is safe to infer. Stop and ask when the job or identity is genuinely ambiguous. Never
fill unknowns with dashboard filler, invented metrics, or an assumed information architecture.

## 2. Make a direction

Design from the brief, not from a trend list. For a new theme or substantial redesign, complete
[docs/CUSTOM_THEME.md](docs/CUSTOM_THEME.md) first, and read
[references/visual-grammar.md](references/visual-grammar.md) in full.

- Choose one coherent world: ink on a measured surface, a dense operational instrument, a tactile
  shelf, a typographic editor, or a product-specific world the task supports. Let that one logic
  govern type, spacing, edges, motion, and imagery together. Never assemble attractive parts from
  unrelated visual systems.
- Make one signature decision specific enough that it could not be pasted into a competitor
  unchanged. A signature is a real artifact, an authored layout, a typographic behavior, a bespoke
  icon construction. It is not a glow, a gradient, a card grid, or a decorative hero stack.
- State what stays quiet so the signature has room. Minimal means every remaining element carries
  more responsibility, not that fewer decisions were made.

### Recognize the defaults

Agent-generated product UI clusters around unchosen answers. Know them so you can refuse them:

- the sidebar + topbar + stat-card shell, big number over small label, whatever the actual job;
- one saturated hue on a dark ground, gradient text, glows, blurred blooms behind elements;
- tracked-uppercase 11px labels as the only hierarchy; one sans carrying every role;
- cards inside cards, stacked even shadows, the same radius on everything;
- a lone colored bar glued to a card edge, or a colored dot as the only carrier of status;
- marketing moves inside a working tool: oversized hero headline, CTA pair, feature-card trio;
- emoji or generic thin-line icon packs filling space;
- hairline rules and eyebrow ticks used as ornament where spacing and type would do the job;
- hover lift or scale on controls; entrance animations that hide content until they run.

When the brief explicitly names one of these, the brief wins. When it leaves the axis free, do
not spend that freedom on a default.

## 3. Establish foundations

Primitive values first, then semantic roles, then component tokens. Components never consume raw
color or arbitrary layout values. Load only what the task needs:

- spacing, proximity, target size, responsive behavior:
  [references/spacing-and-layout.md](references/spacing-and-layout.md)
- type roles, color roles, modes, contrast, CJK:
  [references/typography-and-color.md](references/typography-and-color.md)
- borders, focus geometry, containment, field width:
  [references/boundaries-and-bezels.md](references/boundaries-and-bezels.md)

Validate the token source after changing it:

```bash
python3 scripts/validate_theme.py tokens/kokuen.tokens.json
```

## 4. Design components by contract

Write the contract before the polish:
[docs/COMPONENT_CONTRACT_TEMPLATE.md](docs/COMPONENT_CONTRACT_TEMPLATE.md). Build every state the
component can enter (default, hover, focus-visible, pressed, selected, disabled, busy, invalid,
empty, loading, error) before refining any single one.

| Work | Required reference |
| --- | --- |
| buttons, icon actions, destructive or busy actions | [references/buttons-and-actions.md](references/buttons-and-actions.md) |
| fields, forms, textarea, checkbox, radio, switch, slider, select | [references/forms-and-input.md](references/forms-and-input.md) |
| navigation, tabs, rows, lists, tables, pagination | [references/navigation-and-data.md](references/navigation-and-data.md) |
| menu, tooltip, popover, dialog, toast, command/search | [references/overlays-and-command.md](references/overlays-and-command.md) |
| generation, streaming, sources, approval, stop/cancel | [references/ai-surfaces.md](references/ai-surfaces.md) |

### Invariants

Hard constraints, not judgment calls:

1. content is visible before animation runs, and never gated behind an animation;
2. interactive targets are at least 44 by 44 CSS px unless a documented platform exception applies;
3. one control has one perceived resting boundary and one focus geometry;
4. every visible boundary has a named job: affordance, state, containment, clipping, separation;
5. state styling affects the whole silhouette, never a colored bar attached to one edge;
6. focus is visible, unobscured, unclipped, and follows the real interactive region;
7. field actions stay attached to the field they change;
8. no essential state is communicated by color alone;
9. custom controls implement one complete native or WAI-ARIA interaction model, keyboard included;
10. busy actions reject repeat activation and never imply completion before it occurs;
11. dialogs and popovers define focus entry, containment, Escape policy, close, and return;
12. controls do not lift, scale, or jump on hover;
13. the latest real surface is rendered and exercised before completion is claimed.

## 5. Prove it on the real surface

[references/qa-and-antipatterns.md](references/qa-and-antipatterns.md) is the audit reference.
Run the deterministic validators, then exercise the latest real surface with pointer and keyboard:
wide and narrow viewports, 200 percent zoom, long and CJK content, reduced motion, forced colors,
every changed state. Console must be clean. Fix failures and repeat the pass until it holds.

A screenshot pass or a green test alone is not proof.

## Figma

Conditional. Include it only when the user requests Figma output or the product names Figma parity
as a requirement; then read [references/figma-contract.md](references/figma-contract.md) and keep
[docs/FIGMA_SYNC.md](docs/FIGMA_SYNC.md) current. Figma specifies and reviews the contract. It
never proves production behavior, and missing Figma evidence is not a blocker when Figma is out of
scope.

## Companion skills

Load the smallest relevant set, and say why:

| Situation | Skill |
| --- | --- |
| visual judgment or critique | `human-taste` |
| new composition or page design | `frontend-design` |
| targeted pattern lookup | `ui-ux-pro-max` |
| existing product tokens to preserve | `extract-design-system` |
| rendered browser verification | `webapp-testing` |
| final evidence audit | `verification-before-completion` |

Use one primary art-direction authority per task. Product rules and the invariants above outrank
any imported recommendation.

## Hard stops

Stop and resolve the issue before continuing when:

- the product identity, main user job, or canonical repository is genuinely ambiguous;
- a custom control lacks a complete keyboard and focus model;
- a boundary exists without a declared job;
- a required state or realistic content fixture is missing;
- a Figma/code mismatch is hidden while Figma is in scope;
- the real surface cannot be rendered or exercised;
- an external permission or irreversible AI action lacks an explicit approval boundary.

## Report

Report separately:

1. foundations, contracts, components, and patterns changed;
2. product-specific decisions preserved or introduced;
3. Figma coverage and known drift when in scope, or that it was excluded;
4. rendered viewport and content proof;
5. pointer, keyboard, focus, and state proof;
6. validation, lint, test, accessibility, and console proof;
7. exclusions, blocked checks, exceptions, and remaining risk.

Do not say complete while any required evidence is missing.

## Repository map

- [docs/KOKUEN_V5_MASTER_PLAN.md](docs/KOKUEN_V5_MASTER_PLAN.md): architecture and acceptance gates
- [docs/RESEARCH.md](docs/RESEARCH.md): standards and professional system sources
- [docs/FORWARD_TESTS.md](docs/FORWARD_TESTS.md): product-neutrality evidence
- [docs/ANTI_SLOP_AUDIT.md](docs/ANTI_SLOP_AUDIT.md): visual quality audit
- [docs/CUSTOM_THEME.md](docs/CUSTOM_THEME.md): product-specific design brief and token workflow
- [references/](references/): focused professional rules, loaded on demand
- [tokens/kokuen.tokens.json](tokens/kokuen.tokens.json): portable token source
- [contracts/kokuen.components.json](contracts/kokuen.components.json): component contract registry
- [kokuen.css](kokuen.css): portable reference primitives, not a mandatory skin
- [Universal UI Template.html](designs/kokuen-visual-template/Universal%20UI%20Template.html):
  functional visual specimen
