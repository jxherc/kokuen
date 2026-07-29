# KOKUEN reference index

KOKUEN v5 keeps the entry skill concise and loads professional rules by task. Start with
[`SKILL.md`](SKILL.md), then open only the references relevant to the work.

| Work | Reference |
| --- | --- |
| Product direction and universal boundary | [`visual-grammar.md`](references/visual-grammar.md) |
| Borders, cards, focus, containment, field width | [`boundaries-and-bezels.md`](references/boundaries-and-bezels.md) |
| Layout, proximity, target size, responsive behavior | [`spacing-and-layout.md`](references/spacing-and-layout.md) |
| Type roles, modes, color, contrast, CJK | [`typography-and-color.md`](references/typography-and-color.md) |
| Buttons, icon actions, busy and destructive actions | [`buttons-and-actions.md`](references/buttons-and-actions.md) |
| Fields, textarea, checkbox, radio, switch, slider, select | [`forms-and-input.md`](references/forms-and-input.md) |
| Navigation, tabs, rows, tables, pagination | [`navigation-and-data.md`](references/navigation-and-data.md) |
| Menu, tooltip, popover, dialog, toast, command | [`overlays-and-command.md`](references/overlays-and-command.md) |
| Generation, streaming, sources, approval, stop/cancel | [`ai-surfaces.md`](references/ai-surfaces.md) |
| Variables, components, documentation, code mapping | [`figma-contract.md`](references/figma-contract.md) |
| Render, keyboard, accessibility, anti-slop, completion | [`qa-and-antipatterns.md`](references/qa-and-antipatterns.md) |

## Machine-readable contracts

- [`kokuen.tokens.json`](tokens/kokuen.tokens.json): 118-token primitive, semantic, component, and
  mode contract.
- [`kokuen.components.json`](contracts/kokuen.components.json): 23 candidate common-component
  records with state, boundary, keyboard, content, Figma, and fixture requirements.
- [`kokuen.library.json`](figma/kokuen.library.json): validated Figma collection, page, component,
  review-frame, and remote-ID synchronization ledger.
- [`KOKUEN_V5_MASTER_PLAN.md`](docs/KOKUEN_V5_MASTER_PLAN.md): architecture and acceptance gates.
- [`FORWARD_TESTS.md`](docs/FORWARD_TESTS.md): product-neutrality proof across three unrelated briefs.
- [`ANTI_SLOP_AUDIT.md`](docs/ANTI_SLOP_AUDIT.md): final point-by-point visual quality audit.

## Validation

```bash
python3 scripts/validate_theme.py tokens/kokuen.tokens.json
python3 scripts/validate_contracts.py contracts
python3 scripts/validate_figma_manifest.py
python3 scripts/lint_ui_rules.py kokuen.css preview.html designs/kokuen-visual-template tests/forward-fixtures
```

The HTML specimen and Figma library demonstrate the contract. Only the current rendered product
surface proves delivery behavior. See [`FIGMA_SYNC.md`](docs/FIGMA_SYNC.md) for current remote status.
