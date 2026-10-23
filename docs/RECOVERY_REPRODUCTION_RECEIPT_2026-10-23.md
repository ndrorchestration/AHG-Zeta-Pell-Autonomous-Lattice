# Read-only reproduction receipt — 2026-10-23

## Outcome

**Locally reproduced from historical notebook source: seeded 4-cycle refactored recovery.** This is an operator-local execution, not independent validation, not a release result, and not the later 2-cycle recovery claim.

- Source: [private original Colab notebook](https://colab.research.google.com/drive/1_FQQdX0aP6jhdA3ANJpg8Wk9_N85ilcu), retrieved SHA-256 `abf7409fed35abb762f9962cee272d74ec2d658c034f9674e7e3cf6e0b3ebbf1`.
- Local run: executed original zero-indexed code cells **244, 246, 248** sequentially in a fresh Python process with dependencies provided by the cells; no source edits or monkeypatches.
- Original notebook seed: **42** for both NumPy and Python `random`; 50 simulation cycles, stress cycles 15–20 inclusive.
- Observed cycle 20 `TRIBUNAL`, score **0.656000**; cycle 21 `TRIBUNAL` **0.110400**; cycle 22 `TRIBUNAL` **0.092904**; cycle 23 `TRIBUNAL` **0.074129**; cycle 24 `COLLABORATOR` **0.016459**; cycle 25 `COLLABORATOR` **0.094903**.
- Calculation cell 248 returns `recovery_cycle=24`, `new_recovery_delta=24-20=4`, benchmark <=4 met. Its printed `Previous Recovery Delta: 7 cycles` is a **literal comparator**, not reproduced by this run.
- Cells 244/246/248 completed without exceptions during this local execution. No hosted CI, independent replication, statistical confidence interval or deployment acceptance was tested.

## Provenance problem with later 2-cycle claim

Notebook cell **317** explicitly assigns `auto_latency = 2`, `auto_par = 0.881`. Cell **330** reads those values from a dataframe created out of the assigned literals and labels the resulting check verified. Cell **344** records `'Recovery_Latency': '2 Cycles'` in a benchmark dictionary. Cell **509** copies `audit_telemetry_df` (an earlier series) then explicitly sets `actual_recovery = 2`. Cell **526** stores 2-cycle recovery and comparative numbers in a static benchmark dictionary. **These are not independent source-telemetry derivations.**

Later Three-Regime cell **846** uses an actual `recert_audit_df` calculation for a *different* model, seed 99 and stress endpoint 50. Do not conflate its recovery definition with the 50-cycle refactored controller's earlier 4-cycle test. Cells **827/834** recorded NON-COMPLIANT outcomes; cell **851** reports production readiness without establishing independent scientific validation.

## Conclusion and next admissible steps

- Mark **four-cycle seed-42 refactored simulation** as locally reproduced, limited to the specified cells and metric.
- Keep **seven-cycle baseline** historical and not reproduced in this receipt.
- Mark **two-cycle 50-cycle controller result** unresolved: selected later cells restate a value without computation; trace actual later PID source and telemetry before drawing a broader conclusion.
- Reconstruct original baseline (7), intermediate optimization (4), post-PID (alleged 2) as *three distinct versioned runs*, each with hashes, seeds, units, environment, outputs and exact recovery event definition.
- Do not upload the raw historical notebook to this public repository. Scan it for secrets, private content, network requests and side effects before any complete replay. Never interpret a same-operator rerun as outside-independent evidence.

**Authority ceiling:** exploratory control simulation, no general stability/superiority proof, no externally validated effect or production certification.