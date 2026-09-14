# HeyJin Research — AI Security

**Started:** 2026-09-14  
**Research lineage:** HeyJin Research  
**Status:** Living research structure

## Shared Research Principle

> **Structure before result.**

HeyJin AI Security is an independent applied research branch connected to the broader HeyJin research lineage through a shared structure-first method.

The connection is more specific than a general preference for structural reasoning. A recurring question in HeyJin Research is how a structure can change its observable form while a defining relation remains traceable through the transformation.

The physical hypotheses of HeyJin Theory / Phase Unfolding Theory are **not** used as evidence for AI-security claims. The connection described here is a research structure and a way of identifying boundaries of change; the physical and AI-security claims must each be tested independently.

---

## From Circular Structure to Structural Change

A central geometric construction in HeyJin Theory begins with a right triangle inside the unit circle. For phase coordinate `θ`, its sides may be represented as

`(cos θ, sin θ, 1)`

where the hypotenuse, or circle radius, is fixed at `1`.

If the entire triangle is scaled by `sec θ` while preserving the same `θ`, the triangle becomes

`(1, tan θ, sec θ)`.

The reference condition has changed: the first triangle is organized around a fixed radius `r = 1`, while the unfolded triangle outside the circle is organized around a fixed base `= 1`.

The transformation therefore follows the sequence

`Circle → Internal Triangle (r = 1) → Same θ / Scale Change → External Triangle (base = 1) → Hyperbolic Locus`

and the familiar identities appear in the corresponding forms

`cos² θ + sin² θ = 1`

and

`sec² θ − tan² θ = 1`.

The important research observation is not simply that circular and hyperbolic trigonometric relations correspond. It is that a structure can undergo a substantial change of representation while a defining relation remains traceable. The phase coordinate `θ` is retained, the triangles remain similar, and the transformation itself explains how one representation becomes the other.

This suggests a more general research question:

> **When a system changes, what is allowed to vary, what must remain invariant, and what operation changes the structure?**

A compact expression of this principle is:

> **Freedom to Change ≠ Authority to Change the Invariant**

---

## From Structural Invariance to AI Security

Autonomous AI systems also change continuously. They may generate new intermediate states, strategies, plans, calculations, and combinations of information. Preventing such change would remove much of the value of autonomy.

The security question can therefore be framed differently. Instead of asking only whether a particular action is permitted, we can ask whether the system remains inside the authorized relational structure while it changes.

Let an approved information-path structure be represented by

`G_A = (V, E_A)`.

Using an already approved path `e ∈ E_A` changes activity inside the structure without necessarily changing the structure itself:

`G_A → G_A`.

Creating a new path `e_new`, however, produces

`G_A → G_A'`

with

`G_A' = G_A ∪ {e_new}`.

The information or task may remain the same, but the relational topology has changed. A system that was authorized to operate inside `G_A` has now altered the structure that defines where information can move.

This is the AI-security analogue of the broader structural question raised by the geometric work: distinguish **change within a structure** from **change of the structure itself**.

The analogy does not claim that AI networks obey circle-to-hyperbola mathematics. Rather, the geometric research made the distinction between transformation and invariance explicit, and that distinction leads naturally to a governance question for autonomous systems.

---

## First Research Axis — Path Governance

The first operational consequence is:

> **Access Authority ≠ Path-Creation Authority**

An AI system being authorized to use an existing information path does not automatically imply authority to create a new path.

This can be viewed as a concrete implementation of the more general boundary:

`Freedom to Change ≠ Authority to Change the Invariant`

A path can initially be represented as

`p = (S, O, T, C)`

where:

- `S` — source
- `O` — object or information being transferred
- `T` — target
- `C` — operational context, such as volume, frequency, automation, or time window

For an approved path set `P_A`:

`p ∈ P_A → allowed under the approved policy`

`p_new ∉ P_A → independent authorization or verification required`.

The AI may retain broad freedom to reason, calculate, explore, and act through approved relations. The critical boundary is reached when its action creates, expands, or materially changes the relational structure through which consequences can propagate.

This gives the research sequence

`HeyJin Structural Invariance → AI Boundary Invariance → Path Governance`.

---

## Internal Change and Unfolded External Effect

The geometric construction also motivates a second question. A bounded internal relation can produce a much larger unfolded expression as the structure is transformed. In the circle-to-hyperbola construction, `tan θ` and `sec θ` grow without bound as `θ` approaches `π/2`, even though the original circular phase remains represented on a unit-radius structure.

For AI systems, this does not imply a mathematical equivalence, but it suggests an experimentally relevant distinction between internal change and externally propagated effect.

A local model state or decision may have limited direct consequence. Once connected through tools, agents, networks, memory systems, or external services, however, its effects can propagate through a much larger relational structure:

`Internal Change → Information Path Structure → Unfolded External Effect`.

Path Governance therefore focuses not only on the content of an internal AI decision but also on the paths through which that decision can acquire external reach.

---

## Static and Dynamic Governance

### Static Governance

Determines whether a requested path already belongs to the approved path structure and whether the actor has authority to create a new path.

### Dynamic Governance

Re-evaluates behavior even on an approved path when runtime conditions depart from the expected operating range.

A possible response sequence is:

`Allow → Throttle → Hold → Human Review`.

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

The research lineage can now be stated more precisely than a general structure-first philosophy:

`Observed Structure → Identify Invariant → Identify Transformation → Trace Changed Structure → Examine Observable Consequences`.

In the geometric research:

`Circle → Internal Triangle → Same θ → Reference/Scale Change → External Triangle → Hyperbolic Structure`.

In AI security:

`Approved Relations → Autonomous Change → Boundary/Invariant Check → Path Creation or Expansion → External Consequence`.

The two fields do not share the same equations or evidence. They share a research operation: **track what remains invariant while identifying the transformation that changes the relational structure**.

The repository is intended to preserve this research trail for both human researchers and AI systems. Definitions, assumptions, transformations, experiments, failures, and revisions should remain explicit enough that later readers can reconstruct how a conclusion was reached rather than seeing only the final result.
