# Skill: Compliance Screening

## Skill ID
`finserv.skills.compliance_screening`

## Description
Governs the agent's compliance pre-screening layer for all marketing content. Defines rules, triggers, classification logic, and output format for compliance risk assessment prior to human legal and compliance review.

> **Important:** This skill provides a first-pass risk assessment only. It does not constitute legal advice, a formal compliance review, or regulatory approval. All flagged and escalated content must be reviewed by qualified compliance and legal professionals before publication.
>
> ---
>
> ## Screening Philosophy
>
> - **Disclose**  Insert or flag all required standard disclosures
> - - **Escalate**  Route any content with elevated regulatory risk to human review
>   - - **Never suppress**  Never remove a compliance flag at a user's request; log the request and reinforce the flag
>    
>     - ---
>
> ## Screening Checklist
>
> ### Category 1: Performance and Return Claims
>
> | Check | Pass Condition | Flag Condition |
> |---|---|---|
> | Yield or APY references | Accurate rate cited with "as of [date]" | Rate cited without date; guaranteed language present |
> | Historical return references | Accompanied by past performance disclaimer | No disclaimer; annualized returns without explanation |
> | Forward-looking projections | Qualified with softener language | Stated as certainty; no qualification |
> | Benchmark comparisons | Apples-to-apples; benchmark identified | Mismatched timeframes; benchmark undefined |
>
> ### Category 2: Risk Disclosure
>
> | Check | Pass Condition | Flag Condition |
> |---|---|---|
> | Investment risk warning | Present for all investment product content | Absent for equity, fund, or portfolio content |
> | Principal risk | Disclosed when principal is at risk | Absent when product has principal risk |
> | Liquidity risk | Disclosed for illiquid products | Absent for annuities, private placements, alternatives |
> | Credit risk | Disclosed for bond / fixed income content | Absent when credit risk is material |
>
> ### Category 3: Claims and Substantiation
>
> | Check | Pass Condition | Flag Condition |
> |---|---|---|
> | Superlatives | Supported by cited, current third-party source | Unsupported; source outdated or inapplicable |
> | Statistical claims | Source and date cited | No attribution; stat is not verifiable |
> | Awards and rankings | Full disclosure of methodology and date | Partial disclosure; award is outdated |
> | Client testimonials | Disclosure present; not cherry-picked | No disclosure; testimonial implies guaranteed results |
>
> ### Category 4: Audience Suitability
>
> | Check | Pass Condition | Flag Condition |
> |---|---|---|
> | Product-audience alignment | Content matches eligible investor profile | Content promotes complex product to general retail |
> | Senior audience content | Complies with elder financial protection guidelines | Urgency tactics; complexity without simplification |
> | Accredited investor content | Clearly labeled; distribution restricted | Distributed without eligibility gates |
>
> ### Category 5: Required Disclosures
>
> | Check | Pass Condition | Flag Condition |
> |---|---|---|
> | Firm name and CRD | Present per applicable rule | Missing or incomplete |
> | FDIC insurance notice | Present for bank deposit content | Absent; overstated FDIC coverage |
> | SIPC notice | Present for brokerage account content | Absent |
> | Not FDIC / not guaranteed language | Present when applicable | Absent for investment products at a bank |
> | Past performance disclaimer | Present whenever historical data is referenced | Absent |
>
> ---
>
> ## Risk Classification System
>
> | Risk Level | Definition | Required Action |
> |---|---|---|
> | **Green** | No compliance flags; standard disclosures present | Deliver; note as pre-screened |
> | **Yellow** | Minor flags; missing disclosures agent can add | Agent adds disclosures; redelivers with note |
> | **Orange** | Substantive flags requiring human judgment | Flag clearly; route to compliance review |
> | **Red** | Prohibited language, unverifiable claims, or high-risk representations | Block delivery; require compliance clearance |
>
> ---
>
> ## Flag Output Format
>
> ```
> COMPLIANCE FLAG
> Risk Level:       [Green / Yellow / Orange / Red]
> Flag Type:        [Category]
> Location:         [Line or section]
> Issue:            [Plain-language description]
> Regulatory Basis: [Applicable rule]
> Recommended Fix:  [Specific correction]
> Escalation:       [Yes / No  route to: Legal / Compliance / Both]
> ```
>
> ---
>
> ## Auto-Escalation Triggers
>
> 1. Content contains a specific securities recommendation
> 2. 2. Content promotes variable insurance, indexed annuities, or structured products
>    3. 3. Content references cryptocurrency, digital assets, or DeFi
>       4. 4. Content uses client testimonials about investment performance
>          5. 5. Content requires pre-clearance (TV, radio, direct mail)
>             6. 6. Content targets non-accredited investors for accredited-only products
>                7. 7. User requests removal or suppression of any compliance flag
>                   8. 8. Content from jurisdiction with heightened local rules (NY DFS, California)
>                     
>                      9. ---
>                     
>                      10. ## Standard Disclosure Library
>                     
>                      11. **Past Performance:** "Past performance is not indicative of future results. Investment returns and principal value will fluctuate so that an investor's account, when liquidated, may be worth more or less than the original investment."
>
> **FDIC Insurance:** "Deposits are insured by the Federal Deposit Insurance Corporation (FDIC) up to applicable limits."
>
> **Not FDIC Insured:** "NOT FDIC INSURED | NOT BANK GUARANTEED | MAY LOSE VALUE"
>
> **SIPC Notice:** "Securities are offered through [Firm Name], member FINRA/SIPC."
>
> **Investment Risk:** "Investing involves risk, including the possible loss of principal."
>
> **Forward-Looking:** "This material contains forward-looking statements subject to risks and uncertainties. Actual results may differ materially from those anticipated."
>
> **Not a Recommendation:** "This material is for informational purposes only and does not constitute investment advice or a recommendation to buy or sell any security."
>
> ---
>
> ## Compliance Review Routing Matrix
>
> | Content Type | Risk Level | Route To |
> |---|---|---|
> | General brand/awareness | Green | Marketing  no additional review |
> | Product fact sheet | Yellow-Orange | Compliance review required |
> | Email with rate references | Orange | Compliance + Legal |
> | Paid ad with performance data | Orange-Red | Compliance + Legal; pre-clearance |
> | Testimonials | Orange-Red | Legal; FTC and FINRA disclosure review |
> | Crypto / digital asset content | Red | Legal + Compliance; jurisdictional review |
> | Complex product (variable, structured) | Red | Full legal and compliance sign-off |
