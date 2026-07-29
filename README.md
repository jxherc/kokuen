<h1 align="center">KOKUEN</h1>

<p align="center"><strong>A design operating system for product UI.</strong></p>

<p align="center">
  Coherent controls, spacing, interaction, accessibility, and verification<br>
  without forcing every product into the same visual theme.
</p>

<p align="center">
  <a href="SKILL.md">Skill</a> ·
  <a href="reference.md">Reference</a> ·
  <a href="designs/kokuen-visual-template/Universal%20UI%20Template.html">Visual template</a> ·
  <a href="https://www.figma.com/design/dMpK3ZOhraefh9L6m4BgBi">Figma</a>
</p>

## What KOKUEN does

KOKUEN gives an app one reliable contract for the interface that repeats everywhere: spacing,
controls, forms, navigation, command search, overlays, feedback, AI surfaces, accessibility,
tokens, and visual verification.

It does not prescribe a brand, palette, typeface, or component-library aesthetic.

> **KOKUEN owns recurring behavior. The product owns character.**

That boundary lets a product look completely like itself without every button, field, menu, and
state behaving as if it came from a different system.

## Install

Clone KOKUEN into the Codex skills directory:

```sh
git clone https://github.com/jxherc/kokuen.git ~/.codex/skills/kokuen
```

Then invoke it directly:

```text
Use $kokuen to design and verify a coherent, accessible product UI surface.
```

## The contract

KOKUEN protects six things across a product:

1. **Product character stays product-specific.** No mandatory grayscale theme, accent color, font,
   radius, dashboard layout, or material treatment.
2. **Shared geometry stays disciplined.** Use the spacing scale
   `0, 4, 8, 12, 16, 24, 32, 48, 64` and a 44px default interactive target.
3. **Common controls stay real.** Buttons, fields, selection controls, menus, dialogs, command,
   feedback, and async actions receive complete keyboard, focus, disabled, error, and recovery
   behavior.
4. **Actions stay close to what they change.** Never stretch a field across spare width and strand
   `Clear`, `Edit`, validation, or another field action at the far edge.
5. **Content remains visible by default.** Motion can support state and causality, but an animation
   cannot decide whether content exists.
6. **Rendered behavior is the proof.** Source, screenshots, tests, and Figma are supporting evidence.
   The final delivery surface must still be opened, exercised, and inspected.

## Workflow

| Stage | Decision | Primary artifact |
| --- | --- | --- |
| 1. Brief | Define the product, users, tasks, visual character, density, and constraints | [Custom-theme brief](docs/CUSTOM_THEME.md) |
| 2. System | Map primitive values to semantic roles and component decisions | [Design tokens](tokens/kokuen.tokens.json) |
| 3. Contract | Specify anatomy, states, keyboard behavior, content, and responsive rules | [Component contract](docs/COMPONENT_CONTRACT_TEMPLATE.md) |
| 4. Build | Reuse the product stack and apply KOKUEN behavior without importing a generic skin | [Skill workflow](SKILL.md) |
| 5. Prove | Exercise real states at representative sizes in the delivery surface | [Verification reference](reference.md) |

Validate the token graph before handoff:

```sh
python3 scripts/validate_theme.py tokens/kokuen.tokens.json
```

## Universal system, product-specific result

| Layer | KOKUEN decides | The product decides |
| --- | --- | --- |
| Foundations | semantic token roles, spacing scale, control geometry | palette, typography, density, radius, material |
| Primitives | anatomy, states, focus, keyboard behavior | labels, icons, visual treatment |
| Patterns | field recovery, collections, command/search, overlays, feedback | task flow and information hierarchy |
| Screens | responsive and accessibility review requirements | composition, content, brand character |

## Repository map

| Artifact | Use it for |
| --- | --- |
| [`SKILL.md`](SKILL.md) | Designing, implementing, or auditing product UI with KOKUEN |
| [`reference.md`](reference.md) | Exact component, accessibility, command, overlay, data, AI, and QA contracts |
| [`docs/CUSTOM_THEME.md`](docs/CUSTOM_THEME.md) | A new theme, rebrand, or substantial visual direction |
| [`docs/SPACING.md`](docs/SPACING.md) | Screen composition, proximity, field width, and responsive spacing |
| [`docs/COMPONENT_CONTRACT_TEMPLATE.md`](docs/COMPONENT_CONTRACT_TEMPLATE.md) | Promoting a primitive into the shared system |
| [`tokens/kokuen.tokens.json`](tokens/kokuen.tokens.json) | Portable primitive, semantic, and component decisions |
| [`kokuen.css`](kokuen.css) | A no-build semantic baseline, not a mandatory product skin |
| [`preview.html`](preview.html) | Lightweight interaction and component behavior checks |
| [Universal UI template](designs/kokuen-visual-template/Universal%20UI%20Template.html) | Product-neutral visual and interaction stress testing |
| [`scripts/validate_theme.py`](scripts/validate_theme.py) | Token type, alias, and reference validation |

## Definition of done

A KOKUEN implementation is ready only when:

- semantic tokens are valid and every alias resolves;
- changed controls include their required states and keyboard behavior;
- focus enters, remains within, and returns from overlays correctly;
- spacing, action proximity, contrast, and hierarchy survive realistic content;
- narrow layouts, long strings, empty states, errors, loading, and reduced motion are covered;
- no content is clipped, obscured, or dependent on an entrance animation;
- the latest rendered surface has been inspected and every changed interaction has been exercised.

## Figma

The [KOKUEN Figma file](https://www.figma.com/design/dMpK3ZOhraefh9L6m4BgBi) is a review and
specification companion. Code and rendered behavior remain the delivery source of truth.

## License

[MIT](LICENSE)
