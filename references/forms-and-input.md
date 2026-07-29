# Forms and input controls

Read this reference for text fields, search, textarea, validation, checkbox, radio, switch, slider,
select/listbox, and form composition.

## Field anatomy

Use this order:

```text
label
optional requirement or format information
field or composite field
hint, status, or error
```

- Associate the label programmatically.
- Connect hint and error IDs with `aria-describedby`.
- Set `aria-invalid=true` only while invalid.
- Keep entered text after a failed submit unless security requires removal.
- State requiredness in semantics and visible language.
- Placeholder text never replaces a label.

## Field width and boundaries

Choose a width model from expected content:

- short value: bounded inline field;
- ordinary text: readable bounded field with an explicit maximum;
- full-row search, command, or composition: container width;
- narrow viewport: responsive full width with the same action proximity.

For a field with prefix, suffix, unit, clear, reveal, or browse action, the wrapper owns the single
resting boundary and `:focus-within` geometry. Child inputs have no independent border or outline.
Independent adjacent actions retain their own focus rings but remain immediately proximal.

## Text input and textarea

- Use the correct native input type and autocomplete purpose.
- Use a textarea for multiline intent.
- Do not use fixed heights that clip enlarged text.
- Preserve visible selection, caret, autofill, spellcheck, and password-manager behavior.
- Search fields may expose a clear action only when a value exists; the action remains labelled.
- Composition fields keep Send, Stop, attachment, and scope actions within the same spatial group.
- Read-only content remains selectable and distinguishable from disabled content.

## Validation

Validate at the least disruptive useful time. Do not announce an error before the user has had a
reasonable chance to satisfy the field.

- Error text names the problem and recovery: `Enter a project name`, not `Invalid input`.
- Associate each error with its field.
- Move focus to the first invalid field or an error summary after failed submit when appropriate.
- An error summary links back to fields and does not replace inline messages.
- Keep layout stable enough that the field does not move away from focus when an error appears.
- Do not use color, asterisk, or icon alone.

## Checkbox

Prefer a styled native `<input type="checkbox">` when compatible with the product. A fully custom
checkbox uses `role=checkbox`, `aria-checked`, and Space. Enter may activate when consistent with the
platform, but Space is required.

States: unchecked, checked, indeterminate if applicable, focus-visible, hover, pressed, disabled,
invalid when part of a required group. The label participates in the 44px target.

## Radio group

A radio pattern requires at least two mutually exclusive choices in a labelled group.

- Use native radios when possible.
- Custom radios use `role=radiogroup` and child `role=radio`.
- One radio has `tabindex=0`; peers use `tabindex=-1`.
- Arrow keys move focus and selection through enabled choices.
- Space selects the focused choice.
- Home and End may move to first and last choice.
- Disabled choices are skipped and exposed.
- Do not demonstrate a lone radio as if it were a complete group.

## Switch

Use a switch for an immediate binary setting, not for submitting a preference later.

- Expose `role=switch` and `aria-checked` or use a native checkbox with equivalent labelling.
- The label states what is on or off; avoid labels that change meaning with state.
- Space toggles. Enter may toggle for button-based implementations.
- Announce failure if the setting cannot persist; do not visually flip and silently revert.
- The track and knob are one control with one 44px focus geometry.

## Slider

Prefer native range input when it can be styled without losing platform behavior. A custom slider
requires `role=slider`, accessible name, min, max, current value, and text value when raw numbers are
not meaningful.

- Arrow keys adjust by step.
- Page Up and Page Down may use a larger step.
- Home and End move to limits.
- Respect orientation and right-to-left behavior.
- Pointer interaction uses the whole track target.
- Do not rely on a tiny thumb as the only hit region.
- Expose current value visibly when the task needs precision.

## Select and listbox

Use a native `<select>` when native appearance is allowed. In products that require custom KOKUEN
controls, choose one complete model:

### Select-only combobox with `aria-activedescendant`

- Trigger has `role=combobox`, `aria-expanded`, `aria-controls`, and accessible name.
- DOM focus remains on the trigger.
- Open listbox has one active option referenced by `aria-activedescendant`.
- Arrow keys move active option; Home and End jump; Enter or Space commits; Escape closes without
  changing the committed value; printable characters may perform typeahead.
- On close, focus remains on the trigger.

### Button plus listbox with option focus

- Trigger is a button with `aria-haspopup=listbox` and `aria-expanded`.
- On open, focus moves to the selected or first enabled option.
- Options implement Arrow, Home, End, Enter, Space, Escape, and typeahead.
- Close restores focus to the trigger.

Do not mix DOM focus on options with an unrelated `aria-activedescendant` on the trigger. Disabled
options are skipped in navigation but remain perceivable when useful.

## Form composition

- Group related fields with `fieldset` and `legend` or an equivalent labelled group.
- Use 8px label-to-field and field-to-help gaps; use 16px between complete field groups.
- Keep actions adjacent to the form they submit.
- Do not put every field in its own card.
- At narrow widths, preserve DOM order and error association.
- Avoid multi-column forms unless the field relationships are obvious and remain usable at zoom.
- Confirm what Enter submits; multiline and composite fields may need different behavior.

## Disabled, read-only, unavailable, and busy

- `disabled`: unavailable and normally removed from focus order.
- `aria-disabled`: discoverable but blocked; event handlers must reject activation.
- `readonly`: value can be focused and copied but not edited.
- unavailable: explain the condition and recovery.
- busy: current operation in progress; input policy and cancellation are explicit.

Do not use opacity alone to distinguish these states.

## Required fixtures

- empty, placeholder, filled, focus, invalid, disabled, read-only, and autofill field;
- composite field with proximal clear action and one perceived boundary;
- textarea with long CJK input;
- checkbox checked, unchecked, indeterminate, and disabled;
- radio group Arrow, Home, End, and disabled-skip behavior;
- switch persistence success and failure;
- slider Arrow, Home, End, pointer, and value text;
- select open, navigation, commit, cancel, typeahead, and focus return;
- failed submit with focus and `aria-describedby` proof;
- narrow and 200 percent zoom layouts.
