# Tian–Yau tangent-bundle coupling gate

## Verdict

For the actual Fermat/bilinear threefold in `P3_x × P3_y` and its free diagonal `Z3`, the tangent bundle is the cohomology of the equivariant monad

`0 → O_X^2 --E--> O_X(1,0)^4 ⊕ O_X(0,1)^4 --J--> O_X(3,0) ⊕ O_X(1,1) ⊕ O_X(0,3) → 0`,

where `E` is the two Euler maps and `J=(∂p_a/∂z_i)`. Exact reduction gives `J E = [[3p1,0],[p2,p2],[0,3p3]] = 0` in the defining ideal. The maps have the required `Z3` phases. The exact polynomial deformation complex has characterwise presentation quotients `(12,14,14)`. Hence the quotient has a **12-dimensional invariant polynomial tangent-bundle deformation subspace**.

For all twelve invariant classes represented by fixed-`E` perturbations, the concrete Yoneda/cup map

`Ext1(TX,TX) × H1(TX) → H2(TX)`

vanishes on all terminal normal-bundle representatives. Its Serre pairing therefore gives an exact zero `12 × 9 × 6` neutral–`L`–`Lbar` mass tensor on this computed subspace. Thus these twelve neutral directions do **not** obstruct the predecessor's `e32,e33` two-pair alignment through `F_S` at cubic order. This does not prove full neutral F-flatness: the calculation does not establish that the polynomial subspace exhausts `H1(End TX)`.

The minimal unresolved component is explicit: the endomorphism hypercohomology has a possible incoming `d3` source from the off-diagonal `H2(Hom(C_x,A_y)) ⊕ H2(Hom(C_y,A_x))` sector. Its 12 mixed-quadratic representatives have characters `(4,4,4)`. Computing this differential—and any surviving classes' action on charged cohomology—is required before accepting or rejecting the two-pair branch.

## Exact geometry and assumptions

Coordinates and weights are

`g: (x0,x1,x2,x3;y0,y1,y2,y3) ↦ (x0,ω²x1,ωx2,ωx3;y0,ωy1,ω²y2,ω²y3)`.

All three defining equations are invariant and the residue-form phase is zero. Smoothness of the cover is checked by exhausting the 15 possible common supports in the Lagrange-multiplier equations: on a support of size `m`, the Fermat equation forces `m c=0` while projectivity forces `c≠0`; exact Gröbner bases are `[1]` for `m=1..4`. Freeness reduces on the sole positive-dimensional fixed stratum to `r³=t³=-1, rt+1=0`; its Gröbner basis is `[1]`. These checks establish the assumptions needed for exact normal/Euler sequences for this member. They are algebraic checks over characteristic zero, not numerical sampling.

## Cohomology boundary

The same finite polynomial quotient independently reproduces `H1(TX)` characters `(9,7,7)`. A line-bundle/Koszul connecting-map calculation gives `H2(TX)` characters `(6,4,4)`, matching the predecessor. The neutral result is deliberately named a **polynomial monad-map subspace**. Hypercohomology convergence is standard, but higher differentials were not assumed zero. Infinitesimal classes were not called an actual unobstructed branch: quadratic Kuranishi obstructions in `H2(End TX)` remain uncomputed.

A zero tensor here is stronger than a Wilson selection rule: invariant couplings are symmetry-allowed, but the constructed Yoneda map itself vanishes on this subspace. It is not evidence that every allowed tensor is nonzero—or zero.

## Sources and code search

* Butbaia et al., arXiv:2401.15078, eqs. 4.7–4.11 and Table 2: geometry/action and nine invariant `H1(TX)` modes. The paper studies `(27)^3` Yukawas, not `H1(End TX)·27·27bar`.
* Candelas et al., arXiv:0706.3134, §2.1: generic freeness, quotient Hodge numbers `(6,9)`, and nine polynomial complex-structure parameters.
* `Justin-Tan/cymyc`, pinned commit `2039ea4349247317352e59d673444ad3865387fe`: searched before implementation. Its Tian–Yau scripts supply the 23 mode polynomial basis and numerical harmonic/Yukawa workflow, but no tangent-bundle-modulus/charged-pair tensor implementation. Pinned source files and tree are retained under `sources/`.
* Stacks Project tag 015J: bounded hypercohomology spectral sequences converge with finite filtrations; this justifies retaining, rather than silently deleting, the possible higher differential.
* Anderson et al., arXiv:2103.10454: heterotic Yukawa cup products can vanish for geometric/cohomological reasons; symmetry allowance alone is insufficient.

Exact hashes are embedded in `certificate.json`, including predecessor source evidence and all pinned source files.

## Replay

From this directory with native Windows Python:

```
C:/Python313/python.exe -B exact_certificate.py
C:/Python313/python.exe -B verify.py
```

`verify.py` replays both predecessor gates, checks this immutable certificate, tests missing/tampered/exclusive-create controls, and compiles the two Lean theorems with no axioms. Local verification only; no hosted CI or independent expert review.
