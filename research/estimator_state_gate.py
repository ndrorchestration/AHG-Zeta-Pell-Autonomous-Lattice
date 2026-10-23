"""Research-only fail-closed gate for prospective AHG estimator feedback.

Does not replace, patch, or invoke the historical controller. Admission of an
estimator signal requires an independently specified model and test protocol.
"""
from dataclasses import dataclass
from math import isfinite
from typing import Sequence


@dataclass(frozen=True)
class EstimatorGateResult:
    admitted: bool
    reason: str
    state: tuple[float, ...] | None


def assess_estimator_state(
    state: Sequence[float] | None,
    covariance_diagonal: Sequence[float] | None,
    *,
    expected_dimension: int = 4,
    max_abs_state: float = 1e3,
    max_variance: float = 1e2,
    max_age_cycles: int = 1,
    age_cycles: int | None = None,
) -> EstimatorGateResult:
    """Validate evidence quality; never authorize a control action.

    Covariance diagonal is a bounded screening proxy, not a PSD proof.
    All rejected inputs fail closed without substituting synthetic data.
    """
    if state is None or covariance_diagonal is None:
        return EstimatorGateResult(False, "MISSING_INPUT", None)
    if isinstance(state, (str, bytes, bytearray)) or isinstance(
        covariance_diagonal, (str, bytes, bytearray)
    ):
        return EstimatorGateResult(False, "MALFORMED_INPUT", None)
    if type(expected_dimension) is not int or expected_dimension <= 0:
        return EstimatorGateResult(False, "INVALID_CONTRACT", None)
    try:
        valid_limits = (
            isfinite(max_abs_state) and 0 < max_abs_state and
            isfinite(max_variance) and 0 < max_variance
        )
    except (TypeError, OverflowError):
        valid_limits = False
    if not valid_limits or isinstance(max_abs_state, bool) or isinstance(max_variance, bool):
        return EstimatorGateResult(False, "INVALID_CONTRACT", None)
    if type(max_age_cycles) is not int or max_age_cycles < 0:
        return EstimatorGateResult(False, "INVALID_CONTRACT", None)
    if type(age_cycles) is not int or age_cycles < 0 or age_cycles > max_age_cycles:
        return EstimatorGateResult(False, "STALE_OR_UNKNOWN", None)
    try:
        raw_values = tuple(state)
        raw_variance = tuple(covariance_diagonal)
    except (TypeError, ValueError, OverflowError):
        return EstimatorGateResult(False, "MALFORMED_INPUT", None)
    if any(isinstance(x, bool) for x in raw_values + raw_variance):
        return EstimatorGateResult(False, "MALFORMED_INPUT", None)
    try:
        values = tuple(float(x) for x in raw_values)
        variance = tuple(float(x) for x in raw_variance)
    except (TypeError, ValueError, OverflowError):
        return EstimatorGateResult(False, "MALFORMED_INPUT", None)
    if len(values) != expected_dimension or len(variance) != expected_dimension:
        return EstimatorGateResult(False, "DIMENSION_MISMATCH", None)
    if not all(isfinite(x) and abs(x) <= max_abs_state for x in values):
        return EstimatorGateResult(False, "UNTRUSTED_STATE", None)
    if not all(isfinite(x) and 0 <= x <= max_variance for x in variance):
        return EstimatorGateResult(False, "UNTRUSTED_COVARIANCE", None)
    return EstimatorGateResult(True, "SCREENING_PASS_NOT_AUTHORIZATION", values)
