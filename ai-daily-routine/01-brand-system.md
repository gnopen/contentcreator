# Brand System — Field Manual / Atelier Blue

## Identity Direction

**Field Manual** — premium technical journal aesthetic. Not "soft editorial book" (Anthropic-style). Not "tech-startup gradient" (OpenAI/SaaS-style). Not "playful illustrated" (consumer-app-style).

Reference parallels: Monocle magazine, Bloomberg Businessweek, Werner Herzog production notes, Dieter Rams catalog, architectural blueprint.

## Color Palette — Atelier Blue

| Token | Hex | Use |
|-------|-----|-----|
| `bg.slide` | `#DDE6EE` | Slide background (mist blue) |
| `ink.primary` | `#0A1F3D` | All headline + primary text (deep navy) |
| `ink.muted` | `#4A5A7A` | Body paragraph text |
| `accent.cobalt` | `#2E5AAC` | Underline emphasis, send buttons, accent fills |
| `surface.card` | `#FAFCFE` | Mockup/document card background (cool white) |
| `slate.metadata` | `#88A4C9` | Page numbers, captions, register marks, metadata |
| `divider` | `#B5C2D0` | Hairline borders, dividers |
| `body.bg` | `#1a1a1a` | Dark container around slides (artifact preview only) |

## Typography System (3-font stack)

| Font | Source | Use |
|------|--------|-----|
| **Fraunces** | Google Fonts (300 / 400 / 600 / 700) | All headlines, decks, document headings, big folio numerals |
| **Inter** | Google Fonts (400 / 500 / 600) | Body text, mockup UI text |
| **IBM Plex Mono** | Google Fonts (400 / 500 / 600) | All metadata, labels, captions, masthead, footer, table headers |

### Type Scale

| Level | Font | Size | Line-height | Use |
|-------|------|------|-------------|-----|
| `title-xl` | Fraunces 300 | 120px | 0.95 | Cover & colophon titles |
| `title-lg` | Fraunces 300 | 88px | 0.98 | Folio 02-05 headlines |
| `deck` | Fraunces italic 400 | 28px | 1.35 | Subtitles/deck after title |
| `body-text` | Inter 400 | 20px | 1.55 | Body paragraphs |
| `label` | IBM Plex Mono 500 | 11px | — | All-caps labels w/ 0.14em letter-spacing |
| `caption` | IBM Plex Mono 400 | 12px | — | All-caps captions w/ 0.10em letter-spacing |
| `folio.bg` | Fraunces 300 | 320px | 1.0 | Background Roman numeral (opacity 0.06) |

### Emphasis Rule (CRITICAL)

**One keyword per headline gets emphasized.** The emphasis is NOT bold weight — it is a cobalt highlight bar behind the text. Implemented via `<em>` tag with `::after` pseudo-element creating a 5-6px cobalt bar positioned behind the text (z-index: -1).

This is the single most distinctive typographic move. Bold weight is forbidden for emphasis.

## Slide Anatomy (Universal)

Every slide has these mandatory elements:

1. **Register marks** — 4 small circles (18px) with crosshair at each corner, color `#88A4C9`. Architectural detail.
2. **Masthead** — top bar with two-column mono text + 1px ink hairline below. Left: chapter info. Right: folio info.
3. **Footer** — bottom bar with 1px ink hairline above + two-column mono text. Left: `Vol. 01 / 30 — Chapter X — Folio XX`. Right: `@aidailyroutine` (or `DM 'AGENT' — waitlist` for CTA-heavy slides).
4. **Body area** — content varies by folio type.

## Folio System

- **Slide 1 (Cover)**: no Roman numeral, hero diagram with grid pattern background
- **Slide 2**: Roman numeral `I` (large, opacity 0.06, background-positioned)
- **Slide 3**: Roman numeral `II`
- **Slide 4**: Roman numeral `III`
- **Slide 5**: Roman numeral `IV`
- **Slide 6 (Colophon)**: no Roman numeral, end-mark with cobalt dots

Roman numerals alternate left/right positioning per slide for visual rhythm.

## Visual Types (per folio)

| Type | Layout | Use case |
|------|--------|----------|
| **A** | Body text (left col) + Mockup card (right col, partially out of frame) with `[a][b][c]` annotations | Tool demos, configurations |
| **B** | Pull quote (with 180px curly mark) + Document card (right) | Quotes, postmortems |
| **C** | Flow diagram (3-node Input→Process→Output) + Table (№/Task/Owner/Status) | Workflows, schedules |
| **D** | 3-column specimen grid (label + big numeral + name + body + meta) | Comparisons, categorizations |
| **E** | Sidebar comparison (left vs right, divided) | Before/after, preferred/avoid |

## Annotation System

- **Marker**: 22px circle, 1.5px cobalt border, contains digit 1/2/3
- **Connector**: dotted line `stroke-dasharray "2,3"`, cobalt
- **Label**: `[a] = description` in IBM Plex Mono 13px

Used to label diagram elements, mockup details, or reference points within slides.

## Pull Quote Treatment

- Body: Fraunces italic 26px, line-height 1.4
- Quotation mark: massive 180px Fraunces serif, cobalt color, positioned absolute behind the quote text
- Attribution: IBM Plex Mono 12px uppercase letter-spacing 0.12em, slate color

## Card / Mockup Spec

- Background: `#FAFCFE`
- Border: 1px `#B5C2D0`
- Border-radius: 4px (more square than rounded — technical feel)
- Shadow: `0 8px 32px rgba(10, 31, 61, 0.06)`
- Header bar (if applicable): cobalt background, cool-white text, mono font uppercase
- Table header: ink-navy background, cool-white text
- Highlighted row/cell: linear-gradient transparent 60% → cobalt 25% (subtle hover-like marker)

## Absolute Rules

1. One keyword per headline gets cobalt underline emphasis (via `<em>`)
2. Bold font-weight is **forbidden** for emphasis
3. No emoji in body or headline (allowed only inside mockup UI when natural)
4. All metadata uses IBM Plex Mono uppercase with letter-spacing
5. No gradients, no soft shadows, no decorative flourishes
6. Whitespace is non-negotiable — empty space is design
7. Color palette is the identity — never substitute

## Why This System Works

- **Distinct in feed**: cool blue editorial stops the scroll among warm/saturated AI content
- **Premium signal**: technical journal aesthetic = perceived expertise
- **Sustainable**: same template, 30 instances — visual identity locked
- **Scalable**: any future chapter (post-Day 30) inherits identity automatically
- **Recognizable**: someone scrolling can identify a slide as yours from thumbnail
