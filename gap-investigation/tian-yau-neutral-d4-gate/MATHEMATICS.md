# Chain identities, page survival, and representative independence

This is a mathematical explanation of the executable certificate, not a Lean-kernel proof.

## Why the total operator is a differential

Let L be the ambient three-term monad, with differential d_L. Its square is the actual curvature R=Σ f_i H_i, where H_i:A→C has coefficients given by the multidegrees. On End(L), the graded commutator δ satisfies δ²=[R,-]. The Koszul contraction κ satisfies κ²=0. The added horizontal-degree-two term is the signed exterior multiplication operator implementing -Σ ε_i[H_i,-]; the predecessor code spells out its signs for every source/target pair.

Its anticommutator with κ is -[Σ f_i H_i,-], cancelling δ². The mixed End/curvature relation follows from d_L H_i=H_i d_L=0: these compositions would cross beyond the three-term monad. The square of the curvature correction vanishes because the H_i commute (indeed all H_i H_j=0) and the ε_i anticommute. The signed tensor Čech operator anticommutes with all other terms and squares to zero. Hence D²=0 algebraically, for arbitrary admissible Laurent cochains, not only the chosen representatives. The executable gate additionally checks the implemented identity individually on all 6470 keys appearing in the solved chains.

## Actual E4 groups

The computed edge d1 maps have shapes 64×38 on q=3 and 38×64 on q=0, both rank 34. Thus the source kernel and target cokernel each have dimension four. The target quotient is by the actual column space of the q=0 map, not by a named four-dimensional placeholder.

The saved middle-row matrices are replayed and give:

- q=2, p=-2,-1,0: E2 dimensions 0,60,0;
- q=1, p=0,1,2: E2 dimensions 0,60,0.

The native predecessor d2 replay computes the invertible 60×60 map from (-1,2) to (1,1), and its saved inverse is checked again here. Therefore both middle groups disappear on E3.

The source (-2,3) has no incoming arrow. Its possible d2 target (0,2) is zero already on E2; its d3 target (1,1) is zero on E3. The target (2,0) has possible incoming d2 source (0,1), zero on E2, and d3 source (-1,2), zero on E3. Consequently the computed four-dimensional edge groups really are E4, and no earlier uncomputed boundary quotient has been omitted.

## Primitives and representative changes

For each source, all three primitive equations and the fourth horizontal endpoint are computed in the full Čech/Koszul/End complex. Every endpoint cancels to zero as a cochain before projection. Each source therefore extends to an explicitly saved D-closed total-degree-one cocycle. These classes are linearly independent because their leading E1 classes form the computed source kernel basis.

For an exact source change dv η, extend all later components by the corresponding filtered components of Dη. The change in the full cocycle is Dη and D²η=0. The gate executes a nontrivial admissible, same-character version of this change for each source. It also checks all 64 actual sheaf-H0 generators of incoming target d1 boundaries and all six ambient polynomial Koszul generators of vertical target boundaries. These are representative tests of the implementations of the general boundary identities, not a claim to enumerate an infinite Čech cochain space.

Intermediate primitive choices are governed by the standard filtered-complex construction of d_r: changing them can alter the endpoint only by the earlier-page ambiguity subspaces. Here those are exactly the groups and boundary quotients just computed. In particular, possible p=-1,q=2 ambiguity is not silently discarded: its E2 class is removed by the verified invertible d2. Thus it cannot furnish an additional E3 source for a d3 boundary in the target. Exact source changes and target changes remain distinct from this page-survival argument.

## Rank and abutment

The first exploratory computation assembled the endpoint columns without any zero-rank assertion and obtained the zero 4×4 matrix. The release verifier derives those columns again and checks this independently observed equality. No endpoint is assigned a desired value. All four complete total cocycles are retained in `d4-chains.json` for later Yoneda calculation.

The unshifted Ext1 diagonal is p+q=1. Its only nonzero surviving groups are (-2,3), dimension ker(d4)=4, and (1,0), dimension 12 from the separately recomputed q=0 kernel/image quotient. The other diagonal groups vanish on E2 or E3. Incoming higher arrows to (1,0) have zero source or lie outside the horizontal strip. Once d4 is settled, r≥5 cannot fit in -2≤p≤2. Hence dim Ext1_invariant=12+4=16 for this declared model. This is not a nonlinear unobstructedness, F-flatness, vacuum, or Yukawa/Yoneda-tensor statement.
