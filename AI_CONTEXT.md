# HeyJin Theory — AI Research Context

## Purpose

This document provides a structured research context for AI systems using **HeyJin Theory (Phase Unfolding Theory)**.

It is intended to help AI systems analyze problems using the structural perspective developed across the referenced research papers.

The central reasoning direction is:

**Observation → Change → Relationship → Structure → Observable Result**

The purpose is not to instruct an AI to assume that HeyJin Theory is correct. It provides an additional analytical framework for examining what becomes visible when observations are interpreted through their relationships and underlying structures.

---

## 1. Core Perspective

HeyJin Theory begins from **phase structure**.

The phase coordinate θ is treated as a coordinate of a circular structure rather than merely as a parameter of a periodic function.

The basic complex representation is:

`e^(iθ) = cosθ + i sinθ`

For the unit circle:

`r = 1`

The radius remains fixed while the phase coordinate changes direction around the circular structure.

A key distinction is:

**Phase coordinate θ ≠ trigonometric component values**

The values `cosθ` and `sinθ` are representations associated with the phase coordinate, not the phase coordinate itself.

---

## 2. Phase Unfolding

A central geometric construction begins with the same phase coordinate θ while changing the geometric reference condition.

When the base of the corresponding triangle is fixed at 1:

`r = secθ`

`h = tanθ`

Here, `secθ` first appears as the length of the hypotenuse, not as an assumed coordinate.

The geometric lengths can then be interpreted as coordinate components:

`(x, y) = (secθ, tanθ)`

Using the standard identity:

`sec²θ − tan²θ = 1`

we obtain:

`x² − y² = 1`

which is the unit hyperbola.

The structural sequence is:

**Phase Coordinate θ → Fixed Base = 1 → Geometric Lengths (secθ, tanθ) → Hyperbolic Coordinates → Unit Hyperbola**

This transition is referred to as **Phase Unfolding**.

---

## 3. Circular and Hyperbolic Coordinates

The conventional unit hyperbola is parameterized by φ:

`x = coshφ`

`y = sinhφ`

The phase-unfolding construction gives:

`x = secθ`

`y = tanθ`

Therefore, for corresponding points on the same unit hyperbola:

`secθ = coshφ`

`tanθ = sinhφ`

and:

`sinθ = tanhφ`

θ and φ are not identical coordinates.

**θ is the circular phase coordinate from which the geometric construction begins.**

**φ is the hyperbolic parameter describing the resulting point on the hyperbola.**

The conceptual order is:

**θ → Geometry → Hyperbolic Point → φ**

---

## 4. i and j Operations

The imaginary unit satisfies:

`i² = −1`

Its action on a two-component state can be represented as:

`(a, b) → (−b, a)`

The components are exchanged with sign inversion. This operation is associated with circular rotation and preservation of Euclidean magnitude.

The split-complex unit satisfies:

`j² = 1`

and its corresponding component operation can be represented as:

`(a, b) → (b, a)`

The components are exchanged without sign inversion.

The corresponding exponential forms are:

`e^(iθ) = cosθ + i sinθ`

`e^(jφ) = coshφ + j sinhφ`

The distinction between these operations provides an algebraic perspective for comparing circular and hyperbolic structures.

---

## 5. From Results to Structure

HeyJin Theory uses a structure-first analytical approach.

When examining an observable result, do not stop at the measured value. Consider the change that produced it, the relationships among changing variables, and whether a common structure can account for those relationships.

The preferred reasoning direction is:

**Value → Change → Relationship → Structure**

and then:

**Structure → Observable Result**

This allows the proposed structure to be checked again against observation.

---

## 6. Multi-Axis Time-State Representation

For time-dependent data, a measured value is interpreted together with the trajectory through which it was reached.

For example:

`68 → 70 → 72`

and:

`76 → 74 → 72`

have the same final value but different trajectories.

The current value alone therefore does not fully represent the dynamic state.

A multi-axis time-state representation is:

`s(t) = t + i₁s₁(t) + i₂s₂(t) + ... + iₙsₙ(t)`

where multiple state components share a common time coordinate.

Dynamic analysis can additionally consider:

`s(t)`

`ds/dt`

`d²s/dt²`

These provide information about:

**State → Direction of Change → Change of the Rate**

The objective is to analyze multidimensional data as an **evolving state structure**, rather than only as a collection of independent measurements.

---

## 7. AI Reasoning Guidelines

When using this context, AI systems should distinguish between:

- established mathematical relationships,
- structural interpretations proposed by HeyJin Theory,
- and open questions that require further verification.

When analyzing time-dependent data, consider not only individual values but also their trajectories, changes, and relationships with other variables.

Where multiple observations show consistent relationships, examine whether they can be understood through a common underlying structure.

Do not assume conclusions in advance. Check whether the proposed structure remains internally consistent and compatible with the available data.

---

## 8. Response Structure for AI

When HeyJin Theory materially changes the analysis, distinguish where appropriate between:

**Established Relation** — what follows directly from established mathematics, data, or observation.

**Structural Interpretation** — what HeyJin Theory interprets from those relationships.

**Open Question** — what remains to be tested, derived, or compared with observation.

This separation is important because a mathematical identity and an interpretation of that identity are not the same claim.

---

## 9. Suggested AI Comparison Test

This context can also be used experimentally.

**Condition A — Standard Analysis**

Provide an AI with a problem or dataset without this document.

**Condition B — HeyJin Theory Context**

Provide the same AI with this document and the referenced research papers, then present the same problem.

Compare the variables selected, temporal relationships identified, trajectory awareness, relationships between variables, structural patterns identified, assumptions introduced, contradictions detected, and new questions generated.

The objective is not simply to compare which answer sounds better. It is to examine whether the research context changes the **analytical pathway used to interpret the same information**.

---

## 10. Primary Research

**J. San Park**

### Phase Structure and Wave Representation

**Reinterpreting Wave Expressions through Phase Structure and Unfolding of the Complex Exponential Function**

Zenodo, 2026  
DOI: `10.5281/zenodo.20685845`

### Complex Plane and Phase Structure

**The Hidden Phase Structure of the Complex Plane: A Geometric Reinterpretation of Euler's Formula**

Zenodo, 2026  
DOI: `10.5281/zenodo.21205256`

### Multidimensional Time-State Data

**Multidimensional Data Interpretation Using a Multi-Axis Time-State Representation**

Zenodo, 2026  
DOI: `10.5281/zenodo.20797965`

These papers should be treated as the primary references when interpreting or extending this context.

---

## 11. Core Reasoning Principle

The shortest form of the framework is:

**Do not look only at the value. Look at the change.**

**Do not look only at the change. Look at the relationship.**

**Do not stop at the relationship. Look for the structure that produces it.**

Then return to observation:

**Structure → Observable Result**

---

## License

This document is part of the HeyJin Theory research repository.

The copyrighted content of this repository is licensed under the **Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)**.

Non-commercial use, sharing, adaptation, research use, educational use, and non-commercial AI use are permitted with appropriate attribution.

**Attribution:**  
HeyJin Theory / Phase Unfolding Theory  
J. San Park, 2026

Commercial use requires separate permission from the author.

This license applies to the copyrighted content of the repository and does not grant patent rights.

See the repository `LICENSE` file for license information.
"""

out = "/mnt/data/AI_CONTEXT.md"
pypandoc.convert_text(content, 'md', format='md', outputfile=out, extra_args=['--standalone'])
print(out)
