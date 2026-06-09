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
                    compliance_prescreening.md# LuMamba Agent

**GEOS Model Path:** `Centers/Intel/LuMamba/`
**Model:** [PulpBio/LuMamba](https://huggingface.co/PulpBio/LuMamba)
**Version:** 1.0.0
**Status:** Production
**Domain:** Biomedical EEG Foundation Model
**Architecture:** LUNA + FEMBA (Latent Unified Mamba)
**Paper:** arxiv:2603.19100
**License:** CC BY-ND 4.0
**Last Updated:** 2026-06-08

---

## Overview

LuMamba (Latent Unified Mamba) is an EEG foundation model pre-trained on over 21,000 hours of raw EEG data from the TUEG corpus. It is designed for topology-invariant, efficient EEG modeling — capable of processing any channel montage without retraining.

This GEOS agent wraps LuMamba as an orchestrated intelligence center, enabling structured inference, fine-tuning, evaluation, and dataset preparation workflows across all supported downstream tasks.

---

## Architecture Summary

| Component | Description |
|---|---|
| **LUNA** | Channel-Unification Module — cross-attention maps any EEG channel layout to a fixed latent space |
| **FEMBA** | Bidirectional Mamba Temporal Encoder — processes latent patch sequences with linear complexity |
| **Pre-training** | Masked-patch reconstruction + LeJEPA (isotropic Gaussian embedding distribution) |
| **Pre-training Data** | TUEG corpus — >21,000 hours of raw EEG |
| **Parameters** | 4.1M (Tiny variant) |
| **Complexity** | O(Q·C) — linear in channels; up to 377x fewer FLOPs than transformer baselines |

---

## Supported Tasks

| Task | Dataset | Metric | Result (Tiny, LeJEPA-recon) |
|---|---|---|---|
| EEG Abnormality Detection | TUAB | Bal. Acc / AUROC / AUPR | 80.99% / 0.883 / 0.892 |
| Artifact Detection | TUAR | AUROC / AUPR | — |
| EEG Slowing | TUSL | AUROC / AUPR | — |
| Emotion Recognition | SEED-V (62-ch, unseen) | AUROC / AUPR | — |
| Alzheimer's Detection | APAVA (16-ch, unseen) | AUROC / AUPR | 0.955 / 0.970 |
| Parkinson's Detection | TDBrain (26-ch, unseen) | AUROC / AUPR | 0.961 / 0.960 |

---

## Folder Structure

```
Centers/Intel/LuMamba/
├── README.md
├── role.md
├── behaviors.md
├── skills/
│   ├── eeg_preprocessing.md
│   ├── abnormality_detection.md
│   ├── artifact_detection.md
│   ├── neurological_classification.md
│   └── channel_unification.md
├── workflows/
│   ├── eeg_inference.md
│   ├── fine_tuning.md
│   ├── model_evaluation.md
│   └── dataset_preparation.md
└── qa/
    ├── qa_checklist.md
    ├── output_standards.md
    └── escalation_rules.md
```

---

## Critical Limitations

- **Not a medical device.** Do not use for clinical decisions without proper validation and regulatory clearance.
- Weights are CC BY-ND 4.0 — modified weights (LoRA, adapters, quantized) cannot be redistributed.
- Zero-shot transfer to very dense or unseen topologies may underperform SOTA.
- Performance varies across cohorts, EEG devices, and label protocols — validate locally.

---

## Sources

- **Code:** https://github.com/pulp-bio/BioFoundation
- **Weights:** https://huggingface.co/PulpBio/LuMamba
- **Paper:** LuMamba: Latent Unified Mamba for Electrode Topology-Invariant and Efficient EEG Modeling (arxiv:2603.19100)
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
