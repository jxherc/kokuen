# KOKUEN reference

## Token contract

Use names, not fixed colors. Every product supplies values for `--ui-canvas`, `--ui-surface`,
`--ui-text`, `--ui-muted`, `--ui-border`, `--ui-border-strong`, `--ui-focus`, `--ui-error`, and
`--ui-success`. Keep the spacing scale at 4, 8, 12, 16, 24, 32 and document any exception.
Read [`docs/SPACING.md`](docs/SPACING.md) before composing a screen. Spacing is a contract, not an aesthetic suggestion.

Use the token ladder consistently:

| Layer | Owns | Example | May reference |
| --- | --- | --- | --- |
| Primitive | raw, reusable values | `color.neutral.950`, `space.24` | final value only |
| Semantic | product meaning | `color.text.primary`, `space.layout.section` | primitives |
| Component | durable component-specific decision | `button.primary.background` | semantic tokens |

Components consume semantic or component tokens, never raw values. Do not create a component token
for a one-off local adjustment; fix the composition or define the semantic role first. The portable
schema is [`tokens/kokuen.tokens.json`](tokens/kokuen.tokens.json); run
`python3 scripts/validate_theme.py tokens/kokuen.tokens.json` after a token change.

## Component contract

| Component | Required states | Non-negotiable behavior |
| --- | --- | --- |
| Button | primary, secondary, quiet, destructive, loading, disabled | 44px target; direct label; no hover lift |
| Field | default, focus, filled, hint, invalid, disabled | Label and error are programmatic; focus is visible; inline actions stay adjacent to the field value |
| Switch / checkbox | checked, unchecked, disabled | Native button semantics plus `role`; Space and Enter work |
| Slider | min, max, intermediate, disabled | `role=slider`, Arrow, Home, End, value ARIA |
| Listbox | default, active, selected, disabled, empty | One active option; Arrow/Home/End/Enter/Escape |
| Dialog | opening, open, loading, error, closing | labelled, focus managed, Escape where appropriate |
| Toast / feedback | neutral, success, warning, error | concise text; not color-only |
| Navigation / tabs | default, current, hover, focus, disabled | `aria-current` or tablist keyboard model |
| Menu | closed, open, focused, disabled, destructive | menu button and menuitem semantics; Escape and focus return |
| Data table / list | loading, empty, populated, selected, error | headings, row actions, responsive fallback |
| Pagination | default, current, unavailable | current page announced; previous/next disabled correctly |
| Empty / loading / error | initial, retryable, permission-gated | explain the state and offer only relevant recovery |

## Universal command contract

Use one dialog, one focused input, and one listbox. Groups are presentational labels, not nested
listboxes. Each actionable row is a semantic button with `role=option`. The input owns
`aria-activedescendant`; exactly one option has `aria-selected=true`.

- `ArrowDown` / `ArrowUp`: move active option, wrapping when useful.
- `Home` / `End`: first / last option.
- `Enter`: perform active action.
- `Escape`: close and restore focus to the opener.
- Filtered results retain the same keyboard model.
- Provide loading, empty, error, and unavailable/no-permission content in the same dialog.
- AI actions must name the scope and consequences, and never pretend to have acted before they do.

## Figma contract

Create semantic variables first, then components. A component set must document its variants and
states. Treat the following as the minimum Figma inventory: Foundation tokens, Button, Field,
selection controls, List row, Dialog, Command, feedback, and one real product screen. Figma is a
review and specification tool; code remains the delivery surface.

## Complete universal inventory

The universal layer is deliberately broad but not a giant visual kit. Its stable API includes:

- **Foundation:** semantic colors, type roles, spacing, radii, breakpoints, focus, motion.
- **Actions:** text, primary, secondary, quiet, destructive, icon, loading, disabled buttons.
- **Inputs:** text, search, password, textarea, prefix/suffix, validation, helper text.
- **Choice:** checkbox, switch, radio, slider, listbox/select, segmented control, tabs.
- **Structure:** page shell, navigation, sidebar, header, stack, cluster, card, divider.
- **Collections:** row, list, table, pagination, filter bar, empty/loading/error states.
- **Overlays:** menu, tooltip, popover, dialog, confirmation, command palette, toast.
- **AI:** scoped input, streaming, approval, error, citation/result, and stop/cancel states.

Every entry gets states, keyboard behavior, focus treatment, disabled behavior, and responsive
rules before it is called reusable.

## Delivery check

- Test every changed control with pointer and keyboard.
- Confirm focus entry, active state, Escape, and focus restoration.
- Check narrow and wide layouts, text overflow, empty/loading/error/disabled states, and reduced
  motion.
- Inspect the actual final surface and console. A local mockup or Figma frame does not substitute.
- Re-check the theme stress set: primary/quiet actions, field error, choice control, command or
  dialog, dense content, feedback, and a real screen. If a theme works only in its hero, it is not a system.
