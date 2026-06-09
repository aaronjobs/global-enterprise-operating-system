# Workflow: Reporting Digest

**Agent:** FinServ Marketing Agent  
**Workflow ID:** `workflow_reporting_digest`  
**Version:** 1.0.0  
**Trigger:** Operator submits performance data for digest generation, or digest is triggered on a recurring schedule  
**Estimated Runtime:** Single-session

---

## Overview

This workflow governs the production of scheduled or on-demand marketing performance digests for financial services marketing teams and leadership stakeholders. It ingests campaign data, applies the Performance Reporting skill, and produces a formatted digest calibrated to the specified audience.

---

## Digest Types

| Digest Type | Cadence | Audience | Length | Format |
|---|---|---|---|---|
| Weekly Flash | Weekly | Marketing team | 1 page | Bullet summary + KPI table |
| Monthly Campaign Digest | Monthly | Marketing + Directors | 3-5 pages | Narrative + charts guidance + recommendations |
| Quarterly Marketing Review | Quarterly | CMO + C-suite | 5-8 pages | Executive narrative + strategic framing |
| Ad-Hoc Campaign Report | On demand | Varies | Calibrated to brief | Varies |

---

## Input Requirements

### Required per Digest Run
| Field | Description |
|---|---|
| `digest_type` | One of the digest types above |
| `reporting_period` | Start and end dates |
| `campaigns_included` | List of campaign names or IDs |
| `performance_data` | Raw data (CSV, JSON, or pasted table) |
| `stakeholder_audience` | Team / Director / C-suite |

### Optional Enrichment Inputs
| Field | Description |
|---|---|
| `prior_period_data` | For period-over-period comparison |
| `benchmark_data` | Operator-supplied firm or industry benchmarks |
| `narrative_focus` | Topic to emphasize |
| `strategic_context` | Business events that may explain performance |

---

## Workflow Steps

### Step 1 - Data Intake and Validation
**Human Gate:** None  
**Output:** Validated data summary

1. Ingest all performance data provided
2. Validate required fields per the Performance Reporting skill data requirements
3. Flag any missing fields as [DATA REQUIRED] and produce the digest with available data, noting gaps
4. Identify the reporting period, campaigns, and channels represented
5. If prior-period data is supplied, align the data schemas for comparison

---

### Step 2 - Metric Calculation and Benchmarking
**Skill Invoked:** `skill_performance_reporting`  
**Human Gate:** None  
**Output:** Calculated metrics table with benchmark comparisons

1. Calculate all derived metrics (CTR, conversion rate, CPA, ROAS, etc.) if not pre-calculated in input data
2. Compare all metrics against the benchmark reference table in the Performance Reporting skill
3. If operator-supplied benchmarks are provided, use those in addition to industry benchmarks
4. Flag any metrics that are statistically anomalous (more than 2 standard deviations from benchmark)
5. Produce the metrics table with status indicators: At or above benchmark / Within 20% below / More than 20% below

---

### Step 3 - Insight Generation
**Skill Invoked:** `skill_performance_reporting`  
**Human Gate:** None  
**Output:** Ranked insight list (max 5)

Generate the top 5 most strategically significant insights from the data, prioritized by business impact magnitude, actionability, and urgency.

For each insight, apply the insight type classification: Outperformance / Underperformance / Trend / Anomaly.

---

### Step 4 - Narrative Drafting
**Human Gate:** None  
**Output:** Calibrated narrative sections

Draft narrative sections calibrated to the `stakeholder_audience`:

**Team-Level (Weekly Flash):**
- Bulleted, tactical, channel-specific
- Focus: What happened and what do we do next week?
- Tone: Collegial, direct

**Director-Level (Monthly Digest):**
- Short narrative paragraphs + supporting tables
- Focus: Are we on track? What needs a decision?
- Tone: Professional, analytical

**C-Suite (Quarterly Review):**
- Executive summary paragraph
- Strategic framing: connect marketing performance to business outcomes
- Focus: What does this tell us about the business, and what is the recommendation?
- Tone: Confident, concise, strategic

---

### Step 5 - Recommendations
**Skill Invoked:** `skill_performance_reporting`  
**Human Gate:** None  
**Output:** Prioritized recommendation set

Produce the top 3-5 recommendations, each with metric or insight that drives it, specific action, expected impact, priority level, and suggested owner.

For C-suite digests, recommendations must be framed at the strategic level (budget reallocation, channel investment, product-market fit) rather than the tactical level.

---

### Step 6 - Digest Assembly and Formatting
**Human Gate:** None  
**Output:** Complete formatted digest

Assemble the digest in the following structure based on digest type:

**Weekly Flash Format:**
- Header: Weekly Marketing Flash with week date
- This Week at a Glance: 3-5 bullet points covering biggest wins, biggest misses, one action item
- KPI Snapshot: Metrics table with status indicators
- Top 3 Actions for Next Week

**Monthly Campaign Digest Format:**
- Executive Summary narrative
- Campaign Performance Overview KPI table across all campaigns
- Channel Breakdown per-channel section
- Audience Segment Performance (if data available)
- Top Insights numbered list
- Recommendations structured set
- Appendix with raw data table

**Quarterly Marketing Review Format:**
- Board-Level Summary: 1 paragraph covering results, interpretation, strategic recommendation
- Quarter in Review: performance narrative with business context and results
- Objective Achievement table: Objective, Target, Actual, Status
- Campaign Portfolio Review: summary of all campaigns
- Strategic Insights: top 3 insights with strategic framing
- Recommendations for next quarter
- Full Metrics Appendix

---

## Compliance Note for Digests

- Digests shared outside the marketing team must be reviewed for any claims that could be interpreted as investment performance advertising
- Digests referencing fund, portfolio, or product performance must include the full standard performance disclaimer block
- Digests shared with regulators or boards of directors must be routed through compliance review before distribution
