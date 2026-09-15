# Kernel-checked odd cubic obstruction

## New result

`CubicGate.invariant_odd_trilinear_vanishes` proves that a separately additive map on three odd input spaces, invariant under their simultaneous sign transformation and valued in a target without additive 2-torsion, is zero at every triple. This is a new obstruction theorem, not any of the earlier `Gap.lean` coefficient-postcomposition or injectivity bridges.

The proof derives, rather than assumes, the crucial identity:

    T(-x,-y,-z) = -T(x,y,z).

Separate additivity first forces T to preserve zero and negatives in each slot (using additive cancellation and inverse laws). Three negative signs then leave one negative sign. Invariance gives T(x,y,z) = -T(x,y,z); adding T(x,y,z) gives twice that value equal to zero, and the no-2-torsion premise forces the value to vanish. There is no premise named “no cubic”, nor an assumed sign law for T.

## Exact formal scope

This is a `prelude` Lean 4.32.1 kernel-only additive analogue. `AddCore` explicitly supplies zero, addition, negation, right-zero, both inverse laws and left cancellation. Every additive group supplies these laws; associativity and commutativity are not needed in the argument. `NoTwoTorsion` means q+q=0 implies q=0. For vector spaces over fields of characteristic other than two this condition is standard, but that field/vector-space implication is NOT formalized here. “Characteristic not two” for an arbitrary ring alone is not sufficient; the precise hypothesis here avoids that overclaim.

`Eqv` is an inductively defined reflexive equality with its own eliminator, symmetry, transitivity and congruence, not an arbitrary relation. The statement is pointwise vanishing, so function extensionality is unnecessary. No standard Lean algebra or Mathlib was imported: the inspected partial distribution has no `lib/lean/Init.olean`. The two empty inductive declarations `lcAny` and `lcErased` supply names required by this bootstrap compiler when processing data constructors; they are not assumed inhabitants, mathematical axioms or proof premises. Definitions are noncomputable and no VM/native evaluation is trusted for proofs.

The transformations sA,sB,sC are explicitly required to equal negation. In an additive group they therefore square to the identity. A group, its center, representations, tensor products, scalar linearity and representation integration have not been constructed in Lean. Centrality is not needed by this local algebraic implication: invariance under that one transformation suffices. No assumption that an entire group action exists is hidden in the proof.

## Nonvacuity and sharp boundary, also checked by Lean

`Examples.lean.part` constructs explicit finite additive cores with three and two distinct constructors, addition and multiplication tables modulo three/two, and complete recursor proofs of the required laws. The Python generator only writes proof terms; Lean checks every branch.

* Over the three-element core, `noTwo3` proves the no-2-torsion hypothesis. `zero3_gate` actually instantiates the main theorem on three nontrivial input spaces; its zero tensor satisfies all premises.
* The nonzero cubic xyz on this same core is separately additive (`linearA3/B3/C3`), but `cubic3_not_invariant` proves that simultaneous odd-sign invariance fails. Thus the map class is not identically zero before the invariance condition.
* Over the two-element core, xyz is separately additive, invariant under negation, and nonzero. `characteristic_two_fails` proves that no-2-torsion cannot hold there. This is a kernel-checked counterexample to dropping the torsion hypothesis, not merely a Python enumeration.

## Bridge to the existing E7 exact computation

Read-only predecessor: `../next-gate/representation_checks.py`, `representation-receipt.json`, and `REPORT.md`. Its audited Weyl-weight calculation finds zero weight multiplicity zero in the full tensor cube of 56 and simple-root coordinates of omega7 `(1,3/2,2,3,5/2,2,3/2)`, giving a nontrivial order-two root-lattice class. The local verifier replays that saved receipt (including its source hashes) without regenerating it.

The new Lean theorem formalizes the algebraic obstruction underlying the odd-class conclusion, **not** the E7 data themselves. To instantiate it for the simply connected complex or compact E7 fundamental 56, independent representation theory must identify a central order-two element acting as minus identity on 56, with trivial action on the scalar target, and translate an invariant scalar trilinear form into the separate additivity and invariance premises. The weight/root-lattice-to-central-character correspondence and the actual E7 center action remain outside the kernel. The predecessor exact character calculation is independent evidence, not a Lean import or an axiom magically discharged by its JSON receipt.

No claim is made that the symmetric/exterior-square decompositions, Weyl character theory, absence of zero weights or absence of tensor singlets have now been completely formalized in Lean. The formalized result applies to scalar trilinear forms; relating invariant tensors to these forms needs the usual finite-dimensional duality/representation arguments. Symmetry of the form is not required, and the three odd spaces may be different. It does not obstruct an even-even-even cubic, a two-odd-one-even interaction, quartics, or an interaction with a nontrivially transforming target. It does not select a coupling or solve the physical E7 theory.

## Reproduction

    python -B C:/Users/mikeb/e7-alpha-theory/gap-investigation/lean-cubic-gate/verify.py

The verifier compiles `Checked.lean` (exact concatenation of `Cubic.lean` and `Examples.lean.part`), checks all 18 requested axiom reports, rejects placeholder/axiom declarations, regenerates finite proofs in a temporary directory for byte comparison, and replays the existing representation receipt. `verification.json` stores real output, executable version and source hashes. This is a local verification, not hosted CI or independent expert review. AI-assisted authorship; Lean kernel checking and exact receipt replay are the evidence.

Only this new lane was written. The filesystem tools initially wrote a Cygwin shadow path despite reporting a canonical path; canonical Windows Python reads/copies and actual Lean execution corrected the delivery. No predecessor, embedding lane, legacy physics source, or publication was modified.
