# AHG Zeta-Pell Autonomous Lattice

## Overview

Experimental control-plane simulation combining PID control, Savitzky-Golay filtering, Kalman estimation/reset behavior, and a silver-ratio/Pell-derived timing anchor. The repository is **not currently production-certified**; benchmark claims are tracked by evidence level in [`docs/AUDIT_PASS_1.md`](docs/AUDIT_PASS_1.md).

## Evidence Status

The current repository contains historical benchmark assertions including PAR 88.1%, a 2-cycle recovery claim, peak entropy 0.8616, and a 200x jitter-resilience claim. These are **not all independently reproducible from the current README or sampled source cells**. In particular, the jitter multiplier lacks a defined 1x baseline, and the 2-cycle recovery result requires a closed trace from the intermediate 4-cycle retest to the final 2-cycle claim.

Treat these values as historical/experimental until the source telemetry and derivations are recomputed.

## Core Experimental Components

1. **PID-based control:** continuous modulation and flicker mitigation.
2. **Savitzky-Golay filtering:** signal smoothing; latency/zero-lag claims require measurement-specific qualification.
3. **Kalman estimation/reset:** covariance-state estimation and recovery behavior.
4. **Silver Ratio / Pell anchor:** deterministic timing reference based on the standard identity `1 + sqrt(2)` as the limiting Pell-ratio constant.

## Audit Boundary

AHG Zeta-Pell is a separate track from PDMAL. Similar uses of mathematical constants or convergence timing do not establish a shared architecture or mathematical dependency.

See [`docs/AUDIT_PASS_1.md`](docs/AUDIT_PASS_1.md) for the current Fact-Fiction Ledger, including unsupported precision, misleading mathematical terminology, traceability gaps, and the unaudited notebook sections.
