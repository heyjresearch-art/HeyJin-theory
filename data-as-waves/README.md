# Data as Waves

> **Represent process data not only by individual sensor values, but also by relationships among signals and by how those relationships progress through time.**

**Paper and public reproducibility package for semiconductor process analysis using relative phase.**

## Research Publication

**J. San Park, “Data as Waves: A Relational Approach to Semiconductor Process Analysis Using Relative Phase,” 2026.**

**Zenodo Concept DOI:** [10.5281/zenodo.23191068](https://doi.org/10.5281/zenodo.23191068)

The Zenodo record is the archival research package and contains the paper together with the public reproducibility code. The Concept DOI is used here so that this repository continues to point to the research package across Zenodo versions.

## Core Concept

Conventional process analysis often begins from individual sensor measurements and asks how those values relate to a process result.

This study adds a second level of representation:

> **The relationship formed between sensor signals can itself be treated as process-state information, and the path through which that relationship evolves can contain additional information.**

The research structure is:

`Sensor Data → Recurrent Structure → Relational State → Relational Progression → Process Representation`

The aim is not to replace individual sensor values. It is to examine whether relational information that is normally compressed or discarded during analysis can clarify process state and process outcomes.

## From Sensor Values to Relational State

Using BOSCH plasma-etching process data, a recurrent temporal structure is first identified directly from the timestamped sensor data and then compared with the process recipe.

Within that recurrent structure, the relationship between **Platen RF Load Power** and **Pressure** is represented through relative phase.

A cycle-wise relational state can be written as

`r_k = (cos Δθ_k, sin Δθ_k)`

where `Δθ_k` is the relative phase for cycle `k`.

This representation preserves a relationship between signals rather than treating each signal only as an independent value.

## Relational Progression

A current relational state does not necessarily contain all information about how that state was reached.

The study therefore also examines the progression of the cycle-wise relational states.

`r_1 → r_2 → r_3 → ... → r_n`

Progression measures include direction continuity, total relational path, net displacement, circular variance, and early–late displacement.

The analysis distinguishes **Relational State** from **Relational Progression**:

`Current Relationship + Path of Relationship Change → Expanded Process Representation`

Relational change itself is not defined as abnormal. Instead, progression is tested for whether it provides additional explanatory or predictive information.

## Reproducibility Structure

The public reproducibility package follows the main analytical path reported in the paper:

`Raw Sensor Data`
`→ Recurrent-Structure Discovery`
`→ Relative Phase / Relational State`
`→ Relational Progression`
`→ Out-of-Fold Predictive Evaluation`
`→ Reported Results`

The public code is intended to reproduce the principal analyses and reported results within the public disclosure scope of the paper.

The archival Zenodo package should be treated as the reference public release for the paper and reproducibility materials.

## Relationship to the Broader Research

This work develops naturally from the repository’s broader time-state research direction.

The earlier **Multi-Axis Time-State Representation** asks how measured states evolve along a common temporal progression. Data as Waves extends that question toward relationships among signals:

`Time-State → Relational State → Relational Progression`

The common research question is not that every intermediate path must be preserved. It is whether information compressed while obtaining a result still contains useful structure for understanding state, transition, or outcome.

## Public Scope

This repository page describes the published research and its reproducibility structure. It does not imply public release of unpublished extensions, private research code, raw datasets with separate redistribution conditions, or patent-related implementation details beyond the published disclosure.

Copyrighted materials in this repository are subject to the repository-level **CC BY-NC 4.0** license unless a specific file states otherwise. The copyright license does not grant patent rights.

---

### One idea to remember

> **A process result can become clearer when we examine not only the measured states, but also the relationships and progression through which those states were formed.**
