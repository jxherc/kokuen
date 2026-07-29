# Conventions

## Product boundary

KOKUEN owns repeated interaction contracts. The consuming product owns palette, typography, imagery,
icon grammar, density, composition, navigation model, and signature. Never turn a test fixture or the
graphite specimen into a universal page skeleton.

## Geometry

- Layout spacing: `0, 4, 8, 12, 16, 24, 32, 48, 64`.
- Default target: at least 44 by 44 CSS pixels.
- Density may change visual rhythm, never hit area, semantics, or keyboard behavior.
- Field width follows expected content. Search, command, composition, and true full-row entry are the
  only default full-width cases.
- Field actions stay inside a composite end affordance or immediately beside a bounded field.

## Boundaries

- One control has one perceived resting boundary and one focus geometry.
- Every edge names input affordance, state, containment, clipping, or separation as its job.
- Prefer spacing, alignment, and tone to ornamental borders and dividers.
- Focus hugs the active region, remains unclipped and unobscured, and changes at least 3:1 from rest.
- Do not stack wrapper edge, child edge, and focus outline into nested rectangles.

## Components

- Prefer native HTML when it provides the required behavior and can meet product styling constraints.
- A custom composite implements one complete WAI-ARIA keyboard and focus model.
- Busy actions reject repeat activation and preserve the action's outcome label.
- Errors are programmatically associated and explain recovery without discarding input.
- Dialogs and temporary layers define focus entry, containment, Escape policy, and return.
- Product copy uses direct verbs and keeps the same action name through confirmation and outcome.

## Motion and visual quality

- Content is visible before any animation runs.
- Hover never moves or scales buttons and ordinary controls.
- State feedback respects reduced motion and does not imply false completion.
- Apply the complete anti-slop law before visual handoff. Passing a ban list does not replace a
  product-specific visual decision.

## Promotion and proof

A component remains `candidate` until code, Figma, and rendered fixture proof agree. Before a
completion claim, run all deterministic validators, browser suites, narrow and zoom checks, forced
colors, reduced motion, pointer and keyboard flows, console inspection, and a point-by-point
anti-slop audit. State external blockers separately.
