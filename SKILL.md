---
name: kokuen
description: >-
  Design, implement, or audit professional product UI with KOKUEN. Use for shared UI foundations,
  spacing systems, common components, universal command/search, AI surfaces, Figma libraries, visual
  redesigns, and accessibility or rendered-UI reviews. Enforces explicit geometry, states, keyboard
  behavior, Figma/code parity, and evidence-based visual QA.
---

# KOKUEN: professional universal product UI

KOKUEN is a strict operating skill for the reusable parts of a product UI. It is not a theme, a
grayscale prescription, or a generic landing-page kit. A product chooses its own character, palette,
type, and imagery. KOKUEN makes its common controls, spacing, states, behavior, and review process
coherent.

## Authority and required reading

1. Current product source and rendered behavior outrank this repository.
2. Read `docs/CUSTOM_THEME.md` before defining or replacing a product visual language.
3. Read `docs/SPACING.md` for every screen or component composition.
4. Read `reference.md` for components, command, Figma, and delivery requirements.
5. Read the relevant product rules before adding a library or changing interaction.
6. Do not claim completion from a source diff, Figma frame, mockup, or unit test alone.

## Trigger and scope

Use KOKUEN when a request involves a product screen, design system, common UI, visual refactor,
button/input/control, navigation, form, list/table, overlay, feedback, universal search/command,
AI surface, Figma component library, or visual quality review.

Do not use it to impose a house palette or rebuild product-specific identity. The universal layer
stops at the shared interaction and geometry contract. Brand decisions remain product decisions.

## Custom-theme contract

For a new theme or visual rebuild, work in this order:

1. Write the one-page theme brief in `docs/CUSTOM_THEME.md`: user/job, product character, visual
   medium, type role, color roles, geometry, motion, icon/asset direction, explicit anti-references.
2. Create primitive tokens only for raw values, then semantic tokens for meaning, then component
   tokens for a stable component-specific decision. Never let component CSS consume a raw color or
   arbitrary spacing value directly.
3. Put the token source in `tokens/kokuen.tokens.json`. It follows the DTCG shape: `$value`, `$type`,
   aliases, and token groups. The shipped values are an editable schema and neutral starter, not a
   brand prescription.
4. Prove the direction through a representative stress set before expanding it: primary and quiet
   button, field with error, selection control, command/dialog, dense row or table, feedback, and a
   real product screen. A theme is not approved from a hero alone.
5. Bind Figma variables and code variables to the same semantic names. Document unavoidable drift.
6. Record the type and asset source, license, version, fallback behavior, and localization coverage.
   A distinctive display face does not excuse broken CJK, long-name, data, error, or fallback text.
7. Define component contracts with stable IDs, anatomy, variants, states, token dependencies,
   keyboard/focus behavior, accessible naming, localization constraints, code path, and Figma key.
8. Run `python3 scripts/validate_theme.py tokens/kokuen.tokens.json` before handoff. It catches
   malformed token objects, missing types/values, unresolved aliases, alias cycles, and token-type
   mismatches.

Use `docs/CUSTOM_THEME.md` for the detailed process, source-of-truth map, designer review questions,
theme handoff format, and QA matrix. Use `docs/COMPONENT_CONTRACT_TEMPLATE.md` whenever a primitive
becomes stable. Do not copy a moodboard, a component library, or a reference product's visual identity.
Extract a design principle and make the product-specific decision yourself.

## Automatic companion-skill routing

KOKUEN is the governing workflow, not an isolated style prompt. On every KOKUEN task, select the
smallest companion set below and follow it automatically when available. Do not load every skill by
default: that wastes context and creates contradictory art direction.

