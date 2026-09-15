# Nonlinear Kahler persistence of the known Tian–Yau Higgs branch

## Outcome

**Arbitrary regular analytic gauge-invariant positive Kahler corrections preserve nearby D-flat representatives of the verified small known-cubic branch.** This is a conditional local mathematical result, not a computation of the actual CY Kahler potential or a compactification vacuum. The conditions, stabilizer and small-amplitude limit are explicit below. Unknown neutral F terms and higher superpotentials remain potential obstructions.

The exact full orbit Jacobian has rank twelve, with four stabilizer zero modes. A four-dimensional centralizer slice has canonical Jacobian diag(32,8,8,8). Dividing the moment map by amplitude squared before applying the implicit-function theorem removes the origin degeneracy. A genuinely nonlinear quartic invariant example is solved exactly on the same complex orbit; equal raw conjugate norms fail for that example.

## 1. Retained inputs and FI audit

Read the geometry report `../heterotic-e6-three-family-gate/REPORT.md`, group/anomaly report `../tian-yau-wilson-line-gate/REPORT.md`, and complete `../tian-yau-flavor-higgs-consistency-gate/REPORT.md` and `calculate.py`. The executable verifies every hash in the flavor-Higgs release manifest and reads its saved tensor/rank data; it does not recompute the expensive cohomology chain. The superseded assigned-zero d3 calculation is not used.

The model remains the smooth Fermat/bilinear (3,0),(1,1),(0,3) complete intersection in P3 x P3, free diagonal Z3 quotient and tangent SU3 standard embedding in visible E8, with trivial hidden E8 bundle. This is the E6 route, not an E7 repair. The Wilson line leaves `(SU3_C x SU3_L x SU3_R)/Z3_diag`. The Higgs flavors are precisely c0,c1 and beta0,beta1 of the predecessor. In one-based gauge indices the canonical point is

```
L0=e32, L1=e33; B0=e23, B1=e33;
all other charged fields and sixteen bundle neutrals zero.
```

For an arbitrary positive quadratic flavor metric use the predecessor's adjusted invertible dual-column matrix U, not an assumed canonical cohomology basis. Denote that quadratic D-zero vector by v. Its compact stabilizer H in SU3_L x SU3_R has algebra su2 on L indices 1,2 and Y, with

```
6Y_L=diag(-1,-1,2), 6Y_R=diag(-4,2,2).
```

A constant equivariant moment-map shift is an invariant functional on the parent algebra. Invariance makes it annihilate all commutators; semisimplicity gives `[g,g]=g`, so it is zero. The finite diagonal quotient adds no continuous central generator. Neither visible trinification nor hidden e8 has a U1 factor. **No independent FI coefficient is allowed by this declared parent group.**

This also checks the anomalous-U1/axion issue rather than silently fixing a modulus. The retained spectrum has vanishing linear and cubic Cartan trace tensors, as calculated in the Wilson-line predecessor. Internal curvature at the standard embedding lies in holonomy su3, orthogonal to the e6 commutant under the E8 invariant form. Explicitly B([a,b],x)=B(a,[b,x])=0 for a,b in holonomy su3 and x commuting with it; su3 is perfect. Thus the internal B-field shift proportional to Tr(lambda F_internal) has no visible-commutant component. The flat Wilson connection adds no real internal curvature to this contraction. Discrete torsion is not a continuous FI coefficient. An independent additive shift of a gauge-singlet modulus would be a homomorphism from a perfect algebra to abelian translations and is zero.

These statements concern the given standard embedding and ordinary local field representation. A changed bundle, gauged R symmetry, additional anomalous U1 or genuinely charged/shifting modulus requires a new full moment-map analysis; it cannot be frozen away. No all-orders global anomaly proof is claimed.

The emergent unbroken Y is a generator inside the original semisimple algebra, not a newly added U1 with free FI level. On the H-fixed locus its vector field is zero and the inherited moment component mu_Y is identically zero. Integrating out heavy fields must match the parent D equation; appending an independent low-energy FI constant changes the problem. A useful hypothesis-drop obstruction is a genuinely added U1 that fixes every field on the trial orbit but has level xi!=0: D=xi there, so no representative exists. This is not a feature established for Tian–Yau.

## 2. Conditional local theorem

Fix neutral parameters m at a regular parent-gauge-invariant point, retaining all relevant light charged fields as local holomorphic linear-representation coordinates z. Assume:

1. K(m,z,zbar) is real analytic, real, compact-parent-gauge invariant and strictly plurisubharmonic near z=0. Its moment map is the inherited zero-level map in a gauge-invariant local Kahler gauge; no shifting coordinate or gauged Kahler character was suppressed.
2. K=K0+K2+R, with K2 a positive Hermitian gauge-invariant charged form and R of charged degree at least three, after separating harmless holomorphic plus antiholomorphic quadratic terms. Invariant holomorphic terms of any degree contribute no D term. Neutral dependence is permitted.
3. v is the predecessor's K2-D-zero vector for that metric with both charged row directions and both dual column directions spanning the R indices 2,3 block. Its compact stabilizer is H and complex stabilizer H_C. In particular the predecessor U is invertible.
4. To conclude F as well as D: the holomorphic equations under consideration define a complex-gauge-invariant locus containing t v. This is established only for the available massless cubic equations, not the unknown full compactification equations.

Then, for all sufficiently small real nonzero t, an H-commuting complex gauge transformation exp(A(t)) exists with A(t) Hermitian and tending to zero such that

```
z(t)=t exp(A(t)).v,      mu_K(z(t))=0.
```

It is on the same complex orbit as t v, leaves gauge-singlet neutral backgrounds unchanged, preserves the F equations of premise 4, and retains exactly H as compact stabilizer (plus color). A(t) is locally unique in a specified four-real-dimensional centralizer gauge; this is not isolation of moduli or of all D-zero points.

Generally A=O(t), hence z-tv=O(t^2). If the first D-active correction has degree d>=4, A=O(t^(d-2)) and z-tv=O(t^(d-1)). Quartic corrections therefore give an O(t^2) gauge displacement. The neighborhood and constants depend on actual coefficients and the positive metric: no physical radius is supplied.

### Proof with the zero modes retained

Use Hermitian generators T and convention `mu_T=K_i (T.z)^i`, equal to one half the derivative of K along exp(sT). Compact invariance makes it real. Overall sign/gauge coupling does not affect its zero set. Complex-orbit convexity and moment-map zeros have standard Kempf–Ness context.[1] Here only a direct local calculation is used, not a global stability/properness theorem.

At quadratic D-zero v the orbit derivative is

```
J(T,S)=2 Re <T.v,S.v>_K2.
```

Thus its kernel is exactly h, by positivity of K2, for every allowed predecessor metric. At t v this is t^2 J, and at t=0 it is zero. Applying the usual inverse-function theorem to the unscaled origin Jacobian would be invalid.

Instead use the centralizer C_G(H). Its Hermitian algebra c consists of L=diag(a,a,-2a) and an R block preserving index 1 versus indices 2,3; it has dimension five. Its intersection with h is span(Y). A complement to this one-dimensional kernel is

```
C0=(diag(1,1,-2),0),
C1=(0,E23+E32),
C2=(0,i(E32-E23)),
C3=(0,diag(0,1,-1)).
```

They commute with H; no orthogonality to Y is needed. If A is in their real span, t exp(A).v is H-fixed. Equivariance puts mu, identified using an invariant positive inner product, in c. Furthermore mu_h=0 identically because h.z=0 in the derivative formula, with no FI. Since c is spanned by these four Cj and Y, the four Cj equations force the whole moment map to zero. The other components are exact identities, not discarded equations. Untouched color similarly acts trivially.

For t!=0 define F_j(t,A)=t^(-2) mu_Cj(t exp(A).v). The charged Taylor expansion extends F real analytically to t=0: the lowest D-active degree is two. At (0,0), F=0 and its A derivative is J restricted to the four-dimensional complement. This restriction is positive definite: a generator in the complement killing v would be in h, whose intersection with that complement is zero.

The finite-dimensional real analytic implicit-function theorem now gives A(t). This standard analytic theorem is an external mathematical ingredient, not Lean-formalized here. Existence and uniqueness can also be obtained directly by writing F=J_c A+E and iterating A -> -J_c^(-1)E(t,A). Continuity of d_A E gives contraction norm below 1/2 on a sufficiently small neighborhood; E(t,0)=O(t) makes a ball of radius proportional to |t| invariant. The first nonzero correction degree gives the refined estimate stated above. This shows explicitly why no uniform inverse of t^2 J was assumed.

Because exp(A) commutes with H, the conjugated complex stabilizer remains H_C; intersecting with the compact group gives H. Holomorphic gauge invariance makes the critical locus invariant under the complexified connected group. Therefore all already-verified F derivatives, including ones normal to the original field support, remain zero. This does not infer any unknown F equation.

## 3. Exact executable Jacobian

`calculate.py` constructs all sixteen Hermitian su3_L+su3_R generators, including both directions of every off-diagonal root pair, and acts on all four nonzero matrices. It computes the full tangent matrix T, J=2 Re(T^dagger T), exact rank, kernel and slice restriction. Results in its stated normalization:

* rank 12, nullity 4;
* kernel S12_L, A12_L, H1_L and 6Y;
* characteristic polynomial `lambda^4 (lambda-12) (lambda-8)^7 (lambda-4)^4`;
* slice matrix diag(32,8,8,8), determinant 16384.

