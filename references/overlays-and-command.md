# Overlays, feedback, and universal command

Read this reference for menu, tooltip, popover, dialog, confirmation, toast, and universal command or
search.

## Layer model

Every temporary layer defines:

```text
Trigger and accessible name:
Relationship to trigger or viewport:
Modal or nonmodal:
Initial focus:
Focus boundary:
Pointer outside policy:
Escape policy:
Close controls:
Return-focus target:
Scroll and resize behavior:
Layer and collision tokens:
```

Use one surface boundary. Do not nest decorative shells or clip focus indicators.

## Menu

- Trigger is a button with `aria-haspopup=menu` and `aria-expanded`.
- Opening places focus on the first enabled, last, or selected item according to the initiating key.
- Arrow Down and Arrow Up move through enabled items.
- Home and End move to first and last enabled items.
- Enter and Space invoke an item.
- Escape closes and restores focus to the trigger.
- Printable characters perform typeahead when useful.
- Disabled items are skipped but exposed.
- Pointer outside behavior closes without moving focus to an arbitrary location.

Menus contain actions or choices, not arbitrary form layouts. Use a popover or dialog for richer
content.

## Tooltip

- Supplements an already named control; never provides its only accessible name.
- Appears on hover and focus after a deliberate delay, remains available while hovered when needed,
  and closes on Escape.
- Does not contain interactive content.
- Avoids covering the trigger or required nearby content.
- Is not shown for every familiar icon by default.

## Popover

A popover contains nonmodal contextual content. It needs an anchor, accessible name when necessary,
focus policy, outside-dismiss policy, Escape behavior, collision handling, and return behavior. Do
not trap focus unless the interaction is modal or the chosen pattern requires containment.

## Dialog

- Use a native `<dialog>` when its behavior fits and is normalized across supported browsers, or a
  tested dialog implementation.
- Expose `role=dialog` and `aria-modal=true` for modal dialogs.
- Label with `aria-labelledby` and describe consequential content with `aria-describedby`.
- Move focus to the least destructive useful control, first field, or dialog container based on task.
- Trap Tab and Shift+Tab within the open dialog.
- Close by Escape unless the operation cannot safely dismiss; document exceptions.
- Provide an explicit close or cancel action.
- Restore focus to the opener or the nearest logical surviving control.
- Prevent background interaction and manage scroll without layout jump.
- Keep headings and final actions visible at narrow height and 200 percent zoom.

## Confirmation

Confirmation states the object, consequence, reversibility, and affected scope. The destructive
button repeats the consequence. Do not ask for confirmation for harmless or easily reversible work.
Do not use a toast as a pre-action confirmation.

## Toast and live feedback

- Use a toast for nonblocking outcome information.
- Use `role=status` for polite updates and `role=alert` only for urgent interruption.
- Keep the message concise and provide an action only when it supports recovery or undo.
- Do not move focus into a toast automatically.
- Pause dismissal while hovered or focused.
- Give enough time to read and support persistent alternatives for important information.
- Avoid stacking many toasts or using them as an activity log.

## Universal command

Universal command is a product service that may combine navigation, search, creation, contextual
actions, and bounded AI actions. It is not a large decorative search field.

### Anatomy

```text
labelled modal dialog
one autofocus search or combobox input
optional scope and query status
one listbox
presentational group labels
semantic options
empty, loading, error, unavailable, and permission states
optional preview or consequence description
```

### Semantics and focus

- The input owns `role=combobox`, `aria-expanded`, `aria-controls`, and `aria-activedescendant`.
- The result container has one `role=listbox`.
- Each actionable result has `role=option`, a stable ID, and `aria-selected`.
- DOM focus remains on the input while active descendant changes.
- Group labels are presentational and do not create nested listboxes.
- Exactly one enabled result is active when actionable results exist.

### Keyboard model

- Arrow Down and Arrow Up move active result.
- Home and End move to first and last enabled result.
- Enter invokes the active result.
- Escape clears an intermediate state first only if this policy is visible; otherwise it closes.
- Tab remains inside the modal and reaches any explicit scope, preview, or close actions.
- The global shortcut opens without stealing focus while a conflicting text composition is active.
- Closing restores focus to the opener or logical destination after navigation.

### Filtering and async states

- Filtering preserves the same focus model and stable IDs where possible.
- No results clears `aria-activedescendant` and announces the empty state.
- Loading exposes busy state without presenting stale results as current.
- Errors preserve the query and offer retry.
- Unavailable and permission-bound results explain why and are not invokable.
- Results do not reorder under the pointer or active descendant without an explicit update policy.

### AI actions

An AI option names its scope and effect before invocation. It must distinguish asking, previewing, and
executing. External or irreversible action requires confirmation. Generated completion is never
assumed from an animated state.

## Focus-trap algorithm

For small framework-free fixtures:

1. capture the opener;
2. reveal the overlay and remove background interaction;
3. focus the documented initial element;
4. on Tab or Shift+Tab, cycle among currently visible enabled focusable descendants;
5. on close, hide the overlay, restore background interaction, and focus the opener if it survives;
6. when the opener is removed, focus the nearest logical task control.

Production code should prefer a proven dialog primitive over a hand-rolled trap.

## Required fixtures

- menu pointer open, Arrow open, Arrow/Home/End navigation, invoke, Escape, outside close, focus return;
- tooltip hover, focus, Escape, and collision placement;
- dialog Tab and Shift+Tab wrap, Escape, cancel, confirm, focus return, narrow height, zoom;
- toast polite announcement, pause, undo, and stacking policy;
- command shortcut, active descendant, filter, Home/End, invoke, empty, loading, error, unavailable,
  permission, Escape, Tab trap, and focus return.
