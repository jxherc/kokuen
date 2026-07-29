# Boundaries, bezels, and focus geometry

Read this reference before adding a border, background shell, divider, clipping container, card,
focus ring, or inset control.

## Boundary law

A boundary is a visual or physical edge that makes a region read as separate. Borders, surface
changes, shadows, clipping, inset fills, strong radii, and surrounding focus rings can all create a
perceived boundary even when no CSS `border` exists.

Every visible boundary must name exactly why it exists:

| Job | Legitimate use | Typical evidence |
| --- | --- | --- |
| Input affordance | marks the editable or activatable region | field, button, switch track |
| State | communicates focus, invalid, selected, or unavailable | focus ring, error edge |
| Containment | binds children into one interactive or semantic object | command dialog, composite field |
| Clipping | constrains media, scrolling, or a shaped viewport | image crop, scroll region |
| Separation | prevents adjacent content from being confused | table header boundary, modal scrim |

If the edge has no job in this table, remove it.

## One control, one perceived boundary

At rest, a user should see one region to click or edit. On focus, that same region gains one focus
geometry. Common failures:

- bordered wrapper plus bordered input;
- input border plus inset shadow plus outer focus ring with different radii;
- search shell spanning the row while the actual input occupies only part of it;
- button inside a bordered field that draws a second unrelated rectangle;
- card around a form section whose fields already establish containment;
- outline on a grid cell instead of the actual interactive control.

Choose the component owner before styling:

1. If the wrapper owns prefixes, input, and end action as one composite, the wrapper owns the resting
   boundary and focus-within geometry. Children have no independent border or outline.
2. If controls are independent, each owns its boundary and focus. Do not add a shared wrapper edge.
3. If the input alone is the control, its width and focus geometry stop with the input.

## Whole-silhouette state

Apply state to the complete object the user perceives.

- For an already contained box, row, toast, card, or control, change the full perimeter, the full
  surface tone, the content treatment, or a combination of those signals.
- Never thicken or recolor only the left, right, top, inline-start, or inline-end edge as an accent
  rail for focus, selection, status, validation, or completion.
- Keep perimeter width and radius continuous around all sides. A state must not look stapled onto the
  component after the component was designed.
- Preserve a written, symbolic, or programmatic state cue so color is not the only signal.
- If a full state border is too loud, keep the neutral perimeter and use a restrained full-surface
  tonal shift plus explicit state copy. Do not fall back to a side bar.

A line-only field or tab may use its single baseline because that line is the control's entire
resting affordance. It must not sit inside another complete border. Structural rails, timelines, and
table separators require a non-state boundary job and must not masquerade as selection or status.

## Focus geometry

Focus must be perceivable without being mistaken for a resting border.

- Use `:focus-visible` for keyboard focus. Do not suppress focus without a replacement.
- For line-based fields, the resting edge yields while focus is visible so the focus outline becomes
  the only perceived boundary. Invalid focus may recolor that outline; it must not add another.
- Make the change at least 2 CSS pixels thick in aggregate or provide an equivalent visible area.
- The focused and unfocused appearance must differ by at least 3:1 where the focus indicator relies
  on color contrast.
- Keep the indicator outside or inside the same component silhouette. Do not combine mismatched
  wrapper and child shapes.
- The indicator must not be clipped by `overflow: hidden`, sticky headers, dialogs, or adjacent layers.
- Focus follows the 44px target, not only a 16px glyph.
- In forced colors, use system colors or a preserved outline; never depend on a box shadow alone.
- Pointer focus may be quieter only if keyboard focus remains unmistakable.

Use a documented exception when a browser-native text caret supplies input focus but retain a visible
field state for low vision and keyboard orientation.

## Width behavior

Every component contract names its width model:

- **content:** button or chip follows its label with bounded padding;
- **bounded:** field or select has an intentional inline size and maximum;
- **container:** control fills a known parent region because the task needs that width;
- **viewport service:** command/search/composition spans the designated working width;
- **responsive switch:** model changes at a named breakpoint, such as bounded field to full width.

`width: 100%` is not a default. It is a declared behavior. A full-width field must serve full-row
content, search, command, composition, or narrow-screen adaptation.

## Field-action proximity

Clear, reveal, edit, validation, browse, and unit actions remain visually and operationally attached
to their value.

- Put an end affordance inside a composite field when it acts on the field value.
- Place an independent action immediately beside a bounded field when it has its own label and focus.
- Move complex recovery or explanation below the field rather than across the row.
- Do not use flexible grid space to push an action to a distant edge.
- Keep the action reachable at 200 percent zoom without horizontal hunting.

The field and action may have separate focus indicators while sharing one resting composite boundary.
The wrapper must not add a third focus rectangle.

## Containers and cards

A card is appropriate only when the content is movable, selectable as one item, repeated as a peer,
or requires independent containment. It is not a default section wrapper.

- Prefer section spacing and aligned starts for ordinary page structure.
- Do not place a bordered card inside another same-level bordered card.
- Do not wrap a single field, button row, or heading in a card for visual interest.
- Avoid uniform cards when the content has unequal hierarchy.
- A tonal surface shift may establish a working region, but it still needs a containment job.
- Elevation must follow a declared layer model. No all-around shadow by default.

## Dividers

Use a divider only when spacing cannot prevent two adjacent regions from being misread as one.

- Prefer 24 to 48px separation for section changes.
- A table rule supports row or header scanning; a line under every label does not.
- Avoid isolated decorative hairlines.
- When a rule is necessary, align it to the content system and ensure it does not imitate focus.
- Do not use multiple nearby tone, border, and shadow changes to perform the same separation.

## Overlays and layers

Dialogs, menus, popovers, and command surfaces need containment because they occupy a distinct layer.

- Use one surface boundary and a scrim or anchoring relationship, not stacked glowing shells.
- A scrim separates interaction layers; its opacity must preserve sufficient context without making
  underlying controls appear active.
- The overlay edge must not clip its focus ring or live content.
- Menus and popovers align to their trigger or a named anchor.
- Toasts use placement and surface tone for separation. A status may change the full toast perimeter
  or full surface, never one colored edge. Do not add a decorative card inside the toast.

## Do and do not fixtures

The visual specimen and Figma library must include paired examples for:

1. one composite field boundary vs wrapper plus input borders;
2. focus around the actual field vs focus around unused row width;
3. bounded field with proximal action vs stretched field with stranded action;
4. grouped content using space vs every group inside a card;
5. one dialog surface vs multiple nested modal shells;
6. 44px icon target vs focus only around the glyph.

Bad examples are noninteractive or explicitly labelled as diagnostic. Never leave broken behavior in
a specimen where it could be mistaken for the recommended implementation.

## Audit procedure

For each visible edge:

```text
Element:
Boundary mechanism: border / tone / shadow / clip / radius / focus
Declared job:
Owner:
Resting geometry:
Focused geometry:
Width model:
Nested same-level boundary present: yes / no
Could spacing or alignment do the job: yes / no
Forced-colors behavior:
Evidence fixture:
```

Remove the edge when the job is blank, duplicated, or better solved by layout.

## Exceptions

An exception records the component, job, user benefit, why a simpler geometry failed, modes affected,
and rendered evidence. “Looks better,” “matches the kit,” or “makes it feel premium” is not a reason.
