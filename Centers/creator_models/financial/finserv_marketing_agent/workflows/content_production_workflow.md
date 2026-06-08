# Workflow: Content Production

## Workflow ID
`finserv.workflows.content_production`

## Description
Defines the end-to-end process for producing a single piece of marketing content — from intake through compliance pre-screening to delivery. This workflow applies to all content types defined in `skills/content_creation.md`.

---

## Workflow Diagram

```
[REQUEST RECEIVED]
       |
       v
[STEP 1: INTAKE & SCOPE CHECK]
  - Identify content type, channel, audience, objective
  - Check for missing critical inputs
  - If inputs insufficient: surface intake prompt
       |
       v
[STEP 2: MESSAGING ARCHITECTURE]
  - Define primary message
  - Map supporting messages and proof points
  - Confirm CTA
       |
       v
[STEP 3: DRAFT PRODUCTION]
  - Write content per format template
  - Apply tone register for audience
  - Insert [DATA REQUIRED] placeholders where needed
       |
       v
[STEP 4: COMPLIANCE PRE-SCREEN]
  - Run checklist from skills/compliance_screening.md
  - Assign risk level (Green / Yellow / Orange / Red)
  - Insert required disclosures
  - Log any flags
       |
       |-- Green/Yellow: Proceed to delivery
       |
       |-- Orange/Red: Escalation note added; deliver with flags visible
       |
       v
[STEP 5: DELIVERY]
  - Attach version header
  - Attach compliance metadata block
  - Offer A/B variant (for emails and ads)
  - Suggest next step
```

---

## Step-by-Step Instructions

### Step 1 - Intake and Scope Check

**Trigger:** Any request to create, draft, edit, or rewrite a piece of content.

**Actions:**
1. Identify the 9 brief inputs (from `skills/content_creation.md - Step 1`)
2. Determine which are provided, implied, or missing
3. If 4 or more are missing: surface the intake prompt form before proceeding
4. If fewer than 4 are missing: state assumptions and proceed

**Intake Prompt (when needed):**
```
Before I draft this, I need a few quick inputs:
1. What product or service is this marketing?
2. Who is the primary audience? (e.g., retail consumers, HNW individuals, SMB owners)
3. Where will this content appear? (e.g., email, LinkedIn, landing page)
4. What is the primary CTA -- what should the reader do?
[Optional: Any specific messages or proof points to include?]
```

**Output:** Confirmed brief (stated or inferred)

---

### Step 2 - Messaging Architecture

**Trigger:** Intake confirmed.

**Actions:**
1. State the Primary Message (1 sentence)
2. List 2-4 Supporting Messages (proof points, benefits, differentiators)
3. Identify the Proof Elements available (data, awards, testimonials with disclosure, etc.)
4. Confirm the CTA

**Output:** Internal messaging hierarchy (used to guide drafting)

---

### Step 3 - Draft Production

**Trigger:** Messaging architecture confirmed.

**Actions:**
1. Select the appropriate format template from `skills/content_creation.md`
2. Write the full draft following tone register rules (`behaviors.md - 2.1`)
3. Apply prohibited language check (`behaviors.md - 2.2`)
4. Insert softeners for all forward-looking statements (`behaviors.md - 2.3`)
5. Insert `[DATA REQUIRED: source suggestion]` for any unsupported statistics

**Word Count Targets by Content Type:**

| Content Type | Target Length |
|---|---|
| Email (promotional) | 150-250 words (body) |
| Social post (LinkedIn) | 150-300 words |
| Paid search ad | 30 words (headlines) + 90 words (descriptions) |
| Landing page | 400-800 words |
| Blog post / article | 800-1,500 words |
| One-pager | 300-500 words |
| Press release | 400-600 words |

**Output:** Full draft

---

### Step 4 - Compliance Pre-Screen

**Trigger:** Draft complete.

**Actions:**
1. Run the full screening checklist from `skills/compliance_screening.md`
2. Assign a Risk Level (Green / Yellow / Orange / Red)
3. For Yellow: insert missing standard disclosures from the disclosure library
4. For Orange/Red: generate Flag Output blocks (one per flag)
5. Append the Compliance Metadata Block to the draft

**Output:** Screened draft with compliance metadata block and any flag outputs

---

### Step 5 - Delivery

**Trigger:** Compliance pre-screen complete.

**Actions:**
1. Prepend version header
2. Deliver the complete draft with metadata block
3. For emails and ads: deliver one A/B variant of the subject line / headline
4. Append the suggested next step

**Output:** Final deliverable package

---

## Revision Handling

When a revision is requested after delivery:
1. Apply the specific change requested
2. Do not alter sections not mentioned in the revision request
3. Append a Revision Notes block with version number, change description, and compliance re-check status
4. Re-run compliance pre-screen if the revision is substantive
5. Update version number to reflect revision

---

## Workflow Quality Gates

| Gate | Condition to Pass | Failure Action |
|---|---|---|
| Intake Gate | Minimum 5 of 9 brief inputs confirmed | Surface intake prompt |
| Draft Gate | All required sections present; word count in range | Revise before delivering |
| Compliance Gate | Risk level Green or Yellow with disclosures added | Flag before delivering; never suppress |
| Delivery Gate | Version header and metadata block present | Add before sending |
