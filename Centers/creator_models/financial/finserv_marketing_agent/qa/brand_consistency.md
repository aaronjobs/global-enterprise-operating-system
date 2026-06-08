# QA Layer 3: Brand Consistency

## Layer ID
`finserv.qa.brand_consistency`

## Description
Defines the brand consistency evaluation criteria for all outputs produced by the GEOS FinServ Marketing Agent. This is Layer 3 of the three-layer QA framework and runs after Layers 1 and 2 pass. It ensures every output aligns with the firm's approved voice, terminology, positioning, and visual identity standards.

---

## Layer 3 Evaluation Structure

Layer 3 evaluates brand consistency across five dimensions. Configuration parameters (brand voice guide, approved terminology, positioning statements) are provided by the firm's Brand Agent or brand standards documentation. In the absence of firm-specific brand standards, the agent applies the default GEOS FinServ Marketing Agent voice and positioning standards defined in `behaviors.md`.

---

### Dimension 1: Voice and Tone

**Definition:** Does the output sound like the firm  not generic, not off-brand, not inconsistent with the established personality?

| Status | Condition |
|---|---|
| **PASS** | Tone matches the audience register and is consistent with the firm's stated voice |
| **NOTE** | Tone is acceptable but slightly flat or generic  could be elevated |
| **FAIL** | Tone is clearly inconsistent with brand (e.g., playful voice in a brand that requires gravitas; clinical voice in a brand built on warmth) |

**Default Voice Attributes (override with firm-specific guide if available):**

| Attribute | Default Value |
|---|---|
| Personality | Authoritative and trustworthy |
| Energy | Confident, not boastful |
| Warmth | Present but professional |
| Complexity | Matched to audience; never condescending |
| Urgency | Purposeful, not manipulative |

**Checklist:**
- [ ] Tone matches stated brand voice guide (or default above)
- [ ] - [ ] Consistent throughout  no jarring shifts in register mid-content
- [ ] - [ ] Personality is appropriate for the channel (LinkedIn vs. consumer email vs. institutional deck)
- [ ] - [ ] Not overly formal where warmth is needed; not casual where authority is required

- [ ] ---

- [ ] ### Dimension 2: Approved Terminology

- [ ] **Definition:** Does the output use the firm's approved product names, category names, and branded terms  and avoid prohibited or deprecated language?

- [ ] | Status | Condition |
- [ ] |---|---|
- [ ] | **PASS** | All product and category names match approved terminology |
- [ ] | **NOTE** | Generic term used where brand term exists  not blocking but should be updated |
- [ ] | **FAIL** | Deprecated product name used; competitor's brand name used; prohibited term present |

- [ ] **Term Categories to Check:**

- [ ] | Category | What to Verify |
- [ ] |---|---|
- [ ] | Product names | Match exact approved names (capitalization, spacing, trademark symbols) |
- [ ] | Service names | Use approved descriptors; avoid informal nicknames unless approved |
- [ ] | Category labels | Use firm's own language (e.g., "wealth management" vs. "asset management" if the firm has a preference) |
- [ ] | Competitor references | Never use competitor names in client-facing content without legal approval |
- [ ] | Jargon / internal terms | Internal language does not appear in external content |

- [ ] **Checklist:**
- [ ] - [ ] All product names match approved naming convention
- [ ] - [ ] Trademark symbols present where required
- [ ] - [ ] No competitor names in client-facing content (unless approved comparative advertising)
- [ ] - [ ] No internal jargon or code names in external content
- [ ] - [ ] Any abbreviations spelled out on first use

- [ ] ---

- [ ] ### Dimension 3: Messaging and Positioning Alignment

- [ ] **Definition:** Does the output reflect the firm's approved positioning, value proposition, and key messages  not drift into off-strategy narratives?

- [ ] | Status | Condition |
- [ ] |---|---|
- [ ] | **PASS** | Primary message aligns with approved value proposition; differentiator is on-strategy |
- [ ] | **NOTE** | Positioning slightly generic  could be more specifically tied to the brand's differentiated story |
- [ ] | **FAIL** | Content positions the firm in a way that contradicts its strategy |

