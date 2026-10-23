# Local baseline-failure reproduction — 2026-10-23

**Status: same-operator seeded simulation replay; independent validation NOT ESTABLISHED.**

Original historical Colab notebook: https://colab.research.google.com/drive/1_FQQdX0aP6jhdA3ANJpg8Wk9_N85ilcu . Baseline source: zero-indexed code cells **216, 218, 231** (executed in this order with no source edits in an isolated Python process). Original configuration: 50 cycles; random seed 42; stress cycles 15–20. Reproduction uses local process only, not hosted CI or independent operator.

## Direct result

- Benchmark peak destabilization `<1.2`: measured **0.861566**; pass under the original code's check.
- Original recovery benchmark: `<=4` cycles.
- Cycle 20: `TRIBUNAL`, destabilization `0.744777`.
- Cycles 21–26 remain `TRIBUNAL`.
- Cycle 27: first `COLLABORATOR`, destabilization `0.048313`.
- `27 - 20 = 7` recovery cycles; historical benchmark **FAIL** as the original cell 231 itself reports.

Measured scores cycles 21–27: `0.236659, 0.055767, 0.127540, 0.189378, 0.004294, 0.054607, 0.048313`. The governance hysteresis means low scores on earlier cycles do not by themselves define recovery. Compare against locally reproduced **4-cycle refactored** run in `RECOVERY_REPRODUCTION_RECEIPT_2026-10-23.md`, under its separate implementation.

## Interpretation and outstanding work

The locally reproduced historical **7→4** sequence is now supported by two seeded implementation-specific replays. It is not a controlled between-implementation estimate under multiple seeds or independent validation. The post-PID 2-cycle result remains **NOT REPRODUCED**; later hardcoded values do not count as trace data. Do not mix the separately implemented Three-Regime controller with the initial 50-cycle recovery metric. No production, efficacy, general stability, or cross-project claim is promoted.

## Reproduction instructions (private notebook required)

Review source cells for network/file side effects and sensitive data; in an offline Python environment with NumPy and pandas, load the JSON notebook, extract cell `source` strings at indices 216,218,231, then execute them in order in a fresh namespace. Inspect `audit_telemetry_df` and compute first `phase == 'COLLABORATOR'` with `cycle > 20`; expected cycle 27. Preserve deviations and exceptions rather than overwriting this receipt.