Every nonzero eigenvalue scales by t^2. These are orbit Jacobian eigenvalues, not physical scalar masses. The saved certificate includes the full matrices and kernel coordinates. The canonical example tests the abstract positive-metric kernel proof; it does not physically normalize geometric cohomology coordinates.

## 4. Solved nonlinear invariant family

Take an explicitly diagnostic EFT family, not assigned CY data:

```
x=sum_i Tr(L_i^dagger L_i), y=sum_j Tr(B_j^dagger B_j),
K=x+y+lambda x^2 + canonical norms of other charged fields,
lambda>=0 arbitrary.
```

This is a genuinely allowed gauge-invariant quartic correction, not just a function of total norm that trivially preserves conjugate cancellation. The L metric eigenvalues are 1+2lambda x transverse to L and 1+4lambda x radially; the B metric is identity. Hence positivity is explicit.

The full moment matrices are `(1+2lambda x) sum L Ldag - sum Bdag B` and `-(1+2lambda x) sum Ldag L + sum B Bdag`. For any a>0 their exact solution is

```
L0=a e32, L1=a e33,
B0=a sqrt(1+4lambda a^2) e23,
B1=a sqrt(1+4lambda a^2) e33.
```

Both unprojected matrices vanish symbolically. The known F terms remain zero. This solution is on the same complex orbit as t times the quadratic canonical vector, where

```
t^2=a^2 sqrt(1+4lambda a^2),
r^2=(1+4lambda a^2)^(-1/2), L=t r Lbase, B=t/r Bbase.
```

The transformation is SL3_L diag(r^(-1/2),r^(-1/2),r), with R identity; no extra U1 or changed holomorphic invariant was introduced. For each prescribed t>0 a is unique because a^2 sqrt(1+4lambda a^2) is strictly increasing from zero to infinity. Equivalently z=r^2 is the unique positive root

```
z^2+4lambda t^2 z^3=1,
partial_z=2z+12lambda t^2 z^2>0.
```

This exact positive algebraic parametrization solves D without selecting an arbitrary cubic-root branch. Near zero z=1-2lambda t^2+O(t^4), agreeing with the theorem. No VEV amplitude is stabilized or selected. The program's lambda=1,a=1 substitution is an exact mathematical control only, not a physical parameter choice.

Negative control: retaining equal raw norms gives mu_L=diag(0,0,8lambda t^4), mu_R=diag(0,-4lambda t^4,-4lambda t^4); traceless projections are nonzero for lambda,t>0. Thus the old representative generally must move even though existence persists.

## 5. What remains physically unproved

The semisimple FI restriction and local mathematical persistence are stronger than the earlier quadratic-only gate. However, real analyticity/regularity of the actual charged Wilsonian K near this CY branch has **not been computed or proved**. Smooth Ricci-flat internal geometry alone does not prove that full four-dimensional field-dependent expansion. Positive kinetic metrics at a regular point are the usual Hodge/kinetic expectation and the theorem accepts any such matrix, not a derived numerical matrix. No physical Kahler or Wilson coefficient was fitted or assigned.

Retain all light fields: a 1PI effective action or integration of fields becoming massless at t=0 can generate logs/singularities, outside the analytic premises. Degenerate kinetic forms and singular moduli limits are also outside them. No coefficient-independent numerical neighborhood, all-orders string background, or scalar Hessian is claimed.

The four actual neutral entries are T[12,5,1]=-1, T[13,6,1]=-1, T[14,7,0]=-1, T[15,8,0]=-1; c0,c1 lie in the common kernel. This proves no additional neutral equations. Other-neutral X L B couplings, higher W, nonzero backgrounds or W0 may lift the branch. For the pure known cubic truncation W=0, so changing K does not change the already-zero supergravity covariant F derivatives; with W0, terms K_i W0 require a new calculation. Moduli stabilization, exotic masses, stability and alpha prediction remain open.

## 6. Reproduction and formal scope

Run `C:/Python313/python.exe -B C:/Users/mikeb/e7-alpha-theory/gap-investigation/tian-yau-nonlinear-dflat-gate/calculate.py`. Default replay requires the saved certificate and compares its entire deterministic payload including source/predecessor hashes. Creation is exclusive via --create. Local exact SymPy is the executable verification layer. The analytic theorem is a written proof, not Lean-kernel checked or peer reviewed. The supplied incomplete Mathlib stack does not make a useful analytic formalization feasible without installation; no arithmetic-only Lean placeholder was added.

Only this lane is changed. The file tool initially wrote into the known Cygwin shadow despite reporting a canonical-looking resolved path; new lane files were copied to the native directory before execution. No predecessor source was modified, no nested delegation used, and nothing published.

## Sources

[1] https://www.numdam.org/item/10.5802/ccirm.4.pdf — Chris Woodward, Moment maps and geometric invariant theory
