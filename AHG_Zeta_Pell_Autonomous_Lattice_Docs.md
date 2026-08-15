# AHG Zeta-Pell Autonomous Lattice: Technical Documentation

## Evidence Status

This document is a **current-state technical summary**, not a certification. Claims inherited from the historical Colab notebooks are retained only where their evidence status is explicit. The notebooks' unaudited cells are not present in this repository, so this repository cannot independently reproduce Pass 2 claims from those cells.

## 1. Executive Summary

The AHG Zeta-Pell Autonomous Lattice is a Kalman-filter / rule-based control simulation using the Silver Ratio ($\\delta_S = 1 + \\sqrt{2}$) as a deterministic timing parameter. It is a separate track from PDMAL and does not currently implement PDMAL's dodecahedral topology.

**Evidence classification:** experimental engineering system; not production-certified by this document.

## 2. Historical Performance Claims

The following figures were reported by the historical notebook work, but are **not independently certified by this repository**:

* **Packet Acceptance Rate (PAR): 88.1%** — historical benchmark; recomputation from source telemetry required.
* **Recovery: 2 cycles** — historical result; the sampled audit established an earlier 7-cycle failure and a 4-cycle retest, but the complete 4→2 derivation was not established from the sampled cells.
* **Peak entropy: 0.8616** — historical benchmark; source computation not reproduced here.
* **150x / 180x / 200x jitter resilience** — **unsupported as ratios** until a defined 1x baseline and reproducible measurement protocol are supplied.

These figures must not be presented as independently verified production benchmarks until the underlying experiment is reproduced.

## 3. Core Architectural Pillars

* **PID-based control:** continuous modulation for recovery and stabilization.
* **Savitzky-Golay filtering:** smoothing of entropy/control signals. The historical documentation's stronger "zero-lag" wording is not treated as established without a latency analysis.
* **Aggressive Kalman resets:** covariance re-initialization used to reduce estimator inertia.
* **Silver Ratio parameterization:** $\\delta_S = 1 + \\sqrt{2} \\approx 2.414$ is mathematically verified as the Silver Ratio. Its use as a timing parameter is an engineering design choice, not a theorem that proves optimality.

## 4. Mathematical / Terminology Boundary

### Canonical acronym

**AHG = Adaptive Harmonic Governance.** Historical conflicting expansions, including "Adaptive Hierarchical Governance," are retained only as historical audit findings and are not current definitions.

### Silver Ratio

The identity $1 + \\sqrt{2}$ and its relationship to Pell-number ratios are standard mathematics. That fact does **not** by itself prove that the Silver Ratio minimizes spectral overlap, guarantees stability, or causes an observed entropy reduction. Such claims require derivation or experiment.

### Hecke Operator terminology

Historical notebook cells labeled the spatial admission test a **"Hecke Operator simulation."** The inspected implementation is a stochastic threshold/admission test, not an implementation or approximation of a Hecke operator on modular-form spaces. The label should therefore not be used in current technical documentation unless a genuine operator construction is added.

### Jitter multipliers

"150x", "180x", and "200x" are not accepted as quantitative resilience ratios without a defined baseline, units, experimental protocol, and reproducible calculation. A statement such as "effective at a jitter magnitude of X under configuration Y" is preferable when X is directly measured.

### 12x multiplier

The arithmetic $0.15 \\times 6.0 \\times 12.0 = 10.80$ is correct. The factor 12 was characterized in the audit as an engineering margin rather than a mathematically derived bound. It must not be formatted as a theorem or stability proof without an actual derivation.

## 5. Strategic Justification / RoC

Historical claims including:

* **RoC Score: 5.68**
* **14.21x Starlink Proxy comparison**
* **Instruction Density Tax: 1.29x / 1,550 cycles**
* **7.5x recovery comparison**
* **2x industry jitter comparison**

are treated as **unreproduced historical assertions** unless the source datasets, calculation cells, definitions, and comparison methodology are supplied. They are not current verified benchmarks.

## 6. Audit Status

### Pass 1 — completed

The sampled audit identified:

- historical AHG acronym inconsistency; **current canonical expansion is Adaptive Harmonic Governance**;
- qualitative naming judgments expressed as unsupported percentages;
- misleading Hecke-operator terminology;
- unsupported jitter multipliers;
- reverse-engineered 12x safety margin presented too strongly;
- Silver Ratio premise correctly stated but unrelated stability conclusions overstated;
- historical benchmark dictionaries asserted rather than recomputed in place;
- traceability gap around the 4→2 recovery claim.

### Pass 2 — scope limitation

The proposed Pass 2 targets notebook cells **534–582** (chaos/FML mitigation) and **797–851** (Three-Regime Governor), plus the generated documentation. Those notebook cells are **not currently stored in this repository**, so they cannot be independently audited from GitHub alone.

Accordingly, Pass 2 is recorded as **PENDING SOURCE ACQUISITION**, not as a completed audit.

## 7. Canonical Evidence Rule

A number is not a verified benchmark merely because it appears in a benchmark dictionary, README, generated document, or assertion. Current acceptance requires a traceable path:

`source telemetry → calculation → reproducible test → reported result`

Historical results may remain in the record, but they must retain their historical/unreproduced status until that chain is demonstrated.

## 8. Relationship to PDMAL

AHG Zeta-Pell and PDMAL are separate tracks. The current evidence shows no direct PDMAL references in the audited Zeta-Pell artifacts. Similar use of mathematical constants as convergence/timing parameters is not evidence of architectural identity. Any future bridge between the systems must be explicitly designed and documented.

---

**Canonical status:** Experimental / audited for epistemic hygiene; not production-certified.
