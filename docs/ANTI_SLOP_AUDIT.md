# KOKUEN v5 anti-slop audit

## Scope and evidence

Audited on 2026-07-30 after the final v5 visual changes.

Surfaces reviewed:

- `banner.svg`;
- `designs/kokuen-visual-template/Universal UI Template.html` at desktop, 390px narrow, and
  640px 200-percent-equivalent viewports;
- command and dialog open states;
- forced colors and reduced motion;
- Draftroom, Relay ledger, and Afterimage forward fixtures at wide and narrow sizes.

Evidence includes source lint, token contrast checks, browser target measurement, pointer and keyboard
interaction, console capture, screenshots, and direct visual inspection. Remote Figma is excluded by
owner direction and is not a completion gate for this audit.

## Direct visual tells

| Check | Result |
| --- | --- |
| Lucide or one generic line-icon pack everywhere | Pass. No icon dependency. Small marks are bare and job-specific; the media covers use one authored flat-line system. |
| Em dashes as interface voice | Pass. None occur in the audited UI or documentation surfaces. |
| Pill or eyebrow badge | Pass. No decorative badge above headings and no pill metadata field. |
| Fraunces plus Work Sans | Pass. Not used. |
| Glowy pill buttons | Pass. No pill radius, gradient fill, blur, or glow. |
| Oversized icon in a colored tile | Pass. No icon tile. Program art is the media object itself, not an icon container. |
| Floating or bobbing cards | Pass. No card lift, loop, float, or parallax decoration. |
| Cut-off glow | Pass. No glow. |
| Kitchen-sink card | Pass. The universal reference has no card catalog. |
| Fake macOS or app-window hero | Pass. No window prop or traffic-light dots. |
| Space Grotesk as default tech voice | Pass. Not used. |
| Purple or blue-to-purple gradient | Pass. No gradient or purple palette. The graphite specimen uses a semantic indigo focus role only. |
| Gradient pill with icon and text | Pass. Not present. |
| Default filled CTA plus outlined secondary pair | Pass. No marketing CTA row. Action hierarchies are task-specific and not presented as a prefab pair. |
| Three-tier pricing block | Not applicable. No marketing or pricing page. |
| Testimonial or ornamental quote card | Not applicable. No testimonials or decorative quote marks. |
| Gradient initials avatar | Pass. No fake avatar. |
| Pre-footer CTA banner | Not applicable. No marketing footer sequence. |
| Gradient icon-tile logo lockup | Pass. KOKUEN uses type only and no boxed mark. |
| Cormorant Garamond luxury default | Pass. Not used. |
| Split hero | Pass. The universal reference is a measured document, not a hero; all three forward fixtures use different task compositions. |
| Full-page graph-paper background | Pass. No grid background. The banner ruler encodes the real spacing scale. |
| Crude CSS/SVG placeholder illustration | Pass with a reviewed conditional use. Afterimage covers are the actual authored program art, share a deliberate construction, and are not generic hero filler. |
| Accent-bar card or status rail | Fixed. The pagination toast had a green inline-start rail. Outcome styling now covers its full perimeter and surface; lint rejects partial-edge state markers. |
| Background radial glow | Pass. No radial background or bloom. |
| Fake code-snippet window | Pass. No code prop. |
| Sora or JetBrains Mono costume | Pass. Not used. System mono appears only for event IDs and timestamps. |
| Floating tag pinned to an image | Pass. No overlay tag. |
| Syne display default | Pass. Not used. |
| Gradient-filled headline | Pass. No text gradient. |
| Archivo or Inter everywhere | Pass. Neither carries the identity. |
| Hairline light border on every box | Pass. The reference uses few containers and each edge has a declared job. |
| Countdown timer | Not applicable. |
| Card hover lift | Pass. Strict lint rejects hover transforms; browser fixtures do not move. |
| Letterspaced luxury serif wordmark | Pass. No serif luxury lockup. The banner's lowercase label supports the Japanese mark and is not the identity alone. |
| Bodoni, Didot, Playfair, or another reflexive Didone | Pass. Not used. |
| Monospace as the house voice | Pass. Mono is confined to real data in Relay. |
| One tracked uppercase label treatment everywhere | Pass. The reference uses sentence case. Afterimage uses uppercase only for its program-display voice, not utility labels. |
| Botched glass | Pass. No transparency, blur, refraction, or glass. |
| Lazy faint grid background | Pass. No page grid. |
| Botched fill animation | Pass. No animated fill. Slider fill is direct state, keeps stable caps, and is not a decorative hover effect. |
| Hidden entrance content | Pass. No content starts at opacity zero or depends on JavaScript to appear. |
| Content sliced by an edge | Pass. Narrow, zoom, command, dialog, and table screenshots were checked; live content remains reachable. |
| Ragged comparison columns | Not applicable. No comparison card grid. Repeated table roles share columns. |
| Text jammed against an edge | Pass. Audited surfaces retain consistent gutters at wide and narrow widths. |
| Default all-around shadow | Pass. No drop shadow. Afterimage's 3px inset line is selected-state geometry inside the real media target. |
| Content flung to opposite rims | Pass. Header ends share a common grid and content axis; wide spacing is functional, not marooned clusters. |
| Missing or fake logos and icons | Pass. No social proof or integration claim warrants logos; none are fabricated. |
| Chronic centering miss | Pass. Button, choice, slider, close, player, and check marks were visually inspected and target-measured. |
| Shadow faked with a second box | Pass. No duplicate shadow geometry. |
| Icon or logo with a box behind it | Pass. Bare marks remain bare. Media posters are content, not icon backplates. |
| Eyebrow tick or little rule beside a label | Pass. No decorative kicker line. |
| Oversized footer wordmark pasted in | Not applicable. No marketing footer wordmark. |
| Colliding colors or hard color seams | Pass. Each surface uses one disciplined palette. No gradients stop at section boundaries. |
| Hard-edged box masquerading as shadow | Pass. No drop shadow. |
| Text without contrast | Pass. All 12 declared foreground/background pairs validate; muted text was inspected in screenshots. |
| Blurred duplicate silhouette or bloom | Pass. No glow or blur. |
| Dot under active navigation | Pass. Active state uses type and underline state only where tabs require selection geometry. |
| Content clipped across an overlap | Pass. Fixed player, dialogs, command, and local scroll regions preserve access to live content. |
| Cramped display type | Pass. Large titles use controlled line-height and tracking and retain readable word spacing. |
| Grain over live content | Pass. No grain layer. |
| Cool blue-charcoal dark default | Pass. The owner-directed default is neutral graphite; Relay is warm umber-black and Afterimage is wine-black. |
| Pastel candy gradient | Pass. No gradient. Draftroom uses one pale eucalyptus surface, not a candy wash. |
| Drifting blend-mode gradient blobs | Pass. Not present. |
| Radial halo behind an object | Pass. Not present. |
| Hero fails to own the fold | Not applicable to the long universal reference. Forward fixtures intentionally compose their first viewport and do not expose a stray next section. |
| Default cream or beige editorial surface | Pass. Draftroom uses a cool subject-linked eucalyptus paper, not a generic cream treatment. |
| Default UI-kit light gray | Pass. No gray-100 card or footer band. |
| Default Google-font rotation | Pass. No remote font import. System faces serve utility; content-specific type is restrained. |
| Hover boop | Pass. No hover translation or scale. |
| Inner-glow badge | Pass. No badge or glow. |
| Off-center strike/cut line | Pass. No strike decoration. Revision underline follows text metrics. |
| Default centered hero stack | Pass. No marketing hero stack. |
| Fixed decorative background | Pass. No fixed background texture. The fixed Afterimage player is a real control surface. |
| Hard image seam | Not applicable. No full-bleed photographic band. |
| Saturated accent sprayed everywhere | Pass. Focus, error, and selection use semantic roles and do not carry the page identity. |
| Underline-fill hover animation | Pass. No animated underline. |
| Sun-and-moon toggle or redrawn generic icon set | Pass. Theme proof uses named text controls. Media line art has one subject-specific construction. |
| Unrounded decorative hairline rule | Pass with one functional exception. The banner ruler measures the real spacing scale; table and control lines communicate state or structure. |

