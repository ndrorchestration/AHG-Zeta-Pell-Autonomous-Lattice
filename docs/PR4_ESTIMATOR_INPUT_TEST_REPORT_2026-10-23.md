# PR #4 estimator-input test report — 2026-10-23

## Scope

This report records an execution review of draft PR #4:

- Repository: `ndrorchestration/AHG-Zeta-Pell-Autonomous-Lattice`
- PR: `#4`
- PR title: `research: bound proof-assisted AHG protocol and semantic verification gates`
- PR head before review changes: `055bd684b38b8846650d6774831c769154429761`
- PR base: `main` at `be50f3a076e1405fcf211aea72c0ef5c644df6cd`
- Working branch: `review/pr-4-estimator-input-tests`
- Review changes commit: `a666d6181456d6ef45cfc941a1c9611daacd7a5e`

The review was limited to the isolated research estimator-input gate and its standard-library unit tests. No historical experimental results, controller implementation, benchmark values, or validation data were modified.

This report does **not** establish scientific validation, stability, efficacy, safety, or independent reproduction of any historical result.

## Environment

Captured from the Windows Git Bash environment used for execution:

- OS shell: MSYS_NT-10.0-26300, x86_64
- Git: `2.53.0.windows.3`
- Python: `3.14.7`
- Python executable: `C:\Users\Admin\AppData\Local\hermes\tools\python-3.14.7+202****0901-win32-x64\python.exe`
- GitHub CLI: `gh version 2.98.0 (2026-08-20)`
- Test dependencies: Python standard library only (`unittest`)

## Exact commands and results

### PR inspection

```bash
gh pr view 4 --repo ndrorchestration/AHG-Zeta-Pell-Autonomous-Lattice \
  --json number,title,state,isDraft,author,headRefName,headRefOid,baseRefName,baseRefOid,mergeable,mergeStateStatus,body,url
gh pr diff 4 --repo ndrorchestration/AHG-Zeta-Pell-Autonomous-Lattice --name-only
```

Observed:

- PR #4 is open and draft.
- Head branch: `research/proof-assisted-ahg-2026-10`.
- Head SHA: `055bd684b38b8846650d6774831c769154429761`.
- Merge state at inspection: `CLEAN`; no merge was attempted.
- Estimator files in the PR: `research/estimator_state_gate.py` and `research/test_estimator_state_gate.py`.

### Baseline PR #4 tests

Executed from `research/` at the unmodified PR #4 head:

```bash
python -m unittest test_estimator_state_gate -v
```

Result:

```text
Ran 4 tests in 0.001s
OK
exit code: 0
```

### Baseline defect probe

Executed against the unmodified PR #4 head:

```bash
python -c "from estimator_state_gate import assess_estimator_state as a; print(a([0]*4,[1]*4,age_cycles=0,max_abs_state='1000'))"
```

Result:

```text
TypeError: must be real number, not str
exit code: 1
```

This violates the documented fail-closed contract for malformed contract limits: the function raised instead of returning an `EstimatorGateResult` with a rejection reason.

The original implementation also accepted `bool` values for integer parameters because Python `bool` is a subclass of `int`. For example, `age_cycles=True` could pass as cycle `1`, and `max_age_cycles=True` could be accepted as a contract bound.

### Review-branch tests after the proposed change

Executed from `research/`:

```bash
python -m unittest test_estimator_state_gate -v
python -m unittest discover -v
python -m compileall -q estimator_state_gate.py test_estimator_state_gate.py
```

Results:

```text
python -m unittest test_estimator_state_gate -v
Ran 5 tests in 0.000s
OK
exit code: 0

python -m unittest discover -v
Ran 5 tests in 0.000s
OK
exit code: 0

python -m compileall -q estimator_state_gate.py test_estimator_state_gate.py
exit code: 0
```

Additional post-change probes returned fail-closed results:

```text
age_cycles=True -> EstimatorGateResult(admitted=False, reason='STALE_OR_UNKNOWN', state=None)
max_age_cycles=True -> EstimatorGateResult(admitted=False, reason='INVALID_CONTRACT', state=None)
max_abs_state=True -> EstimatorGateResult(admitted=False, reason='INVALID_CONTRACT', state=None)
max_variance="100" -> EstimatorGateResult(admitted=False, reason='INVALID_CONTRACT', state=None)
```

