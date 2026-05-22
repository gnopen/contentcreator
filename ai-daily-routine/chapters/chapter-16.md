# Chapter 16 — Anatomy of a Good Agent

**Topic**: 4-part anatomy — Trigger, Context, Action, Guardrail. Engineering principles.

**Bold words**: *agent* (cover), *start* (folio 02), *knows* (folio 03), *actually* (folio 04), *never* (folio 05), *boring* (colophon)

---

## Paste-Ready Spec

```
Render Chapter 16 — "Anatomy of a Good Agent".

COVER:
Issue mark: "Chapter 16 — Engineering Principles"
Title-xl: "The four parts<br>every working<br><em>agent</em> needs."
Deck: "A blueprint. Skip any of these and your agent will fail in a specific, predictable way."
Hero diagram: SVG blueprint-style diagram of simple robot dengan 4 area labeled, fill cobalt di kepala, annotation [a]/[b]/[c]/[d] = "Trigger / Context / Action / Guardrail"
Caption: "Fig. 16 — Agent Anatomy"

FOLIO 02 — Type D (Specimen):
Label: "Part No. 01 — Trigger"
Headline: "What makes it <em>start</em>."
Specimen grid:
  A: "Trigger · Time-based" | 01 | Scheduled | "Every morning 06:30, every Friday 17:00." | "Use · briefs, reports"
  B: "Trigger · Event-based" | 02 | Conditional | "New email from VIP, calendar conflict detected." | "Use · responses"
  C: "Trigger · Manual" | 03 | On-demand | "Voice command, hotkey, message." | "Use · ad-hoc tasks"

FOLIO 03 — Type A:
Label: "Part No. 02 — Context"
Headline: "What it already <em>knows</em>."
Body kiri: "Files loaded. Memory active. Voice profile attached. Past decisions accessible. The agent shouldn't ask you what it should already know."
Mockup kanan: Context inventory card "Active Context — Morning Brief Agent" with checkbox list: "✓ Brand voice doc | ✓ Past 30 emails | ✓ Customer list | ✓ Q3 OKRs | ✓ Style guide | ✓ Calendar permissions"

FOLIO 04 — Type C:
Label: "Part No. 03 — Action"
Headline: "What it <em>actually</em><br>does."
Flow diagram: "Read inputs → Process → Output"
Table:
  01 | Read inbox + calendar | → Source query | Auto
  02 | Categorize urgency | → LLM call | Auto
  03 | Draft response set | → LLM call | Auto
  04 | Save drafts to Gmail | → API write | Auto
  05 | Notify operator | → Slack ping | Auto

FOLIO 05 — Type B:
Label: "Part No. 04 — Guardrail"
Headline: "What it <em>never</em><br>does."
Pull quote: "Never sends without review. Never charges anything. Never replies to a domain not in trusted list. Never overrides your calendar without confirmation."
Pull quote attr: "— Guardrail policy, customer-facing agents"
Doc card kanan: Guardrail policy card with prohibition list, each with red prohibition icon: "🚫 Auto-send to clients | 🚫 Initiate payments | 🚫 Reply to unknown domains | 🚫 Override calendar | 🚫 Share private docs"

COLOPHON:
End mark: "End · Chapter 16 · Of 30"
Title-xl: "Good agents are<br><em>boring</em> by design."
End deck: "An exciting agent is one that surprised you. That's not the goal."
Next: "Chapter 17 · Skills for Creators"
```
