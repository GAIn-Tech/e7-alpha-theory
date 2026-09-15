# exp47: exact finite-vacuum next-gate audit

## Outcome and boundary

**The printed eight-entry tuple is not a unique solution of the implemented predicates, even after explicitly extending the arity to eight.** Under the diagnostic domain `[0,10]^8`, the target-selected sum has **2,010,423 ordered tuples**, occupying **593 distinct permutation orbits**. These are counts of integer tuples satisfying toy predicates, **not physical vacuum counts**. Permutation orbits are a conservative combinatorial check, not an assertion that permutations are the true gauge-equivalence relation.

The physical next gate is **BLOCKED_MISSING_ACTION**. exp47 and its summary do not supply the equations and kinetic data needed to solve a finite physical vacuum problem or certify stability. This is a failure of the specified legacy candidate's evidence, not a general no-go theorem for E7 compactifications. No measured alpha value, fitting, residual correction, or parameter optimization is used in this audit. The literal `137` appears only because it is the legacy acceptance target being audited.

The stdlib Python certificate is exact rational/integer arithmetic plus source inspection, **not a Lean-kernel proof**. It does not repeat the previous `[0,10]^4` enumeration. The pre-existing result remains provenance, not this audit's new deliverable.

## Actual implemented predicates

`exp47_unique_vacuum.py:846–945` defines:

- Four entries, independently sampled as integers in `[0,10]` (`:895`). A sample count is not exhaustive coverage.
- `e7_preserved := sum(flux) % 7 == 0` (`:897–898`). No individual-entry divisibility and no representation/commutator calculation.
- `moduli_stabilized := number of strictly positive entries >= 3` (`:900–901`). No stationarity equation or mass calculation.
- `a := 133 + sum(flux)/14` (`:903–906`). This is a prescribed arithmetic formula, not a gauge-kinetic function derived from the geometry.
- `swampland_ok := 120 < a < 150` (`:908–909`). The search does **not call** the separate WGC routine.
- Acceptance additionally requires `abs(a-137) < 0.1` (`:858–861`). The printed best candidates are further sorted by distance from that same target (`:933`).

The certificate checks the relevant AST expressions against these predicates, then evaluates selected legacy expressions after replacing division and float literals with exact `Fraction` operations. It never runs legacy `main` or writes legacy output. The saved function/line inventory supports manual inspection; absence of physics is not inferred from a keyword search alone.

Let `S=sum(flux)`. The residual is `(S-56)/14`; the target window is `|S-56| < 7/5`. Without the sum-divisibility predicate the integer possibilities are 55, 56 and 57. With `S` divisible by 7, **only 56 survives**. Thus the number 56 is already determined by the supplied target and coupling ansatz, not independently selected by a vacuum equation. The original domain cannot reach it; changing arity is a change of the search problem, not recovery of an original result.

## Executed bounded diagnostic extension

To test the printed arity without an unbounded scan, this audit declares **exactly eight nonnegative integer entries, each at most 10**, preserving the source predicates otherwise. It computes the full `(sum, positive-entry count)` distribution by integer dynamic programming **before** applying the legacy target. The algorithm is cross-checked against direct enumeration on three small independent domains. A separate `combinations_with_replacement` enumeration counts permutation orbits.

- Total ordered tuples: **214,358,881**.
- Passing all three non-target source predicates: **30,622,283**.
- Passing the legacy target as well: **2,010,423**.
- Target-selected permutation orbits: **593**.
- Exact sum/coupling histograms and all witnesses are in `vacuum-receipt.json`.

Explicit counterexamples to uniqueness:

1. `(7,7,7,7,7,7,7,7)` has sum 56 and `a=137`.
2. `(6,8,7,7,7,7,7,7)` has the same sum and passes every predicate. It is not even a permutation of the first tuple.

Neither tuple is in the original four-entry domain. Both are inside the declared diagnostic domain.

The non-target predicates also permit different couplings. For example, `(0,0,0,0,0,7,7,7)` has sum 21 and `a=269/2`, whereas `(0,0,0,0,0,7,7,14)` has sum 28 and `a=135` (the latter is outside cap 10, so is only a predicate witness). Within cap 10, the complete pre-target histogram establishes the same non-identifiability without changing bounds. Even the original-domain tuple `(1,1,1,4)` passes the three non-target predicates with `a=267/2` although none of its positive entries is a multiple of 7.

### Extra per-entry flux quantization is a different premise

The summary (`EXP47_UNIQUE_VACUUM_SUMMARY.md:164–167`) proposes flux quantized in units of 7 and a total of 56. The implementation only checks the **sum** modulo 7. If one adds individual multiples of 7, retains eight entries and cap 10, then the allowed entries are only 0 or 7. Imposing total 56 forces all eight to be 7. The certificate exhausts these choices and finds one target-selected tuple. This conditional uniqueness is imposed by the added premises and saturation of the cap, not established dynamics.

Without that cap, `(0,0,7,7,7,7,14,14)` is another eight-entry multiple-of-7 tuple with total 56 and at least three positive entries. It passes all legacy predicates. The restriction to eight entries is itself absent from the physical model; no flux lattice, topological cycle count, tadpole form or geometric upper bound was supplied to justify it. No diagnostic-domain change here is offered as a theory repair.

