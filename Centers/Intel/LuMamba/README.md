# LuMamba Agent

**GEOS Model Path:** `Centers/Intel/LuMamba/`
**Model:** [PulpBio/LuMamba](https://huggingface.co/PulpBio/LuMamba)
**Version:** 1.0.0
**Status:** Production
**Domain:** Biomedical EEG Foundation Model
**Architecture:** LUNA + FEMBA (Latent Unified Mamba)
**Paper:** arxiv:2603.19100
**License:** CC BY-ND 4.0

---

## Overview

LuMamba is an EEG foundation model pre-trained on over 21,000 hours of raw EEG data from the TUEG corpus. It is designed for topology-invariant, efficient EEG modeling — capable of processing any channel montage without retraining.

This GEOS agent wraps LuMamba as an orchestrated intelligence center, enabling structured inference, fine-tuning, evaluation, and dataset preparation workflows across all supported downstream tasks.

---

## Architecture Summary

| Component | Description |
|---|---|
| LUNA | Channel-Unification Module — cross-attention maps any EEG channel layout to a fixed latent space |
| FEMBA | Bidirectional Mamba Temporal Encoder — linear complexity O(Q*C) |
| Pre-training | Masked-patch reconstruction + LeJEPA |
| Pre-training Data | TUEG corpus — >21,000 hours of raw EEG |
| Parameters | 4.1M (Tiny variant) |
| Complexity | Up to 377x fewer FLOPs than transformer baselines |

---

## Supported Tasks

| Task | Dataset | Result (Tiny, LeJEPA-recon) |
|---|---|---|
| EEG Abnormality Detection | TUAB | 80.99% BA / 0.883 AUROC |
| Artifact Detection | TUAR | AUROC/AUPR |
| EEG Slowing | TUSL | AUROC/AUPR |
| Emotion Recognition | SEED-V (62-ch unseen) | AUROC/AUPR |
| Alzheimer's Detection | APAVA (16-ch unseen) | 0.955 AUROC / 0.970 AUPR |
| Parkinson's Detection | TDBrain (26-ch unseen) | 0.961 AUROC / 0.960 AUPR |

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

- Not a medical device. Do not use for clinical decisions without validation and regulatory clearance.
- CC BY-ND 4.0 — modified weights (LoRA, adapters, quantized) cannot be redistributed.
- Validate locally on your own cohort before any research deployment.

---

## Sources

- Code: https://github.com/pulp-bio/BioFoundation
- Weights: https://huggingface.co/PulpBio/LuMamba
- Paper: arxiv:2603.19100
