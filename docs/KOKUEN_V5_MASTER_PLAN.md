# KOKUEN v5 master plan

## Objective

Turn KOKUEN into a professional design operating system for reusable product UI. It must give an
agent exact rules for common controls, spacing, boundaries, keyboard behavior, Figma parity, and
rendered proof without forcing every product into one visual identity.

The shipped specimen uses the original dark KOKUEN palette by default. That palette demonstrates
the contract; it is not a global color doctrine. Product type, color, imagery, density, and signature
remain product decisions.

## Design brief

```text
Primary users: product designers and coding agents building real application UI
Primary job: make shared controls coherent, accessible, and implementation-ready
Character: graphite instrument manual; sparse, exact, quiet, operational
Must never feel: modular dashboard, card catalog, generic SaaS kit, decorative showroom
Signature: a measured content rail whose state and interaction evidence are visible in place
Default palette: original KOKUEN dark graphite specimen
Geometry: one perceived boundary per control, 44px targets, low radii, no ornamental shells
Motion: state feedback only; content visible before motion; no lift or scale on hover
Type: readable system body and explicit data role; no tiny metadata costume
```

## What is universal

KOKUEN owns these contracts:

- semantic token roles and mode resolution;
- spacing relationships, target sizes, boundaries, and focus geometry;
- common component anatomy, states, content constraints, and responsive behavior;
- native or WAI-ARIA keyboard and focus models;
- universal command/search and bounded AI-action behavior;
- Figma variable and component parity;
- deterministic linting, contract validation, and rendered verification.

KOKUEN does not own these product decisions:

- brand palette, signature type, imagery, icon style, or illustration medium;
- product navigation model, information architecture, and domain language;
- which component variants a product exposes;
- a decorative hero or a reusable page skeleton.

## Rule taxonomy

Every rule must be identified as one of the following. A vague preference is not enforceable.

1. **Invariant:** must pass in every implementation. Example: an interactive target is at least
   44 by 44 CSS pixels unless an equivalent adjacent-target exception is documented and tested.
2. **Hard anti-pattern:** must not appear without a recorded exception. Example: wrapper border,
   input border, and focus outline producing three perceived boundaries.
3. **Conditional rule:** allowed only for a named job. Example: a container boundary is allowed when
   it clips, groups, separates, or communicates state.
4. **Product decision:** selected from the product brief. Example: palette, density, type, radius,
   icon grammar, and signature artifact.
5. **Proof gate:** evidence required before completion. Example: keyboard traversal and 200 percent
   zoom screenshots of the actual delivery surface.

## Boundary and bezel law

1. No component gets a box merely because it exists.
2. Every visible boundary must name one job: input affordance, state, containment, clipping, or
   separation. If it has no named job, remove it.
3. One control has one perceived resting boundary and one focus geometry.
4. Never stack wrapper border, child border, and focus outline into nested rectangles.
5. Focus must hug the actual interactive region, not unused flex or grid width.
6. A field width follows expected content. Full-row fields are reserved for command, search,
   composition, or truly full-row data entry.
7. Field actions stay inside the end affordance or directly beside a deliberately bounded field.
8. Prefer spacing, alignment, and tonal change before adding a border or divider.
9. Same-level containers do not nest shells merely to create depth.
10. A resting border must not imitate the focus state.
11. Focus must remain visible, unclipped, unobscured, and distinguishable at a 3:1 state change.
12. Decorative separators are prohibited when whitespace establishes the relationship.

Every stable component contract must include a `Boundary rationale` and a `Width behavior` field.

## Foundation contracts

### Spacing

Use the layout scale `0, 4, 8, 12, 16, 24, 32, 48, 64`. Optical construction values such as a
1px edge or 2px focus ring do not become layout tokens. Each gap names a relationship rather than
merely a size.

### Targets and density

- Default interactive target: 44 by 44 CSS pixels or larger.
- Compact visual marks may sit inside a 44px hit target.
- Density changes internal rhythm, never keyboard behavior, semantics, or minimum hit areas.
- Neighboring controls keep at least 8px separation unless they form one documented composite.

### Type and content

- Normal interface text defaults to at least 14px with a readable line height.
- Essential labels and help text must not rely on 10 to 12px type.
- Metadata may be smaller only when nonessential and still meets contrast and zoom requirements.
- Test CJK, long names, timestamps, numbers, empty states, and recovery copy before locking type.
- Keep interface language direct. Do not repeat specimen labels above every example when placement
  and content already explain the role.

### Color and contrast

- Color tokens express roles, not a universal accent or signal ideology.
- Text and controls pass documented foreground/background contrast pairs.
- Focus, error, selected, busy, and success states never rely on color alone.
- Theme, contrast, and density are independent axes.
- Forced-colors behavior is a platform mode, not another product palette.

### Motion

- Content is visible before any animation runs.
- Hover changes state without moving the control.
- Busy motion has a reduced-motion equivalent and cannot imply completion.
- Motion explains state or continuity; it is not ambient decoration.

## Component contract

Every stable primitive or pattern records:

- stable ID, status, user job, code path, and Figma key;
- anatomy and named slots;
- variants, required states, and content constraints;
- semantic and component token dependencies;
- boundary rationale and width behavior;
- pointer, touch, disabled, loading, and repeat-activation behavior;
- role, accessible name, description, error relationship, and state exposure;
- keyboard model, focus entry, focus boundary, exit, and restoration;
- responsive, density, high-contrast, CJK, overflow, and 200 percent zoom behavior;
- deterministic visual and interaction fixtures;
- known exception, migration, and replacement notes.

