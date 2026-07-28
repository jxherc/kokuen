# Custom theme: professional system workflow

## Purpose

Use this process when a product needs a complete visual language, a re-theme, or a new Figma/code
foundation. It creates a system with a point of view without turning every product into the same UI.

## 1. Theme brief before components

Fill this in before choosing tokens or a component library.

```text
Product / primary user / job:
What must feel true in three words:
What must never feel true:
Visual medium and asset grammar (photo, diagram, type-led, illustration, material, etc.):
Type role: signature display treatment / quiet body treatment / data treatment:
Color roles: canvas, surface, ink, muted, focus, destructive, success, selection:
Geometry: control density, radius family, edge/border/elevation behavior:
Motion: functional feedback only, reduced-motion behavior:
Icon and image language: source, construction, sizing, and when not to use one:
Reference principles to borrow (not layouts/assets/copy):
Anti-references and known product constraints:
Required common UI and hardest content state:
```

Do not start with a palette site or a hero. Start with the user task and the material world the product
belongs to. A custom theme has a deliberate answer for type, color, geometry, assets, density, and
motion, not merely a different hex value.

## 2. Build the token ladder

Keep raw values isolated from product meaning.

```text
primitive: color.neutral.950 = #171717
semantic:  color.text.primary = {color.neutral.950}
component: button.primary.label = {color.action.primary.label}
```

Use a primitive token for a raw scale. Use a semantic token for a role that can change by theme or
mode. Use a component token only where a stable component decision adds clarity. Alias upward through
the ladder; do not point a semantic token at a component token.

Required foundation groups:

- color: canvas, surface, ink, muted, border, focus, destructive, success, selection;
- space: `0, 4, 8, 12, 16, 24, 32, 48, 64` plus semantic layout aliases;
- typography: family, size, line-height, weight, tracking, roles;
- geometry: control height, radius, border, page gutter, content width;
- motion: duration and easing for feedback only;
- elevation: only if the product has a deliberate physical-depth model.

### Modes and contrast are a contract

Every public semantic token resolves in every supported visual mode. Color scheme/contrast and
density are independent axes: do not clone an entire color theme merely to create compact controls.
Define and test foreground/background/focus pairs explicitly. The baseline is 4.5:1 for normal text,
3:1 for large text, and 3:1 for required control/focus boundaries. Also test forced colors; a
high-contrast product theme is not a replacement for the platform accessibility mode.

Use opaque text and control colors unless transparency is a deliberate, tested material decision.
Alpha text frequently changes contrast when a surface is reused.

### Type and assets are data, not decoration

Before locking type, render a specimen with real product content: long names, CJK, command results,
timestamps, numeric tables, errors, and empty states. Store each font's license/SPDX identifier,
source, version/checksum, supported scripts, fallback stack, and loading policy. Define role tokens
for body, dense body, label, metadata, title, code, and data rather than scattering face-specific
settings through components.

For every icon or other reusable asset, record ID, product purpose, source/license, version, viewBox,
optical size, directionality, status, and replacement ID. Add an icon only when real product evidence
requires it. A complete custom theme needs a coherent asset grammar, not a larger icon pack.

## 3. Prove it under stress

Build one real, populated composition containing all of the following before scaling the theme:

1. primary, quiet, destructive, disabled, and busy actions;
2. a labelled field in filled, focus, invalid, and disabled states;
3. a checkbox, switch, radio, or select with keyboard focus;
4. a command/dialog or menu, including return focus;
5. a dense row, table, or list with long content and empty/loading/error states;
6. a non-blocking feedback state and a consequential confirmation;
7. one actual product screen at wide and narrow widths.

If the type scale, contrast, spacing rhythm, or hierarchy fails in one of these, correct the token or
the component contract. Do not patch each screen independently.

## 4. Figma and code parity

| Source of truth | Must contain | Must not contain |
| --- | --- | --- |
| Token JSON | primitive, semantic, component values and aliases | screen-local one-offs |
| Figma | variables, component variants, realistic usage frames | unbound visual values that diverge silently |
| Code | semantic CSS/custom properties and accessible behavior | duplicated raw values for the same role |
| Decision record | intentional exceptions and migration notes | vague taste claims without an observable rule |

Create Figma collections/modes from the semantic groups. Bind component variants to semantic variables.
Create Code Connect only after the code and component APIs are stable. If Figma cannot be updated,
record exactly which components or modes are missing and keep the code contract authoritative.

## 5. Component contracts and QA

Use [`COMPONENT_CONTRACT_TEMPLATE.md`](COMPONENT_CONTRACT_TEMPLATE.md) before calling a component
stable. A component's visual variant is not its contract: the record must include its slots, state
matrix, token dependencies, keyboard/focus model, accessible naming, content constraints, code path,
and Figma key.

Give the lab a deterministic fixture or URL for each important state. Test approved visual baselines
at desktop and narrow widths, regular/high contrast, normal/reduced motion, and supported density
modes. Exercise Tab/Shift+Tab, arrows, Home/End, Enter, Space, Escape, focus return, pointer, error
recovery, long localized content, font fallback, empty/loading/partial/stale data, and 200% zoom.
Automated accessibility checks support this work; they do not replace real screen-reader review.

## 6. Theme review questions

- Could the palette, type, or geometry be swapped onto a competitor unchanged? If yes, the direction
  has not made a product-specific decision yet.
- Is every visual distinction backed by a semantic role and accessible state, or is color carrying
  meaning alone?
- Does the system still work with long names, user font scaling, forced colors, reduced motion,
  errors, and empty data?
- Do all common controls share intentional height, padding, focus, disabled treatment, and action
  hierarchy?
- Are icons/assets real, licensed, and part of one visual grammar rather than filler?
- Does one strong product-specific visual decision survive across the real screen, rather than only a
  marketing-style first view?

## Handoff

Deliver the completed brief, token file, Figma library/screen status, code mapping, stress-set proof,
and a short list of intentional exceptions. A theme is incomplete when one of those is missing.
