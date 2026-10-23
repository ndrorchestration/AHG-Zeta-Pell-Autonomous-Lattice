# Held-out estimator feedback — negative pilot, 2026-10-23

Source: private historical Colab notebook (SHA-256 `abf7409fed35abb762f9962cee272d74ec2d658c034f9674e7e3cf6e0b3ebbf1`). Operator-local exploratory replay, NOT preregistered or independent.

Training seeds 10–17; disjoint held-out seeds 101–108. Four measurement noise settings (0, 0.05, 0.2, 1.0); candidate feedback weights (0, 0.01, 0.025, 0.05). Primary metric: mean delay to earliest five-consecutive-COLLABORATOR window after stress, with a 31-cycle penalty for missing windows.

Training scores (mean cycles): 0 → 16.0; 0.01 → 16.25; 0.025 → 16.5; 0.05 → 16.78125. Training selected weight 0. Held-out baseline and selected controller both average 12.125 cycles over 32 paired seed/noise conditions. Equality is a **tautology** because the selected controller IS the baseline, not evidence that positive coupling generalizes.

The saved Python protocol was rerun with the original notebook on 2026-10-23; regenerated JSON was byte-equivalent as parsed JSON to the saved results. The notebook is NOT copied into this public repository. Correlated observations, exploratory model selection, same-operator run and missing preregistration preclude efficacy claims.

**Disposition:** negative pilot; retain original controller unchanged. Next work: characterize alternative estimator feedback mechanisms on disjoint development seeds and freeze evaluation before using any new holdout. Do not merge or promote scientific/release status without review.