The initial v5 inventory covers actions, fields, textarea, checkbox, radio group, switch, slider,
select/listbox, tabs, menu, row/list, table, pagination, feedback, empty/loading/error states, toast,
dialog, confirmation, universal command, and bounded AI generation.

## Professional interaction rules

- Use native HTML when it provides the needed interaction and appearance can be styled safely.
- A custom composite follows one complete WAI-ARIA pattern. Do not mix focus models.
- Dialogs trap Tab and Shift+Tab while open, close by documented Escape policy, and restore focus.
- Menus support Arrow keys, Home, End, Enter or Space, Escape, and focus return.
- Radio groups expose multiple choices, one checked item, roving focus, and Arrow-key selection.
- Select/listbox uses either DOM focus on options or `aria-activedescendant`, never both at once.
- Busy actions reject repeat activation and expose an explicit busy label.
- Errors are programmatically associated with the field and explain recovery.
- Universal command maintains one active option, filters without losing its keyboard model, and
  exposes loading, empty, error, unavailable, and permission states in the same surface.
- AI surfaces distinguish user input, generated output, sources or scope, pending, streaming,
  stopped, cancelled, failed, retryable, and permission-bound actions.

## Repository architecture

`SKILL.md` becomes a concise router. Detailed rules live one level deep under `references/`:

- `visual-grammar.md`
- `boundaries-and-bezels.md`
- `spacing-and-layout.md`
- `typography-and-color.md`
- `forms-and-input.md`
- `buttons-and-actions.md`
- `navigation-and-data.md`
- `overlays-and-command.md`
- `ai-surfaces.md`
- `figma-contract.md`
- `qa-and-antipatterns.md`

Deterministic scripts validate tokens, component contracts, and source-level UI rules. The HTML
specimen remains a product-neutral, functional reference. It is arranged as a measured reading
surface rather than a card grid or a fake product home page.

## Visual specimen

The v5 specimen must:

- use the original dark KOKUEN palette as its default theme;
- show common UI in a calm vertical flow with generous section separation and very few containers;
- demonstrate good and bad boundary examples without leaving broken controls interactive;
- use 44px targets for every control;
- include deterministic state controls for default, hover, focus, pressed, busy, disabled, invalid,
  selected, empty, loading, error, confirmation, and toast states;
- include keyboard-complete select, radio, menu, dialog, and universal command fixtures;
- include long English and CJK content, narrow layout, high contrast, reduced motion, and zoom stress;
- avoid decorative status dots, card grids, generic modular boxes, or an Alles-specific hero.

## Figma library

Figma is an inspectable contract, not delivery proof.

1. Audit the existing file before writing.
2. Separate foundation variables by concern: theme, contrast, density, type, geometry, and motion.
3. Bind components to semantic variables before composing review pages.
4. Use independent component properties rather than multiplying opaque variant names.
5. Add a `Do and do not` page for unnecessary bezel, nested boundaries, stranded field action,
   overwide field, double focus geometry, and tiny targets.
6. Add a stress page for long content, CJK, empty, loading, error, narrow layout, and 200 percent zoom.
7. Add Code Connect only after both code and Figma APIs are stable.
8. Record all node IDs, component keys, variable IDs, and any intentional drift.

## Deterministic validation

The v5 validation suite must provide:

- DTCG token shape, aliases, cycles, types, public mode coverage, and contrast-pair checks;
- component contract schema validation and duplicate ID detection;
- UI source linting for raw layout spacing, too-small targets, opacity-zero content entrances,
  hover transforms, missing focus replacements, unsupported native controls, and repeatable warnings
  for border density or nested boundaries;
- deterministic fixture IDs for browser interaction tests;
- repository skill validation with the official skill validator.

Lint warnings are evidence prompts, not permission to make false claims. A warning may be suppressed
only by a nearby reason or an explicit fixture exception.

## Forward tests

Apply the router and contracts to three unrelated briefs without changing their product identity:

1. a writing workspace with long-form text and command search;
2. a dense operational data tool with tables, filters, and destructive actions;
3. a consumer media browser with imagery, playback actions, and selection.

Each exercise must produce a different visual direction while preserving the same target, boundary,
focus, state, keyboard, and proof contracts. If the outputs converge into one KOKUEN look, the skill
has exceeded its boundary.

## Acceptance gates

KOKUEN v5 is complete only when all of the following have evidence:

- each inventory item has anatomy, states, keyboard model, boundary rationale, width behavior,
  mode behavior, content constraints, Figma mapping, and code path;
- every interactive target in the specimen measures at least 44 by 44 CSS pixels;
- field errors, busy repeat rejection, menu/select/radio keyboard models, dialog focus traps, command
  focus restoration, and AI stop/cancel behavior work through real interaction;
- no visible boundary exists without a declared job;
- desktop, narrow, forced-colors, reduced-motion, 200 percent zoom, and CJK fixtures are inspected;
- token, contract, UI lint, skill validation, and browser tests pass;
- the final anti-slop law is rechecked point by point;
- the written rules, visual specimen, and Figma library are each reviewed as separate approval gates.

## Implementation sequence

1. Persist this plan and decisions as repository truth.
2. Rebuild the skill as a concise router and add focused references.
3. Formalize component contracts, token schema, and deterministic validation.
4. Rebuild the visual specimen and interaction fixtures.
5. Audit and update the Figma variables, components, and review pages.
6. Run the three forward tests and record the outcomes.
7. Run rendered, keyboard, responsive, accessibility, and anti-slop verification.
8. Review the final diff and create intentional local commits.
