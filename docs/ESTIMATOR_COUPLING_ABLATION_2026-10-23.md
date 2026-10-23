# Estimator coupling ablation — 2026-10-23

Operator-local exploratory experiment, NOT preregistered, independently validated, or production qualified. Original controller unchanged. A separate subclass sends the original destabilization score plus 0.05 times tanh of the first estimator state component into the historical governance method. This coefficient is arbitrary and uncalibrated.

Test matrix: five seeds (0,1,2,42,99), four measurement noise values (0,0.05,0.2,1), two variants = 40 simulations of 50 cycles each. First return and first five-consecutive-collaborator dwell windows computed relative to end of stress at cycle 20.

Noise variation across outcomes: original 0 of 5 seeds; experimental coupled variant 4 of 5 seeds. At noise 1.0, five-cycle dwell start (original versus coupled): seed 0: 8 vs 22; seed 1: 8 vs 8; seed 2: 13 vs 13; seed 42: 20 vs 25; seed 99: 19 vs 22. First-return times were unchanged in these five high-noise cases. Changing the estimator input can therefore change controller results, but these observations do not show superiority; high-noise dwell is worse for three seeds.

Limitations: selective notebook class extraction in local Python, same operator, very small seed sample, arbitrary coefficient, no uncertainty estimates or proof, and no externally verified source telemetry. No production claim. Do not modify the historical version or merge without review. See draft PR #4 and issue #3.