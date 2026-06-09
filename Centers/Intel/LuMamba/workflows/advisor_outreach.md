# Workflow: Advisor Outreach

**Agent:** FinServ Marketing Agent  
**Workflow ID:** `workflow_advisor_outreach`  
**Version:** 1.0.0  
**Trigger:** Operator submits an advisor outreach brief or requests advisor-facing content  
**Estimated Runtime:** Single-session; human gates as noted

---

## Overview

This workflow governs the production of marketing content and outreach materials targeted at financial advisors, RIAs, broker-dealer representatives, and other intermediaries who recommend or distribute financial products to end clients. Advisor-facing content operates under distinct compliance, tone, and content rules compared to direct retail investor content.

---

## Advisor Outreach Content Types

| Content Type | Description | Primary Use Case |
|---|---|---|
| Product Fact Sheet | 1-2 page overview of a product for advisor use | New product introduction |
| Practice Management Guide | Educational content on growing advisor practices | Relationship deepening |
| Market Commentary | Timely market or economic perspective from the firm | Thought leadership / CRM |
| Talking Points Sheet | Bullet-point scripts for advisor-client conversations | Product launch support |
| Wholesaler Email | Outreach email from wholesaler to advisor | Prospecting / relationship |
| Advisor Newsletter | Regular digest of product, market, and practice updates | Ongoing engagement |
| Co-Branded Material | Firm + advisor co-branded client-facing piece | Advisor-as-distributor |
| Training Deck | Educational slide content for advisor onboarding | New product or policy training |
| RFP Response Support | Talking points and content for RFP responses | Institutional / platform selling |

---

## Compliance Considerations - Advisor vs. Retail

Advisor-facing content operates under different standards than retail-investor-facing content. The agent applies the following rule adjustments:

| Rule Area | Retail Investor Content | Advisor / Professional Content |
|---|---|---|
| Jargon | Restricted - must be plain language | Permitted - advisors are licensed professionals |
| Risk disclosures | Mandatory in-content | Required but can be in footnote/disclosure section |
| Suitability language | This may not be suitable for all investors | For advisor use only - not for distribution to retail investors |
| Performance data | Strict hedge language required | Standard performance disclosure block required |
| Forward-looking statements | Maximum hedge language | Hedge language required |
| Testimonials | Full FTC/FINRA disclosure | Standard disclosure |

All advisor-facing content must carry the footer: FOR ADVISOR AND INSTITUTIONAL USE ONLY - NOT FOR DISTRIBUTION TO RETAIL INVESTORS OR THE GENERAL PUBLIC - unless the content is explicitly co-branded for advisor-to-client distribution (in which case, full retail rules apply).

---

## Workflow Steps

### Step 1 - Brief Intake
**Human Gate:** None  
**Output:** Validated advisor outreach brief

Parse the incoming brief for:
- `content_type` - from the supported content types above (required)
- `product_or_service` - the product or service being communicated (required)
- `advisor_segment` - from the B2B segments in `skill_audience_segmentation` (required)
- `outreach_goal` - e.g., awareness, trial/recommendation, retention, education (required)
- `key_message` - the primary message for this outreach (required)
- `cta` - the desired advisor action (required)
- `market_context` - relevant market conditions or events to reference (optional)
- `product_data_inputs` - performance data, features, fees to be included (optional but recommended)
- `wholesaler_name` - for personalized wholesaler emails (optional)
- `compliance_notes` - operator-supplied guidance (optional)

---

### Step 2 - Advisor Segment Calibration
**Skill Invoked:** `skill_audience_segmentation`  
**Human Gate:** None  
**Output:** Segment profile + message calibration guidance

Load the specified advisor segment profile. Calibrate technical depth, practice pain points, decision drivers, and channel preference for this advisor segment.

---

### Step 3 - Content Drafting
**Skill Invoked:** `skill_content_creation`  
**Human Gate:** Optional creative review  
**Output:** Advisor outreach content draft(s)

Produce the content asset(s) specified in the brief. Apply advisor-specific content rules:

**For Product Fact Sheets:**
- Structure: Product overview / Investment objective / Key features / Performance (with disclosures) / Fees / Who it's for / How to recommend / Contact / Disclosures
- Length: 1-2 pages (400-700 words of narrative; remainder in tables and bullet points)
- Data: All performance figures must include time period, benchmark, and net/gross basis

**For Talking Points Sheets:**
- Structure: Opening / Value proposition / 3 key talking points / Common objections + responses / CTA / Disclosure
- Format: Scannable bullets - advisors use these in live client conversations
- Tone: Confident and direct

**For Market Commentary:**
- Structure: Executive summary (2-3 sentences) / Market context / Firm perspective / Implications for clients / Action points for advisors
- Length: 500-800 words
- Tone: Thoughtful, informed, balanced - do not be alarmist or promotional

**For Wholesaler Emails:**
- Subject line: Specific, benefit-led, not generic
- Body: Brief context + specific product or idea + clear ask + easy next step
- Length: 150-250 words - must be scannable in under 30 seconds
- Personalization: Include {{ADVISOR_NAME}}, {{FIRM_NAME}}, {{WHOLESALER_NAME}} merge tags

---

### Step 4 - Compliance Pre-Screen
**Skill Invoked:** `skill_compliance_prescreening`  
**Human Gate:** Required if FLAGGED or ESCALATE  
**Output:** Compliance Pre-Screen Report

Run the drafted content through the compliance pre-screen with advisor-audience rule adjustments applied. Confirm the For Advisor Use Only footer is present on all applicable assets.

---

### Step 5 - Handoff Package
**Human Gate:** None  
**Output:** Advisor outreach package

Deliver:
- Finalized content asset(s) in Markdown format
- Compliance Pre-Screen Report
- Usage guidance note (which advisor segment, which channel, when to deploy)
- Suggested follow-up cadence (if applicable)

---

## Error and Exception Handling

| Exception | Agent Response |
|---|---|
| Product data not supplied | Produce template with [PRODUCT DATA REQUIRED] placeholders |
| Co-branded content requested | Flag: apply full retail compliance rules to co-branded assets; confirm with operator |
| Content intended for retail distribution mislabeled as advisor | Refuse; flag; ask operator to confirm intended audience |
| Market data or commentary requires real-time data | Flag [DATA REQUIRED: current market data]; produce framework with placeholder figures |
