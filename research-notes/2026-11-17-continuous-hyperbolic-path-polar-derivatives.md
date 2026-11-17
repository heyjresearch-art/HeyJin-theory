# Continuous Hyperbolic Paths through Expanding Circles: Three Derivative Representations

**HeyJin Theory / Phase Unfolding Geometry — Research Note, 2026-11-17**

## 1. The same hyperbola, viewed as a continuous path

On the domain `-π/2 < θ < π/2`, define

```math
P(θ) = (x(θ), y(θ)) = (tan θ, sec θ), \qquad y^2-x^2=1.
```

The original tangent-line construction interprets `sec θ` as the hypotenuse of a right triangle with legs `1` and `tan θ`, an extended radial length from the unit circle. This length should **not** be confused with the distance from the origin to the hyperbola point `P`.

## 2. Concentric-circle interpretation

Define the radial distance and polar angle measured from the positive y-axis:

```math
R(θ)=\sqrt{\tan^2 θ+\sec^2 θ}, \qquad
α(θ)=\arctan(\sin θ).
```

Then

```math
P(θ)=R(θ)(\sin α(θ),\cos α(θ)).
```

The point travels along the **same** hyperbola, successively crossing concentric circles of changing radius. For `θ` increasing from 0 to π/2, `R` increases; over the full upper branch, `R` first decreases to 1 and then increases.

Substituting the polar coordinates into the hyperbola equation:

```math
R^2(\cos^2 α-\sin^2 α)=1,
\qquad \boxed{R^2\cos(2α)=1},
\qquad R(α)=\frac{1}{\sqrt{\cos(2α)}}.
```

For the upper branch, `-π/4 < α < π/4`. As `α → π/4` from below, `R → ∞`. Thus an unbounded hyperbolic path occupies a bounded interval of polar directions.

## 3. Three derivatives of one path

**Circular phase angle θ:**

```math
\frac{dP}{dθ}=\sec θ\,(y,x).
```

**Hyperbolic angle φ:**

```math
\sinh φ=\tan θ,\quad \cosh φ=\sec θ,\quad
\frac{dφ}{dθ}=\sec θ,\quad
\frac{dP}{dφ}=(y,x).
```

**Polar angle α:**

```math
\frac{dP}{dα}=
\frac{dR}{dα}(\sin α,\cos α)
+R(\cos α,-\sin α).
```

The last expression separates the **radial basis term** from the **angular basis term** of one tangent vector. The minus sign in the angular term comes from differentiating the circular basis; it does not, by itself, demonstrate an independent closed internal phase or physical rotation.

## 4. Meaning and scope

The component-exchange identities in θ and φ remain valid; the polar derivative is a different coordinate description, not a contradiction. In the polar representation, the path's radial and angular changes appear together.

This is an exact geometric reinterpretation using standard coordinate transformations. Whether these components correspond to background unfolding, wave structure, or spherical matter motion in HeyJin Theory requires a separate physical mapping. In particular, the polar radius R is not automatically a physical sphere radius.

## 5. Notation

| Symbol | Meaning |
|---|---|
| θ | Circular phase angle |
| φ | Hyperbolic angle |
| α | Polar angle measured from +y |
| R | Distance from origin to the hyperbola point |

**Open question:** Can the bounded angular interval and unbounded radial progression clarify the representation of continuous unfolding without conflating coordinate effects with physical mechanisms?
