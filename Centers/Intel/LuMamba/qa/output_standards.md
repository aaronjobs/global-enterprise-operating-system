# Output Standards: FinServ Marketing Agent

**Agent:** FinServ Marketing Agent
**QA Layer ID:** `qa_output_standards`
**Version:** 1.0.0
**Purpose:** Defines the structural, formatting, and delivery standards for all agent outputs

---

## Overview

This file defines the mandatory and recommended standards for how the FinServ Marketing Agent structures, formats, and delivers its outputs. All outputs must conform to these standards before passing the QA checklist.

---

## 1. Universal Output Requirements

Every output produced by the agent must include:

### 1.1 Metadata Block

```yaml
---
agent: finserv_marketing_agent
version: 1.0.0
generated: [ISO 8601 timestamp]
workflow: [workflow_id or ad_hoc]
skill: [skill_id or multiple]
audience_segment: [segment_id or name]
channel: [channel name or n/a]
campaign_name: [name or n/a]
compliance_status: PENDING REVIEW | FLAGGED | CLEAN | ESCALATED
brand_voice_score: [0-100 or n/a]
jurisdiction: [US | UK | EU | CA | Other]
qa_status: PASS | PASS WITH FLAGS | FAIL REVISED | ESCALATED
---
```

### 1.2 QA Summary Block

```
---
## QA Summary
**Critical Checks:** [X passed / Y total]
**Standard Checks:** [X passed / Y total]
**Advisory Notes:** [Count or None]
**QA Status:** [PASS | PASS WITH FLAGS | FAIL REVISED | ESCALATED]
**QA Timestamp:** [ISO 8601]
```

### 1.3 Compliance Watermark
Required on any output that references investment performance, forward-looking statements, or implies product suitability:

```
[COMPLIANCE REVIEW REQUIRED - This content has not been reviewed or approved by a licensed
compliance officer. Do not publish or distribute without obtaining required compliance sign-off.]
```

---

## 2. Formatting Standards by Output Type

### 2.1 Marketing Copy (Emails, Ads, Social Posts, Landing Pages)

| Element | Standard |
|---|---|
| Format | Markdown |
| Headings | H2 for major sections |
| Subject lines | Presented on a labeled line before the body |
| CTAs | Bold and clearly labeled: **CTA:** [text] |
| Disclaimer blocks | Set off in a blockquote below the body copy |
| Merge tags | Double curly braces: {{FIRST_NAME}}, {{FIRM_NAME}} |
| Character counts | Appended in brackets for subject lines, social posts, and ad copy |

### 2.2 Strategy and Planning Documents

| Element | Standard |
|---|---|
| Format | Markdown with H1 title, H2 major sections, H3 subsections |
| Tables | Used for structured data (segment profiles, channel matrices, budget splits) |
| Numbered lists | Used for sequential steps, ranked priorities |
| Bullet lists | Used for non-sequential items, feature lists |
| Human gate markers | Labeled: **HUMAN GATE REQUIRED:** [description] |
| Assumptions | Marked with [ASSUMPTION MADE] inline |

### 2.3 Analysis and Reporting Outputs

| Element | Standard |
|---|---|
| Format | Markdown with narrative sections and data tables |
| Executive summary | Always first section; max 5 sentences |
| Metrics tables | Include: Metric / Actual / Benchmark / Variance / Status columns |
| Status indicators | At or above benchmark / Within 20% below / More than 20% below |
| Recommendations | Structured: metric, action, expected impact, priority, owner |
| Fabrication prohibition | Missing data labeled [NOT PROVIDED] - never estimated |

### 2.4 Compliance Reports

| Element | Standard |
|---|---|
| Format | Markdown |
| Finding severity | Labeled: PASS / FLAG / ESCALATE |
| Finding table | Check ID / Status / Finding / Recommended Action |
| Required actions | Numbered list after findings table |
| Escalation block | Set off with [ESCALATION REQUIRED] header |
| Limitation statement | Mandatory verbatim text from skill_compliance_prescreening |

---

## 3. Length Standards

| Output Type | Target Length | Hard Ceiling |
|---|---|---|
| Email body copy | 200-500 words | 600 words |
| LinkedIn post | 150-800 characters | 1,200 characters |
| X post | 200-280 characters | 280 characters |
| Display ad headline | 20-30 characters | 40 characters |
| Display ad body | 60-90 characters | 120 characters |
| Landing page | 400-800 words | 1,200 words |
| Blog / article | 800-1,500 words | 2,000 words |
| Campaign brief | 600-1,200 words | 2,000 words |
| Compliance pre-screen report | 300-600 words | 1,000 words |
| Weekly flash digest | 200-350 words | 500 words |
| Monthly campaign digest | 800-1,500 words | 2,500 words |
| Quarterly review | 1,200-2,000 words | 3,500 words |
| Fact sheet | 400-700 words | 1,000 words |
| Talking points sheet | 300-500 words | 700 words |

Outputs that exceed the hard ceiling must be split into sections and labeled accordingly.

---

## 4. Tone and Language Standards

### 4.1 Prohibited Language

- Guaranteed / guarantee (in investment context)
- Risk-free
- Can't lose / you won't lose
- #1 / best / top / leading / only (without substantiation)
- Will return / will grow / will outperform (forward-looking absolute)

### 4.2 Required Hedge Language for Forward-Looking Statements

All forward-looking statements must include one of: may, could, subject to market conditions, there is no guarantee that, past performance is not indicative of future results, potential (as a modifier).

### 4.3 Inclusive Language

- Use gender-neutral language for all personas and examples
- Do not use age-based stereotypes in audience descriptions
- Use client rather than customer for investment management contexts
- Use investor rather than consumer for investment product contexts

---

## 5. Deliverable Packaging Standards

When delivering multiple outputs in a single session, package them as:

```
# Campaign Asset Package - [Campaign Name]
**Delivered:** [ISO 8601 timestamp]
**Total Assets:** [Count]
**Compliance Status:** [Overall status]

---

## Asset Index
| Asset # | Content Type | Channel | Audience | Compliance Status | Word Count |
|---|---|---|---|---|---|
| 1 | Email Launch | Email | [Segment] | CLEAN | 312 |

---

## Asset 1: [Content Type] - [Channel]
[Full asset content]

---
[PACKAGE-LEVEL QA SUMMARY]
```

---

## 6. Version Control Standards

All outputs are versioned at the session level. If an operator requests a revision, label the revised output v2, v3, etc. in the metadata block. Preserve the original version in the session for reference if requested. Include a brief change log in the revised metadata:

```yaml
revision_history:
  v1: Initial draft
  v2: Compliance flags resolved; CTA strengthened
```
