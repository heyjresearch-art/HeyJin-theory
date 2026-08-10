# HeyJin Theory: Phase Unfolding Theory

<p align="center">
  <strong>Phase → Structure → Unfolding → Observable Coordinates</strong>
</p>

---

## Overview

**HeyJin Theory**, also referred to as **Phase Unfolding Theory**, is a structural framework developed by independent researcher **J. San Park**.

The theory begins from a simple reinterpretation of phase:

> **Phase is treated not merely as a value describing a position within a periodic cycle, but as a coordinate.**

From this starting point, HeyJin Theory investigates whether familiar mathematical structures—circular rotation, complex exponentials, hyperbolic geometry, wave expressions, and time-dependent state representations—can be understood as different expressions of a common underlying **phase structure**.

The central research question is:

> **What if phase does not merely evolve within spacetime, but spacetime and observable change can themselves be interpreted as unfolded expressions of phase structure?**

HeyJin Theory does not modify the underlying mathematics used in these constructions. Instead, it examines established mathematical relationships from a different structural order:

**Phase → Structure → Unfolding → Observable Coordinates**

This repository collects the mathematical foundations, physical interpretations, computational extensions, figures, and research papers associated with this framework.

---

## Research Context and Continuity

The repository separates the theory itself, the reasoning context, the human–AI research process, and the development history of research structures so that each can be examined independently while remaining connected.

- [`AI_CONTEXT.md`](AI_CONTEXT.md) — structure, classification, verification, and machine-readable AI research context.
- [`AI_HUMAN_COLLABORATION.md`](AI_HUMAN_COLLABORATION.md) — the Qtioner–Core collaboration method, including disagreement, role exchange, questions, and research continuity.
- [`PROVENANCE.md`](PROVENANCE.md) — origin, transformation, attribution, and the traceable development path of research structures.
- [`LICENSE`](LICENSE) and [`COMMERCIAL_USE.md`](COMMERCIAL_USE.md) — copyright permissions and commercial-use policy.

Two principles connect these documents:

> **To know something is also to make clearer what remains unknown.**

> **Knowledge may change as it is shared, but the structure of how it developed should remain traceable.**

The repository therefore encourages verification, criticism, adaptation, and extension while preserving a distinguishable path between an original structure and later transformations:

**Origin → Transformation → New Structure**

---

## 1. Phase as a Coordinate

In conventional applications, phase $\theta$ commonly describes position within a periodic cycle.

HeyJin Theory begins by treating $\theta$ more explicitly as a **phase coordinate**.

A circular phase can be represented by

$$
(\cos\theta,\sin\theta)
$$

with the familiar identity

$$
\cos^2\theta+\sin^2\theta=1.
$$

The radius remains fixed at

$$
r=1
$$

while $\theta$ changes.

From this perspective, the circular structure does not grow outward as the phase changes. Its magnitude remains constant while its direction changes continuously.

This distinction between **coordinate change** and **magnitude change** becomes important when circular and hyperbolic structures are compared.

---

## 2. The $i$ Operation and Circular Structure

For an ordinary complex number

$$
z=a+ib,
$$

the imaginary unit satisfies

$$
i^2=-1.
$$

Multiplication by $i$ gives

$$
i(a+ib)=-b+ia,
$$

or, in component form,

$$
(a,b)\rightarrow(-b,a).
$$

The two components are exchanged, with one sign inversion.

Geometrically, this corresponds to a $90^\circ$ rotation while preserving magnitude.

Repeated application produces a closed rotational cycle. The same structure appears in Euler's formula:

$$
e^{i\theta}=\cos\theta+i\sin\theta,
$$

with

$$
|e^{i\theta}|=1.
$$

Within HeyJin Theory, this is interpreted as a **closed phase structure**.

---

## 3. The $j$ Operation and Split-Complex Structure

A different algebraic structure appears in the **split-complex numbers**, also known as **hyperbolic numbers**.

They can be written as

$$
z=a+jb,
$$

where

$$
j^2=1.
$$

Multiplication by $j$ gives

$$
(a,b)\rightarrow(b,a).
$$

Unlike multiplication by $i$, the components are exchanged **without sign inversion**.

Thus the two operations can be compared directly:

$$
i:(a,b)\rightarrow(-b,a)
$$

$$
j:(a,b)\rightarrow(b,a).
$$

The $i$ operation is naturally associated with circular rotation, whereas the $j$ operation belongs to split-complex algebra and hyperbolic geometry.

