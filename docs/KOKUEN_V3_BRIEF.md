# KOKUEN v3: universal UI template

## Purpose

KOKUEN is the reusable baseline for common product UI. It supplies coherent behavior and geometry,
not a single visual identity. Each product owns its palette, type, imagery, and character.

## Inventory

1. Foundations: semantic color, type roles, spacing, radii, focus, motion.
2. Actions: primary, secondary, quiet, destructive, loading, disabled buttons.
3. Inputs: text field, textarea, search, validation, helper text.
4. Selection: switch, checkbox, radio/listbox, slider.
5. Structure: app shell, page header, card/container, row/list, empty/loading/error.
6. Overlay: dialog, confirmation, toast.
7. Universal command: search, navigation, creation, contextual actions, bounded AI actions.
8. Figma library and one real product screen.

## Design rules

- Use the same spacing and control height across features.
- Prefer direct labels over icon-only ambiguity.
- Keep one clear primary action per decision point.
- Make state visible in wording and shape, not only color.
- Custom controls must be fully keyboard accessible.
- Content is visible by default; motion is optional refinement.
- The first product screen is a working index, never a generic marketing hero.

## Current artifacts

- Code baseline: `kokuen.css`
- Interactive proof: `preview.html`
- Component and accessibility contract: `reference.md`
- Figma file: https://www.figma.com/design/dMpK3ZOhraefh9L6m4BgBi

## Acceptance

The template is acceptable only when its components are reusable across differing project palettes,
all changed interactions work with pointer and keyboard input, and a real product screen demonstrates
the command surface without hiding actual work behind decorative UI.
