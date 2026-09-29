"""Lorenz transition precursor experiment.

Exploratory code from the HeyJin Theory research program.
It tests whether second-order change can precede Lorenz wing transitions.

This is NOT an AI-safety guarantee or a universal stability detector.
"""

import numpy as np
from scipy.integrate import solve_ivp

SIGMA = 10.0
BETA = 8.0 / 3.0
RHO = 28.0
DT = 0.002
BURN = 20.0
T = 300.0


def lorenz(_t, s):
    x, y, z = s
    return np.array([
        SIGMA * (y - x),
        x * (RHO - z) - y,
        x * y - BETA * z,
    ])


def jacobian(s):
    x, y, z = s
    return np.array([
        [-SIGMA, SIGMA, 0.0],
        [RHO - z, -1.0, -x],
        [y, x, -BETA],
    ])


def wing_transitions(states):
    x = states[:, 0]
    sign = np.sign(x)
    sign[sign == 0] = 1
    candidates = np.where(sign[1:] != sign[:-1])[0] + 1
    sep = int(0.5 / DT)
    events = []
    for i in candidates:
        if i < sep or i + sep >= len(x):
            continue
        left = np.median(x[i-sep:i])
        right = np.median(x[i:i+sep])
        if left * right < 0 and abs(left) > 2 and abs(right) > 2:
            if not events or i - events[-1] > sep:
                events.append(i)
    return np.asarray(events, dtype=int)


def robust_stats(a, excluded):
    b = a[~excluded]
    med = np.median(b)
    scale = 1.4826 * np.median(np.abs(b - med))
    return med, max(scale, 1e-9)


def alarm_starts(zscore, threshold=4.0, sustain_seconds=0.05):
    n = int(sustain_seconds / DT)
    above = zscore > threshold
    run = np.convolve(above.astype(int), np.ones(n, dtype=int), "same") >= n
    return np.where(run & ~np.r_[False, run[:-1]])[0]


def evaluate(zscore, events, horizon_seconds=0.75):
    horizon = int(horizon_seconds / DT)
    alarms = alarm_starts(zscore)
    leads = []
    for event in events:
        candidates = alarms[(alarms >= event-horizon) & (alarms < event)]
        if len(candidates):
            leads.append((event-candidates[-1]) * DT)
    useful = sum(np.any((events > a) & (events <= a+horizon)) for a in alarms)
    return {
        "recall": len(leads) / len(events),
        "useful_alarm_fraction": useful / max(len(alarms), 1),
        "median_lead_s": float(np.median(leads)) if leads else np.nan,
        "alarms": len(alarms),
    }


def main():
    t = np.arange(0, T + DT/2, DT)
    sol = solve_ivp(lorenz, [0, T], [1, 1, 1], t_eval=t,
                    rtol=1e-10, atol=1e-12)
    states = sol.y.T[t >= BURN]
    split = len(states) // 2
    train, test = states[:split], states[split:]

    def derivatives(s):
        velocity = np.array([lorenz(0, q) for q in s])
        acceleration = np.array([jacobian(q) @ v for q, v in zip(s, velocity)])
        return velocity, acceleration

    v_train, a_train = derivatives(train)
    v_test, a_test = derivatives(test)
    train_events = wing_transitions(train)
    test_events = wing_transitions(test)

    excluded = np.zeros(len(train), dtype=bool)
    for i in train_events:
        excluded[max(0, i-int(1/DT)):min(len(train), i+int(0.3/DT))] = True

    signals_train = {
        "x": train[:, 0], "y": train[:, 1], "z": train[:, 2],
        "xdot": v_train[:, 0], "ydot": v_train[:, 1], "zdot": v_train[:, 2],
        "xddot": a_train[:, 0], "yddot": a_train[:, 1], "zddot": a_train[:, 2],
    }
    signals_test = {
        "x": test[:, 0], "y": test[:, 1], "z": test[:, 2],
        "xdot": v_test[:, 0], "ydot": v_test[:, 1], "zdot": v_test[:, 2],
        "xddot": a_test[:, 0], "yddot": a_test[:, 1], "zddot": a_test[:, 2],
    }

    print(f"test wing transitions: {len(test_events)}")
    print("signal   recall   useful/alarm   median lead(s)   alarms")
    for name in signals_train:
        med, scale = robust_stats(signals_train[name], excluded)
        zscore = np.abs(signals_test[name] - med) / scale
        r = evaluate(zscore, test_events)
        print(f"{name:6s}   {r['recall']:.3f}       "
              f"{r['useful_alarm_fraction']:.3f}          "
              f"{r['median_lead_s']:.3f}          {r['alarms']}")


if __name__ == "__main__":
    main()
