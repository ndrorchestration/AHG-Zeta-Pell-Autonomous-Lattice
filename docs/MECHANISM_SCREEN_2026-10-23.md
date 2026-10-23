# AHG mechanism-development screen — October 23, 2026

Exploratory same-operator local test, not preregistered or independently validated. 48 runs: development seeds 20–23, measurement noise 0/0.2/1, four arms (original, estimator-triggered reset, estimator-informed proportional score gain, estimator-informed disturbance detection). Primary endpoint is five-consecutive-COLLABORATOR window delay, missing window penalized at 31.

| Arm | Mean penalized dwell delay | Changed-outcome noise-sensitive seeds | Missing windows |
|---|---:|---:|---:|
| Original | 17.0 | 0/4 | 0 |
| Reset | 17.0 | 0/4 | 0 |
| Gain | 17.0 | 0/4 | 0 |
| Disturbance detection | 19.1667 | 3/4 | 1 |

All arms had 0.87 mean packet acceptance in this small screen. Provisional intervention definitions: reset estimator stability matrices for sufficiently large estimator magnitude while score exceeds 0.1; multiply score by 1 + 0.1*tanh(first estimator component); or add 0.05 to score when first estimator component >0.5. Coefficients and thresholds are exploratory and uncalibrated. No intervention improved the chosen metric. Changed noise responsiveness is not proof of robustness. Do not choose a winner or use previously inspected held-out seeds to certify performance; future experiments require fresh hidden seeds and independent review. Historical controller unchanged.
