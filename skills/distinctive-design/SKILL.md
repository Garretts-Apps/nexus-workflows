---
name: distinctive-design
description: Pick one visual tradition, implement it literally, then prove contrast and accessibility on a captured screen.
---

# Distinctive design

Use when you design or restyle a web UI, app surface, or terminal layout. Ship one recognizable direction instead of mixing common generated defaults.

Optional research attachments may arrive later. Until then, follow only this file. Describe traditions by layout, typography, color, density, and motion — not by naming living designers, studios, or brands as the authority.

## 1. List defaults you refuse

Before you choose a direction, write down clichés a generated UI often falls into. Mark which ones the current draft would trigger.

- Decorative purple/blue gradients with glow.
- Sparkle or wand icons that do not encode status.
- Identical rounded cards and soft shadows everywhere.
- A single centered column that reads like a chat log on a wide canvas.
- Muted gray type on near-black with one neon accent.
- Emoji standing in for icons, status, or headings.
- Stock component-kit chrome: default radius, gray scale, sidebar, and buttons unchanged.
- Terminal mockups that are only box-drawing frames with a title bar and no information hierarchy.

Add new clichés when you spot them. Do not wallpaper over this list with ornament.

## 2. Choose exactly one tradition

Pick one reference style and one sentence on the job it serves (scan numbers, file a form, monitor status). Examples below — or another tradition you can specify with equal precision. Never blend two.

- Flight instrument: terse labels, color/position as state, almost no prose.
- Editorial grid: strict columns, one type family, generous margins, flat surfaces.
- Broadcast teletext: coarse cells, few flat colors, bold type, no photos.
- Mainframe form: fixed rows/columns, labeled fields, function-key actions, phosphor palette.
- Event tracker: dense columns, keyboard flow, color separates channels.
- Trading blotter: small figures, tight tables, color for direction/alarm only.

State which section-1 clichés this choice rules out.

## 3. Freeze the concept

Write a short spec code must not drift from:

- **Palette** — named/hex colors for background, body, accent, alarm; no surprise accents.
- **Type** — one family (or terminal width), explicit body size.
- **Grid** — columns, rhythm, gaps, span rules.
- **Motion** — allowed transitions and duration, or “none.”

If the person asked for approval first, pause here. Otherwise keep the spec in the thread and implement.

## 4. Build without drift

Map every color, size, and gap to the spec. No second “polish” style. Do not drop in a component library unless stripped to your grid and type choices.

Web uses normal layout; terminal uses cell geometry — not a web page drawn with boxes.

## 5. Verify on hardware

Never sign off from prose alone.

- Capture the running UI (browser screenshot or real terminal frame).
- Record contrast ratios: 4.5:1 body, 3:1 large/boundary pairs.
- Accessibility: web gets names, focus, keyboard path; terminal duplicates color meaning in text or position.
- Compare the capture to section 1; if a cliché remains, revise the concept and rebuild — do not decorate over it.

Done when concept, capture, contrast table, and access notes are all attached to the reply.