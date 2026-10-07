"""
Public reproducibility code for:

J. San Park,
"Data as Waves: A Relational Approach to Semiconductor Process Analysis Using Relative Phase"
(2026).

Purpose
-------
This public package reproduces the analyses and numerical results reported in the manuscript.
It preserves the implemented path from recurrent-structure discovery through overall relative
phase, relational progression, and nested out-of-fold predictive comparison.

Scope
-----
Included:
- data-derived recurrent-period discovery from raw timestamped sensor signals;
- fixed Platen RF Load Power–Pressure relative phase after exploratory selection;
- wafer-position baseline and nested group-level OOF Ridge validation;
- Gas5Flow-aligned cycle-wise relational progression;
- reported progression measures and exploratory Spearman associations;
- manuscript Models A/B/C and inner-fold feature/alpha selection.

Not included because they were not implemented or validated as results in this manuscript:
- automatic sensor-pair discovery/ranking;
- automatic reference-relational-structure generation;
- real-time virtual-metrology deployment;
- prediction-reliability decision logic;
- feedback/feedforward process control or actuator integration.

The code is intended for scientific reproducibility. Relationship change is not treated as an
abnormality criterion, and exploratory p-values are not multiple-comparison corrected.
"""

from pathlib import Path
import re
import argparse
import json
import platform
import sys
from datetime import datetime, timezone
import h5py
import numpy as np
import pandas as pd

from scipy.stats import spearmanr
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler


DATA_DIR = Path(__file__).resolve().parent
PROCESS_FILE = DATA_DIR / "Process_data.nc"
METROLOGY_FILE = DATA_DIR / "Si_Oxide_etch_9_points.csv"
OUTPUT_DIR = DATA_DIR / "outputs"
DISCOVERY_DIR = OUTPUT_DIR / "recurrent_structure_discovery"
PREDICTION_DIR = OUTPUT_DIR / "prediction"
PROGRESSION_DIR = OUTPUT_DIR / "relational_progression"
COMPARISON_DIR = OUTPUT_DIR / "state_progression_comparison"

PERIOD_S = 6.0
F0_HZ = 1.0 / PERIOD_S

# Branch 0 discovery settings.
# The 6 s value above remains the manuscript analysis reference. Branch 0 does
# not use it to locate a peak; it scans a broader period range independently.
DISCOVERY_PERIOD_MIN_S = 2.0
DISCOVERY_PERIOD_MAX_S = 12.0
DISCOVERY_PERIOD_STEP_S = 0.05
DISCOVERY_TOP_K_PER_SIGNAL = 5
DISCOVERY_MIN_VALID_SAMPLES = 100

SENSOR_A = "Stat3_Etch_MV_PlatenRFLoadPower"
SENSOR_B = "Stat3_Etch_MV_Pressure"
CYCLE_SENSOR = "Stat3_Etch_MV_Gas5Flow"

ALPHAS = np.array([0.001, 0.01, 0.1, 1.0, 10.0, 100.0, 1000.0])


ARCHIVE_VERSION = "public-v01"
PAPER_TITLE = (
    "Data as Waves: A Relational Approach to Semiconductor Process Analysis "
    "Using Relative Phase"
)

REQUIRED_METROLOGY_COLUMNS = {
    "experiment_key", "wafer_number", "si_etch"
}


def validate_inputs():
    """Fail early when required files or basic schema elements are missing."""
    missing_files = [
        str(p.name) for p in (PROCESS_FILE, METROLOGY_FILE) if not p.exists()
    ]
    if missing_files:
        raise FileNotFoundError(
            "Required input file(s) not found beside the script: "
            + ", ".join(missing_files)
        )

    metrology_columns = set(pd.read_csv(METROLOGY_FILE, nrows=0).columns)
    missing_columns = sorted(REQUIRED_METROLOGY_COLUMNS - metrology_columns)
    if missing_columns:
        raise ValueError(
            "Metrology file is missing required column(s): "
            + ", ".join(missing_columns)
        )

    with h5py.File(PROCESS_FILE, "r") as h5:
        if len(h5.keys()) == 0:
            raise ValueError("Process_data.nc contains no process groups.")
        common = common_sensor_set(h5)
        required_sensors = [SENSOR_A, SENSOR_B, CYCLE_SENSOR]
        missing_sensors = [s for s in required_sensors if s not in common]
        if missing_sensors:
            raise KeyError(
                "Required sensor(s) are not present in the common sensor set: "
                + ", ".join(missing_sensors)
            )


def write_run_metadata():
    """Record the execution environment without changing analytical results."""
    metadata = {
        "archive_version": ARCHIVE_VERSION,
        "paper_title": PAPER_TITLE,
        "run_utc": datetime.now(timezone.utc).isoformat(),
        "python": sys.version,
        "platform": platform.platform(),
        "period_s": PERIOD_S,
        "frequency_hz": F0_HZ,
        "discovery_period_min_s": DISCOVERY_PERIOD_MIN_S,
        "discovery_period_max_s": DISCOVERY_PERIOD_MAX_S,
        "discovery_period_step_s": DISCOVERY_PERIOD_STEP_S,
        "sensor_a": SENSOR_A,
        "sensor_b": SENSOR_B,
        "cycle_sensor": CYCLE_SENSOR,
        "ridge_alphas": ALPHAS.tolist(),
        "process_file": PROCESS_FILE.name,
        "metrology_file": METROLOGY_FILE.name,
    }
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_DIR / "run_metadata.json", "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)



