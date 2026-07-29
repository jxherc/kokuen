# Architecture

KOKUEN is a portable design operating system, not a runtime framework or mandatory visual theme.

## Source-of-truth flow

```text
product brief
  -> SKILL.md router and focused references
  -> tokens/kokuen.tokens.json
  -> contracts/kokuen.components.json
  -> kokuen.css and the functional visual specimen
  -> rendered browser proof

tokens + component contracts
  -> figma/kokuen.library.json
  -> remote Figma variables and components when synchronization is available
```

The current rendered product remains the delivery source of truth. Figma, screenshots, isolated
fixtures, validators, and source inspection are supporting evidence.

## Major artifacts

- `SKILL.md`: compact task router, authority order, invariants, and completion contract.
- `references/`: one-level professional guidance for visual grammar, foundations, common controls,
  navigation, overlays, command, AI surfaces, Figma, and QA.
- `tokens/kokuen.tokens.json`: 118 typed tokens, 49 aliases, six public modes across theme,
  contrast, and density, plus contrast-pair assertions.
- `contracts/kokuen.components.json`: 23 candidate component contracts and 55 deterministic fixture IDs.
- `kokuen.css`: no-build product-neutral reference implementation.
- `designs/kokuen-visual-template/Universal UI Template.html`: canonical visual and interaction specimen.
- `tests/forward-fixtures/`: three intentionally different product-direction fixtures used only to
  test KOKUEN's universal/product boundary.
- `figma/kokuen.library.json`: validated synchronization plan and remote ID ledger.

## Validation

- `validate_theme.py`: DTCG shape, types, aliases, cycles, modes, overrides, and contrast.
- `validate_contracts.py`: component completeness, tokens, states, keyboard, paths, and fixture coverage.
- `validate_figma_manifest.py`: token mode axes, component property mappings, remote claims, and source paths.
- `lint_ui_rules.py`: spacing, target, focus, content visibility, hover motion, native controls,
  button semantics, type, and likely boundary warnings.
- `test_visual_template.py`: browser interaction and rendered-state suite for the canonical specimen.
- `test_forward_fixtures.py`: browser proof that the same contracts preserve three product identities.
- `test_validators.py`: positive and negative validator regression tests.

## Remote Figma boundary

The canonical file key is `dMpK3ZOhraefh9L6m4BgBi`. The 2026-07-30 discovery attempt confirmed a
single top-level `Cover` page, then the Starter-plan MCP call limit blocked further reads and writes.
No remote variables, components, or keys are claimed. Resume from `docs/FIGMA_SYNC.md` and update the
manifest incrementally after every verified mutation.
