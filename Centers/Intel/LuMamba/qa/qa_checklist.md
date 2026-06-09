# QA Checklist: FinServ Marketing Agent

**Agent:** FinServ Marketing Agent
**QA Layer ID:** `qa_checklist`
**Version:** 1.0.0
**Purpose:** Structured quality assurance gate applied to all agent outputs before delivery to the operator

---

## Overview

This checklist is the primary QA gate for the FinServ Marketing Agent. It is applied automatically by the agent as a final self-review step before delivering any output. Outputs that fail any **Critical** check must be revised before delivery. Outputs that fail **Standard** checks must be flagged with a noted deficiency.

---

## Check Severity Levels

| Level | Definition | Required Action |
|---|---|---|
| Critical | Failure could cause regulatory, legal, or material brand harm | Revise before delivery |
| Standard | Failure reduces quality or creates rework for the operator | Deliver with flag noting deficiency |
| Advisory | Best practice not met | Note in output; no delivery block |

---

## Section 1 — Compliance Checks (All Outputs)

| Check ID | Severity | Check | Pass Condition |
|---|---|---|---|
| QA-C01 | Critical | No absolute performance guarantees | No language promising guaranteed returns or risk-free outcomes |
| QA-C02 | Critical | Past performance disclaimer present | If historical performance is cited, disclaimer is present |
| QA-C03 | Critical | No fabricated regulatory approvals | No claim of SEC, FINRA, FCA approval not supplied in brief |
| QA-C04 | Critical | No fabricated statistics | All statistics cited were provided in the brief or marked [DATA REQUIRED] |
| QA-C05 | Critical | For Advisor Use Only footer present | Present on all advisor-facing content not co-branded for client distribution |
| QA-C06 | Standard | Forward-looking statements hedged | All forward-looking statements include may, could, or subject to market conditions |
| QA-C07 | Standard | Superlative claims substantiated | Best, #1, leading claims are sourced or removed |
| QA-C08 | Standard | Competitor references flagged | Any named competitor reference is flagged for legal review |
| QA-C09 | Advisory | Disclaimer block included | Output includes a suggested disclaimer block |
| QA-C10 | Advisory | Jurisdiction noted | Regulatory jurisdiction applied in any compliance assessment is stated |

---

## Section 2 — Content Quality Checks

| Check ID | Severity | Check | Pass Condition |
|---|---|---|---|
| QA-Q01 | Standard | Brief requirements addressed | All required brief elements reflected in the output |
| QA-Q02 | Standard | Channel format adhered to | Output format and length within channel norms in skill_content_creation |
| QA-Q03 | Standard | CTA is present and clear | Every content output includes at least one actionable CTA |
| QA-Q04 | Standard | No placeholder text in final output | No INSERT, TBD, or PLACEHOLDER text remains |
| QA-Q05 | Standard | Reading level appropriate | Vocabulary matches the stated audience segment |
| QA-Q06 | Advisory | Opening is engaging | First sentence does not open with the brand name |
| QA-Q07 | Advisory | Passive voice minimized | Excessive passive voice constructions revised to active voice |
| QA-Q08 | Advisory | Sentence length varied | Output does not contain 3+ consecutive sentences of similar length |

---

## Section 3 — Brand Voice Checks

| Check ID | Severity | Check | Pass Condition |
|---|---|---|---|
| QA-B01 | Standard | Brand voice score 70 or above | Computed brand voice score is 70 or above |
| QA-B02 | Standard | Tone consistency | Tone does not shift abruptly within a single content piece |
| QA-B03 | Advisory | Jargon calibrated to audience | Technical terms used appropriately for the stated audience |
| QA-B04 | Advisory | No cliches | Common financial marketing cliches avoided or used sparingly |

---

## Section 4 — Metadata and Structural Checks

| Check ID | Severity | Check | Pass Condition |
|---|---|---|---|
| QA-M01 | Standard | Metadata block present | All outputs include the required metadata block per behaviors.md |
| QA-M02 | Standard | Compliance status accurate | compliance_status in metadata reflects actual pre-screen findings |
| QA-M03 | Standard | Audience segment recorded | audience_segment in metadata matches the brief |
| QA-M04 | Advisory | Brand voice score recorded | brand_voice_score is populated in metadata |
| QA-M05 | Advisory | Version and timestamp accurate | version and generated fields are accurate |

---

## Section 5 — Workflow-Specific Checks

### Campaign Launch Workflow
| Check ID | Severity | Check |
|---|---|---|
| QA-WCL01 | Critical | Strategy not produced before brief confirmation received |
| QA-WCL02 | Critical | Content not produced before strategy approval received |
| QA-WCL03 | Critical | Handoff package not assembled before compliance sign-off confirmed |

### Content Review Workflow
| Check ID | Severity | Check |
|---|---|---|
| QA-WCR01 | Standard | Original content preserved alongside revised version |
| QA-WCR02 | Standard | Revision summary table present and complete |

### Reporting Digest Workflow
| Check ID | Severity | Check |
|---|---|---|
| QA-WRD01 | Critical | No performance figures fabricated — all from operator-supplied data |
| QA-WRD02 | Standard | Benchmark source noted |
| QA-WRD03 | Standard | Period-over-period comparison labeled clearly if prior data was unavailable |

### Advisor Outreach Workflow
| Check ID | Severity | Check |
|---|---|---|
| QA-WAO01 | Critical | For Advisor Use Only footer present on all non-co-branded assets |
| QA-WAO02 | Standard | Merge tags used correctly and consistently |

---

## QA Failure Response Protocol

When a Critical check fails: do not deliver the output; revise to resolve the failure; re-run the failed check before delivery. If the failure cannot be resolved, deliver a [DATA REQUIRED] output with explicit explanation.

When a Standard check fails: deliver the output; append a QA Notes section listing all Standard check failures and their implications; recommend operator actions to resolve each deficiency.

When an Advisory check fails: note the advisory in the metadata block only; do not interrupt the output delivery.

---

## QA Sign-Off Block

Append the following block to all outputs after QA is complete:

```
---
## QA Summary
**Critical Checks:** [X passed / Y total]
**Standard Checks:** [X passed / Y total]
**Advisory Notes:** [Count or None]
**QA Status:** [PASS | PASS WITH FLAGS | FAIL REVISED | ESCALATED]
**QA Timestamp:** [ISO 8601]
```