- [ ] **Positioning Alignment Checklist:**
- [ ] - [ ] Primary message reflects the firm's core value proposition
- [ ] - [ ] Differentiator is consistent with what the firm actually claims to do better
- [ ] - [ ] Content does not make claims that are inconsistent with the firm's market position
- [ ] - [ ] Audience addressed matches the firm's target customer profile
- [ ] - [ ] Content does not inadvertently position the firm in a category it does not want to own

- [ ] ---

- [ ] ### Dimension 4: Visual and Formatting Standards

- [ ] **Definition:** Does the output follow the firm's visual identity and formatting conventions?

- [ ] | Status | Condition |
- [ ] |---|---|
- [ ] | **PASS** | Copy length, structure, and format compatible with brand design system |
- [ ] | **NOTE** | Copy may need trimming or restructuring to fit standard templates |
- [ ] | **FAIL** | Copy structure is fundamentally incompatible with the channel's design format |

- [ ] **Formatting Checklist:**
- [ ] - [ ] Character/word counts compatible with visual templates
- [ ] - [ ] Headline length appropriate for channel (email subject >= 60 chars; hero headline >= 10 words)
- [ ] - [ ] CTA copy matches button copy conventions (length, verb style)
- [ ] - [ ] Paragraph length appropriate for channel (email: 3 sentences max per paragraph)
- [ ] - [ ] Subheadings present for long-form content

- [ ] ---

- [ ] ### Dimension 5: Legal Entity and Attribution

- [ ] **Definition:** Is the correct legal entity name, registration information, and content attribution present?

- [ ] | Status | Condition |
- [ ] |---|---|
- [ ] | **PASS** | Correct legal entity name present; required registration info present for channel |
- [ ] | **NOTE** | Legal entity name uses informal version  flag to use full legal name |
- [ ] | **FAIL** | Wrong legal entity named; registration information missing where required by regulation |

- [ ] **Checklist:**
- [ ] - [ ] Full legal entity name used in disclosures and footers
- [ ] - [ ] FINRA/SEC registration information present where required
- [ ] - [ ] State registration information present where applicable
- [ ] - [ ] Content attribution consistent with firm's policy

- [ ] ---

- [ ] ## Layer 3 Scoring Summary

- [ ] | Dimension | Status | Notes |
- [ ] |---|---|---|
- [ ] | Voice and Tone | [PASS / NOTE / FAIL] | |
- [ ] | Approved Terminology | [PASS / NOTE / FAIL] | |
- [ ] | Messaging and Positioning | [PASS / NOTE / FAIL] | |
- [ ] | Visual and Formatting | [PASS / NOTE / FAIL] | |
- [ ] | Legal Entity and Attribution | [PASS / NOTE / FAIL] | |

- [ ] **Layer 3 Result:**
- [ ] - All dimensions PASS -> **PASS** -> Proceed to delivery
- [ ] - One or more NOTE, no FAIL -> **PASS WITH NOTES** -> Deliver with notes; incorporate before final use
- [ ] - Any FAIL -> **FAIL** -> Revise and re-run Layer 3

- [ ] ---

- [ ] ## Brand Standards Configuration

- [ ] When firm-specific brand standards are available, they override the defaults in this file. Accepted inputs:

- [ ] | Input Type | How to Provide |
- [ ] |---|---|
- [ ] | Voice and tone guide | Paste key attributes or upload the guide |
- [ ] | Approved product name list | Provide as a list in the session |
- [ ] | Positioning statement | State the firm's approved positioning in the session |
- [ ] | Prohibited terms list | Provide as a list in the session |
- [ ] | Legal entity name | State the full legal entity name in the session |

- [ ] Brand standards are retained within the session and applied to all outputs until the session ends or the user overrides them.

- [ ] ---

- [ ] ## Common Layer 3 Failure Patterns

- [ ] | Failure | Typical Cause | Fix |
- [ ] |---|---|---|
- [ ] | Generic tone | Drafting without brand voice guide | Load brand voice attributes before drafting |
- [ ] | Wrong product name | Using informal or deprecated name | Verify against approved naming list |
- [ ] | Off-strategy positioning | Over-focusing on features vs. brand story | Re-anchor to approved value proposition |
- [ ] | Copy too long for template | Written for narrative, not design context | Trim to fit channel design constraints |
- [ ] | Wrong legal entity | Using parent brand vs. regulated subsidiary | Confirm legal entity for the specific product |
