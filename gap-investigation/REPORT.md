# E7 physical-gap investigation — results and finite milestones

## Verified outcome

**The tested symmetry constraints determine a quadratic form's shape but leave a positive real normalization free. In the stated one-loop EFT/matching model, running transports that boundary freedom; it does not select a coupling.** This is a conditional result, not a general no-go theorem for E7 UV completions.

`check_gap.py` ran with Z3 5.1.0. All **13 SMT checks** passed and were replayed from saved `.smt2` files by `verify_existing.py`, without regenerating the original receipt. That verifier also checked original experiment/Theory2 source hashes. `Gap.lean` compiled with actual **Lean 4.32.1**, commit `f054605aea4b840552cca2e725580bffd1e1b704`, and produced `Gap.olean`. Each of its **three public bridge theorems** printed `does not depend on any axioms`. They are polymorphic conditional statements, not a Lean formalization of all E7 representation theory or QED.

### What the checks actually establish

1. Constructed the Bourbaki E7 Cartan matrix (chain 1–3–4–5–6–7, branch 2–4) and all seven simple reflections, rather than assuming the free-scale conclusion. Exact determinant is 2. Rational LDL-transpose pivots are `2, 2, 3/2, 5/6, 4/5, 3/4, 2/3`, all positive; reconstruction is checked exactly.
2. Solved all symmetric-matrix reflection-invariance equations. The assertion that a solution differs from `k*A` is **UNSAT**. Conversely, the assertion that *some positive real k* makes `k*A` fail a reflection equation is **UNSAT**. Thus this is a full positive ray, not just two sampled constants. This explicitly constructs **Weyl invariance on the real Cartan space**, not full Lie-algebra adjoint invariance.
3. Proved conditionally in Lean that every coefficient postcomposition preserves a base invariant functional. For a conventional kinetic functional, postcomposition is multiplication by the coefficient. Full adjoint invariance of that base functional is an explicit input to this theorem.
4. For fixed positive embedding index `kY` and common threshold/running contribution `d`, tested `y=kY*x+d`, where `x` is a boundary inverse coupling and `y` the low-energy inverse coupling. Distinct boundary values cannot yield equal outputs (**UNSAT**); distinct positive outputs are possible (**SAT**). Independently fixing the same boundary value restores uniqueness (**UNSAT** for differing outputs). No 137 or experimental alpha enters these equations, except in a separate deliberate test of whether they imply the selected 137 ansatz; they do not.
5. A toy scalar potential `(phi-v)^2` has a unique minimum while two independent positive kinetic coefficients remain allowed. This disproves the logical inference *unique scalar vacuum alone implies fixed gauge coefficient* in this toy class. It does **not** classify E7 compactification vacua or include quantum effective-potential feedback.

## Explicit physics assumptions

Take a four-dimensional gauge EFT with fixed generator and charge normalization, connection convention `F=dA+[A,A]`, matter covariant derivative `D=d+A`, canonically normalized matter, and kinetic term `L_kin = -c B(F,F)/4`, `c=1/g^2>0`. Once these conventions are fixed, changing c changes the interaction coupling after canonical normalization; it is not merely relabeling the generators. The ad-invariant form B is assumed to exist. Gauge invariance of B constrains its tensor structure, not the separately supplied positive coefficient.

The matching/RG check is the **affine one-loop approximation with fixed spectrum, scales, embedding, thresholds and beta coefficients**, all packaged in `kY,d`. It is not a formal solution of the full quantum field theory. Two-loop, coupling-dependent masses/thresholds, a dynamical gauge-kinetic function or UV boundary selection need separate analysis. The present check says nothing against a completion that actually derives those data.

## Concrete legacy failure milestones

All citations refer to unchanged original source files; their SHA-256 hashes are in `smt-receipt.json`.

| Milestone | Evidence | Bounded result |
|---|---|---|
| Lagrangian tensor consistency | `exp44_lagrangian_derivation.py:238–265` | Claims `Sym^2(56)=1+1463`; exact symmetric-square dimension is 1596, not 1464. Its quoted `56*56` decomposition contains no 56 despite its asserted invariant cubic on three 56s. The latter is an audit inference, not newly verified representation theory. |
| State normalization | exp44:272–302 | Unit vector normalization does not force every component probability to 1/56. An exact unit-vector counterexample is checked. The source alternates between `y0/sqrt(56)` and `y0/56`. A specified state, coupling tensor and Higgs sector are missing. |
| Common invariant normalization | exp44:61–69; `exp58_alpha_running.py:374–386`; `exp63_delta_derivation.py:211–215` | With the supplied trace identity, `C2(56)=57/4` gives `T(56)=6`; exp44's `57/2` instead gives 12 while retaining adjoint Casimir 18. The two source conventions cannot be silently mixed. SMT checks the algebra, not an independent representation-table derivation. |
| Vacuum search reachability | `exp47_unique_vacuum.py:893–906,938–943` | Exhausted **all 14,641** four-tuples in `[0,10]^4`: maximum inverse coupling is `951/7`; **zero** are within 0.1 of 137. The printed eight-entry “unique solution” is outside the implemented search domain. This is not a general vacuum nonexistence result. |
| Boundary-free running | exp58:395–409 | Starts from `alpha_GUT=1/25`, then calculates `25+delta`; it assumes the boundary coefficient rather than deriving it. `exp46_coupling_running.py:190–199` explicitly uses an empirical two-loop correction; interpolated endpoint claims at :525–536 are not an independently derived fixed point. |
| Derived correction | exp63:608–612,636–655 | Computes an experimental residual and searches candidate expressions against it. Such target-informed selection is not a loop calculation or a prediction. No independent remainder bound was found. |

