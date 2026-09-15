# Tian–Yau standard-embedding moduli-stabilization gate

## Verdict

The most conservative primary-source mechanism compatible with the retained field content is **gaugino condensation in the untouched hidden E8**, including its one-loop Kähler-modulus threshold.[1][4] On the actual inherited overall ray `J=t(h+k)` of the Tian–Yau quotient, the required topological threshold coefficient is computable rather than assignable. The resulting leading two-field potential has **no finite stationary point anywhere in its physical domain**. Hence it has no SUSY, AdS, Minkowski, Hessian-stable, or BF-stable vacuum to classify.

A worldsheet-instanton term is a literature-established possible second effect, but its Pfaffian and curve sum have not been computed for this actual quotient/tangent bundle.[4][6] It therefore cannot be assigned a nonzero constant. Nonzero H/torsion is not used: the N=1 torsion relation makes a nonzero H background non-Kähler, changing the retained `H=0`, Kähler Calabi–Yau standard-embedding ansatz.[1][5]

This is a negative gate for the tested minimal mechanism, not a claim that the full compactification cannot be stabilized.

## 1. Retained model and allowed ingredients

The model remains the smooth free-Z3 Tian–Yau quotient `Q`, visible `V=TQ`, hidden bundle trivial, no five-brane class, `H=0`, and hidden E8 unbroken.[2][3] The Wilson-line predecessor may additionally use the visible Z3 trinification line; it does not act on hidden E8. No hidden bundle or extra condensing factor is introduced.

| ingredient | status without changing model |
|---|---|
| hidden pure-E8 gaugino condensation | allowed; primary mechanism tested |
| one-loop threshold in `f_hid` | allowed and mandatory at the same retained order |
| worldsheet instantons | allowed in principle, but actual curve/Pfaffian sum missing; coefficient not assigned |
| harmonic H or torsion | excluded from this gate because nonzero H changes the Kähler CY ansatz |
| racetrack from splitting hidden E8 | excluded: requires new hidden bundle/Wilson data |
| constant `W0` | excluded: no flux or separately established fractional Chern–Simons invariant is supplied |

The bundle-coupling lane found a 12-dimensional polynomial tangent-bundle deformation subspace and an unresolved incoming hypercohomology differential. Nothing here sets those modes, the nine complex structures, five Kähler-shape directions, or charged Higgs fields to massive values.

## 2. Explicit N=1 EFT and declared coefficients

Set reduced Planck units `M_P=1`, hold all untested fields fixed only to define the two-field slice, and use

```
S=s+iσ,  T=t+iτ,  s>0, t>0,
V_Q(t)=3 t^3,
K=-ln(S+Sbar)-3 ln(T+Tbar)+K0,
f_hid=S-γ T.
```

`K0` is the fixed complex-structure normalization. The ray intersection arithmetic is

```
∫Q (h+k)^3 = 18,              V=(1/6)18 t^3=3t^3,
c2(TQ)=3h²+hk+3k²,
∫Q c2(TQ)∧(h+k)=24.
```

The quotient factors are computed by ambient integration on the cover and division by the free degree three. In the normalization of eq. (2.23) of [1],

```
β = (1/4π) ∫Q[c2(Vvis)-c2(Vhid)]∧(h+k) = 6/π,
γ=β/2=3/π,
f_hid=S-(3/π)T.
```

This fixes the **linear topological slope on this ray**. It does not evaluate the complete physical genus-one threshold or threshold prefactor.

For pure E8, `C2(E8)=30`, `b0=3C2=90`, and the holomorphic condensate exponent is declared as

```
a=24π²/b0=8π²/C2(E8)=4π²/15,
Wgc=A exp[-a f_hid].
```

`A` is the UV matching determinant (dimension three before Planck rescaling). It is left symbolic: changing nonzero `A` rescales the potential and cannot repair the stationary-point obstruction. No value is fitted.

## 3. F terms and SUSY obstruction

Writing `W=Wgc`,

```
D_S W=-(a+1/(2s))W,
D_T W=(aγ-3/(2t))W.
```

For finite `s,t>0` and `A≠0`, `D_S W` cannot vanish. Thus there is no supersymmetric vacuum. `A=0` gives `W=0` and leaves both fields flat; it is not stabilization.

For comparison, if the threshold is dropped (`γ=0`), the condensate is independent of T and still cannot produce an isolated S–T vacuum. The threshold supplies T dependence but not a vacuum.

## 4. Exact no-stationary theorem

After minimizing the one condensate phase (which is absent from `|W|²` anyway), define

```
x=a s>0,  y=aγ t>0,
F=4x²+4x+1+(4/3)y²-4y.
```

Up to a strictly positive constant,

```
V_F = exp(-2x+2y) F/(x y³).
```

At any finite stationary point with `F≠0`, `∂x V=0` gives

```
-2-1/x+(8x+4)/F=0  =>  F=4x,
```

while `∂y V=0` gives

```
2-3/y+((8/3)y-4)/F=0  =>  F=-(4/3)y.
```

