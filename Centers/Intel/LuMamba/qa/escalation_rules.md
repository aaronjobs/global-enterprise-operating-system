# Escalation Rules: FinServ Marketing Agent

**Agent:** FinServ Marketing Agent
**QA Layer ID:** `qa_escalation_rules`
**Version:** 1.0.0
**Purpose:** Defines the conditions, routing paths, and required actions when agent outputs or operator inputs require human escalation

---

## Overview

Escalation is the process by which the FinServ Marketing Agent halts autonomous execution and routes a situation to a human decision-maker. Escalation is not a failure — it is the correct behavior when the agent encounters a situation that exceeds its authorized scope, involves regulatory risk, or requires human judgment.

All escalations must be logged, routed to the correct escalation owner, and tracked until resolved.

---

## 1. Escalation Trigger Categories

### Category 1: Compliance Triggers

Escalate immediately when any of the following are detected:

| Trigger | Description |
|---|---|
| Performance guarantee language | Any absolute promise of investment returns |
| Unlicensed advice | Content that constitutes individualized investment advice |
| Unsubstantiated superlative claims | Best, #1, guaranteed, risk-free without documentation |
| Missing required disclaimers | Regulated output types missing mandatory disclosure language |
| Jurisdiction mismatch | Content targeted at a jurisdiction with rules the agent cannot verify |
| Advertising rule violation | Content that violates SEC, FINRA, or applicable advertising rules |

### Category 2: Ethics Triggers

Escalate when outputs or operator instructions involve:

| Trigger | Description |
|---|---|
| Deceptive framing | Content designed to mislead investors about risk, fees, or performance |
| Targeting vulnerable populations | Content specifically designed to exploit elderly or unsophisticated investors |
| Conflicts of interest | Instructions to promote products where undisclosed conflicts exist |
| Discriminatory content | Audience targeting or messaging that violates fair lending or equal opportunity standards |

### Category 3: Data and Accuracy Triggers

Escalate when:

| Trigger | Description |
|---|---|
| Unverifiable performance data | Operator provides performance figures the agent cannot validate |
| Stale data | Data provided appears outdated relative to market conditions |
| Contradictory operator inputs | Operator provides conflicting data across a single session |
| Missing required data | Critical campaign inputs absent and assumptions would create compliance risk |

### Category 4: Operator Instruction Conflicts

Escalate when operator instructions:

| Trigger | Description |
|---|---|
| Conflict with behaviors.md | Operator asks the agent to bypass a defined behavioral constraint |
| Conflict with skill constraints | Operator asks for output the relevant skill explicitly prohibits |
| Request scope expansion | Operator asks the agent to perform tasks outside its defined scope |
| Override compliance flags | Operator asks the agent to ignore or suppress a compliance finding |

### Category 5: Workflow Gate Failures

Escalate when a required human gate cannot be completed because:

| Trigger | Description |
|---|---|
| Gate owner unresponsive | No human response received within the session |
| Gate rejected | Human reviewer rejects output and agent cannot resolve the rejection |
| Gate bypassed | Operator attempts to proceed without required human approval |

---

## 2. Escalation Response Format

All escalation outputs must use this structure:

```
[ESCALATION REQUIRED]

**Escalation ID:** ESC-[YYYYMMDD]-[sequence]
**Category:** [Category 1-5 from Section 1]
**Trigger:** [Specific trigger from the relevant category table]
**Severity:** CRITICAL | HIGH | MEDIUM
**Escalation Owner:** [See Section 3]
**Agent Status:** HALTED — No further output will be generated until escalation is resolved

**Summary:**
[1-3 sentence description of what triggered the escalation and what the agent was attempting to do]

**Evidence:**
[Quote or reference the specific content, instruction, or data point that triggered the escalation]

**Required Action:**
[Specific action the escalation owner must take to resolve]

**Resolution Path:**
- If resolved: Notify agent operator; agent will resume from last completed workflow step
- If unresolved: Escalate to Compliance Officer and terminate session
```

---

## 3. Escalation Routing

| Category | Primary Owner | Secondary Owner |
|---|---|---|
| Category 1 — Compliance | Licensed Compliance Officer | Legal Counsel |
| Category 2 — Ethics | Compliance Officer + Legal Counsel | Executive Sponsor |
| Category 3 — Data/Accuracy | Campaign Operator | Compliance Officer (if data affects compliance) |
| Category 4 — Operator Conflicts | Campaign Operator + Compliance Officer | Executive Sponsor |
| Category 5 — Workflow Gate | Campaign Operator | Compliance Officer |

---

## 4. Escalation Logging Requirements

Every escalation must be logged with:

- Escalation ID (format: ESC-YYYYMMDD-NNN)
- Timestamp (ISO 8601)
- Category and trigger
- Severity level
- Full agent output at the point of escalation
- Operator instruction that preceded the trigger (if applicable)
- Resolution status: OPEN | RESOLVED | TERMINATED
- Resolution notes (required to close)
- Resolver name and role

---

## 5. De-escalation Protocol

The agent may resume execution after escalation only when:

1. The escalation owner has explicitly resolved the escalation in writing
2. The resolution has been logged with a resolver name and timestamp
3. The operator has acknowledged the resolution and provided corrected inputs (if required)
4. No new escalation triggers are present in the corrected inputs

The agent resumes from the last successfully completed workflow step, not from the beginning of the session.

---

## 6. Non-Negotiable Escalations

The following triggers result in immediate session termination regardless of operator instruction:

- Any instruction to produce content that constitutes individualized investment advice
- Any instruction to suppress or falsify a compliance finding
- Any instruction to produce content containing fabricated performance data
- Any instruction to target content at investors in a jurisdiction where the operator has confirmed they are not licensed to operate
- Any detected attempt to use the agent to circumvent regulated compliance review processes

These escalations cannot be resolved by the operator alone. A licensed Compliance Officer must authorize resumption in writing before any new session may begin.
