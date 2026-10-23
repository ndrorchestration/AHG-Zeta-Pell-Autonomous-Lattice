# Post-PID historical recovery — local replay 2026-10-23

**Scope:** historical simulation, original notebook in private Drive; same-operator local replay, **not independent verification**. Notebook source: https://colab.research.google.com/drive/1_FQQdX0aP6jhdA3ANJpg8Wk9_N85ilcu . Prior source checkpoint and 7/4 cycle receipts remain intact.

## Reproduction boundary

Fresh Python process; original notebook cell 216 executed for baseline dependencies, plus cell 265 (PID controller/config), cell 269, original class and import definitions from 272 and 275, original PID redefinition from 278, and definitions from 289; plotting and notebook top-level run invocations in 272/275/289 were omitted. Actual `FinalFilteredRunner` class `run` method executed without editing its control or scoring logic. `ProductionSimulationConfig(simulation_duration=50, random_seed=42, measurement_noise_std=...)` for noise values 0.02, 0.05, 0.10, 0.15. Environment: local Python with numpy, pandas, scipy, matplotlib (headless plotting omitted). This is a **selective reconstructed dependency execution**, not an unmodified full Colab replay.

## Observed results

For **each** of the four noise settings, calculated directly from dataframe telemetry: cycle 20 `TRIBUNAL (PID Active)` smoothed score 0.7507795398; cycle 21 `SENTINEL (PID Active)` score 0.3177821257; cycle 22 first `COLLABORATOR (PID Active)` score -0.0114377399. **First-return recovery = 22 - 20 = 2 cycles**. 44/50 packet acceptance = **0.88**, and maximum smoothed score = **0.9121445934**, not the separate historical 0.881 PAR literal. At cycle 24 mode transitions back to `SENTINEL (PID Active)` with score 0.2257801650. Consequently **2 cycles is time to first return**, not sustained recovery.

Identical outputs at all four claimed noise settings are a serious sensitivity/falsification question, not robustness proof. Inspect estimator influence, source of noise in scoring, pseudorandom reseeding, and whether measurement noise can affect the reported metrics. A negative smoothed score is also a signal-domain interpretation issue if the metric is claimed to be nonnegative entropy.

## Admission and caveats

The exact 2-cycle *first-return* figure is now **locally reproduced for this reconstructed post-PID runner only**. It does not establish sustained stability, multi-seed performance improvement, noise resilience, historical 88.1% PAR, independent validation or production acceptance. Do not compare 7→4→2 as controlled effect sizes until state definitions, implementation versions and test conditions are harmonized. Raw notebooks remain outside public repository. Proposed next ablations: vary seeds, selectively disable PID/smoothing/reset, test noise-to-score causal path, and add sustained-recovery criterion with fixed dwell window.
