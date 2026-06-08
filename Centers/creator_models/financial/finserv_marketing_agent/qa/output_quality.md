# QA Layer 1: Output Quality

## Layer ID
`finserv.qa.output_quality`

## Description
Defines the quality evaluation criteria and pass/fail thresholds for all outputs produced by the GEOS FinServ Marketing Agent. This is Layer 1 of the three-layer QA framework and must pass before Layers 2 and 3 are executed.

---

## Evaluation Dimensions

Layer 1 evaluates output across six dimensions. Each dimension has a Pass condition, a Note condition (non-blocking), and a Fail condition (blocking).

---

### Dimension 1: Completeness

**Definition:** All requested sections and components are present in the output.

| Status | Condition |
|---|---|
| PASS | All requested sections present; no required component missing |
| NOTE | Minor optional element absent (e.g., A/B variant not requested but could add value) |
| FAIL | One or more required sections missing; CTA absent; brief requirement not addressed |

**Checklist:**
- [ ] All sections from the applicable format template are present
- [ ] CTA is explicit and specific
- [ ] Version header is present
- [ ] Compliance metadata block is present (for client-facing content)
- [ ] All [DATA REQUIRED] placeholders are either filled or explicitly flagged

---

### Dimension 2: Accuracy

**Definition:** All factual claims are substantiated, attributed, or appropriately hedged.

| Status | Condition |
|---|---|
| PASS | All statistics cited with source and date; no unsupported factual claims |
| NOTE | One or more [DATA REQUIRED] placeholders present -- flagged but not blocking |
| FAIL | Specific figures cited without attribution; fabricated or unverifiable claims present |

**Checklist:**
- [ ] All statistics include source attribution
- [ ] All date-sensitive data (rates, rankings, market data) include "as of [date]"
- [ ] No performance figures cited without basis
- [ ] Product features described accurately (no overclaiming)
- [ ] No invented quotes, endorsements, or testimonials

---

### Dimension 3: Clarity

**Definition:** The content is understandable to its intended audience without unnecessary complexity.

| Status | Condition |
|---|---|
| PASS | Reading level appropriate for audience; key message clear within first 30 words (short-form) or first paragraph (long-form) |
| NOTE | Minor jargon present that may benefit from simplification for retail audiences |
| FAIL | Key message buried or absent; dense financial jargon without explanation in retail content |

**Reading Level Standards:**

| Audience | Target Grade Level |
|---|---|
| Retail / Consumer | Grade 8 or below |
| Mass Affluent | Grade 10 or below |
| HNW / Institutional | Grade 12 or below (complexity acceptable) |
| Internal / Sales | Unrestricted |

**Checklist:**
- [ ] Primary message is clear in the first 30 words (short-form) or opening paragraph (long-form)
- [ ] No unexplained acronyms in retail-facing content
- [ ] Sentences average 20 words or fewer in retail content
- [ ] Active voice used in CTAs and key messages
- [ ] Subheadings present in content over 300 words

---

### Dimension 4: Actionability

**Definition:** The output gives the recipient a clear understanding of what to do next.

| Status | Condition |
|---|---|
| PASS | CTA is specific, verb-led, and links to a concrete next step |
| NOTE | CTA present but could be stronger or more specific |
| FAIL | No CTA; CTA is vague (e.g., "Learn more" with no context); multiple conflicting CTAs |

**CTA Quality Standards:**
- Must begin with a verb (Get, Start, Open, Discover, Schedule, Download, Apply)
- Must specify what the reader will receive or experience
- Must match the funnel stage (awareness: informational CTA; conversion: transactional CTA)
- One primary CTA per content unit (secondary CTAs permitted but subordinate)

**Checklist:**
- [ ] CTA present and verb-led
- [ ] CTA matches stated campaign objective and funnel stage
- [ ] No more than one primary CTA
- [ ] CTA URL or destination placeholder included
- [ ] Urgency trigger present where applicable (limited time, enrollment deadline, etc.)

---

### Dimension 5: Structural Integrity

**Definition:** The output follows the correct format template and structural conventions for the content type.

| Status | Condition |
|---|---|
| PASS | Format template followed; section order correct; formatting consistent |
| NOTE | Minor deviation from template that does not affect usability |
| FAIL | Wrong template used; critical structural element missing; formatting inconsistent throughout |

**Checklist:**
- [ ] Correct format template applied (from skills/content_creation.md)
- [ ] Section headers consistent with template
- [ ] Word count within the target range for the content type
- [ ] For emails: subject line, preview text, body, CTA, and disclosures all present
- [ ] For landing pages: hero, benefits, proof, how it works, and CTA sections all present
- [ ] Version header present and correctly formatted

---

### Dimension 6: Tone and Voice Alignment

**Definition:** The output reflects the appropriate register for the audience and channel.

| Status | Condition |
|---|---|
| PASS | Tone matches audience register table; no prohibited language present |
| NOTE | Minor tone inconsistency; overly formal or informal for context |
| FAIL | Prohibited language present; tone inappropriate for audience |

**Checklist:**
- [ ] Tone matches the audience register from behaviors.md
- [ ] No prohibited language present
- [ ] Forward-looking statements include required softeners
- [ ] No superlatives without substantiation
- [ ] Consistent person and voice throughout

---

## Layer 1 Scoring Summary

| Dimension | Status | Notes |
|---|---|---|
| Completeness | [PASS / NOTE / FAIL] | |
| Accuracy | [PASS / NOTE / FAIL] | |
| Clarity | [PASS / NOTE / FAIL] | |
| Actionability | [PASS / NOTE / FAIL] | |
| Structural Integrity | [PASS / NOTE / FAIL] | |
| Tone and Voice | [PASS / NOTE / FAIL] | |

**Layer 1 Result:**
- All dimensions PASS: PASS -- Proceed to Layer 2
- One or more NOTE, no FAIL: PASS WITH NOTES -- Proceed to Layer 2; include notes in QA summary
- Any FAIL: FAIL -- Revise and re-run Layer 1 before proceeding

---

## Common Layer 1 Failure Patterns

| Failure | Typical Cause | Fix |
|---|---|---|
| CTA missing or weak | Draft focused on information, not conversion | Add or strengthen CTA; match to funnel stage |
| Key message buried | Over-written introduction | Move primary message to opening line |
| Unsupported statistics | Data not provided by user | Insert [DATA REQUIRED] placeholder; flag source |
| Wrong reading level | Technical author writing for retail | Simplify; replace jargon; shorten sentences |
| Incomplete template | Skipped sections to save length | Complete all required template sections |
| Inconsistent voice | Multiple sections drafted separately | Edit for unified voice throughout |
