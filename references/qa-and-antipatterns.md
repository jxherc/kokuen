# Quality assurance and anti-patterns

Read this reference before visual handoff or a completion claim.

## Proof hierarchy

Use the strongest available evidence:

1. real production or local delivery surface with current build and data-safe fixtures;
2. browser or app interaction through pointer, keyboard, zoom, and platform modes;
3. automated accessibility, visual, unit, integration, and source validation;
4. Figma, mockup, screenshot, or isolated component supporting evidence;
5. source inspection only.

Lower levels do not replace missing higher-level proof. State exactly what remains unverified.

## Source-level hard failures

Reject or fix:

- interactive target below 44px without a valid documented exception;
- opacity-zero or translated-away content that depends on animation to appear;
- hover transform or scale on buttons and ordinary cards;
- focus suppression without a visible replacement;
- clickable nonsemantic containers;
- error text not associated with its field;
- busy action that accepts repeat activation;
- dialog with no focus boundary or focus return;
- custom select, menu, radio, tabs, slider, or command with an incomplete keyboard model;
- native controls forbidden by the consuming product's rules;
- color-only state;
- colored or thickened partial-edge status rail on an already contained box;
- raw layout spacing outside the scale without a semantic exception.

## Boundary warnings

Investigate rather than automatically reject:

- nested elements both drawing border, shadow, or focus geometry;
- one edge of a contained component carrying a different state thickness or color;
- more than one strong boundary within 8px;
- full-width field for short content;
- field action separated by flexible space;
- same-level card nesting;
- divider next to sufficient section spacing;
- container radius, surface, border, and shadow all expressing the same separation;
- outline clipped by overflow or layer collision.

Resolve each warning with a declared boundary job or remove the redundant edge.

## Visual anti-pattern pass

Check the complete active anti-slop law, including:

- generic card grids and modular dashboard composition;
- pill badges, glowy buttons, background glows, gradient text, and blue-purple defaults;
- icon tiles, fake app windows, fake code snippets, fabricated logos, and decorative metrics;
- default hero stacks, split heroes, filled-plus-outline action pairs, and repeated kicker headings;
- tiny uppercase or monospace labels everywhere;
- all-around shadows, hover lifts, hidden entrance content, clipped text, and ragged peer alignment;
- default sun/moon toggles, active-nav dots, decorative rules, and unreadable muted text;
- accent bars or side rails stapled onto cards, toasts, rows, or status boxes;
- generic free-font choices used as product identity without a brief;
- technically clean but empty work with no product-specific point of view.

This is not a substitution checklist. Confirm the design has a coherent product-specific decision.

## Render matrix

At minimum inspect:

| Axis | Required cases |
| --- | --- |
| viewport | wide, 768px class, 320 to 390px narrow |
| zoom | 100 and 200 percent |
| content | normal, long English, CJK, mixed data |
| data | populated, empty, loading, error, unavailable, permission, partial or stale where relevant |
| state | hover, focus-visible, pressed, selected, disabled, busy, invalid |
| preference | reduced motion, forced colors or high contrast |
| input | pointer, keyboard, touch model where applicable |

Check horizontal overflow, clipping, scroll reachability, sticky collisions, target size, text measure,
focus visibility, and stable action placement in each relevant case.

## Keyboard matrix

- Tab and Shift+Tab through all interactive controls in DOM order.
- Space and Enter for buttons and choice controls.
- Arrow, Home, and End for tabs, radio, slider, select, menu, and command as their pattern requires.
- Escape for temporary layers and cancellation policy.
- Focus entry and return for menu, popover, dialog, confirmation, and command.
- Rapid repeat activation for async actions.
- Keyboard access to row secondary actions and horizontally scrolled content.
- IME composition without global-shortcut interference.

Record the expected and observed active element at each composite boundary.

## Accessibility pass

- landmarks, headings, labels, names, descriptions, roles, states, and relationships;
- focus order and visible focus;
- live-region urgency and update rate;
- target size and pointer cancellation;
- text, nontext, focus, and state contrast;
- reflow and text spacing at zoom;
- motion, flashing, and animation preference;
- error identification, recovery, and preserved input;
- screen-reader review for custom composites when available.

Automated scans support this pass but do not prove interaction or screen-reader quality.

## Console and runtime pass

- reload or restart after the final change;
- confirm the tested process serves the current source;
- inspect console errors, warnings, failed assets, and accessibility messages;
- verify no fixture mutates private or production data;
- test offline, slow, or failed async paths when applicable;
- distinguish current local proof from network, credentials, vendor, or device blockers.

## Deterministic validators

Run the repository validators and relevant project checks:

```bash
python3 scripts/validate_theme.py tokens/kokuen.tokens.json
python3 scripts/validate_contracts.py contracts
python3 scripts/lint_ui_rules.py .
```

Also run the official skill validator, build, typecheck, lint, unit/integration tests, and browser
fixtures supported by the repository. Do not report a command that was not run.

## Completion ledger

Record:

```text
Surface and revision tested:
Viewports and zoom:
Content fixtures:
Pointer interactions:
Keyboard interactions:
Focus entry, boundary, and return:
Accessibility tools and manual checks:
Forced colors and reduced motion:
Console and logs:
Token, contract, UI lint, build, type, and test results:
Figma coverage and known drift:
Exceptions and blocked proof:
Anti-slop findings fixed:
```

Do not call the work complete if a required row is blank.