## Defects and test gaps

1. **Malformed numeric contract limits could raise `TypeError`.**
   `isfinite()` was called outside a protective failure path. A string-valued limit therefore escaped the intended fail-closed result contract. Fixed in the review branch by handling `TypeError` and returning `INVALID_CONTRACT`.

2. **Boolean values were accepted where strict integer contract values were intended.**
   `bool` values passed `isinstance(value, int)`. Fixed for `expected_dimension`, `max_age_cycles`, and `age_cycles`; boolean numeric limits are also rejected as invalid contract values.

3. **Original tests did not assert rejection reason codes for most negative cases.**
   They checked `admitted=False`, but a wrong rejection reason could have gone unnoticed. The review adds reason-code assertions for the newly covered malformed contract cases.

4. **The documented phrase “overflow of state bounds” is stronger than the original test.**
   The original case tested `1001` against the default bound of `1000`; it did not exercise floating-point overflow. This remains a wording/coverage limitation, not a scientific conclusion.

## Proposed changes

The review branch contains only research-gate hardening and test/report documentation:

- Reject malformed and boolean contract limits without raising.
- Preserve fail-closed rejection for invalid age values.
- Add unit coverage for the newly identified contract-input cases.
- Record exact execution evidence in this report.

No historical result, benchmark, controller path, or empirical claim was changed.

## Follow-up review execution — 2026-10-23

A red-green test cycle was run for textual and byte sequences that can otherwise be coerced into numeric vectors:

```bash
python -m unittest test_estimator_state_gate.EstimatorGateTests.test_textual_and_byte_sequences_are_not_numeric_vectors -v
```

The new test failed on the unpatched implementation because all four malformed cases were admitted. The gate was then changed to reject `str`, `bytes`, and `bytearray` state/covariance inputs as `MALFORMED_INPUT`.

Post-fix verification:

```bash
python -m unittest test_estimator_state_gate.EstimatorGateTests.test_textual_and_byte_sequences_are_not_numeric_vectors -v
python -m unittest test_estimator_state_gate -v
python -m compileall -q estimator_state_gate.py test_estimator_state_gate.py
```

Results:

```text
focused test: 1 test passed
full estimator suite: 6 tests passed
compile check: passed
```

The estimator contract now states explicitly that the module screens only covariance diagonal entries. It does not validate a full covariance matrix, symmetry, cross-covariances, positive semidefiniteness, eigenvalues, innovation consistency, or estimator provenance.

## Additional adversarial execution — 2026-10-23

ChatGPT review identified two further malformed-input cases on the exact PR #5 lineage: boolean entries inside the state/covariance vectors and very large integer contract limits. The red phase produced two assertion failures for boolean entries and two `OverflowError` escapes from `math.isfinite(10**1000)`.

Added tests:

```bash
python -m unittest test_estimator_state_gate.EstimatorGateTests.test_boolean_entries_are_not_numeric_measurements test_estimator_state_gate.EstimatorGateTests.test_huge_numeric_limits_fail_closed -v
```

The gate now rejects boolean vector entries as `MALFORMED_INPUT` and catches `OverflowError` while screening numeric limits, returning `INVALID_CONTRACT`.

Post-fix verification:

```bash
python -m unittest test_estimator_state_gate -v
python -m unittest discover -v
python -m compileall -q estimator_state_gate.py test_estimator_state_gate.py
```

Results:

```text
focused tests: 2 passed
full estimator suite: 8 tests passed
unittest discovery: 8 tests passed
compile check: passed
```

Custom iterables or custom `__float__` implementations that raise unexpected exceptions remain outside the contract. The implementation catches defined conversion/type/overflow failures only; it does not broadly catch `BaseException`.

## Commit and collaboration state

- Initial code/test commit: `a666d6181456d6ef45cfc941a1c9611daacd7a5e`
- Text/byte and covariance-boundary follow-up: `546746a2311d78512c6d8df6504599328436548c`.
- Report-binding commit: `3af15db58130f3bea1aa6fd6f4deb7936d6ab00d`.
- Additional adversarial changes: `e6ae1d210eacbcab8fd452e81e0c7b328b9f4e70`.
- Draft follow-up PR: #5 remains open and draft against PR #4's source branch.
- Merge status: not merged; no merge or auto-merge action authorized or attempted.
