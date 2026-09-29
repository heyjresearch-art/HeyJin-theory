# Dynamic Response and Transition Precursors

This folder contains a small reproducible experiment motivated by a broader question:

> Can a dynamical system be monitored through its response to change rather than only through fixed state thresholds?

The experiment uses the standard Lorenz system as an established nonlinear test case. It compares the original state variables, their first derivatives, and their second derivatives before transitions between the two Lorenz wings.

## Current observation

In the tested trajectory at `rho = 28`, second-order signals such as `yddot` and `zddot` carried substantially stronger pre-transition information than the raw state values under the same simple detector.

This repository does **not** claim that second derivatives are a universal instability detector, that the Lorenz result generalizes to AI systems, or that this constitutes an AI-safety mechanism.

The present research position is narrower:

**State-transition information may become visible in dynamic response before it becomes visible in the state value itself.**

## Reproduce

Requirements:

- Python 3
- NumPy
- SciPy

Run:

`python lorenz_second_order_transition.py`

The script performs a continuous Lorenz simulation, splits the post-burn trajectory into training and test halves, learns normal robust statistics only from the training half, and evaluates the same detector on the unused test half.

Detector used in this exploratory reproduction:

- deviation > 4 training robust standard deviations
- sustained for 50 ms
- a transition is associated with an alarm when it follows within 0.75 s

These values are analysis settings, not physical constants or proposed safety thresholds.

## Why the code is public

The code is published so that the numerical observation can be reproduced, challenged, and compared with standard dynamical-systems methods. The exploratory reasoning path that led to this experiment is maintained separately in the private research archive.

## Next question

Why do second-order changes in the Lorenz dynamics become strong before wing transitions, and how much of this behavior is already explained by established nonlinear dynamics and stability theory?