## Vacuum-equation and stability audit

The source names relevant concepts but does not instantiate the required computation:

- **G2 (`:172–221`):** geometric volumes are dataclass fields but the coupling routine uses a constant `133.0` plus the *mean* flux, ignoring those volume fields. `n_moduli=43`; `n_stabilized=min(len(flux),43)` merely counts entries, including zero entries. The printed `[4]` route gives `137` but claims only **1 of 43** moduli stabilized even by its own counting proxy. For eight sevens its formula gives **140**, not the Part 8 value **137**. These are different ansatz formulas, not two independent derivations. The superpotential integral is prose, not an evaluated function of moduli.
- **F-theory (`:295–355`):** `cycle_volume=137.0` is supplied as a default; `e7_factor` explicitly includes `133+56/14`. For nonzero volume the executed expression simplifies to `137*cycle_volume*tau_imag/(4*pi)`, leaving continuous supplied inputs. Stabilization returns the number of flux entries; no equations are solved. The `sum % 7` flag is not a singlet-flux test.
- **Heterotic (`:437–465,523–543`):** the dilaton is an input and is scanned, including `log(137)/2`. The KKLT-like expression is printed, not implemented as a potential whose critical points are found. No dilaton stabilization calculation accompanies the coupling routine.
- **Swampland (`:575–651,668–675`):** the separate routine compares a hypothesized maximal WGC mass to a species cutoff, without constructing a charged spectrum. Its caller passes `alpha` as `g`, although these differ under the conventional `alpha=g^2/(4*pi)` definition. Regardless of this additional convention problem, none of it is called by the finite search. The distance-conjecture and unique-vacuum conditions are strings/lists, not executable constraints on a specified moduli metric or potential.

There is no specified finite scalar action with an evaluated potential, stationary-point equations, gauge-equivalence quotient, positive kinetic metric, physical mass matrix, flat-direction exclusion, or appropriate AdS/Minkowski stability test linking these predicates to an isolated vacuum. A Hessian alone would also need the field metric and the appropriate vacuum stability criterion. A point count or a Boolean named `moduli_stabilized` establishes none of these.

The summary does label its overall mechanism a hypothesis needing derivation (`:4,157–173,209–242`), but its “resolved” correction and geometric/non-anthropic-selection prose (`:124–153,175–180,273–286`) exceeds the supplied computation. No confidence percentage in that document is an audited statistical quantity. Its linked historical `STRING_COMPACTIFICATION_ALPHA.md` was not present at the canonical project-root path; no missing background content is assumed.

## Next physical gate: finite and target-blind, but presently blocked

Follow the pre-existing `gap-investigation/REPORT.md:75–80` rather than expanding a number search:

1. Require **one** independently specified action/compactification and finite field/flux ansatz. Freeze the source, field domain, flux basis, charge/trace conventions, actual E7 singlet constraints, tadpole/bound data and gauge equivalence before evaluating any coupling.
2. Derive the potential, stationary equations, field-space metric and gauge-kinetic function from that input. Stop with “missing action/data” if these cannot be supplied; do not invent a toy potential to stand in for exp47.
3. Enumerate/solve the declared finite flux cases and classify **all** stationary solutions in the declared domain, including boundary cases and continuous families. Establish completeness within that domain, and classify physical zero modes and stability with the appropriate mass criterion. Do not use closeness to 137 as a constraint or sort key.
4. If a continuous physical coupling/modulus or multiple physically inequivalent solutions survives, report it and stop the uniqueness/prediction claim. If exactly one valid solution survives, evaluate its independently defined gauge-kinetic function; matching and RG are a separate frozen-input gate.

The current audit completes the warranted bounded combinatorial diagnostic and stops at the missing-action boundary. It does **not** claim completion of this future physical gate.

## Reproduce and verify

From Windows Bash with native forward-slash paths:

```bash
python -B C:/Users/mikeb/e7-alpha-theory/gap-investigation/next-gate/vacuum_audit.py
```

The default command reads the existing receipt first, then recomputes the full deterministic payload and compares it, including exact source and artifact SHA-256 hashes. Missing or stale evidence fails; it is not silently replaced. Initial generation uses `--create` and exclusive file creation, refusing to overwrite an existing receipt. There are no external packages or randomized checks.

Owned additive files only:

- `C:/Users/mikeb/e7-alpha-theory/gap-investigation/next-gate/vacuum_audit.py`
- `C:/Users/mikeb/e7-alpha-theory/gap-investigation/next-gate/vacuum-report.md`
- `C:/Users/mikeb/e7-alpha-theory/gap-investigation/next-gate/vacuum-receipt.json`

Canonical originals were read through `/cygdrive/c`. File-tool writes landed in the compatibility tree, so the newly authored script/report were copied byte-for-byte using native Python and verified at the canonical paths. The receipt is created by native Python directly. No existing project source, prior gate artifact, or parent-owned next-gate file is modified. This audit is AI-assisted, self-reviewed, and locally executed; no external peer review or hosted CI is claimed.
