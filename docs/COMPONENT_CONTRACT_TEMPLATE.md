# Stable component contract

Create one completed record for each KOKUEN primitive before calling it stable. Keep the record near
the consumer code or design-data registry when one exists; this template defines the required fields.

```text
ID and status:
User job:
Code path and public API:
Figma component key and property mapping:

Anatomy / named slots:
Variants and supported states:
Semantic and component token dependencies:
Keyboard model, focus entry/exit, and focus restoration:
Accessible role, name, description, state, and error relationship:
Pointer, touch, disabled, loading, and async behavior:
Content/localization limits and overflow strategy:
Responsive and density behavior:
Required data states: populated / empty / loading / error / unavailable:
Visual and interaction fixtures:
Known exceptions, migration notes, and deprecation/replacement:
```

Link a custom control to the matching WAI-ARIA Authoring Practices pattern. ARIA attributes without
the corresponding keyboard and focus behavior are not a component contract.