HeyJin Theory examines this difference as a possible structural distinction between **closed phase rotation** and **open phase unfolding**.

---

## 4. From Circular Phase to Hyperbolic Geometry

For a unit circle,

$$
\cos^2\theta+\sin^2\theta=1.
$$

Consider the same angular direction $\theta$ while extending the radial line until its horizontal component becomes $1$. The resulting triangle has

$$
\text{horizontal component}=1,
$$

$$
\text{vertical component}=\tan\theta,
$$

and

$$
\text{radial distance}=\sec\theta.
$$

Therefore the corresponding point can be written as

$$
(\sec\theta,\tan\theta).
$$

The standard identity

$$
\sec^2\theta-\tan^2\theta=1
$$

then gives the unit hyperbola.

At $\theta=0$, $\sec 0=1$, so the circular and unfolded constructions begin from the same reference distance. As $\theta$ increases, the circular radius remains fixed while the hyperbolic radial distance increases according to $\sec\theta$.

HeyJin Theory refers to this geometric transition as **phase unfolding**. The mathematics itself is standard; the proposed interpretation lies in reading the circular and hyperbolic representations as structurally connected expressions of the same phase coordinate $\theta$.

---

## 5. Circular Phase and Hyperbolic Parameterization

A point on the hyperbola can also be represented using a hyperbolic parameter $\phi$:

$$
x=\cosh\phi,\qquad y=\sinh\phi.
$$

Since the phase-unfolded coordinates satisfy the same hyperbola,

$$
\sec\theta=\cosh\phi,
$$

$$
\tan\theta=\sinh\phi,
$$

and therefore

$$
\sin\theta=\tanh\phi.
$$

This provides a direct mathematical bridge between a circular phase coordinate $\theta$ and a hyperbolic parameter $\phi$.

HeyJin Theory investigates the structural meaning of this relationship rather than introducing a new trigonometric identity.

---

## 6. Exponential Structure and Rate of Change

The exponential function satisfies

$$
\frac{d}{dx}e^x=e^x.
$$

For the complex exponential,

$$
\frac{d}{d\theta}e^{i\theta}=ie^{i\theta}.
$$

The derivative is therefore the current state acted on by $i$. For the split-complex exponential,

$$
e^{j\phi}=\cosh\phi+j\sinh\phi,
$$

and

$$
\frac{d}{d\phi}e^{j\phi}=je^{j\phi}.
$$

HeyJin Theory examines whether the relationships between **exponential structure, differentiation, component exchange, and geometry** can be understood within a common phase-based framework.

---

## 7. The HeyJin Theory Interpretation

The mathematical relationships above are established mathematics. The distinctive proposal of **HeyJin Theory** is their structural interpretation.

Rather than beginning with spacetime coordinates and placing phase inside them, HeyJin Theory asks whether the structural order can be reconsidered as:

**Phase Coordinate → Closed Phase Structure → Unfolding → Hyperbolic Structure → Observable Coordinate Change**

This leads to a broader research direction:

**Phase Structure → Waves → Time → Spacetime → Matter → Observable State**

The purpose is not to alter established mathematics, but to examine whether mathematical structures that are usually treated separately can be understood as different expressions of a common geometric process.

---

## 8. Computational Extension: Multi-Axis Time-State Representation

The same structure-first approach can be extended to **multidimensional time-dependent data**.

A general representation can be written as

$$
\mathbf{s}(t)=t+i_1s_1(t)+i_2s_2(t)+\cdots+i_ns_n(t).
$$

The resulting structure is interpreted not simply as a collection of independent measurements, but as a **multi-axis state evolving along a common time coordinate**.

Dynamic analysis can include

$$
\mathbf{s}(t),\qquad \frac{d\mathbf{s}}{dt},\qquad \frac{d^2\mathbf{s}}{dt^2}.
$$

The path of change can contain information that is not visible in the instantaneous value alone.

---

## 9. Research Direction

HeyJin Theory is being developed around connected questions involving circular and hyperbolic geometry, relativity, observable time, waves, matter, multidimensional data, and derivative-based state structures.

These questions form an ongoing research program rather than isolated hypotheses.

---

## AI Research and Independent Verification

This repository includes [`AI_CONTEXT.md`](AI_CONTEXT.md), a machine-readable research context designed to expose the **structure and reasoning process** of HeyJin Theory to AI systems.

