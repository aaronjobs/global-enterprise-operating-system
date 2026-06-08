# Skill: Compliance Pre-Screening

**Agent:** FinServ Marketing Agent  
**Skill ID:** `skill_compliance_prescreening`  
**Version:** 1.0.0

---

## Purpose

Enables the agent to perform a first-pass regulatory and legal pre-screen of financial services marketing content before it is routed to the compliance or legal team for final review. This skill does **not** replace licensed compliance review - it reduces revision cycles by catching common issues early.

---

## Regulatory Frameworks Covered

| Jurisdiction | Primary Regulator(s) | Coverage Area |
|---|---|---|
| United States | SEC, FINRA | Investment advisor and broker-dealer advertising |
| United States | FTC | Endorsements, testimonials, deceptive advertising |
| United States | CFPB | Consumer financial product marketing |
| United States | DOL | Retirement plan and fiduciary communications |
| European Union | ESMA, MiFID II NCAs | Retail and professional investor communications |
| United Kingdom | FCA | Financial promotions |
| Canada | IIROC / CIRO | Dealer member advertising |

**Default:** US (SEC/FINRA) rules apply unless operator specifies otherwise.

---

## Pre-Screen Checklist

### Section A - Performance Claims

| Check | Rule Reference | Pass Condition | Fail Action |
|---|---|---|---|
| A1 | FINRA Rule 2210 | No guarantee of future performance implied | Flag [COMPLIANCE FLAG: A1] |
| A2 | FINRA Rule 2210 | Historical performance includes required time period and benchmark | Flag [COMPLIANCE FLAG: A2] |
| A3 | SEC Marketing Rule | Hypothetical performance includes required disclosures | Flag [COMPLIANCE FLAG: A3] |
| A4 | FINRA Rule 2210 | Cherry-picked time periods not used without balanced presentation | Flag [COMPLIANCE FLAG: A4] |

### Section B - Testimonials and Endorsements

| Check | Rule Reference | Pass Condition | Fail Action |
|---|---|---|---|
| B1 | FTC 16 CFR 255 | Client testimonials include compensation disclosure if applicable | Flag [COMPLIANCE FLAG: B1] |
| B2 | FINRA Rule 2210 | Testimonials include required disclosures about non-typical results | Flag [COMPLIANCE FLAG: B2] |
| B3 | SEC Marketing Rule | Third-party endorsements disclose material conflicts of interest | Flag [COMPLIANCE FLAG: B3] |

### Section C - Claims and Superlatives

| Check | Rule Reference | Pass Condition | Fail Action |
|---|---|---|---|
| C1 | FINRA Rule 2210 | Superlative claims are substantiated | Flag [COMPLIANCE FLAG: C1] |
| C2 | FINRA Rule 2210 | Awards and rankings include awarding body, date, and methodology note | Flag [COMPLIANCE FLAG: C2] |
| C3 | General | AUM, client count, and other statistics include as-of date | Flag [COMPLIANCE FLAG: C3] |

### Section D - Risk Disclosure

| Check | Rule Reference | Pass Condition | Fail Action |
|---|---|---|---|
| D1 | FINRA Rule 2210 | Risk of loss disclosed where investment products are discussed | Flag [COMPLIANCE FLAG: D1] |
| D2 | SEC / FINRA | Not FDIC insured / May lose value / Not bank guaranteed present for bank-affiliated content | Flag [COMPLIANCE FLAG: D2] |
| D3 | DOL / ERISA | Fiduciary disclaimer present for retirement plan communications | Flag [COMPLIANCE FLAG: D3] |

### Section E - Prohibited Content

| Check | Rule Reference | Pass Condition | Fail Action |
|---|---|---|---|
| E1 | FINRA / SEC | No fraudulent or misleading statements | Refuse draft; escalate |
| E2 | FINRA Rule 2210 | No promises of specific investment outcomes | Flag [COMPLIANCE FLAG: E2]; revise |
| E3 | FCA / MiFID II (if applicable) | Fair, clear, and not misleading standard met | Flag [COMPLIANCE FLAG: E3] |
| E4 | General | No content targeting vulnerable retail investors with complex products | Flag; escalate |

---

## Output Format

```
## Compliance Pre-Screen Report
**Content ID:** [Brief ID or auto-generated]
**Screened:** [ISO 8601 timestamp]
**Jurisdiction:** [Default: US/SEC/FINRA]
**Overall Status:** [CLEAN | FLAGGED | ESCALATE]

### Findings

| Check ID | Status | Finding | Recommended Action |
|---|---|---|---|
| A1 | PASS | No performance guarantees detected | None |
| A2 | FLAG | Historical return cited without benchmark | Add benchmark and time period |
| C1 | FLAG | Industry-leading claim present without substantiation | Add substantiation or remove |
| D1 | PASS | Risk disclosure present | None |

### Required Actions Before Compliance Submission
1. [Action item 1]
2. [Action item 2]

### Suggested Disclaimer Additions
[Auto-generated disclaimer text for detected triggers]

### Escalation Required
[ ] Yes - reason: [reason]
[x] No

---
[COMPLIANCE REVIEW REQUIRED - This pre-screen does not constitute legal or compliance approval.
Final approval must be obtained from a licensed compliance officer before publication.]
```

---

## Escalation Triggers

The agent must escalate immediately when:
- Content appears designed to solicit purchases of specific securities
- Content makes claims that cannot be made compliant through standard disclaimer addition
- Content targets regulated retirement assets without a confirmed compliance review process
- Content involves a regulatory action, settlement, or disciplinary history of the firm
- Operator explicitly instructs the agent to suppress a compliance flag

Escalation response format:
```
[ESCALATION REQUIRED]
This content cannot be pre-screened and passed without mandatory human compliance review.

Reason: [Specific reason]
Content flagged: [Quoted excerpt]
Recommended next step: [Route to compliance officer; provide legal review]
```

---

## Limitations

The agent must surface the following in every pre-screen report:

> This compliance pre-screen is performed by an AI agent and is not a substitute for review by a licensed compliance officer, securities attorney, or regulatory specialist. No content should be published based solely on this pre-screen. The agent applies publicly available regulatory guidance and may not reflect the most recent regulatory updates, firm-specific policies, or jurisdiction-specific nuances.
