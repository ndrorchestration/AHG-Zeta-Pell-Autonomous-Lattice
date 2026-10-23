"""Standalone standard-library checks of the research screening boundary."""
import unittest
from estimator_state_gate import assess_estimator_state


class EstimatorGateTests(unittest.TestCase):
    def test_finite_fresh_bounded_input_passes_screening_only(self):
        r = assess_estimator_state([0, 1, 2, 3], [0.1]*4, age_cycles=0)
        self.assertTrue(r.admitted)
        self.assertEqual(r.reason, "SCREENING_PASS_NOT_AUTHORIZATION")

    def test_missing_stale_and_wrong_dimensions_fail_closed(self):
        for args in (
            (None, None, None),
            ([0]*4, [0.1]*4, None),
            ([0]*3, [0.1]*3, 0),
        ):
            with self.subTest(args=args):
                self.assertFalse(assess_estimator_state(args[0], args[1], age_cycles=args[2]).admitted)
        self.assertFalse(assess_estimator_state([0]*4, [1]*4, age_cycles=2).admitted)

    def test_nan_infinity_negative_or_excess_variance_rejected(self):
        for state, variance in (
            ([0, float('nan'), 0, 0], [1]*4),
            ([0, 0, float('inf'), 0], [1]*4),
            ([0]*4, [1, -1, 1, 1]),
            ([0]*4, [1, 101, 1, 1]),
            ([1001, 0, 0, 0], [1]*4),
        ):
            with self.subTest(state=state, variance=variance):
                self.assertFalse(assess_estimator_state(state, variance, age_cycles=0).admitted)

    def test_invalid_contract_types_fail_closed(self):
        invalid_contracts = (
            ({"age_cycles": True}, "STALE_OR_UNKNOWN"),
            ({"max_age_cycles": True}, "INVALID_CONTRACT"),
            ({"max_abs_state": True}, "INVALID_CONTRACT"),
            ({"max_variance": "100"}, "INVALID_CONTRACT"),
        )
        for kwargs, expected_reason in invalid_contracts:
            with self.subTest(kwargs=kwargs):
                call_kwargs = dict(kwargs)
                result = assess_estimator_state(
                    [0] * 4,
                    [1] * 4,
                    age_cycles=call_kwargs.pop("age_cycles", 0),
                    **call_kwargs,
                )
                self.assertFalse(result.admitted)
                self.assertEqual(result.reason, expected_reason)

    def test_bad_contract_and_nonnumeric_inputs_rejected(self):
        self.assertFalse(assess_estimator_state(["bad"]*4, [1]*4, age_cycles=0).admitted)
        self.assertFalse(assess_estimator_state([0]*4, [1]*4, age_cycles=0, max_variance=-1).admitted)


if __name__ == "__main__":
    unittest.main()
