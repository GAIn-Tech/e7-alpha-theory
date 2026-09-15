# Tian–Yau worldsheet-instanton gate

## Verdict

For the explicit Fermat/bilinear Tian–Yau cover

\[
X=\{\sum x_i^3=0,\ \sum x_i y_i=0,\ \sum y_i^3=0\}\subset\mathbf P^3_x\times\mathbf P^3_y
\]

with the free diagonal `Z3` action used by Butbaia et al., the low-bidegree search is exact:

| bidegree | cover | quotient orbits | status |
|---|---:|---:|---|
| `(1,0)` | 81 | 27 | isolated, `N=O(-1)⊕O(-1)` |
| `(0,1)` | 81 | 27 | isolated, `N=O(-1)⊕O(-1)` |
| `(1,1)` | 567 | 189 | isolated, `N=O(-1)⊕O(-1)` |

There are no positive-dimensional `(1,1)` families in this member. Another 162 ordered pairs of Fermat lines give rank-one bilinear pairing and no `(1,1)` map.

Every actual isolated curve has **zero Witten Pfaffian for the retained standard embedding `V=TQ`**. Therefore the degree-one and degree-two worldsheet-superpotential sectors vanish term by term, before any quotient phase sum. No determinant magnitude is assigned. More strongly, the same tangent-sequence argument applies to every smooth isolated rational curve in a Calabi–Yau threefold with `V=TQ`; increasing degree cannot produce a nonzero ordinary isolated-genus-zero Pfaffian without changing the bundle/mechanism.

## Exact curve construction

A Fermat cubic surface contains the 27 lines

`x_i=-ζ^a x_j, x_k=-ζ^b x_l`,

where the coordinates are partitioned into two pairs (three choices) and `a,b∈Z/3`. For `(1,0)`, fixing such a line forces `y` into its annihilator `P1`. The restricted second Fermat cubic is, after a nonzero scalar and affine coordinate choice, `u^3+1`. Its Gröbner basis is `[u^3+1]` and

`Res(u^3+1,3u^2)=27≠0`,

so it gives three reduced points for each of 27 lines: 81 isolated curves. The `(0,1)` result is symmetric.

For `(1,1)`, choose Fermat lines with two-dimensional vector spaces `U,V` and let `M=U^T V` be the exact bilinear-pairing matrix over `Q(ζ)`, `ζ²+ζ+1=0`. A bidegree `(1,1)` graph is an invertible map `A:U→V`; the bilinear equation is precisely that `MA` is skew. Exact linear Gröbner elimination has:

* `rank(M)=2`: one projective solution `A=M^{-1}J`, hence one curve;
* `rank(M)=1`: no invertible solution;
* `rank(M)=0`: a `PGL2` family.

Exhausting all `27²=729` ordered line pairs gives ranks `(0,1,2)=(0,162,567)`. Thus 567 isolated curves and no families occur.

## Isolation and normal bundles

For a `(1,0)` curve in `S_x×S_y`,

`N_{C/(S_x×S_y)}=O(-1)⊕O⊕O`,

and the `(1,1)` divisor differential maps this to `O(1)`. The nonzero resultant makes the induced map on global sections an isomorphism. Its kernel has rank two, degree `-2`, and no sections, hence is `O(-1)⊕O(-1)`. The `(0,1)` case is symmetric.

For `(1,1)`, the graph has

`N_{C/(S_x×S_y)}=O(2)⊕O(-1)⊕O(-1)`

and the divisor differential maps to `O(2)`. The exact rank-two `M` solution is reduced and isolated, so the kernel has rank two, degree `-2`, and `H0=0`; therefore it is again `O(-1)⊕O(-1)`. Rank-one cases have no invertible graph, while rank zero—absent here—would have produced a family.

## Tangent restriction and Pfaffian

For every listed curve,

`0→TC=O(2)→TX|C→N_{C/X}=O(-1)²→0`.

The extension splits because

`Ext¹(O(-1),O(2))=H¹(O(3))=0`.

Consequently

`TX|C=O(2)⊕O(-1)⊕O(-1)`

and

`H0(C, TX|C⊗O(-1)) = H0(O(1))`,

which has dimension two. Witten’s criterion says the chiral determinant/Pfaffian vanishes when this space has zero modes.[2] Since `TX=π* TQ` on the étale cover, the conclusion is unchanged after descent. This establishes zero, not a numerical determinant.

## Quotient orbits, phases, and the superpotential

The certificate applies the exact coordinate weights `(0,2,1,1;0,1,2,2)` over `Q(ζ)` to every curve witness. All orbits have length three, producing 27, 27, and 189 quotient curves respectively. This also follows geometrically: a setwise invariant rational curve would carry an order-three automorphism of `P1`, which has fixed points, contradicting freeness on `X`.

Along `J=t(h+k)`, the cover/downstairs bidegrees give `q=d_x+d_y`. The only possible exponent structures in the searched range are therefore

`exp(-2πT)` for `(1,0),(0,1)` and `exp(-4πT)` for `(1,1)`.

Equivariant/Wilson phases could only multiply and sum orbit terms. Here every summand already has `Pfaff_C=0`, so phases cannot revive either coefficient:

`B_1=Σ_orbits phase(C) Pfaff_C=0`, `B_2=Σ_orbits phase(C) Pfaff_C=0`.

The next **unenumerated** total bidegree is three, but it is not a candidate nonzero sector for `V=TQ`: any smooth isolated rational curve there has the same universal tangent zero modes. Singular/multiple-cover effects would require a separate treatment, but cannot be used as an assigned nonzero constant. Thus this gate supplies no additional term to the moduli-stabilization superpotential and does not alter the predecessor’s no-stationary result for the single hidden-E8 condensate.[3]

## Reproduction and controls

```text
C:/Python313/python.exe -B exact_certificate.py
C:/Python313/python.exe -B exact_certificate.py --verify
```

`exact_certificate.py` stores all orbit representatives, rank examples, exact counts, splitting data and exponent structure in `certificate.json`. Controls include the nonzero resultant, all 729 line-pair ranks, absence of rank-zero families, invertibility of every constructed graph, exact three-cycles under the quotient action, and expected negative cases for the 162 rank-one pairs.

## Sources

[1] G. Butbaia et al., *Physical Yukawa Couplings in Heterotic String Compactifications*, arXiv:2401.15078, eqs. (4.7)–(4.9), https://arxiv.org/pdf/2401.15078 . Geometry and free diagonal action.

[2] E. Witten, *Non-Perturbative Superpotentials in String Theory*, hep-th/9604030, https://arxiv.org/pdf/hep-th/9604030 . Worldsheet Pfaffian and zero-mode criterion.

[3] `../tian-yau-moduli-stabilization-gate/REPORT.md`. Retained normalization `Wws=Σ Pfaff_C exp(-2πq_CT)` and the single-condensate obstruction.
