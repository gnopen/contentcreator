# Chapter 14 — New Ways to Be a QA

**Topic**: Niche-specific carousel for QA engineers. 4 augmented practices. Designed for high save & share rate in tech communities.

**Bold words**: *QA* (cover), *story* (folio 02), *steps* (folio 03), *sleep* (folio 04), *think* (folio 05), *mighty* (colophon)

---

## Paste-Ready Spec

```
Render Chapter 14 — "New Ways to Be a QA".

COVER:
Issue mark: "Chapter 14 — Profession Series"
Title-xl: "Six new ways<br>to be a <em>QA</em><br>in 2026."
Deck: "An operating manual for testers who want to ship faster, not be replaced faster."
Hero diagram: SVG kaca pembesar dengan bug kecil di dalam lensa, fill cobalt pada lensa, annotation [a] = "Inspect (deeper)", [b] = "Repeat (faster)", [c] = "Discover (wider)"
Caption: "Fig. 14 — The Augmented Tester"

FOLIO 02 — Type B:
Label: "Way No. 01"
Headline: "Test cases from<br>every user <em>story</em>,<br>in seconds."
Pull quote: "Saya udah generate 23 test cases dari ticket ini: 8 happy path, 9 edge cases (timeout, network drop, partial payment), 6 negative scenarios. Format Gherkin atau plain?"
Pull quote attr: "— Agent response, 04 sec elapsed"
Doc card kanan: Jira ticket mockup "TICKET PAY-2847" with title "User wants to checkout with multiple payment methods" and acceptance criteria list

FOLIO 03 — Type C:
Label: "Way No. 02"
Headline: "Reproducible <em>steps</em><br>from flaky bugs,<br>automatically."
Flow diagram: "Bug spotted → Agent reconstructs → Reproducible ticket"
Table:
  01 | Bug ID | → #2847 | Auto
  02 | Severity | → High | Detected
  03 | Environment | → iOS 17.4 Safari prod | Logged
  04 | Steps reproduced | → 5 of 5 | Verified
  05 | Console log | → Attached | Done

FOLIO 04 — Type A:
Label: "Way No. 03"
Headline: "Regression checks<br>while you <em>sleep</em>."
Body kiri: "Agent jalanin 240 test cases jam 2 pagi. Pagi buka laptop — udah ada report. 237 passed, 3 failed (1 false positive, 2 real). Bug tickets auto-created."
Mockup kanan: SVG bulan sabit dengan ceklis kecil di sebelahnya, fill cobalt di dalam bulan. Below: nightly run card "Nightly Run · 2026-05-21 02:00" — "Total · 240 | Passed · 237 | Failed · 3 | Auto-created tickets · 2"

FOLIO 05 — Type B:
Label: "Way No. 04"
Headline: "Edge cases you'd<br>never <em>think</em> of."
Pull quote: "Edge cases yang kamu mungkin lewat untuk fitur upload file: file 0 byte, filename 255 karakter + emoji, upload bersamaan 2 tab, network drop 99% progress, ZIP bom, filename traversal '../../../etc/passwd'."
Pull quote attr: "— Agent edge case analysis"
Doc card kanan: Edge case checklist card with 8 items, first 3 checked cobalt, rest unchecked, footer "Total · 8 | Reviewed · 3 | Awaiting · 5"

COLOPHON:
End mark: "End · Chapter 14 · Of 30"
Title-xl: "A QA can do<br><em>mighty</em> things."
End deck: "AI doesn't replace testers. It replaces the boring parts so testers can do what only humans can: think like adversaries."
Next: "Chapter 15 · The Morning Brief Agent"
```