| Situation | Automatically use | What it contributes |
| --- | --- | --- |
| Any visual decision or redesign | `human-taste` | brief, product-specific visual judgment, final critique |
| New or substantially reshaped interface | `frontend-design` | distinctive art direction and non-generic composition |
| Production UI/component implementation | `frontend-ui-engineering` | component architecture, responsive behavior, accessibility, state management |
| Need a targeted pattern, UX rule, or stack-specific research | `ui-ux-pro-max` | query its local database on demand; read only the matching result/reference |
| Mockup, standalone prototype, visual exploration, or `.fig` import | `baoyu-design` | artifact workflow, local preview, import and design-system scaffolding |
| Figma library, screen, or token mutation | `figma:figma-use` + appropriate Figma skill | variables, variants, component/library or screen creation |
| Final visual/interaction validation | `webapp-testing` + `verification-before-completion` | actual rendered behavior and evidence discipline |

Routing rules:

1. `human-taste` is the default visual auditor. It does not replace product rules or KOKUEN geometry.
2. Use **one** primary art-direction skill: `frontend-design` for new/rebuilt composition or
   `baoyu-design` for a design artifact/prototype. Do not use both as independent visual authorities.
3. `frontend-ui-engineering` complements either primary direction whenever production UI code changes.
4. Use `ui-ux-pro-max` narrowly: query a concrete uncertainty such as `form validation`, `responsive
   data table`, or `command palette`. Do not run its full generic design-system generator over an
   established product unless the owner explicitly requests a new product direction.
5. Existing project identity, user directions, and KOKUEN spacing/accessibility contracts outrank any
   imported recommendation. Reject a recommendation that conflicts with them.
6. Announce the selected companion skills and why before taking visual action. At completion state how
   each materially affected the result.

## Non-negotiable operating sequence

### Gate 0: establish the real problem

Before editing, inspect the smallest relevant set of source files, existing component APIs, tests,
current rendered surface, and any user-provided references. Write a compact design map:

```text
Primary user / job:
Primary action:
Secondary actions:
Content hierarchy:
Required data states:
Keyboard and focus model:
Viewport constraints:
Existing primitives to reuse:
Product-specific visual decision:
```

If an answer is unknown, inspect. Do not fill it with generic dashboard copy, fake metrics, or a
decorative component that cannot work.

### Gate 1: choose the system boundary

Classify the work before making a component:

| Class | Use when | Required output |
| --- | --- | --- |
| Foundation | repeated visual rule | semantic token and usage rule |
| Primitive | one focused behavior | accessible component and state matrix |
| Pattern | multiple primitives solve one job | composition, data states, responsive behavior |
| Product screen | real task flow | rendered interaction proof |
| Figma artifact | review/specification is needed | variables, variants, and a real usage frame |

Never turn a product-specific one-off into a global primitive without at least two credible reuse
contexts. Never make a new primitive when an existing one can be extended with a stable variant.

### Gate 2: compose with spacing, not guesses

Use **only** `0, 4, 8, 12, 16, 24, 32, 48, 64` for layout gaps, padding, and margins. Do not introduce `10`, `14`,
`18`, `20`, `22`, `28`, `36`, or `40` because they look close. An internal control drawing may use a
necessary optical measurement such as a 1px border or 2px focus outline; it must not become a layout
spacing value. If an exception is truly required,
create a semantic token, record its purpose, and reuse it consistently.

| Relationship | Required token |
| --- | --- |
| icon ↔ label | 4 or 8 |
| adjacent compact controls | 8 |
| label ↔ input / hint ↔ input | 8 |
| form field ↔ form field | 16 |
| related content groups | 16 |
| card padding / sibling cards | 24 |
| header ↔ first work block | 32 |
| sections | 48 |
| major page blocks | 64 |

Rules:

- Default interactive hit area: 44×44px or larger. The visible mark may be smaller.
- A repeated row uses one height, one horizontal padding, and one gap. No item-by-item corrections.
- A card family shares padding, corner geometry, and internal rhythm. Do not fix unequal card actions
  with random top margins.
- Page gutters use one responsive token. Components may not invent viewport margins.
- Collapse columns before a gap falls below 16px on narrow screens.
- Align to a page gutter, a column, or a container edge. "Almost aligned" is a bug.
- No negative margins for layout correction. Rework the parent geometry instead.

### Gate 3: build every state before polish

For every primitive or pattern, create the state matrix before final styling:

