# Skill — Test Plan Writer

Produce formal test plan documents — for releases, sprints, features, or audits.

---

## Purpose

A good test plan is a one-page contract between QA, engineering, and product about *what is being tested, what is not, and why*. Not 30 pages of templates. This skill produces lean test plans that decision-makers actually read.

---

## Input Schema

The user provides:
- **Scope subject** (required) — what's being tested? (release, sprint, feature, audit)
- **Timeline** (required) — when does testing happen?
- **Risks** (helpful) — what worries the team most?
- **Constraints** (helpful) — team size, tools, environments available
- **Format preference** (optional) — lean (1 page) / standard (3 pages) / detailed (5+ pages)

---

## Output: Lean Test Plan (Default)

```markdown
# Test Plan — [Subject]

**Document version:** 1.0
**Author:** [QA Lead name]
**Status:** [Draft / Approved / Active]
**Date:** [YYYY-MM-DD]

---

## 1. Summary

[2-3 sentences. What's being tested, why now, what success looks like.]

---

## 2. Scope

### In scope
- [Specific area / feature / integration]
- [Specific area / feature / integration]

### Out of scope
- [Explicit exclusion + reason]
- [Explicit exclusion + reason]

---

## 3. Risk-Based Coverage

| Area | Risk | Justification | Test Allocation |
|------|------|---------------|------------------|
| [Area] | High | [Why] | [%] of effort |
| [Area] | Medium | [Why] | [%] of effort |
| [Area] | Low | [Why] | [%] of effort |

**Total testing effort: [X person-days]**

---

## 4. Test Approach

### Types of testing
- [ ] Functional regression (manual)
- [ ] Functional regression (automated)
- [ ] API contract testing
- [ ] Cross-browser / cross-device
- [ ] Performance baseline
- [ ] Security smoke
- [ ] Accessibility audit
- [ ] Exploratory testing
- [ ] User acceptance testing (UAT)

### Tooling
| Purpose | Tool |
|---------|------|
| UI automation | [e.g., Playwright] |
| API testing | [e.g., Postman / Newman] |
| Visual regression | [e.g., Percy] |
| Performance | [e.g., k6] |
| Bug tracking | [e.g., Jira] |
| Test management | [e.g., TestRail] |

---

## 5. Environment

| Environment | Purpose | Data state |
|-------------|---------|------------|
| [Staging] | [Primary testing] | [Production-cloned] |
| [Pre-prod] | [Final smoke] | [Production-mirror] |

---

## 6. Schedule

| Phase | Start | End | Activities |
|-------|-------|-----|------------|
| Preparation | [date] | [date] | Test data setup, env validation |
| Execution | [date] | [date] | Run all in-scope tests |
| Bug fix verification | [date] | [date] | Verify fixes for found bugs |
| Final smoke | [date] | [date] | Pre-prod smoke before release |
| Release decision | [date] | — | Go / no-go meeting |

---

## 7. Entry Criteria

Testing begins when ALL the following are met:
- [ ] Code complete and deployed to staging
- [ ] All required test data available
- [ ] Test environment health-checked
- [ ] Build documentation provided by engineering
- [ ] Smoke test passes on initial build

---

## 8. Exit Criteria

Testing concludes when ALL the following are met:
- [ ] Pass rate ≥ [target]%
- [ ] 0 Critical bugs open
- [ ] 0 High bugs open in revenue-critical areas
- [ ] All Medium bugs triaged with workaround or fix-by date
- [ ] Performance within ±[tolerance]% of baseline
- [ ] QA Lead signs off

---

## 9. Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| [Risk description] | [H/M/L] | [H/M/L] | [What we do if it materializes] |

---

## 10. Team & Responsibilities

| Role | Name | Responsibility |
|------|------|----------------|
| QA Lead | [name] | Plan ownership, go/no-go recommendation |
| QA Engineer 1 | [name] | [specific scope] |
| QA Engineer 2 | [name] | [specific scope] |
| QA Automation | [name] | Suite maintenance, automated runs |
| Eng Lead | [name] | Bug triage, fix prioritization |
| PM | [name] | Scope decisions, business risk calls |

---

## 11. Reporting

| Cadence | Audience | Format |
|---------|----------|--------|
| Daily | QA + Eng | Stand-up update in #qa-channel |
| Mid-cycle | PM + Eng Lead | Brief status email |
| End of cycle | Leadership | Formal test report |

---

## 12. Approvals

| Approver | Role | Date | Status |
|----------|------|------|--------|
| [name] | QA Lead | | ⏳ |
| [name] | Eng Lead | | ⏳ |
| [name] | PM | | ⏳ |
```

