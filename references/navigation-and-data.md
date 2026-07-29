# Navigation, collections, and data

Read this reference for page navigation, tabs, sidebars, rows, lists, tables, filters, sorting, and
pagination.

## Navigation model

Choose semantics from the user action:

- link: changes location or route;
- button: performs an action in the current context;
- tab: switches a peer panel without leaving the context;
- menu: reveals a temporary action set;
- disclosure: expands content in place.

Do not use tab visuals for navigation while exposing button semantics. Do not make a current page a
disabled link. Use `aria-current` for navigation and `aria-selected` for selected composite items.

## Global and local navigation

- Keep primary destinations stable and ordered by user job.
- Current state changes type, tone, or surface and is programmatically exposed; no decorative dot.
- All links have 44px targets where they operate as application navigation.
- Collapse navigation through a real menu or alternate pattern, not hidden overflow with no access.
- Preserve focus and announce route or view changes when the framework does not do so.
- Do not place product navigation inside decorative icon tiles.

## Tabs

- Container has `role=tablist` and an accessible name.
- Each tab has `role=tab`, `aria-selected`, and `aria-controls`.
- Each panel has `role=tabpanel` and `aria-labelledby`.
- One tab participates in the Tab sequence. Arrow keys move among tabs; Home and End are supported.
- Automatic activation is appropriate only when panels appear without latency. Otherwise Enter or
  Space activates the focused tab.
- Disabled tabs are skipped and exposed.
- Narrow layouts scroll or change composition without shrinking targets.

## Rows and lists

A row has one clear primary action. Use a link or button for the actionable region rather than a
click handler on a generic `div`.

- Keep primary label, metadata, status, and secondary actions in stable columns.
- Secondary actions have their own names and 44px targets.
- Do not place a separate button inside another button or link.
- Use a split DOM structure or menu when the whole row navigates and also has actions.
- Selection and activation are separate concepts unless the task intentionally combines them.
- Long labels wrap or truncate under a documented strategy. Essential values remain available.
- Empty, loading, error, partial, stale, unavailable, and permission states use the same collection
  footprint when practical.

## Tables

Use a table for relationships that users compare across rows and columns.

- Associate headers with cells using native table semantics.
- Use row and column headers where both dimensions carry meaning.
- Align numeric values consistently and use tabular figures when helpful.
- Put units in headers when they apply to the whole column.
- Sorting controls expose direction and remain keyboard reachable.
- Row selection uses labelled checkboxes and announces selected count.
- Row actions do not disappear on hover only.
- Keep focus visible within scroll containers.
- Preserve column meaning at narrow widths through horizontal scroll, priority columns, or an
  alternate labelled-row representation. Do not collapse into anonymous values.

## Filters and search

- Name filter scope and current values.
- Keep Clear or Reset proximal to the filter group, not at a distant page edge.
- Announce result count changes when they are not otherwise obvious.
- Preserve filter values on recoverable errors.
- Distinguish search submission from live filtering.
- Empty results explain active filters and offer the relevant recovery.

## Pagination

- Wrap controls in navigation with an accessible label.
- Use links for route-based pages and buttons for client-side view changes.
- Current page uses `aria-current=page`.
- Previous and next expose their destination in the accessible name.
- Unavailable controls are actually disabled or omitted according to the chosen model.
- Every page control is at least 44 by 44px.
- Do not show every page when a compact range communicates position more clearly.
- Preserve scroll and focus behavior intentionally after navigation.

## Loading and skeletons

- Preserve layout when that reduces disorientation.
- Skeletons match the final content shape and count; they are not decorative bars.
- Mark the region busy and keep a readable loading label for assistive technology.
- Avoid infinite skeleton animation under reduced motion.
- Partial and stale data remain identified rather than replaced with generic loading.

## Empty and error states

- Explain why content is absent.
- Offer only actions relevant to recovery or first use.
- Keep error copy near the affected collection and retain usable data when possible.
- Permission failures state the missing capability and how it can be obtained.
- Do not use a large illustration, icon tile, or card merely to fill empty space.

## Responsive and content stress

Test:

- many navigation items and one very long label;
- deep CJK names and mixed numeric content;
- 0, 1, and many rows;
- sorted, selected, disabled, stale, and permission-restricted rows;
- narrow layout and 200 percent zoom;
- keyboard movement inside tablists, toolbars, and scroll containers;
- focus retention after filtering, sorting, pagination, and row deletion.

## Required proof

- active navigation programmatically exposed;
- full tab keyboard model and panel association;
- rows with primary and secondary actions have valid nonnested semantics;
- table header, sort, selection, and narrow strategy verified;
- pagination current and unavailable states announced;
- loading, empty, error, partial, stale, and unavailable fixtures inspected.
