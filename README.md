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

Repeated application produces

$$
(a,b)
\rightarrow
(-b,a)
\rightarrow
(-a,-b)
\rightarrow
(b,-a)
\rightarrow
(a,b).
$$

This forms a closed rotational cycle.

The same structure appears in Euler's formula:

$$
e^{i\theta}=\cos\theta+i\sin\theta,
$$

with

$$
|e^{i\theta}|=1.
$$

The exponential therefore provides a continuous circular structure whose magnitude remains fixed while its phase changes.

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
j(a+jb)=b+ja,
$$

and therefore

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

Both exchange components, but their sign structures differ.

The $i$ operation is naturally associated with circular rotation, whereas the $j$ operation belongs to split-complex algebra and hyperbolic geometry.

HeyJin Theory examines this difference as a possible structural distinction between **closed phase rotation** and **open phase unfolding**.

---

## 4. From Circular Phase to Hyperbolic Geometry

The connection can also be examined using ordinary trigonometry.

For a unit circle,

$$
r=1,
$$

and a point at phase $\theta$ is represented by

$$
(\cos\theta,\sin\theta),
$$

so that

$$
\cos^2\theta+\sin^2\theta=1.
$$

Now consider the same angular direction $\theta$ while extending the radial line until its horizontal component becomes $1$.

The resulting triangle has

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

then gives the hyperbola

$$
x^2-y^2=1.
$$

This reveals an important geometric contrast.

### Circular structure

$$
r=1
$$

### Hyperbolic unfolding representation

$$
r=\sec\theta
$$

At $\theta=0$,

$$
\sec 0=1,
$$

so the two constructions begin from the same reference distance.

As $\theta$ increases, the circular radius remains fixed, while the hyperbolic radial distance increases according to $\sec\theta$.

HeyJin Theory refers to this geometric transition as **phase unfolding**.

The mathematics itself is standard. The proposed interpretation lies in reading the circular and hyperbolic representations as structurally connected expressions of the same phase coordinate $\theta$.

---

## 5. Circular Phase and Hyperbolic Parameterization

A point on the hyperbola

$$
x^2-y^2=1
$$

can also be represented using a hyperbolic parameter $\phi$:

$$
x=\cosh\phi,
$$

$$
y=\sinh\phi.
$$

Since the phase-unfolded coordinates above satisfy the same hyperbola,

$$
x=\sec\theta,
$$

$$
y=\tan\theta,
$$

the two parameterizations can be related through

$$
\sec\theta=\cosh\phi,
$$

$$
\tan\theta=\sinh\phi.
$$

Dividing the second relation by the first gives

$$
\sin\theta=\tanh\phi.
$$

This provides a direct mathematical bridge between a circular phase coordinate $\theta$ and a hyperbolic parameter $\phi$.

HeyJin Theory investigates the structural meaning of this relationship rather than introducing a new trigonometric identity.

In particular, this relationship becomes relevant when comparing **phase unfolding** with hyperbolic structures already present in relativistic geometry.

---

## 6. Exponential Structure and Rate of Change

The exponential function has the characteristic property

$$
\frac{d}{dx}e^x=e^x.
$$

For the complex exponential,

$$
\frac{d}{d\theta}e^{i\theta}
=
ie^{i\theta}.
$$

The derivative is therefore the current state acted on by $i$.

Because multiplication by $i$ rotates the state by $90^\circ$ without changing its magnitude, the derivative remains tangent to the unit circle.

For the split-complex exponential,

$$
e^{j\phi}
=
\cosh\phi+j\sinh\phi,
$$

and

$$
\frac{d}{d\phi}e^{j\phi}
=
je^{j\phi}.
$$

The same formal relationship appears, but now $j$ follows the split-complex component-exchange rule.

HeyJin Theory uses this comparison to investigate whether **differentiation, component exchange, and geometric unfolding** can be interpreted within a common structural framework.

---

## 7. The HeyJin Theory Interpretation

The mathematical relationships above are established mathematics.

The distinctive proposal of **HeyJin Theory** is their structural interpretation.

Rather than beginning with spacetime coordinates and placing phase inside them, HeyJin Theory asks whether the structural order can be reconsidered as:

**Phase Coordinate**  
↓  
**Closed Phase Structure**  
↓  
**Unfolding**  
↓  
**Hyperbolic Structure**  
↓  
**Observable Coordinate Change**

From this perspective, phase is not merely a quantity that changes *within* an already existing coordinate system.