def decode_strings(values):
    return [
        v.decode("utf-8") if isinstance(v, (bytes, np.bytes_)) else str(v)
        for v in values
    ]


def parse_process_group(group_name):
    """Day_2024_07_02_Wafer_01 -> ('2024-07-02_01', '2024-07-02', 1)."""
    m = re.fullmatch(r"Day_(\d{4})_(\d{2})_(\d{2})_Wafer_(\d{2})", group_name)
    if not m:
        raise ValueError(f"Unexpected process group name: {group_name}")
    year, month, day, wafer = m.groups()
    date = f"{year}-{month}-{day}"
    wafer_number = int(wafer)
    return f"{date}_{wafer_number:02d}", date, wafer_number


def continuous_end_index(times):
    """
    Keep the continuous record before an isolated final timestamp gap.
    The dataset normally samples near 0.2 s. A gap > 5 * median positive dt
    is treated as a discontinuity; the segment before the first such gap is used.
    """
    times = np.asarray(times, dtype=float)
    dt = np.diff(times)
    positive = dt[np.isfinite(dt) & (dt > 0)]
    if len(positive) == 0:
        return len(times)
    median_dt = np.median(positive)
    gap_idx = np.where(dt > 5.0 * median_dt)[0]
    if len(gap_idx) == 0:
        return len(times)
    return int(gap_idx[0] + 1)


def complex_component(times, signal, f0=F0_HZ):
    """Complex Fourier-like component using recorded timestamps."""
    times = np.asarray(times, dtype=float)
    signal = np.asarray(signal, dtype=float)
    mask = np.isfinite(times) & np.isfinite(signal)
    times, signal = times[mask], signal[mask]
    if len(signal) == 0:
        return np.nan + 1j * np.nan
    centered = signal - np.mean(signal)
    return (2.0 / len(centered)) * np.sum(
        centered * np.exp(-2j * np.pi * f0 * times)
    )


def load_metrology():
    df = pd.read_csv(METROLOGY_FILE)
    valid = df["experiment_key"].notna() & df["wafer_number"].notna()
    df = df.loc[valid].copy()

    agg = {
        "wafer_number": ("wafer_number", "first"),
        "n_metrology_points": ("si_etch", "size"),
        "si_etch_mean": ("si_etch", "mean"),
        "si_etch_std": ("si_etch", "std"),
    }
    if "oxide_etch" in df.columns:
        agg["oxide_etch_mean"] = ("oxide_etch", "mean")

    wafer = df.groupby("experiment_key", as_index=False).agg(**agg)
    wafer["wafer_number"] = wafer["wafer_number"].astype(int)
    return wafer


def common_sensor_set(h5):
    sets = []
    for name in h5.keys():
        sets.append(set(decode_strings(h5[name]["feature"][:])))
    return sorted(set.intersection(*sets))


# ---------------------------------------------------------------------
# Branch A: whole-wafer relative-phase prediction
# ---------------------------------------------------------------------

def _frequency_grid_from_periods():
    """Return an ascending frequency grid corresponding to the discovery period scan."""
    periods = np.arange(
        DISCOVERY_PERIOD_MIN_S,
        DISCOVERY_PERIOD_MAX_S + 0.5 * DISCOVERY_PERIOD_STEP_S,
        DISCOVERY_PERIOD_STEP_S,
        dtype=float,
    )
    frequencies = 1.0 / periods
    order = np.argsort(frequencies)
    return periods[order], frequencies[order]


def normalized_complex_power(times, signal, frequencies):
    """
    Compute a variance-normalized complex projection on actual timestamps.

    This is an exploratory recurrent-structure score, not a replacement for a
    full spectral-density estimator. The signal mean is removed first. The
    squared complex projection is normalized by signal energy and sample count,
    so scores from different sensor units can be compared at the evidence level.
    """
    t = np.asarray(times, dtype=float)
    x = np.asarray(signal, dtype=float)

    valid = np.isfinite(t) & np.isfinite(x)
    t = t[valid]
    x = x[valid]
    if len(x) < DISCOVERY_MIN_VALID_SAMPLES:
        return None

    x = x - np.mean(x)
    energy = float(np.sum(x * x))
    if not np.isfinite(energy) or energy <= 0:
        return None

    t = t - t[0]
    scores = np.empty(len(frequencies), dtype=float)

    # Chunking keeps memory bounded for long process records.
    chunk = 64
    for start in range(0, len(frequencies), chunk):
        f = frequencies[start:start + chunk]
        phase = np.exp(-2j * np.pi * f[:, None] * t[None, :])
        z = phase @ x
        scores[start:start + chunk] = (np.abs(z) ** 2) / (energy * len(x))

    return scores


