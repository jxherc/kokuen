---
name: kokuen
description: Design, implement, audit, or specify professional product UI with KOKUEN. Use for design systems, shared UI foundations, spacing, boundaries and bezels, buttons, fields, custom controls, navigation, data views, overlays, universal command or search, AI surfaces, Figma libraries, visual redesigns, and rendered accessibility review. Routes work through explicit component contracts, product-specific art direction, deterministic validation, and real interaction proof.
---

# KOKUEN

KOKUEN is a design operating system for the reusable parts of product UI. It governs geometry,
spacing, component behavior, accessibility, Figma parity, and proof. It does not impose one palette,
typeface, page skeleton, or product identity.

The bundled visual specimen uses the original dark KOKUEN palette by default. Treat that as a
reference theme, not a universal accent or signal doctrine.

## Authority

Apply this order when guidance conflicts:

1. explicit user direction;
2. current product rules and real user needs;
3. rendered behavior and current source;
4. KOKUEN invariants and component contracts;
5. product-specific theme decisions;
6. references, libraries, and examples.

A mockup, Figma frame, screenshot, unit test, or source diff never outranks the real delivery surface.

## Start here

Before editing, record this compact map:

```text
Primary user and job:
Primary action:
Secondary actions:
Content hierarchy and hardest content:
Required default, empty, loading, error, unavailable, and permission states:
Keyboard and focus model:
Viewport, zoom, localization, and input constraints:
Existing primitives and product identity to preserve:
Product decisions still required:
Proof surface and completion gates:
```

Inspect unknowns. Do not fill them with generic dashboard copy, fabricated metrics, decorative
components, or an assumed information architecture.

## Rule classes

Classify every design rule before enforcing it:

- **Invariant:** must pass in every implementation.
- **Hard anti-pattern:** prohibited unless the user explicitly directs it or an exception is recorded.
- **Conditional rule:** allowed only for a named job and verified in context.
- **Product decision:** palette, type, imagery, icon grammar, density, radius, signature, and content.
- **Proof gate:** evidence required before completion.

Read [visual-grammar.md](references/visual-grammar.md) for the universal/product boundary and rule
application model.

## Non-negotiable invariants

1. Content is visible before animation runs.
2. Every interactive target is at least 44 by 44 CSS pixels unless a documented target-spacing
   exception is valid for the platform and verified.
3. One control has one perceived resting boundary and one focus geometry.
4. A visible boundary names its job: input affordance, state, containment, clipping, or separation.
5. Focus is visible, unobscured, unclipped, and follows the actual interactive region.
6. Field actions remain inside the field end affordance or directly beside a deliberately bounded
   field. Spare layout width never strands an action.
7. Essential state is not communicated by color alone.
8. Custom controls implement one complete native or WAI-ARIA interaction model.
9. Busy actions reject repeat activation and never imply completion before it occurs.
10. Dialogs and popovers define focus entry, boundary, Escape policy, close behavior, and return.
11. Product identity remains product-specific. KOKUEN must not make unrelated products converge.
12. Completion requires the latest real surface to be rendered and exercised.

Read [boundaries-and-bezels.md](references/boundaries-and-bezels.md) and
[qa-and-antipatterns.md](references/qa-and-antipatterns.md) before changing visual containers or
claiming completion.

## Operating sequence

### 1. Classify the work

| Class | Meaning | Required artifact |
| --- | --- | --- |
| Foundation | repeated visual or behavioral rule | semantic token and usage rule |
| Primitive | one focused interaction | component contract and complete state matrix |
| Pattern | primitives composed for one job | responsive, data-state, and focus behavior |
| Product screen | a real task flow | real content and rendered interaction proof |
| Figma artifact | inspectable specification | variables, components, usage, and drift record |

Do not globalize a one-off without two credible reuse contexts. Extend a stable primitive before
creating a parallel one.

### 2. Choose product character

For a new theme or substantial redesign, complete [CUSTOM_THEME.md](docs/CUSTOM_THEME.md) before
choosing final tokens. Use [visual-grammar.md](references/visual-grammar.md) to define one coherent
world and the explicit anti-references. Preserve established product character when the request is
for shared UI rather than rebranding.

### 3. Establish foundations

Build primitive values, then semantic roles, then durable component tokens. Components do not
consume raw colors or arbitrary layout values. Read only the relevant foundation references:

- layout and proximity: [spacing-and-layout.md](references/spacing-and-layout.md)
- type, color, modes, contrast: [typography-and-color.md](references/typography-and-color.md)
- borders, focus, containment: [boundaries-and-bezels.md](references/boundaries-and-bezels.md)

Validate the token source with:

```bash
python3 scripts/validate_theme.py tokens/kokuen.tokens.json
```

### 4. Write the contract before polishing

