# Skill — Bug Report Formatter

Convert messy bug observations into clean, reproducible, ticket-ready reports.

---

## Purpose

A QA's raw notes after spotting a bug often look like: *"login broke on Safari mobile maybe? screenshot attached, happens sometimes."* This skill turns that into a structured ticket that engineering can act on immediately.

---

## Input Schema

The user provides (any subset):
- Raw notes describing the bug
- Screenshot or recording (optional, but described)
- Console logs / network logs (optional)
- Environment details (optional)
- Severity guess (optional)

The skill fills in gaps by asking targeted questions, then produces a clean report.

---

## Output Template

```markdown
## Bug Report

**ID:** BUG-[YYYYMMDD]-[NNN]
**Title:** [One-line summary, format: "[Component] action fails when condition"]
**Severity:** [Critical / High / Medium / Low]
**Status:** New
**Reporter:** [name or username]
**Date discovered:** [YYYY-MM-DD HH:MM TZ]

---

### Environment
- **Product version / commit:** [v1.2.3 or commit hash]
- **Environment:** [Production / Staging / Dev]
- **Platform:** [Web / iOS / Android / Desktop]
- **OS + version:** [e.g., iOS 17.4]
- **Browser + version:** [e.g., Safari 17.4 mobile]
- **Network conditions:** [Wifi / 4G / Offline / Slow 3G]
- **Account / role:** [Free user / Admin / Guest]

---

### Steps to Reproduce
1. [Specific action]
2. [Specific action]
3. [Specific action]
4. [Bug appears at this step]

---

### Expected Result
[What should have happened, in one sentence]

---

### Actual Result
[What actually happened, in one sentence + screenshot reference]

---

### Reproducibility
[Always / Sometimes (X out of Y attempts) / Rare]

---

### Impact
- **Users affected:** [estimate or "unknown until measured"]
- **Workaround:** [exists / none]
- **Blocks release?:** [Yes / No]

---

### Attached Evidence
- Screenshot: [link or filename]
- Video: [link or filename]
- Console log: [paste or attach]
- Network log: [paste or attach]
- HAR file: [link]

---

### Initial Investigation Notes
[Any clues from logs, recent deploys, similar past bugs]

---

### Suggested Owner
[Team / individual who likely owns this area]
```

---

## Severity Definitions (Default)

Adjust to match your team's standard.

| Level | Definition | Example |
|-------|------------|---------|
| **Critical** | Blocks core business function; revenue loss; data loss; security breach | Cannot complete purchase; PII leaked |
| **High** | Significant feature broken; many users affected; workaround painful | Cannot upload files; key dashboard blank |
| **Medium** | Feature degraded; some users affected; workaround available | Date picker shows wrong format; sort order wrong |
| **Low** | Cosmetic; rare; trivial workaround | Typo in label; misaligned icon by 2px |

---

## Asking Questions (when input is incomplete)

If the user's note is vague, ask the **minimum** needed questions in one batch. Don't interrogate.

### Example

**User input:**
> Saw a weird bug on the cart page, the total is wrong sometimes

**Agent response:**
> Before I format this, I need 3 things to make the ticket actionable:
>
> 1. **Reproducibility:** Did you see it once, or every time? If sometimes — any pattern (specific items, cart size, currency)?
> 2. **Environment:** Production, staging, or dev? Which browser and device?
> 3. **The actual numbers:** What was the expected total vs what showed? (Even ballpark is fine.)
>
> Once I have those, I'll generate the full report.

---

## Example: Raw → Formatted

### Raw input from user

> "OK so I was testing checkout on Safari iPhone, like the iPhone 15 Pro on iOS 17.4. Production. Adding 3 items, all under $50 each, used promo code WELCOME10. Should be $129.30 after the 10% off but it showed $143.67. Tried 4 times, happened all 4 times. Tax calculation looks off when promo applied. Have screen recording."

### Formatted output

```markdown
## Bug Report

**ID:** BUG-20260522-014
**Title:** [Checkout] Total calculation incorrect when promo code applied
**Severity:** High
**Status:** New
**Reporter:** QA Engineer
**Date discovered:** 2026-05-22 14:30 WIB

---

### Environment
- **Product version / commit:** [needs confirmation from user]
- **Environment:** Production
- **Platform:** iOS Mobile Web
- **OS + version:** iOS 17.4
- **Browser + version:** Safari (default version on iOS 17.4)
- **Network conditions:** Not noted
- **Account / role:** [needs confirmation — guest or logged-in?]

---

### Steps to Reproduce
1. Navigate to product catalog on Safari iOS 17.4
2. Add 3 items to cart, each priced under $50 (specific SKUs needed — confirm with reporter)
3. Proceed to checkout
4. Apply promo code "WELCOME10"
5. View order total

---

### Expected Result
Cart total should reflect 10% discount applied correctly. Per reporter's math: $129.30.

---

### Actual Result
Order total shown as $143.67. Discount appears not fully applied OR tax recalculation logic is incorrect when promo is active. Difference: $14.37.

---

### Reproducibility
Always (4 out of 4 attempts)

---

### Impact
- **Users affected:** Potentially every iOS Safari user using promo codes. Needs measurement from production analytics.
- **Workaround:** None — customer either overpays or abandons cart
- **Blocks release?:** Production-only issue; investigate immediately

---

### Attached Evidence
- Video: screen recording (referenced — attach file)
- Screenshot: needed (recommend capturing checkout summary view)
- Network log: not yet collected — request HAR file from Safari Web Inspector
- Console log: not yet collected

---

### Initial Investigation Notes
- Difference of $14.37 against expected $129.30 suggests tax is being calculated on pre-discount amount rather than discounted amount
- Could be a server-side promo application bug OR a client-side display issue
- Check if same scenario reproduces on:
  - Safari desktop (rule out mobile-specific)
  - Chrome iOS (rule out Safari-specific)
  - Without promo code (rule out promo logic vs tax logic)

---

### Suggested Owner
Checkout / Payments team — promo discount calculation pipeline
```

---

## Quality Self-Check (Agent should verify before delivery)

- [ ] Title is one line, format `[Component] specific failure mode`
- [ ] Severity matches team scale (not generic high/low without reasoning)
- [ ] Steps are numbered, specific, reproducible by someone who's never seen the bug
- [ ] Expected ≠ Actual is unambiguous
- [ ] Environment fully captured (or explicitly marked as needs-confirm)
- [ ] Reproducibility specified
- [ ] Suggested investigation directions listed
- [ ] No assumptions filled in as facts — anything uncertain is flagged
