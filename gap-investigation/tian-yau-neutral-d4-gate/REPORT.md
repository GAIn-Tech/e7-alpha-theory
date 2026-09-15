# Invariant neutral d4 gate

## Claim boundary
This lane computes the character-zero spectral-sequence differential of the declared Tian–Yau curved-End Koszul model, not a vacuum or a Yoneda tensor. Only an immutable `verify.py` exit-zero replay promotes the computed result. `computed-chains.json` is the initial exploratory calculation, not the release receipt.

## Result
The exact computation gives d4 = 0_(4x4), rank 0, determinant 0, kernel QQ^4 with the standard coordinate basis. All four fourth-horizontal endpoints vanish already as computed cochains, stronger than vanishing only in the target quotient. The invariant Ext1 associated-graded dimensions are 4 at (-2,3) and 12 at (1,0), hence invariant Ext1 dimension 16 for this declared model. This conclusion supersedes the previous bound only when the immutable replay passes.

## Construction
Use the predecessor tensor Čech differential `dc`, Koszul differential `kap`, End commutator `d1`, and curvature correction `d2cor`. With horizontal degree p and Koszul exterior degree k, the signed Čech differential is (-1)^(p+k) times the tensor-cover differential. The vertical differential is dv=dc+kap and D=dv+d1+d2cor.

The existing Čech contraction is extended to the Koszul totalization by the finite perturbation series

- i' = sum (-hc kap)^n i;
- pi' = pc sum (-kap hc)^n;
- H' = hc sum (-kap hc)^n.

The Koszul degree bounds make these sums terminate. Ambient cohomology lives in rows 0,3,6; a higher transferred row-jump would need four Koszul factors, while only three exist. Hence the transferred differential is the actual Laurent-monomial Koszul matrix, not an assumed cohomology map. Primitives use exact rational solves of those matrices and are checked back against dv at chain level.

The q=3 edge source is the computed kernel of d1 from p=-2 to -1. The q=0 target is the computed cokernel of d1 from p=1 to 2. No assigned 4-dimensional vector space replaces these constructions. Earlier middle-page groups are calculated from the saved exact q1/q2 matrices; the native predecessor d2 replay and its explicit inverse eliminate both 60-dimensional groups. This establishes the actual E4 source and target quotients. The polynomial Ext1 piece is recomputed as ker(d1 at p=1,q=0)/im(d1 at p=0,q=0).

For each source a0, solve dv a1=-d1 a0, dv a2=-d1 a1-d2cor a0, and dv a3=-d1 a2-d2cor a1. The fourth horizontal endpoint is d1 a3+d2cor a2. Every matrix column is the endpoint's computed cohomology coordinate in the computed target quotient. Endpoint matrices are assembled from these columns; an empty sparse list means computed cancellation, not an initialized answer.

For each zero endpoint class, additionally subtract its computed d1-boundary representative and solve its remaining vertical boundary. Save the resulting full D-closed degree-one cocycle, including any fourth vertical primitive, for subsequent Yoneda work. No tensor is synthesized here.

## Controls and interpretation
The replay checks lift equations, D-squared on every monomial key in the chains, the Čech contraction on those keys, total cocycle closure, source exact-boundary changes with the full filtered D-boundary extension, all target sheaf-cohomology d1-boundary generators, available vertical-boundary generators, wrong primitive signs, wrong curvature signs, and tampered saved matrix payloads. It recomputes rank, determinant and kernel over QQ. Representative changes by exact total boundaries preserve the total classes by D-squared=0; remaining intermediate cohomology ambiguities are governed by the verified earlier pages, rather than being silently treated as zero cochains.

The Ext1 diagonal is p+q=1. After middle-page elimination, its only slots are (-2,3) and (1,0). Their dimensions are respectively ker(d4) and the polynomial quotient dimension. Higher differentials cannot occur beyond the bounded horizontal strip -2<=p<=2. The replay is the authority for the numerical sum.

Canonical replay:

`C:/Python313/python.exe -B C:/Users/mikeb/e7-alpha-theory/gap-investigation/tian-yau-neutral-d4-gate/verify.py`

Creation uses `--create` with exclusive file creation; normal replay requires saved artifacts first and does not regenerate them before comparison. Native paths avoid a discovered shadow-tree hazard in Windows-style paths passed to filesystem tools. Predecessor artifacts are read-only and hashed. This is an exact computational certificate, not a Lean-kernel formalization or independent peer review.
