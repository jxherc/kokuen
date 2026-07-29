# KOKUEN v5 forward tests

## Purpose

These fixtures test the most important boundary in KOKUEN: shared interaction rules must survive
without turning unrelated products into one visual theme. Each fixture starts from a different user,
task, content shape, palette, type voice, density, and composition. They reuse the same geometry,
focus, state, and accessibility contracts from `SKILL.md`.

The fixtures are evidence, not starters. Products must not copy their layouts or visual identities.

## Shared contract under test

| Contract | Required in every fixture |
| --- | --- |
| Target | Visible interactive targets measure at least 44 by 44 CSS pixels. |
| Boundary | One resting boundary and one focus geometry per control. Every container edge has a job. |
| Proximity | Field actions remain attached to the field they modify. |
| Focus | Temporary layers trap focus, close by documented Escape policy, and return focus. |
| State | Selection, destructive confirmation, playback, busy work, and errors use text or semantics in addition to color. |
| Motion | Content is visible without animation. Hover does not move controls. Reduced motion remains usable. |
| Reflow | The page does not create viewport-level horizontal overflow at 390px or 640px. Local data or media rails scroll inside a named region. |
| Language | Controls name the actual action. Status copy confirms the same action and its consequence. |

## Test A: Draftroom writing workspace

### Brief

- **User:** an editor revising long-form narrative copy.
- **Primary job:** read the manuscript and resolve notes without losing place.
- **Hardest content:** long prose, a long document title, and editorial notes with specific recovery.
- **Required layer:** a universal find-or-act command that preserves manuscript context.

### Product decisions

- **Palette:** eucalyptus paper `#eaf1ed`, clean sheet `#f7faf8`, near-black ink `#17201d`,
  revision red `#8e2f2a`, and deep green focus `#174c42`.
- **Type:** Georgia for the manuscript and the platform system sans for controls. The serif belongs to
  the reading material, not every label.
- **Composition:** manuscript and editorial margin share the page. The notes are a functional tinted
  gutter, not independent cards.
- **Signature:** edits appear in the text and align with numbered margin commentary.

```text
document identity                                      find or act

manuscript title                              editorial margin
long reading measure                          01 specific note
revision inside prose                         02 source check
                                               add margin note
```

### Uniqueness review

The first idea used a centered document card with a toolbar. That would reduce a writing product to
a generic editor window. The final direction removes the window shell and lets the manuscript occupy
the surface. The margin is content-bearing and would not make sense in the ledger or media fixture.

### Contract application

- The command trigger and every command option meet the target contract.
- The command field owns its resting edge; its close action sits in an adjacent 44px region.
- The dialog traps Tab in both directions, accepts Escape, and returns focus to the trigger.
- Long text reflows into one column and the margin follows below at narrow widths.

Fixture: [`../tests/forward-fixtures/writer.html`](../tests/forward-fixtures/writer.html)

## Test B: Relay operational ledger

### Brief

- **User:** an operations lead handing off active service events.
- **Primary job:** inspect, select, and close events with an auditable consequence.
- **Hardest content:** dense tabular data, timestamps, long service names, urgency, and destructive bulk action.
- **Required layer:** an explicit confirmation boundary before closing selected events.

### Product decisions

- **Palette:** warm black `#15120e`, umber surface `#1c1813`, parchment ink `#f2ead8`, quiet
  amber focus `#f2cf85`, and readable error coral `#ff9b8e`.
- **Type:** system sans for operations and system mono only for event IDs and time data.
- **Composition:** a continuous ledger with row separation. The table is not wrapped in a decorative card.
- **Signature:** handoff information reads like a live dispatch sheet, with time and audit consequence kept visible.

```text
relay ledger / region / shift                              time

12 open events                             close selected events
filter + clear                                      result count
select | event | service | owner | opened | state | inspect
```

### Uniqueness review

The first idea used status cards above the table. That would make summary values louder than the
actual work and repeat a dashboard pattern. The final direction puts the operational queue first.
The warm ledger palette and data rhythm are specific to a handoff surface.

### Contract application

- The filter clear action remains inside the composite field boundary.
- Row selections expose `role=checkbox` and `aria-checked` while preserving a 44px target.
- The table scrolls within a keyboard-focusable named region on narrow screens.
- Confirmation explains consequence, traps focus, returns it, rejects repeat activation while busy,
  and reports the completed event IDs in a live region.

Fixture: [`../tests/forward-fixtures/operations.html`](../tests/forward-fixtures/operations.html)

## Test C: Afterimage media browser

### Brief

- **User:** a viewer choosing and continuing short documentary programs.
- **Primary job:** browse programs and preserve playback continuity.
- **Hardest content:** visual covers, long titles, horizontal selection, persistent playback, and search.
- **Required layer:** global program search without interrupting the current program.

### Product decisions

- **Palette:** wine-black `#170d11`, blush ink `#fff2f1`, quiet rose edge `#563840`, and four
  flat authored program colors. The focus tone is warm and light, not a bright branded accent.
- **Type:** a condensed platform face for program display and system sans for utility copy.
- **Composition:** an oversized season title, a bare horizontal poster strip, and a persistent player.
- **Signature:** each program has a flat, custom line-art cover. Posters are media, not generic icon tiles.

```text
AFTERIMAGE                                             search

CITIES AFTER MIDNIGHT                     season context
[poster] [poster] [poster] [poster]  -> local horizontal rail

pause | active title and city                         time
```

### Uniqueness review

The first idea placed program metadata in bordered cards. That would hide the actual media behind
component chrome. The final direction leaves the authored covers bare, gives the season title the
largest scale, and uses one continuous player surface. This structure would be inappropriate for
manuscript revision or operational triage.

### Contract application

- Program posters are real selection controls with `aria-pressed`, 44px-plus targets, and text labels.
- Playback exposes its current pressed state and updates its accessible name between Play and Pause.
- Search is a focus-contained dialog with Escape and focus return.
- The media rail scrolls locally without widening the page.

Fixture: [`../tests/forward-fixtures/media.html`](../tests/forward-fixtures/media.html)

## Cross-test result

| Axis | Draftroom | Relay ledger | Afterimage |
| --- | --- | --- | --- |
| Surface | pale eucalyptus paper | warm black dispatch sheet | wine-black screening room |
| Primary content | flowing prose | dense rows | authored covers |
| Type voice | reading serif | operational sans and data mono | condensed program display |
| Density | spacious reading | dense but touch-safe | cinematic and horizontally browsed |
| Signature | editorial margin | live handoff ledger | program-art strip plus player |
| Temporary layer | command | destructive confirmation | search |

The three outputs do not converge on one palette, card style, hero, navigation skeleton, or type
treatment. They do converge on target size, focus, state, action proximity, keyboard behavior, and
rendered proof. That is the intended KOKUEN boundary.

## Automated evidence

Run the fixtures through the real browser:

```bash
python3 /Users/jxh/.codex/skills/webapp-testing/scripts/with_server.py \
  --server "python3 -m http.server 4312 --bind 127.0.0.1" \
  --port 4312 -- python3 tests/test_forward_fixtures.py
```

The suite measures interactive targets, viewport overflow, focus entry and return, dialog trapping,
selection state, destructive busy handling, playback state, console errors, and reduced-motion
rendering. It captures wide and narrow screenshots for each direction.
