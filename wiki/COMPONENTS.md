# Components

## Registry

`contracts/kokuen.components.json` contains 23 candidate contracts:

- actions: button and icon action;
- fields and choice: text field, textarea, checkbox, radio group, switch, slider, select/listbox;
- navigation and data: tabs, menu, row, table, pagination;
- overlays and feedback: tooltip, popover, dialog, confirmation, toast, and reusable state;
- universal command;
- AI composer and response.

Each record defines user job, code API, Figma mapping, anatomy, variants, states, tokens, boundary and
width behavior, accessibility, keyboard, focus, pointer/touch, disabled and busy behavior, content,
responsive behavior, data states, fixtures, and exceptions.

## Status model

- `draft`: incomplete contract or architecture.
- `candidate`: complete written/code contract with evidence still pending.
- `stable`: code, Figma component key, and rendered fixture proof agree.
- `deprecated`: retained only with migration or replacement guidance.

The v5 registry intentionally remains candidate because the remote Figma mapping is blocked. The
validator rejects a false stable claim when a mapped Figma component key is missing.

## Visual and code fixtures

The canonical specimen covers all 55 fixture IDs. `tests/test_visual_template.py` exercises target
measurement, fields, choices, slider, select, tabs, menu, data states, tooltip, popover, dialog,
confirmation, command, AI streaming and Stop, theme, focus, reflow, forced colors, and reduced motion.

The three forward fixtures are not reusable components or starter screens. They prove the same
contracts can support writing, operational data, and consumer media without sharing one aesthetic.

## Figma mapping

`figma/kokuen.library.json` maps every component ID to its intended Figma name and independent public
properties. Remote component keys stay `null` until the real file is written and inspected. Code
Connect stays deferred until contracts become stable.
