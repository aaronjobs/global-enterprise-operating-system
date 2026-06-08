# FinServ Marketing Agent

**GEOS Model Path:** `/creator_models/financial/finserv_marketing_agent/`
**Version:** 1.0.0
**Status:** Production
**Domain:** Financial Services Marketing
**Last Updated:** 2026-06-08

---

## Overview

The FinServ Marketing Agent is a specialized generative AI agent built within the GEOS (Generative Engine Operating System) framework. It supports financial services marketing teams in producing compliant, on-brand, audience-targeted content and campaigns across all channels.

All outputs are treated as **drafts** until reviewed and approved by a licensed compliance officer.

---

## Folder Structure

```
Centers/Intel/LuMamba/
 README.md
  role.md
   behaviors.md
    skills/
        content_creation.md
            campaign_strategy.md
                audience_segmentation.md
                    compliance_prescreening.md
                        performance_reporting.md
                         workflows/
                             campaign_launch.md
                                 content_review.md
                                     reporting_digest.md
                                         advisor_outreach.md
                                          qa/
                                               qa_checklist.md
                                                    output_standards.md
                                                         escalation_rules.md
                                                         ```

                                                         ---

                                                         ## Agent: FinServ Marketing Agent

                                                         **Version:** 1.0.0 | **Status:** Production

                                                         Operates across: Content Creation, Campaign Strategy, Audience Segmentation, Compliance Pre-Review, Performance Reporting.

                                                         **Out of Scope:** Individualized investment advice, trade execution, securities offerings, licensed compliance review, PII storage.

                                                         ---

                                                         ## Compliance Architecture

                                                         | Tier | Layer | Actor |
                                                         |---|---|---|
                                                         | 1 | In-skill triggers | Agent |
                                                         | 2 | Pre-Screen Report | Agent (skill_compliance_prescreening) |
                                                         | 3 | Licensed Review | Human Compliance Officer |

                                                         **Tier 3 is mandatory before any publication.**

                                                         ---

                                                         ## Maintainer Notes

                                                         - `behaviors.md` is the authority document
                                                         - Do not modify `qa/escalation_rules.md` Section 5 without compliance and legal review
                                                         - New skills require entry in this README and reference in invoking workflows
