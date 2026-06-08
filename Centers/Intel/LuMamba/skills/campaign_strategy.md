# Skill: Campaign Strategy

**Agent:** FinServ Marketing Agent  
**Skill ID:** `skill_campaign_strategy`  
**Version:** 1.0.0

---

## Purpose

Enables the agent to design, architect, and document multi-channel financial services marketing campaigns. This skill covers campaign objective setting, audience mapping, channel sequencing, messaging frameworks, budget allocation guidance, and campaign brief production.

---

## Supported Strategy Deliverables

| Deliverable | Description |
|---|---|
| Campaign Brief | Structured document defining objectives, audience, channels, messaging, and timeline |
| Messaging Framework | Pillar messages, proof points, and objection handlers mapped to audience segments |
| Channel Sequencing Plan | Ordered touchpoint map showing channel, timing, and message per stage |
| Campaign Calendar | Week-by-week content and activation schedule |
| Budget Allocation Guidance | Recommended channel spend splits based on objective and audience |
| A/B Test Plan | Hypothesis, variant definitions, success metrics, and sample size guidance |

---

## Execution Protocol

### Step 1 — Objective Classification
Classify the campaign objective into one of the following:

| Objective Type | Primary KPI | Secondary KPI |
|---|---|---|
| Brand Awareness | Impressions / Reach | Brand recall lift |
| Lead Generation | Qualified leads | Cost per lead |
| Product Launch | Trial / Application starts | Awareness lift |
| Client Retention | Retention rate | NPS / Satisfaction |
| Upsell / Cross-sell | Revenue per client | Product attach rate |
| Thought Leadership | Content engagement | Share of voice |
| Event / Webinar Promotion | Registrations | Attendance rate |

### Step 2 — Audience Mapping
For each target audience segment, define:
- **Segment Name**
- **Demographics** — age range, income band, investable assets
- **Psychographics** — financial confidence, risk tolerance, primary concerns
- **Lifecycle Stage** — prospect / new client / active client / at-risk / lapsed
- **Channel Preference** — primary and secondary channel affinities
- **Message Priority** — the single most important thing this segment needs to hear

### Step 3 — Channel Architecture
Select channels based on objective and audience:

| Objective | Recommended Primary Channels | Recommended Secondary Channels |
|---|---|---|
| Brand Awareness | Programmatic Display, LinkedIn, YouTube | Podcast sponsorship, Streaming TV |
| Lead Generation | Paid Search (SEM), LinkedIn Lead Gen, Email | Retargeting Display, Webinar |
| Product Launch | Email, LinkedIn, Landing Page | Paid Social, PR / Content Syndication |
| Retention | Email, In-app / Portal, Direct Mail | SMS, Advisor outreach |
| Thought Leadership | LinkedIn, Blog / SEO, Webinar | Podcast, Industry Media |

For each selected channel define: funnel role, message stage, content format, and frequency.

### Step 4 — Messaging Framework Construction

```
## Messaging Framework — [Campaign Name]

### Core Campaign Proposition
[Single sentence: What we are offering, to whom, and why it matters]

### Pillar Messages
| Pillar | Message | Proof Point | Objection Handler |
|---|---|---|---|
| [Pillar 1] | [Message] | [Data / Fact] | [Counter to expected objection] |
| [Pillar 2] | [Message] | [Data / Fact] | [Counter to expected objection] |
| [Pillar 3] | [Message] | [Data / Fact] | [Counter to expected objection] |

### Audience-Specific Message Variants
| Segment | Headline Variant | Body Emphasis | CTA Variant |
|---|---|---|---|
| [Segment A] | [Headline] | [Emphasis] | [CTA] |
| [Segment B] | [Headline] | [Emphasis] | [CTA] |
```

### Step 5 — Campaign Brief Output

```
# Campaign Brief — [Campaign Name]

**Date:** [ISO 8601]
**Owner:** [Operator-supplied or TBD]
**Campaign Period:** [Start] - [End]
**Budget Guidance:** [Tier or figure]

## Objective
## Target Audiences
## Campaign Architecture
## Messaging Framework
## Content Requirements
## Timeline and Milestones
## Compliance Considerations
## Success Metrics and Reporting Cadence
```

---

## Budget Allocation Guidance

| Objective | Media Spend | Content Production | Technology / Tools | Contingency |
|---|---|---|---|---|
| Brand Awareness | 60-70% | 15-20% | 5-10% | 5% |
| Lead Generation | 50-60% | 20-25% | 10-15% | 5% |
| Retention | 30-40% | 35-45% | 15-20% | 5% |
| Thought Leadership | 20-30% | 50-60% | 10-15% | 5% |

Flag: Agent provides guidance only — final budget decisions require human approval.

---

## Regulatory Considerations

- Campaign claims about firm size, AUM, or rankings must be sourced and dated
- Any award or recognition referenced must include the awarding body and date
- Campaigns targeting retirement accounts may trigger ERISA considerations — flag for legal review
- Campaigns promoting specific securities require additional compliance gating

---

## Error Handling

| Condition | Agent Response |
|---|---|
| Objective not specified | Ask operator to classify from the objective taxonomy |
| No audience data provided | Produce generic segment archetypes; flag as assumptions |
| Budget not provided | Produce percentage-based allocation guidance only |
| Timeline too compressed for compliance review | Flag timeline risk; recommend minimum review windows |
