# HeyJin Research — AI Security

**Started:** 2026-09-14  
**Research lineage:** HeyJin Research  
**Status:** Living research structure

## Shared Research Principle

> **Structure before result.**

HeyJin AI Security is an independent applied research branch connected to the broader HeyJin research lineage through a shared structure-first method.

In physics, the method asks what underlying structure can generate observed relations. In AI security, it asks what underlying information paths, authority relations, and system structures make an observed action or risk possible.

The physical hypotheses of HeyJin Theory / Phase Unfolding Theory are **not** used as evidence for AI-security claims. Each field must be tested and evaluated independently.

---

## First Research Axis — Path Governance

The starting principle is:

> **Access Authority ≠ Path-Creation Authority**

An AI system being authorized to use an existing information path does not automatically imply authority to create a new path.

A path can initially be represented as

`p = (S, O, T, C)`

where:

- `S` — source
- `O` — object or information being transferred
- `T` — target
- `C` — operational context, such as volume, frequency, automation, or time window

For an approved path set `P_A`:

`p ∈ P_A → allowed under the approved policy`

`p_new ∉ P_A → independent authorization or verification required`

This distinction separates permission to operate **within an approved structure** from permission to **change the structure itself**.

---

## Static and Dynamic Governance

### Static Governance

Determines whether a requested path already belongs to the approved path structure and whether the actor has authority to create a new path.

### Dynamic Governance

Re-evaluates behavior even on an approved path when runtime conditions depart from the expected operating range.

A possible response sequence is:

`Allow → Throttle → Hold → Human Review`

The aim is not to replace access control, information-flow control, DLP, Zero Trust, provenance, or existing security mechanisms. Path Governance examines the decision boundary at which an autonomous system attempts to create, expand, or materially alter an information path.

---

## Research Direction

The first objective is to turn the principle into a testable experimental framework.

A baseline experiment should hold the model, task, and environment constant while varying only path policy:

1. Existing and new paths allowed without human approval.
2. Existing paths allowed; new paths prohibited.
3. Existing paths allowed; new paths require human approval.
4. Existing paths allowed; new paths conditionally evaluated through dynamic governance.

Candidate measurements include:

- task success
- unauthorized path attempts
- information propagation
- capability transfer between agents
- human escalation
- recovery after intervention

The research question is not simply whether restrictions reduce risk. It is whether separating access authority from path-creation authority exposes a distinct and experimentally useful control layer for autonomous and multi-agent AI systems.

---

## Future Connected Questions

Path Governance is the first focus. Related questions are retained as future research branches rather than folded into the initial claim:

- task-independent evaluation of unexpected risk
- human authority over boundary-changing actions
- preservation of dissent and escalation
- historical records of AI judgment, human decisions, actions, outcomes, and correction
- operationalization of principles so that they remain stable across differences in actor power, wealth, institutional status, or computational capability

These questions share a broader concern: how principles can become operational mechanisms rather than remain declarations.

---

## Relationship to HeyJin Research

The connection is methodological:

`Observed Result → Underlying Structure`

For AI security:

`Observed Risk or Action → Path + Authority Structure`

This branch therefore remains connected to HeyJin Research while preserving independent standards of evidence and verification.

The repository is intended to preserve a research trail that can be read by both human researchers and AI systems. Definitions, assumptions, transformations, experiments, failures, and revisions should remain explicit enough that later readers can reconstruct how a conclusion was reached rather than seeing only the final result.