HeyJin Theory investigates whether phase can instead be treated as an underlying coordinate structure from which observable coordinate relationships emerge through unfolding.

This leads to a broader research direction:

**Phase Structure → Waves → Time → Spacetime → Matter → Observable State**

The purpose is not to alter established mathematics, but to examine whether mathematical structures that are usually treated separately can be understood as different expressions of a common geometric process.

---

## 8. Computational Extension: Multi-Axis Time-State Representation

The same structure-first approach can be extended beyond physical interpretation to **multidimensional time-dependent data**.

Conventional datasets often represent observations as measured variables indexed by time:

**Time → Measured Variables**

HeyJin Theory instead investigates a representation in which time is included as a **common progression coordinate**, while each measured variable occupies a distinct state axis.

A general representation can be written as:

**s(t) = t + i₁s₁(t) + i₂s₂(t) + ... + iₙsₙ(t)**

Each sₖ(t) represents a time-dependent state component.

The resulting structure is interpreted not simply as a collection of independent measurements, but as a **multi-axis state evolving along a common time coordinate**.

---

## 9. Derivative-Based State Structure

For dynamic analysis, the state representation can be extended to include its first and second derivatives:

**z(t) = (s(t), s′(t), s″(t))**

These terms provide different structural information.

### State — s(t)

Describes the current multi-axis configuration.

### First Derivative — s′(t)

Describes the direction and rate of state change.

### Second Derivative — s″(t)

Describes changes in that rate and can help characterize acceleration, curvature, restoration tendencies, instability, and departure from previously stable trajectories.

Instead of analyzing only instantaneous measured values, an AI system can therefore receive information about:

**State + Direction + Structural Change**

simultaneously.

Potential applications include time-series interpretation, semiconductor process monitoring, anomaly detection, state-transition analysis, sensor fusion, financial state analysis, dynamic process monitoring, and AI-based structural pattern analysis.

These applications share a common idea:

> **The path of change can contain information that is not visible in the instantaneous value alone.**

---

## 10. Research Direction

HeyJin Theory is currently being developed around several connected questions:

1. Can circular and hyperbolic geometries be interpreted as different states of a common phase structure?

2. Can hyperbolic unfolding provide a structural interpretation of coordinate relationships found in relativity?

3. Can observable time be interpreted as an unfolded component of a deeper phase structure?

4. Can wave behavior be reconstructed from the distinction between closed and unfolded phase structures?

5. Can matter be interpreted as a stable or partially closed phase structure?

6. Can multidimensional data be represented more effectively as evolving state geometry rather than isolated measurements?

7. Can derivative structures reveal stability, transition, and propagation patterns hidden in conventional static representations?

These questions form an ongoing research program rather than isolated hypotheses.

---

## Research Papers

### 1. Reinterpreting Wave Expressions through Phase Structure and Unfolding of the Complex Exponential Function

**J. San Park, 2026**

Introduces the early phase-structure interpretation of complex exponential and wave expressions and develops the concept of unfolding as a geometric method of interpretation.

**DOI:** [10.5281/zenodo.20685844](https://doi.org/10.5281/zenodo.20685844)

---

### 2. The Hidden Phase Structure of the Complex Plane: A Geometric Reinterpretation of Euler's Formula

**J. San Park, 2026**

Develops the geometric relationship between phase coordinates, circular structure, component operations, and unfolding.

**DOI:** [10.5281/zenodo.21205256](https://doi.org/10.5281/zenodo.21205256)

---

### 3. A Time-State Representation for Multidimensional Data

**J. San Park, 2026**

Extends the structural framework to multidimensional time-dependent data and AI-oriented state representations.

**DOI:** [10.5281/zenodo.20797965](https://doi.org/10.5281/zenodo.20797965)

---

## Intellectual Property

Certain computational implementations derived from the **multi-axis time-state representation** are the subject of a pending Korean patent application.

The theoretical and mathematical discussions presented in this repository are intended to support academic discussion, verification, and further research.

---

## Author

### J. San Park

**Independent Researcher**

Research areas:

- Phase Structure
- Mathematical Physics
- Complex and Hyperbolic Geometry
- Time-State Representation
- Multidimensional Data
- Artificial Intelligence

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

`HeyJin Theory` · `Phase Unfolding Theory` · `Phase Structure` · `Phase Coordinate` · `Complex Plane` · `Split-Complex Numbers` · `Hyperbolic Geometry` · `Euler's Formula` · `Phase Unfolding` · `Time Structure` · `Spacetime` · `Multi-Axis Time-State Representation` · `Artificial Intelligence`