Together these require `3x+y=0`, impossible for `x,y>0`. If `F=0`, stationarity would require both `F_x=0` and `F_y=0`; the first gives `x=-1/2`, also outside the domain. Therefore the physical domain has no finite critical point. The certificate checks the topology and this elimination with exact rational arithmetic.

Consequences:

* SUSY status: no SUSY solution (`D_SW` already obstructs it).
* AdS/Minkowski/dS status: no finite vacuum of any sign.
* Hessian and BF status: inapplicable because there is no critical point. Claiming BF stability without an AdS extremum would be meaningless.
* Control: there is no candidate at `s>>1`, `V=3t³>>1`, or elsewhere. Along suitable asymptotic directions the condensate potential runs away or reaches the boundary where `Re f_hid=s-γt` ceases to be positive.

## 5. Negative controls

1. **Constant W/no-scale check.** For `W=W0`, the T sector satisfies `K^{T Tbar}K_TK_Tbar=3`, but the dilaton contributes one additional unit. Hence `V=exp(K)|W0|²`, proportional to `|W0|²/(s t³)`, and runs to zero at weak coupling/large volume. Calling the complete S–T system “no-scale” would miss the dilaton remainder.
2. **No threshold.** `β=0` leaves W independent of T and cannot isolate both moduli.
3. **No condensate.** `A=0` gives the original continuous moduli family.
4. **No topology selector.** Keeping the same `Q,TQ`, Chern classes, index, and Wilson line while scaling `J→λJ` and shifting the constant dilaton preserves the topology and leading standard-embedding equations but changes volume and `s`. This is exactly the fixed-topology/moduli-continuous comparison of the clock lane.

## 6. Conditional completion region and exact missing data

A sourced completion would add the actual worldsheet sum

```
Wws(T,z,c)=Σ_[C] Pfaff_C(z,c) exp[-2π q_C T]
```

in the displayed T normalization, with effective-curve degree `q_C>0` and Pfaffian depending on complex-structure/bundle moduli.[6] For a one-term truncation `B exp(-bT)`, `b=2πq` is quantized by the curve class; `B` is **not** free numerical input. The SUSY equations would imply, with `X=Ae^{-a(S-γT)}` and `Y=Be^{-bT}`,

```
Y=-(1+2as)X,
b(1+2as)+aγ+3as/t=0.
```

For the actual `γ=3/π>0`, `a,b,s,t>0`, the second equation is impossible. Thus even one ordinary positive-area worldsheet exponential does not yield a SUSY vacuum with this threshold sign. Multiple curve terms could evade the two-term sign reduction through phases and distinct degrees, but their existence cannot be tested until the actual sum is known.

The exact missing computable objects are:

* isolated rational curves/effective classes on `Q` along the chosen ray and their degrees `q_C`;
* each chiral Dirac Pfaffian `Pfaff_C` for `TQ|_C` and its dependence on the unresolved bundle/complex-structure coordinates;
* the homology-class sum, including Z3 quotient phases/cancellations;
* complete one-loop threshold functions (not merely the topological linear term) and the corrected Kähler metric.

No value is assigned to any of these. The known topological coefficient `∫c2∧J0=24` is not the missing Pfaffian.

## 7. Clock relation and scope

On the two-field slice, the tree visible coupling has canonical gradient `(-sqrt(2),0)` in the clock lane’s `(u,v)` basis. Thresholds and any stabilized mass matrix would rotate a mass eigenstate `e_m=(e_u,e_v,...)`; conditionally its tree UV gauge response is `-sqrt(2)e_u`, plus the uncomputed threshold derivative. Since this gate finds no vacuum, it supplies no mass eigenvector. Even a future eigenvector would give only a response coefficient: a clock drift additionally requires a cosmological/environmental solution and initial conditions. No drift is predicted.

## Reproduction

```
python -B exact_certificate.py
python -B exact_certificate.py --verify
```

No Lean theorem is included: the substantive algebra is the real-domain exponential-potential elimination above, while a kernel-only natural-number sign lemma would not formalize the physical calculus and would add no rigor.

## Sources

[1] M. Cicoli, S. de Alwis, A. Westphal, *Heterotic Moduli Stabilisation*, arXiv:1304.1809v3, https://arxiv.org/pdf/1304.1809 .

[2] G. Butbaia et al., *Physical Yukawa Couplings in Heterotic String Compactifications*, arXiv:2401.15078, https://arxiv.org/pdf/2401.15078 .

[3] P. Candelas, X. de la Ossa, Y.-H. He, B. Szendrői, *Triadophilia*, arXiv:0706.3134, https://people.maths.ox.ac.uk/szendroi/atmp_triadophilia.pdf .

[4] G. Curio, A. Krause, D. Lüst, *Moduli stabilization in the heterotic/IIB discretuum*, hep-th/0502168, https://arxiv.org/pdf/hep-th/0502168 .

[5] A. Strominger, *Superstrings with Torsion*, Nucl. Phys. B274 (1986) 253, https://doi.org/10.1016/0550-3213(86)90286-5 .

[6] E. Witten, *Non-Perturbative Superpotentials in String Theory*, hep-th/9604030, https://arxiv.org/pdf/hep-th/9604030 .
