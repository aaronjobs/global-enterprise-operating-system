# Workflow: Campaign Launch

## Workflow ID
`finserv.workflows.campaign_launch`

## Description
Defines the end-to-end process for planning, building, and launching a complete integrated marketing campaign for a financial services brand. This workflow coordinates across brief development, asset production, compliance review, channel activation, and go-live readiness.

---

## Workflow Diagram

```
[CAMPAIGN REQUEST RECEIVED]
       |
       v
[STEP 1: CAMPAIGN BRIEF DEVELOPMENT]
  - Intake objective, audience, budget, dates, channels
  - Build full campaign brief (template from skills/campaign_planning.md)
  - Confirm with stakeholder before proceeding
       |
       v
[STEP 2: AUDIENCE AND SEGMENT DEFINITION]
  - Apply skills/audience_segmentation.md
  - Deliver segment profiles and activation plan
       |
       v
[STEP 3: MESSAGING HIERARCHY AND CREATIVE STRATEGY]
  - Define primary message, supporting messages, differentiator, CTA
  - Map message variants by channel and audience
       |
       v
[STEP 4: ASSET PRODUCTION]
  - Produce all content assets per skills/content_creation.md
  - Apply compliance pre-screen per skills/compliance_screening.md
  - Deliver asset library with compliance metadata
       |
       v
[STEP 5: COMPLIANCE AND LEGAL REVIEW ROUTING]
  - Generate compliance routing memo
  - Identify assets requiring pre-clearance
  - Provide review deadline and escalation contacts
       |
       v
[STEP 6: CHANNEL ACTIVATION PLAN]
  - Define setup requirements per channel
  - Audience targeting specs (paid media)
  - Technical specs (email deployment, landing page)
  - Trafficking instructions
       |
       v
[STEP 7: MEASUREMENT SETUP]
  - Confirm KPIs and tracking requirements
  - Define reporting cadence and owner
  - Provide UTM parameter naming convention
       |
       v
[STEP 8: LAUNCH READINESS CHECKLIST]
  - Run pre-launch gate check
  - Confirm all approvals received
  - Confirm all assets trafficked
  - GO / NO-GO decision
```

---

## Step-by-Step Instructions

### Step 1 - Campaign Brief Development

**Trigger:** Any request to plan or launch a campaign.

**Actions:**
1. Gather inputs for the Campaign Brief Template (`skills/campaign_planning.md`)
2. If fewer than 6 of the 13 brief sections are populated, surface an intake prompt
3. Draft the complete Campaign Brief
4. Deliver and request stakeholder confirmation before proceeding to asset production

**Minimum Viable Inputs to Proceed:**
- Business objective and target metric
- Primary audience segment
- Campaign dates (start and end)
- Budget (even a rough range)
- At least 2 channels
- Primary CTA

---

### Step 2 - Audience and Segment Definition

**Trigger:** Campaign brief confirmed.

**Actions:**
1. Apply the Segmentation Framework from `skills/audience_segmentation.md`
2. Build persona cards for each target segment
3. Map each segment to activation channels
4. Flag any segments with compliance implications (seniors, accredited investor requirements, etc.)

**Output:** Segment profiles + channel activation map

---

### Step 3 - Messaging Hierarchy and Creative Strategy

**Trigger:** Audience definition complete.

**Actions:**
1. Define primary message (1 sentence; the single idea the campaign must land)
2. Map message variants by audience segment, channel, and funnel stage
3. Define differentiator (what makes this campaign's offer distinct)
4. Confirm CTA for each channel

**Output:** Messaging matrix

```
MESSAGING MATRIX
Channel       | Audience      | Primary Message          | CTA
--------------------------------------------------------------
[Email]       | [Segment A]   | [Message variant]        | [CTA]
[Paid Social] | [Segment B]   | [Message variant]        | [CTA]
[Search]      | [Intent]      | [Message variant]        | [CTA]
[Landing Pg]  | [All]         | [Unified message]        | [CTA]
```

---

### Step 4 - Asset Production

**Trigger:** Messaging hierarchy confirmed.

**Actions:**
1. Generate the complete asset list based on channel plan
2. Produce each asset using `workflows/content_production_workflow.md`
3. Track asset status in an Asset Tracker

**Output:** Asset library with compliance metadata for each piece

---

### Step 5 - Compliance and Legal Review Routing

**Trigger:** All assets drafted and pre-screened.

**Actions:**
1. Generate the Compliance Routing Memo listing assets by review type
2. Identify any assets with Red flags -- do not include in trafficking until cleared
3. Set review deadlines and escalation contacts

**Output:** Compliance routing memo

---

### Step 6 - Channel Activation Plan

**Trigger:** Compliance routing underway; assets with Green/Yellow status ready.

**For each channel, provide:**

**Email:**
- Deployment platform requirements
- Audience list specification (include / exclude / suppression)
- Send timing recommendation
- Subject line and preview text for A/B test
- Tracking parameters

**Paid Search:**
- Campaign structure (campaign > ad group > ad)
- Keyword targeting list with match types
- Negative keyword list
- Bidding strategy recommendation
- Landing page URL with UTM parameters

**Paid Social:**
- Audience targeting spec
- Ad format spec
- Budget pacing and frequency cap
- UTM parameters

**Landing Page:**
- URL and slug recommendation
- Form fields
- Tracking pixel requirements
- CRM integration requirements

---

### Step 7 - Measurement Setup

**Trigger:** Channel activation plan complete.

**Actions:**
1. Confirm primary and secondary KPIs from campaign brief
2. Define UTM parameter naming convention
3. Identify required tracking implementations
4. Define reporting cadence and template (use `skills/performance_insights.md`)
5. Set baseline measurements before launch

---

### Step 8 - Launch Readiness Checklist

**Trigger:** All steps complete; go-live date approaching.

**Pre-Launch Gate:**

```
PRE-LAUNCH CHECKLIST
Campaign: [Name] | Go-Live: [Date]
-----------------------------------------
APPROVALS
[ ] Campaign brief approved
[ ] Compliance review complete
[ ] Legal review complete
[ ] Executive sponsor signed off

ASSETS
[ ] All creative assets final and version-locked
[ ] All disclosures reviewed and incorporated
[ ] All landing pages live and QA tested
[ ] All tracking implemented and tested

CHANNEL SETUP
[ ] Email list segmented and suppression applied
[ ] Paid campaigns set up in platforms
[ ] Audience targeting confirmed
[ ] Budget pacing configured
[ ] UTM parameters implemented

MEASUREMENT
[ ] Tracking pixels firing correctly
[ ] CRM integration tested
[ ] Reporting dashboard configured
[ ] Baseline metrics captured

GO / NO-GO DECISION
[ ] All gates passed -> GO
[ ] Outstanding items: [List] -> NO-GO
-----------------------------------------
```

**Output:** Launch readiness status with GO / NO-GO recommendation

---

## Escalation Paths

| Situation | Action |
|---|---|
| Compliance review not complete by deadline | Escalate to marketing lead; delay go-live |
| Red-flagged asset not cleared | Remove from launch plan; launch remaining assets |
| Budget not confirmed | Pause paid channel setup; proceed with organic assets |
| Technical implementation delayed | Adjust launch date; notify stakeholders |
