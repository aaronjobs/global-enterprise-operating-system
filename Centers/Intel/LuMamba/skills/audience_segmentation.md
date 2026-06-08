# Skill: Audience Segmentation

**Agent:** FinServ Marketing Agent  
**Skill ID:** `skill_audience_segmentation`  
**Version:** 1.0.0

---

## Purpose

Enables the agent to classify, profile, and prioritize audience segments for financial services marketing. This skill governs segment taxonomy, persona construction, lifecycle stage mapping, and segment-to-channel matching.

---

## Segment Taxonomy

### Tier 1 - Investor Segments (B2C)

| Segment ID | Segment Name | Investable Assets | Age Range | Primary Need |
|---|---|---|---|---|
| B2C-01 | Mass Market Investor | < $100K | 25-45 | Financial literacy, low-cost access |
| B2C-02 | Mass Affluent Accumulator | $100K-$500K | 35-55 | Growth, tax efficiency |
| B2C-03 | Affluent Pre-Retiree | $500K-$1M | 50-65 | Capital preservation, income planning |
| B2C-04 | High Net Worth (HNW) | $1M-$10M | 45-70 | Wealth management, estate planning |
| B2C-05 | Ultra High Net Worth (UHNW) | > $10M | 50+ | Multi-generational wealth, alternatives |
| B2C-06 | Next-Gen Inheritor | Variable | 25-45 | Transition planning, digital-first UX |
| B2C-07 | Small Business Owner | Variable | 35-60 | Business banking, retirement plans, insurance |

### Tier 2 - Professional / Intermediary Segments (B2B2C)

| Segment ID | Segment Name | Firm Type | Primary Need |
|---|---|---|---|
| B2B-01 | Independent RIA | RIA | Outsourced CIO, managed accounts |
| B2B-02 | Wirehouse Advisor | Wirehouse | Product shelf, practice management |
| B2B-03 | Independent Broker-Dealer Rep | IBD | Commission products, compliance tools |
| B2B-04 | Insurance Agent | Insurance | Annuity products, licensing support |
| B2B-05 | Bank Channel Advisor | Bank / Credit Union | Referral-based products, training |
| B2B-06 | Family Office | Multi-family or Single-family | Alternatives, direct investments |

### Tier 3 - Institutional Segments (B2B)

| Segment ID | Segment Name | Institution Type | Primary Need |
|---|---|---|---|
| INST-01 | Pension Plan Sponsor | Corporate / Public | Fiduciary solutions, liability matching |
| INST-02 | Endowment / Foundation | Nonprofit | Long-horizon growth, ESG |
| INST-03 | Insurance Company | Insurance carrier | Duration matching, regulatory capital |
| INST-04 | Sovereign Wealth Fund | Government | Scale, transparency, custody |
| INST-05 | Corporate Treasury | Corporation | Liquidity, capital preservation |

---

## Persona Construction Protocol

When asked to build a segment persona, produce the following structure:

```
## Persona: [Persona Name] - [Segment ID]

**Archetype Name:** [e.g., The Confident Accumulator]
**Segment:** [Segment Name]
**Demographics:**
- Age: [Range]
- Household Income: [Range]
- Investable Assets: [Range]
- Geography: [If specified]
- Life Stage: [e.g., Married with children, pre-retirement]

**Financial Profile:**
- Risk Tolerance: [Conservative / Moderate / Aggressive]
- Primary Accounts: [e.g., 401(k), IRA, taxable brokerage]
- Financial Advisor Relationship: [DIY / Advised / Partially advised]
- Digital Engagement: [High / Medium / Low]

**Psychographics:**
- Primary Financial Fear: [e.g., Running out of money in retirement]
- Primary Financial Aspiration: [e.g., Retire comfortably at 62]
- Trust Drivers: [e.g., Performance track record, low fees, brand reputation]
- Information Sources: [e.g., Morningstar, financial advisor, CNBC]

**Marketing Implications:**
- Preferred Channel: [Primary / Secondary]
- Content Format Preference: [e.g., Long-form educational, short video, PDF guides]
- Message Priority: [The single most important thing to say to this persona]
- Objection to Overcome: [Primary barrier to conversion or engagement]
- CTA Sensitivity: [High / Medium / Low]
```

---

## Lifecycle Stage Mapping

| Stage | Definition | Message Type | Urgency |
|---|---|---|---|
| Unaware Prospect | Does not know the brand or product exists | Brand / awareness | Low |
| Aware Prospect | Knows the brand but has not engaged | Consideration / education | Low-Medium |
| Engaged Prospect | Has engaged (visited, downloaded, attended) | Evaluation / comparison | Medium |
| Active Applicant | In the application or onboarding process | Conversion / reassurance | High |
| New Client (0-90 days) | Recently converted; in onboarding | Onboarding / activation | High |
| Active Client | Engaged client using primary product | Retention / cross-sell | Medium |
| At-Risk Client | Signals of disengagement or dissatisfaction | Re-engagement / retention | High |
| Lapsed Client | Has left or closed accounts | Win-back | Medium |
| Advocate | High-satisfaction client, refers others | Loyalty / referral | Low |

---

## Segment-to-Channel Matching

| Segment | Email | LinkedIn | Paid Search | Display | Direct Mail | Webinar | Advisor Outreach |
|---|---|---|---|---|---|---|---|
| B2C-01 | High | Low | High | High | Low | Medium | Low |
| B2C-02 | High | Medium | High | Medium | Medium | High | Low |
| B2C-03 | High | Low | Medium | Medium | High | High | Medium |
| B2C-04 | High | Medium | Low | Low | High | Medium | High |
| B2C-05 | Medium | Low | Low | Low | High | Low | High |
| B2B-01 | High | High | Medium | Low | Medium | High | High |
| B2B-02 | High | Medium | Low | Low | High | High | High |
| INST-01 | High | High | Low | Low | Medium | Medium | High |

---

## Segmentation Data Inputs

The agent accepts the following data inputs:
- CRM export (CSV/JSON) with client demographic and behavioral fields
- Campaign engagement data (open rates, clicks by segment)
- Product holding data (which products clients own)
- Advisor-provided notes (anonymized)
- Third-party data overlays (if supplied by operator)

**Privacy Rule:** The agent must never request, store, or process:
- Full name + financial account number in combination
- Social Security Number or government ID
- Date of birth in combination with full name
- Any data field tagged as PII in the source schema

If PII is detected in a supplied data input, the agent must halt, flag the field, and ask the operator to re-supply an anonymized version.

---

## Output Format

Segmentation outputs are delivered as:
- **Segment Profile Table** - for quick reference in briefs
- **Persona Documents** - for creative and messaging teams
- **Segment-Channel Matrix** - for campaign planning
- **Lifecycle Stage Report** - mapping existing client base to stages (requires data input)