## Repeated layout audit

| Layout | Result |
| --- | --- |
| Kicker plus serif section heading | Pass. Universal sections begin from the content hierarchy, not repeated kicker/H2 pairs. |
| Big serif philosophy statement | Pass. Not present. |
| Inset enquiry island with form | Pass. Not present. |
| Email pill plus button | Pass. Not present. |
| Image card with overlay caption | Pass. Afterimage uses bare posters with metadata below, not gradient captions. |
| Flat fill for every section after a hero | Not applicable. The universal reference is one continuous document; the forward fixtures are single task surfaces. |
| Recycled house-style sequence | Pass. The three forward fixtures use different content, palettes, type voices, density, axes, and signatures. |
| Left hero stack plus right panel | Pass. Not used. |
| Three- or four-line dangling-accent headline | Pass. No accent word. Draftroom and Afterimage line breaks are controlled and use one or two conceptual phrases. |
| Filled button beside outlined button | Pass. No prefab CTA pairing. |
| Small label over large heading everywhere | Pass. The reference does not repeat that section-head formula. |
| Numbered steps beside a vertical rail | Pass. Draftroom note numbers label real editorial references and have no decorative rail. |
| Several slop layouts stacked together | Pass. No marketing section stack. |
| Whole SaaS product-page meta-skeleton | Pass. No hero/features/tabs/pricing/FAQ/CTA/footer sequence. |
| Metadata wrapped in tinted chips everywhere | Pass. No chip field. |
| Dead controls or fake interactivity | Pass. Every displayed control has tested interaction or is explicitly static diagnostic content. |

