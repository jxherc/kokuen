# Visual grammar and product boundary

Read this reference when defining a theme, reshaping a screen, or deciding whether a rule belongs in
KOKUEN or the product.

## The universal layer

KOKUEN may standardize a decision when it protects comprehension, interaction, accessibility, or
cross-surface consistency. It may standardize:

- semantic roles and token structure;
- spacing relationships and target sizes;
- component anatomy and states;
- boundary and focus behavior;
- pointer, keyboard, and assistive-technology behavior;
- responsive and content stress behavior;
- Figma/code parity and proof requirements.

KOKUEN may not standardize a decision merely because a reusable CSS value is convenient. Keep these
product-specific unless the product explicitly adopts a shared family:

- signature type, color palette, imagery, illustration, material, and icon construction;
- information architecture, navigation labels, product nouns, and task priority;
- page composition, brand artifact, density preference, and emotional tone;
- marketing sections, hero composition, and decorative motion.

## Product brief

Complete this before a new theme or major visual redesign:

```text
Product, primary user, and high-frequency job:
Moment of greatest risk or cognitive load:
Three qualities that must feel true:
Three qualities that must never feel true:
Real content and hardest content case:
Visual medium and signature artifact:
Type voice, body voice, and data voice:
Canvas, surface, ink, state, and selection relationships:
Edge, radius, elevation, and density behavior:
Motion purpose and reduced-motion equivalent:
Icon, image, and asset grammar:
References: principles to borrow, not layouts or assets:
Anti-references and known slop risks:
Accessibility, localization, platform, and performance constraints:
```

Do not proceed from adjectives alone. Convert each quality into an observable decision. “Quiet” may
mean few simultaneous actions, low boundary density, controlled type contrast, and no ambient motion.
“Fast” may mean short labels, stable action placement, keyboard reachability, and immediate feedback.

## One coherent world

A strong product direction has one material logic. Decide how the interface exists:

- ink on a measured working surface;
- a dense operational instrument;
- a tactile media shelf;
- a spatial canvas;
- a typographic editor;
- another product-specific world supported by its task.

The material logic governs type, spacing, edges, motion, icons, and imagery together. Do not assemble
individually attractive parts from unrelated visual systems.

Use one signature decision with enough specificity that it could not be pasted unchanged into a
competitor. The signature can be a real product artifact, an authored information layout, a specific
typographic behavior, bespoke icon construction, or a task-linked spatial interaction. It is not a
generic glow, gradient, card grid, fake app window, or decorative hero stack.

## Sparse is not empty

Minimal product UI removes redundant structure while preserving orientation, action, and feedback.
Every remaining element carries more responsibility.

- Remove copy that repeats the layout.
- Remove boxes when alignment and space already communicate grouping.
- Keep the primary job visible without marketing explanation.
- Give the user state, scope, and consequence exactly where decisions occur.
- Add authored character through task-specific structure, not ornament.

A screen with no hierarchy, feedback, or product-specific idea is unfinished, even if it is clean.

## Shared behavior, distinct expression

Two products may share the same Button contract while differing in type, tone, radius, border model,
icon grammar, and action hierarchy. KOKUEN checks that both have complete states, 44px targets, visible
focus, stable labels, busy repeat rejection, and accessible names. It does not make them look alike.

Forward-test any new universal rule against at least three unrelated products. Reject or narrow the
rule when it forces the same composition or visual character onto all three.

## Content is structural material

Use real product nouns and plausible data. Test:

- one-character and very long labels;
- English, CJK, mixed-script, and right-to-left content when supported;
- timestamps, units, negative numbers, and large values;
- empty, loading, error, unavailable, permission, stale, and partial data;
- generated text, citations, and user-authored text;
- destructive consequences and recovery language.

Never use invented customer logos, fake success metrics, generic Latin filler, or decorative metadata
to make an empty composition look finished.

## Icon and asset decisions

An icon earns its place when it improves recognition, scanning, spatial economy, or a repeated action.

- Prefer a real product asset or a coherent product-specific icon family.
- Use bare marks unless containment has a functional job.
- Give icon-only actions accessible names and 44px targets.
- Test optical alignment at the rendered size.
- Record source, license, version, viewBox, directionality, and replacement ID.
- Do not redraw a generic thin-line pack and call it bespoke.
- Do not remove every icon merely to avoid an icon-pack look.

## Motion decisions

Motion must explain state, relationship, or continuity.

- Content begins visible.
- Hover never lifts or scales a control.
- Use state transitions that do not move the target under the pointer.
- Preserve spatial continuity for opening, closing, reordering, and expanding.
- Provide a reduced-motion path with the same information and control.
- Do not use loading motion as evidence of success.
- Avoid decorative looping motion in working surfaces.

## Professional critique pass

Ask in this order:

1. Can the user identify the main job and current state without explanatory copy?
2. Does every element belong to one product-specific world?
3. Is any component boxed merely because it exists?
4. Did a prebuilt layout determine the information architecture?
5. Are hierarchy and grouping still clear when color is removed?
6. Does real long, empty, error, and localized content preserve the composition?
7. Is the screen calm because decisions are clear, or empty because decisions are missing?
8. Could the signature be swapped into a competitor unchanged?
9. Did KOKUEN preserve behavior without imposing the specimen theme?
10. Has the real surface been rendered and exercised?