def discover_recurrent_structure():
    """
    Independently scan recurrent periods before applying the fixed 6 s analysis.

    Evidence is accumulated over multiple common sensor channels and process
    groups. No metrology target, RF/Pressure relationship, or recipe period is
    used to choose the discovery peak.

    Outputs:
      - recurrent_period_scores.csv:
          aggregate score and support at every scanned period
      - recurrent_period_top_peaks.csv:
          strongest aggregate local peaks
      - recurrent_period_sensor_support.csv:
          per-sensor support for the aggregate candidate periods
      - recurrent_period_summary.txt:
          concise archival summary

    The approximately 6 s recipe period is compared only after the data-derived
    candidate periods have been ranked.
    """
    DISCOVERY_DIR.mkdir(parents=True, exist_ok=True)
    periods, frequencies = _frequency_grid_from_periods()

    aggregate_sum = np.zeros(len(frequencies), dtype=float)
    aggregate_count = np.zeros(len(frequencies), dtype=int)

    sensor_sum = {}
    sensor_count = {}
    top_hits = []

    with h5py.File(PROCESS_FILE, "r") as h5:
        common = sorted(common_sensor_set(h5))
        if not common:
            raise ValueError("No common sensor channels are available for Branch 0.")

        for group_name in sorted(h5.keys()):
            group = h5[group_name]
            times = np.asarray(group["times"][:], dtype=float)
            names = decode_strings(group["feature"][:])
            data = np.asarray(group["data"][:], dtype=float)
            index = {name: i for i, name in enumerate(names)}

            end = continuous_end_index(times)
            t = times[:end]
            if len(t) < DISCOVERY_MIN_VALID_SAMPLES:
                continue

            # Vectorized frequency projection for all common sensors in this process group.
            present = [sensor for sensor in common if sensor in index]
            if not present:
                continue
            X = np.asarray(data[:end, [index[s] for s in present]], dtype=float)
            finite_rows = np.all(np.isfinite(X), axis=1) & np.isfinite(t)
            tv = t[finite_rows]
            X = X[finite_rows]
            if len(tv) < DISCOVERY_MIN_VALID_SAMPLES:
                continue
            X = X - np.mean(X, axis=0, keepdims=True)
            energy = np.sum(X * X, axis=0)
            valid_sensor = np.isfinite(energy) & (energy > 0)
            if not np.any(valid_sensor):
                continue
            tv = tv - tv[0]
            phase = np.exp(-2j * np.pi * frequencies[:, None] * tv[None, :])
            Z = phase @ X[:, valid_sensor]
            scores_matrix = (np.abs(Z) ** 2) / (energy[valid_sensor][None, :] * len(tv))
            valid_names = [present[i] for i in np.where(valid_sensor)[0]]

            for col, sensor in enumerate(valid_names):
                scores = scores_matrix[:, col]
                finite = np.isfinite(scores)
                aggregate_sum[finite] += scores[finite]
                aggregate_count[finite] += 1

                if sensor not in sensor_sum:
                    sensor_sum[sensor] = np.zeros(len(frequencies), dtype=float)
                    sensor_count[sensor] = np.zeros(len(frequencies), dtype=int)
                sensor_sum[sensor][finite] += scores[finite]
                sensor_count[sensor][finite] += 1

                n_top = min(DISCOVERY_TOP_K_PER_SIGNAL, int(np.sum(finite)))
                if n_top > 0:
                    valid_idx = np.where(finite)[0]
                    strongest = valid_idx[np.argsort(scores[valid_idx])[-n_top:][::-1]]
                    for rank, idx in enumerate(strongest, start=1):
                        top_hits.append({
                            "process_group": group_name,
                            "sensor": sensor,
                            "rank_within_signal": rank,
                            "period_s": float(periods[idx]),
                            "frequency_hz": float(frequencies[idx]),
                            "normalized_power": float(scores[idx]),
                        })

    aggregate_mean = np.divide(
        aggregate_sum,
        aggregate_count,
        out=np.full_like(aggregate_sum, np.nan, dtype=float),
        where=aggregate_count > 0,
    )

    score_df = pd.DataFrame({
        "period_s": periods,
        "frequency_hz": frequencies,
        "mean_normalized_power": aggregate_mean,
        "n_sensor_wafer_signals": aggregate_count,
    }).sort_values("period_s")
    score_df.to_csv(DISCOVERY_DIR / "recurrent_period_scores.csv", index=False)

    hit_df = pd.DataFrame(top_hits)
    hit_df.to_csv(DISCOVERY_DIR / "recurrent_period_signal_top_hits.csv", index=False)

    # Identify aggregate local maxima without using the recipe period.
    finite_score = np.nan_to_num(aggregate_mean, nan=-np.inf)
    peak_idx = []
    for i in range(1, len(finite_score) - 1):
        if finite_score[i] > finite_score[i - 1] and finite_score[i] >= finite_score[i + 1]:
            peak_idx.append(i)
    if not peak_idx and np.any(np.isfinite(aggregate_mean)):
        peak_idx = [int(np.nanargmax(aggregate_mean))]

    ranked = sorted(
        peak_idx,
        key=lambda i: finite_score[i],
        reverse=True,
    )[:20]

    peak_rows = []
    for rank, idx in enumerate(ranked, start=1):
        # Support: how many individual signal top-hit periods fall within one
        # discovery-grid step of this candidate.
        if len(hit_df):
            support_mask = np.abs(hit_df["period_s"] - periods[idx]) <= DISCOVERY_PERIOD_STEP_S
            support_signals = int(support_mask.sum())
            support_sensors = int(hit_df.loc[support_mask, "sensor"].nunique())
            support_groups = int(hit_df.loc[support_mask, "process_group"].nunique())
        else:
            support_signals = support_sensors = support_groups = 0

        peak_rows.append({
            "rank": rank,
            "period_s": float(periods[idx]),
            "frequency_hz": float(frequencies[idx]),
            "mean_normalized_power": float(aggregate_mean[idx]),
            "n_sensor_wafer_signals": int(aggregate_count[idx]),
            "top_hit_support_count": support_signals,
            "supporting_unique_sensors": support_sensors,
            "supporting_process_groups": support_groups,
            "distance_from_recipe_6s_s": float(abs(periods[idx] - PERIOD_S)),
        })

    peak_df = pd.DataFrame(peak_rows)
    peak_df.to_csv(DISCOVERY_DIR / "recurrent_period_top_peaks.csv", index=False)

    # For each aggregate candidate, show which sensors independently support it.
    support_rows = []
    for _, peak in peak_df.iterrows():
        idx = int(np.argmin(np.abs(periods - float(peak["period_s"]))))
        for sensor in sorted(sensor_sum):
            mean_sensor = np.divide(
                sensor_sum[sensor],
                sensor_count[sensor],
                out=np.full_like(sensor_sum[sensor], np.nan, dtype=float),
                where=sensor_count[sensor] > 0,
            )
            support_rows.append({
                "candidate_rank": int(peak["rank"]),
                "candidate_period_s": float(periods[idx]),
                "sensor": sensor,
                "sensor_mean_normalized_power": float(mean_sensor[idx])
                    if np.isfinite(mean_sensor[idx]) else np.nan,
                "n_process_groups": int(sensor_count[sensor][idx]),
            })

    pd.DataFrame(support_rows).to_csv(
        DISCOVERY_DIR / "recurrent_period_sensor_support.csv", index=False
    )

    if len(peak_df):
        best = peak_df.iloc[0]
        closest = peak_df.iloc[
            np.argmin(np.abs(peak_df["period_s"].to_numpy(dtype=float) - PERIOD_S))
        ]
        summary = (
            "Branch 0 — Recurrent-Structure Discovery\n"
            "========================================\n"
            f"Scan range: {DISCOVERY_PERIOD_MIN_S:.2f}–{DISCOVERY_PERIOD_MAX_S:.2f} s\n"
            f"Grid step: {DISCOVERY_PERIOD_STEP_S:.3f} s\n"
            f"Strongest data-derived aggregate candidate: {best['period_s']:.3f} s "
            f"(score={best['mean_normalized_power']:.6g})\n"
            f"Recipe/reference period used later in the manuscript: {PERIOD_S:.3f} s\n"
            f"Ranked candidate nearest 6 s: {closest['period_s']:.3f} s "
            f"(rank={int(closest['rank'])}, "
            f"distance={closest['distance_from_recipe_6s_s']:.3f} s)\n\n"
            "Interpretation rule:\n"
            "The discovery ranking is data-derived. The 6 s recipe period is used "
            "only for post-discovery comparison and for the manuscript analyses "
            "that follow.\n"
        )
    else:
        summary = (
            "Branch 0 — Recurrent-Structure Discovery\n"
            "No valid aggregate recurrent-period candidate was found.\n"
        )

    (DISCOVERY_DIR / "recurrent_period_summary.txt").write_text(
        summary, encoding="utf-8"
    )

    return score_df, peak_df



