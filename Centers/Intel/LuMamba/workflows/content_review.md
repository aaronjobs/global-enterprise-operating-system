# Workflow: Content Review

**Agent:** FinServ Marketing Agent  
**Workflow ID:** `workflow_content_review`  
**Version:** 1.0.0  
**Trigger:** Operator submits existing content for review and revision  
**Estimated Runtime:** Single-session; human gates as noted

---

## Overview

This workflow governs the review, scoring, and revision of existing financial services marketing content. It is used when the operator has already-drafted content that needs brand voice scoring, compliance pre-screening, audience alignment assessment, or copy improvement before publication.

This workflow differs from `workflow_campaign_launch` in that it begins with existing content rather than a brief, and is oriented toward evaluation and improvement rather than creation.

---

## Supported Review Types

| Review Type | Trigger Phrase | Skills Invoked |
|---|---|---|
| Full Review | Review this content | All skills |
| Compliance Only | Check this for compliance | `skill_compliance_prescreening` |
| Brand Voice Only | Score this for brand voice | `skill_content_creation` (scoring module) |
| Audience Alignment | Is this right for [segment]? | `skill_audience_segmentation` |
| Copy Improvement | Improve this copy | `skill_content_creation` |
| Performance Analysis | Why isn't this performing? | `skill_performance_reporting` |

---

## Workflow Steps

### Step 1 - Content Intake
**Human Gate:** None  
**Output:** Classified content + review scope confirmation

1. Accept the content submission (pasted text, uploaded document, or structured input)
2. Identify content type, channel, audience segment, campaign goal, and review scope
3. Echo back the intake summary to confirm before proceeding

---

### Step 2 - Compliance Pre-Screen
**Skill Invoked:** `skill_compliance_prescreening`  
**Human Gate:** Required if ESCALATE items found  
**Output:** Compliance Pre-Screen Report

Run the submitted content through the full compliance pre-screen checklist. Produce the Compliance Pre-Screen Report.

If the overall status is ESCALATE, halt the review and deliver the escalation memo to the operator before proceeding to other review dimensions.

---

### Step 3 - Brand Voice Scoring
**Skill Invoked:** `skill_content_creation` (scoring module)  
**Human Gate:** None  
**Output:** Brand voice score + dimension breakdown

Score the submitted content on the four brand voice dimensions:
- Tone match (0-25)
- Vocabulary match (0-25)
- Message clarity (0-25)
- CTA effectiveness (0-25)

Provide a 2-3 sentence narrative rationale for the overall score, and identify the single highest-impact improvement.

---

### Step 4 - Audience Alignment Assessment
**Skill Invoked:** `skill_audience_segmentation`  
**Human Gate:** None  
**Output:** Alignment rating + misalignment flags

Evaluate whether the content is appropriately calibrated for the stated audience segment across register, empathy posture, channel fit, and message relevance.

Produce an alignment rating: STRONG | MODERATE | WEAK | MISALIGNED

For WEAK or MISALIGNED ratings, identify specific lines or sections causing misalignment and suggest targeted revisions.

---

### Step 5 - Revised Draft Production
**Skill Invoked:** `skill_content_creation`  
**Human Gate:** Optional  
**Output:** Revised draft with tracked changes noted

Produce a revised version of the submitted content that:
1. Resolves all FLAGGED compliance findings (excluding ESCALATE items)
2. Improves brand voice score by addressing the highest-impact gap identified in Step 3
3. Corrects any audience misalignment identified in Step 4
4. Preserves the operator's original intent, key message, and CTA

---

### Step 6 - Review Report Assembly
**Human Gate:** None  
**Output:** Complete content review report

Assemble the full review report including compliance pre-screen status, brand voice score breakdown, audience alignment rating, revised draft, revision summary table, and recommended next steps.

---

## Error and Exception Handling

| Exception | Agent Response |
|---|---|
| Content too long to review in one session | Split into sections; review in parts; note section boundaries |
| Audience segment not supplied | Ask; if operator declines, review against closest general FinServ professional audience |
| Content in language other than English | Flag; note that compliance rules applied are US-English based; recommend local review |
| Content is already published | Note that compliance findings apply retroactively; flag urgency if issues found |
