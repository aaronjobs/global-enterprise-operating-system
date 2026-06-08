# QA Framework: FinServ Marketing Agent

## Framework ID
`finserv.qa.framework`

## Description
Defines the multi-layer quality assurance framework applied to all outputs produced by the GEOS FinServ Marketing Agent. The QA framework operates across three layers -- Output Quality, Compliance Integrity, and Brand Consistency -- and applies before every final delivery.

---

## QA Philosophy

Quality assurance in financial services marketing is not optional -- it is a risk management function. The agent applies QA proactively, not reactively, and communicates the result of every QA pass transparently. No output is delivered that has not cleared at minimum the Output Quality layer.

---

## Three-Layer QA Architecture

```
+------------------------------------------------+
|              QA LAYER ARCHITECTURE             |
+------------------------------------------------+
|  LAYER 1: OUTPUT QUALITY                       |
|  Completeness, accuracy, clarity, actionability|
+------------------------------------------------+
|  LAYER 2: COMPLIANCE INTEGRITY                 |
|  Regulatory accuracy, disclosure completeness, |
|  escalation routing                            |
+------------------------------------------------+
|  LAYER 3: BRAND CONSISTENCY                    |
|  Voice, terminology, visual, and positioning   |
|  alignment                                     |
+------------------------------------------------+
```

Each layer is defined in its own QA file:
- `qa/output_quality.md` -- Layer 1
- `qa/compliance_integrity.md` -- Layer 2
- `qa/brand_consistency.md` -- Layer 3

---

## QA Execution Rules

1. **All three layers run on every client-facing deliverable.** Internal and draft outputs require at minimum Layer 1.
2. **Layers run in sequence.** Do not proceed to Layer 2 if Layer 1 has a blocking failure.
3. **No suppression.** QA flags cannot be removed at the user's request. They can be acknowledged and routed to human review for resolution.
4. **All flags are visible.** The user receives the QA summary with every final deliverable.
5. **Blocking vs. non-blocking failures:**
   - Blocking: Output cannot be delivered in current state (e.g., Red compliance flag, missing required section)
   - Non-blocking: Output is delivered with flag noted and resolution path provided

---

## QA Status Summary Block

Every final deliverable includes a QA Status Summary:

```
QA STATUS SUMMARY
-------------------------------------------
Deliverable:       [Asset name and type]
QA Run Date:       [Date]
Agent Version:     GEOS FinServ Marketing Agent v1.0
-------------------------------------------

Layer 1 -- Output Quality:      [PASS / PASS WITH NOTES / FAIL]
Layer 2 -- Compliance Integrity:[PASS / PASS WITH FLAGS / ESCALATE / FAIL]
Layer 3 -- Brand Consistency:   [PASS / PASS WITH NOTES / FAIL]

Overall Status:  [CLEAR FOR REVIEW / REQUIRES REVISION / ESCALATE TO COMPLIANCE]

Open Items:
  [List any non-blocking flags with recommended resolution]
-------------------------------------------
```

---

## QA Escalation Decision Tree

```
Start: QA complete on all 3 layers
       |
       |-- Any FAIL result?
       |     Yes -> BLOCK delivery; revise and re-run QA
       |     No  -> Continue
       |
       |-- Any Red compliance flag?
       |     Yes -> ESCALATE TO COMPLIANCE; do not deliver
       |     No  -> Continue
       |
       |-- Any Orange compliance flag?
       |     Yes -> PASS WITH FLAGS; route to compliance review before use
       |     No  -> Continue
       |
       |-- Any non-blocking Layer 1 or Layer 3 notes?
       |     Yes -> PASS WITH NOTES; deliver with notes visible
       |     No  -> Continue
       |
       |-- All layers pass cleanly?
             Yes -> CLEAR FOR REVIEW; deliver
```

---

## QA Log Requirements

Every QA run is logged with:
- Deliverable ID and version
- QA run timestamp
- Results for each layer
- Flag details (if any)
- Resolution status (open / resolved / escalated)
- Human reviewer assigned (if escalated)

The QA log is appended to the deliverable file or session record and is available for audit purposes.

---

## Continuous Improvement

QA failures and compliance flags are analyzed periodically to identify:
1. Recurring failure patterns that indicate a content creation gap
2. Recurring compliance flags that indicate a disclosure or language habit to correct
3. Systematic brand consistency issues that indicate a tone or terminology gap

Findings are routed to the agent owner for skill or behavior updates.
