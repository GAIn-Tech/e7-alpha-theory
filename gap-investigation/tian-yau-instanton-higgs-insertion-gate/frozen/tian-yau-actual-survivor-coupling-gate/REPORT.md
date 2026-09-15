# Actual invariant neutral-survivor Yoneda tensor

## Outcome and scope

The four **actual total-degree-one** neutral survivors of the accepted d4 calculation have a **nonzero** invariant neutral–L–Lbar cubic tensor. This is not the obsolete degree-zero d3-source construction. The complete 4 x 9 x 6 tensor is derived through explicit total cocycles, End-on-tangent products, exact boundary primitives, dual-tangent cocycles and an invertible Serre pairing. All arithmetic is rational.

With **zero-based** indices in the saved bases, its only nonzero entries are

```
T[0,5,1] = -1
T[1,6,1] = -1
T[2,7,0] = -1
T[3,8,0] = -1.
```

The signs use the displayed scalar H3(O_X) generator as residue normalization and the order beta composed with alpha acting on c. This is an algebraic superpotential tensor, not a physically normalized Yukawa: the holomorphic-volume normalization, Kahler metrics and field rescalings have not been fixed. A common normalization does not change which entries vanish.

## Actual domains and bases

The tangent monad remains A in degree -1, B in degree 0, C in degree 1 on the same Fermat/bilinear member and free invariant Z3 quotient. The code constructs invariant ambient Laurent/Koszul cohomology quotients, not dimensions imported from a Hodge table. Its tangent E2 rows, ordered p=-1,0,1, are

| vertical q | E1 dimensions | E2 dimensions |
|---|---|---|
| 0 | 2,12,19 | 0,0,9 |
| 1 | 0,4,8 | 0,0,4 |
| 2 | 0,0,0 | 0,0,0 |
| 3 | 2,0,0 | 2,0,0 |

Thus H1(TX)_0 has the actual nine-dimensional terminal-C quotient basis. H2(TX)_0 has four terminal-C H1 quotient classes plus two explicitly lifted A H3 classes. The only possible higher arrows affecting these slots have zero target or lie outside the three-column strip. On the dual module the corresponding E2 rows are (0,0,2), (0,0,0), (4,0,0), (9,0,0); the six H1(TX*) classes are constructed, not merely called abstract dual coordinates.

The nine charged polynomial representatives, in order, are:

```
c0=(x3^3,0,0)       c1=(x2*x3^2,0,0)
c2=(x2^2*x3,0,0)    c3=(x2^3,0,0)
c4=(x1^3,0,0)       c5=(x0*x1*x3,0,0)
c6=(x0*x1*x2,0,0)   c7=(0,0,y0*y1*y3)
c8=(0,0,y0*y1*y2).
```

These are quotient representatives, so their appearance as monomials does not mean that normal-bundle relations or Jacobian images were ignored. Full basis, differential and quotient matrices are saved in `module-action.json`. The first two dual basis classes beta0,beta1 are the two global A* terminal generators. The other four dual classes have explicit nonpolynomial lifts in `serre-tensor.json`.

For the ordered H2 basis (four C classes, then two lifted A classes), the computed Serre matrix (dual basis labels on rows) is

```
 0  0  0  0 -1  0
 0  0  0  0  0 -1
-1  0  0  0  0  0
 0 -1  0  0  0  0
 0  0  1  0  0  0
 0  0  0  1  0  0
```

Its determinant is 1. The four nonzero module-coordinate entries before pairing are (0,5,5), (1,6,5), (2,7,4), (3,8,4), each +1. Every other product is accompanied by a genuine total boundary primitive; the nonzero products are accompanied by a primitive for the difference from their H2 representative. No product is defined by assigning a desired zero matrix.

## What happens to the e32/e33 Higgs alignment?

The predecessor `interactions.py` specifies **gauge matrices and two abstract flavor labels, not a map into geometric cohomology bases**. Therefore its original witness does not have a uniquely determined tensor contraction. This lane does not retrospectively identify those unnamed flavors.