## Deeper design check

| Check | Result |
| --- | --- |
| Safe font swap instead of a real decision | Pass. KOKUEN does not prescribe product display type. Each forward fixture chooses type from its content role. |
| Same skeleton recolored | Pass. Forward fixture DOM and composition differ materially. |
| Standard multi-column footer | Pass. No footer template. |
| Removing all icons to dodge icon-pack slop | Pass. Marks are used where the action benefits; they are bare and sparse. |
| Mechanically avoiding the list without inventing anything | Pass. The universal signature is measured live evidence; Draftroom has aligned margin revision, Relay has a dispatch ledger, and Afterimage has authored covers plus persistent playback. |
| Incoherent palette, type, or component language | Pass. Each audited surface holds one palette, type hierarchy, spacing scale, and interaction language. |
| Literal realism used as a shortcut for creativity | Pass. No stock photography or fake realism. |
| Empty product artifact | Pass. Fixtures use concrete prose, IDs, owners, times, cities, duration, failures, and permission states. |
| Reference content copied rather than reference language learned | Pass. Copy and data are original and task-specific. |
| Dead-looking restraint | Pass. Interaction states, selection, command, streaming, Stop, local rails, and playback create a functional heartbeat without decorative motion. |

## Premium craft checks that apply

- **Tonal elevation:** overlays use a restrained surface shift and one real containment edge.
- **Bare marks:** icon actions carry no tile or decorative container.
- **Say less:** specimen headings and fixture copy are short and operational.
- **Authored interaction:** command, select, menu, dialog, confirmation, busy, toast, streaming,
  Stop, program selection, and playback states are implemented for their specific jobs.
- **Whole-page composition:** each forward fixture is composed around its primary content rather than
  assembled from generic sections.
- **Custom SVG:** Afterimage cover marks use consistent stroke weight, square construction, flat color,
  and subject-specific silhouettes.
- **Signature:** measured reference rail; manuscript margin; dispatch ledger; program strip and player.
- **Real specificity:** fixtures use concrete names, IDs, times, locations, content, and consequences.
- **Cohesion:** every surface holds one world rather than stacking unrelated premium techniques.

Glass, glow, grain, logo walls, photographic atmosphere, marketing nav treatment, inset islands,
scroll-authored reveals, and oversized footer typography are intentionally absent because none serves
the universal reference or the three test briefs.

## Findings fixed during the audit

1. Contained Relay's wide data table with local inline-size, layout, and paint containment so it
   remains horizontally operable without widening the page.
2. Returned a toggled selection to its original state before the destructive fixture screenshot so
   the selected count, confirmation copy, and visible rows agree.
3. Removed the outdated grayscale/accent/signal banner, green live dot, boxed swatches, decorative
   divider, stale font defaults, and obsolete doctrine.
4. Added a reusable visually-hidden utility so table action headings stay available to assistive
   technology without entering visual layout.
5. Removed the resting edge while a field, textarea, composite shell, or select trigger owns visible
   focus, leaving one perceived focused boundary instead of an outline nested around a line.
6. Removed the green inline-start rail from toast feedback, applied the outcome to the full toast
   silhouette, and added a regression rule against partial-edge state markers on contained boxes.

## Result

The audited code-native surfaces pass the anti-slop check. Figma is outside this audit by explicit
owner direction.
