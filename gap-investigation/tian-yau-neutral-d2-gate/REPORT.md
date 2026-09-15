# Tian-Yau invariant neutral d2: exact rank 60

## Accepted result

For the canonical geometry and Euler/normal tangent monad, the character-zero map

`d2: E2^(-1,2)_0 -> E2^(1,1)_0`

is computed from actual total Cech/Koszul cocycles and primitives. Both spaces have dimension 60; the exact rational matrix has rank 60. `d2-invariant-matrix.json` records the complete dense and sparse matrix with source/target bases fixed by `partial-character-0.json`. `total-cech-lifts.json` records every Laurent monomial, Koszul wedge, tensor-cover intersection, and rational coefficient for all 60 source cocycles, primitives, and endpoints. No endpoint is assigned from a dimension or a generic-rank hypothesis.

The early `partial-*` and `curved-koszul-diagnostic.json` artifacts intentionally retain their stage-specific noncompletion flags. Likewise `total-cech-lifts.json` alone does not claim representative independence; the separate `representative-controls.json` discharges that gate. Only `receipt.json` combines these layers into the accepted invariant d2 result.

## Complex and filtered comparison

Let K=(A -> B -> C) have degrees -1,0,1. Its ambient polynomial differential d is curved, not square zero: `d^2 = sum_a f_a H_a`, where `H_a:A_b -> C_a` has the actual coefficient `degree(f_a)_b`. This is Euler's identity, checked symbolically. The earlier missing comparison cannot be supplied by simply treating ambient d as a differential.

Use the tensor standard affine Cech covers of P3 x P3 and the Koszul resolution on the three defining equations. A stored cochain key is `(Hom pair, Koszul subset I, Laurent exponent e, x intersection, y intersection)`. Put p=target K degree minus source degree, k=|I|, and q=total Cech degree. Its total degree is `p+q-k`. The executable total differential is

- `V = (-1)^(p+k) delta_Cech + kappa`, preserving p;
- `A = (-1)^k [d,-]_super`, increasing p by 1;
- `B = -sum_a epsilon_a wedge [H_a,-]`, increasing p by 2.

Here H_a has even End degree, so its commutator has no super sign. The identities are `V^2=0`, `VA+AV=0`, `A^2+VB+BV=0`, `AB+BA=0`, and `B^2=0`. The third identity uses the **nonzero** ambient curvature. The complete total differential is `V+A+B`, not merely a double complex with a falsely square-zero horizontal arrow.

Augmentation of the Koszul complex to O_X, with positive Koszul degree sent to zero, intertwines this total differential with the actual End(K|X) differential. Filter both complexes by End degree p. On each associated-graded column this is the Koszul resolution of the locally free ambient Hom summand restricted to X. Thus augmentation is a filtered quasi-isomorphism, using the same complete-intersection/regular-sequence premise as the canonical geometry gate. Its first page is exactly H^q(X,End^p K). This gives the required comparison to the geometric hypercohomology spectral sequence; it is not an identification based only on dimensions. The cover intersections are affine and the tensor-cover totalization computes sheaf cohomology.

## Actual lift and projection

`partial_chains.py` constructs H2 representatives directly, rather than obtaining a basis by dimension-only Serre duality. In character zero its H2 row is `16 -> 80 -> 4`, with d1 ranks 16 and 4. The H1 row is `4 -> 80 -> 16`, with ranks 4 and 16. Exact quotient complements give the source and target 60-dimensional E2 bases.

For each source column a, `total_cech.py` constructs all lower-Cech-degree corrections, then solves

`V a = 0`, `V u = -A a`.

The actual next endpoint is **computed** as `A u + B a`. It verifies `V(Au+Ba)=0`, computes its actual H1 Koszul quotient coordinates, checks d1 closure, and applies the saved E2 target projector. Full total-differential nilpotence is checked on each source and primitive. The ambient projected primitive is only the initial term of the total primitive, never substituted for the completed lift.

The Cech contraction chooses the first vertex outside the negative support. It uses the tensor homotopy `h_x tensor 1 + P_x tensor h_y` with its graded sign and the corresponding cohomology projector. Its identity is checked on all 160 one-factor support/intersection test cases in the two tensor positions, as well as on the actual source lifts. All arithmetic is rational (`Fraction` and SymPy Rational), with no numerical tolerance or float signs.

## Representative controls and negative controls

- All 16 H2 End^-2 basis classes are lifted; their actual incoming d1 boundaries have executable primitives and zero next endpoint.
- All 56 ambient-H3 Koszul source-boundary generators are tested through total V-boundaries. Their endpoint changes are explicitly V-exact and project to zero.
- All four nonexact H1 End^0 primitive ambiguities are lifted. Their nonzero endpoint changes lie in target d1 boundaries and project to zero.
- Four nonconstant Cech-exact representative changes are checked; arbitrary exact changes are covered by the verified operator identities `A V=-V A` and `A^2+B V=-V B`.
- Reversing the curvature-correction sign violates total nilpotence on all 60 source columns. This is a nontrivial sign control, not a test of a zero assignment.
- Wrong lift and projector mutations fail in the source/target construction. The final replay rejects a changed matrix entry and missing payload without touching saved artifacts.

## Associated-graded consequence, not a vacuum

This invariant d2 makes `E3^(-1,2)_0=0` and `E3^(1,1)_0=0`. The polynomial slot `(1,0)` remains its already established dimension 12. The invariant `(-2,3)` slot remains dimension 4; its d3 target `(1,1)` is now zero. Its remaining possible differential is

`d4: E4^(-2,3)_0 -> E4^(2,0)_0`, of shape 4 by 4.

Consequently `dim Ext1_0 = 12 + 4 - rank(d4_0)` and the remaining bounds are **12 to 16**, not an assertion that the answer is 16. The degree-zero source `(-2,2)` remains absent and is never added to Ext1. No higher differential on another character is inferred. Characters 1 and 2 remain at the canonical E2 ledger; no new matrix is claimed for them in this release.

There is no full neutral Yoneda tensor, Kuranishi result, full Higgs/F-flatness statement, exotic mass result, stable vacuum, coupling prediction, Lean-kernel proof, hosted-CI result, or independent expert-review claim.

## Replay

From this directory, run:

`C:/Python313/python.exe -B verify.py`

The verifier requires the existing receipt and all saved payloads, recomputes every stage, compares complete deterministic payloads without regeneration, checks hashes, reads the exact matrix back, and replays the canonical survivor-yoneda verification. Expect several minutes because complete Cech traces are regenerated in memory and compared to the saved artifact; no file is overwritten during replay. `--create` is exclusive initial issuance, not the acceptance command. The canonical predecessor directory is read-only and Python bytecode writes are disabled.

## Operational disclosure

File-tool writes initially landed in a shadow filesystem. Source text was delivered in bounded native-Python chunks to the canonical Windows tree and then executed with `C:/Python313/python.exe -B`. A negative-power Python sign initially introduced float arithmetic in the direct H2 constructor; it was corrected to exact SymPy integer powers before any partial certificate was issued. A source-boundary control initially required its exact endpoint to be nonzero; actual endpoints are zero for these generators, so the nonvacuity condition now checks that the source boundary is nonzero, while independent primitive/sign controls retain genuinely nonzero changes. No failed run was promoted.

