# Spacing, layout, and proximity

Read this reference for any component or screen composition.

## Scale

Layout uses `0, 4, 8, 12, 16, 24, 32, 48, 64` CSS pixels. The scale applies to gaps, padding,
margins, gutters, and layout offsets. Optical construction may use 1px edges, 2px focus rings, or
measured icon corrections, but those values do not become general layout spacing.

| Value | Relationship |
| ---: | --- |
| 4 | tightly coupled mark and detail; rare optical grouping |
| 8 | icon to label, label to field, adjacent compact controls |
| 12 | dense row internals, compact composite padding |
| 16 | field to field, ordinary stack, narrow gutter minimum |
| 24 | related group padding, page gutter, peer group separation |
| 32 | header to first work, major internal subdivision |
| 48 | section transition |
| 64 | major page or task transition |

Use the smallest value that preserves comprehension and target separation. Do not use a fresh number
because one sample looks slightly off.

## Relationship before number

Name the relationship before choosing the token:

```text
Objects:
Relationship: same control / same field / peer control / same group / new section / new task
Required target clearance:
Content stress:
Responsive behavior:
Chosen token and semantic alias:
```

If the relationship changes at a breakpoint, record both modes. Do not patch one viewport with an
arbitrary margin.

## Alignment

Every edge aligns to one of these systems:

- viewport or page gutter;
- content column;
- component boundary;
- text baseline;
- data column;
- intentional optical axis.

“Almost aligned” is a defect. Repeated elements share exact starts, widths, internal padding, and
baselines. A local optical correction belongs inside the icon or glyph, not in the page grid.

## Proximity

Proximity communicates ownership before borders do.

- Label to control: 8px.
- Hint or error to its control: 8px.
- One complete field to the next: 16px.
- Inline field action: 8px from the value region or inside the end affordance.
- Controls in one action cluster: 8px.
- Related content groups: 16 or 24px.
- Header to first work: 32px.
- Sections: 48px.
- Major task areas: 64px.

Do not let flexible space separate a field from its action, a label from its value, an error from its
cause, or a row action from its row.

## Control size and target spacing

- Default hit target: at least 44 by 44 CSS pixels.
- Text button height: 44px minimum, with 12 to 16px inline padding.
- Icon mark: commonly 16 to 20px inside a 44px target.
- Input, select, tab, menu item, pagination button, and row action: 44px minimum.
- Adjacent targets need clear visual ownership and at least 8px separation unless one documented
  composite handles target boundaries.
- Do not create a 28 to 36px “compact” variant that shrinks the hit target. Compact density changes
  content spacing within the 44px target.

## Width and measure

Width follows content and task:

- Body copy: use a readable measure, usually 45 to 75 characters.
- Short field values: bounded field, not full-row expansion.
- Search, command, and composition: may use the working width.
- Buttons: content width unless the platform or task needs equal-width actions.
- Tables: preserve readable columns, then scroll or change representation rather than squeezing.
- Dialogs: size to the decision and content, with viewport gutters preserved.

Define `min`, preferred, and `max` behavior. Test long content before adding truncation. Truncation is
acceptable only when the full value is available through another accessible path.

## Responsive composition

Responsive work preserves hierarchy, not only fit.

1. Keep a minimum 16px page gutter on narrow screens.
2. Collapse columns before gaps or controls shrink below contract values.
3. Keep primary action placement stable when possible.
4. Convert dense tables to horizontal scroll, priority columns, or an alternate row pattern. Do not
   silently hide essential data.
5. Reflow field actions with their field; never leave them on the former row edge.
6. Keep dialog content within viewport and maintain access to close and final actions.
7. Test 320px CSS width and 200 percent zoom at a desktop viewport.
8. Avoid fixed heights around text and controls.

## Density

Density is independent from color and contrast. Define it through semantic tokens:

```text
density comfortable: 44px control, 12 or 16px internal gaps, 16px row rhythm
density compact: 44px target, tighter visible mark and copy rhythm, unchanged semantics
```

Do not reduce essential text, focus area, or hit target to achieve density. Dense data may reduce
vertical whitespace around noninteractive content while actions retain accessible targets.

## Repeated and parallel content

Peer components share the same grid. When columns are compared, titles, values, descriptions,
content starts, and actions align across rows regardless of copy length. Reserve space or use a
shared layout rather than letting the longest string move only one column's actions.

Avoid card grids as a universal solution. Use tables, lists, spatial canvases, or task-specific
compositions when they better express the relationship.

## CJK and localization stress

- Test unbroken strings and scripts with different glyph metrics.
- Do not use letter spacing as a universal label treatment.
- Allow labels to wrap or allocate enough inline measure.
- Keep vertical rhythm when fallback fonts have taller glyph boxes.
- Avoid fixed row heights for multi-line content; use minimum heights.
- Verify icon and text alignment with actual fallback fonts.

## Spacing audit

1. Search source for raw layout values outside the scale.
2. Map each exception to a semantic token and reason.
3. Overlay repeated component starts and target boxes.
4. Inspect at wide, narrow, and 200 percent zoom.
5. Load long English and CJK fixtures.
6. Check that errors and helper text do not collapse group rhythm.
7. Check that no negative margin repairs a parent layout.
8. Remove borders or dividers whose job is already done by spacing.
