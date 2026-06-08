# Workflow: Performance Reporting

## Workflow ID
`finserv.workflows.performance_reporting`

## Description
Defines the process for ingesting marketing performance data, generating insights, and delivering actionable performance reports for financial services campaigns. This workflow applies to all campaign types and reporting cadences (weekly, monthly, end-of-campaign).

---

## Workflow Diagram

```
[REPORTING REQUEST RECEIVED]
       |
       v
[STEP 1: DATA INTAKE]
  - Identify report type and period
  - Receive or request performance data
  - Identify gaps or data quality issues
       |
       v
[STEP 2: DATA VALIDATION]
  - Check for completeness, consistency, and anomalies
  - Flag data quality issues
  - Apply attribution model context
       |
       v
[STEP 3: INSIGHT GENERATION]
  - Apply Insight Hierarchy (skills/performance_insights.md)
  - Compute vs. goal and vs. prior period
  - Surface top findings by priority
       |
       v
[STEP 4: REPORT ASSEMBLY]
  - Populate performance report template
  - Write executive summary
  - Build channel breakdown
  - Formulate optimization recommendations
       |
       v
[STEP 5: DELIVERY]
  - Deliver report with version header
  - Offer follow-up: deep-dive on specific channel or metric
  - Suggest next reporting milestone
```

---

## Step-by-Step Instructions

### Step 1 - Data Intake

**Trigger:** Any request to analyze campaign data, produce a report, or interpret metrics.

**Required Inputs:**

| Input | Source |
|---|---|
| Campaign name and period | User |
| Primary and secondary KPIs | Campaign brief or user |
| Channel-level data (spend, impressions, clicks, conversions) | User-provided or platform export |
| Prior period benchmarks | User or prior report |
| Campaign goals (targets) | Campaign brief |
| Attribution model in use | User or platform default |

**If data is not provided:**
```
To generate your performance report, please share:
1. The campaign name and reporting period (e.g., May 2026)
2. Your performance data -- ideally a CSV or summary by channel
3. Your campaign goals or KPI targets
4. Which attribution model is applied (last touch, multi-touch, etc.)
If you don't have all of these, share what you have and I'll note the gaps.
```

---

### Step 2 - Data Validation

**Trigger:** Data received.

**Actions:**
1. Check for completeness -- are all channels in the plan represented?
2. Check for consistency -- do totals add up? Do dates align?
3. Flag anomalies:
   - Spend without corresponding impressions or clicks
   - CTR outside of expected range (>20% or <0.01%)
   - Conversion rate spikes that may indicate tracking errors
   - Zero-value cells that may indicate missing data vs. true zero
4. Note which metrics are model-dependent (attribution, assisted conversions)

**Data Quality Flag Format:**
```
DATA QUALITY NOTE
Metric:     [Metric name]
Channel:    [Channel]
Issue:      [Description of anomaly or gap]
Impact:     [How this affects interpretation]
Action:     [Recommend re-pulling / flagging / noting in report]
```

---

### Step 3 - Insight Generation

**Trigger:** Data validated.

**Actions:**
1. Apply the Insight Hierarchy from `skills/performance_insights.md`:
   - Headline Finding
   - Supporting Evidence
   - Causal Hypothesis
   - Implication
   - Recommendation
2. For each channel: compute delta vs. goal and vs. prior period
3. Rank insights by business impact (not by size of data movement)
4. Identify the top 3 insights for the executive summary

**Insight Prioritization:**
- Revenue or acquisition impact > engagement metrics
- Declining metrics > below-goal metrics > on-target metrics
- Anomalies > trends
- Actionable insights > explanatory insights

---

### Step 4 - Report Assembly

**Trigger:** Insights generated.

**Actions:**
1. Populate the Performance Report Template from `skills/performance_insights.md`
2. Write the Executive Summary (2-3 sentences; lead with headline finding)
3. Complete the Performance Scorecard with goals, actuals, and deltas
4. Write the Channel Breakdown (one paragraph per channel)
5. List Key Insights (3-5; formatted as finding + evidence)
6. Write Optimization Recommendations (3 priorities; each with action, expected impact, owner, timeline)
7. List Risks and Watch Items
8. Confirm Next Steps with owners and dates

**Report Status Indicators:**
- Green: On Track -- metric within 10% of goal
- Yellow: At Risk -- metric 10-25% below goal or prior period
- Red: Below Goal -- metric more than 25% below goal

---

### Step 5 - Delivery

**Trigger:** Report assembled.

**Actions:**
1. Prepend version and date header
2. Deliver the full report
3. Offer one of the following follow-ups:
   - "Would you like a deeper dive on [underperforming channel]?"
   - "I can draft an optimization brief for [priority recommendation] if useful."
   - "Would you like a stakeholder summary version (executive one-pager)?"
4. Note next reporting milestone

---

## Report Type Variations

### Weekly Pulse Report
- Focus: Pacing vs. budget; early trend signals
- Format: Scorecard + 2-3 top insights + immediate action items
- Length: 1 page / short-form

### Monthly Campaign Report
- Focus: Full performance review; optimization decisions
- Format: Full template from `skills/performance_insights.md`
- Length: 2-3 pages

### End-of-Campaign Report
- Focus: Final results vs. goals; lessons learned; future recommendations
- Format: Full template + Lessons Learned section + Next Campaign Implications
- Length: 3-5 pages

### Executive Summary (Standalone)
- Focus: Headline findings only; strategic implications
- Format: 5 bullets max; traffic-light status; 1 recommendation
- Audience: C-suite, marketing leadership

---

## Lessons Learned Section Template (End-of-Campaign)

```
LESSONS LEARNED

What Worked:
1. [Finding -- what performed and why]
2. [Finding]
3. [Finding]

What Didn't Work:
1. [Finding -- what underperformed and likely cause]
2. [Finding]

Surprises:
1. [Unexpected outcome -- positive or negative]

Apply to Next Campaign:
1. [Specific recommendation derived from this campaign's data]
2. [Specific recommendation]
3. [Specific recommendation]
```
