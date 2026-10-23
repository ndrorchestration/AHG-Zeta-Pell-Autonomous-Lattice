# Proof-assisted AHG research contract (2026-10-23)

Status: **EXPERIMENT DESIGN ONLY — NOT PREREGISTERED; NOT RUN; NOT VALIDATED**.

This document is linked to [research issue #3](https://github.com/ndrorchestration/AHG-Zeta-Pell-Autonomous-Lattice/issues/3) and requires source recovery under [issue #1](https://github.com/ndrorchestration/AHG-Zeta-Pell-Autonomous-Lattice/issues/1). It does not modify the controller or certify historical output.

## Scope and external evidence

OpenAI released a proposed September 2026 Navier–Stokes result with Lean artifacts; Clay lists the prize problem as active during evaluation. A contemporary critique challenges semantic fidelity between informal and formal statements (https://arxiv.org/abs/2610.08144). Therefore **Lean compilation cannot substitute for a documented correspondence review**. October 2026 work on zero-free half-planes for Hecke L-functions (https://arxiv.org/abs/2610.12234) supplies no theorem about AHG controller stability or Pell timing performance.

References: https://openai.com/index/navier-stokes-solution/ ; https://www.claymath.org/news/navier-stokes-announcement/ ; https://www.claymath.org/millennium/Navier-Stokes-Equation/ .

## Evidence recovery gate

Capture source notebook identity and cryptographic hash; relevant exact cells and program outputs; parameter versions; raw seed-level telemetry; units; calculation scripts; disturbance inputs; accepted/excluded run rationale. Restore true historical chronology 7-cycle failure → 4-cycle retest → claimed 2-cycle recovery. Treat all jitter multipliers without a declared one-times baseline as **unsupported**.

## Formal proof gate

Start only with standard identities and exact definitions: Pell recurrence P(0)=0, P(1)=1, P(n+2)=2 P(n+1)+P(n), and silver ratio δ=1+sqrt(2). Define informal theorem, Lean theorem, hypotheses, imports, and axioms in a side-by-side mapping reviewed by a second reviewer. A valid elementary identity cannot prove control stability or spectral optimality. No proof claim should be admitted from a translated statement without this semantic check.

## Matched experiment proposal (not yet frozen)

**Primary null:** under matched conditions, Pell-derived scheduling does not improve median settling time relative to the strongest prespecified conventional schedule. Compare fixed, randomized, golden-ratio, Pell/silver-ratio and tuned conventional schedules at identical average opportunity rate, computation budget, noise stream and controller configuration. Use paired seeds and held-out disturbances. Measure recovery cycles, overshoot, phase lag, stability violations, packet acceptance, and per-run uncertainty. Prespecify sample size, acceptable missingness, effect threshold and significance/multiplicity correction *after* baseline reconstruction, before seeing new experimental outcomes. An observed null or conventional comparator superiority falsifies the practical Pell-advantage hypothesis under tested conditions.

**Controls:** zero-disturbance negative control, seeded stress tests, deliberate filter latency probes, estimator reset ablations, timing schedule swap only (otherwise same system), and a simple non-Pell optimized comparator.

**Stop conditions:** missing source custody; unresolved signal definitions; denominator-free ratios; mismatch between informal and formal theorem; comparison leakage; lack of independently reproducible data. Do not run an efficacy evaluation until those prerequisites are resolved and a protocol is frozen.

## Assigned review roles (not assigned persons)

Mathematician: identities and operator definitions. Formal reviewer: semantics/axioms. Control engineer: dynamics and stability assumptions. Experiment reviewer: baselines/falsifiers. Provenance/security reviewer: custody and CI disclosures. None is an independent approval until assigned and documented.

## Boundaries

Separate project from PDMAL and DGAF. No inferred topology, efficacy, independent validation, high assurance, production release or mathematical breakthrough. Historical benchmark literals remain quarantined. This file documents a proposal rather than a successful experiment.