`legacy_checks.py` executed the exhaustive finite-domain and dimension/vector checks; `legacy-checks.json` contains exact results. No random sample or synthetic empirical data is used.

## Arithmetic remains separate

Using the **user-provided** CODATA 2022 central value `137.035999177` and quoted standard uncertainty `0.000000021`:

- Integer candidate: signed residual `-35999177/1000000000`.
- Chosen corrected candidate `137+9/250`: signed residual **`+823/1000000000`**, or **`823/21` quoted experimental uncertainty units**.

Both are outside one quoted uncertainty. The second comparison is not a model significance, a look-elsewhere-corrected probability, or a rejection of every possible corrected E7 theory. No model error bar was supplied or invented. An independently derived expansion and remainder bound could change the comparison; simply naming an unspecified next term cannot.

## Theory2 reuse and environment limits

Actual Windows paths were verified with native Python:

- `C:/Users/mikeb/e7-alpha-theory`: HEAD `7f1309c04581f22081f0dde8185ad1fb523e4613`; tracked diff remained empty.
- `C:/Users/mikeb/theory2`: only a docs directory in the inspected local copy.
- `C:/Users/mikeb/theory2-full/formal`: rich source library with `leanprover/lean4:v4.32.1`, Mathlib `v4.32.1`; no installed `.lake` tree was found there. The local Theory2-full git directory is unborn (no HEAD), with pre-existing staged files; it was not modified.
- Theory2 `Formal/E7.lean` proves arithmetic on supplied invariants. `Formal/Running.lean:27–30,55–73` proves crossing for a **stipulated logarithmic function**. Its prose identification near an electron threshold is stronger than a formal equation alone establishes; scheme and massive-threshold matching remain physical assumptions. `Formal/AlphaContentAudit.lean` is an accounting/dependence audit, not an alpha derivation.

No Lean/Lake executable was on PATH; targeted local installations were absent, and a broader cache scan hit its 120-second bound. A full native Lean release download hit its 480-second bound at 75,202,396/576,976,598 bytes. The automatic retry was stopped. Before that retry, six complete initial archive entries (Lean executable and required runtime DLLs) had been extracted into this directory; **that executable was actually run and compiled the kernel-only proof**. This is a working partial Lean runtime, not a complete Lean/Mathlib installation. Do not treat the retained partial `.tar.zst` as an intact archive. Full Theory2/Mathlib rebuild is **not claimed**.

An initial isolated Z3 install timed out; retry succeeded with `z3-solver==5.1.0.0`, `zstandard==0.25.0`, Python 3.11.11. No global Python package environment was changed.

The file tool's Windows path mapping was inconsistent: reads via `/cygdrive/c/...` reached the intended originals, but new writes were actually placed under `C:/cygwin64/c/Users/mikeb/...` despite reporting the native target. Newly authored artifacts were copied byte-for-byte to the canonical directory before execution. Those accidental copies were left alone rather than deleting unrelated compatibility-tree contents. A GitHub release metadata diagnostic also resides at `C:/Users/mikeb/AppData/Local/Temp/e7-lean-release.json`. No existing project/history file was rewritten, committed or pushed.

## Reproduce from Windows Bash

```bash
# These commands have actually run successfully (forward-slash native paths).
C:/Users/mikeb/e7-alpha-theory/gap-investigation/.venv/Scripts/python.exe -B C:/Users/mikeb/e7-alpha-theory/gap-investigation/check_gap.py
C:/Users/mikeb/e7-alpha-theory/gap-investigation/.venv/Scripts/python.exe -B C:/Users/mikeb/e7-alpha-theory/gap-investigation/legacy_checks.py
# Verify the saved receipt and recompile Lean; do not regenerate before verification.
C:/Users/mikeb/e7-alpha-theory/gap-investigation/.venv/Scripts/python.exe -B C:/Users/mikeb/e7-alpha-theory/gap-investigation/verify_existing.py
C:/Users/mikeb/e7-alpha-theory/gap-investigation/lean-4.32.1-windows/bin/lean.exe --root=C:/Users/mikeb/e7-alpha-theory/gap-investigation -o C:/Users/mikeb/e7-alpha-theory/gap-investigation/Gap.olean C:/Users/mikeb/e7-alpha-theory/gap-investigation/Gap.lean
```

`verification.json` stores exact subprocess arguments, exit codes, stdout, source/artifact hashes and SMT replay statuses. For a clean setup, obtain a full trusted Lean 4.32.1 release and point the verifier at its binary; the local extracted runtime should not be redistributed as a complete toolchain.

## Next finite physical gates — no endless fitting

1. **Specify one candidate action**, including consistent trace convention, matter/Higgs reps and gauge-kinetic function. Fail the candidate if its claimed invariants do not exist or a coefficient is chosen using alpha. Do not repair it with an unconstrained extra parameter.
2. **Solve that action's vacuum problem** in a declared finite ansatz: equations, constraints, gauge equivalence, stationary points and stability. If a continuous coupling/modulus remains, record non-identifiability and stop that candidate's prediction claim. No generic flux search can replace this.
3. **Compute matching and RG with all inputs frozen before comparison**, including U(1) embedding/normalization, particle masses, thresholds, scheme and independently fixed boundary data. A free boundary value is an explicit failure of a parameter-free alpha prediction, not a cue to fit it.
4. **Derive the correction from the same action**, with perturbative order and a justified truncation bound. Test the resulting alpha prediction and at least one independent observable. If the interval misses measurement, reject that specified candidate or publish the failed approximation; do not subtract the observed residual to invent the next term.

The current finite investigation stops after identifying these concrete broken prerequisites and verifying the normalization/boundary freedom. It does **not** deliver a solved physical theory or select a unique future action.
