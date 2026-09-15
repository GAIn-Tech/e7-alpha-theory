# E7 next gate: corrected representation prerequisites, action, and vacuum boundary

## Result

The exp44 invariant cubic on three 56s does **not exist**. Exact weight-character computation gives

- `Sym^2 V(omega7) = V(2 omega7) + V(omega1) = 1463 + 133`;
- `Lambda^2 V(omega7) = V(omega6) + 1 = 1539 + 1`;
- the full tensor cube has **no zero weight**, hence no invariant tensor, symmetric or otherwise.

This is stronger than the first gate's dimension mismatch or an inference from a quoted tensor-product table. The legacy Yukawa/superpotential cannot be retained with its stated fields. A consistent replacement is possible but introduces explicitly free input couplings; it is not a derivation of alpha.

The exp47 diagnostic extension also fails uniqueness: with eight entries in `[0,10]` its target-selected predicates accept **2,010,423 ordered tuples / 593 permutation orbits**. Those are toy integer counts, not physical vacua. See `vacuum-report.md` and the replayable `vacuum-receipt.json`; actual vacuum classification remains blocked by missing action/geometric data.

## Exact representation computation and provenance

`representation_checks.py` imports **only** `cartan_E`, `positive_roots`, and `weyl_dim` (via module loading) from the existing independent computation `C:/Users/mikeb/theory2-full/docs/analysis/weyl_verification.py`. It uses standard-library integers and `Fraction`, not the exp44 hardcoded representation answers. SymPy was absent in the inspected Python interpreter; installing Sage or another Lean/Mathlib toolchain was unnecessary. No new download was attempted.

Bourbaki labeling is fixed explicitly: chain 1–3–4–5–6–7, branch 2–4. The algorithm:

1. Constructs the Cartan matrix and 63 positive roots using Theory2 root-string closure. Inverts the matrix by exact Gaussian elimination.
2. Generates the Weyl orbit of omega7 under all seven simple reflections. Its 56 distinct weights saturate the independently computed Weyl dimension 56, so the whole representation has those weights with multiplicity one. Checks the minuscule positive-root pairings as well.
3. Builds **every weight multiplicity** of the symmetric and exterior squares using unordered pairs with and without the diagonal, respectively. No decomposition is supplied as input.
4. Selects the maximal remaining dominant weight and constructs its irreducible character with the Freudenthal recurrence. All computed multiplicities must be nonnegative integers, Weyl invariant, and sum to the independently calculated Weyl dimension. Subtraction from the actual square character must leave no negative coefficient; the process ends with zero residual. The resulting highest weights and dimensions are in `representation-receipt.json`.
5. Counts zero-weight triples by convolution of the full square with the original weight set, obtaining zero. Since an invariant must be torus invariant, this rules out *all* invariant tensors in `56 tensor 56 tensor 56`, not only a symmetric cubic. Independently checks omega7's simple-root coordinates `(1,3/2,2,3,5/2,2,3/2)`: its root-lattice class has order two. Odd tensor powers stay in the nontrivial class.

Freudenthal is the mathematical input, not a newly kernel-proved theorem: `(||lambda+rho||^2-||mu+rho||^2)m(mu)=2 sum_{alpha>0,k>=1}(mu+k alpha,alpha)m(mu+k alpha)`. The script uses twice the root inner product to keep its recurrence integral. Restricting to the actual square support is valid because every constituent weight is a tensor-product weight. Weyl's character/dimension theory and highest-weight complete reducibility over the complex semisimple algebra are assumed standard mathematical results. This is an exact executable audit, **not a Lean formalization** or an independent expert review. The source and script SHA-256 hashes are included in the receipt. The character algorithm is new; the root/dimension routines are reused with explicit provenance.

## Normalization derived from weights, not mixed tables

Let `B0` denote the invariant bilinear form whose dual root metric has long-root squared length 2. For simple coroots `H_i`, `B0(H_i,H_j)=A_ij`. Direct sums over all 56 weights and all 126 roots independently give, for **every** Cartan entry:

```
tr_56(H_i H_j) = 12 A_ij
tr_adj(H_i H_j) = 36 A_ij
```

For a simple algebra, an invariant trace form is fixed by its Cartan restriction. These are trace coefficients **12 and 36 relative to B0**; they are not yet the common physics `T=6,18` convention. Define `Bphys=2 B0`, and choose a compact Hermitian generator basis with `Bphys(t_a,t_b)=delta_ab` (equivalently use minus the real compact anti-Hermitian trace where appropriate). Then

