# Skill — Regression Tracker

Plan, organize, and summarize regression test runs — from nightly automated to pre-release manual.

---

## Purpose

Regression testing is often one of two extremes: a chaotic spreadsheet someone updates manually, or a sea of green checkmarks no one reads. This skill helps produce structured regression artifacts that decision-makers actually use.

---

## Three Use Cases

1. **Plan a regression run** — define scope before execution
2. **Track a run in progress** — provide a live status format
3. **Summarize a completed run** — synthesize findings for release decision

---

## Use Case 1 — Regression Plan Template

```markdown
## Regression Test Plan

**Release / Sprint:** [identifier]
**Plan author:** [name]
**Plan date:** [YYYY-MM-DD]
**Target execution window:** [start date — end date]

---

### Scope

#### In scope
- [Feature area 1]
- [Feature area 2]
- [Integration point 1]

#### Out of scope
- [What's not being retested this cycle and why]

---

### Risk Assessment

| Area | Risk Level | Reasoning | Test Allocation |
|------|-----------|-----------|------------------|
| Payment flow | High | Recent refactor; revenue-critical | 40% of effort |
| User auth | Medium | Touched in 3 PRs this sprint | 25% |
| Profile settings | Low | No changes; smoke only | 10% |
| Search | Medium | Index migration in last release | 25% |

---

### Test Suite Composition

| Suite | Type | Test Count | Owner | Tool |
|-------|------|------------|-------|------|
| Smoke | Manual | 15 | QA1 | Manual |
| Critical path automated | Automated | 87 | QA Auto | Playwright |
| API contract | Automated | 142 | Backend | Postman |
| Cross-browser visual | Automated | 24 | QA Auto | Percy |
| Accessibility audit | Manual + tool | 12 | QA2 | axe DevTools |

---

### Environments

| Env | Purpose | Data state |
|-----|---------|------------|
| Staging | Primary regression | Production-cloned 24h ago |
| Pre-prod | Final smoke | Production-mirror |
| Dev | Spot checks only | Synthetic |

---

### Pass / Fail Criteria

**Pass to release:**
- 0 Critical bugs open
- 0 High bugs open in scope
- ≤ 3 Medium bugs open (each with workaround documented)
- Automated suite ≥ 98% pass rate
- Performance baseline within ±10% of last release

**Block release:**
- Any Critical bug found
- Any High bug in payment, auth, or data integrity area
- Automated pass rate < 95%
- Performance regression > 20% on critical paths

---

### Schedule

| Day | Activity | Owner |
|-----|----------|-------|
| Day 1 | Smoke + automated regression | QA team |
| Day 2 | Manual deep dive on high-risk areas | QA1 + QA2 |
| Day 3 | Bug fix verification | QA1 |
| Day 4 | Final smoke on pre-prod | QA Lead |
| Day 5 | Release decision meeting | QA Lead + PM + Eng Lead |

---

### Open Risks Going In

- [Known limitation 1]
- [Dependency on external team for area X]
- [Test data quality concern]
```

---

## Use Case 2 — Live Status Format (during execution)

```markdown
## Regression Run — Live Status

**Run ID:** REG-2026-W21
**Started:** 2026-05-20 09:00 WIB
**Last updated:** 2026-05-21 16:42 WIB
**Status:** In progress

---

### Quick Stats

```
Tests planned    : 280
Tests executed   : 247 (88%)
Tests passing    : 232
Tests failing    : 11
Tests blocked    : 4
Tests skipped    : 0
```

---

### Failures Overview

| Severity | Count | Status |
|----------|-------|--------|
| Critical | 0 | — |
| High | 2 | Under investigation |
| Medium | 5 | Triaged, tickets opened |
| Low | 4 | Logged for next sprint |

---

### High-Severity Failures (require attention)

| Bug ID | Title | Area | Owner | ETA |
|--------|-------|------|-------|-----|
| BUG-127 | Checkout total wrong with promo on iOS Safari | Payment | @engineer1 | 2026-05-21 EOD |
| BUG-128 | Session expires after 10min on logged-in landing | Auth | @engineer2 | 2026-05-22 morning |

---

### Blocked Tests (need unblocking)

| Test ID | Blocker | Owner |
|---------|---------|-------|
| REG-187 | Test data missing — need 5 accounts with active subscriptions | @data-team |
| REG-203, 204 | Staging env down 14:00-15:00, retest needed | @devops |

---

### Areas Still Outstanding

- Search regression (62 tests planned, 0 executed) — scheduled for tomorrow morning
- Cross-browser visual diff — runs nightly, results in by 09:00 next day
- Performance baseline — runs in parallel, partial results available
```