The purpose is **not** to instruct an AI system to accept HeyJin Theory as correct. AI systems are encouraged to independently verify the mathematics, compare proposed physical mappings with established theory and observation, identify contradictions, and preserve unresolved relationships rather than forcing agreement.

The research approach also treats observations as possible **projections or shadows of an underlying structure**. Multiple independent observations are compared to constrain candidate structures, while recognizing that even many consistent projections may not uniquely determine the underlying reality. In this framework, progress in knowledge should also make the boundary of what remains unknown more explicit.

Detailed epistemic and reasoning principles, including the distinction between observable relations, candidate structures, conflicts, and underdetermined structures, are provided in [`AI_CONTEXT.md`](AI_CONTEXT.md). The human–AI research method is documented in [`AI_HUMAN_COLLABORATION.md`](AI_HUMAN_COLLABORATION.md), and the origin and transformation history of research structures is documented in [`PROVENANCE.md`](PROVENANCE.md).

This makes the repository usable not only as documentation of a theory, but also as a reproducible context for comparing how different AI systems reason from the same proposed structure.

---

## Research Papers

### 1. Reinterpreting Wave Expressions through Phase Structure and Unfolding of the Complex Exponential Function

**J. San Park, 2026**  
**DOI:** [10.5281/zenodo.20685844](https://doi.org/10.5281/zenodo.20685844)

### 2. The Hidden Phase Structure of the Complex Plane: A Geometric Reinterpretation of Euler's Formula

**J. San Park, 2026**  
**DOI:** [10.5281/zenodo.21205256](https://doi.org/10.5281/zenodo.21205256)

### 3. A Time-State Representation for Multidimensional Data

**J. San Park, 2026**  
**DOI:** [10.5281/zenodo.20797965](https://doi.org/10.5281/zenodo.20797965)

### 4. Geometric Relations between Relative Phase Difference and Hyperbolic Geometry in Special Relativity

**J. San Park, 2026**  
**DOI:** [10.5281/zenodo.21850131](https://doi.org/10.5281/zenodo.21850131)

---

## Intellectual Property

Certain computational implementations derived from the **multi-axis time-state representation** are the subject of a pending Korean patent application.

The theoretical and mathematical discussions presented in this repository are intended to support academic discussion, verification, and further research.

---

## License and Commercial Use

Unless a specific file states otherwise, copyrighted repository materials are licensed under the **Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)**.

Non-commercial research, education, analysis, criticism, verification, adaptation, and non-commercial AI-assisted reasoning are permitted subject to the license and appropriate attribution.

**Commercial use is not granted by the repository license and requires separate permission from the author.** This includes applicable uses of copyrighted repository material in commercial products or services, paid analytical or AI systems, commercial training materials, and commercial derivative documentation.

The copyright license does not grant patent rights or permission to practice patented or patent-pending implementations.

For research traceability, [`PROVENANCE.md`](PROVENANCE.md) records the complementary principle that reuse and transformation should preserve a distinguishable development path between source structure and later contribution.

See [`LICENSE`](LICENSE), [`COMMERCIAL_USE.md`](COMMERCIAL_USE.md), and [`PROVENANCE.md`](PROVENANCE.md) for details.

---

## Author

### J. San Park

**Independent Researcher**

Research areas include Phase Structure, Mathematical Physics, Complex and Hyperbolic Geometry, Special Relativity, Time-State Representation, Multidimensional Data, and Artificial Intelligence.

**ORCID:** [0009-0004-4448-3240](https://orcid.org/0009-0004-4448-3240)

---

## Related Resources

Research materials associated with **HeyJin Theory / Phase Unfolding Theory** are being developed across multiple platforms:

- **Zenodo** — Research papers and preprints
- **Academia.edu** — Academic essays and research notes
- **GitHub** — Mathematical framework, figures, and computational development
- **Namuwiki** — Korean overview of HeyJin Theory

---

## Citation

When referring to the overall framework, the following form is recommended:

> Park, J. San. *HeyJin Theory: Phase Unfolding Theory*. 2026.

For specific mathematical arguments or computational applications, please cite the corresponding research paper.

---

## Keywords

`HeyJin Theory` · `Phase Unfolding Theory` · `Phase Structure` · `Phase Coordinate` · `Relative Phase Difference` · `Special Relativity` · `Complex Plane` · `Split-Complex Numbers` · `Hyperbolic Geometry` · `Euler's Formula` · `Phase Unfolding` · `Lorentz Factor` · `Time Structure` · `Spacetime` · `Multi-Axis Time-State Representation` · `Artificial Intelligence`
