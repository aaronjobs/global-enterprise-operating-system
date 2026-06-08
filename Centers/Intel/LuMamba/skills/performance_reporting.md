# Skill: Performance Reporting

**Agent:** FinServ Marketing Agent  
**Skill ID:** `skill_performance_reporting`  
**Version:** 1.0.0

---

## Purpose

Enables the agent to ingest campaign performance data and produce narrative analysis, insight summaries, and actionable recommendations for financial services marketing teams.

---

## Supported Report Types

| Report Type | Cadence | Audience | Primary Purpose |
|---|---|---|---|
| Campaign Flash Report | Weekly | Marketing team | Quick performance pulse |
| Campaign Performance Report | Monthly | Marketing + Leadership | Full channel breakdown + insights |
| Quarterly Marketing Review | Quarterly | CMO + C-suite | Strategic summary + attribution |
| Channel Effectiveness Analysis | Ad hoc | Marketing strategy | Channel ROI and optimization |
| A/B Test Results Report | Post-test | Marketing + Creative | Test outcomes + recommendations |
| Audience Engagement Report | Monthly | Marketing + CRM | Segment behavior analysis |
| Lead Quality Report | Monthly | Marketing + Sales | Lead volume, quality, and funnel conversion |

---

## Data Input Requirements

### Accepted Input Formats
- CSV export from analytics platform
- JSON data payload
- Pasted tabular data in plain text
- Verbal summary of key metrics (agent will note reduced analytical confidence)

### Required Fields - Campaign Performance Report

| Field | Description |
|---|---|
| campaign_name | Name of the campaign |
| campaign_period | Start and end dates |
| channel | Channel(s) included |
| impressions | Total impressions served |
| clicks | Total clicks |
| ctr | Click-through rate (%) |
| conversions | Total conversions |
| conversion_rate | Conversion rate (%) |
| cost | Total media cost |
| cpc | Cost per click |
| cpa | Cost per acquisition / conversion |
| revenue_influenced | Pipeline or revenue attributed (if available) |
| roas | Return on ad spend (if available) |

Optional: audience_segment, creative_variant, geo, device_split, engagement_rate, email_open_rate, email_ctr, unsubscribe_rate

---

## Execution Protocol

### Step 1 - Data Validation
- Confirm all required fields are present
- Flag missing fields as [DATA REQUIRED]
- Check for obvious anomalies (CTR > 100%, negative cost, zero impressions with non-zero clicks)
- Confirm data date range matches reporting period

### Step 2 - Benchmark Comparison

| Metric | Email | Display | Paid Search | LinkedIn |
|---|---|---|---|---|
| Open Rate | 20-28% | - | - | - |
| CTR | 2.5-4.5% | 0.05-0.1% | 3-6% | 0.4-0.9% |
| Conversion Rate | 1-3% | 0.1-0.5% | 2-5% | 0.5-1.5% |
| Unsubscribe Rate (Email) | < 0.5% | - | - | - |

Note: Benchmarks are guidance only. Operator should supply firm-specific benchmarks when available.

### Step 3 - Insight Generation
For each key metric, generate one of:
- **Outperformance Insight** - metric beats benchmark; identify likely driver
- **Underperformance Insight** - metric misses benchmark; identify likely cause and recommendation
- **Trend Insight** - metric is moving directionally over time; project trajectory
- **Anomaly Insight** - metric is statistically unusual; flag for investigation

Limit to top 5 most strategically significant insights per report.

### Step 4 - Recommendation Generation

```
## Recommendation [#]
**Metric Affected:** [Metric name]
**Current Performance:** [Value]
**Benchmark:** [Value]
**Gap:** [% or absolute]
**Recommended Action:** [Specific, actionable step]
**Expected Impact:** [Estimated improvement or outcome]
**Priority:** [High / Medium / Low]
**Owner:** [Marketing / Creative / Media / Analytics - or TBD]
```

### Step 5 - Report Assembly

```
# [Report Type] - [Campaign Name or Period]
**Prepared:** [ISO 8601 date]
**Reporting Period:** [Start] - [End]
**Channels Included:** [List]
**Data Source:** [Platform / Operator-supplied]

---

## Executive Summary
[3-5 sentence narrative: What happened, what worked, what did not, and the single most important action to take.]

## Key Metrics at a Glance
[Table: Metric | Actual | Benchmark | Variance | Status]

## Channel Performance Breakdown
[Per-channel section with metrics table + 2-3 sentence narrative]

## Audience Segment Performance (if data available)
[Per-segment breakdown]

## Creative Performance (if variant data available)
[Winning variant identification + rationale]

## Top Insights
[Numbered insight list - max 5]

## Recommendations
[Structured recommendations from Step 4]

## Appendix: Raw Metrics Table
[Full data table]

---
[METADATA BLOCK]
```

---

## Analytical Constraints

- **No fabrication** - if a metric is not supplied, list as [NOT PROVIDED]; never estimate or fabricate
- **Causation vs. correlation** - do not claim causation without explicit supporting evidence
- **Attribution limitations** - multi-touch attribution must be noted as modeled, not factual
- **Benchmark currency** - note that benchmarks are general industry references
- **Revenue attribution** - any revenue figures must come from operator-supplied data

---

## Compliance Note for Reporting

When performance reports are shared externally:
- Reports referencing investment performance outcomes must include standard performance disclaimers
- Reports shared with retail investors must meet plain-language standards
- Reports shared with regulatory bodies must be flagged for compliance review before distribution