| Category | Required states |
| --- | --- |
| Button | default, hover, focus-visible, pressed, loading, disabled, destructive if applicable |
| Field | label, placeholder, filled, focus, hint, invalid, disabled, read-only where needed |
| Choice control | checked, unchecked, focus-visible, disabled, indeterminate where applicable |
| List / row | default, hover, active, selected, empty, loading, error, unavailable |
| Overlay | trigger, opening/open, focus boundary, Escape, outside interaction policy, close, return focus |
| Async / AI | idle, pending, streaming, completed, cancelled, error, retry, permission-boundary |

Do not use color as the only differentiator. Every state needs a combination of wording, position,
shape, iconography, value, or semantic state so it survives low vision and color blindness.

### Gate 4: preserve accessible native behavior

Use native HTML whenever it supplies the interaction. If the product needs a custom visual, preserve
its semantic contract or provide the correct ARIA pattern.

- Buttons perform actions. Links navigate.
- Rows are buttons or links when actionable, never clickable `div`s.
- Form labels have programmatic association; help and errors are associated with their fields.
- Controls expose disabled state, visible focus, and keyboard behavior.
- Custom checkbox/switch/radio uses a real `<button>` plus appropriate role and ARIA state.
- A custom select is a trigger plus listbox. It supports Arrow keys, Home, End, Enter, Escape,
  disabled options, typeahead where relevant, and focus restoration.
- A dialog is labelled, modal when necessary, owns focus while open, and restores focus to its opener.
- Respect `prefers-reduced-motion`. Content is visible before any animation runs.

Never ship browser-default select, checkbox, radio, range, or context-menu UI in products that require
custom KOKUEN controls. Never hide live content behind an entrance animation.

## Universal component contract

### Foundations

Define semantic tokens, not a mandatory visual palette:

```css
--ui-canvas --ui-surface --ui-text --ui-muted --ui-border --ui-border-strong
--ui-focus --ui-error --ui-success --ui-space-* --ui-control-height
--ui-page-gutter --ui-content-max --ui-radius-control --ui-radius-container
```

One project may map these to warm paper; another may map them to a dark editorial system. The names,
spacing scale, and component API stay stable.

### Actions

- One clear primary action per decision point unless there is a documented equal-priority decision.
- Button label starts with a verb and names the outcome: `Save changes`, not `Continue`.
- Loading replaces ambiguity with an explicit busy state and prevents duplicate action.
- Destructive action describes its consequence and uses confirmation when recovery is costly.
- Icon-only actions need an accessible name and a tooltip only when the icon is not universally clear.
- Hover changes tone, border, or icon treatment. Buttons and cards do not jump upward or scale.

### Fields and forms

- A field group is: label → field → hint or error. The default gaps are 8px / 8px / 16px.
- **Field-action proximity is non-negotiable.** Never let a full-width input push `Clear`, `Edit`,
  validation, or any secondary field action to the far edge of a row. A field action either sits
  inside the field's end affordance, immediately beside a deliberately bounded field, or moves to
  its own clearly labelled row. A control that visually separates typed text from its action is a
  layout bug, even if its CSS grid technically aligns.
- A lone text field must have a deliberate readable maximum width. Full-bleed fields are reserved
  for search, command, or genuinely full-row data entry, never used merely because a grid column
  happens to be available.
- Errors explain recovery: `Enter a project name`, not `Invalid input`.
- Preserve input text after a failed submit unless security requires clearing it.
- Required is semantic, not only an asterisk. Disabled means unavailable, not loading.
- Use a textarea for multi-line intent. Do not fake a textarea with a growing single-line input.
- Put validation next to the failing field; use a summary only for long forms or after submit.

### Navigation, collections, and data

- Active navigation uses `aria-current` or the selected tab state, not a decorative dot.
- A tablist changes views without leaving the context; navigation changes location. Do not conflate them.
- Rows have one clear click target. Secondary actions remain reachable by keyboard.
- Tables preserve header association, numeric alignment, empty/loading/error states, and a narrow-screen
  fallback. Do not squeeze a dense table until it is unreadable.