def extract_process_features():
    rows = []
    with h5py.File(PROCESS_FILE, "r") as h5:
        common = common_sensor_set(h5)
        if SENSOR_A not in common or SENSOR_B not in common:
            raise KeyError("Required fixed sensor pair is not in the common sensor set.")

        for group_name in sorted(h5.keys()):
            exp_key, date_group, wafer_number = parse_process_group(group_name)
            g = h5[group_name]

            features = decode_strings(g["feature"][:])
            index = {name: i for i, name in enumerate(features)}
            times = np.asarray(g["times"][:], dtype=float)
            data = np.asarray(g["data"][:], dtype=float)

            end = continuous_end_index(times)
            t = times[:end]

            za = complex_component(t, data[:end, index[SENSOR_A]])
            zb = complex_component(t, data[:end, index[SENSOR_B]])

            theta_a = np.angle(za)
            theta_b = np.angle(zb)
            dtheta = np.angle(np.exp(1j * (theta_a - theta_b)))

            rows.append({
                "experiment_key": exp_key,
                "date_group": date_group,
                "wafer_number": wafer_number,
                "n_samples_used": end,
                "amplitude_rf": abs(za),
                "amplitude_pressure": abs(zb),
                "phase_rf": theta_a,
                "phase_pressure": theta_b,
                "delta_phase": dtheta,
                "cos_delta_phase": np.cos(dtheta),
                "sin_delta_phase": np.sin(dtheta),
                "interference_term": 2.0 * abs(za) * abs(zb) * np.cos(dtheta),
            })

    return pd.DataFrame(rows), common