Write the two geometric L flavor columns as l_{i,0}, l_{i,1}, multiplying e32,e33 respectively, and the dual flavor columns as b_{j,0}, b_{j,1}, multiplying e23,e33. Direct replay of the predecessor matrices gives the gauge trace pairing diag(1,1), with zero cross traces. The four new neutral F terms are exactly

```
F0 = -b1,0*l5,0 - b1,1*l5,1
F1 = -b1,0*l6,0 - b1,1*l6,1
F2 = -b0,0*l7,0 - b0,1*l7,1
F3 = -b0,0*l8,0 - b0,1*l8,1.
```

Two **new, explicitly identified geometric embeddings** of the same gauge pattern demonstrate the difference:

* L32=c0, L33=c1, Lbar23=beta0, Lbar33=beta1: all four F terms vanish.
* L32=c5, L33=c7, Lbar23=beta1, Lbar33=beta0: the unit-magnitude F vector is (-1,0,-1,0), so this embedding is obstructed at the tested cubic order.

The common kernel on the charged side of all four neutral action maps is exactly span(c0,...,c4), dimension five. Consequently the first construction is not an isolated cancellation dependent on a numerically fitted ratio.

The **four newly calculated conditions** must be distinguished from the **twelve inherited polynomial-neutral conditions**, whose tensor vanishes on the previously established polynomial subspace. Adopting that predecessor result, the first embedding clears the cubic F_S test for all sixteen invariant tangent-bundle neutral modes. It does not establish every neutral field's F equation, a Kahler-normalized simultaneous F/D vacuum, nonlinear bundle unobstructedness, all higher superpotential terms, exotic mass ranks, moduli stabilization or a physical coupling prediction. The visible ansatz is E6 standard embedding, not an E7 repair.

## Controls and evidence

* 58,230 keywise End-action Leibniz tests, covering every saved neutral support key against all nine charged cocycles.
* 7,546 detections of the deliberately unsigned wrong product.
* 48 charged-boundary action identities and 36 nontrivial neutral representative-change identities; 504 resulting scalar boundary residues vanish.
* 672 additional dual-side keywise Leibniz tests, plus 24 nontrivial dual exact-change pairing tests.
* All 36 saved product/cohomology-representative/primitive decompositions independently recomputed; explicit phase mutation rejected and wrong-curvature signs rejected on both lifted H2 classes.
* Nontrivial charged/dual basis shears checked against tensor covariance.
* Actual source, target and dual invariant quotient maps, localization admissibility, total degrees and curve/Koszul signs retained in executable data.

The terminal-C charged boundaries and Koszul vertical boundaries are kept separate. The total product obeys D(alpha*c)=(D alpha)*c+(-1)^|alpha| alpha*(Dc); for closed degree-one alpha the charged representative-change primitive is -alpha*b. Neutral and dual exact changes use actual degree-zero primitives, not prose placeholders.

## Replay and provenance

Run natively:

```
C:/Python313/python.exe -B C:/Users/mikeb/e7-alpha-theory/gap-investigation/tian-yau-actual-survivor-coupling-gate/verify.py
```

`verify.py` first requires the frozen manifest and saved receipts, checks source hashes, reexecutes all three calculations without `--create`, compares complete deterministic payloads, and checks that replay changed no frozen bytes. `native-replay-status.json` and `native-replay.log` are the local execution authority. Creation receipts alone are not immutable replay. No Lean-kernel, hosted-CI or peer-review claim is made.

The old interrupted task transcript ended immediately after loading the formal-proof skill; the canonical target lane had no files. A live process inventory found no identifiable calculation for this lane (two unrelated Python process command lines were inaccessible). No active calculation was duplicated. The accepted d4 chain and verifier hashes are pinned verbatim. Only this lane was written; predecessor files were read only.

Two operational problems are preserved rather than misclassified as mathematics: filesystem-tool writes initially landed in the documented Cygwin shadow tree and were copied to the native canonical lane before execution; one initial dual-boundary negative-control fixture chose a chart with zero contraction. Its source is retained as `final-controls-initial-failed.py`; choosing an actual top-Cech chart produces nonzero admissible exact perturbations and the full control passes. The successful module and Serre sources/receipts were not changed to repair that auxiliary test.