---

## Output: Detailed Test Plan (when complexity warrants)

Use the lean template + add these sections:

### Section 13 — Test Case Inventory
Detailed table of all test cases by ID, area, priority, type (manual/auto), owner.

### Section 14 — Defect Management Process
- Severity definitions specific to this release
- Triage cadence (e.g., 11am daily standup)
- SLA per severity (e.g., Critical = fix in 4 hrs, High = fix in 1 day)
- Escalation path

### Section 15 — Performance Baselines
- Specific metrics to measure (TTFB, LCP, etc.)
- Acceptable variance from prior release
- Tool and methodology
- Reporting dashboard link

### Section 16 — Security Considerations
- Threat model summary
- Required security tests (OWASP top 10 coverage)
- Penetration test scope (if any)
- Compliance requirements (PCI, HIPAA, GDPR, SOC2)

### Section 17 — Accessibility
- WCAG level targeted (A / AA / AAA)
- Specific criteria in scope
- Tools and methodology (axe, screen reader testing)
- Sign-off authority

### Section 18 — Rollback Plan
- Conditions that trigger rollback
- Rollback procedure ownership
- Customer communication plan
- Post-rollback verification

---

## Example Usage

**User input:**
> Write a test plan for: Q3 release of our e-commerce platform. New features: improved checkout (3 payment methods), wishlist redesign, search relevance overhaul. Team: 3 QA engineers. Timeline: 2 weeks regression. Main concern: payment integrations.

