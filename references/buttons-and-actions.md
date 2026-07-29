# Buttons and actions

Read this reference for text buttons, icon actions, action groups, busy operations, destructive
actions, and confirmation boundaries.

## Contract anatomy

A button may contain:

- a direct outcome label;
- an optional leading or trailing icon that supports the label;
- a busy indicator that does not erase the outcome;
- optional shortcut text outside the accessible name;
- a 44px or larger target.

The button owns one resting boundary and one focus geometry. An icon does not receive a second tile or
focus box merely because it is present.

## Action hierarchy

- Give one action clear priority at a decision point.
- When two actions are equal, express the relationship intentionally; do not default to the familiar
  filled-primary plus outlined-secondary pair.
- Quiet actions may use type and tonal change without a resting border.
- Destructive styling belongs only to a destructive consequence.
- Links navigate. Buttons change state or perform actions.
- Do not make an entire ambiguous container clickable when a named action is clearer.

## Labels

- Start with a verb and name the outcome: `Save changes`, `Create note`, `Stop generation`.
- Avoid vague labels such as `Continue`, `Yes`, `Submit`, or `Do it` when the outcome can be named.
- Keep the label stable while work proceeds. Add `Saving changes` or a nearby progress description
  rather than replacing the action with an unlabeled spinner.
- Icon-only actions need an accessible name. Use tooltips only as supplementary explanation.
- Do not place shortcut text inside the name announced by assistive technology.

## Required states

| State | Behavior |
| --- | --- |
| default | available with clear label and target |
| hover | tonal or edge change; target does not move or scale |
| focus-visible | one visible focus geometry around the target |
| pressed | immediate, nonmoving acknowledgement |
| busy | `aria-busy=true`, repeat activation rejected, outcome still named |
| disabled | native `disabled` where possible; not focusable unless discovery requires `aria-disabled` |
| destructive | consequence explicit; confirmation when recovery is costly |
| error | failure message and retry policy near the action or affected work |

`disabled` does not mean busy. A busy action can be unavailable to repeat while still exposing its
current operation and cancellation policy.

## Busy and async behavior

1. Commit to the operation only after validation and permission checks.
2. Disable or otherwise reject repeat activation immediately.
3. Set `aria-busy=true` on the affected region or action.
4. Keep a stable progress label.
5. Provide Stop or Cancel when the operation is long-running or consequential.
6. Report success only after the operation actually completes.
7. On failure, preserve user input and expose a recovery action.
8. Restore availability at a deterministic point.

Tests must activate the button twice rapidly and prove the operation runs once.

## Destructive actions

- Name the object and consequence.
- Prefer recovery or undo when feasible.
- Use a dialog when the effect is costly, external, irreversible, or surprising.
- Put the safer action first in focus order unless platform convention and risk analysis say otherwise.
- Confirmation buttons repeat the exact consequence: `Delete project`, not `Confirm`.
- Do not use a toast as confirmation before the action.

## Icon actions

- Bare icon, no decorative tile.
- 16 to 20px optical mark inside at least a 44px target.
- Verify mathematical and optical centering at rendered size.
- Increase target, not glyph size, when accessibility needs more area.
- Use a coherent product icon grammar and real brand marks when applicable.
- Mirror directional icons for right-to-left layouts when their meaning is directional.

## Action groups

- Group by one decision and keep 8px between peer controls.
- Keep unrelated actions in separate groups.
- Avoid sending the secondary action to a distant container edge.
- At narrow widths, stack while preserving priority and reading order.
- Do not create equal-width buttons unless comparison or platform convention benefits.
- A toolbar defines arrow-key behavior only when it is implemented as a toolbar composite.

## Boundary and width

- Content-width is the default button model.
- Full-width is valid for narrow primary actions or a task that genuinely occupies the row.
- Quiet buttons may have no resting edge, but focus still surrounds the 44px target.
- Filled buttons need legible label contrast in every state.
- No all-around glow, hover lift, scale, or duplicate offset box.

## Verification fixtures

Provide deterministic fixtures for:

- default, hover, focus-visible, pressed, disabled, and busy;
- long and CJK labels;
- icon-only accessible name and target measurement;
- rapid double activation;
- destructive confirmation, Escape policy, cancel, confirm, and focus return;
- async failure with preserved input and retry;
- narrow reflow and 200 percent zoom.
