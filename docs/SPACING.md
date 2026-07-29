# KOKUEN spacing contract

The canonical v5 spacing, target, alignment, width, density, responsive, and localization rules live
in [`references/spacing-and-layout.md`](../references/spacing-and-layout.md). Boundary and focus
geometry live in [`references/boundaries-and-bezels.md`](../references/boundaries-and-bezels.md).

The invariant layout scale is:

```text
0, 4, 8, 12, 16, 24, 32, 48, 64
```

Every gap names a relationship. Optical 1px edges and 2px focus rings do not become layout tokens.
Every interactive target is at least 44 by 44 CSS pixels. A short-content field is deliberately
bounded; only search, command, composition, true full-row entry, or narrow responsive layout expands
it to the working width. Field actions remain inside the end affordance or directly beside the field.

Run `python3 scripts/lint_ui_rules.py ...` on changed UI source and resolve every spacing error and
boundary warning before handoff.