def position_baseline(train, test, target="si_etch_mean"):
    means = train.groupby("wafer_number")[target].mean()
    return test["wafer_number"].map(means).to_numpy(dtype=float)


def make_xy(train, baseline):
    X = train[["cos_delta_phase", "sin_delta_phase"]].to_numpy(dtype=float)
    residual = train["si_etch_mean"].to_numpy(dtype=float) - baseline
    return X, residual


def choose_alpha_inner(train):
    groups = sorted(train["date_group"].unique())
    scores = []

    for alpha in ALPHAS:
        pred_all, true_all = [], []

        for held_group in groups:
            inner_train = train[train["date_group"] != held_group].copy()
            inner_valid = train[train["date_group"] == held_group].copy()

            b_train = position_baseline(inner_train, inner_train)
            b_valid = position_baseline(inner_train, inner_valid)

            X_train, y_resid = make_xy(inner_train, b_train)
            X_valid = inner_valid[
                ["cos_delta_phase", "sin_delta_phase"]
            ].to_numpy(dtype=float)

            scaler = StandardScaler().fit(X_train)
            model = Ridge(alpha=alpha)
            model.fit(scaler.transform(X_train), y_resid)

            pred = b_valid + model.predict(scaler.transform(X_valid))
            pred_all.extend(pred)
            true_all.extend(inner_valid["si_etch_mean"].to_numpy(dtype=float))

        scores.append((alpha, mean_squared_error(true_all, pred_all)))

    scores.sort(key=lambda x: (x[1], x[0]))
    return scores[0][0], scores


def run_nested_oof(df):
    predictions = []
    fold_rows = []

    for outer_group in sorted(df["date_group"].unique()):
        train = df[df["date_group"] != outer_group].copy()
        test = df[df["date_group"] == outer_group].copy()

        alpha, _ = choose_alpha_inner(train)

        b_train = position_baseline(train, train)
        b_test = position_baseline(train, test)

        X_train, y_resid = make_xy(train, b_train)
        X_test = test[["cos_delta_phase", "sin_delta_phase"]].to_numpy(dtype=float)

        scaler = StandardScaler().fit(X_train)
        model = Ridge(alpha=alpha)
        model.fit(scaler.transform(X_train), y_resid)

        pred = b_test + model.predict(scaler.transform(X_test))

        fold = test[
            ["experiment_key", "date_group", "wafer_number", "si_etch_mean"]
        ].copy()
        fold["baseline_prediction"] = b_test
        fold["prediction"] = pred
        fold["alpha"] = alpha
        predictions.append(fold)

        fold_rows.append({
            "held_out_group": outer_group,
            "n_test": len(test),
            "alpha": alpha,
            "MAE": mean_absolute_error(test["si_etch_mean"], pred),
            "RMSE": np.sqrt(mean_squared_error(test["si_etch_mean"], pred)),
            "R2": r2_score(test["si_etch_mean"], pred) if len(test) > 1 else np.nan,
        })

    pred_df = pd.concat(predictions, ignore_index=True).sort_values(
        ["date_group", "wafer_number"]
    )
    fold_df = pd.DataFrame(fold_rows)

    y = pred_df["si_etch_mean"].to_numpy()
    baseline = pred_df["baseline_prediction"].to_numpy()
    pred = pred_df["prediction"].to_numpy()

    metrics = {
        "n_wafers": len(pred_df),
        "baseline_MAE": mean_absolute_error(y, baseline),
        "baseline_RMSE": np.sqrt(mean_squared_error(y, baseline)),
        "baseline_R2": r2_score(y, baseline),
        "model_MAE": mean_absolute_error(y, pred),
        "model_RMSE": np.sqrt(mean_squared_error(y, pred)),
        "model_R2": r2_score(y, pred),
    }
    return pred_df, fold_df, metrics


# ---------------------------------------------------------------------
# Branch B: cycle-wise relational progression
# ---------------------------------------------------------------------

def longest_regular_edge_sequence(edges, min_gap_samples=25, max_gap_samples=35):
    """
    Keep the longest rising-edge sequence with ~5–7 s spacing at ~5 Hz.
    This is a follow-up alignment rule for progression analysis.
    """
    edges = np.asarray(edges, dtype=int)
    if len(edges) < 2:
        return edges

    best = []
    current = [int(edges[0])]

    for a, b in zip(edges[:-1], edges[1:]):
        gap = int(b - a)
        if min_gap_samples <= gap <= max_gap_samples:
            current.append(int(b))
        else:
            if len(current) > len(best):
                best = current
            current = [int(b)]

    if len(current) > len(best):
        best = current
    return np.asarray(best, dtype=int)


def detect_bosch_cycle_edges(gas_signal):
    """
    Detect Gas5Flow rising transitions.
    Threshold is the midpoint of the 10th and 90th percentiles.
    """
    gas = np.asarray(gas_signal, dtype=float)
    lo, hi = np.nanpercentile(gas, [10, 90])
    threshold = (lo + hi) / 2.0
    high = gas >= threshold
    edges = np.where((~high[:-1]) & high[1:])[0] + 1
    return longest_regular_edge_sequence(edges)