```
tr_56(t_a t_b)=6 delta_ab
tr_adj(t_a t_b)=18 delta_ab
C2(lambda)=(lambda,lambda+2 rho)_root / 2
C2(56)=57/4, C2(adj)=18
56 C2(56)=133 T(56).
```

Both the weight sums and the highest-weight Casimir formula are executed. If one instead uses the `B0`-orthonormal basis, the **entire pair** doubles: `T56=12, Tadj=36, C56=57/2, Cadj=36`. exp44's `C56=57/2` alongside `Cadj=18` does not represent either consistent convention. Choosing a trace convention does not select the separately multiplying physical inverse coupling.

## What exactly must change in exp44

The unchanged source `exp44_lagrangian_derivation.py:238–265` asserts a unique invariant cubic of chiral superfields in 56 and places the singlet in the symmetric square. Both are false. The singlet is the **antisymmetric** symplectic form Omega. Consequently `Omega_AB Q^A Q^B=0` for one commuting chiral superfield, not a nonzero superpotential interaction. For a single species of left-handed Weyl fermion, Lorentz scalar contraction makes the remaining gauge/flavor bilinear symmetric; an antisymmetric gauge contraction alone again vanishes. With distinct flavors an antisymmetric flavor structure can give a nonzero term. A singlet Higgs is not a 56; a coupling of two 56s to a singlet and a cubic of three 56s must not be conflated.

Two minimal kinds of representation repair exist, neither a unique physical model:

- keep a **single** 56 chiral superfield but use a Higgs in 133 (or 1463), since these occur in its symmetric square;
- keep the singlet Higgs and use **two distinct** 56 chiral superfields, allowing their antisymmetric gauge contraction.

The latter is the explicit candidate below. No claim is made that it reproduces Standard Model chirality, a neutrino mass, or E7 breaking. The normalized vector argument at exp44:272–305 still does not determine a selected component probability or a Yukawa Clebsch coefficient; repairing the tensor does not repair that inference.

## Minimal explicit corrected candidate action (new, not attributed to exp47)

Take four-dimensional **rigid N=1 supersymmetry**, compact simply connected E7, two chiral superfields `Q1,Q2` in 56, and a gauge singlet chiral field `S`. This deliberately omits gravity, soft breaking and higher-dimensional EFT operators. Use a canonical Kahler potential

```
K = Q1^dagger exp(2V) Q1 + Q2^dagger exp(2V) Q2 + S^dagger S
W = (m+y S) Omega_AB Q1^A Q2^B + a S + (b/2) S^2 + (kappa/3) S^3.
```

Omega is chosen unitary in the canonical Hermitian metric (`Omega Omega^dagger=1`); its scale is fixed once as part of field/tensor conventions; changes of that scale must be absorbed into `m,y`. The standard rigid superspace action consists of the D-term of K, the F-term of W plus its Hermitian conjugate, and a **constant** gauge kinetic F-term whose component convention is

```
L_gauge = - c/4 Bphys(F_mu_nu,F^mu_nu) + theta q_top,
c=1/g^2>0, F=dA+[A,A], D=d+A.
```

`q_top` denotes the topological density normalized to integer instanton charge for this global group; no numerical theta-to-trace conversion is required for the perturbative/vacuum calculation. In the B0 convention above, the standard long-root SU(2) embedding fixes that integer normalization. Gauge/fermion/superspace factors are chosen to reproduce the displayed component gauge term, not inferred from a conflicting trace table.

**All supplied free coefficients in these fixed coordinates:**

| Input | Freedom / dimension |
|---|---|
| `c` | one positive real dimensionless boundary inverse gauge coupling |
| `theta` | one real topological angle modulo its period |
| `m` | complex, mass dimension 1 |
| `y` | complex, dimensionless |
| `a` | complex, mass dimension 2 |
| `b` | complex, mass dimension 1 |
| `kappa` | complex, dimensionless |

This enumerates action coefficients, **not a claim that all phases are physically independent**. Field rephasings and singlet translations relate parametrizations and can move phases, coefficients and theta; no such change removes the physical gauge-strength freedom. A constant superpotential has no effect in rigid SUSY and is omitted; an additive vacuum energy convention is set to zero. Canonical K, constant gauge kinetic function, the field content, global group and omission of other operators are explicit model choices, not E7-derived facts. Including supergravity, noncanonical K, a singlet-dependent gauge kinetic function or higher-dimensional terms supplies further parameters and changes the vacuum problem; none is silently included.

