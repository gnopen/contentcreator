# Skill — Test Case Generator

Generate comprehensive test cases from a user story, requirement, or feature description.

---

## Purpose

Given a user story or feature, produce a structured set of test cases covering:
- Happy path scenarios
- Edge cases (boundary, timeout, null, empty)
- Negative scenarios (invalid input, unauthorized access)
- Cross-cutting concerns (accessibility, performance, security if relevant)

---

## Input Schema

The user provides:
- **User story or requirement** (required) — written in any form
- **Format preference** (optional) — Gherkin / plain steps / TestRail CSV / Xray
- **Coverage level** (optional) — minimal / standard / exhaustive
- **Specific concerns** (optional) — e.g., "focus on payment edge cases"

If format and coverage are not specified, ask once before generating.

---

## Output Format

### Default: Gherkin

```gherkin
Feature: [Feature Name]
  As a [user type]
  I want to [action]
  So that [outcome]

  Background:
    Given [common preconditions]

  # === HAPPY PATH ===

  Scenario: [Primary success scenario]
    Given [precondition]
    When [action]
    Then [expected outcome]

  # === EDGE CASES ===

  Scenario: [Boundary case]
    Given [edge condition]
    When [action]
    Then [expected behavior]

  # === NEGATIVE SCENARIOS ===

  Scenario: [Invalid input case]
    Given [invalid precondition]
    When [action]
    Then [expected error]
```

### Alternative: Structured Table

| ID | Category | Scenario | Steps | Expected Result | Priority |
|----|----------|----------|-------|------------------|----------|
| TC01 | Happy Path | User logs in with valid credentials | 1. Open login 2. Enter valid email 3. Enter valid pwd 4. Click submit | Redirected to dashboard | High |
| TC02 | Edge | Email with 254 characters | 1. Open login 2. Paste 254-char email | Accepted (RFC 5321) | Medium |

---

## Coverage Categories Checklist

When generating, walk through these categories explicitly. Skip categories that don't apply, but name them as skipped:

### 1. Happy Path
- Primary success scenario
- Alternative valid paths
- Different user roles / permission levels

### 2. Boundary Cases
- Minimum / maximum input values
- Empty / null / zero inputs
- Exact-at-limit values
- One-over and one-under limits

### 3. Negative Scenarios
- Invalid format inputs
- Unauthorized access attempts
- Missing required fields
- Mutually exclusive options selected together

### 4. State-Based Cases
- First-time user
- Returning user with existing data
- User with corrupted/incomplete state
- Concurrent action by another user

### 5. Environment Cases
- Different browsers (Chrome / Safari / Firefox / Edge)
- Different devices (desktop / tablet / mobile)
- Different OS versions
- Network conditions (offline / slow 3G / fast wifi)

### 6. Security Cases (if applicable)
- SQL injection attempts
- XSS payload in input fields
- CSRF token validation
- Session timeout / hijack scenarios

### 7. Performance Cases (if applicable)
- Large input volume
- Many concurrent requests
- Long-running operation
- Memory / resource limits

### 8. Accessibility Cases (if applicable)
- Keyboard-only navigation
- Screen reader compatibility
- High contrast mode
- Text scaling 200%

### 9. Internationalization Cases (if applicable)
- RTL languages (Arabic, Hebrew)
- Unicode characters (emoji, CJK)
- Different date / number / currency formats
- Long translations breaking UI

---

## Example Usage

**User input:**
> Generate test cases for: As a user, I want to upload a profile picture, so that my account feels personal. File size up to 5MB, formats JPG/PNG.

**Agent output:**
```gherkin
Feature: Profile Picture Upload
  As a registered user
  I want to upload a profile picture
  So that my account feels personalized

  Background:
    Given I am logged in
    And I am on my profile settings page

  # === HAPPY PATH ===

  Scenario: Upload a valid JPG
    Given I have a 2MB JPG image
    When I select the image and submit
    Then the image displays on my profile within 5 seconds
    And the image is also cached for next session

  Scenario: Replace existing profile picture
    Given I already have a profile picture
    When I upload a new valid PNG
    Then the new image replaces the old one
    And the old image is removed from storage

  # === BOUNDARY CASES ===

  Scenario: Upload file exactly at 5MB limit
    Given I have a JPG of exactly 5,242,880 bytes
    When I upload it
    Then the upload succeeds

  Scenario: Upload file one byte over limit
    Given I have a JPG of 5,242,881 bytes
    When I attempt to upload
    Then I see error "File exceeds 5MB limit"
    And no upload is initiated

  Scenario: Upload 1KB image (very small)
    Given I have a JPG of 1KB
    When I upload it
    Then the upload succeeds
    And the image displays without distortion

  # === NEGATIVE SCENARIOS ===

  Scenario Outline: Invalid file format rejected
    Given I have a file of type <format>
    When I attempt to upload
    Then I see error "Only JPG and PNG accepted"

    Examples:
      | format |
      | .gif   |
      | .bmp   |
      | .pdf   |
      | .exe   |
      | .svg   |

  Scenario: Upload corrupted image file
    Given I have a JPG with corrupted header
    When I attempt to upload
    Then I see error "File appears corrupted"

  Scenario: Filename with path traversal payload
    Given I have a file named "../../../etc/passwd.jpg"
    When I attempt to upload
    Then the filename is sanitized
    And no directory traversal occurs

  # === STATE-BASED ===

  Scenario: Upload interrupted by browser refresh
    Given I am uploading a 4MB file
    When I refresh the browser at 50% progress
    Then no partial file is stored
    And my previous profile picture remains

  # === SECURITY ===

  Scenario: Upload file with embedded script payload
    Given I have a JPG with EXIF metadata containing a script tag
    When I upload it
    Then the metadata is stripped before storage
    And no script executes when the image is rendered

  # === SKIPPED ===
  # - Internationalization: filename non-ASCII (defer; out of scope for v1)
  # - Performance: concurrent upload from 1000 users (load test, separate suite)
  # - Accessibility: drag-drop with screen reader (separate a11y audit)
```

---

## Customization Hooks

Edit the prompt that calls this skill to adjust:

| Variable | Default | Example override |
|----------|---------|-------------------|
| Output format | Gherkin | "Output as TestRail CSV with columns: title, steps, expected, type, priority" |
| Naming convention | TC01, TC02... | "Use prefix PAY- for payment tests, AUTH- for auth tests" |
| Severity scale | High/Medium/Low | "Use our P0/P1/P2 priority scale" |
| Tooling context | Generic | "We use Playwright, generate locator selectors where possible" |
| Compliance focus | None | "We handle HIPAA data, flag any test that touches PHI" |

---

## Quality Self-Check (Agent should verify before delivery)

- [ ] Happy path covered with at least 2 variations
- [ ] At least 3 boundary cases identified
- [ ] At least 2 negative scenarios per input field
- [ ] State-based cases considered (not just stateless)
- [ ] Security cases flagged if input is user-controlled
- [ ] Categories explicitly skipped are listed at the bottom
- [ ] Test IDs follow the user's naming convention (or default if not specified)
