# Verified Tian–Yau clock-response gate

**Result:** the sourced leading heterotic action fixes the canonical pure-dilaton fractional gauge gradient, but Tian–Yau net-three topology does not fix the absolute coupling or a physical clock signal.

```
s=V_string exp(-2 Phi),
sigma=M/sqrt(2) ln(s/s0), rho=M/sqrt(6) ln(V/V0),
g6^-2=s0 exp(sqrt(2) sigma/M),
partial_(sigma/M,rho/M) ln(g6²)=(-sqrt(2),0).
```

The clock bridge remains conditional on a realistic E6 breaking/photon sector:
`H=e_atom^-2=(8/3)s+D`, `A_I=-partial_I H/H`.
The Al/Hg and Hg/Cs ratio rows are `(16/5) A_I` and `-6 A_I-B_I-N_I`, with explicit mass-ratio and nuclear response nuisances, not static alpha substitution. See `REPORT.md` for sourced conventions and the source's Al/Hg sign inconsistency.

Same actual quotient and tangent bundle, `J=lambda J0`, constant `Phi=Phi0+delta`, gives `s/s0=lambda³ exp(-2delta)` while retaining the same index. This is a controlled family of leading-order constant backgrounds, not assumed scalar motion or all-orders stabilized vacua.

## Executed result

- **41 exact/source/kernel checks passed** (includes source hashes and equation evidence; not 41 independent physical results).
- **16 saved SMT cases passed**, with positive and negative identifiability controls.
- **Four Lean declarations** printed no axiom dependencies; Lean exited zero. Kernel-only, not Mathlib/QFT formalization.
- **Six receipt-negative controls** rejected corrupted/missing evidence.
- SVD nullspace code reused read-only and independently checked by symbolic nullspace calculation.
- Citation evidence gate passed. No hosted CI, no publication, no numerical alpha/clock prediction.

## Replay

```
C:/Python313/python.exe -B C:/Users/mikeb/e7-alpha-theory/gap-investigation/tian-yau-clock-response-gate/verify.py
```

This verifies existing evidence without rebuilding the retained certificate. The native Python interpreter needs SymPy/NumPy; Z3 and Lean use the existing installations in the parent gap directory. No package installation is performed.

Artifacts: `REPORT.md`, `RELEASE_DISCLOSURE.md`, `formalization.yaml`; `calculate.py`, `smt_cases.py`, `Formalization.lean`; `certificate.json`, `verification.json`; `smt/`; exact source bytes/text and equation/URL/hash evidence under `sources/`. `prepare.py` and `finalize_sources.py` are acquisition/preparation utilities, not verification commands. Do not rerun them merely to replay evidence.