- Pagination exposes current page and unavailable previous/next actions.

### Menus, overlays, and feedback

- Menu triggers announce state; menus close with Escape and return focus to their trigger.
- Use a dialog for consequential confirmation, not a toast. Use a toast for non-blocking feedback.
- A tooltip supplements a control; it never supplies its only label.
- Empty states explain why nothing is shown and expose the one useful next action.
- Loading state preserves layout where possible. Skeletons mirror final content shape and are not
  decorative animation.

### Universal command

Universal command is a product service, not a decorated input. It can provide navigation, search,
creation, contextual actions, and bounded AI actions through one keyboard-first dialog.

Required implementation:

1. One labelled dialog, one autofocus input, one listbox.
2. Group labels are presentational. Do not nest listboxes.
3. Options are semantic buttons with `role=option`; exactly one is active/selected.
4. Input owns `aria-activedescendant`.
5. Arrow keys move active result; Home/End jump; Enter invokes; Escape closes and returns focus.
6. Filtered results retain the same model.
7. Loading, empty, error, unavailable, and no-permission content exist in the same surface.
8. AI actions state scope and effect before execution. No invented completion.

## AI surface rules

- State whether an answer is generated, grounded, streaming, incomplete, or failed.
- Keep user text distinguishable from assistant output; preserve selection and copy affordances.
- Give Stop/Cancel a stable location during streaming.
- Require confirmation before actions with external or irreversible impact.
- Show citations, sources, or affected scope where the product can provide them.
- Never use an animated cursor, glow, or speculative status as proof that work succeeded.

## Figma requirements

Use Figma as an inspectable contract, not an isolated image.

1. Audit file/page/component state before writing.
2. Create semantic variables before components.
3. Create a component set for each stable primitive; variants map to code states.
4. Document default, focus, disabled, error, loading, and selected states in the library.
5. Include one actual product screen demonstrating the library in context.
6. Create Code Connect mappings only after the code API and Figma component API are stable.
7. Keep Figma and code differences explicit. Do not silently let one drift.

For Figma work, load `figma:figma-use` and `figma:figma-generate-library`. For screen composition also
load `figma:figma-generate-design`. If the platform blocks writes, record the exact limitation and
continue with code; do not pretend the missing Figma work exists.

## Visual quality review

Review at desktop and narrow viewport, at 100% zoom, in the actual target surface. Check:

- page gutters, baseline alignment, repeated gaps, card padding, and control heights;
- text wrapping, overflow, truncation, clipped edges, and empty space caused by failed layout;
- contrast, focus ring, pressed/disabled/error states, and icon labels;
- every changed pointer and keyboard interaction;
- command focus entry, active navigation, Escape, Enter, and focus restoration;
- motion-disabled behavior and content visibility;
- console errors and stale render/build state.

Run a final spacing pass specifically searching raw spacing values outside the scale. If a value is
not a token, replace it or document it as a deliberate semantic exception.

## Completion report

Do not say “done” while a required component state, visual check, or real interaction remains
unverified. Report separately:

1. changed foundations/components/patterns;
2. Figma coverage and any blocked write work;
3. rendered visual proof;
4. pointer and keyboard proof;
5. build, lint, type, test, and console proof;
6. known exclusions or external blockers.

## Repository map

- `docs/SPACING.md`: exact geometry and spacing review rules.
- `docs/CUSTOM_THEME.md`: custom-theme brief, token ladder, review, and handoff process.
- `docs/COMPONENT_CONTRACT_TEMPLATE.md`: stable component API and accessibility contract.
- `reference.md`: component inventory and accessibility contract.
- `tokens/kokuen.tokens.json`: editable DTCG-aligned token schema and neutral starter values.
- `scripts/validate_theme.py`: deterministic token and alias validation.
- `kokuen.css`: portable semantic CSS primitives.
- `preview.html`: interactive visual regression lab.
- `docs/KOKUEN_V3_BRIEF.md`: current product/library scope.
