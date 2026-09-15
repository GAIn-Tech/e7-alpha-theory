# Tian–Yau endomorphism `d3` coupling gate

## Verdict

**The requested geometric `d3` is not computed by the predecessor artifacts, and I did not replace it by a generic-maximal-rank assumption.** The exact data supplied there determine the source, target, grading, and first signed horizontal arrow, but they do not contain the Čech/Koszul representatives and two vertical contracting homotopies needed to obtain the endpoint matrix.

For the monad in cochain degrees `K^{-1}=A`, `K^0=B`, `K^1=C`, the only differential at issue is

`d3 : E3^{-2,2} -> E3^{1,0}`.

The bounded source is the 12-dimensional off-diagonal sector

`H2(Hom(Cx,Ay)) ⊕ H2(Hom(Cy,Ax))`,

with basis dual to `x_i x_j` and `y_i y_j` for `i<j`. Direct computation from `geometry.json` gives character multiplicities `(4,4,4)`. The stated polynomial target has character dimensions `(12,14,14)`.

## Fixed sign convention and actual zig-zag boundary

The total differential on `End(K)` is

`D(phi)=d_K phi - (-1)^p phi d_K`, `phi in End^p(K)`.

Thus for `phi:C->A` (`p=-2`) its first horizontal image has the two components

* `C->B : +E phi`,
* `B->A : -phi J`.

A geometric `d3` requires: represent `phi` by an actual degree-two Čech/Koszul cocycle; solve a vertical coboundary equation for this signed pair; apply the horizontal differential; solve a second vertical equation; apply the horizontal differential once more; and project the resulting `End^1=Hom(A,B)⊕Hom(B,C)` section through the exact polynomial constraint/gauge quotient. Neither a cohomology dimension nor a Serre-dual mixed quadratic supplies those two primitives.

## Why no rank is reported

Character preservation only splits the map into three blocks `4 -> 12`, `4 -> 14`, `4 -> 14`. Both the zero map and blockwise injections are compatible with all supplied dimensions and `Z3` characters. `exact_certificate.py` saves this as a negative control. Consequently, claiming rank `(4,4,4)` would be precisely the forbidden generic-maximal-rank assumption; claiming zero would be equally unsupported.

No survivor space, nullspace certificate, charged Yoneda action, or neutral `F`-term test is reported because each depends on the missing endpoint matrix. The predecessor's zero `12×9×6` tensor remains valid only on its represented polynomial subspace. No claim is made that `H1(End TX)` is exhausted.

## Needed input to close the gate

A reproducible closure needs one of:

1. an affine cover plus explicit Čech representatives and deterministic normal forms for both vertical solves, or
2. a complete graded free/Tate resolution of the threefold module together with chain maps for `E` and `J`.

The current pinned `cymyc` sources provide numerical harmonic workflows, not these algebraic chain-level data.

## Replay

```text
C:/Python313/python.exe -B exact_certificate.py
```

The receipt is immutable by default; `--create` is exclusive. This is a local exact boundary certificate, not a completed `d3` calculation.
