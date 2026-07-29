# Research basis

## Scope

KOKUEN v5 was checked against current primary standards, official design-system documentation, and
the README structure of established open-source UI projects. Research was reviewed on 2026-07-30.
The goal was not to copy a visual language. It was to turn established practice into explicit,
testable rules while preserving KOKUEN's product-neutral boundary.

## Standards and platform guidance

| Source | What it establishes | KOKUEN decision |
| --- | --- | --- |
| [Design Tokens Format Module 2025.10](https://www.designtokens.org/TR/2025.10/format/) | Stable exchange format concepts, typed values, groups, aliases, and design-tool interoperability. | Keep the token source DTCG-aligned, validate types and aliases, and separate portable data from CSS implementation. |
| [WCAG 2.2](https://www.w3.org/TR/WCAG22/) | Normative requirements for reflow, focus visibility and obscuring, non-text contrast, names and states, keyboard access, and target sizing. | Test reflow, 200 percent text/zoom equivalents, focus area and contrast, state semantics, and actual target measurements. |
| [Target Size (Enhanced)](https://www.w3.org/WAI/WCAG22/Understanding/target-size-enhanced.html) | The 44 by 44 CSS pixel enhanced target and documented exceptions. | Use 44px as KOKUEN's default invariant, while allowing only explicit platform or inline-text exceptions. |
| [ARIA APG keyboard interface](https://www.w3.org/WAI/ARIA/apg/practices/keyboard-interface/) | Composite widgets need managed focus, one tab stop, predictable arrow-key movement, and visible distinction between focus and selection. | Give radio, tabs, menu, listbox, and command one complete focus model rather than mixing roving focus and `aria-activedescendant`. |
| [ARIA APG patterns](https://www.w3.org/WAI/ARIA/apg/patterns/) | Purpose, semantics, keyboard models, and functional examples for common widgets. APG is informative, not a production design system. | Treat APG keyboard conventions as the interaction baseline, then verify the product implementation instead of copying examples as finished components. |
| [Figma variables, collections, and modes](https://help.figma.com/hc/en-us/articles/14506821864087-Overview-of-variables-collections-and-modes) | Variables can change by mode, alias to other variables, and publish through libraries. Mode limits depend on plan. | Separate theme, contrast, and density axes rather than multiplying combined themes. |
| [Figma component properties](https://help.figma.com/hc/en-us/articles/5579474826519-Explore-component-properties) | Boolean, text, instance-swap, slot, and variant properties expose a component's intended public controls. | Map independent Figma properties to the code API and document intended usage, states, and accessibility. |

WCAG is normative. APG examples and design-system documentation are guidance. KOKUEN records that
difference so an example is not mistaken for a compliance guarantee.

## Professional design-system references

| Source | Useful practice | Applied in v5 |
| --- | --- | --- |
| [Adobe Spectrum design tokens](https://spectrum.adobe.com/page/design-tokens/) | Tokens are decisions and communication, with global, alias, and component-specific scopes. Spectrum recommends aliases for intent and a focused token set. | Primitive values feed semantic roles; component tokens exist only for durable decisions. The validator rejects unknown aliases and type mismatch. |
| [Atlassian foundations](https://atlassian.design/foundations) | Foundations cover tokens, spacing, type, iconography, elevation, borders, radius, content, and accessibility as related systems. | KOKUEN separates foundation concerns and treats boundary, radius, and spacing as explicit relationships rather than decorative defaults. |
| [Atlassian design tools](https://atlassian.design/tools/) | Mature systems pair Figma libraries with code providers, lint rules, and theme testing. | KOKUEN includes token, contract, Figma-manifest, and UI-source validators plus rendered browser fixtures. |
| [GOV.UK Design System components](https://design-system.service.gov.uk/components/) | Reusable components include guidance, coded examples, and evidence about when to use them. | Every candidate contract includes user job, anatomy, states, behavior, content, accessibility, fixtures, and exceptions. |
| [GOV.UK extending components](https://design-system.service.gov.uk/get-started/extending-and-modifying-components/) | Extensions need isolated naming, accessibility review, and care not to break upstream behavior. | KOKUEN uses the `k-` namespace, favors extending stable primitives, and requires rendered regression proof. |

## README benchmarks

The README was benchmarked against projects with substantial real adoption, including
[shadcn/ui](https://github.com/shadcn-ui/ui), [Tailwind CSS](https://github.com/tailwindlabs/tailwindcss),
and [Radix Primitives](https://github.com/radix-ui/primitives). Their READMEs lead with a concise
definition, provide the shortest usable install path, send detailed reference material to dedicated
documentation, and avoid turning the repository landing page into the full manual.

KOKUEN follows that information hierarchy while adding the proof and boundary information its job
requires: what it owns, what the product owns, the first command to run, the contract map, and the
truthful status of Figma and rendered verification.

## Professional theme workflow distilled

A complete custom theme is not a palette swap. The professional sequence used by KOKUEN is:

1. Define the user, job, content, constraints, and existing identity.
2. Choose one visual world and explicit anti-references before selecting components.
3. Map primitive values to semantic roles and independent mode axes.
4. Establish spacing relationships, target geometry, type roles, boundary ownership, and motion.
5. Specify component anatomy, public properties, full states, content limits, keyboard, and focus.
6. Build real product compositions from the brief instead of stacking reusable page skeletons.
7. Align Figma variables and components with code contracts without claiming Figma as runtime proof.
8. Stress long content, CJK, narrow layouts, zoom, data failures, permissions, and reduced motion.
9. Exercise the real delivery surface with pointer and keyboard, inspect the render, and record gaps.

The three forward fixtures in [`FORWARD_TESTS.md`](FORWARD_TESTS.md) are the boundary test: the same
professional contracts produce different product identities instead of a recognizable KOKUEN skin.
