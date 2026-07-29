# AI surfaces

Read this reference for prompting, generation, streaming, agent actions, citations, approvals, and
AI-assisted search.

## State model

An AI surface distinguishes:

- idle;
- validating or awaiting permission;
- queued or pending;
- streaming;
- paused or stopped;
- cancelled;
- completed;
- incomplete or partial;
- failed and retryable;
- failed and not retryable;
- stale or superseded.

Do not collapse these into a generic “thinking” animation.

## User and system boundaries

- Keep user-authored input distinguishable from generated output.
- Preserve the prompt and attachments after recoverable failure.
- State the model or automation scope only when useful for the task or required for trust.
- Separate a proposed action from an executed action.
- Show which files, records, people, accounts, or external systems an action can affect.
- Do not imply grounding, citation, tool use, or completion without evidence.

## Input and composition

- Use a real textarea or editor for multiline intent.
- Keep Send, Stop, attachment, scope, and permission controls proximal to the composition region.
- Enter and Shift+Enter behavior is visible and platform-appropriate.
- Preserve IME composition; global shortcuts do not fire mid-composition.
- Disable or reject duplicate sends while the same request is being committed.
- Long prompts, CJK, attachments, and error copy remain usable at 200 percent zoom.

## Streaming

- Give Stop a stable 44px target in a consistent location.
- Maintain readable scroll behavior; do not force-scroll when the user has moved away from the end.
- Mark incomplete content and preserve it after Stop unless the user discards it.
- Announce updates at a rate that does not overwhelm assistive technology.
- Do not use an animated cursor, glowing border, or speculative status as proof of progress.
- Reduced motion keeps the same state and Stop control.

## Tool and agent actions

Classify the action before execution:

| Class | Example | Required boundary |
| --- | --- | --- |
| read-only | search, inspect, summarize | scope visible when meaningful |
| reversible local | draft, stage, rename with undo | outcome and recovery |
| external write | send, publish, update shared record | explicit confirmation |
| destructive or irreversible | delete, overwrite, purchase | exact target and final confirmation |
| permission expansion | connect account, grant access | purpose, duration, and affected data |

Approval must occur at the decision point, not hidden in onboarding or a generic terms screen.

## Sources and grounding

- Cite the source next to the claim or output it supports.
- Distinguish direct source content, model inference, and unsupported suggestion.
- Expose stale, missing, partial, or conflicting sources.
- Do not fabricate URLs, quotes, document names, or retrieval success.
- Keep source controls keyboard reachable and readable with long titles.

## Errors and recovery

- Name what failed: model response, retrieval, permission, tool action, upload, or network.
- Preserve prompt, output, and affected scope when safe.
- Offer Retry only when retry is valid.
- Offer Edit and retry when the prompt or scope caused the failure.
- Do not silently switch models, tools, accounts, or permissions.
- If partial external effects occurred, enumerate them before offering recovery.

## AI in universal command

- AI results sit in the same listbox model as other command options.
- The option label names the scope: `Summarize selected notes`, not `Ask AI`.
- Preview or confirmation separates suggestion from external action.
- Permission-bound options explain why they cannot run.
- Invocation closes command only when the destination or next state is clear; long-running work should
  expose status in a stable product surface.

## Trust copy

Use concrete language:

- `Drafting a reply from the three selected messages`
- `Stopped. The partial draft is available below.`
- `Could not access the shared folder. Request access or choose another source.`

Avoid anthropomorphic filler, fake certainty, “magic” language, and generic sparkles as an AI label.

## Required fixtures

- prompt idle, long/CJK input, validation, and duplicate-send rejection;
- pending, streaming, Stop, stopped partial, resume or retry policy;
- completed with and without sources;
- retrieval failure, permission failure, tool failure, and partial external effect;
- reversible local action, external write confirmation, destructive confirmation;
- command AI option with explicit scope and permission-unavailable state;
- reduced motion, keyboard-only, screen-reader update policy, narrow layout, and 200 percent zoom.
