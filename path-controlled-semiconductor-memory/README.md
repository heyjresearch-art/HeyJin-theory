# Path-Controlled Semiconductor Memory

> **Memory through carrier-path control rather than reliance on retained stored charge.**

**Research and technology development based on the patent-pending Transition-Controlled Semiconductor Memory architecture.**

## Core Concept

Conventional semiconductor memory commonly represents information through stored charge or charge-dependent electrical states. Path-Controlled Semiconductor Memory explores a different architectural viewpoint:

> **Information can be represented by a physical state that controls how carriers enter and propagate through the device, rather than requiring the information itself to be represented solely by retained stored charge.**

The architecture places a transition region between the source and channel. The physical state of this region controls the carrier-injection barrier or injection condition, and the resulting channel current becomes the observable memory state.

`Transition State → Carrier Injection → Channel Current → Memory State`

The transition state may be implemented through physical mechanisms including polarization, magnetization, trap occupation, interface states, local charge distribution, or energy-barrier configuration. The concept is therefore not restricted to a single storage material or physical mechanism.

## Why This Matters

The central question changes from:

> **How much stored charge must be retained?**

into:

> **What carrier-transition state must be maintained?**

This distinction opens a path toward memory architectures in which information retention is based on a stable physical transition condition. Readout can then be performed by observing the current response produced through that state.

The architecture also separates state control from read/verification. Programming and correction act on the transition region, while read and verification operations can be performed under conditions intended not to substantially disturb the stored transition state.

## Memory and Logic in the Same Current Path

A particularly important feature of the architecture is that the stored state directly determines current flow.

`Stored State → Carrier Path → Current Response → Computation`

The stored physical state therefore does not need to exist only as an abstract value that is first retrieved and then separately supplied to a logic unit. Its electrical consequence already appears as a current response in the device.

This creates a natural bridge between **memory and computation**.

Potential directions include:

- non-volatile memory
- multi-level memory
- analog state storage
- in-memory computing
- neuromorphic weight control
- current-based computational arrays

In an array, current responses from multiple devices may participate directly in accumulation, comparison, weighting, or other state-based operations.

## Adaptive State Control

The proposed control method does not assume that a single programming pulse always produces the intended memory state.

Instead, it uses a feedback sequence:

`Read → Compare → Program → Verify → Correct → Confirm`

A target current range is defined for the desired memory state. The device can first read its present condition, determine an appropriate programming pulse, verify the resulting current, and apply corrective pulses when necessary.

This control structure can also account for operating factors such as temperature, degradation, reference-current variation, and previous programming history.

## From Charge Storage to Path State

The broader architectural idea can be summarized as:

`Charge-Centered Storage → Transition-State Control → Carrier-Path Response → Memory + Computation`

The term **Path-Controlled Semiconductor Memory** is used here as the research and technology name for this broader architectural direction. The filed patent uses the formal title **Control Method of Transition-Controlled Semiconductor Memory Device**.

The goal of this research page is to make the underlying concept, architecture, and future development path easier to understand than a patent document alone.

## Patent Status

A Korean patent application covering the transition-controlled semiconductor memory control method was filed in 2026 and examination was requested.

This repository presents a research-oriented description of the technology. The scope of legal protection is determined by the filed patent application and its claims.

---

### One idea to remember

> **Store the state that controls the carrier path, and let that same state participate naturally in computation.**
