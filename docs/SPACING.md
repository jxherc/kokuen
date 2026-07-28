# KOKUEN spacing contract

AI does not get to pick a fresh number because a gap looks almost right. Use the scale and name the relationship first.
This contract covers layout gaps, padding, and margins. Optical control construction may use necessary
measurements such as a 1px border or 2px focus outline, but those values must not leak into layout.

| Token | px | Use |
| --- | ---: | --- |
| `space-1` | 4 | icon-to-label, tiny internal correction |
| `space-2` | 8 | adjacent controls, compact rows |
| `space-3` | 12 | dense content |
| `space-4` | 16 | default stack gap, control padding |
| `space-5` | 24 | card padding, related groups |
| `space-6` | 32 | section subdivision, page header blocks |
| `space-7` | 48 | section separation |
| `space-8` | 64 | major page separation |

Use no other default pixel gaps. An exception needs a semantic token and a reason.

## Relationship rules

- Inside one control: 8 or 12px. Button height is `--ui-control-height` (44px by default).
- Label to field: 8px. Hint/error to field: 8px. Separate form fields: 16px.
- Field action proximity is part of spacing, not a cosmetic preference: `Clear`, `Edit`, validation,
  and inline field actions sit inside the end affordance or directly beside a deliberately bounded
  field. Never stretch an input across spare page width and leave its action marooned at the far end.
- Within one card: 24px padding; related child groups: 16px; individual lines: 8px.
- Between sibling cards: 24px. Page title to supporting copy: 8px. Header to first work: 32px.
- Sections: 48px. Major page transitions: 64px. Screen edge: `--ui-page-gutter`.

## Alignment rules

1. Align to the page gutter, card edge, or deliberate column. Never eyeball a near match.
2. A repeated layout has one gap token and one padding token. No per-item patching.
3. Cards in a grid share padding and vertical rhythm. Do not fix unequal actions with random margins.
4. Icon-only controls keep the same 44px target as text controls.
5. On narrow screens, collapse columns before squeezing gaps below 16px.

## Agent check

- Search for raw layout spacing values outside this scale; do not flag a documented optical drawing value.
- Compare repeated components side by side at 100% zoom.
- Check a narrow and wide viewport.
- Check text wrapping does not create unequal card/action alignment.
- Never compensate for a bad layout with negative margins.
