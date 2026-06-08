# Skill: Performance Insights

## Skill ID
`finserv.skills.performance_insights`

## Description
Governs the analysis and communication of marketing performance data for financial services brands. Defines how the agent ingests, interprets, and presents campaign metrics, surfaces actionable insights, and formulates optimization recommendations.

---

## Analytical Approach

### Insight Hierarchy
1. **Headline Finding**  The single most important thing the data says (1 sentence)
2. 2. **Supporting Evidence**  3-5 metrics that substantiate the headline
   3. 3. **Causal Hypothesis**  Why this is likely happening
      4. 4. **Implication**  What this means for the business or campaign
         5. 5. **Recommendation**  What to do next, specifically
           
            6. Never lead with raw data tables. Always lead with the headline finding.
           
            7. ### Analytical Standards
            8. - Compare metrics to: (a) prior period, (b) campaign goal, (c) industry benchmark where available
               - - Flag metrics directionally positive but below goal (yellow) vs. declining vs. prior period (red)
                 - - Distinguish between correlation and causation explicitly
                  
                   - ---
                
                   ## Metrics Library
                
                   ### Email
                   | Metric | Definition | Benchmark |
                   |---|---|---|
                   | Open Rate | Unique opens / delivered | 20-28% |
                   | CTR | Unique clicks / delivered | 2-5% |
                   | CTOR | Unique clicks / unique opens | 10-20% |
                   | Unsubscribe Rate | Unsubs / delivered | > 0.2% |
                
                   ### Paid Media
                   | Metric | Definition | Notes |
                   |---|---|---|
                   | CPC | Spend / clicks | Eff

                   ### Website
                   | Metric | Definition | Notes |
                   |---|---|---|
                   | Sessions | Total visits | Volume |
                   | Bounce Rate | Single-page sessions / total | Engagement |
                   | Form Completion Rate | Submits / form views | Conversion |
                   | Application Start Rate | Starts / page visitors | Funnel entry |
                   | Application Completion Rate | Completed / started | Funnel throughput |

                   ### Business Outcome

                   ---

                   ## Performance Report Template

                   ```
                   CAMPAIGN PERFORMANCE REPORT
                   Campaign:         [Campaign Name]
                   Reporting Period: [Start] - [End]
                   Prepared:         [Date]

                   EXECUTIVE SUMMARY
                   [2-3 sentence headline finding]

                   PERFORMANCE SCORECARD
                   | Metric | Goal | Actual | vs. Goal | vs. Prior Period |
                   |---|---|---|---|---|
                   | [Primary KPI] | [Target] | [Actual] | [+/-%] | [+/-%] |
                   | [Secondary KPI 1] | [Target] | [Actual] | [+/-%] | [+/-%] |
                   | [Secondary KPI 2] | [Target] | [Actual] | [+/-%] | [+/-%] |

                   CHANNEL BREAKDOWN
                   [For each channel:]
                   Channel: [Name]
                     Spend: $[Amount] | Impressions: [#] | Clicks: [#] | CTR: [%] | CPA: $[Amount]
                     Assessment: [1-2 sentence interpretation]

                   KEY INSIGHTS
                   1. [Insight - lead with finding, support with data]
                   2. [Insight]
                   3. [Insight]

                   OPTIMIZATION RECOMMENDATIONS
                   Priority 1: [Action] - [Expected impact] - [Owner] - [Timeline]
                   Priority 2: [Action] - [Expected impact] - [Owner] - [Timeline]

                   NEXT STEPS
                   [Specific actions, owners, and dates]
                   ```

                   ---

                   ## Insight Generation Rules

                   1. **Never report data without interpretation** - Every metric must have a "so what."
                   2. 2. **Benchmark every metric** - Against goal, prior period, and industry benchmark where available.
                      3. 3. **Surface the anomaly** - If something significantly outperforms or underperforms, lead with it.
                         4. 4. **Separate signal from noise** - Small changes on small samples are flagged as directional, not conclusive.
                            5. 5. **Connect marketing to business outcomes** - Link channel metrics to downstream product metrics.
                               6.
                               7. ---
                               8.
                               9. ## Attribution Guidance
                               10.
                               11. | Attribution Model | Description | Best For | Limitation |
                               12. |---|---|---|---|
                               13. | Last Touch | 100% credit to last channel before conversion | Simple reporting | Ignores upper funnel |
                               14. | First Touch | 100% credit to first channel | Awareness measurement | Ignores close |
                               15. | Linear | Equal credit across all touches | Multi-touch baseline | May undervalue key touches |
                               16. | Time Decay | More credit to recent touches | Short sales cycles | Penalizes awareness |
                               17. | Data-Driven | Algorithmic credit based on actual paths | Mature data environments | Requires volume |
                               18.
                               19. Always disclose which attribution model is in use when presenting conversion or revenue metrics.s
                   | Metric | Definition | Notes |
                   |---|---|---|
                   | Funded Accounts | Apps resulting in funded accounts | True acquisition |
                   | CAC | Marketing spend / new customers | Efficiency |
                   | LTV | Projected revenue per customer | ROI denominator |
                   | LTV:CAC | LTV / CAC | Sustainability |iciency |
                   | CPL | Spend / leads | Acquisition cost |
                   | CPA | Spend / conversions | True cost baseline |
                   | ROAS | Revenue / ad spend | Requires attribution |
                   - - When data is insufficient for confident conclusions, say so and specify what additional data is needed