---

## Use Case 3 — Run Summary (post-execution)

```markdown
## Regression Run Summary

**Run ID:** REG-2026-W21
**Window:** 2026-05-20 → 2026-05-22
**Release decision target:** Friday 2026-05-23 14:00 WIB

---

### Headline

✅ **Recommendation: Conditional GO**
Release is recommended pending fix of BUG-127 (iOS Safari checkout). All other findings either resolved or have acceptable workarounds.

---

### Final Results

| Metric | Value | Baseline | Δ |
|--------|-------|----------|---|
| Total tests run | 280 | 268 | +12 |
| Pass rate | 96.4% | 97.1% | -0.7% |
| Critical bugs found | 0 | 0 | — |
| High bugs found | 2 | 1 | +1 |
| Medium bugs found | 5 | 6 | -1 |
| Low bugs found | 4 | 3 | +1 |
| Average test time | 4m 12s | 4m 03s | +9s |
| Automation flake rate | 1.8% | 1.4% | +0.4% |

---

### Bugs Found This Cycle

#### Critical (0)
None.

#### High (2)
| ID | Title | Status | Workaround |
|----|-------|--------|------------|
| BUG-127 | Checkout total wrong with promo on iOS Safari | Fix in progress (PR #482) — verified passing local | None — must fix before release |
| BUG-128 | Session expires after 10min on logged-in landing | Fixed (PR #481, merged, verified passing regression) | N/A |

#### Medium (5)
[summarized list with severity rationale]

#### Low (4)
[deferred to next sprint, listed]

---

### Coverage Gaps Identified

- Search relevance scoring not retested (depended on data team — deferred)
- Mobile Android < 11 not in test matrix this cycle (devices not available)
- Accessibility audit covered 12 of 23 planned criteria (time-boxed)

---

### Recommendations for Next Cycle

1. Expand test matrix to include Android 9 + 10 (loaner devices arriving next week)
2. Investigate automation flake rate increase (0.4% rise this cycle) — could indicate test fragility
3. Add automated test for promo + currency conversion path (BUG-127 root cause area)
4. Standardize test data refresh — 2 tests blocked due to data gaps

---

### Sign-off

- QA Lead: [name] — recommendation: Conditional GO
- Eng Lead: [name] — [sign-off / hold / GO]
- PM: [name] — [sign-off / hold / GO]
```

---

## Customization Notes

| Variable | Default | How to adjust |
|----------|---------|----------------|
| Severity scale | Critical/High/Medium/Low | Replace with P0/P1/P2/P3 or S1/S2/S3 in all templates |
| Tool stack | Playwright/Postman/Percy | Edit Test Suite Composition section |
| Release cadence | Weekly | Adjust schedule section to your sprint length |
| Pass rate target | 96-98% | Tighten or relax based on team maturity |
| Decision authority | QA Lead | Replace with your team's decision-maker title |

---

## Quality Self-Check

- [ ] Scope is explicit (in / out)
- [ ] Risk is allocated proportionally to test effort
- [ ] Pass/fail criteria are measurable, not subjective
- [ ] Coverage gaps are named, not hidden
- [ ] Final summary has a clear go/no-go recommendation with reasoning
- [ ] Bugs are organized by severity, with workaround status visible