At `Q1=Q2=0`, D vanishes and the F-flat equation is `a+b S+kappa S^2=0`. For generic coefficients there are two complex roots, not a unique vacuum. With positive canonical metric the potential is a sum of F squares and a nonnegative D term; F=D=0 gives a tree-level supersymmetric minimum. If `b+2 kappa S` and `m+yS` are nonzero, the singlet and charged scalar directions at this point have positive mass squared. Gauge bosons remain massless and E7 is unbroken. This is a consistent **restricted-branch** calculation, not enumeration of all Higgs branches.

`candidate_checks.py` executes a target-blind example `a=-1,b=0,kappa=1,m=2,y=1` in arbitrary fixed mass units: roots `S=-1,+1`, singlet mass squared 4 at both, charged mass squared 1 and 9. These numbers are **illustrative freely chosen inputs**, not E7 predictions, flux data or fitted alpha parameters. It also checks an explicit antisymmetric contraction vanishes for an identical commuting field but need not vanish for distinct fields. Its small matrix check illustrates tensor symmetry; the E7 existence statement comes from the full weight-character audit, not that matrix.

The scalar vacuum equation and both zero-energy minima survive **every** `c>0` at tree level: c multiplies neither the F-flat equation nor a nonzero D contribution on this branch. This is an analytic coefficient-independence statement, with three rational positive examples additionally checked. Quantum dynamics, running and possible nonperturbative lifting are not solved. Even if one restricted the action to a single vacuum, an independently prescribed gauge boundary coefficient would still be required. We stop this candidate's **parameter-free alpha prediction claim** here rather than fit c. Since the displayed vacua leave E7 unbroken, they do not even define a Standard Model electromagnetic U(1) matching problem.

## exp47 next finite result

The separately authored `vacuum_audit.py` uses an AST-level audit of the unchanged predicates and exact dynamic programming with small-domain brute-force cross-checks. It computes the full eight-entry sum/positive-entry distribution before applying the legacy acceptance target. The target condition plus sum divisibility forces sum 56; that value is therefore selected by the supplied target, not by stationary equations. `(7,7,7,7,7,7,7,7)` and `(6,8,7,7,7,7,7,7)` are explicit inequivalent-under-permutation accepted examples. Per-entry multiples of seven are a new premise absent from the implemented sum-divisibility predicate. See the dedicated report for complete histograms, differing G2/F-theory coupling ansatzes, missing stabilization equations and the bounded physical gate.

## Downstream independent observable: clocks, not a boundary-fixing premise

The parallel `../atomic-clock-gate/REPORT.md` supplies a separately executed clock-response audit (13 new Z3 checks, independently replayed by the parent). Its verified conditional results distinguish dimensionless frequency-ratio changes from an unknown static intercept: a nonzero known optical sensitivity difference can identify an alpha change, whereas zero drift does not fix a static boundary coupling. Nuclear/mass nuisances and a scalar-amplitude/coupling product can remain degenerate. Those checks are not rerun or counted as representation progress here.

This is a useful **downstream test opportunity**, not an extra equation selecting c. A genuine application first needs E7 breaking, electromagnetic embedding, matter/nuclear matching, a specified dynamical light field if variations are proposed, and calculated response coefficients with nuisance uncertainties. The current constant-gauge-kinetic, unbroken-E7 candidate supplies no map to actual atomic species or their transitions. Adding `f(S)` would be a new action choice with new coefficients, not a consequence of the representation repair. No clock precision, fixed SI frequency or equality involving 133 is used to fix a free coefficient or repair a residual.

## Local verification and reproducibility

Run from Windows Bash:

```
python -B C:/Users/mikeb/e7-alpha-theory/gap-investigation/next-gate/representation_checks.py
python -B C:/Users/mikeb/e7-alpha-theory/gap-investigation/next-gate/vacuum_audit.py
python -B C:/Users/mikeb/e7-alpha-theory/gap-investigation/next-gate/candidate_checks.py
```

The first two default commands load saved receipts before recomputing and compare deterministic results and source hashes. Missing receipts fail; initial generation is separately opt-in `--create` with exclusive creation. `run_checks.py` runs all three and records exit codes/output and next-gate artifact hashes in `verification.json`. No legacy source or history is modified. The old Lean/Z3 gate is not counted as new progress. Exact executable mathematics, tree-level action consistency, finite toy predicates and actual physical-vacuum claims remain separate. No hosted CI, publication, full Lean representation proof, full quantum vacuum solution, or measured-alpha fit is claimed.
