# Figma synchronization status

## Current state

| Field | Value |
| --- | --- |
| File | [KOKUEN](https://www.figma.com/design/dMpK3ZOhraefh9L6m4BgBi) |
| File key | `dMpK3ZOhraefh9L6m4BgBi` |
| Connector session | Installed and authenticated |
| Plan observed | Starter, Full seat |
| Last attempt | 2026-07-30 |
| Remote status | Blocked by the Figma MCP Starter-plan tool-call limit |
| Confirmed page metadata | `0:1` - `Cover` |
| Variables, styles, components, libraries | Not inspected because the next read-only call was rejected |
| Remote mutations | None |
| Desktop fallback | Figma Desktop is not installed in `/Applications` |
| Browser fallback | Correct file opens, but the in-app browser session requires sign-in |

The Figma connector is installed and authenticated. This is not an installation failure. Both the
library-discovery call and the general Figma execution call returned the same plan-limit response,
so KOKUEN must not claim remote parity or invent component keys.

The desktop app would only be needed for the alternate local-development-plugin route. Do not
install it merely to avoid documenting the quota. The normal connector route can resume when its
quota is available. The browser route can resume after the owner signs in to Figma in the in-app
browser, but creating a complete library through canvas UI is not a safe substitute for variable and
component API access.

## Prepared local contract

[`figma/kokuen.library.json`](../figma/kokuen.library.json) records the exact file key, collection
axes, page architecture, 23 component mappings, review frames, source paths, observed remote ID, and
blocked fields. [`validate_figma_manifest.py`](../scripts/validate_figma_manifest.py) checks that the
plan still agrees with the token mode axes and component property contracts.

Run:

```bash
python3 scripts/validate_figma_manifest.py
```

The manifest deliberately leaves every uncreated remote page ID and component key as `null`.

## Required remote build sequence

When the Figma quota is available, resume in this order:

1. Re-run read-only discovery for pages, local collections, variables, styles, components, component
   sets, subscribed libraries, and available libraries.
2. Compare discovered assets with the manifest. Stop on any user-owned conflict rather than creating
   duplicates or silently replacing components.
3. Create or reconcile the five variable collections: Primitive, Theme, Contrast, Density, and Fixed.
4. Bind semantic variables through aliases and verify Dark, Light, Standard, More, Comfortable, and
   Compact modes independently.
5. Create the Foundations page and inspect a screenshot before creating components.
6. Build the 23 candidate component mappings incrementally with independent public properties.
7. Add Components, Do and do not, and Stress pages. Bad examples remain ordinary frames, never
   published components.
8. Capture and inspect screenshots at each page gate. Record all page IDs, variable IDs, component
   node IDs, and component keys in the manifest.
9. Mark a contract `stable` only after its code fixture, Figma component, and rendered interaction
   proof agree.
10. Add Code Connect only after both public APIs are stable.

## Review gates

The remote work is not accepted until all of these are reviewed in Figma:

- no component binds directly to a raw palette value when a semantic role exists;
- theme, contrast, and density modes change independently;
- each component exposes understandable properties instead of opaque combined variants;
- boundary owner, focus owner, width behavior, and 44px target measurements are visible;
- field actions remain proximal and no example creates a nested bezel;
- long English, CJK, empty, loading, error, unavailable, permission, narrow, high-contrast,
  reduced-motion, and zoom cases are present;
- screenshots match the current code specimen and any intentional drift has an owner.

Remote Figma synchronization remains a completion blocker. The code-native design system can be
validated independently, but it must not be described as Figma-complete until these gates pass.
