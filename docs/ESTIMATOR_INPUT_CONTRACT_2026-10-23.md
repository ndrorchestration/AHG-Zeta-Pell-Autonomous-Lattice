# Estimator-to-controller interface — research contract

**Status: proposed, not admitted or validated.** This interface does not modify or wrap the historical AHG governor. The isolated module `research/estimator_state_gate.py` screens estimator input quality only.

## Inputs and rejection

A candidate estimate must include a four-dimensional finite state, four finite nonnegative covariance-diagonal values, and an explicitly known age in cycles. Default exploratory limits are state absolute value <= 1000, covariance diagonal <= 100 and age <= 1 cycle. Missing, malformed, stale, nonfinite or out-of-bounds values are rejected with a reason code. The thresholds are **screening placeholders**, not scientifically justified or safe operating ranges.

### Covariance-validation boundary

This interface accepts and screens only a covariance **diagonal**, not a full covariance matrix. It checks finiteness, nonnegativity and the exploratory upper bound for each diagonal entry. It does **not** check symmetry, off-diagonal cross-covariances, positive semidefiniteness, eigenvalues, innovation consistency, filter consistency, or whether the values came from a valid estimator. A covariance screening pass therefore cannot establish covariance validity or estimator correctness.

## Authority separation

An input screening pass is named `SCREENING_PASS_NOT_AUTHORIZATION`. It never supplies actuator values, changes PID gains, authorizes a Kalman reset, chooses phases, or certifies estimated state correctness. A future research variant must declare a separate typed decision policy, clamping, temporal consistency checks, uncertainty treatment, fallback behavior and human-reviewed stop conditions. Rejected inputs cannot be silently replaced with zeros or used to trigger privileged actions.

## Tests and validation gates

`research/test_estimator_state_gate.py` covers nominal bounded input, absent age, stale age, dimensions, NaN/infinity, negative or excessive variance, out-of-bounds state, invalid contract limits including oversized integers, textual/byte sequences, and boolean entries that must not be accepted as numeric measurements. Run with Python standard library from `research/`: `python -m unittest test_estimator_state_gate -v`. Tests are candidate code in draft PR #5; hosted CI and outside review are not established. A future integrated experiment must confirm changed state-to-actuator behavior under matched disturbances without introducing safety regressions and must keep validation data untouched by tuning.

## Evidence continuity

Prior local observations: estimator resets change estimator internals while fixed-score historical governance ignores estimator-state differences; nonzero simple feedback variants failed to improve dwell-window delay. This new screening gate tests input quality, **not** performance, stability, efficacy, or independent validation. No code paths in the historical simulation are altered.