# Typography, color, modes, and contrast

Read this reference when defining tokens, selecting type, styling states, or auditing readability.

## Role-based type

Define roles before font families:

| Role | Job | Baseline guidance |
| --- | --- | --- |
| body | primary interface reading | 14 to 16px, 1.4 to 1.6 line height |
| label | identifies a control or value | 14px minimum when essential, clear weight difference |
| dense body | data-rich rows and tables | 13 to 14px only with tested contrast and line height |
| metadata | supplementary, nonessential context | may be 12 to 13px if still readable and zoom-safe |
| title | page or task hierarchy | product-specific scale with controlled wrapping |
| data | aligned numeric or structured values | tabular figures where useful |
| code | actual code, identifiers, or machine output | monospace only when content is code-like |

Do not make 10 to 12px uppercase or monospace labels the house voice. Do not use tiny type to make
an overfilled interface appear spacious.

## Type selection

- Choose a signature face from the product brief, not a trend list.
- Use a quiet system or licensed workhorse for body text when it improves clarity.
- Record source, license or SPDX identifier, version/checksum, loading policy, supported scripts,
  fallback stack, and metric-adjustment strategy.
- Preview actual glyphs before selecting. A font name is not proof of character or quality.
- Avoid multiple display voices competing on one surface.
- Do not fake hierarchy through tracked uppercase labels everywhere.

## Content and type stress

Render all of these before locking tokens:

- short and long control labels;
- English, Traditional and Simplified Chinese, Japanese, and mixed-script strings as applicable;
- names, file paths, URLs, timestamps, units, percentages, decimals, and negative values;
- validation messages, empty states, generated output, citations, and permission copy;
- 200 percent zoom and system font fallback.

Do not clip ascenders, descenders, ruby text, focus rings, or CJK glyph boxes with fixed heights.

## Color roles

Use semantic roles. A product may map them to any coherent palette.

```text
canvas
surface.primary / surface.raised / surface.sunken
text.primary / text.secondary / text.disabled / text.inverse
edge.default / edge.strong
focus
selection.background / selection.text
status.error / status.warning / status.success / status.info
action.primary.* / action.quiet.* / action.destructive.*
scrim
```

Do not require a global accent or signal hue. A role exists because content or state needs it, not to
decorate an otherwise flat screen.

## Modes are independent axes

Keep these concerns separate:

- theme or color scheme;
- contrast preference;
- density;
- motion preference;
- platform forced colors;
- input modality.

A compact mode is not a new color theme. A high-contrast mode is not a saturated brand palette.
Every public semantic token resolves in every supported theme mode. Record unsupported combinations.

## Contrast pairs

Validate named foreground/background pairs after aliases resolve:

- normal text: at least 4.5:1;
- large text: at least 3:1 when it meets the actual size and weight threshold;
- essential icons and control boundaries: at least 3:1 against adjacent colors;
- focus indicator: at least 3:1 between focused and unfocused appearance where color carries it;
- disabled content: remain identifiable, but do not imply availability;
- placeholder: readable enough to understand while clearly distinct from entered text.

Do not average contrast across gradients or transparency. Test the worst underlying point. Prefer
opaque text colors unless transparency is a deliberate material decision with tested surfaces.

## State communication

Pair color with another cue:

- invalid: message plus `aria-invalid` and edge or icon change;
- selected: state attribute plus position, weight, check, or surface change;
- busy: busy label plus disabled repeat action and progress behavior;
- success: outcome text plus live-region policy;
- disabled: native or ARIA disabled state plus visual reduction;
- warning: explicit consequence and next action.

Never use a colored dot alone to communicate status.

## Focus and selection

Focus color is a functional role, not the product accent. It must remain distinguishable across every
surface and state. Selection tokens must define both foreground and background. Selected text must not
lose legibility when the OS or browser applies its own highlight.

## Forced colors

Test with platform forced colors:

- retain or restore borders using system colors;
- use `forced-color-adjust` only for essential authored marks, never globally;
- ensure custom check, radio, switch, and slider states remain visible;
- do not rely only on background images, shadows, or color mixing;
- preserve focus and disabled semantics.

## Default KOKUEN specimen palette

The shipped specimen uses dark neutral graphite as a demonstration mode:

```text
canvas: near-black graphite
surface: a slight tonal lift, used only when containment needs it
text: high-contrast warm white
secondary text: readable neutral gray
edge: low-contrast graphite; strong edge reserved for state
focus: a high-contrast neutral ring
error and success: restrained semantic tones plus explicit wording
```

Do not describe the specimen as a mandatory greyscale system. Product themes may use color, but every
color must have a role and pass the same contracts.

## Audit

1. Inventory every font family, size, line height, weight, and tracking value.
2. Replace screen-local type values with roles or document the exception.
3. Resolve all semantic color aliases for every mode.
4. Validate named contrast pairs.
5. Inspect actual CJK and fallback rendering.
6. Check error, disabled, placeholder, selected, focus, and inverse states.
7. Remove color whose only job is decorative emphasis.
8. Confirm type and palette still express the product brief rather than the KOKUEN specimen.