def cycle_relative_phases(times, rf, pressure, edges):
    rows = []
    for cycle_index, (start, stop) in enumerate(zip(edges[:-1], edges[1:]), start=1):
        if stop - start < 10:
            continue

        t = times[start:stop]
        za = complex_component(t, rf[start:stop])
        zb = complex_component(t, pressure[start:stop])

        if not np.isfinite(za.real) or not np.isfinite(zb.real):
            continue

        dtheta = np.angle(za * np.conj(zb))
        rows.append({
            "cycle_index": cycle_index,
            "start_time": float(t[0]),
            "end_time": float(t[-1]),
            "delta_phase": float(dtheta),
            "cos_delta_phase": float(np.cos(dtheta)),
            "sin_delta_phase": float(np.sin(dtheta)),
            "amplitude_rf": float(abs(za)),
            "amplitude_pressure": float(abs(zb)),
        })
    return pd.DataFrame(rows)


def progression_summary(cycles):
    """
    Circular/geometric summaries of z_k = exp(i*delta_phase_k).
    No custom anomaly score is introduced.
    """
    if len(cycles) < 4:
        return {
            "n_cycles": len(cycles),
            "direction_continuity": np.nan,
            "total_path": np.nan,
            "net_displacement": np.nan,
            "circular_variance": np.nan,
            "early_late_displacement": np.nan,
        }

    phi = cycles["delta_phase"].to_numpy(dtype=float)
    z = np.exp(1j * phi)
    dz = np.diff(z)

    a = dz[:-1]
    b = dz[1:]
    denom = np.abs(a) * np.abs(b)
    valid = denom > 1e-12
    if np.any(valid):
        direction = np.mean(
            np.real(a[valid] * np.conj(b[valid])) / denom[valid]
        )
    else:
        direction = np.nan

    q = max(1, len(z) // 4)
    early = np.mean(z[:q])
    late = np.mean(z[-q:])

    return {
        "n_cycles": len(cycles),
        "direction_continuity": float(direction),
        "total_path": float(np.sum(np.abs(dz))),
        "net_displacement": float(abs(z[-1] - z[0])),
        "circular_variance": float(1.0 - abs(np.mean(z))),
        "early_late_displacement": float(abs(late - early)),
    }


def extract_relational_progression():
    wafer_rows = []
    cycle_tables = []

    with h5py.File(PROCESS_FILE, "r") as h5:
        common = common_sensor_set(h5)
        required = [SENSOR_A, SENSOR_B, CYCLE_SENSOR]
        missing = [x for x in required if x not in common]
        if missing:
            raise KeyError(f"Required progression sensors missing: {missing}")

        for group_name in sorted(h5.keys()):
            exp_key, date_group, wafer_number = parse_process_group(group_name)
            g = h5[group_name]

            features = decode_strings(g["feature"][:])
            index = {name: i for i, name in enumerate(features)}
            times = np.asarray(g["times"][:], dtype=float)
            data = np.asarray(g["data"][:], dtype=float)

            end = continuous_end_index(times)
            t = times[:end]
            rf = data[:end, index[SENSOR_A]]
            pressure = data[:end, index[SENSOR_B]]
            gas = data[:end, index[CYCLE_SENSOR]]

            edges = detect_bosch_cycle_edges(gas)
            cycles = cycle_relative_phases(t, rf, pressure, edges)

            if len(cycles):
                cycles.insert(0, "experiment_key", exp_key)
                cycles.insert(1, "date_group", date_group)
                cycles.insert(2, "wafer_number", wafer_number)
                cycle_tables.append(cycles)

            wafer_rows.append({
                "experiment_key": exp_key,
                "date_group": date_group,
                "wafer_number": wafer_number,
                **progression_summary(cycles),
            })

    cycle_df = (
        pd.concat(cycle_tables, ignore_index=True)
        if cycle_tables else pd.DataFrame()
    )
    return pd.DataFrame(wafer_rows), cycle_df


def oof_position_baseline(df, target):
    """
    Leave-one-date-group-out baseline at the same wafer processing position.
    """
    prediction = np.full(len(df), np.nan, dtype=float)
    groups = df["date_group"].astype(str)

    for held_group in sorted(groups.unique()):
        test_mask = groups == held_group
        train_mask = ~test_mask

        means = (
            df.loc[train_mask]
            .groupby("wafer_number")[target]
            .mean()
        )
        prediction[test_mask] = (
            df.loc[test_mask, "wafer_number"]
            .map(means)
            .to_numpy(dtype=float)
        )

    return prediction


def progression_associations(df, target_deviation):
    features = [
        "direction_continuity",
        "total_path",
        "net_displacement",
        "circular_variance",
        "early_late_displacement",
    ]

    rows = []
    for feature in features:
        x = df[feature].to_numpy(dtype=float)
        y = df[target_deviation].to_numpy(dtype=float)
        valid = np.isfinite(x) & np.isfinite(y)

        if np.sum(valid) < 5:
            rho, p = np.nan, np.nan
        else:
            rho, p = spearmanr(x[valid], y[valid])

        rows.append({
            "feature": feature,
            "target": target_deviation,
            "n": int(np.sum(valid)),
            "spearman_rho": rho,
            "p_value_uncorrected": p,
        })

    return pd.DataFrame(rows)


def run_progression_analysis(metrology):
    progression, cycles = extract_relational_progression()
    df = progression.merge(
        metrology,
        on=["experiment_key", "wafer_number"],
        how="inner"
    ).sort_values(["date_group", "wafer_number"]).reset_index(drop=True)

    df["si_baseline_oof"] = oof_position_baseline(df, "si_etch_mean")
    df["si_abs_baseline_deviation"] = np.abs(
        df["si_etch_mean"] - df["si_baseline_oof"]
    )

    tables = [
        progression_associations(df, "si_abs_baseline_deviation")
    ]

    if "oxide_etch_mean" in df.columns:
        df["oxide_baseline_oof"] = oof_position_baseline(
            df, "oxide_etch_mean"
        )
        df["oxide_abs_baseline_deviation"] = np.abs(
            df["oxide_etch_mean"] - df["oxide_baseline_oof"]
        )
        tables.append(
            progression_associations(df, "oxide_abs_baseline_deviation")
        )

    associations = pd.concat(tables, ignore_index=True)
    return df, cycles, associations



# ---------------------------------------------------------------------
# Branch C: nested OOF comparison of state and progression information
# ---------------------------------------------------------------------

PROGRESSION_FEATURES = [
    "direction_continuity", "total_path", "net_displacement",
    "circular_variance", "early_late_displacement"
]
PHASE_FEATURES = ["cos_delta_phase", "sin_delta_phase"]

def fit_predict_feature_set(train, test, features, alpha):
    b_train = position_baseline(train, train)
    b_test = position_baseline(train, test)
    X_train = train[features].to_numpy(dtype=float)
    y_resid = train["si_etch_mean"].to_numpy(dtype=float) - b_train
    X_test = test[features].to_numpy(dtype=float)
    scaler = StandardScaler().fit(X_train)
    model = Ridge(alpha=alpha).fit(scaler.transform(X_train), y_resid)
    return b_test + model.predict(scaler.transform(X_test))

def select_feature_set_inner(train, feature_sets):
    best = None
    for features in feature_sets:
        for alpha in ALPHAS:
            y_true, y_pred = [], []
            for held_group in sorted(train["date_group"].unique()):
                inner_train = train[train["date_group"] != held_group].copy()
                inner_valid = train[train["date_group"] == held_group].copy()
                pred = fit_predict_feature_set(inner_train, inner_valid, features, alpha)
                y_true.extend(inner_valid["si_etch_mean"].to_numpy(dtype=float))
                y_pred.extend(pred)
            mse = mean_squared_error(y_true, y_pred)
            key = (mse, len(features), alpha, ",".join(features))
            if best is None or key < best[0]:
                best = (key, list(features), alpha)
    return best[1], best[2]

def run_state_progression_comparison(prediction_input, progression_df):
    d = prediction_input.merge(
        progression_df[["experiment_key", "date_group", "wafer_number"] + PROGRESSION_FEATURES],
        on=["experiment_key", "date_group", "wafer_number"], how="inner"
    ).sort_values(["date_group", "wafer_number"]).reset_index(drop=True)

    candidates = {
        "A_phase": [PHASE_FEATURES],
        "B_progression": [[f] for f in PROGRESSION_FEATURES] + [PROGRESSION_FEATURES],
        "C_combined": [PHASE_FEATURES + [f] for f in PROGRESSION_FEATURES] + [PHASE_FEATURES + PROGRESSION_FEATURES],
    }

    metric_rows, selection_rows, prediction_rows = [], [], []
    for model_name, feature_sets in candidates.items():
        all_true, all_pred = [], []
        for held_group in sorted(d["date_group"].unique()):
            train = d[d["date_group"] != held_group].copy()
            test = d[d["date_group"] == held_group].copy()
            features, alpha = select_feature_set_inner(train, feature_sets)
            pred = fit_predict_feature_set(train, test, features, alpha)
            all_true.extend(test["si_etch_mean"].to_numpy(dtype=float))
            all_pred.extend(pred)
            selection_rows.append({
                "model": model_name, "held_out_group": held_group,
                "features": "+".join(features), "alpha": alpha
            })
            for (_, row), pv in zip(test.iterrows(), pred):
                prediction_rows.append({
                    "model": model_name, "experiment_key": row["experiment_key"],
                    "date_group": row["date_group"], "wafer_number": row["wafer_number"],
                    "si_etch_mean": row["si_etch_mean"], "prediction": pv
                })
        all_true, all_pred = np.asarray(all_true), np.asarray(all_pred)
        metric_rows.append({
            "model": model_name,
            "MAE": mean_absolute_error(all_true, all_pred),
            "RMSE": np.sqrt(mean_squared_error(all_true, all_pred)),
            "R2": r2_score(all_true, all_pred),
        })
    return pd.DataFrame(metric_rows), pd.DataFrame(selection_rows), pd.DataFrame(prediction_rows)


def parse_args():
    parser = argparse.ArgumentParser(
        description=(
            "Reproduce the manuscript analyses for 'Data as Waves: "
            "A Relational Approach to Semiconductor Process Analysis Using Relative Phase'."
        )
    )
    parser.add_argument(
        "--process-data",
        default=str(PROCESS_FILE),
        help="Path to Process_data.nc",
    )
    parser.add_argument(
        "--metrology",
        default=str(METROLOGY_FILE),
        help="Path to Si_Oxide_etch_9_points.csv",
    )
    parser.add_argument(
        "--output-dir",
        default=str(OUTPUT_DIR),
        help="Directory for generated tables, figures, and metadata",
    )
    return parser.parse_args()


def configure_paths(args):
    global PROCESS_FILE, METROLOGY_FILE, OUTPUT_DIR, DISCOVERY_DIR
    PROCESS_FILE = Path(args.process_data)
    METROLOGY_FILE = Path(args.metrology)
    OUTPUT_DIR = Path(args.output_dir)
    DISCOVERY_DIR = OUTPUT_DIR / "recurrent_structure_discovery"



def main():
    args = parse_args()
    configure_paths(args)
    validate_inputs()
    PREDICTION_DIR.mkdir(parents=True, exist_ok=True)
    PROGRESSION_DIR.mkdir(parents=True, exist_ok=True)
    COMPARISON_DIR.mkdir(parents=True, exist_ok=True)
    write_run_metadata()

    print("Branch 0: discovering recurrent temporal structure from raw sensor data...")
    discovery_scores, discovery_peaks = discover_recurrent_structure()
    if len(discovery_peaks):
        print(
            "  strongest data-derived recurrent-period candidate: "
            f"{discovery_peaks.iloc[0]['period_s']:.3f} s"
        )

    metrology = load_metrology()

    # Branch A
    process, common = extract_process_features()
    prediction_input = process.merge(
        metrology,
        on=["experiment_key", "wafer_number"],
        how="inner"
    ).sort_values(["date_group", "wafer_number"]).reset_index(drop=True)

    pred_df, fold_df, metrics = run_nested_oof(prediction_input)

    pd.DataFrame({"sensor": common}).to_csv(
        PREDICTION_DIR / "common_sensor_channels.csv", index=False
    )
    prediction_input.to_csv(
        PREDICTION_DIR / "matched_wafer_features.csv", index=False
    )
    pred_df.to_csv(PREDICTION_DIR / "oof_predictions.csv", index=False)
    fold_df.to_csv(PREDICTION_DIR / "fold_metrics.csv", index=False)
    pd.DataFrame([metrics]).to_csv(
        PREDICTION_DIR / "overall_metrics.csv", index=False
    )

    # Branch B
    progression_df, cycles_df, assoc_df = run_progression_analysis(metrology)
    progression_df.to_csv(
        PROGRESSION_DIR / "wafer_progression_features.csv", index=False
    )
    cycles_df.to_csv(
        PROGRESSION_DIR / "cycle_relative_phase.csv", index=False
    )
    assoc_df.to_csv(
        PROGRESSION_DIR / "association_results.csv", index=False
    )

    # Branch C: nested OOF state/progression comparison
    comparison_metrics, comparison_selections, comparison_predictions = \
        run_state_progression_comparison(prediction_input, progression_df)
    comparison_metrics.to_csv(COMPARISON_DIR / "comparison_metrics.csv", index=False)
    comparison_selections.to_csv(COMPARISON_DIR / "feature_selections_by_fold.csv", index=False)
    comparison_predictions.to_csv(COMPARISON_DIR / "oof_predictions.csv", index=False)

    print("=== Branch A: Prediction ===")
    print(f"Process records: {len(process)}")
    print(f"Common sensors: {len(common)}")
    print(f"Matched wafers: {len(prediction_input)}")
    print(f"Conditioning/date groups: {prediction_input['date_group'].nunique()}")
    print()
    print("Wafer-position baseline")
    print(f"  MAE : {metrics['baseline_MAE']:.4f}")
    print(f"  RMSE: {metrics['baseline_RMSE']:.4f}")
    print(f"  R2  : {metrics['baseline_R2']:.3f}")
    print()
    print("Baseline + RF-Power/Pressure relative phase")
    print(f"  MAE : {metrics['model_MAE']:.4f}")
    print(f"  RMSE: {metrics['model_RMSE']:.4f}")
    print(f"  R2  : {metrics['model_R2']:.3f}")

    print()
    print("=== Branch B: Relational Progression ===")
    print(f"Matched wafers: {len(progression_df)}")
    print(f"Median extracted cycles: {progression_df['n_cycles'].median():.1f}")
    print()
    print("Exploratory associations (uncorrected p-values)")
    print(assoc_df.to_string(index=False))
    print()
    print("=== Branch C: State + Progression Prediction Comparison ===")
    print(comparison_metrics.to_string(index=False))
    print()
    print("Selected features by outer fold:")
    print(comparison_selections.to_string(index=False))
    print()
    print(f"Outputs written to: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