Use [COMPONENT_CONTRACT_TEMPLATE.md](docs/COMPONENT_CONTRACT_TEMPLATE.md). A stable component needs
anatomy, variants, states, tokens, boundary rationale, width behavior, accessible semantics,
keyboard model, focus entry and return, content constraints, responsive behavior, fixture IDs, code
path, and Figma key.

Load the component reference that matches the task:

| Work | Required reference |
| --- | --- |
| buttons, icon actions, destructive or busy actions | [buttons-and-actions.md](references/buttons-and-actions.md) |
| fields, forms, textarea, checkbox, radio, switch, slider, select | [forms-and-input.md](references/forms-and-input.md) |
| navigation, tabs, rows, lists, tables, pagination | [navigation-and-data.md](references/navigation-and-data.md) |
| menu, tooltip, popover, dialog, toast, command/search | [overlays-and-command.md](references/overlays-and-command.md) |
| generation, streaming, sources, approval, stop/cancel | [ai-surfaces.md](references/ai-surfaces.md) |

Build every required state before visual polish. Default, hover, focus-visible, pressed, selected,
disabled, busy, invalid, empty, loading, error, unavailable, and permission states apply where the
component can enter them.

### 5. Align Figma and code

Read [figma-contract.md](references/figma-contract.md) and use the active Figma skills before any
Figma mutation. Create semantic variables before components. Component properties map independently
to the public code API. Add review and stress examples, not only a polished default. Code Connect
waits until both APIs are stable.

Figma specifies and reviews the contract. It is not evidence that production behavior works.

### 6. Validate the actual surface

Read [qa-and-antipatterns.md](references/qa-and-antipatterns.md). Run deterministic validators,
then exercise the latest real surface with pointer and keyboard. Inspect wide, narrow, 200 percent
zoom, long and CJK content, reduced motion, forced colors, and every changed state. Check console and
application logs. Fix failures and repeat the pass.

## Companion-skill routing

Use the smallest relevant set and announce why:

| Situation | Companion |
| --- | --- |
| any visual judgment or critique | `human-taste` |
| new or substantially reshaped composition | `frontend-design` |
| production UI implementation | `frontend-ui-engineering` |
| targeted UX or pattern uncertainty | `ui-ux-pro-max` |
| standalone HTML prototype or mockup | `baoyu-design` |
| Figma variables/components/library | `figma:figma-use` plus the relevant Figma skill |
| rendered browser verification | `webapp-testing` |
| final evidence audit | `verification-before-completion` |

Use one primary art-direction authority. Product rules and KOKUEN invariants outrank an imported
recommendation. Do not load every visual skill by default.

## Hard stops

Stop and resolve the issue before completion when:

- the product identity, main user job, or canonical repository is genuinely ambiguous;
- a custom control lacks a complete keyboard and focus model;
- a boundary exists without a declared job;
- a required state or realistic content fixture is missing;
- a Figma/code mismatch is hidden or undocumented;
- the real surface cannot be rendered or exercised;
- an external permission or irreversible AI action lacks an explicit approval boundary.

## Completion report

Report these separately:

1. foundations, contracts, components, and patterns changed;
2. product-specific decisions preserved or introduced;
3. Figma coverage, node or component identifiers, and known drift;
4. rendered viewport and content proof;
5. pointer, keyboard, focus, and state proof;
6. validation, build, lint, test, accessibility, and console proof;
7. exclusions, blocked checks, exceptions, and remaining risk.

Do not say complete while any required evidence is missing.

## Repository map

- [KOKUEN_V5_MASTER_PLAN.md](docs/KOKUEN_V5_MASTER_PLAN.md): architecture and acceptance gates
- [RESEARCH.md](docs/RESEARCH.md): primary standards and professional system references
- [FORWARD_TESTS.md](docs/FORWARD_TESTS.md): product-neutrality evidence
- [ANTI_SLOP_AUDIT.md](docs/ANTI_SLOP_AUDIT.md): final visual quality audit
- [FIGMA_SYNC.md](docs/FIGMA_SYNC.md): current remote status and resume sequence
- [CUSTOM_THEME.md](docs/CUSTOM_THEME.md): product-specific design brief and token workflow
- [COMPONENT_CONTRACT_TEMPLATE.md](docs/COMPONENT_CONTRACT_TEMPLATE.md): stable component record
- [references/](references/): focused professional rules loaded on demand
- [kokuen.tokens.json](tokens/kokuen.tokens.json): portable token source
- [validate_theme.py](scripts/validate_theme.py): deterministic token validation
- [kokuen.library.json](figma/kokuen.library.json): validated Figma synchronization manifest
- [kokuen.css](kokuen.css): portable reference primitives
- [Universal UI Template.html](designs/kokuen-visual-template/Universal%20UI%20Template.html): functional visual specimen
