# Chapter 19 — Five Mistakes Building Agents

**Topic**: Five anti-patterns to avoid. Common failure modes with fixes.

**Bold words**: *skip* (cover), *mapped* (folio 02), *guardrails* (folio 03), *too* (folio 04), *refine* (folio 05), *gardens* (colophon)

---

## Paste-Ready Spec

```
Render Chapter 19 — "Five Mistakes Building Agents".

COVER:
Issue mark: "Chapter 19 — Anti-Patterns"
Title-xl: "Five common<br>traps and how<br>to <em>skip</em> them."
Deck: "Each of these I learned by hitting. Save yourself the receipts."
Hero diagram: SVG jalur berkelok dengan 5 titik, satu titik fill cobalt sebagai peringatan, annotation [a] = "Trap zone 1", [b] = "Trap zone 2", [c] = "Trap zone 3"
Caption: "Fig. 19 — The Five Common Traps"

FOLIO 02 — Type B:
Label: "Mistake No. 01"
Headline: "Building before<br>you <em>mapped</em> the<br>workflow."
Pull quote: "Automated a broken process. Got faster broken-ness. Lesson: clean the manual workflow first, then automate the cleaned version. Never the other order."
Pull quote attr: "— Postmortem, May 2024"
Doc card kanan: Anti-pattern card "Symptom · agent makes mistakes faster | Cause · automating without first removing redundancy | Fix · manual cleanup, then agent layer"

FOLIO 03 — Type B:
Label: "Mistake No. 02"
Headline: "Skipping the<br><em>guardrails</em>."
Pull quote: "First agent sent invoice with wrong client name. No review step. Now every agent has 'pause and confirm' before any irreversible action."
Pull quote attr: "— Postmortem, March 2024"
Doc card kanan: Guardrail checklist card "Mandatory Guardrails" — "✓ Human review on customer-facing | ✓ Confirmation on irreversible actions | ✓ Trusted domain whitelist | ✓ Spending caps | ✓ Daily activity audit"

FOLIO 04 — Type A:
Label: "Mistake No. 03"
Headline: "Making it do<br><em>too</em> much."
Body kiri: "An agent that handles email + calendar + invoicing + social = breaks in four ways. Five small agents > one mega-agent. Each does one thing well."
Mockup kanan: Architecture comparison card "BEFORE (mega-agent): 1 agent, 12 functions, fails in 12 ways | AFTER (modular): 5 agents, 2-3 functions each, isolated failures"

FOLIO 05 — Type C:
Label: "Mistakes No. 04 & 05"
Headline: "Forgetting to <em>refine</em>.<br>Treating it as magic."
Flow diagram: "Built once → Never touched → Stale by month 2"
Table:
  01 | Week 01 | → Built | Functional
  02 | Week 04 | → Untouched | Slight drift
  03 | Week 08 | → Untouched | Misaligned
  04 | Week 12 | → Untouched | Useless
  05 | Lesson | → Refine weekly | Always

COLOPHON:
End mark: "End · Chapter 19 · Of 30"
Title-xl: "Agents are <em>gardens</em>,<br>not statues."
End deck: "If you stopped tending it, you stopped owning it."
Next: "Chapter 20 · Inside My Studio"
```
