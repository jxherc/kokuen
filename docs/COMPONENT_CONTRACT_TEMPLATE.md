# Stable component contract

Use this record before promoting a KOKUEN primitive or pattern to `stable`. The machine-readable
registry is [`contracts/kokuen.components.json`](../contracts/kokuen.components.json). Its schema is
[`contracts/kokuen.components.schema.json`](../contracts/kokuen.components.schema.json).

## Record

```text
Stable ID:
Status: draft / candidate / stable / deprecated
User job:

Code path:
Public API:
Figma status:
Figma component key:
Figma property -> code property mapping:

Anatomy and named slots:
Variants:
Required visual and data states:
Semantic and component token dependencies:

Boundary job: input affordance / state / containment / clipping / separation / none
Boundary rationale:
Resting boundary owner:
Focus boundary owner:
Width behavior: content / bounded / container / viewport service / responsive switch

Accessible role:
Accessible name:
Description and help relationship:
State exposure:
Error relationship:

Keyboard keys and behavior:
Focus entry:
Focus boundary and exit:
Focus restoration:

Pointer behavior:
Touch target behavior:
Disabled behavior:
Loading and async behavior:
Repeat-activation policy:

Content limits:
Localization and CJK behavior:
Overflow and truncation strategy:
Density behavior:
Responsive and 200 percent zoom behavior:

Required data states: populated / empty / loading / error / partial / stale / unavailable / permission
Deterministic visual and interaction fixture IDs:
Known exceptions, owner, evidence, and expiry:
Migration, deprecation, and replacement:
```

## Promotion gates

A component may be `candidate` while Figma or production usage remains incomplete. It may become
`stable` only when:

1. every field above is complete;
2. every token path resolves in all supported modes;
3. the boundary job and width behavior survive long, CJK, narrow, and zoom fixtures;
4. pointer, touch, keyboard, focus entry, focus exit, and focus return are exercised;
5. disabled, busy, invalid, error, and unavailable behavior exist where relevant;
6. the code API and independent Figma properties map without hidden combinations;
7. the component key and deterministic fixture IDs are recorded;
8. the real delivery surface passes the KOKUEN proof matrix.

Run:

```bash
python3 scripts/validate_contracts.py contracts
```

Use `--require-stable` only for a release whose full inventory is expected to be production and
Figma complete.

ARIA attributes without the matching keyboard, focus, and state behavior do not satisfy the
contract. A visually complete Figma component without a mapped code API also does not satisfy it.
