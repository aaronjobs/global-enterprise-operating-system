# Skill: Content Creation

**Agent:** FinServ Marketing Agent  
**Skill ID:** `skill_content_creation`  
**Version:** 1.0.0

---

## Purpose

Enables the agent to produce compliant, on-brand financial services marketing content across all standard digital and print channels. This skill governs format selection, length norms, channel-specific copywriting rules, and output structure for all content creation tasks.

---

## Supported Content Types

| Content Type | Channel | Max Length | Tone Default |
|---|---|---|---|
| Email — Nurture | Email | 300–500 words body | Warm, advisory |
| Email — Product Launch | Email | 200–350 words body | Confident, benefit-led |
| Email — Transactional | Email | 100–200 words body | Clear, direct |
| Social Post — LinkedIn | LinkedIn | 1,200 characters | Thought leadership |
| Social Post — X (Twitter) | X | 280 characters | Sharp, punchy |
| Social Post — Instagram | Instagram | 150–300 characters + hashtags | Visual-first, aspirational |
| Display Ad — Banner | Paid Media | Headline 30 chars; Body 90 chars | Benefit-led |
| Display Ad — Native | Paid Media | Headline 60 chars; Body 150 chars | Informational |
| Landing Page | Web | 400–800 words | Persuasive, conversion-focused |
| Blog / Article | Web | 800–1,500 words | Educational, authoritative |
| Whitepaper Section | PDF / Web | 500–1,000 words per section | Research-grade, formal |
| Direct Mail | Print | 250–400 words | Personal, trustworthy |
| Script — Video / Webinar | Video | 150 words per minute | Conversational, engaging |

---

## Execution Protocol

### Step 1 — Brief Parsing
Parse the incoming brief for:
- `audience_segment` (required)
- `product_or_service` (required)
- `channel` (required)
- `campaign_goal` (required)
- `key_message` (required)
- `cta` (required)
- `compliance_notes` (optional)
- `brand_voice_profile` (optional)
- `word_count_target` (optional)
- `regulatory_jurisdiction` (optional — default: US/SEC/FINRA)

If any required fields are missing, output a `[DATA REQUIRED]` block listing missing fields before proceeding.

### Step 2 — Audience Calibration
Select the appropriate register, vocabulary level, and empathy posture based on the `audience_segment`:

| Segment | Register | Vocabulary | Empathy Posture |
|---|---|---|---|
| Retail Investor — Mass Market | Accessible | Plain English | High — address anxiety and confusion |
| Retail Investor — Affluent | Sophisticated accessible | Some jargon with explanation | Moderate — address aspiration and trust |
| High Net Worth (HNW) | Peer-level | Jargon permitted | Low — address complexity and exclusivity |
| Financial Advisor / RIA | Professional | Full jargon | Minimal — address efficiency and insight |
| Institutional | Formal / technical | Full technical | None — address data and structure |
| Small Business Owner | Practical | Mixed | Moderate — address risk and growth |

### Step 3 — Compliance Pre-Screen
Before drafting, review the brief for the following triggers:

| Trigger Detected | Required Action |
|---|---|
| Performance figures | Add past-performance disclaimer prompt; flag output `[COMPLIANCE FLAG]` |
| Guarantee / risk-free language | Refuse; suggest compliant alternative |
| Forward-looking projection | Add hedge language; flag output |
| Competitor name | Flag for legal review; offer compliant competitive framing |
| Specific rate or yield | Confirm time period and basis are supplied; flag if missing |
| Testimonial or endorsement | Flag; confirm FTC/FINRA testimonial rule compliance |

### Step 4 — Draft Production
Produce the content output in the format specified for the channel:

```
## [Content Type] — [Campaign Name or Brief ID]

**Audience:** [Segment]
**Channel:** [Channel]
**Goal:** [Campaign Goal]
**CTA:** [Call to Action]

---

[CONTENT BODY]

---

**Suggested Disclaimer Block:**
[Auto-generated disclaimer text based on detected triggers]

---
[METADATA BLOCK — see behaviors.md Output Defaults]
```

### Step 5 — Brand Voice Scoring
After drafting, self-assess brand voice alignment on a 0–100 scale across:
- Tone match (0–25)
- Vocabulary match (0–25)
- Message clarity (0–25)
- CTA effectiveness (0–25)

Append score and brief rationale to the metadata block.

---

## Channel-Specific Rules

### Email
- Subject line must be 50 characters for optimal deliverability
- Preview text must be 90 characters and must not repeat the subject line verbatim
- Body must lead with the key benefit or problem statement within the first two sentences
- Single, clear CTA — do not include more than two CTA links per email
- Never include specific investment returns in subject lines

### LinkedIn
- Open with a hook line that does not lead with the brand name
- Use line breaks after every 1–3 sentences for mobile readability
- Include 3–5 relevant hashtags at the end
- Thought leadership framing preferred over promotional framing
- Engagement question at end is optional but recommended

### Paid Display Ads
- Headline must convey the primary benefit without the body copy
- Body must reinforce and extend — not repeat — the headline
- CTA must be a verb phrase (e.g., "Learn More," "Get Started," "Explore Options")
- Never use superlatives ("best," "#1," "only") without substantiation

### Landing Pages
- Above-the-fold section must contain: headline, sub-headline, hero image guidance, and primary CTA
- Include a social proof or trust signal section (awards, AUM, client count — must be verified)
- FAQ section recommended for product pages targeting retail investors
- Footer must include the full compliance disclosure block

---

## Error Handling

| Condition | Agent Response |
|---|---|
| Brief too vague to produce specific content | Ask for clarification on the top 2–3 missing specifics |
| Product details not provided | Flag `[DATA REQUIRED: product details]`; produce a placeholder-templated draft |
| Compliance conflict unresolvable | Refuse draft; escalate to human with written explanation |
| Word count target conflicts with channel norm | Produce at channel norm; note the discrepancy |
