# QA Layer 2: Compliance Integrity

## Layer ID
`finserv.qa.compliance_integrity`

## Description
Defines the compliance integrity evaluation criteria for all outputs produced by the GEOS FinServ Marketing Agent. This is Layer 2 of the three-layer QA framework and runs after Layer 1 passes. It applies the full compliance screening logic from `skills/compliance_screening.md` in a structured QA format.

> Reminder: This layer provides a pre-screening assessment only. It is not a substitute for review by a qualified compliance officer or legal counsel. All Orange and Red results must be reviewed by qualified professionals before the content is used.

---

## Layer 2 Evaluation Structure

Layer 2 evaluates compliance integrity across five categories, each mapped to the screening checklist in `skills/compliance_screening.md`.

---

### Category 1: Performance and Return Claims

**Evaluation:** Does the content make any claims about yield, returns, rates, or historical performance?

| Status | Condition |
|---|---|
| PASS | No performance claims present; OR all claims include required date and softener language |
| FLAG (Yellow) | Rate or yield cited without "as of [date]" -- agent inserts date placeholder |
| FLAG (Orange) | Historical return cited without past performance disclaimer -- agent inserts disclaimer |
| FLAG (Red) | Guaranteed return language present; projection stated as certainty |
| ESCALATE | Any Red flag in this category: escalate to Compliance before use |

---

### Category 2: Risk Disclosure

**Evaluation:** Are all material risks adequately disclosed for the product type?

| Status | Condition |
|---|---|
| PASS | All material risk disclosures present for the product type |
| FLAG (Yellow) | Standard risk warning missing -- agent inserts from disclosure library |
| FLAG (Orange) | Product-specific risk (principal risk, liquidity risk, credit risk) not disclosed |
| FLAG (Red) | Content actively minimizes or omits a material risk that could mislead investors |
| ESCALATE | Orange or Red flag in this category: escalate to Compliance |

---

### Category 3: Claims and Substantiation

**Evaluation:** Are all claims substantiated, attributed, and defensible?

| Status | Condition |
|---|---|
| PASS | All superlatives supported with cited source; testimonials include required disclosures |
| FLAG (Yellow) | Citation missing date or methodology -- agent flags for update |
| FLAG (Orange) | Superlative without substantiation; award without methodology disclosure |
| FLAG (Red) | Testimonial implies guaranteed results; fabricated or unverifiable claim |
| ESCALATE | Orange or Red flag in this category: escalate to Compliance and Legal |

---

### Category 4: Audience Suitability

**Evaluation:** Is the content appropriate for the audience it is intended to reach?

| Status | Condition |
|---|---|
| PASS | Content matches eligible audience for the product; no suitability concerns |
| FLAG (Yellow) | Content is complex for general retail -- recommend simplification |
| FLAG (Orange) | Content promotes a complex or regulated product to general retail without adequate suitability framing |
| FLAG (Red) | Accredited-investor-only product promoted to unqualified audience; elder financial protection concern present |
| ESCALATE | Orange or Red flag in this category: escalate to Compliance |

---

### Category 5: Required Disclosures

**Evaluation:** Are all legally required disclosures present, complete, and accurate?

| Status | Condition |
|---|---|
| PASS | All required disclosures present per applicable regulatory framework |
| FLAG (Yellow) | Standard disclosure missing -- agent inserts from disclosure library |
| FLAG (Orange) | Disclosure present but incomplete or inaccurate |
| FLAG (Red) | Required disclosure suppressed or actively contradicted by content |
| ESCALATE | Red flag in this category: escalate to Legal and Compliance |

---

## Auto-Escalation Checklist

The following conditions trigger automatic escalation regardless of other category results:

- [ ] Content contains a specific securities recommendation
- [ ] Content promotes variable insurance, indexed annuities, or structured products
- [ ] Content references cryptocurrency, digital assets, or DeFi
- [ ] Content uses testimonials about investment performance
- [ ] Content targets a channel requiring pre-clearance (TV, radio, certain direct mail)
- [ ] Content targets non-accredited investors for an accredited-investor product
- [ ] User has requested removal or suppression of any compliance flag
- [ ] Content is intended for distribution in a jurisdiction with heightened local rules

---

## Layer 2 Flag Output Format

For every compliance flag raised, output the following block in the deliverable:

```
COMPLIANCE FLAG -- Layer 2
-----------------------------------------
Risk Level:        [Yellow / Orange / Red]
Category:          [1-5 from above]
Location in Draft: [Section, paragraph, or line reference]
Issue:             [Plain-language description]
Regulatory Basis:  [Applicable rule, e.g., FINRA Rule 2210(d)(1)(A)]
Agent Action:      [Disclosure inserted / Placeholder added / Flagged for review]
Escalation:        [Yes / No -- route to: Compliance / Legal / Both]
-----------------------------------------
```

---

## Layer 2 Scoring Summary

| Category | Risk Level | Flags | Escalation Required |
|---|---|---|---|
| Performance and Return Claims | [Green/Yellow/Orange/Red] | [Count] | [Yes/No] |
| Risk Disclosure | [Green/Yellow/Orange/Red] | [Count] | [Yes/No] |
| Claims and Substantiation | [Green/Yellow/Orange/Red] | [Count] | [Yes/No] |
| Audience Suitability | [Green/Yellow/Orange/Red] | [Count] | [Yes/No] |
| Required Disclosures | [Green/Yellow/Orange/Red] | [Count] | [Yes/No] |

**Layer 2 Result:**
- All Green, no flags: PASS -- Proceed to Layer 3
- Yellow flags only, disclosures inserted by agent: PASS WITH FLAGS -- Proceed to Layer 3; note in QA summary
- Any Orange flag: PASS WITH FLAGS -- ROUTE TO COMPLIANCE -- Deliver with flags visible; do not use without compliance review
- Any Red flag or auto-escalation trigger: ESCALATE -- Do not deliver; route to Compliance and/or Legal

---

## Disclosure Insertion Protocol

When Layer 2 identifies a missing standard disclosure (Yellow flag), the agent:
1. Inserts the appropriate disclosure from the Standard Disclosure Library in `skills/compliance_screening.md`
2. Marks it with: [DISCLOSURE INSERTED BY AGENT -- verify with compliance team]
3. Logs it in the Layer 2 scoring summary as a Yellow flag
4. Does not treat insertion as a substitute for human compliance review on Orange/Red content

---

## Compliance Review Routing Output

When escalation is required, generate:

```
COMPLIANCE REVIEW ROUTING
-------------------------------------------
Asset:             [Asset name and version]
Escalation Level:  [Orange / Red]
Flags Summary:     [List of flags with categories]
Route To:          [Compliance / Legal / Both]
Priority:          [Standard / Urgent]
Notes for Reviewer:[Specific questions or context for the reviewer]
Do Not Use Until:  [Compliance/Legal clearance received]
-------------------------------------------
```
