# Figma contract

Read this reference before mutating a Figma file or claiming Figma/code parity.

## Purpose

Figma is the inspectable design contract for variables, component APIs, states, examples, and review.
Code remains the delivery surface. A polished frame without bindings, states, or behavior mapping is
not a design system.

## Discovery before writing

Record:

```text
File key and file name:
Pages and purpose:
Existing variable collections and modes:
Published libraries and dependencies:
Local components and component sets:
Duplicate or detached components:
Existing review, stress, and product usage frames:
Code API and token source:
Known drift, conflicts, and missing coverage:
```

Inspect before creating. Reuse or migrate stable assets rather than duplicating them.

## Variable architecture

Separate collections by concern when modes differ independently:

- primitive color and raw values;
- semantic theme roles;
- contrast adjustments;
- spacing and geometry;
- density;
- typography roles;
- motion;
- component aliases only where stable component decisions require them.

Use aliases from semantic to primitive and component to semantic. Do not bind components directly to
raw palette values. Keep theme, contrast, and density as independent mode axes.

Name variables with a stable path that maps to token JSON and code. Record intentional normalization
differences such as slash vs dot syntax.

## Component architecture

One stable primitive becomes a component set only after its contract is known.

- Use independent variant properties such as `Hierarchy`, `State`, `Size`, and `Icon`, not a single
  opaque property containing every combination.
- Prefer boolean and instance-swap properties for optional icons and slots.
- Bind dimensions, colors, type, radii, and effects to variables.
- Keep layer names semantic and stable enough for inspection and Code Connect.
- Include default, hover, focus, pressed, disabled, busy, invalid, selected, and destructive states
  only where the component can actually enter them.
- Match code property names and value vocabulary where possible.
- Do not create impossible combinations merely to fill a matrix.

## Minimum library inventory

- foundations and mode matrix;
- Button and icon action;
- Field and composite field;
- Checkbox, radio group, switch, slider, and select/listbox;
- Tabs, row/list, table primitives, and pagination;
- Menu, dialog, confirmation, toast, and universal command;
- AI composition and streaming controls when the consuming product uses them.

## Documentation pages

Create pages or clearly separated frames for:

1. **Foundations:** token roles, modes, spacing relationships, target geometry, type, focus, layers.
2. **Components:** anatomy, property mapping, state matrix, content constraints, code status.
3. **Do and do not:** unnecessary bezel, nested boundary, focus around unused width, stranded field
   action, overwide field, tiny target, color-only state, and hover movement.
4. **Stress:** long English, CJK, empty, loading, error, unavailable, permission, narrow layout,
   high contrast, reduced motion, and 200 percent zoom examples.
5. **Usage:** at least one real product flow after the library is stable. Product usage does not turn
   product-specific composition into a universal primitive.

Bad examples are labelled and visually separated from reusable components. Do not publish them as
library assets.

## Boundary documentation

Each component description records:

```text
Boundary job:
Resting boundary owner:
Focus boundary owner:
Width behavior:
Nested-boundary prohibition:
High-contrast behavior:
```

Use measurement annotations to prove 44px targets and spacing relationships. Do not decorate the
page with arbitrary ruler graphics.

## Code mapping

Maintain a mapping table:

```text
Component stable ID:
Figma node ID and component key:
Figma property -> code property:
Variable -> token -> code variable:
Code import and public API:
Unsupported combinations:
Intentional drift and owner:
Last verified revision:
```

Create Code Connect only after both APIs are stable. A mapping cannot repair a mismatched API; fix or
record the mismatch first.

## Mutation discipline

- Follow the active Figma skill's discovery and approval phases.
- Write incrementally and verify each mutation before the next.
- Use explicit node IDs and store a state ledger for long runs.
- Tag generated nodes with shared plugin data when the tool supports it.
- Never silently delete or replace user-owned components.
- Record all created variable IDs, component IDs, component keys, page IDs, and review frame IDs.
- Capture screenshots after major mutations and inspect them, not only metadata.

## Review gates

Review foundations, components, and documentation separately. Verify:

- all public variables resolve in supported modes;
- component properties map to code without opaque combination names;
- targets, spacing, boundary ownership, and focus states are measurable;
- stress examples use real content rather than placeholders;
- no bad example is published as a component;
- the latest library screenshot matches the source and token contract;
- known drift is visible and assigned.

Figma completion must be reported separately from rendered code completion.
