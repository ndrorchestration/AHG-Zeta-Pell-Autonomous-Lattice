# AHG estimator causal-path regression

Read-only test of the historical notebook's PIDAHGControlPlane.govern method. Does not modify the original notebook or qualify as independent validation.

Run locally with Python, NumPy and the original private notebook in /mnt/data. The test fixes seven destabilization scores and compares phase, control actions, and reset counts for three different estimator-state vectors (zero, all ones, and a divergent vector containing NaN). It asserts the output sequence is identical. This is a negative regression demonstrating that the exposed estimator-state parameter has no causal influence on these reported decisions in this method. It does not prove all system behavior is noise-invariant.

Original notebook remains private. See research issue #3 and draft PR #4 for context. No performance, stability or production claim.
