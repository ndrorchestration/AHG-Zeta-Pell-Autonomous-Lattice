# Mechanism causal-path diagnostic — 2026-10-23

Operator-local follow-up on the 48-run development screen only. No new held-out evaluation, independent validation, production clearance, or modification of historical controller. Input: original private Colab notebook SHA-256 `abf7409fed35abb762f9962cee272d74ec2d658c034f9674e7e3cf6e0b3ebbf1`.

A diagnostic wrapper around the original `FinalPIDAHGControlPlane` counted intervention triggers and compared cycle-by-cycle phases and PID epsilon/tau actions with the original at each matched (seed, noise) pair. Seeds 20–23, noise standard deviation 0, 0.2, 1.0; each of three experimental arms has 12 matched cases.

| Intervention | Trigger count across 12 cases | Phase trace differs | PID epsilon/tau trace differs |
|---|---:|---:|---:|
| Estimator stability reset (abs(state[0]) > 0.5 and score > 0.1) | 75 additional resets | 0/12 | 0/12 |
| Score gain (score * [1 + 0.1*tanh(state[0])]) | 600 nonzero score changes | 9/12 | 12/12 |
| Disturbance detection (+0.05 score if state[0] > 0.5) | 118 triggers | 10/12 | 12/12 |

The reset intervention executes but does not affect the observable phase/action output here; consistent with estimator state not entering the decision function. This does NOT establish the internal estimator state was unchanged or that estimator resetting is harmless. The gain intervention changes phase/action traces despite the unchanged aggregate dwell metric in the previous screen. The detection intervention changes phases/actions but previously worsened dwell mean. All are negative with respect to the previously chosen recovery objective.

**Review requirement:** Verify exact reset call effects and causal topology; distinguish estimator-side state changes, phase transitions, continuous actuator changes, and outcome changes. Only then propose one externally reviewable mechanism. Do not retune on previously disclosed holdout seeds. Keep research branch draft and scientific ceilings intact.

Local reproducibility artifacts were generated in the conversation workspace (`ahg_mechanism_diagnostic.py`, `ahg_mechanism_diagnostic_results.json`), not a public copy of the private notebook.