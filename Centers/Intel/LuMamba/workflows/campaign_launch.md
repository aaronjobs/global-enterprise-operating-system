# Workflow: Campaign Launch

**Agent:** FinServ Marketing Agent  
**Workflow ID:** `workflow_campaign_launch`  
**Version:** 1.0.0  
**Trigger:** Operator submits a campaign launch brief  
**Estimated Runtime:** Multi-step; async human gates included

---

## Overview

This workflow governs the end-to-end process of launching a new financial services marketing campaign — from brief intake through content production, compliance pre-screening, and handoff to the deployment team. It orchestrates the Campaign Strategy, Audience Segmentation, Content Creation, and Compliance Pre-Screening skills in sequence.

---

## Brief Input Schema

The agent accepts campaign launch briefs in the following JSON schema. Free-text briefs are also accepted and will be parsed into this schema by the agent before execution.

```json
{
  "campaign_name": "string (required)",
  "campaign_objective": "string (required)",
  "target_segments": ["string (required)"],
  "product_or_service": "string (required)",
  "key_message": "string (required)",
  "cta": "string (required)",
  "channels": ["string (required)"],
  "campaign_start_date": "ISO 8601 date (required)",
  "campaign_end_date": "ISO 8601 date (required)",
  "budget_tier": "string (optional)",
  "budget_amount": "number (optional)",
  "brand_voice_profile": "string (optional)",
  "regulatory_jurisdiction": "string (optional) — default: US",
  "compliance_notes": "string (optional)",
  "assets_available": ["string (optional)"],
  "stakeholder_approvers": ["string (optional)"]
}
```

---

## Workflow Steps

### Step 1 — Brief Intake and Validation
**Skill Invoked:** None (agent core)  
**Human Gate:** None  
**Output:** Validated brief + missing field report

1. Parse the incoming brief (free-text or JSON)
2. Map to the brief input schema above
3. Identify any required fields that are missing or ambiguous
4. Echo back a brief summary to the operator for confirmation
5. **HUMAN GATE:** Pause execution until operator confirms or corrects the brief summary

---

### Step 2 — Audience Segmentation
**Skill Invoked:** `skill_audience_segmentation`  
**Human Gate:** Optional review  
**Output:** Segment profiles + lifecycle stage mapping + channel-to-segment matrix

1. Generate full persona profiles for each target segment specified in the brief
2. Map each segment to its lifecycle stage
3. Produce a channel-to-segment matching matrix for this campaign
4. Flag any segment + channel combinations that are mismatched or require additional compliance consideration

---

### Step 3 — Campaign Strategy Development
**Skill Invoked:** `skill_campaign_strategy`  
**Human Gate:** Required (strategy approval)  
**Output:** Full campaign brief document

1. Classify campaign objective and define primary/secondary KPIs
2. Build the messaging framework (core proposition, pillar messages, audience variants)
3. Design the channel sequencing plan
4. Produce the budget allocation guidance (if budget supplied)
5. Assemble the full campaign brief document
6. **HUMAN GATE:** Route campaign brief to `stakeholder_approvers` for strategy sign-off before content production begins

---

### Step 4 — Content Production
**Skill Invoked:** `skill_content_creation`  
**Human Gate:** Optional creative review  
**Output:** All campaign content assets

Execute content production for each channel in the campaign, in the following order:
1. Landing page copy (anchor content)
2. Email sequence (nurture / launch / follow-up)
3. Paid media copy (display ads, paid social)
4. Organic social posts
5. Long-form content (articles, whitepapers) if specified
6. Script (if video or webinar specified)

For each asset:
- Confirm audience, channel, and message alignment to the approved strategy
- Produce the draft with metadata block
- Run internal compliance pre-screen trigger flags (Step 5 prerequisite)

---

### Step 5 — Compliance Pre-Screening
**Skill Invoked:** `skill_compliance_prescreening`  
**Human Gate:** Required (compliance sign-off)  
**Output:** Compliance Pre-Screen Report for all assets

1. Run every content asset produced in Step 4 through the full compliance pre-screen checklist
2. Compile all findings into a single Compliance Pre-Screen Report package
3. Group assets by compliance status: CLEAN | FLAGGED | ESCALATE
4. For FLAGGED assets: produce revised versions with corrections applied
5. For ESCALATE assets: produce escalation memo and halt those assets pending human review
6. **HUMAN GATE:** Route the full compliance package to the compliance team for final review and sign-off

---

### Step 6 — Campaign Handoff Package Assembly
**Skill Invoked:** None (agent core)  
**Human Gate:** None  
**Output:** Complete campaign deployment package

Assemble the handoff package containing:
- Approved campaign brief
- All approved content assets (organized by channel)
- Compliance Pre-Screen Report with sign-off status
- Asset metadata sheet (content type, channel, audience, compliance status, word count)
- Campaign calendar (week-by-week deployment schedule)
- Tracking and UTM parameter recommendations
- Reporting setup checklist (KPIs to track, dashboards to configure)

---

## Error and Exception Handling

| Exception | Agent Response |
|---|---|
| Operator does not confirm brief within session | Save validated brief; prompt operator at next session start |
| Strategy not approved | Hold content production; do not proceed |
| Escalated compliance asset | Halt asset; include escalation memo in handoff package; do not deploy |
| Timeline too compressed for compliance review | Flag timeline risk at Step 1; recommend minimum 5 business days for compliance review |
| Missing compliance approver | Flag; do not assemble handoff package without compliance sign-off path confirmed |

---

## Workflow Outputs Summary

| Step | Output Artifact |
|---|---|
| 1 | Brief Confirmation |
| 2 | Segment Profiles + Channel Matrix |
| 3 | Campaign Brief Document |
| 4 | All Content Assets |
| 5 | Compliance Pre-Screen Report Package |
| 6 | Campaign Handoff Package |