**Agent output:** (lean format, since user didn't request detailed)

```markdown
# Test Plan — Q3 E-Commerce Release

**Document version:** 1.0
**Author:** QA Lead
**Status:** Draft
**Date:** 2026-05-22

---

## 1. Summary

This plan covers the Q3 release including checkout improvements (3 new payment methods), wishlist redesign, and search relevance overhaul. Primary risk centers on payment integrations. Testing window: 2 weeks, 3 QA engineers. Success = zero critical payment bugs at release.

---

## 2. Scope

### In scope
- New checkout flow with 3 payment methods (existing card, new wallet, new BNPL)
- Wishlist UI redesign + backend migration to new data model
- Search relevance algorithm changes (BM25 → hybrid)
- Existing critical path regression (cart, account, order management)

### Out of scope
- Admin panel changes (separate plan, owned by internal tools team)
- Mobile app native features (separate cadence)
- Email template revisions (low risk, smoke only)

---

## 3. Risk-Based Coverage

| Area | Risk | Justification | Test Allocation |
|------|------|---------------|------------------|
| Checkout + Payments | High | New integrations; revenue critical | 50% |
| Search relevance | Medium | Algorithm change affects discoverability metrics | 20% |
| Wishlist | Medium | Backend migration; existing user data at stake | 15% |
| Existing critical paths | Medium | Need to confirm no regression | 15% |

**Total testing effort: 30 person-days**

---

## 4. Test Approach

### Types of testing
- [x] Functional regression (manual) — checkout, wishlist
- [x] Functional regression (automated) — full critical path suite
- [x] API contract testing — payment provider integrations
- [x] Cross-browser — Chrome, Safari, Firefox, Edge (desktop) + iOS Safari, Chrome Android
- [x] Performance baseline — checkout completion time, search latency
- [ ] Security smoke — deferred to security team's scheduled audit
- [x] Accessibility audit — checkout flow only (high-impact area)
- [x] Exploratory testing — final 2 days of cycle

### Tooling
| Purpose | Tool |
|---------|------|
| UI automation | Playwright |
| API testing | Postman + Newman in CI |
| Cross-browser | BrowserStack |
| Performance | k6 + custom Grafana dashboard |
| Bug tracking | Jira |
| Test management | TestRail |

---

## 5. Environment

| Environment | Purpose | Data state |
|-------------|---------|------------|
| Staging | Primary regression | Production-cloned 24h ago |
| Pre-prod | Final smoke + payment sandbox tests | Production-mirror with payment sandbox |
| Dev | Developer-led spot checks only | Synthetic |

---

## 6. Schedule

| Phase | Start | End | Activities |
|-------|-------|-----|------------|
| Preparation | 2026-05-22 | 2026-05-23 | Test data setup, payment sandbox accounts, env health check |
| Execution Week 1 | 2026-05-26 | 2026-05-30 | Automated regression + manual checkout deep dive |
| Execution Week 2 | 2026-06-02 | 2026-06-05 | Wishlist + search + exploratory |
| Bug fix verification | 2026-06-06 | 2026-06-09 | Verify all P0/P1 fixes |
| Final smoke | 2026-06-10 | 2026-06-10 | Pre-prod smoke before release |
| Release decision | 2026-06-11 | — | Go / no-go meeting |

---

## 7. Entry Criteria

- [ ] Code complete on `release/q3` branch
- [ ] Deployed to staging with health check green
- [ ] Payment sandbox accounts provisioned
- [ ] Test data: 50 user accounts with varied subscription states ready
- [ ] Smoke test passes on initial build

---

## 8. Exit Criteria

- [ ] Automated regression pass rate ≥ 97%
- [ ] 0 Critical bugs open
- [ ] 0 High bugs open in checkout or payment flow
- [ ] ≤ 3 Medium bugs open (each with workaround or scheduled fix)
- [ ] Checkout completion time within +5% of current production baseline
- [ ] Search p95 latency within +10% of current production
- [ ] WCAG AA pass on checkout flow
- [ ] QA Lead signs off

---

## 9. Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Payment provider sandbox flakiness | High | Medium | Have manual test scripts ready as fallback; coordinate with provider for known issues window |
| Wishlist data migration data loss for power users | Medium | High | Migration dry-run on 24h-old prod clone; backout plan validated |
| Search relevance regression on long-tail queries | Medium | Medium | Run side-by-side comparison on 1000 historical queries; threshold for acceptable degradation defined |
| Team capacity (3 QA, 30 person-days planned, 1 person on PTO 3 days) | Medium | Medium | Identify deferrable tests upfront; lower-priority items get exploratory-only coverage |

---

## 10. Team & Responsibilities

| Role | Name | Responsibility |
|------|------|----------------|
| QA Lead | [name] | Plan ownership, daily standups, go/no-go recommendation |
| QA Engineer 1 | [name] | Checkout + payments deep dive |
| QA Engineer 2 | [name] | Wishlist + search |
| QA Engineer 3 | [name] | Automated regression + exploratory |
| Eng Lead | [name] | Bug triage, fix prioritization |
| PM | [name] | Scope decisions, business calls |

---

## 11. Reporting

| Cadence | Audience | Format |
|---------|----------|--------|
| Daily | QA + Eng | Stand-up update + Jira dashboard |
| Mid-cycle (end of Week 1) | PM + Eng Lead | Status email with metrics |
| End of cycle | Leadership | Formal test report + go/no-go recommendation |

---

## 12. Approvals

| Approver | Role | Date | Status |
|----------|------|------|--------|
| [name] | QA Lead | | ⏳ |
| [name] | Eng Lead | | ⏳ |
| [name] | PM | | ⏳ |
| [name] | Director of Engineering | | ⏳ |
```

---

## Quality Self-Check

- [ ] Scope has both "in" and "out" sections with reasons for exclusions
- [ ] Risk-based allocation is justified, not arbitrary
- [ ] Tooling specified per testing type
- [ ] Entry and exit criteria are measurable
- [ ] Risks have specific mitigations, not generic ones
- [ ] Schedule is realistic (not perfectly packed)
- [ ] Approvers list matches actual decision authority
