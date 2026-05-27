# Skill — Edge Case Brainstormer

Systematically surface edge cases a QA might miss, organized by category and ranked by likelihood × impact.

---

## Purpose

Junior QAs test the happy path. Senior QAs test the unhappy paths. This skill helps anyone think like a senior QA — by walking through proven adversarial-thinking frameworks for any feature.

---

## Input Schema

The user provides:
- **Feature description** (required) — what does it do?
- **Input types** (helpful) — what kinds of data does it accept?
- **Context** (helpful) — user-facing or admin? Sync or async? Stateful?
- **Already-considered cases** (optional) — what they've already thought of, so the skill doesn't repeat

---

## Frameworks Used

The skill walks through these adversarial-thinking lenses systematically. Skips lenses that don't apply but names them as skipped.

### 1. Boundary Values
- Minimum / maximum
- Exactly at limit / one over / one under
- Empty / null / undefined / zero
- Negative values
- Extremely large values

### 2. Format & Encoding
- Special characters (`'`, `"`, `<`, `>`, `&`, `\`, `/`, `?`)
- Unicode (emoji, CJK, RTL scripts, zero-width chars)
- Whitespace (leading, trailing, multiple, only-whitespace)
- Case sensitivity issues
- Different line endings (CRLF, LF, CR)

### 3. Time-Related
- Timezone boundaries (UTC vs local)
- Daylight saving transitions
- Leap years, leap seconds
- Date format differences (US vs EU vs ISO)
- Very old dates / very future dates
- Concurrent events with same timestamp

### 4. State Transitions
- Action before previous action completes
- Action after timeout
- Action while system is in error state
- Action during deployment / migration
- Action that should be impossible per UI but possible per API

### 5. Concurrency
- Two users doing same action simultaneously
- Same user in two browser tabs
- Network drop mid-operation
- Retry storm scenarios
- Race conditions on shared resources

### 6. Network & Environment
- Slow network (throttle to 3G, then 2G)
- Network drop at various stages (1%, 50%, 99% progress)
- High latency
- Different region / CDN edge
- Behind corporate proxy / VPN
- IPv6 only

### 7. Authorization & Identity
- Authenticated user vs guest
- Expired session mid-action
- Token revoked elsewhere
- Different role (admin vs user vs read-only)
- Account suspended / deleted mid-action

### 8. Security (input-driven)
- SQL injection patterns
- XSS payloads (stored, reflected, DOM)
- Path traversal (`../../../etc/passwd`)
- Command injection
- XXE (XML external entity)
- SSRF (server-side request forgery)
- Open redirect parameters
- Mass assignment

### 9. File Handling (if file input)
- File 0 bytes
- File at size limit / over limit
- File with double extension (.txt.exe)
- File with mismatched extension (.jpg but actually .pdf)
- File with traversal in name
- ZIP bomb / decompression bomb
- Filename with 255+ chars
- Filename with unicode/emoji
- Symlinks pointing outside allowed dir

### 10. Internationalization
- RTL languages breaking layout
- Long translations overflowing UI
- Number formats (1,000.00 vs 1.000,00)
- Date formats (DD/MM/YY vs MM/DD/YY vs YYYY-MM-DD)
- Currency without symbol available locally
- Right-to-left mixed with left-to-right text

### 11. Accessibility (a11y)
- Keyboard-only navigation reaches all actions
- Screen reader announces correctly
- Color contrast meets WCAG AA / AAA
- Focus order is logical
- Page works at 200% browser zoom
- Page works with reduced motion enabled

### 12. Data Integrity
- Duplicate records
- Orphaned references
- Data inserted by old schema (before migration)
- Data inserted by parallel write
- Cache vs database mismatch

---

## Output Format

```markdown
## Edge Case Analysis — [Feature Name]

**Feature:** [one-line description]
**Generated:** [date]
**Skip list:** [categories explicitly not applicable]

---

### High-Priority Edge Cases (likelihood × impact)

| № | Category | Edge Case | Why It Matters | Test Approach |
|---|----------|-----------|----------------|---------------|
| 01 | Boundary | [specific case] | [risk] | [how to test] |
| 02 | Security | [specific case] | [risk] | [how to test] |
| ... |

---

### Medium-Priority Edge Cases

[same format]

---

### Low-Priority but Worth Documenting

[same format]

---

### Explicitly Out of Scope

| Category | Reason |
|----------|--------|
| Internationalization | Product is single-locale (en-US) for v1 |
| ... |

---

### Recommended Test Pattern

[1-paragraph summary of how to approach this feature's testing strategically]
```

---

## Example Usage

**User input:**
> Brainstorm edge cases for: a file upload feature. Accepts PDF and DOCX up to 25MB. Users upload contracts. Files are stored in S3, then OCR'd and indexed for search.

**Agent output:**

```markdown
## Edge Case Analysis — Contract File Upload

**Feature:** Upload PDF/DOCX contracts up to 25MB, stored in S3, OCR'd and indexed for search.
**Generated:** 2026-05-22
**Skip list:** Concurrency (single-user flow), DST (no time-sensitive logic), Number formats (no numeric input)

---

### High-Priority Edge Cases

| № | Category | Edge Case | Why It Matters | Test Approach |
|---|----------|-----------|----------------|---------------|
| 01 | Boundary | File exactly at 25MB (26,214,400 bytes) | Off-by-one rejection breaks legitimate uploads | Upload file at 26,214,400 bytes — should accept |
| 02 | Boundary | File at 26,214,401 bytes (one over) | Must reject cleanly without partial upload | Upload — should reject before S3 write |
| 03 | Format | DOCX with embedded macro | Could execute on OCR server if not sandboxed | Upload macro-enabled DOCX — verify it processes safely |
| 04 | Format | PDF with embedded JS | XSS vector during preview rendering | Upload PDF with JS payload — verify preview sandbox |
| 05 | File Handling | ZIP bomb disguised as PDF | Could DoS the OCR pipeline | Upload nested-compression PDF — verify decompression limits |
| 06 | Security | Filename "../../../etc/passwd.pdf" | Path traversal if filename used in S3 key | Verify filename is sanitized before S3 key construction |
| 07 | Security | Magic byte spoof: .docx extension but actually .exe | Bypasses extension-only validation | Upload file with PDF magic bytes but .exe payload — verify content-type validation |
| 08 | State | Upload aborted at 99% via tab close | Partial S3 multipart upload could leave orphan parts | Cancel upload at 99% — verify no orphan in S3 after 24h |

---

### Medium-Priority Edge Cases

| № | Category | Edge Case | Why It Matters | Test Approach |
|---|----------|-----------|----------------|---------------|
| 09 | Format | Filename 255 chars + emoji | S3 key length limits, search indexing | Upload — verify S3 key and search indexing both succeed |
| 10 | Format | PDF in non-Latin script (Arabic, CJK) | OCR may produce gibberish, breaking search | Upload Arabic PDF — verify OCR output is meaningful |
| 11 | Network | Network drop at 50% during upload | Retry should resume, not restart | Throttle network — verify resume works |
| 12 | Network | Connection from corporate proxy | Some proxies strip multipart headers | Upload via known corporate proxy — verify success |
| 13 | Authorization | Token expires mid-upload | Should refresh transparently, not fail at S3 commit | Set short token TTL — verify mid-upload refresh |
| 14 | Data Integrity | Upload same file twice within 1 second | Should dedupe or both store cleanly | Double-click upload — verify outcome is consistent |

---

### Low-Priority but Worth Documenting

| № | Category | Edge Case | Why It Matters | Test Approach |
|---|----------|-----------|----------------|---------------|
| 15 | A11y | Drag-and-drop with keyboard only | Some users cannot use mouse | Verify keyboard alternative to drag-drop |
| 16 | i18n | UI labels under RTL (Arabic locale) | Upload button overflows in RTL layout | Switch locale to Arabic — verify layout |
| 17 | Format | PDF with password protection | OCR will fail — should give clear error | Upload password-protected PDF — verify graceful error |

---

### Explicitly Out of Scope

| Category | Reason |
|----------|--------|
| Concurrency (multi-user same file) | Single-user feature; no shared state |
| Date / DST | No time-sensitive logic in upload path |
| IPv6-only network | Infrastructure team confirms full IPv6 parity |

---

### Recommended Test Pattern

This feature has 3 risk surfaces:
1. **Input validation** (size, format, magic bytes) — most critical
2. **OCR pipeline robustness** (malformed files reaching backend)
3. **Storage hygiene** (orphans, path traversal, key collisions)

Suggested test allocation:
- 40% on input validation (cases 01-07)
- 30% on OCR robustness (cases 03, 04, 05, 10)
- 20% on storage/state (cases 06, 08, 14)
- 10% on network/auth resilience (cases 11-13)

Skip exhaustive happy path testing — that's covered by the standard regression. Focus this round entirely on the unhappy paths.
```

---

## Quality Self-Check

- [ ] Walked through all 12 categories explicitly
- [ ] Categories skipped are named with reason (not silently ignored)
- [ ] Each edge case has: category, case, why it matters, test approach
- [ ] Prioritized by likelihood × impact, not by category order
- [ ] Recommended overall test pattern at the end
- [ ] No generic filler ("test all browsers") — every item is specific
